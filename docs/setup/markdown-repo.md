

# 助教的笔记仓库格式（供参考）

本文用助教自己的笔记仓库 Mind-City 作例子，说明笔记仓库可以怎样组织，下面按层级列出各个目录。格式不用照搬，按自己的学科和笔记风格调整即可。

## 1. 顶层目录

![Mind-City 仓库的顶层结构](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261021081517146.png)

顶层是四个目录、`.claude` 和两个文件，各自管一类内容：

| 名称        | 内容                           |
| ----------- | ------------------------------ |
| `.claude/`  | 技能文件，见 2                 |
| `Annex/`    | 零散文件与自写的小工具，见 3   |
| `Coursera/` | 学科笔记，见 4                 |
| `Paper/`    | 论文笔记，见 5                 |
| `Skill/`    | 环境配置备忘录，见 6           |
| `CLAUDE.md` | 仓库级提示词，见 7             |
| `README.md` | 笔记目录与电子书的对应表，见 7 |

------

## 2. .claude/skills：仓库级的Agent技能

![.claude/skills 下的十一个技能目录](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261021081632389.png)

技能一个目录一个 `SKILL.md`，按用途命名。仓库里现在有 11 个，分两类：

| 类别         | 技能                                                             | 触发方式                    |
| ------------ | ---------------------------------------------------------------- | --------------------------- |
| 独立任务     | `push`、`pdf-bookmark`、`super-resolution`、`textbook-to-notes`  | 出现在 `/` 列表里，手动调用 |
| 流程中的一步 | `pdf-page-image`、`note-writing`、`pdf-figure-crop`、`coscmd` 等 | 由 Claude 在流程中间调用    |

------

## 3. Annex：杂项

![Annex 目录下的零散文件](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261021081704389.png)

不适合和笔记放在一起的文件放这里：图标、CSS 样式表、备份文件，以及两个自己写的 VSCode 扩展。

- `markdown-preview-scroll-toggle`：在编辑器标题栏放一个按钮，切换预览的滚动同步
- `markdown-preview-smiles`：把预览里 `&CCO&` 形式的文本渲染成分子结构式，对应第 7 节的 `CLAUDE.md` 里「SMILES 渲染」一节

分子结构在化学笔记里出现频繁，做成扩展之后，笔记里直接写 `&CCO&` 就能看到结构式，不必每次裁图、上传、回填链接。

------

## 4. Coursera：笔记的目录分级

![Coursera 下按学科划分的五个目录](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261021081747581.png)

一级目录按学科分，名字写成 `[N]学科`。`N` 只用来排序，方括号把编号和学科名隔开，展开后按数字顺序排列。

二级是课程，写成 `(N)课程名`；课程下每一章一个文件，写成 `(N)章节名.md`。

![抽象代数目录下的五个章节文件](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261021081812150.png)

`(3)抽象代数` 下是 `(0)数论` 到 `(4)域论` 五个章节文件。编号用半角圆括号，和课程目录的写法统一，展开目录时能看出哪一层是编号。

这些笔记的统一风格，由第 7 节的 `CLAUDE.md` 来约束。

------

## 5. Paper：论文笔记

![Paper 目录下的论文笔记与论文稿](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261021081846015.png)

论文笔记按 `年份-论文简称.md` 命名，年份在前，资源管理器里自动按时间排序。

仓库里存的是中文整理版，论文原文同步在 Zotero，不进仓库。

------

## 6. Skill：环境配置备忘录

![Skill 目录下的配置备忘录](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261021081956548.png)

装系统和配软件的过程记在这里，一个主题一篇：`Conda配置`、`Linux配置`、`Docker笔记`、`Zotero配置` 等。这些文件是重装环境时，用于复现的操作记录。

------

## 7. CLAUDE.md STYLES.md 与 README.md

![仓库根目录的 CLAUDE.md STYLES.md 与 README.md](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261023102859507.png)

三个文件分工不同：

- `CLAUDE.md` 是仓库级提示词，写长期约定：仓库结构、技能的放置、文风、标点与断句、文档结构、公式渲染。
- `STYLES.md` 决定文件的形态：节标题层级、结构、标点、公式、插图的写法。用词与语气按 `CLAUDE.md` 的「文风」一节，两份文件的内容不重叠。
- `README.md` 是一张对应表：左边是笔记目录，右边是对应的电子书路径

````markdown title="CLAUDE.md"
--8<-- "quote/markdown-repo/CLAUDE.md"
````

<br><br><br>

````markdown title="STYLES.md"
--8<-- "quote/markdown-repo/STYLES.md"
````

