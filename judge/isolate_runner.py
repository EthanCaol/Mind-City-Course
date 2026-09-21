"""isolate 子进程编排：box 的建立、编译、逐测试点运行、销毁。

行为依据是 2026-09-21 在这台机器上逐条实测的结果。
几条最容易踩的，这里再点一遍：

- `--cg` 必须始终打开，且 `--init` 与 `--run` 必须一致。不一致会得到
  `status:XX` 和退出码 2。所以 `--cg` 由本模块内部统一拼装，调用方没机会漏传。
- 沙箱内环境变量被清空，编译必须显式传 `--env=PATH=...`，否则 gcc 找不到 `ld`。
- `--meta` 是**宿主侧**路径，`--stdin/--stdout/--stderr` 是 **box 内**相对路径。
- meta 和 box 内的输出文件都必须在 `--cleanup` **之前**读完。
- isolate 的退出码把「程序非 0 退出」和「被杀/超时」混在一起（都是 1），
  所以结果一律从 meta 读，不要用退出码判断。

每个子进程调用都带硬超时。没有这层保护的话，isolate 自己卡住会把整条判题队列拖死。
"""

from __future__ import annotations

import dataclasses
import logging
import os
import subprocess
import threading
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator, Sequence

from . import config
from .config import Limits

log = logging.getLogger("judge.isolate")


class IsolateError(Exception):
    """isolate 本身出了问题，不是学生的错。"""


# ---------------------------------------------------------------- meta 解析


@dataclasses.dataclass(frozen=True)
class Meta:
    """一次 `--run` 的输出信息。

    `status` 与 `exitcode` 不会同时出现：程序正常退出时没有 `status`，
    被信号杀死时没有 `exitcode`。缺失一律是 None，不要当成 0。
    """

    status: str | None = None  # RE / SG / TO / XX
    exitcode: int | None = None
    exitsig: int | None = None
    killed: bool = False
    time_s: float = 0.0  # CPU 时间
    wall_time_s: float = 0.0
    max_rss_kb: int | None = None
    cg_mem_kb: int | None = None  # 仅 --cg 模式有
    csw_voluntary: int | None = None
    csw_forced: int | None = None
    message: str | None = None
    raw: dict[str, str] = dataclasses.field(default_factory=dict)

    @property
    def ok(self) -> bool:
        """程序正常退出且退出码为 0。"""
        return self.status is None and self.exitcode == 0


def _int(value: str) -> int | None:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _float(value: str) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def parse_meta(path: Path) -> Meta:
    """读 `--meta` 写出的文件。

    **格式是 `key:value` 纯文本，不是 JSON**（isolate 2.7 没有 --meta-json）。
    """
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        raise IsolateError(f"读不到 meta 文件 {path}：{exc}") from exc

    raw: dict[str, str] = {}
    for line in text.splitlines():
        key, sep, value = line.partition(":")
        if sep:
            raw[key.strip()] = value.strip()

    killed_raw = raw.get("killed", "")
    return Meta(
        status=raw.get("status") or None,
        exitcode=_int(raw.get("exitcode", "")),
        exitsig=_int(raw.get("exitsig", "")),
        killed=killed_raw == "1",
        time_s=_float(raw.get("time", "")) or 0.0,
        wall_time_s=_float(raw.get("time-wall", "")) or 0.0,
        max_rss_kb=_int(raw.get("max-rss", "")),
        cg_mem_kb=_int(raw.get("cg-mem", "")),
        csw_voluntary=_int(raw.get("csw-voluntary", "")),
        csw_forced=_int(raw.get("csw-forced", "")),
        message=raw.get("message") or None,
        raw=raw,
    )


# ---------------------------------------------------------------- 就绪探测


def cgroup_root() -> Path | None:
    """isolate 实际使用的 cgroup 根，不可用则返回 None。

    注意 `/run/isolate/cgroup` 这个文件在 `isolate.service` 停掉之后**不会**
    跟着清理，它会留着一条已经不存在了的路径（见根目录 README 的「三个坑」②）。
    所以必须再去确认那个路径下面真的有 `cgroup.procs`。
    """
    try:
        raw = config.CGROUP_FILE.read_text(encoding="utf-8").strip()
    except OSError:
        return None

    if not raw:
        return None

    path = Path(raw)
    return path if (path / "cgroup.procs").is_file() else None


def judge_ready() -> tuple[bool, str]:
    """判题机是否可用。返回 `(是否就绪, 不可用时的说明)`。"""
    if not config.USE_CG:
        return True, ""

    if cgroup_root() is not None:
        return True, ""

    return False, (
        "判题机未就绪：isolate 的 cgroup 根不存在，`--cg` 模式用不了。\n"
        "请在有 sudo 的终端执行：sudo systemctl enable --now isolate\n"
        "（注意：服务停用后 /run/isolate/cgroup 会留着一条过期路径，"
        "所以这个提示不代表配置写错了。）"
    )


