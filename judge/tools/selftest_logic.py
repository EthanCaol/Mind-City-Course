#!/usr/bin/env python3
"""纯逻辑自测：identity / compare / roster / problem。

不碰 isolate、不需要 sudo、不改任何状态，随时可以跑：

    python3 judge/tools/selftest_logic.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from judge import config  # noqa: E402
from judge.compare import compare, normalize  # noqa: E402
from judge.identity import extract_student_id  # noqa: E402
from judge.problem import list_problems, load_problem  # noqa: E402
from judge.roster import Roster  # noqa: E402

SID = "26803070224"

_failures: list[str] = []
_passed = 0


def check(label: str, got, want) -> None:
    global _passed
    if got == want:
        _passed += 1
    else:
        _failures.append(f"{label}\n    期望: {want!r}\n    实际: {got!r}")


# ---------------------------------------------------------------- 学号解析

def test_identity() -> None:
    body = "int main(){return 0;}\n"
    cases = [
        # (说明, 源码, 期望学号 或 None)
        ("标准写法", f"// {SID}\n{body}", SID),
        ("多个空格", f"//     {SID}     \n{body}", SID),
        ("无空格", f"//{SID}\n{body}", SID),
        ("前面有空行", f"\n\n// {SID}\n{body}", SID),
        ("CRLF 行尾", f"// {SID}\r\nint main(){{return 0;}}\r\n", SID),
        # 取不到就返回 None
        ("第一行是代码", body, None),
        ("学号在第二行", f"#include <stdio.h>\n// {SID}\n{body}", None),
        ("空文件", "", None),
    ]

    for label, src, want in cases:
        check(f"学号解析 · {label}", extract_student_id(src), want)


# ---------------------------------------------------------------- 输出比对

def test_compare() -> None:
    # 这些写法上的差异都不该判错
    check("比对 · 完全相同", compare("8\n", "8\n").matched, True)
    check("比对 · 末尾少换行", compare("8", "8\n").matched, True)
    check("比对 · 末尾多换行", compare("8\n\n\n", "8\n").matched, True)
    check("比对 · 行末空格", compare("8   \n", "8\n").matched, True)
    check("比对 · 行末制表符", compare("8\t\n", "8\n").matched, True)
    check("比对 · 行末全角空格", compare("8　\n", "8\n").matched, True)
    check("比对 · Windows 换行", compare("8\r\n", "8\n").matched, True)
    check("比对 · 裸 CR", compare("8\r9\r", "8\n9\n").matched, True)
    check("比对 · 多行", compare("3 5\n8\n", "3 5\n8\n").matched, True)

    # 这些是真不同
    check("比对 · 数值不同", compare("9\n", "8\n").matched, False)
    check("比对 · 少输出一行", compare("8\n", "3 5\n8\n").matched, False)
    check("比对 · 多输出一行", compare("3 5\n8\n", "8\n").matched, False)
    check("比对 · 行首缩进算不同", compare("  8\n", "8\n").matched, False)
    check("比对 · 大小写算不同", compare("abc\n", "ABC\n").matched, False)

    # 差异提示要能直接念给学生听
    d = compare("-5\n", "5\n").diff
    check("比对 · 差异行号", d.line, 1)
    check("比对 · 差异内容", (d.expected, d.actual), ("5", "-5"))
    check("比对 · 差异提示", d.describe(), "第 1 行：期望 `5`，你输出的是 `-5`")
    check(
        "比对 · 缺行提示",
        compare("8\n", "8\n9\n").diff.describe(),
        "第 2 行：期望 `9`，你没有输出这一行",
    )
    check(
        "比对 · 多行提示",
        compare("8\n9\n", "8\n").diff.describe(),
        "第 2 行：多输出了 `9`",
    )

    # 归一化
    check("归一化 · 丢末尾空行", normalize("a\nb\n\n\n"), ["a", "b"])
    check("归一化 · 空输出", normalize(""), [])
    check("归一化 · 只有换行", normalize("\n\n"), [])


# ---------------------------------------------------------------- 花名册

def test_roster() -> None:
    ro = Roster(config.ROSTER_PATH)
    check("花名册 · 人数", ro.reload(), 74)
    check("花名册 · 能查到", ro.lookup("26113050003"), "曹奕伦")
    check("花名册 · 间隔号姓名", ro.lookup("26300980016"), "伊木然·阿合买提江")
    check("花名册 · 查不到", ro.lookup("99999999999"), None)
    check("花名册 · 教师已剔除", ro.lookup("04356"), None)


# ---------------------------------------------------------------- 题目

def test_problem() -> None:
    prob = load_problem("作业1")
    check("题目 · 测试点数", prob.total_cases, 5)
    check("题目 · 第一组输入", prob.cases[0].stdin, "3 5\n")
    check("题目 · 第一组期望", prob.cases[0].expected, "8\n")
    check("题目 · 索引从 1 开始", [c.index for c in prob.cases], [1, 2, 3, 4, 5])
    check("题目 · 都还没隐藏", all(not c.hidden for c in prob.cases), True)
    check("题目 · 编译参数", "-std=gnu23" in prob.compile_flags, True)
    check("题目 · 运行内存倍于 cg-mem", prob.run_limits.mem_kb, 2 * prob.run_limits.cg_mem_kb)
    check("题目 · 题目列表", [p.slug for p in list_problems()], ["作业1"])


# ---------------------------------------------------------------- main

def main() -> int:
    for fn in (test_identity, test_compare, test_roster, test_problem):
        fn()

    print(f"通过 {_passed} 项")
    if _failures:
        print(f"\n失败 {len(_failures)} 项：\n")
        for f in _failures:
            print(f"  · {f}\n")
        return 1
    print("全部通过")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
