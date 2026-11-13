"""期中考试的批改材料。

材料由 Syncthing 同步到 `docs/midterm-score/期中考卷批改/`，被 `.gitignore` 和
`mkdocs.yml` 的 `exclude_docs` 挡在仓库和站点之外，只有这个服务读它们。

一个学生一个目录 `学号-姓名/`，里面按文件名约定放：

    学号-姓名.jpg                      答卷照片（也可能带 -第一题 / -背面 后缀）
    学号-姓名-第一题.c                  转录的代码
    学号-姓名-第一题-代码评议.md
    学号-姓名-第一题-代码评分.md

题号从 `.c` 文件反推，不写死两题。评议和评分是写给人看的表格，直接渲染成 HTML
交给前端；代码给原文，前端自己做高亮。

照片不按题分：一张卷子的正反面通常同时拍进了两道题，所以整份材料只有一组照片，
放在所有题目前面显示。
"""

from __future__ import annotations

import logging
import re
from pathlib import Path

import markdown

from . import config

log = logging.getLogger("judge.midterm")

NUMERALS = "一二三四五六七八九十"

QUESTION_RE = re.compile(r"-第([一二三四五六七八九十]+)题\.c$")


def _folder(student_id: str) -> Path | None:
    matches = sorted(config.MIDTERM_DIR.glob(f"{student_id}-*"))
    return matches[0] if matches and matches[0].is_dir() else None


def _render(path: Path) -> str:
    """评议/评分文件转 HTML。首行的 H1 去掉 —— 页面上已经有一级标题了。"""
    if not path.is_file():
        return ""
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    if lines and lines[0].startswith("# "):
        text = "\n".join(lines[1:])
    return markdown.markdown(text, extensions=["tables"])


def _photos(folder: Path) -> list[Path]:
    """这个学生的全部答卷照片，按文件名排序。

    名字有两种：`学号-姓名.jpg`（整页拍一张）和 `学号-姓名-第一题.jpg` /
    `-背面.jpg`（分页拍），都算同一份材料。
    """
    return sorted(folder.glob(f"{folder.name}*.jpg"))


def load(student_id: str) -> dict | None:
    """一个学生的全部材料。没有这个人的目录返回 None。"""
    folder = _folder(student_id)
    if folder is None:
        return None

    prefix = folder.name + "-"
    questions = []
    for code_path in sorted(folder.glob(f"{prefix}第*题.c")):
        match = QUESTION_RE.search(code_path.name)
        if match is None:
            continue
        label = match.group(1)
        base = code_path.name[: -len(".c")]
        questions.append(
            {
                "no": label,
                "code": code_path.read_text(encoding="utf-8"),
                "review": _render(folder / f"{base}-代码评议.md"),
                "score": _render(folder / f"{base}-代码评分.md"),
            }
        )

    # 第一题在前、第二题在后。目前只有单个数码，按字符位置排就够。
    questions.sort(key=lambda q: NUMERALS.find(q["no"][0]))

    return {
        "student_id": student_id,
        "name": folder.name.split("-", 1)[1],
        "photo_count": len(_photos(folder)),
        "questions": questions,
    }


def photo(student_id: str, i: int) -> bytes | None:
    """第 i 张照片。索引越界返回 None。

    按索引取而不是按文件名取，前端就没法借这个接口读目录里的任意文件。
    """
    folder = _folder(student_id)
    if folder is None:
        return None

    photos = _photos(folder)
    if not 0 <= i < len(photos):
        return None
    return photos[i].read_bytes()