# ---------------------------------------------------------------- 单次运行


@dataclasses.dataclass
class RunOutcome:
    meta: Meta
    argv: list[str]
    isolate_rc: int
    internal_error: bool  # isolate 自身故障（status:XX / rc==2 / 子进程超时）
    diagnostics: str  # isolate 自己的 stderr，不是被测程序的
    stdout_text: str
    stderr_text: str
    duration_s: float


class Box:
    """一个沙箱实例。用 `BoxPool.acquire()` 拿，不要直接构造。"""

    def __init__(self, box_id: int, workdir: Path) -> None:
        self.box_id = box_id
        self.workdir = Path(workdir)
        self.root = config.BOX_ROOT / str(box_id)
        self.inited = False

    @property
    def box_dir(self) -> Path:
        """宿主侧看到的 box 目录。属主是调用者，往里写文件不需要 sudo。"""
        return self.root / "box"

    # ------------------------------------------------------------ 生命周期

    def init(self) -> None:
        """建 box。遇到残留先清理再重试一次。"""
        self.workdir.mkdir(parents=True, exist_ok=True)
        rc, _out, err = self._spawn(["--init"], time_s=30.0)
        if rc == 0:
            self.inited = True
            return

        # 崩溃遗留的 box 目录/ cgroup 会让 init 失败。cleanup 对不存在的 box
        # 是安全的（isolate 里有 "Nothing to do -- box did not exist"），
        # 所以无条件清一次再试。
        log.warning("box %d 首次 init 失败（rc=%d），清理后重试：%s", self.box_id, rc, err.strip())
        self._spawn(["--cleanup"], time_s=30.0)
        rc, _out, err = self._spawn(["--init"], time_s=30.0)
        if rc != 0:
            raise IsolateError(f"box {self.box_id} 初始化失败（rc={rc}）：{err.strip()}")
        self.inited = True

    def cleanup(self) -> None:
        """销毁 box。对不存在的 box 也安全，所以异常路径上可以直接调。"""
        try:
            rc, _out, err = self._spawn(["--cleanup"], time_s=30.0)
            if rc != 0 and "did not exist" not in err:
                log.warning("box %d cleanup 返回 %d：%s", self.box_id, rc, err.strip())
        except Exception:  # cleanup 失败不能让判题流程崩掉
            log.exception("box %d cleanup 异常", self.box_id)
        finally:
            self.inited = False

    # ------------------------------------------------------------ box 内文件

    def put_text(self, name: str, text: str) -> None:
        (self.box_dir / name).write_text(text, encoding="utf-8")

    def put_bytes(self, name: str, data: bytes) -> None:
        (self.box_dir / name).write_bytes(data)

    def read_text(self, name: str, max_bytes: int = 1 << 20) -> str:
        path = self.box_dir / name
        try:
            data = path.read_bytes()
        except OSError:
            return ""
        if len(data) > max_bytes:
            data = data[:max_bytes]
        return data.decode("utf-8", errors="replace")

    def remove(self, name: str) -> None:
        """删掉 box 内的文件。上一轮的 out/err 不删掉的话，
        这一轮程序没输出时会把上一轮的结果读回来。"""
        try:
            (self.box_dir / name).unlink()
        except OSError:
            pass

    # ------------------------------------------------------------ 运行

    def run(
        self,
        argv: Sequence[str],
        limits: Limits,
        *,
        stdin: str | None = None,
        stdout: str = "out.txt",
        stderr: str = "err.txt",
        env: dict[str, str] | None = None,
        meta_name: str = "run.meta",
    ) -> RunOutcome:
        """在 box 里跑一条命令，读回 meta 与 box 内的 stdout/stderr。

        输出文件在返回前就读完 —— 保证在调用方 cleanup 之前拿到。
        """
        if not self.inited:
            raise IsolateError("box 还没 init")

        # 清掉上一轮的输出，否则本轮无输出时会读到陈旧内容
        self.remove(stdout)
        self.remove(stderr)
        if stdin is not None and not (self.box_dir / stdin).is_file():
            raise IsolateError(f"box 内没有 stdin 文件 {stdin}")

        meta_path = (self.workdir / f"{meta_name}").resolve()
        meta_path.unlink(missing_ok=True)

        args: list[str] = [
            f"--time={limits.time_s}",
            f"--wall-time={limits.wall_time_s}",
            f"--extra-time={limits.extra_time_s}",
            f"--mem={limits.mem_kb}",
            f"--cg-mem={limits.cg_mem_kb}",
            f"--processes={limits.processes}",
            f"--fsize={limits.fsize_kb}",
            f"--open-files={limits.open_files}",
            f"--stack={limits.stack_kb}",
        ]
        for key, value in (env or {}).items():
            args.append(f"--env={key}={value}")
        if stdin is not None:
            args.append(f"--stdin={stdin}")
        args.append(f"--stdout={stdout}")
        args.append(f"--stderr={stderr}")
        args.append(f"--meta={meta_path}")
        args.append("--run")
        args.append("--")
        args.extend(argv)

        started = time.monotonic()
        rc, _out, diag = self._spawn(args, time_s=limits.wall_time_s + config.SUBPROCESS_SLACK_S)
        duration = time.monotonic() - started

        timed_out = rc == _TIMEOUT_RC
        try:
            meta = parse_meta(meta_path)
        except IsolateError:
            meta = Meta(message=diag.strip() or "isolate 没有写出 meta 文件")

        # status:XX 是 isolate 自身故障，绝不能算成学生的错。
        # rc==2 也是 isolate 的错误（用法错、box 不存在、cgroup 模式不匹配）。
        internal_error = timed_out or meta.status == "XX" or rc == 2

        return RunOutcome(
            meta=meta,
            argv=[config.ISOLATE_BIN, *args],
            isolate_rc=rc,
            internal_error=internal_error,
            diagnostics=diag,
            stdout_text=self.read_text(stdout) if stdout else "",
            stderr_text=self.read_text(stderr, max_bytes=64 * 1024) if stderr else "",
            duration_s=duration,
        )

    # ------------------------------------------------------------ 内部

    _TIMEOUT_RC = -9

    def _spawn(self, extra_args: Sequence[str], time_s: float) -> tuple[int, str, str]:
        """跑一次 isolate。返回 (退出码, stdout, stderr)；超时返回 -9。"""
        argv = [config.ISOLATE_BIN, "--box-id=%d" % self.box_id]
        if config.USE_CG:
            argv.append("--cg")  # init / run / cleanup 三处必须一致，只在这里拼
        argv.extend(extra_args)

        try:
            proc = subprocess.run(
                argv,
                capture_output=True,
                text=True,
                timeout=time_s,
                env=self._child_env(),
            )
        except subprocess.TimeoutExpired:
            log.error("isolate 超时（%.0fs）：%s", time_s, " ".join(argv))
            return self._TIMEOUT_RC, "", f"isolate 调用超过 {time_s:.0f} 秒未返回"
        except OSError as exc:
            raise IsolateError(f"无法启动 isolate：{exc}") from exc

        return proc.returncode, proc.stdout, proc.stderr

    @staticmethod
    def _child_env() -> dict[str, str]:
        """isolate 进程自己的环境（不是沙箱内的）。沙箱内的环境由 isolate
        清空后按 --env 重建，所以这里只需给 isolate 一个正常的环境。"""
        env = dict(os.environ)
        env.setdefault("LC_ALL", "C.UTF-8")
        return env


