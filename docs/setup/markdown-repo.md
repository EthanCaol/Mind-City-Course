

# 助教的笔记仓库格式（供参考）

本文用助教自己的笔记仓库 Mind-City 作例子，说明笔记仓库可以怎样组织，下面按层级列出各个目录。格式不用照搬，按自己的学科和笔记风格调整即可。

## 1. 顶层目录

![Mind-City 仓库的顶层结构](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261023113434995.png)

顶层是四个目录、`.claude` 和两个文件，各自管一类内容：

| 名称        | 内容                           |
| ----------- | ------------------------------ |
| `.claude/`  | 技能文件，见 7                 |
| `Annex/`    | 零散文件与自写的小工具，见 2   |
| `Coursera/` | 学科笔记，见 3                 |
| `Paper/`    | 论文笔记，见 4                 |
| `Skill/`    | 环境配置备忘录，见 5           |
| `CLAUDE.md` | 仓库级提示词，见 6             |
| `README.md` | 笔记目录与电子书的对应表，见 6 |

------

## 2. Annex：杂项

![Annex 目录下的零散文件](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261021081704389.png)

不适合和笔记放在一起的文件放这里：图标、CSS 样式表、备份文件，以及两个自己写的 VSCode 扩展。

- `markdown-preview-scroll-toggle`：在编辑器标题栏放一个按钮，切换预览的滚动同步
- `markdown-preview-smiles`：把预览里 `&CCO&` 形式的文本渲染成分子结构式，对应第 6 节的 `CLAUDE.md` 里「SMILES 渲染」一节

分子结构在化学笔记里出现频繁，做成扩展之后，笔记里直接写 `&CCO&` 就能看到结构式，不必每次裁图、上传、回填链接。

------

## 3. Coursera：笔记的目录分级

![Coursera 下按学科划分的五个目录](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261021081747581.png)

一级目录按学科分，名字写成 `[N]学科`。`N` 只用来排序，方括号把编号和学科名隔开，展开后按数字顺序排列。

二级是课程，写成 `(N)课程名`；课程下每一章一个文件，写成 `(N)章节名.md`。

![抽象代数目录下的五个章节文件](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261021081812150.png)

`(3)抽象代数` 下是 `(0)数论` 到 `(4)域论` 五个章节文件。编号用半角圆括号，和课程目录的写法统一，展开目录时能看出哪一层是编号。

这些笔记的统一风格，由第 6 节的 `CLAUDE.md` 来约束。

------

## 4. Paper：论文笔记

![Paper 目录下的论文笔记与论文稿](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261021081846015.png)

论文笔记按 `年份-论文简称.md` 命名，年份在前，资源管理器里自动按时间排序。

仓库里存的是中文整理版，论文原文同步在 Zotero，不进仓库。

------

## 5. Skill：环境配置备忘录

![Skill 目录下的配置备忘录](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261021081956548.png)

装系统和配软件的过程记在这里，一个主题一篇：`Conda配置`、`Linux配置`、`Docker笔记`、`Zotero配置` 等。这些文件是重装环境时，用于复现的操作记录。

------

## 6. CLAUDE.md STYLES.md 与 README.md

![仓库根目录的 CLAUDE.md STYLES.md 与 README.md](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261023102859507.png)

下载链接（`CLAUDE.md`+`STYLES.md`+`README.md`+`skills/`）：<https://mind-city.com/downloads/markdown-repo.zip>

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

## 7. 笔记配套的 Skill 工具链

![.claude/skills 下的十一个技能目录](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261023113138666.png)

下载链接（`CLAUDE.md`+`STYLES.md`+`README.md`+`skills/`）：<https://mind-city.com/downloads/markdown-repo.zip>

| 技能                | 功能描述                                                                                                                                                                                         |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `debug-skill`       | 调试 skill 的流程: 起一个子 agent 按 debug 模式跑一遍真实任务, 收集它遇到的问题与思考过程, 记录到 skill-bug.md, 据此修 skill, 最后复查文风                                                       |
| `textbook-to-notes` | 从教材 PDF 生成 Coursera 笔记的总流程: 对齐风格, 渲染页面, 读图写笔记, 插图默认留空占位, 用户确认后再补图上传                                                                                    |
| `pdf-bookmark`      | 给扫描版教材 PDF 制作书签目录: 读图找目录页, 定每章的书页到 PDF 页偏移量, 从后往前核对, 写入书签                                                                                                 |
| `pdf-page-image`    | 把教材 PDF 的指定页渲染成读图用的页面图, 多页时纵向拼成一张, 同时输出每页在图中的像素区间清单                                                                                                    |
| `pdf-figure-crop`   | 按给定的像素矩形从页面图里裁出插图: 四周留白, 可选换算回源页用更高 dpi 重裁                                                                                                                      |
| `super-resolution`  | 用 SwinIR-L realSR GAN 对本地图片做 4 倍超分. 当用户要求放大图片, 超分, 提高分辨率, 让笔记里的图更清晰, 或需要处理低分辨率插图时使用                                                             |
| `coscmd`            | 用 coscmd 操作腾讯云 COS 图床 image-1379176255 ap-shanghai, 上传, 下载, 列出, 查看, 删除图片对象, 以及替换笔记图片链接的完整流程. 当需要上传图片, 更换图床链接, 清理桶内旧文件或查看桶内容时使用 |
| `push`              | 本笔记仓库 Mind-City 的提交约定: 当用户说 push / 提交 / commit / 推送, 或需要把改动写进 git 提交历史时使用                                                                                       |

------

### 7.1 从教材到笔记的链路

入口是 `textbook-to-notes`，其余技能由它按顺序调用：

1. 读仓库根目录 `README.md` 的映射表，确定教材与这篇笔记的输出路径。表里没有的教材直接问用户
2. 选定参考笔记，把风格整理进仓库根目录的 `STYLES.md`，再把这份文件交给每个写笔记的子 agent
3. 扫描版教材没有文字层，章节范围需要调用技能 `pdf-bookmark` 做一遍书签目录，之后按书签定位章节
4. 调用技能 `pdf-page-image` 把教材页渲染成页面图，读图写笔记正文
5. 用户确认正文之后，调用技能 `pdf-figure-crop` 按坐标从页面图裁出插图
6. 裁出的插图仍然模糊时，调用技能 `super-resolution` 做 4 倍超分
7. 接着调用技能 `coscmd` 上传插图，把公网链接回填进笔记
8. 最后调用技能 `push` 提交并推送

---

!!! todo "文档完成登记：完成本文全部流程后告知助教"

    <div class="read" id="read" data-page="markdown-repo">
      <div class="read__bar">
        <input id="read-id" class="read__input" type="text" inputmode="numeric" autocomplete="off" maxlength="11" placeholder="在这里输入你的学号">
        <button id="read-submit" type="button">我已读完</button>
      </div>
      <p class="read__note" id="read-note" hidden></p>
    </div>
