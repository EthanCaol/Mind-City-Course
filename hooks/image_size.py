"""支持 `![](图片.png =250x)` 这种在地址后面直接写尺寸的图片写法。

Python-Markdown 不认这个写法，也不报错：`=250x` 被当成 URL 的一部分，
渲染出 `<img src="图片.png =250x">`，图片加载不出来。这个 hook 在 Markdown
转换之前把尺寸摘出来，改写成 attr_list 属性（`attr_list` 已在 mkdocs.yml 中启用）：

    ![](a.png =250x)      只给宽   → { width="250" }
    ![](a.png =250x150)   宽和高   → { width="250" height="150" }
    ![](a.png =x150)      只给高   → { height="150" }

三种写法就是 VSCode 扩展 Markdown Image Size 支持的那三种，见
docs/setup/markdown.md 的「5.3 图片尺寸」；这边不多认别的写法，免得同一个
文件在网站和 VSCode 预览里表现不一致。

为什么用 hook 改源码、而不是写一个 Markdown 扩展：MkDocs 用控制台脚本启动时
工作目录不在 `sys.path` 上，`markdown_extensions` 里写本地模块名会报
`ModuleNotFoundError`；而 `hooks` 是按文件路径加载的，没有这个问题。

尺寸必须写成「空白 + =」，所以带查询参数的地址（`?w=250`）不受影响。
行内代码和围栏代码块里的写法原样保留，方便在文档里举这个语法的例子。
"""

import re

# 三种情形：围栏代码块、行内代码、图片。前两种原样返回。
# 围栏必须排在行内代码前面 —— 否则开栅栏那行行首的三个反引号会先被行内代码
# 的规则吃掉两个，导致整个栅栏块落进「图片」分支里被改写。
PATTERN = re.compile(
    r"""
      (?P<fence>^[ ]{0,3}(?:```|~~~)[\s\S]*?^[ ]{0,3}(?:```|~~~)[^\n]*$)
    | (?P<code>`[^`\n]*`)
    | (?P<img>!\[(?P<alt>[^\]]*)\]\(\s*(?P<url>[^)]*?\S)\s+=(?P<size>[0-9]+x[0-9]*|[0-9]*x[0-9]+)\s*\))
    """,
    re.M | re.X,
)


def _replace(match):
    if match.group("img") is None:
        return match.group(0)

    width, _, height = match.group("size").partition("x")
    attrs = "".join(
        f' {name}="{value}"'
        for name, value in (("width", width), ("height", height))
        if value
    )
    return f"![{match.group('alt')}]({match.group('url')}){{{attrs} }}"


def on_page_markdown(markdown, **kwargs):
    return PATTERN.sub(_replace, markdown)