_TIMEOUT_RC = Box._TIMEOUT_RC


# ---------------------------------------------------------------- box 池


class BoxPool:
    """固定大小的 box 池。

    判题是串行的，所以池子通常只有一个 id。按池设计是为了将来开并发时
    只改 `config.BOX_IDS`，调用方不用动。
    """

    def __init__(self, box_ids: Sequence[int] = config.BOX_IDS, workdir: Path | None = None) -> None:
        self._ids = list(box_ids)
        self._workdir = Path(workdir or config.WORK_DIR)
        self._free = list(self._ids)
        self._lock = threading.Lock()
        self._cond = threading.Condition(self._lock)

    @contextmanager
    def acquire(self, timeout: float = 300.0) -> Iterator[Box]:
        """取出一个 box，退出时自动 cleanup 并归还。

        cleanup 放在 finally 里 —— box 泄漏（init 了没 cleanup）久了，
        box 目录和 box cgroup 都会堆积，这是最容易漏的一条。
        """
        box_id = self._take(timeout)
        box = Box(box_id, self._workdir / str(box_id))
        try:
            yield box
        finally:
            box.cleanup()
            self._give_back(box_id)

    def _take(self, timeout: float) -> int:
        deadline = time.monotonic() + timeout
        with self._cond:
            while not self._free:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise IsolateError("等不到空闲的 box")
                self._cond.wait(remaining)
            return self._free.pop()

    def _give_back(self, box_id: int) -> None:
        with self._cond:
            self._free.append(box_id)
            self._cond.notify()

    def reclaim_all(self) -> list[int]:
        """对所有 box id 无条件 cleanup 一次，回收上次崩溃留下的残骸。

        `--cleanup` 对不存在的 box 是安全的，所以可以无脑调用。
        服务启动时跑一次，避免残留的 box 目录/ cgroup 让后续 init 失败。
        """
        reclaimed: list[int] = []
        for box_id in self._ids:
            box = Box(box_id, self._workdir / str(box_id))
            box.cleanup()
            reclaimed.append(box_id)
        return reclaimed
