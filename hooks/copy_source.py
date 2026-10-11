"""在《数学分析》每章笔记的开头插入折叠块，里面放本篇的 Markdown 源码。

块内的代码由 Material 的 `content.code.copy` 提供右上角复制按钮，读者展开后能整段
取走。收起状态下按钮在折叠内容里，点不到，要先展开。

源码从 `page.file.abs_src_path` 读磁盘上的原文，不在页面里另存一份，因此正文有什么
块里就是什么，不会出现两份对不上的情况。

本钩子必须登记在 `image_size.py` **之后**：折叠块里的源码按 4 空格缩进，而
`image_size.py` 只认 3 空格以内的围栏，先跑的话会把这个块里的 `![](x.png =400x)`
当正文改写，读者看到的源码就不是原文了。
"""

import re
from pathlib import Path

# 只处理这一节下的页面。material.md 是 PDF 链接页，没有正文可给。
PREFIX = "math-analysis/"
SKIP = {PREFIX + "material.md"}

# 折叠块里的第一句。放在块内是为了紧挨着要复制的源码 —— 读者展开这个块，就是要拿去用。
REMINDER = (
    "复制到自己的笔记仓库之前，先按「Markdown 笔记仓库」那篇把 VSCode 配好。"
    "图片的 `=600x` 尺寸写法只有 Markdown Image Size 扩展认，不装就按原始尺寸显示；"
    "表格对齐和列表续行要 Markdown All in One。公式用 VSCode 内置的预览就能渲染，不用另装扩展。"
)


def _fence(text):
    """取一段比正文里最长的连续反引号更长的围栏，避免被正文里的围栏提前闭合。"""
    longest = max((len(run) for run in re.findall(r"`+", text)), default=0)
    return "`" * max(3, longest + 1)


def on_page_markdown(markdown, page, config, files):
    src = page.file.src_path
    if not src.startswith(PREFIX) or src in SKIP:
        return markdown

    raw = Path(page.file.abs_src_path).read_text(encoding="utf-8")
    fence = _fence(raw)
    indent = "    "
    body = "\n".join(indent + line for line in raw.split("\n"))

    return (
        '??? quote "点击展开，复制本篇源码"\n'
        "\n"
        f"{indent}{REMINDER}\n"
        "\n"
        f"{indent}{fence}markdown\n"
        f"{body}\n"
        f"{indent}{fence}\n"
        "\n"
        f"{markdown}"
    )
