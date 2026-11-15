"""期中考试的批改材料。

材料由 Syncthing 同步到 `docs/midterm-score/期中考卷批改/`，被 `.gitignore` 和
`mkdocs.yml` 的 `exclude_docs` 挡在仓库和站点之外，只有这个服务读它们。

一个学生一个目录 `学号-姓名/`，里面按文件名约定放：

    学号-姓名-编程题.jpg / -编程题-1.jpg  编程题答卷照片，多页时按页码编号
    学号-姓名-改错题.jpg                改错题照片，同一页上还有完全程序题的答案
    学号-姓名.txt                       本次考试的六项得分与总分
    学号-姓名-第一题.c                  转录的代码
    学号-姓名-第一题-代码评议.md
    学号-姓名-第一题-代码评分.md

题号从 `.c` 文件反推，不写死两题。评议和评分是写给人看的表格，直接渲染成 HTML
交给前端；代码给原文，前端自己做高亮。

照片分两组：改错题一张（上面写着完全程序题的答案），编程题一页到三页。
编程题照片还被两道题共用，所以放在题目列表前面。
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

# 评分表最后一行：| 合计 | 满分 | 扣分 | 得分 | |
TOTAL_RE = re.compile(r"\|\s*合计\s*\|\s*([0-9.]+)\s*\|[^|]*\|\s*([0-9.]+)\s*\|")

# 试卷各部分的满分。编程题是两小问之和。
SECTIONS = (
    ("一", "单选题", 20),
    ("二", "程序阅读题", 20),
    ("三", "改错题", 10),
    ("四", "完全程序题", 21),
    ("五", "编程题", 29),
)

# 登分记录里的一行：[一]单选题 12.5
SCORE_RE = re.compile(r"^\[([一二三四五])\]([^\s]+)\s+([0-9.]+)$")
TOTAL_SCORE_RE = re.compile(r"^总分\s+([0-9.]+)$")


def _folder(student_id: str) -> Path | None:
    matches = sorted(config.MIDTERM_DIR.glob(f"{student_id}-*"))
    return matches[0] if matches and matches[0].is_dir() else None


def _render(path: Path) -> str:
    """评议/评分文件转 HTML。首行的 H1 去掉 —— 页面上已经有一级标题了。

    `nl2br` 不能省：这些文件一行写一条说明，靠换行分隔，Markdown 默认会把
    相邻的几行并成一段，页面上就挤成一条长句。
    """
    if not path.is_file():
        return ""
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    if lines and lines[0].startswith("# "):
        text = "\n".join(lines[1:])
    return markdown.markdown(text, extensions=["tables", "nl2br"])


def _total(path: Path) -> dict | None:
    """评分表合计行的「满分 / 得分」。表里没有这一行就返回 None。"""
    if not path.is_file():
        return None
    match = TOTAL_RE.search(path.read_text(encoding="utf-8"))
    if match is None:
        return None
    return {"full": float(match.group(1)), "got": float(match.group(2))}


def _photos(folder: Path) -> list[tuple[str, Path]]:
    """这个学生的全部答卷照片，改错题在前、编程题在后。

    改错题那张通常同时写着完全程序题的答案，所以归到改错题这一组。
    """
    prefix = folder.name
    correction = sorted(folder.glob(f"{prefix}-改错题*.jpg"))
    programming = sorted(folder.glob(f"{prefix}-编程题*.jpg"))
    return [("correction", p) for p in correction] + [
        ("programming", p) for p in programming
    ]


def _scores(folder: Path) -> dict:
    """登分记录（`学号-姓名.txt`）里的各部分得分与总分。

    客观题与改错题由另一套流程判分，这里只负责读出来给前端显示。
    """
    path = folder / f"{folder.name}.txt"
    got: dict[str, float] = {}
    total = None
    if path.is_file():
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            match = SCORE_RE.match(line)
            if match is not None:
                no, value = match.group(1), float(match.group(3))
                if no == "五":
                    # 编程题分两小问记，汇总成一行。分数单位是 0.1，加完取一位小数
                    got["五"] = round(got.get("五", 0.0) + value, 1)
                else:
                    got[no] = value
                continue
            match = TOTAL_SCORE_RE.match(line)
            if match is not None:
                total = float(match.group(1))

    sections = [
        {"no": no, "title": title, "full": full, "got": got.get(no)}
        for no, title, full in SECTIONS
    ]
    return {"sections": sections, "total": total}


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
        score_path = folder / f"{base}-代码评分.md"
        questions.append(
            {
                "no": label,
                "code": code_path.read_text(encoding="utf-8"),
                "review": _render(folder / f"{base}-代码评议.md"),
                "score": _render(score_path),
                # 标题上要写「11/14分」，从评分表的合计行取
                "total": _total(score_path),
            }
        )

    # 第一题在前、第二题在后。目前只有单个数码，按字符位置排就够。
    questions.sort(key=lambda q: NUMERALS.find(q["no"][0]))

    photos = _photos(folder)
    scores = _scores(folder)
    return {
        "student_id": student_id,
        "name": folder.name.split("-", 1)[1],
        "scores": scores,
        # 每张照片带索引、分组和修改时间。前端把修改时间拼进地址当版本号 ——
        # 照片缓存一年，换了图或插了新图之后序号会挪位，不带版本号就会一直显示旧缓存。
        "photos": [
            {"i": i, "kind": kind, "version": int(path.stat().st_mtime)}
            for i, (kind, path) in enumerate(photos)
        ],
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
    return photos[i][1].read_bytes()
