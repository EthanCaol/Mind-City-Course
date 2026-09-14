"""把「最后更新」提示从页面底部移到标题下方。

为什么用 hook 而不是模板覆盖：Material 的 partials/content.html 把日期渲染在
正文之后（第 10 行才 include source-file.html），模板层面最多只能把它挪到
标题**上方**，不是我们想要的位置。hook 操作的是渲染完成的 HTML，可以精确
插到标题下方。

日期来自 mkdocs-git-revision-date-localized-plugin 写进 page.meta 的数据。

有个坑值得记下来：插件源码里写的是往 page.meta 塞一个 dict（含 date / timeago /
iso_date 等字段），但真正拿到手时它已经是一个**渲染好的 HTML 字符串**了 ——
MkDocs 会把 meta 的值规范化成字符串。所以不要按 dict 去取值，直接当 HTML 处理。

这个字符串里含两个 span：

    <span class="timeago" datetime="..." locale="zh"></span>   ← 前端 JS 填成「X 天前」
    <span ...>2026-09-14</span>                                ← 裸日期

只要前一个，后一个是多余的（会和「X 天前」重复表达同一件事）。

页脚原来的那个日期由 extra.css 里的 .md-source-file { display: none } 隐藏。
"""

import re

import markdown
from material.extensions.emoji import to_svg, twemoji

# 提示文案。想改措辞直接改这里，改完存盘预览站就会刷新。
# 图标用 :material-xxx: 短代码，可选的图标名见
# https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/
NOTICE = ":material-history: 本页最后更新于 {timeago}，内容可能过时"

# hook 在 Markdown 转换之后才运行，所以短代码 :material-history: 不会被自动
# 处理。这里单独建一个只开 emoji 扩展的渲染器，把提示文本先转成 HTML。
# 只开这一个扩展而不是复用全站配置，是为了避免其它扩展带来意料之外的转换。
_renderer = markdown.Markdown(
    extensions=["pymdownx.emoji"],
    extension_configs={
        "pymdownx.emoji": {"emoji_index": twemoji, "emoji_generator": to_svg}
    },
)


def _render_notice(timeago: str) -> str:
    """把提示文本渲染成 HTML，并剥掉 Markdown 自动加的外层 <p>。"""
    _renderer.reset()
    rendered = _renderer.convert(NOTICE.format(timeago=timeago))
    if rendered.startswith("<p>") and rendered.endswith("</p>"):
        rendered = rendered[3:-4]
    return f'<p class="doc-updated">{rendered}</p>'


def on_page_content(html, page, config, files):
    """在标题下方插入提示。没有拿到 git 日期时原样返回，不显示提示。"""
    revision = page.meta.get("git_revision_date_localized")
    if not isinstance(revision, str):
        return html

    # 从渲染好的 HTML 里挑出 timeago 那段，丢掉重复表达同一时间的裸日期
    stamp = re.search(r'<span class="timeago".*?</span>', revision, re.S)
    if not stamp:
        return html

    notice = _render_notice(stamp.group(0))

    # 插到标题下方那组元信息之后。
    #
    # 优先排在 .doc-meta（负责助教 / 实验课时间）后面 —— 那行是文档的身份信息，
    # 应该紧贴标题；提示排在它下面，两行小字连成一组。没有 .doc-meta 的页面
    # 就退化为直接跟在 </h1> 后面；连 h1 都没有的（极少见）放到最前面。
    match = re.search(r'<p class="doc-meta">.*?</p>', html, re.S) or re.search(
        r"</h1>", html
    )
    if match:
        return html[: match.end()] + "\n" + notice + html[match.end() :]
    return notice + html
