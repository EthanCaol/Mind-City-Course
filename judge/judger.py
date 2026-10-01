"""判一份提交：在同一个 box 里编译一次，然后逐测试点运行。

编译和运行共用同一个 box、同一套 `--cg`，因为学生代码在**编译期**也能作恶
（超大全局数组、递归展开的宏、`#include` 巨型文件）。
"""

from __future__ import annotations

import dataclasses
import logging

from . import verdict as V
from .config import SANDBOX_PATH
from .isolate_runner import Box, RunOutcome
from .problem import Problem, TestCase
from .verdict import judge_compile, judge_run

log = logging.getLogger("judge.judger")

SOURCE = "main.c"
BINARY = "main"
IN = "in.txt"
OUT = "out.txt"
ERR = "err.txt"


@dataclasses.dataclass
class CaseOutcome:
    index: int
    verdict: str
    reason: str
    time_s: float
    memory_kb: int
    actual: str


@dataclasses.dataclass
class JudgeOutcome:
    verdict: str
    passed: int
    total: int
    cases: list[CaseOutcome] = dataclasses.field(default_factory=list)
    compile_error: str = ""

    @property
    def worst_time_s(self) -> float:
        return max((c.time_s for c in self.cases), default=0.0)

    @property
    def worst_mem_kb(self) -> int:
        return max((c.memory_kb for c in self.cases), default=0)


def _compile(box: Box, problem: Problem) -> JudgeOutcome | None:
    """编译。返回 None 表示通过，否则返回已经能收尾的结果（CE 或 SYSTEM）。

    源码由调用方提前写进 box（`judge_submission` 负责）。
    """
    argv = ["/usr/bin/gcc", *problem.compile_flags, "-o", BINARY, SOURCE]
    run = box.run(
        argv,
        problem.compile_limits,
        env={"PATH": SANDBOX_PATH},
        stdout="compile.out",
        stderr="compile.err",
        meta_name="compile.meta",
    )

    result, message = judge_compile(run)
    if result == V.AC:
        return None

    if result == V.SYSTEM:
        log.error("编译阶段判题机故障：%s\n%s", message, run.diagnostics)
        return JudgeOutcome(verdict=V.SYSTEM, passed=0, total=0, compile_error=message)

    # CE：把 gcc 的 stderr 原文交给学生，那是他唯一能照着改的东西
    return JudgeOutcome(
        verdict=V.CE,
        passed=0,
        total=0,
        compile_error=run.stderr_text.strip() or message,
    )


def _run_case(box: Box, case: TestCase, problem: Problem) -> CaseOutcome:
    box.put_text(IN, case.stdin)
    run: RunOutcome = box.run(
        [f"./{BINARY}"],
        problem.run_limits,
        stdin=IN,
        stdout=OUT,
        stderr=ERR,
        meta_name=f"case{case.index}.meta",
    )

    result = judge_run(run, case.expected, problem.run_limits)
    return CaseOutcome(
        index=case.index,
        verdict=result.verdict,
        reason=result.reason,
        time_s=run.meta.time_s,
        memory_kb=run.meta.cg_mem_kb or run.meta.max_rss_kb or 0,
        actual=run.stdout_text,
    )


def _overall(cases: list[CaseOutcome]) -> str:
    """整份提交的结论。

    有一个测试点撞上判题机故障就整份报 SYSTEM —— 不能因为机器的问题给学生记个 WA。
    """
    if any(c.verdict == V.SYSTEM for c in cases):
        return V.SYSTEM
    for case in cases:
        if case.verdict != V.AC:
            return case.verdict
    return V.AC


def judge_submission(box: Box, source: str, problem: Problem) -> JudgeOutcome:
    """判一份提交。box 由调用方通过 `BoxPool.acquire()` 提供，生命周期也由它管。"""
    box.put_text(SOURCE, source)

    failed = _compile(box, problem)
    if failed is not None:
        return failed

    cases = [_run_case(box, case, problem) for case in problem.cases]
    passed = sum(1 for c in cases if c.verdict == V.AC)

    return JudgeOutcome(
        verdict=_overall(cases),
        passed=passed,
        total=len(cases),
        cases=cases,
    )
