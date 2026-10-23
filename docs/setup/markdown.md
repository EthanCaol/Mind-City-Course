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

- 仓库根目录的 `CLAUDE.md`：在这个仓库里启动 Claude Code 时自动读入，里面是这个仓库的长期约定，完整内容详见 7.7 节
- `.claude/skills/` 下的技能：每个技能一个目录，里面放 `SKILL.md`，敲 `/` 加技能名触发

---

### 6.1 提交用的技能

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


## 助教的 VSCode 完整配置文件

```json title="settings.json"
--8<-- "quote/settings.json"
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
