"""输出比对。

归一化不能省：Windows 上编辑过的文件带 `\\r\\n`、编辑器自动补末尾换行、
行末多敲了空格 —— 不处理就会出现「学生答案明明对却被判错」。
"""

from __future__ import annotations

import dataclasses


@dataclasses.dataclass(frozen=True)
class Diff:
    """首个差异。某一侧没有该行时为 None。"""

    line: int  # 1-based
    expected: str | None
    actual: str | None

    def describe(self) -> str:
        if self.actual is None:
            return f"第 {self.line} 行：期望 `{self.expected}`，你没有输出这一行"
        if self.expected is None:
            return f"第 {self.line} 行：多输出了 `{self.actual}`"
        return f"第 {self.line} 行：期望 `{self.expected}`，你输出的是 `{self.actual}`"


@dataclasses.dataclass(frozen=True)
class CompareResult:
    matched: bool
    diff: Diff | None = None

    @property
    def summary(self) -> str:
        if self.matched:
            return "输出与期望一致"
        return self.diff.describe() if self.diff else "输出与期望不一致"


def decode(data: bytes) -> str:
    """学生程序输出可能不是 UTF-8（比如 GBK 中文）。解不出就用替代字符，
    结果是 WA，但不能因此抛异常。"""
    return data.decode("utf-8", errors="replace")


def normalize(text: str) -> list[str]:
    """统一换行、剥掉每行行末空白、丢掉末尾空行。"""
    text = text.lstrip("﻿").replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip(" \t　") for line in text.split("\n")]
    while lines and lines[-1] == "":
        lines.pop()
    return lines


def compare(actual: str, expected: str) -> CompareResult:
    act = normalize(actual)
    exp = normalize(expected)

    if act == exp:
        return CompareResult(matched=True)

    for i in range(max(len(act), len(exp))):
        a = act[i] if i < len(act) else None
        e = exp[i] if i < len(exp) else None
        if a != e:
            return CompareResult(matched=False, diff=Diff(line=i + 1, expected=e, actual=a))

    return CompareResult(matched=False)
