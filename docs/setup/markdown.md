# Markdown 笔记仓库

## 1. 把笔记文件夹发布到 GitHub

笔记写成 Markdown 文件放在一个文件夹里，再把这个文件夹发布成 GitHub 仓库，写完之后同步一次，就同时有了版本记录和一份云端副本。整个过程在 VSCode 里点几下即可完成，不需要在命令行里敲 git 命令。

Git 和 GitHub 的基本概念先看《Git-GitHub 基础操作》那一篇。

这一步的前提是本机装了 Git（Windows 上是 Git for Windows）。没装的话，源代码管理面板里会提示下载，装完重启 VSCode 再回来。

### 1.1 新建存放笔记的文件夹

在桌面上新建一个文件夹，名字随意，截图里叫 Note。

![在资源管理器里新建文件夹 Note，右键菜单中有一项「通过 Code 打开」](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261010090219554.png)

右键菜单里出现「通过 Code 打开」，是因为安装 VSCode 时勾选了「添加到 Windows 资源管理器目录上下文菜单」这一项。没勾也没关系，在 VSCode 里用「文件 → 打开文件夹」选到它，效果一样。

### 1.2 在 VSCode 里打开文件夹

文件夹打开后左侧会出现资源管理器，里面是空的。新建一个 `README.md`，内容不限：

![VSCode 打开文件夹后新建 README.md 并写入内容](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261010090231340.png)

`README.md` 不是必须的，它的作用是在仓库页上显示一段说明。文件名固定是 README，大小写都可以。

### 1.3 初始化仓库

点左侧活动栏里的源代码管理图标（从上往下第三个，图标是几个圆点连成的分叉），面板里按顺序点两个按钮：

1. Initialize Repository，在文件夹里建一个 git 仓库。这一步只在本机完成，还没有连到 GitHub
2. Publish to GitHub，把这个仓库发布到 GitHub

![源代码管理面板里的 Initialize Repository 和 Publish to GitHub，以及命令面板里 private / public 两项](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261010090327239.png)

点完 Publish to GitHub，命令面板（顶部的输入框）里出现两项，对应仓库的两种可见性：

- Publish to GitHub private repository：只有自己能看到，别人打开这个地址是 404
- Publish to GitHub public repository：任何人可见，也会被搜索引擎收录

笔记放哪种都可以，不确定就选 private。第一次发布会弹出 GitHub 的授权页面，用浏览器登录账号，点 Authorize Visual-Studio-Code 同意，VSCode 就拿到了新建仓库的权限。授权只需要做一次。

### 1.4 选择要发布的文件

接着是一份文件清单，勾选要放进仓库的文件，点 OK：

![文件清单里勾选 README.md，点 OK 确认](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261010090400279.png)

文件夹里现有的文件都会列出来。不想让某些文件进仓库（临时文件、草稿、素材），在这里把勾去掉即可。以后想排除同一类文件，可以在仓库根目录写一份 `.gitignore`，把文件名或通配符写进去。

### 1.5 确认发布结果

发布完成后右下角弹一条提示，写着 Successfully published … to GitHub。左侧面板里同时出现一条 first commit 记录：

![右下角的发布成功提示和面板里的 first commit 记录](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261010090508901.png)

点提示里的 Open on GitHub，浏览器打开的就是刚建好的仓库页：

![浏览器里 GitHub 上的仓库页，README 已经渲染出来](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261010090543022.png)

页面右上角仓库名旁边有 Private 标记，说明按 private 发布成功。标题下方那个方框是 `README.md` 的渲染结果，文件已经从本机推到了 GitHub。

### 1.6 以后怎么同步

写完新的笔记，回到 VSCode 的源代码管理面板：

1. 在 Message 输入框里写一行说明，比如改了哪一篇
2. 点 Commit，改动记录到本机的 git 仓库；也可以直接按 ++ctrl+enter++
3. 提交后按钮变成 Sync Changes，点它把提交推送到 GitHub

推到 GitHub 之后刷新网页就能看到新内容。提交信息写清楚一些，以后查看历史记录时能知道每次改了什么。

---

## 2. 安装 Markdown All in One

点左侧活动栏最下面的方块图标，打开扩展面板，在搜索框里输入 markdown all in one，安装 Yu Zhang 那个（安装量最高的一个）：

![扩展面板里搜索 markdown all in one，结果第一条已安装](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261010090650903.png)

这个扩展补上 VSCode 内置 Markdown 编辑功能缺的几件事：

