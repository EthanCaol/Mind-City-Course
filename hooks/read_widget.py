"""去掉 nl2br 在「阅读登记」控件里插出来的多余 <br>。

控件那几行是裸 HTML，写在 `!!! todo` 里。admonition 的内容会被再解析一次，
`md_in_html` 因此把这几行当成 Markdown 段落处理，标签之间的换行就进了 inline
流程，nl2br 在每个换行处插一个 <br>。而 `.read__bar` 是 flex 布局，多出来的
<br> 各占一个 flex 项，按钮左边的间距会变大，控件上方也会多出一行空白。

这里把控件区间里的 <br> 去掉，输出与不开 nl2br 时一致。控件的 HTML 由本站自己
写，结构固定，所以正则只匹配这一段。

之所以不给这 18 个页面改源文件：控件的标签要连成一行才不会被插 <br>，那样每个
源文件里会多出一条 350 字符的长行，比这里多两行正则更难读。
"""

import re

WIDGET = re.compile(
    r'<div class="read" id="read".*?<p class="read__note".*?</div>',
    re.S,
)
# nl2br 是在原有换行前插一个 <br>，所以只摘掉 <br> 本身、后面的空白原样留着，
# 输出就与不开 nl2br 时逐字节一致。
BR = re.compile(r"<br\s*/?>")


def on_page_content(html, page, config, files):
    return WIDGET.sub(lambda m: BR.sub("", m.group(0)), html)
