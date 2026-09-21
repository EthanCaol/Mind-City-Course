"""从学生源码第一行取学号。

第一行写成 `// 26803070224`：注释符之后的全部内容去掉前后空格，必须正好是
11 位数字。取不到返回 None，由调用方决定怎么提示学生。
"""

from __future__ import annotations

import re

COMMENT_PREFIX = "//"
STUDENT_ID_RE = re.compile(r"[0-9]{11}")

FORMAT_HINT = "请在代码第一行写上你的学号，格式：// 26803070224"


def extract_student_id(source: str) -> str | None:
    first_line = source.strip().split("\n", 1)[0].strip()
    if not first_line.startswith(COMMENT_PREFIX):
        return None

    body = first_line[len(COMMENT_PREFIX) :].strip()
    return body if STUDENT_ID_RE.fullmatch(body) else None