- 表格自动对齐：光标放在表格里按 ++alt+shift+f++，把各列的竖线对齐
- 快捷键：++ctrl+b++ 加粗、++ctrl+i++ 斜体
- 列表续行：在列表项末尾回车时，自动带上上一个列表项的标记

---

## 3. 配置 Markdown 预览

VSCode 内置的 Markdown 预览（在 `.md` 文件里按 ++ctrl+k++ ++v++ 打开）用浏览器内核渲染，字号、行高、字体都可以改。改法是写进 `settings.json`：按 ++ctrl+shift+p++ 打开命令面板，输入 `Preferences: Open Settings (JSON)` 回车。

把下面这些项加进最外层的大括号里：

```json
{
    "markdown.preview.breaks": true,
    "markdown.preview.fontSize": 15,
    "markdown.preview.lineHeight": 1.6,
    "markdown.preview.linkify": true,
    "markdown.preview.fontFamily": "Cascadia Code",
    "markdown.preview.markEditorSelection": false,
    "markdown.preview.scrollPreviewWithEditor": true,
    "markdown.preview.scrollEditorWithPreview": false,
    "markdown.preview.doubleClickToSwitchToEditor": true,
    // 助教的自定义样式，可以删掉，也可以改成自己喜欢的
    "markdown.styles": [
        "https://cdn.jsdelivr.net/gh/EthanCaol/mathpix-markdown-studio@f9822203519b440daed65d5d767af4425e9cb1e2/styles/Markdown.css"
    ],
    "[markdown]": {
        "editor.wordWrap": "off",
        "editor.wordWrapColumn": 60,
        "editor.tabSize": 4,
        "editor.defaultFormatter": "yzhang.markdown-all-in-one"
    }
}
```

每一项的作用：

| 设置项                                         | 作用                                                                                                   |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `markdown.preview.breaks`                      | 单个换行也当成换行，和 GitHub 网页上的表现一致。关掉的话，必须空一整行才能分段，单个换行被当成空格 |
| `markdown.preview.fontSize`                    | 预览正文字号，单位是像素                                                                               |
| `markdown.preview.lineHeight`                  | 预览的行距倍数                                                                                         |
| `markdown.preview.linkify`                     | 预览里出现的裸网址自动变成可点的链接                                                                   |
| `markdown.preview.fontFamily`                  | 预览正文的字体。Cascadia Code 是等宽字体，中文没有对应的字形，仍然由系统字体渲染                       |
| `markdown.preview.markEditorSelection`         | 编辑区选中的内容是否在预览里同步反色标出                                                               |
| `markdown.preview.scrollPreviewWithEditor`     | 编辑区滚动时预览跟着滚                                                                                 |
| `markdown.preview.scrollEditorWithPreview`     | 反向联动，由预览带动编辑区。关掉可以避免两个窗格互相带动                                               |
| `markdown.preview.doubleClickToSwitchToEditor` | 在预览里双击，光标跳到编辑区对应的位置                                                                 |
| `markdown.styles`                              | 额外加载的样式表，可以写网络地址，也可以写本地路径。上面那条是助教自己用的，删掉不影响其他配置         |

`[markdown]` 这一段只在 Markdown 文件里生效，不影响其他文件：

- `editor.wordWrap` 关掉自动换行，长行靠横向滚动查看
- `editor.tabSize` 是缩进宽度
- `editor.defaultFormatter` 指定 ++alt+shift+f++ 交给哪个扩展做格式化

`markdown.styles` 里的样式表托管在网络上，预览每次打开都会请求一次，断网时退回默认样式，正文内容不受影响。

---

## 4. Markdown 语法补充

常用语法这两页写得比较全：

