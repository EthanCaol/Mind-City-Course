# Markdown 笔记仓库

## 1. 把笔记文件夹发布到 GitHub

笔记用 Markdown 文件写，统一放在一个文件夹里。把这个文件夹发布成 GitHub 仓库，以后每写完一次同步一次，笔记就有了版本记录和一份云端副本。

整个过程在 VSCode 里完成，不需要在命令行里输入 git 命令。

---

### 1.1 新建存放笔记的文件夹

在桌面上新建一个文件夹存放笔记，命名为 `Note`。

![在资源管理器里新建文件夹 Note，右键菜单中有一项「通过 Code 打开」](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261010090219554.png)

---

### 1.2 在 VSCode 里打开文件夹

文件夹打开后左侧会出现资源管理器，里面是空的。新建一个 `README.md`，写这个仓库的说明。它的内容会显示在仓库页上：

![VSCode 打开文件夹后新建 README.md 并写入内容](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261010090231340.png)

---

### 1.3 初始化仓库

点左侧活动栏里的源代码管理

面板里点按钮 Publish to GitHub，把这个仓库发布到 GitHub

![源代码管理面板里的 Initialize Repository 和 Publish to GitHub，以及命令面板里 private / public 两项](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261010090327239.png)

点完 Publish to GitHub，命令面板（顶部的输入框）里出现两项，对应仓库的两种可见性：

- Publish to GitHub private repository：私人仓库，只有自己能看到
- Publish to GitHub public repository：公有仓库，任何人可见

---

### 1.4 选择要发布的文件

接着是一份文件清单，勾选要放进仓库的文件，点 OK：

![文件清单里勾选 README.md，点 OK 确认](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261010090400279.png)

---

### 1.5 确认发布结果

点提示里的 Open on GitHub，浏览器打开的就是刚建好的仓库页：

![右下角的发布成功提示和面板里的 first commit 记录](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261010090508901.png)

![浏览器里 GitHub 上的仓库页，README 已经渲染出来](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261010090543022.png)

页面右上角仓库名旁边有 Private 标记，说明按 private 发布成功。

标题下方那个方框是 `README.md` 的渲染结果，说明文件已经从本机推送到了 GitHub。

---

### 1.6 以后怎么同步

写完一篇笔记后，在 VSCode 的源代码管理面板里提交并推送：

1. 在 Message 输入框里写一行说明，比如改了哪一篇
2. 点 Commit，改动记录到本机的 git 仓库
3. 提交后按钮变成 Sync Changes，点它把提交推送到 GitHub

---

## 2. 安装 Markdown All in One

![扩展面板里搜索 markdown all in one，结果第一条已安装](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261010090650903.png)

这个扩展补上 VSCode 内置 Markdown 编辑功能缺的两件事：

- 表格自动对齐：光标放在表格里按 ++alt+shift+f++，把各列的竖线对齐
- 列表续行：在列表项末尾回车时，自动带上上一个列表项的标记

---

## 3. 快捷键绑定

点左下角的齿轮图标，在菜单里选 `Keyboard Shortcuts`：

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011161904570.png)

在搜索框里输入 `markdown open preview`，找到 `Markdown: Open Preview to the Side`，双击 `Keybinding` 那一列，按下 ++ctrl+alt+m++ 并绑定新快捷键。

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011162000446.png)

改完立即生效，以后在 `.md` 文件里按 ++ctrl+alt+m++，右侧就会打开预览窗格。

---

## 4. 配置 Markdown 预览

把下面这些配置项加到 `settings.json`：

```json
{
    "markdown.preview.fontSize": 15,
    "markdown.preview.breaks": true,
    "markdown.preview.linkify": true,
    "markdown.preview.lineHeight": 1.6,
    "markdown.preview.markEditorSelection": false,
    "markdown.preview.scrollPreviewWithEditor": true,
    "markdown.preview.scrollEditorWithPreview": false,
    "markdown.preview.doubleClickToSwitchToEditor": true,
    "markdown.preview.fontFamily": "Cascadia Code",

    // 助教的自定义样式，可以改成自己喜欢的
    "markdown.styles": [ "https://cdn.jsdelivr.net/gh/EthanCaol/mathpix-markdown-studio@f9822203519b440daed65d5d767af4425e9cb1e2/styles/Markdown.css" ],
    "[markdown]": {
        "editor.wordWrap": "off",
        "editor.wordWrapColumn": 60,
        "editor.tabSize": 4,
        "editor.defaultFormatter": "yzhang.markdown-all-in-one"
    },
}
```