<br><br><br>

````markdown title="README.md"
--8<-- "quote/markdown-repo/README.md"
````

## 8. 笔记配套的 Skill 工具链

技能目录里与写笔记相关的是下面 8 个，按用途分三组：一条把教材 PDF 变成笔记的链路，两个维护仓库的技能，一个调试技能的工具。

这 8 个技能的 `SKILL.md` 与随附脚本打包在 <https://mind-city.com/downloads/markdown-repo-skills.zip>，解压得到 `markdown-repo-skills/` 目录，放进 `.claude/skills/` 即可使用。

| 技能                | 作用                                                                                  |
| ------------------- | ------------------------------------------------------------------------------------- |
| `textbook-to-notes` | 从教材 PDF 到笔记的总流程：定目标文件、对齐风格、读图写笔记、补图                     |
| `pdf-page-image`    | 把 PDF 的指定页渲染成读图用的页面图，多页可以纵向拼成一张，同时给出各页在图中占的区间 |
| `pdf-bookmark`      | 给扫描版教材做书签目录：读目录页、定每章书页到 PDF 页的偏移量、逐章核对、写入书签     |
| `pdf-figure-crop`   | 按像素矩形从页面图裁出插图，四周留白，也可以换算回源页用更高的 dpi 重新裁             |
| `coscmd`            | 操作腾讯云 COS 图床：上传、下载、列出、删除对象，把笔记里的图片换成新链接             |
| `super-resolution`  | 用 SwinIR-L realSR GAN 对本地图片做 4 倍超分                                          |
| `push`              | 本仓库的提交约定                                                                      |
| `debug-skill`       | 用一个子 agent 实际执行一遍待调试的技能，收集它遇到的问题后修改                       |

------

### 8.1 从教材到笔记的链路

入口是 `textbook-to-notes`，其余技能由它按顺序调用：

1. 读仓库根目录 `README.md` 的映射表，确定教材与这篇笔记的输出路径。表里没有的教材直接问用户
2. 选定参考笔记，把风格整理进仓库根目录的 `STYLES.md`，再把这份文件交给每个写笔记的子 agent
3. `pdf-page-image` 把教材页渲染成页面图，读图写笔记。插图先留占位，不和正文一起做
4. 用户确认正文之后，`pdf-figure-crop` 按坐标从页面图裁出插图
5. `coscmd` 上传插图，把公网链接回填进笔记

扫描版教材没有文字层，章节范围依赖 `pdf-bookmark` 单独做一遍书签目录。做完之后按书签定位章节，不必逐页翻找。

------

### 8.2 SKILL.md 与脚本原文

下面依次是各技能目录下 `SKILL.md` 与随附脚本的内容。

````markdown title="textbook-to-notes/SKILL.md"
--8<-- "quote/markdown-repo/skills/textbook-to-notes/SKILL.md"
````

<br><br><br>

````markdown title="pdf-page-image/SKILL.md"
--8<-- "quote/markdown-repo/skills/pdf-page-image/SKILL.md"
````

````python title="pdf-page-image/scripts/render.py"
--8<-- "quote/markdown-repo/skills/pdf-page-image/scripts/render.py"
````

<br><br><br>

````markdown title="pdf-bookmark/SKILL.md"
--8<-- "quote/markdown-repo/skills/pdf-bookmark/SKILL.md"
````

````python title="pdf-bookmark/scripts/bookmark.py"
--8<-- "quote/markdown-repo/skills/pdf-bookmark/scripts/bookmark.py"
````

<br><br><br>

````markdown title="pdf-figure-crop/SKILL.md"
--8<-- "quote/markdown-repo/skills/pdf-figure-crop/SKILL.md"
````

````python title="pdf-figure-crop/scripts/crop.py"
--8<-- "quote/markdown-repo/skills/pdf-figure-crop/scripts/crop.py"
````

<br><br><br>

````markdown title="coscmd/SKILL.md"
--8<-- "quote/markdown-repo/skills/coscmd/SKILL.md"
````

<br><br><br>

````markdown title="super-resolution/SKILL.md"
--8<-- "quote/markdown-repo/skills/super-resolution/SKILL.md"
````

````python title="super-resolution/scripts/sr.py"
--8<-- "quote/markdown-repo/skills/super-resolution/scripts/sr.py"
````

<br><br><br>

````markdown title="push/SKILL.md"
--8<-- "quote/markdown-repo/skills/push/SKILL.md"
````

<br><br><br>

````markdown title="debug-skill/SKILL.md"
--8<-- "quote/markdown-repo/skills/debug-skill/SKILL.md"
````
