"""把 isolate 的 meta 映射成判题结论。

isolate 本身没有 AC/WA/TLE/MLE 这些概念，只有 `status`（RE/SG/TO/XX）、
`exitcode`、`exitsig` 和一堆计量值。映射规则见下面这张表。

两条不能搞错的：

- **`status:XX` 是 isolate 自身故障**，必须报成系统错误并告警，绝不能算成学生的错。
- **MLE 没有直接字段**，只能靠 `cg-mem` 接近上限来推断。这也是运行参数里
  `--mem` 取 `--cg-mem` 两倍的原因：两者同值时 `RLIMIT_AS` 必然先触发，
  `cg-mem` 永远达不到阈值，MLE 会被误判成 RE。
"""

from __future__ import annotations

import dataclasses
import signal

from . import config
from .compare import CompareResult, compare
from .config import Limits
from .isolate_runner import Meta, RunOutcome

AC = "AC"  # 通过
WA = "WA"  # 输出不符
TLE = "TLE"  # 超时
MLE = "MLE"  # 内存超限
RE = "RE"  # 运行错误
CE = "CE"  # 编译错误
OLE = "OLE"  # 输出超限
SYSTEM = "SYSTEM"  # 判题机故障，不是学生的错

ALL_VERDICTS = (AC, WA, TLE, MLE, RE, CE, OLE, SYSTEM)

# 给前端显示的中文名
LABELS = {
    AC: "通过",
    WA: "答案错误",
    TLE: "运行超时",
    MLE: "内存超限",
    RE: "运行错误",
    CE: "编译错误",
    OLE: "输出超限",
    SYSTEM: "判题机故障",
}

SIGXFSZ = 25  # 写文件超过 --fsize 时收到的信号


def signal_name(number: int | None) -> str:
    if number is None:
        return ""
    try:
        return signal.Signals(number).name
    except ValueError:
        return f"信号 {number}"


@dataclasses.dataclass(frozen=True)
class VerdictResult:
    verdict: str
    reason: str = ""  # 给学生看的一句话
    compare: CompareResult | None = None

    @property
    def label(self) -> str:
        return LABELS.get(self.verdict, self.verdict)


# ---------------------------------------------------------------- 编译


def judge_compile(outcome: RunOutcome) -> tuple[str, str]:
    """返回 `(结论, 给学生的说明)`。结论是 AC 表示编译通过。

    编译失败时 gcc 走的是**非 0 退出码**而不是 `status` —— 这是最容易漏的一条：
    `status` 只在被信号杀 / 超时 / isolate 内部错误时出现。
    """
    if outcome.internal_error:
        detail = outcome.meta.message or outcome.diagnostics.strip() or "未知原因"
        return SYSTEM, f"判题机故障（编译阶段）：{detail}"

    meta = outcome.meta

    if meta.status == "TO":
        return CE, (
            "编译超时。检查一下有没有超大数组、递归展开的宏，"
            "或者 `#include` 了很大的文件。"
        )

    if meta.status in ("SG", "RE"):
        if meta.status == "SG":
            return CE, f"编译器被信号终止（{signal_name(meta.exitsig)}）。"
        return CE, f"编译器异常退出（退出码 {meta.exitcode}）。"

    if meta.exitcode not in (0, None):
        return CE, f"编译失败（gcc 退出码 {meta.exitcode}）。"

    if meta.status is not None:
        return CE, f"编译未能正常完成（status={meta.status}）。"

    return AC, ""


# ---------------------------------------------------------------- 运行


def judge_run(outcome: RunOutcome, expected: str, limits: Limits) -> VerdictResult:
    """判一个测试点。判定顺序是先状态、后比对 —— 超时和被杀优先于输出比对。"""
    if outcome.internal_error:
        detail = outcome.meta.message or outcome.diagnostics.strip() or "未知原因"
        return VerdictResult(SYSTEM, f"判题机故障：{detail}")

    meta = outcome.meta

    if meta.status == "TO":
        if meta.time_s >= 0.9 * limits.time_s:
            return VerdictResult(TLE, f"CPU 时间超过 {limits.time_s} 秒")
        return VerdictResult(TLE, f"运行时间超过 {limits.wall_time_s} 秒")

    # 写文件（含 stdout）超过 --fsize 会得到 SIGXFSZ。这多半是输出太多，
    # 所以报「输出超限」比笼统的「运行错误」有用得多。
    if meta.exitsig == SIGXFSZ:
        return VerdictResult(
            OLE,
            f"输出超过 {limits.fsize_kb} KB 上限。检查一下是不是有死循环在疯狂打印。",
        )

    killed_or_crashed = meta.killed or meta.status in ("SG", "RE")

    # MLE：cg-mem 接近上限（cgroup 杀的），或者 rlimit 口径的峰值内存也接近上限
    if killed_or_crashed:
        cg_mem = meta.cg_mem_kb or 0
        if cg_mem >= config.MLE_CGMEM_RATIO * limits.cg_mem_kb:
            return VerdictResult(
                MLE, f"内存使用达到 {limits.cg_mem_kb // 1024} MB 上限"
            )
        max_rss = meta.max_rss_kb or 0
        if max_rss >= config.MLE_MAXRSS_RATIO * limits.cg_mem_kb:
            return VerdictResult(
                MLE, f"内存使用接近 {limits.cg_mem_kb // 1024} MB 上限"
            )

    if meta.status == "SG" or meta.exitsig is not None:
        name = signal_name(meta.exitsig)
        hint = {
            "SIGSEGV": "多半是数组越界、用了空指针，或者 scanf 漏了 `&`",
            "SIGFPE": "多半是整数除以 0",
            "SIGABRT": "程序自己中止了（abort 或断言失败）",
            "SIGBUS": "多半是内存访问越界",
            "SIGKILL": "进程被强制杀掉，通常是内存超限",
        }.get(name, "")
        reason = f"程序异常终止（{name}）"
        return VerdictResult(RE, f"{reason}。{hint}" if hint else reason)

    if meta.status == "RE":
        return VerdictResult(RE, f"程序以非 0 状态退出（退出码 {meta.exitcode}）")

    if meta.exitcode not in (0, None):
        return VerdictResult(RE, f"程序退出码是 {meta.exitcode}，不是 0")

    if meta.status is not None:
        return VerdictResult(RE, f"程序未能正常完成（status={meta.status}）")

    # 到这里说明程序正常退出且退出码为 0，可以比对输出了
    result = compare(outcome.stdout_text, expected)
    if result.matched:
        return VerdictResult(AC, "", compare=result)
    return VerdictResult(WA, result.summary, compare=result)