每一项的作用：

| 设置项                                         | 值             | 作用                           |
| ---------------------------------------------- | -------------- | ------------------------------ |
| `markdown.preview.breaks`                      | true           | 单个换行也分段，与 GitHub 一致 |
| `markdown.preview.fontSize`                    | 15             | 正文字号，单位像素             |
| `markdown.preview.lineHeight`                  | 1.6            | 行距倍数                       |
| `markdown.preview.linkify`                     | true           | 裸网址变成可点链接             |
| `markdown.preview.fontFamily`                  | Cascadia Code  | 正文字体                       |
| `markdown.preview.markEditorSelection`         | false          | 选中内容在预览里反色标出       |
| `markdown.preview.scrollPreviewWithEditor`     | true           | 编辑区滚动带动预览             |
| `markdown.preview.scrollEditorWithPreview`     | false          | 预览滚动带动编辑区             |
| `markdown.preview.doubleClickToSwitchToEditor` | true           | 预览里双击跳回编辑区           |
| `markdown.styles`                              | 网址或本地路径 | 额外加载的样式表               |
 
`markdown.preview.scrollEditorWithPreview` 关掉，避免两个窗格互相带动。`markdown.preview.fontFamily` 用的 Cascadia Code 是等宽字体，中文没有对应字形，仍由系统字体渲染。`markdown.styles` 可以写网址，也可以写本地路径，上面那条是助教自己用的，删掉不影响其他配置。

`[markdown]` 这一段只在 Markdown 文件里生效，不影响其他文件：

- `editor.wordWrap` 关掉自动换行
- `editor.tabSize` 是缩进宽度
- `editor.defaultFormatter` 指定 ++alt+shift+f++ 交给哪个扩展做格式化

---

## 5. Markdown 语法补充

常用语法这两页写得比较全：

