"""花名册的读取、缓存与匹配。

花名册是 `data/roster.csv`（两列：学号,姓名），由助教维护、判题服务**只读**。
权威副本在 COS 上（桶根的 `roster.csv`，对象设成私有），因为里面有学生姓名学号
—— 本仓库是 public 的，绝不能放进来。

服务启动时从 COS 拉到新版本后调 `reload()`。加载失败时**保留旧数据**：
花名册拉不到不该让判题停摆，宁可继续用上一次的副本。
"""

from __future__ import annotations

import csv
import io
import logging
import subprocess
import threading
import time
from pathlib import Path

from . import config

log = logging.getLogger("judge.roster")

EXPECTED_HEADER = ("学号", "姓名")


class RosterError(Exception):
    pass


class Roster:
    """线程安全的花名册。判题 worker 和 HTTP 线程都会读，push 线程会写。

    **文件里的行序会被保留**（`_by_id` 按文件顺序插入），「作业完成情况」页
    直接用这个顺序显示。所以名单的排序是在 CSV 里定的，不在代码里：
    助教在前，其余按姓名拼音。想改顺序就改 CSV。
    """

    def __init__(self, path: Path) -> None:
        self.path = Path(path)
        self._lock = threading.RLock()
        self._by_id: dict[str, str] = {}
        self._loaded_at: float | None = None

    # ------------------------------------------------------------ 加载

    def reload(self) -> int:
        """重新读盘。返回条目数。失败会抛 RosterError，调用方决定要不要吞。"""
        text = self.path.read_text(encoding="utf-8-sig")
        rows = list(csv.reader(io.StringIO(text)))

        if not rows:
            raise RosterError(f"花名册是空的：{self.path}")

        header = tuple(cell.strip() for cell in rows[0])
        if header[:2] != EXPECTED_HEADER:
            raise RosterError(
                f"花名册表头不对：期望 {EXPECTED_HEADER}，实际 {header[:2]}。"
                f"文件：{self.path}"
            )

        by_id: dict[str, str] = {}
        for lineno, row in enumerate(rows[1:], start=2):
            if not row or not row[0].strip():
                continue  # 容忍空行
            if len(row) < 2 or not row[1].strip():
                raise RosterError(f"花名册第 {lineno} 行缺少姓名：{row!r}")

            sid, name = row[0].strip(), row[1].strip()
            if not (len(sid) == 11 and sid.isdigit()):
                raise RosterError(
                    f"花名册第 {lineno} 行的学号不是 11 位数字：{sid!r}"
                )
            if sid in by_id:
                raise RosterError(f"花名册第 {lineno} 行学号重复：{sid}")
            by_id[sid] = name

        with self._lock:
            self._by_id = by_id
            self._loaded_at = time.time()

        log.info("花名册已加载：%d 人（%s）", len(by_id), self.path)
        return len(by_id)

    def reload_or_keep(self) -> bool:
        """加载失败时保留旧数据并记日志。返回是否刷新成功。"""
        try:
            self.reload()
            return True
        except (OSError, RosterError) as exc:
            log.warning("花名册加载失败，继续用上一次的副本：%s", exc)
            return False

    # ------------------------------------------------------------ 查询

    def lookup(self, student_id: str) -> str | None:
        """按学号取姓名。不在名单里返回 None。"""
        with self._lock:
            return self._by_id.get(student_id)

    def contains(self, student_id: str) -> bool:
        return self.lookup(student_id) is not None

    def all(self) -> dict[str, str]:
        with self._lock:
            return dict(self._by_id)

    def __len__(self) -> int:
        with self._lock:
            return len(self._by_id)

    @property
    def loaded_at(self) -> float | None:
        with self._lock:
            return self._loaded_at


def pull_from_cos(roster: Roster) -> bool:
    """从 COS 拉一份花名册覆盖本地，再重新加载。返回是否更新成功。

    拉不到（对象不存在、网络不通、超时）就继续用本地那份 —— 名单拉不到不该让判题停摆。
    先下到临时文件再原子替换：中途断线会留下半截文件，而这份名单是权威的，
    半截名单会让服务按错误的名单判分。

    服务启动时在一个独立线程里调它，网络慢也不至于拖住启动。
    """
    tmp = roster.path.with_name(roster.path.name + ".tmp")
    try:
        done = subprocess.run(
            [config.COS_BIN, "-b", config.COS_BACKUP_BUCKET, "download", "-f",
             config.COS_ROSTER_KEY, str(tmp)],
            capture_output=True, text=True, timeout=config.COS_TIMEOUT_S,
        )
    except subprocess.TimeoutExpired:
        log.warning("从 COS 拉花名册超时，继续用本地那份")
        return False

    if done.returncode != 0 or not tmp.exists():
        log.warning("从 COS 拉花名册失败，继续用本地那份：%s",
                    (done.stderr or done.stdout).strip()[:200])
        tmp.unlink(missing_ok=True)
        return False

    tmp.replace(roster.path)
    log.info("花名册已从 COS 更新")
    return roster.reload_or_keep()