- [Markdown 基础语法](https://markdown.com.cn/basic-syntax/)
- [Markdown 扩展语法](https://markdown.com.cn/extended-syntax/)

这里只补充两件笔记里常用的事。

### 4.1 表格对齐

表格的竖线对不齐不影响渲染结果，只影响源码读起来是否舒服。光标放在表格里按 ++alt+shift+f++，Markdown All in One 会把每列补到同一列宽：

```markdown
| 设置项                    | 作用               |
| ------------------------- | ------------------ |
| `markdown.preview.breaks` | 单个换行也当成换行 |
```

注意 `---` 前面和后面都要有空格，紧贴着写的 `|---|---|` 部分解析器不支持。

### 4.2 数学公式

VSCode 内置的 Markdown 预览自带公式渲染，语法是 LaTeX，不需要额外装扩展。下面三种写法在笔记里用得最多。

行内公式：前后各加一个 `$`。

```markdown
$\lim a_n=a\land\lim a_n=a'\implies a=a'$
$f'(x)=\lim_{t\to x}\frac{f(t)-f(x)}{t-x}$
```

渲染成 $\lim a_n=a\land\lim a_n=a'\implies a=a'$ 和 $f'(x)=\lim_{t\to x}\frac{f(t)-f(x)}{t-x}$。

行内大公式：外面套一层 `\begin{aligned}...\end{aligned}`。分数、极限这类符号直接写在行内尺寸偏小，套上之后按整行的尺寸渲染，下标和分数线都清楚一些，位置仍然跟着文字。

```markdown
$\begin{aligned}f'(x)=\lim_{t\to x}\frac{f(t)-f(x)}{t-x}\end{aligned}$
```

渲染成 $\begin{aligned}f'(x)=\lim_{t\to x}\frac{f(t)-f(x)}{t-x}\end{aligned}$。

行间公式：前后各加两个 `$`，公式独占一行并且居中。多行推导写在 `\begin{aligned}` 里，行与行之间用两个反斜杠断开，对齐位置用 `&` 标出。

```markdown
$$
||w+v||^2&=\langle w+v,w+v\rangle\\
&=\langle w,w\rangle+\langle w,v\rangle+\langle v,w\rangle+\langle v,v\rangle\\
&=\langle w,w\rangle+\langle w,v\rangle+\overline{\langle w,v\rangle}+\langle v,v\rangle\\
&=||w||^2+2Re\langle w,v\rangle+||v||^2\\
&\le||w||^2+2|\langle w,v\rangle|+||v||^2\\
&\le||w||^2+2||w||\cdot||v||+||v||^2\\
&=(||w||+||v||)^2
\end{aligned}
$$
```

渲染出来是：

$$
||w+v||^2&=\langle w+v,w+v\rangle\\
&=\langle w,w\rangle+\langle w,v\rangle+\langle v,w\rangle+\langle v,v\rangle\\
&=\langle w,w\rangle+\langle w,v\rangle+\overline{\langle w,v\rangle}+\langle v,v\rangle\\
&=||w||^2+2Re\langle w,v\rangle+||v||^2\\
&\le||w||^2+2|\langle w,v\rangle|+||v||^2\\
&\le||w||^2+2||w||\cdot||v||+||v||^2\\
&=(||w||+||v||)^2
\end{aligned}
$$

写行间公式时，前后各空一行。紧贴着上一段文字写，预览有时会把它当成行内公式而不是独立公式。

<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>

---

## 5. 给笔记仓库加指令和技能

装了 Claude Code 之后，可以让它按你的习惯往仓库里写文件，而不是每开一个新会话都交代一遍。做法是在仓库里放两个文件：

- 仓库根目录的 `CLAUDE.md`：在这个仓库里启动 Claude Code 时自动读入，里面是这个仓库的长期约定
- `.claude/skills/` 下的技能：每个技能一个目录，里面放 `SKILL.md`，敲 `/` 加技能名触发

Claude Code 的安装和配置见《Claude 工具链配置》那一篇。

### 5.1 仓库指令文件

约定写在仓库根目录的 `CLAUDE.md` 里。把希望 Claude 遵守的约定说清楚，它会建好这个文件。下面是助教用的那份：

````markdown
# Skill

本仓库的 skill 放在 `.claude/skills/` 下
新增 skill 时, frontmatter 默认写 `user-invocable: false`

# 文风

## 用词

适用于写入本仓库的文件, 也适用于对话回复
- 用平实的说明文, 接近产品说明书的写法
- 陈述事实与操作, 以可读性和准确性为准
- 不用夸张、煽动、摆谱的措辞
- 不用口语化说法
- 不拟人, 不调侃, 不评价读者, 不表演共情
- 补充解释之前不写俏皮话
- 动词选最普通的: 由...组成, 演示, 决定, 换成, 生成

## 标点与断句

只适用于写入本仓库的文件, 对话回复不受此约束
- 不用全角标点: `。` `，` `、` `：` `；` `（）` `「」`
- 不用 ①②③, ⑴⑵⑶, ⒈⒉⒊, ㈠㈡㈢ 这类带圈或带括号的序号字符, 序号一律写成 `1.` `2.` 或 `(1)` `(2)`
- 逗号写成半角 `, `, 后面跟一个空格
- 冒号与括号用半角 `:` `(` `)`
- 句末不加终止符, 靠换行断开
- 一行一个短句
- 并列项, 条件, 结论各自成行
- 该停顿的地方换行, 不堆长句

## 结构

- 文档开头空三行
- 块与块之间用 `------` 分隔
- 分割线前后各留一个空行
- 一级与二级标题渲染后自带分割线, 标题前不写 `------`
- 一级与二级标题前空两行
- 三级及以下的标题不带分割线, 标题前照常写 `------`
- 术语写成 `术语: 解释`
- 例题与推导写成 `> 例1-1: ...` 引用块
- 附注, 特例用 `[方括号]` 标出

## 公式渲染

只适用于写入本仓库的文件
如果用户觉得行内公式含分数 `\frac{}{}` 的渲染样式偏小
可以用 `$\begin{aligned}...\end{aligned}$` 包住可以放大渲染样式

公式由 MPE 预览渲染
数学模式内可以放中文, 不需要为此改写公式
不要为了验证渲染去装 KaTeX 等命令行工具, 命令行版与预览内嵌的解析器不是同一套
子 agent 看不到预览, 遇到不确定的写法照原样写, 并在报告里列出待确认项

# 系统编码

本机代码页为 936 (GBK), Python 的 stdout 默认编码是 gbk, 命令行输出中文会乱码
改为 UTF-8 需写以下三个注册表值

[需要管理员权限, 且必须重启后生效]

```
Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Nls\CodePage' -Name ACP   -Value 65001
Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Nls\CodePage' -Name OEMCP -Value 65001
Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Nls\CodePage' -Name MACCP -Value 65001
```

重启后用 `python -I -c "import sys; print(sys.stdout.encoding)"` 验证, 输出 utf-8 即生效
````

内容按自己的习惯改。前四节约束的是写进仓库的文件的写法：用词、标点、结构、公式渲染。最后一节 `系统编码` 不是写作规则，是改 Windows 的命令行编码，避免命令行输出中文时乱码；这一节与笔记内容无关，不需要的话整段删掉。

### 5.2 提交用的技能

技能文件不需要自己建。在仓库里启动 Claude Code，把下面这段粘贴进去即可：

它会建好目录、写好这个文件，要改内容也是直接说，不需要手动改文件。

```markdown
---
name: push
description: "本笔记仓库的提交约定: 当用户说 push / 提交 / commit / 推送, 或需要把改动写进 git 提交历史时使用"
user-invocable: true
---

# 提交方式

1. 触发: 用户说 `push`, 若无其他疑问, 直接提交到远程仓库
2. 范围: 只提交用户点名的内容
   - 临时文件, 草稿, 临时图片一律先列出并征得同意后再处理
   - 不主动 `git add`
3. 格式: 统一写成 `[26/9/29 0:14] 中文一句话简要概括`
   - 方括号内为提交时刻, 月/日/时不补零, 分补两位, 由 agent 取本地时间填入
   - 时间不要自己拼接格式串, 直接用 `$(date '+%y/%-m/%-d %-H:%M')`
   - 概述压到一句话, 一句话写不下时空一行再补正文
   - 不用多行 `-m` 拼 patch note
4. 执行: 一条命令走完 add/commit/push, 命令保持简短
   - 不先单独执行 status/diff/date 再回来确认
```

开头的 `---` 之间是 frontmatter，三个字段的作用：

| 字段             | 作用                                                                                   |
| ---------------- | -------------------------------------------------------------------------------------- |
| `name`           | 技能名，也是 `/` 后面敲的那个词，要和目录名一致                                        |
| `description`    | 一句话说明这个技能干什么、什么时候用。Claude 靠它判断该不该调用这个技能                |
| `user-invocable` | 是否允许手动用 `/push` 触发。只给 Claude 自己用的技能写 false，就不会出现在 `/` 列表里 |

建好之后敲 `/push` 即可使用。技能是在启动 Claude Code 时载入的，刚建好的要下一次启动才会出现在 `/` 列表里。约定集中在这两个文件里，要加新规则直接跟 Claude 说即可，不需要自己去翻语法。

# 助教的 VSCode 完整配置文件

```json title="settings.json"
--8<-- "code/settings.json"
```

---

!!! todo "文档完成登记：完成本文全部流程后告知助教"

    <div class="read" id="read" data-page="markdown">
      <div class="read__bar">
        <input id="read-id" class="read__input" type="text" inputmode="numeric" autocomplete="off" maxlength="11" placeholder="在这里输入你的学号">
        <button id="read-submit" type="button">我已读完</button>
      </div>
      <p class="read__note" id="read-note" hidden></p>
    </div>
