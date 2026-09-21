"""题目与测试点的加载。

目录约定：

    problems/<题目 slug>/
        problem.json
        cases/public/01.in  01.out  02.in  02.out ...

测试点从 `cases/public/` 自动发现，按文件名排序。`visibility` 目前一律是
"public"（学生要能看见输入输出），但数据结构从第一天就带上它 —— 将来要加
隐藏测试点，只需要把文件放到 `cases/hidden/` 并改这里的发现逻辑，
数据库和前端协议都不用动。
"""

from __future__ import annotations

import dataclasses
import json
import logging
from pathlib import Path

from . import config
from .config import Limits

log = logging.getLogger("judge.problem")

PUBLIC = "public"
HIDDEN = "hidden"

# 测试点文本的大小上限。防止误放一个几百 MB 的文件把判题拖死。
MAX_CASE_BYTES = 1 << 20


class ProblemError(Exception):
    pass


@dataclasses.dataclass(frozen=True)
class TestCase:
    index: int  # 1-based，与数据库里的 case_index 对应
    stdin: str
    expected: str
    visibility: str = PUBLIC

    @property
    def hidden(self) -> bool:
        return self.visibility == HIDDEN


@dataclasses.dataclass(frozen=True)
class Problem:
    slug: str
    title: str
    compile_flags: tuple[str, ...]
    compile_limits: Limits
    run_limits: Limits
    cases: tuple[TestCase, ...]

    @property
    def total_cases(self) -> int:
        return len(self.cases)


@dataclasses.dataclass(frozen=True)
class ProblemSummary:
    """列表页用的轻量信息，不含测试点内容。"""

    slug: str
    title: str
    total_cases: int


def _limits_from(base: Limits, override: dict | None) -> Limits:
    """用 problem.json 里的字段覆盖默认限制。未知字段直接报错而不是静默忽略。"""
    if not override:
        return base
    known = {f.name for f in dataclasses.fields(Limits)}
    unknown = set(override) - known
    if unknown:
        raise ProblemError(f"problem.json 里有无法识别的限制字段：{sorted(unknown)}")
    return dataclasses.replace(base, **override)


def _read_case(path: Path) -> str:
    size = path.stat().st_size
    if size > MAX_CASE_BYTES:
        raise ProblemError(f"测试点文件过大（{size} 字节）：{path}")
    return path.read_text(encoding="utf-8-sig")


def _discover_cases(problem_dir: Path) -> list[TestCase]:
    cases: list[TestCase] = []
    index = 0

    for visibility, subdir in ((PUBLIC, "public"), (HIDDEN, "hidden")):
        case_dir = problem_dir / "cases" / subdir
        if not case_dir.is_dir():
            continue
        for in_path in sorted(case_dir.glob("*.in")):
            out_path = in_path.with_suffix(".out")
            if not out_path.is_file():
                raise ProblemError(f"测试点 {in_path.name} 缺少对应的 .out 文件")
            index += 1
            cases.append(
                TestCase(
                    index=index,
                    stdin=_read_case(in_path),
                    expected=_read_case(out_path),
                    visibility=visibility,
                )
            )

    if not cases:
        raise ProblemError(f"{problem_dir} 下没有任何测试点（cases/public/*.in）")
    return cases


def load_problem(slug: str) -> Problem:
    problem_dir = config.PROBLEMS_DIR / slug
    meta_path = problem_dir / "problem.json"
    if not meta_path.is_file():
        raise ProblemError(f"题目不存在：{slug}（找不到 {meta_path}）")

    try:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ProblemError(f"{meta_path} 不是合法 JSON：{exc}") from exc

    compile_limits = _limits_from(config.COMPILE_LIMITS, meta.get("compile_limits"))
    run_limits = _limits_from(config.RUN_LIMITS, meta.get("run_limits"))
    flags = tuple(meta.get("compile_flags", ("-O2", "-std=gnu23", "-Wall", "-DONLINE_JUDGE")))

    return Problem(
        slug=slug,
        title=meta.get("title", slug),
        compile_flags=flags,
        compile_limits=compile_limits,
        run_limits=run_limits,
        cases=tuple(_discover_cases(problem_dir)),
    )


def list_problems() -> list[ProblemSummary]:
    out: list[ProblemSummary] = []
    if not config.PROBLEMS_DIR.is_dir():
        return out
    for entry in sorted(config.PROBLEMS_DIR.iterdir()):
        if not (entry / "problem.json").is_file():
            continue
        try:
            prob = load_problem(entry.name)
        except ProblemError as exc:
            log.warning("跳过加载失败的题目 %s：%s", entry.name, exc)
            continue
        out.append(
            ProblemSummary(slug=prob.slug, title=prob.title, total_cases=prob.total_cases)
        )
    return out