- [Markdown 基础语法](https://markdown.com.cn/basic-syntax/)
- [Markdown 扩展语法](https://markdown.com.cn/extended-syntax/)

---

### 5.1 表格对齐

表格的竖线对不齐不影响渲染结果，只影响源码读起来是否舒服。光标放在表格里按 ++alt+shift+f++，Markdown All in One 会把每列补到同一列宽。

---

### 5.2 数学公式

VSCode 内置的 Markdown 预览自带公式渲染，语法是 LaTeX，不需要额外装扩展。下面三种写法在笔记里用得最多。

行内公式：前后各加一个 `$`。

```markdown
$f'(x)=\lim_{t\to x}\frac{f(t)-f(x)}{t-x}$
$\lim a_n=a\land\lim a_n=a'\implies a=a'$
$\ce{C(石墨) + O2(g) -> CO2(g)}\quad\Delta_rH_\text{m}=-393.5\ \mathrm{kJ\cdot mol^{-1}}$
```

$f'(x)=\lim_{t\to x}\frac{f(t)-f(x)}{t-x}$
$\lim a_n=a\land\lim a_n=a'\implies a=a'$
$\ce{C(石墨) + O2(g) -> CO2(g)}\quad\Delta_rH_\text{m}=-393.5\ \mathrm{kJ\cdot mol^{-1}}$

---

行内大公式：外面套一层 `\begin{aligned}...\end{aligned}`。分数、极限这类符号直接写在行内尺寸偏小，套上之后按整行的尺寸渲染，下标和分数线都清楚一些，位置仍然跟着文字。

```markdown
$\begin{aligned}f'(x)=\lim_{t\to x}\frac{f(t)-f(x)}{t-x}\end{aligned}$
$\begin{aligned}\frac{\partial^2\psi}{\partial x^2}+\frac{\partial^2\psi}{\partial y^2}+\frac{\partial^2\psi}{\partial z^2}+\frac{8\pi^2m}{h^2}(E-V)\psi=0\end{aligned}$
```

$\begin{aligned}f'(x)=\lim_{t\to x}\frac{f(t)-f(x)}{t-x}\end{aligned}$
$\begin{aligned}\frac{\partial^2\psi}{\partial x^2}+\frac{\partial^2\psi}{\partial y^2}+\frac{\partial^2\psi}{\partial z^2}+\frac{8\pi^2m}{h^2}(E-V)\psi=0\end{aligned}$

---

行间公式：前后各加两个 `$`，公式独占一行并且居中。多行推导写在 `\begin{aligned}` 里，行与行之间用两个反斜杠断开，对齐位置用 `&` 标出。

```markdown
$$
\begin{aligned}
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

$$
\begin{aligned}
||w+v||^2&=\langle w+v,w+v\rangle\\
&=\langle w,w\rangle+\langle w,v\rangle+\langle v,w\rangle+\langle v,v\rangle\\
&=\langle w,w\rangle+\langle w,v\rangle+\overline{\langle w,v\rangle}+\langle v,v\rangle\\
&=||w||^2+2Re\langle w,v\rangle+||v||^2\\
&\le||w||^2+2|\langle w,v\rangle|+||v||^2\\
&\le||w||^2+2||w||\cdot||v||+||v||^2\\
&=(||w||+||v||)^2
\end{aligned}
$$

<script src="/assets/katex/katex.min.js"></script>
<script src="/assets/katex/auto-render.min.js"></script>
<script>renderMathInElement(document.querySelector('.md-content'));</script>

---

### 5.3 图片尺寸

VSCode 内置的 Markdown 预览按图片的原始尺寸显示，源码里没法指定宽高。装扩展 Markdown Image Size（发布者 Matt Bierner）之后，可以在图片地址后面直接写尺寸：

![扩展面板里的 Markdown Image Size，发布者 Matt Bierner](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011195120034.png)

写法是 `=` 加尺寸，三种：

| 写法                        | 效果               |
| --------------------------- | ------------------ |
| `![](./img/a.png =250x)`    | 宽 250，高度按比例 |
| `![](./img/a.png =x150)`    | 高 150，宽度按比例 |
| `![](./img/a.png =250x150)` | 宽 250，高 150     |

只写一边时，另一边按原图比例算，图片不会变形。`=` 前面要有一个空格，`=` 后面紧接数字或 `x`，中间不能有空格。

这个写法是扩展提供的，GitHub 不认：在 GitHub 仓库页上看笔记时，`=250x` 被当成图片地址的一部分，图片显示不出来。宽高只在装了扩展的 VSCode 预览里生效。

## 6. 给笔记仓库加指令和技能

装了 Claude Code 之后，可以让它按你的习惯往仓库里写文件，而不是每开一个新会话都交代一遍。做法是在仓库里放两个文件：

- 仓库根目录的 `CLAUDE.md`：在这个仓库里启动 Claude Code 时自动读入，里面是这个仓库的长期约定
- `.claude/skills/` 下的技能：每个技能一个目录，里面放 `SKILL.md`，敲 `/` 加技能名触发

---

### 6.1 仓库指令文件

约定写在仓库根目录的 `CLAUDE.md` 里。把希望 Claude 遵守的约定说清楚，它会建好这个文件。下面是助教用的那份：

````markdown
--8<-- "code/markdown-claude.md"
````

---

### 6.2 提交用的技能

不用自己写技能文件。在仓库里启动 Claude Code，把下面这段粘贴进对话即可。

```markdown
帮我给当前仓库添加一个Skill, 具体内容如下

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

开头两条 `---` 之间是 frontmatter，里面有三个字段：

| 字段             | 作用                                                                                   |
| ---------------- | -------------------------------------------------------------------------------------- |
| `name`           | 技能名，也是 `/` 后面敲的那个词，要和目录名一致                                        |
| `description`    | 一句话说明这个技能干什么、什么时候用。Claude 靠它判断该不该调用这个技能                |
| `user-invocable` | 是否允许手动用 `/push` 触发。只给 Claude 自己用的技能写 false，就不会出现在 `/` 列表里 |

建好之后，在对话里敲 `/push` 就能用。技能在启动 Claude Code 时载入，刚建的技能要下一次启动才出现在 `/` 列表里。仓库的约定都写在这两个文件里，以后要加规则，直接跟 Claude 说，不用自己翻语法。


## 7. 助教的笔记仓库格式（供参考）

这一节用助教自己的笔记仓库 Mind-City 作例子，说明笔记仓库可以怎样组织，下面按层级列出各个目录。格式不用照搬，按自己的学科和笔记风格调整即可。

### 7.1 顶层目录

![Mind-City 仓库的顶层结构](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261021081517146.png)

顶层是四个目录、`.claude` 和两个文件，各自管一类内容：

| 名称        | 内容                             |
| ----------- | -------------------------------- |
| `.claude/`  | 技能文件，见 7.2                 |
| `Annex/`    | 零散文件与自写的小工具，见 7.3   |
| `Coursera/` | 学科笔记，见 7.4                 |
| `Paper/`    | 论文笔记，见 7.5                 |
| `Skill/`    | 环境配置备忘录，见 7.6           |
| `CLAUDE.md` | 仓库级提示词，见 7.7             |
| `README.md` | 笔记目录与电子书的对应表，见 7.7 |

------

### 7.2 .claude/skills：仓库级的Agent技能

![.claude/skills 下的十一个技能目录](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261021081632389.png)

技能一个目录一个 `SKILL.md`，按用途命名。仓库里现在有 11 个，分两类：

| 类别         | 技能                                                             | 触发方式                    |
| ------------ | ---------------------------------------------------------------- | --------------------------- |
| 独立任务     | `push`、`pdf-bookmark`、`super-resolution`、`textbook-to-notes`  | 出现在 `/` 列表里，手动调用 |
| 流程中的一步 | `pdf-page-image`、`note-writing`、`pdf-figure-crop`、`coscmd` 等 | 由 Claude 在流程中间调用    |

------

### 7.3 Annex：杂项

![Annex 目录下的零散文件](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261021081704389.png)

不适合和笔记放在一起的文件放这里：图标、CSS 样式表、备份文件，以及两个自己写的 VSCode 扩展。

- `markdown-preview-scroll-toggle`：在编辑器标题栏放一个按钮，切换预览的滚动同步
- `markdown-preview-smiles`：把预览里 `&CCO&` 形式的文本渲染成分子结构式，对应 7.7 节的 `CLAUDE.md` 里「SMILES 渲染」一节

分子结构在化学笔记里出现频繁，做成扩展之后，笔记里直接写 `&CCO&` 就能看到结构式，不必每次裁图、上传、回填链接。

------

### 7.4 Coursera：笔记的目录分级

![Coursera 下按学科划分的五个目录](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261021081747581.png)

一级目录按学科分，名字写成 `[N]学科`。`N` 只用来排序，方括号把编号和学科名隔开，展开后按数字顺序排列。

二级是课程，写成 `(N)课程名`；课程下每一章一个文件，写成 `(N)章节名.md`。

![抽象代数目录下的五个章节文件](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261021081812150.png)

`(3)抽象代数` 下是 `(0)数论` 到 `(4)域论` 五个章节文件。编号用半角圆括号，和课程目录的写法统一，展开目录时能看出哪一层是编号。

这些笔记的统一风格，由 7.7 节的 `CLAUDE.md` 来约束。

------

### 7.5 Paper：论文笔记

![Paper 目录下的论文笔记与论文稿](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261021081846015.png)

论文笔记按 `年份-论文简称.md` 命名，年份在前，资源管理器里自动按时间排序。

仓库里存的是中文整理版，论文原文同步在 Zotero，不进仓库。

------

### 7.6 Skill：环境配置备忘录

![Skill 目录下的配置备忘录](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261021081956548.png)

装系统和配软件的过程记在这里，一个主题一篇：`Conda配置`、`Linux配置`、`Docker笔记`、`Zotero配置` 等。这些文件是重装环境时，用于复现的操作记录。

------

### 7.7 CLAUDE.md 与 README.md

![仓库根的 CLAUDE.md 与 README.md](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261021082010702.png)

两个文件分工不同：

- `CLAUDE.md` 是仓库级提示词，写长期约定：仓库结构、技能的放置、文风、标点与断句、文档结构、公式渲染。
- `README.md` 是一张对应表：左边是笔记目录，右边是对应的电子书路径

```markdown title="CLAUDE.md"
# 仓库结构

笔记按学科组织在 `Coursera/` 下
笔记目录与配套电子书的对应关系见 `README.md`

# Skill

本仓库的 skill 放在 `.claude/skills/` 下
新增 skill 时, frontmatter 默认写 `user-invocable: false`

从教材 PDF 做笔记走 `textbook-to-notes`, 分渲染, 写作, 裁图, 上传四步

调试 skill 走 `debug-skill`, 分起子 agent 试跑, 记录问题, 改 skill, 复查四步

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
- 不用 ①②③, ⑴⑵⑶, ⒈⒉⒊, ㈠㈡㈢ 这类带圈或带括号的序号字符, 序号一律写成 `(1)` `(2)` 或者 `1.` `2.`
- 逗号写成半角 `, `, 后面跟一个空格
- 冒号与括号用半角 `:` `(` `)`
- 句末不加终止符, 靠换行断开
- 一行一个短句
- 并列项, 条件, 结论各自成行
- 该停顿的地方换行, 不堆长句
- 一行尽量不超过 60 个字符, 中文与 LaTeX 都按 1 个字符计
- 长句在逗号, 以及 `且` `或` `则` `即` `所以` `于是` `由` 等处断开, 拆成多行
- 一条公式单独占一行, 不与说明文字混排
- 推导链一行一步, 写成 `$...$` 顺次排下来
- 断不开的长公式(`\begin{cases}`, 长不等式链)保留整行, 不硬拆
- 全篇非空行的长度中位数不超过 45, 超过 100 字符的行占非空行不到 5%

## 结构

- 文档开头空三行
- 全篇用 `##` 作节标题, 不用 `#` 与 `###`
- 二级标题前空两行, 渲染后自带分割线, 标题前不写 `------`
- 二级标题后空一行, 不与正文紧贴
- 块组之间用 `------` 分隔, 分割线前后各留一个空行
- 块组是一个完整的知识单元, 指一个定义簇, 一个定理连同它的证明, 或一串例题
- 块组内部按阶段用空行分段, 不插 `------`
  - 定理的陈述与它的证明之间空一行
  - 证明内部每 2 到 6 行一段, 分段点取在引入新的量(取, 令, 设), 换到另一个对象, 得出阶段性结论, 以及最后收束处
  - 定义簇里并列的多个定义之间空一行
  - 一串例题之间空一行
- 术语写成 `术语: 解释`
- 例题与推导写成 `> 例1-1: ...` 引用块
- 附注, 特例用 `[方括号]` 标出
- [用到三级标题时, 它不带分割线, 标题前照常写 `------`]
- 排版范例见 `Coursera/[1]数学/(3)抽象代数` 与 `Coursera/[1]数学/(5)数学分析` 下的笔记

## 公式渲染

只适用于写入本仓库的文件
如果用户觉得行内公式含分数 `\frac{}{}` 的渲染样式偏小, 可以用 `\dfrac{}{}`
或者换成使用 `$\begin{aligned}...\end{aligned}$` 包住可以放大渲染样式

公式由 MPE 预览渲染
数学模式内可以放中文, 不需要为此改写公式
不要为了验证渲染去装 KaTeX 等命令行工具, 命令行版与预览内嵌的解析器不是同一套
子 agent 看不到预览, 遇到不确定的写法照原样写, 并在报告里列出待确认项

## SMILES 渲染

分子结构用 SMILES 写, 两端加 `&`, 例如 `&CCO&`
写在正文中间或单独占一行都可以, 渲染宽度由是否独占一行决定

## 示例

改前: 该系统由三部分组成，分别是 A、B 和 C。
改后: 该系统由三部分组成
1. A
2. B
3. C

# 校验

- 写完尽量自己 Read 通读一遍验收, 不要写一堆 Python 校验脚本
- 脚本尽量只用在真正机械的操作上, 例如批量插入空行

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
```

```markdown title="README.md"
# Mind-City

个人笔记仓库。笔记按学科组织在 `Coursera/` 下
配套电子书放在 Google Drive 的 `G:\我的云端硬盘\电子书`
两边大体按 `[学科]/(课程)` 同构命名

- 笔记根目录: `Coursera/`
- 电子书根目录: `G:\我的云端硬盘\电子书`
- 下表「电子书」列是相对电子书根目录的路径

## [1]数学

| 笔记目录        | 电子书                                                                                                                                                                          |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `(0)数理逻辑`   | `[1]数学/(0)数理逻辑/数理逻辑-证明及其限度-杨跃.pdf`                                                                                                                            |
| `(1)组合数学`   | `[1]数学/(1)组合数学/组合数学引论.pdf`                                                                                                                                          |
| `(2)图与网络`   | `[1]数学/(2)图与网络/图论与代数结构.pdf`                                                                                                                                        |
| `(3)抽象代数`   | `[1]数学/(3)抽象代数/初等数论.pdf`<br>`[1]数学/(3)抽象代数/近世代数-丘维声.pdf`<br>`[1]数学/(3)抽象代数/抽象代数基础-丘维声.pdf`<br>`[1]数学/(3)抽象代数/抽象代数学-姚慕生.pdf` |
| `(4)线性代数`   | `[1]数学/(4)线性代数/线性代数应该这样学-第四版.pdf`<br>`[1]数学/(4)线性代数/线性代数应该这样学-第三版.pdf`                                                                      |
| `(5)数学分析`   | `[1]数学/(5)数学分析/数学分析原理.pdf`（Rudin）<br>`[1]数学/(5)数学分析/数学分析-伍胜健.pdf`<br>`[1]数学/(5)数学分析/实分析-陶哲轩.pdf`                                         |
| `(6)概率统计`   | `[1]数学/(6)概率统计/数理统计学导论.pdf`<br>`[1]数学/(6)概率统计/测度论与概率论基础.pdf`                                                                                        |
| `(7)常微分方程` | `[1]数学/(7)常微分方程/常微分方程教程.pdf`                                                                                                                                      |

## [2]计算机

| 笔记目录          | 电子书                                                                                              |
| ----------------- | --------------------------------------------------------------------------------------------------- |
| `(0)C语言`        | `[2]计算机/(0)编程语言/C语言程序设计（第3版）.pdf`                                                  |
| `(0)计算机网络`   | `[2]计算机/(0)计算机网络/计算机网络 自顶向下方法.pdf`                                               |
| `(0)编译原理`     | `[2]计算机/(0)编译原理/编译原理（第2版）.pdf`                                                       |
| `(0)数据库`       | `[2]计算机/(0)数据库系统/数据库系统概念.pdf`                                                        |
| `(0)数字信号`     | `[2]计算机/(0)数字信号/数字信号处理教程.pdf`                                                        |
| `(0)操作系统`     | `[2]计算机/(0)操作系统/操作系统导论.pdf`                                                            |
| `(1)计算理论`     | `[2]计算机/(1)计算理论/计算理论导引.pdf`<br>`[2]计算机/(1)计算理论/计算复杂性-现代方法.pdf`         |
| `(2)算法导论`     | `[2]计算机/(2)算法导论/算法导论（原书第3版）.pdf`<br>`[2]计算机/(2)算法导论/椭圆曲线密码学导论.pdf` |
| `(3-1)监督学习`   | `[2]计算机/(3)机器学习/统计学习方法-李航.pdf`                                                       |
| `(3-2)无监督学习` | `[2]计算机/(3)机器学习/统计学习方法-李航.pdf`                                                       |
| `(4)深度学习`     | `[2]计算机/(4)深度学习/深度学习 花书.pdf`                                                           |

## [3]物理

| 笔记目录      | 电子书                                       |
| ------------- | -------------------------------------------- |
| `(1)理论力学` | `[3]物理/(1)理论力学/经典力学的数学方法.pdf` |
| `(2)电动力学` | `[3]物理/(2)电动力学/电动力学导论.pdf`       |

## [4]化学

| 笔记目录             | 电子书                                                                                         |
| -------------------- | ---------------------------------------------------------------------------------------------- |
| `(1-1)无机化学-上册` | `[4]化学/(1)无机化学/无机化学-上册.pdf`<br>`[4]化学/(1)无机化学/无机化学-习题解答.pdf`         |
| `(1-2)无机化学-下册` | `[4]化学/(1)无机化学/无机化学-下册.pdf`                                                        |
| `(2-1)有机化学-上册` | `[4]化学/(2)有机化学/基础有机化学-上册.pdf`<br>`[4]化学/(2)有机化学/基础有机化学-习题解析.pdf` |
| `(2-2)有机化学-下册` | `[4]化学/(2)有机化学/基础有机化学-下册.pdf`                                                    |

## [5]生物

| 笔记文件           | 电子书                                                                                                                                 |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| `(1)普通生物学.md` | `[5]生物/普通生物学-陈阅增-第5版.pdf`<br>`[5]生物/普通生物学-陈阅增-第4版.pdf`<br>`[5]生物/普通生物学-陈阅增-第4版-笔记和课后习题.pdf` |
| `(2)细胞生物学.md` | `[5]生物/细胞生物学.pdf`                                                                                                               |
| `(3)分子生物学.md` | `[5]生物/分子生物学.pdf`                                                                                                               |
| `(4)生物信息学`    | `[5]生物/生物信息学.pdf`                                                                                                               |
```


## 助教的 VSCode 完整配置文件

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
