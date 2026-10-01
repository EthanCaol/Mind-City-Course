# Mind-City-Course

复旦《程序设计》课程的实验文档站，MkDocs Material 构建，上线在 https://mind-city.com。仓库 `github.com/EthanCaol/Mind-City-Course`（public，默认分支 `main`），里面的 `judge/` 是配套的在线评测后端。

本文件随这个 public 仓库一起发布 —— 不要往里写密钥、令牌、学生姓名学号这类东西。

## 背景

曹奕伦（GitHub `EthanCaol`），复旦大学计算机科学学院《程序设计》课程助教，负责上机实验课部分（主讲周水庚教授）。课程 2026 秋季学期（2026-09 – 2027-01），C 语言。

课程信息的**权威来源是本站的 `docs/index.md`**（给学生看的那份），下面是摘要：

- 实验课：星期三 8:00–9:40，逸夫楼 204、205
- 理论课：星期四 13:30–16:10，四教 H4204
- 成绩构成：编程作业 60% + 期中考 12% + 期末考 28%
- 编程作业在站点上提交，**不设截止日期**，期末前完成即可（见 `docs/homework-code/completion.md`）
- 教材《C语言程序设计（第3版）》（夏宽理、赵子正）

课程安排、成绩构成这类信息以 `docs/index.md` 为准 —— 要改就去改那里，不要改这里。

## 这台机器

腾讯云香港 VM，Ubuntu 26.04.1 LTS（`VM-0-8-ubuntu`），2 核 2G。内网 `10.5.0.8`，公网出口由云厂商 NAT 映射为 `43.161.225.186` —— **公网 IP 不在网卡上**。安全组要放行 80/443，本机看不到也改不了那层规则。

四条环境约束：

- **依赖直接装 conda `base`**，不要提议新建 venv 或 conda 环境。这台机器只跑这一个项目，隔离收益为零；venv 每次使用要先 `source`，conda 新环境会出现 ToS 未接受的报错。真要隔离，先说明具体理由。
- **`/tmp` 是 tmpfs，上限约 966M，且直接占用内存**（整机只有 1.9G）。MkDocs 构建产物、大文件下载都不要放进去 —— 写满时内核返回 `Quota exceeded (os error 122)`（EDQUOT），而调用方往往只会删掉重试，表现成无限循环重新下载。临时产物用 `/var/tmp` 或项目内目录。
- **sudo 用不了**。本机没有免密 sudo，而 Claude Code 的 bash 会话没有控制终端，`sudo` 一律报 `A terminal is required to authenticate`；`!` 前缀也一样无效。需要提权的步骤，把命令交给 Ethan 在**他自己的终端**里跑，再接着做无提权的验证。不要建议 `! sudo ...`，也不要让他把密码贴进对话。（`/usr/local/bin/isolate` 是 setuid 的，判题流程大部分不需要 root。）
- **本机没有浏览器**。视觉问题不要靠读 CSS 猜，让 Ethan 在出问题的页面控制台跑一行量实际数值，比如：

  ```js
  [...document.querySelector('#reads table').tHead.rows[0].cells].map(c => c.offsetWidth)
  ```

  表头 `110, 64, 44, 73` 对表体 `158, 70, 57, 57` 这种数字，可以直接看出问题。

## 仓库结构

```
.
├── mkdocs.yml         # 站点配置：主题、导航(nav)、Markdown 扩展、hooks
├── hooks/
│   └── revision_notice.py   # 构建钩子：把「最后更新」提示从页脚挪到标题下方
├── docs/
│   ├── index.md       # 首页
│   ├── material.md    # 课程资料：网站、书目、课件链接、每周课程安排
│   ├── plan.md        # 站点计划
│   ├── question/      # C 语言题库，按讲课顺序编号的 13 个知识点文件
│   ├── setup/         # 实验课文档：环境搭建与工具链，共 9 篇
│   ├── code/          # 正文用 snippet 引入的示例代码（hello.c、sum.c）
│   └── assets/
│       ├── fonts/         # Cascadia Code（代码字体，自托管，只含 latin 子集）
│       └── stylesheets/   # extra.css、fonts.css
├── judge/             # 在线评测后端
└── README.md          # 仓库页的简介
```

`site/`（构建产物）与 `.cache/`（`privacy` 插件抓取外部资源的缓存）都已 gitignore；页面里引用的 `assets/external/` 是构建时由 `privacy` 插件生成的，仓库里没有。

## 写一篇文档

**1. 在 `docs/` 下创建 Markdown 文件**。文件名用英文短横线风格，便于 URL 可读，例如 `docs/lesson-01-intro.md`。

**2. 在 `mkdocs.yml` 的 `nav` 中登记**：

```yaml
nav:
  - 首页: index.md
  - 基础篇:
      - 第一课: lesson-01-intro.md
      - 第二课: lesson-02-basics.md
```

未登记在 `nav` 中的文件仍会被构建（可通过 URL 访问），但不会出现在侧边栏里。

**3. 本地预览**：

```bash
cd ~/Mind-City-Course
mkdocs serve     # 打开 http://127.0.0.1:8000，保存后浏览器自动刷新
```

**4. 发布**：

```bash
git add -A && git commit -m "添加第一课" && git push
```

推送后约十几秒，https://mind-city.com 自动更新。构建用 `--strict`，存在坏链接或非法语法会失败，**此时线上保持上一版内容**，不会出现半成品页面。

打算「先写下来、回头再决定发不发」的内容，别放进 `docs/`、也别先挂导航 —— 放 MkDocs 够不着的地方（比如仓库根）。Ethan 对上线时机敏感，动 `docs/` 和 `mkdocs.yml` 之前先问。

### 可用的 Markdown 语法

`mkdocs.yml` 中已启用以下扩展：

````markdown
!!! note "提示框"
    支持 `note` / `tip` / `warning` / `danger` / `info` 等类型。

=== "标签页 A"

    用 `=== "标题"` 分页，读者可点击切换。

=== "标签页 B"

    ```python
    print("代码块自动高亮，右上角有复制按钮")
    ```

- [x] 已完成的待办
- [ ] 未完成的待办

| 表格 | 支持 |
|------|------|
| 对齐 | ✓ |

支持行内高亮 `#!python print("x")`、脚注[^1]、以及 :material-city: 图标。

[^1]: 这是脚注内容。

流程图用 `mermaid` 代码块（Material 内置支持，不需要装插件）：

```mermaid
graph LR
    A[Windows] --> B[WSL2]
    B --> C[Ubuntu]
    C --> D[gcc 编译]
```
````

标题会自动生成锚点，**中文标题保留中文锚点**（如 `#部署`），可直接分享该链接。

**图片点击放大**由 `mkdocs-glightbox` 提供，点击图片在浮层中放大，手机上查看实验截图时有用，语法就是标准 Markdown（`![](assets/images/lab-01-step-1.png)`）。

**每页底部显示最后更新时间**由 `mkdocs-git-revision-date-localized-plugin` 根据 git 记录生成「X 天前」。注意它读的是 git 历史 —— 新建的文件要先 commit 并 push，时间戳才会更新。

**中文全文搜索**：`lang: zh` 配合 jieba 分词，搜「镜像」这类词能命中词中的片段，而不是要求整句匹配。

## 写作规范

`docs/` 下的所有内容都按这一套走，题库和书面作业也一样。

### 语气

平实的说明文，像产品说明书：陈述事实和操作，对读者中性。标准是**可读性和准确性，不是生动**。

要避开的几类：

- 花哨动词 —— 撑着、带着你、长出来的、这条路线上的产物
- 装亲切／拟人 —— 能干这几件事、跟别的软件打架
- 拿术语摆谱 —— 撞上了的症状是
- 加戏和夸张 —— 钱直接打水漂、封号很凶、省事得多
- 煽动 —— 强烈建议、务必、保姆级、非常值得
- 写一句俏皮话再补一句解释

动词用最普通的那个：由…组成、演示、决定、换成、生成。不评价读者、不调侃、不表演共情、不用比喻和拟人。

### 排版

- **正文一律不用 `**…**` 加粗**。满屏加粗看着累，到处都是重点等于没有重点。列表项写 `- 名称：说明`；句子里的重点靠措辞，或用 admonition（`!!! warning` / `!!! tip` / `!!! info`）。唯一保留粗体的是每篇标题下面那行 `<p class="doc-meta">`，那是全站统一的模板。
- **各篇之间不加超链接**。正文里直接提文章名即可（「继续看那篇：VSCode 入门教程」）。理由是每篇要能单独发出去、单独改，而跨页相对链接在挪文件或改目录时会全部失效。同页锚点（`[4.3 更新软件列表](#43-更新软件列表)`）照常用。
- **不要用 `#` 当行号引用**：Python-Markdown 会把行首的 `#`（包括 `#include`、`#4`）解析成标题，`- #4 的关键` 会渲染成列表里套 h1。行号一律写中文「第 4 行」；表格的行列直接写数字。
- **空行是硬要求**：列表、表格、引用块、代码围栏前面必须有空行，否则会被吞进上一段 —— 页面上「四个选项挤成一行」就是这么来的。
- **代码块**缩进 4 格，函数之间、`#include` 之后留空行；代码内容不要动。
- **给元素起新 class 名之前，先和 Material 主题 CSS 对一遍**。`grid` 会撞上 `.md-typeset .grid`（卡片宫格，`display: grid` + `grid-template-columns`）：表格变成 Grid 容器后 `<thead>` 和 `<tbody>` 成了两个独立 grid item，各算各的列宽，表现是表头和数据错开一整列，而调表格自己的 CSS 完全没用。Material 有一批很通用的类名（`.grid`、`.cards`……），撞上不报错，只会把元素的布局模型整个换掉，症状离原因很远。体检做法：把 `extra.css` 里所有自定义类名抠出来逐个比对（跳过 `md-` 开头的）。

### 不主动点出的东西

- **会员／付费档位**：不写「会员功能要不要买」这类提示。
- **操作系统**：不写「Windows 和 macOS 都……」，不列 Android／iOS／App Store／Play 商店。默认 Win11，且不要特别声明。Ethan 自己要求写「在 Microsoft Store 里搜」时是例外，照着写。「系统自带的截图工具」这种不点名系统的说法可以留。

读者环境是统一的，写平台差异既啰嗦又把文档框死；付费档位提了只会让人犹豫要不要花钱。

## 题库与书面作业

`docs/question/`（13 篇，按主题编号 01–13）和 `docs/homework-book/chapter-N.md` 走同一套约定。

**措辞**：源材料是扫描件，**材料上的答案不可当标准答案**（可能来自考生作答，也可能是 OCR 出错丢字符 —— 例如 02 第 5 题的括号就是扫描丢的）。解析里一律写「材料上」或「材料上标出的」，**不要写「参考答案」**；材料缺答案、缺题面时如实说明材料状况，不要下「题目有瑕疵／命题疏漏」的结论。

**不编来源、不写备考腔**：不写口诀顺口溜，不替老师／命题人编动机（「是命题人最爱的送命陷阱」这类），不催促背诵（「务必背下来」）。课程 2026-09 才开课，凡「课上讲过／老师强调／我的笔记」都属编造。

解析里只写三类内容：材料上的原样（写明「材料上」）、编译器实测（写明 gcc 版本、必要时给命令）、推导（写明「按题意推导」）。实测数据和推导结论要完整保留，这是题库的主体。

**排版**：选项写成无序列表 `- A. 选项文字`，标记统一半角点加一个空格，不要写回「一行四个选项用全角空格分隔」的形式。标题格式 `### N · 题干简述 [高频考点]`，标记放最末。答案和解析用 `??? note "答案"` / `??? note "解析"`，块内缩进 4 格。表格第一列的表头不写「空」：编号列写「序号」，中文分类列（整型常量／实型常量／两者都不是 这类）把表头留空；列宽要跟着重排对齐。

**书面作业的来源**是教材《C语言程序设计（第3版）》（夏宽理、赵子正，中国铁道出版社）的扫描件 `docs/homework-book/book.pdf`。81MB、受版权保护，`.gitignore` 已排除，不进 public 仓库。扫描件每页是一张位图、没有文本层，不能抽文字，只能渲染成图再读。PDF 里嵌了书签（`pymupdf.open(pdf).get_toc()`），每个「习题」小节都有条目、条目页码是 1 基的 PDF 页，直接拿它定位，不用翻目录；习题的结束边界就是下一章的起始页。渲染用 `page.get_pixmap(dpi=150)`，糊的地方用 `clip=Rect(...)` + `Matrix(8, 8)` 裁图放大再读，不要猜字。

## 教材与今天的标准冲突时

教材是 C89/C90 时代的书。**凡是教材的写法、代码或结论与今天的 gcc 15 + C23 不一致，答案一律按 gcc 15 + C23 走**，同时把差异如实写出来。

学生交作业、判题机跑的都是 `-O2 -std=gnu23 -Wall`，教材当年的结论在今天的编译器下已经不成立，按教材写会给出学生实际编译不过的答案。

已知冲突点：隐式 int 在 C23 被删除（无返回类型的函数定义是硬错误）；`void main()` 只算老写法，答案给 `int main(void)`；常量词法判据引 C23（`0b` 前缀、`'` 数位分隔符）；未定义行为仍然只写「标准未定义 + 实测值」两段，不引申。

句式：「教材按 C89 的写法是 ……，C23 已经不允许（报错原文）。下面按 gcc 15.2.0 的 `-std=gnu23` 给出。」

## 站点与部署

Caddy（system 级）直接托管静态文件：`root /var/www/mind-city` + `file_server`。所以**线上内容来自 `mkdocs build` 的产物**，不是 `mkdocs serve`。线上不存在的路径返回 302 回首页（Caddy `handle_errors` 的行为），可据此确认请求确实落在静态文件上。

| 项 | 值 |
|---|---|
| 仓库 | `github.com/EthanCaol/Mind-City-Course`（public，默认分支 `main`） |
| 服务器部署目录 | `~/Mind-City-Course` |
| 公网地址 | `https://mind-city.com` |
| 网站根目录 | `/var/www/mind-city`（静态文件，属 `ethan`，部署脚本无需 root 即可写；Caddy 以 `caddy` 用户读） |
| 工具链 | conda **base** 环境，Python 3.14.7，`mkdocs` 位于 `~/miniconda3/bin/` |

### 自动部署链路

```
git push (main)
  → GitHub webhook，HMAC-SHA256 签名
  → https://mind-city.com/hooks/deploy   (Caddy 反代)
  → mind-city-webhook.service  监听 127.0.0.1:9000
  → ~/.local/bin/mind-city-deploy.sh
      ├─ git pull --ff-only origin main
      ├─ mkdocs build --strict -d ~/.cache/mind-city-staging
      └─ 成功才 rsync → /var/www/mind-city
  → Caddy file_server 立即可见
```

Webhook 配置在 GitHub 仓库的 Settings → Webhooks，也可用 `gh` 查看：

```bash
gh api repos/EthanCaol/Mind-City-Course/hooks \
  --jq '.[] | {id, url: .config.url, events, active}'
```

### 手动重新部署

正常情况不需要手动操作 —— push 就会触发。需要强制重建时直接跑部署脚本：

```bash
~/Mind-City-Course                     # 确认在部署目录
~/.local/bin/mind-city-deploy.sh       # 拉取 + 构建 + 发布
```

脚本是幂等的，重复执行安全。它自行处理 `flock` 锁，并发调用时后到的会直接跳过。

### 服务管理

systemd **用户级**服务（均设了 `linger`，断 SSH 不死、开机自启）：

```bash
systemctl --user status  mind-city-docs      # 本地写作预览，127.0.0.1:8000
systemctl --user status  mind-city-webhook   # 部署接收器，127.0.0.1:9000
systemctl --user status  mind-city-judge     # 在线评测判题后端，127.0.0.1:9100

systemctl --user restart mind-city-webhook
systemctl --user restart mind-city-judge

journalctl --user -u mind-city-webhook -f    # 实时看部署日志
journalctl --user -u mind-city-judge -f      # 实时看判题日志
```

`mind-city-docs` 跑的是 `mkdocs serve -a 0.0.0.0:8000`（unit 里就是 0.0.0.0），Caddy 并不代理它 —— 它只是写作时的热重载预览，公网由 Caddy 直接托管 `/var/www/mind-city` 的静态文件。

另有两个 system 级 / 定时任务：

```bash
systemctl is-active isolate                          # 判题沙箱依赖，必须 active
sudo systemctl enable --now isolate                  # 没起就拉起来 [sudo]

systemctl --user list-timers mind-city-backup.timer  # 备份，下次触发时间
systemctl --user start mind-city-backup.service      # 手动跑一次
journalctl --user -u mind-city-backup.service        # 看上次跑的结果
```

`mind-city-backup.timer` 每周一 04:00 把判题数据同步到 COS，细节见下面「在线评测 → 备份」。

**找不到的地址一律 302 回首页**，配置在 `/etc/caddy/Caddyfile` 的 `handle_errors` 里（题库改过名、以后章节再调整都会留下旧地址）。两个要点：用 `temporary` 而不是 `permanent`，301 会被浏览器长期缓存，将来真在那个路径放了页面老访客也回不来；必须 `not path /judge/*`，判题接口用 404 表达「没有这份提交」这类正常结果，被重定向后前端就拿不到提示了。

### 依赖（重建用）

若 `~/Mind-City-Course` 丢失，可重新克隆（**不要**把 `/var/www/mind-city` 当源码）：

```bash
git clone git@github.com:EthanCaol/Mind-City-Course.git ~/Mind-City-Course
~/.local/bin/mind-city-deploy.sh
```

依赖装在 conda base。**这些包一个都不能少** —— 缺任何一个都不会报错，只会静默降级：

```bash
pip install mkdocs-material                              # 主题本体
pip install jieba                                        # 中文搜索分词；缺了搜「镜像」搜不到
pip install mkdocs-glightbox                             # 图片点击放大
pip install mkdocs-git-revision-date-localized-plugin    # 页面底部「最后更新于 X 天前」
pip install mkdocs-open-in-new-tab                       # 站外链接新标签页打开
```

自查（注意 `mkdocs-open-in-new-tab` 装出来的模块名是 `open_in_new_tab`，不带 `mkdocs_` 前缀）：

```bash
python3 -c "import jieba, mkdocs_glightbox, mkdocs_git_revision_date_localized_plugin, open_in_new_tab; print('ok')"
```

### 字体与外部资源自托管

`privacy` 插件在构建时把所有外部资源抓下来本地化，学生**无需访问任何境外域名**：

```
assets/external/
├── fonts.googleapis.com/     44K   Roboto 样式表
├── fonts.gstatic.com/       808K   Roboto / Roboto Mono 字体（30 个 woff2）
├── unpkg.com/               3.5M   mermaid（懒加载，仅含流程图的页面才请求）
└── image-...myqcloud.com/   2.3M   教程里的 19 张截图
```

截图因而是本地副本，不受 COS 防盗链或欠费影响。

**构建时必须能联网**（服务器在香港，访问 Google/Cloudflare 无障碍）。首次构建约 7 秒，之后走 `.cache/plugin/privacy` 缓存，2 秒左右。`privacy` 插件是 Material 自带的，不需要单独 pip 安装。

**正文字体**：Material 默认的 Roboto 现由 `privacy` 自托管。Roboto 不含中文字形，中文始终由系统字体渲染（Windows 上通常是微软雅黑，macOS 是苹方）；自托管只是消除了那个被屏蔽的请求，避免首屏阻塞。

**代码字体 Cascadia Code** 自托管在 `docs/assets/fonts/`（3 个 woff2 共 100 KB，只含 latin 子集 —— 代码块是纯 ASCII，体积因此从 3 MB 降到 100 KB），由 `docs/assets/stylesheets/fonts.css` 定义 `@font-face` 并覆盖 `--md-code-font`。选它的理由是 Windows Terminal 和 VSCode 的默认等宽字体就是它。授权 SIL OFL 1.1，可自由分发。

**连字默认开着**：`!=` 显示为 `≠`，`>=` 显示为 `≥`，`=>` 显示为箭头。与 VSCode 一致所以保留默认。若认为一年级学生看 `≠` 会误以为要输入 `≠`，取消 `fonts.css` 末尾那段注释即可全局关闭。

### 已知问题

**一、删掉 `site_url` 会让 mermaid 变成每页加载 3.4 MB**。`privacy` 插件里有个特判：未配置 `site_url` 时它无法把 mermaid 的绝对 URL 改写成本地路径，改为直接加入 `extra_javascript`，**每个页面（含 404）都会加载 3.4 MB**，构建时间从 2 秒涨到 7 秒。配上 `site_url: https://mind-city.com/` 后恢复懒加载。**所以 `site_url` 这一行不能删** —— `sitemap.xml` 里的链接也依赖它。

**二、bash 代码块的命令名不着色**。这是 Pygments `BashLexer` 的固有行为：它只给 shell 语法结构着色，外部命令一律不着色（`sudo`、`apt`、`wsl`、`cat`、`grep` 都是白的），因为词法分析器无法判断 `nginx` 是命令还是文件名。Material 又把 `.n` 映射成正文色，所以 `sudo apt update && sudo apt upgrade -y` 渲染出来只有 `&&` 是淡灰。**换 `pygments_style` 无效**，真要改只能自定义 lexer。

**三、部分插件已倒向 ProperDocs，在 mkdocs 1.6.1 下不可用**。MkDocs 上游放弃 1.x 转向 2.x 后，社区把 1.x 分叉成了 ProperDocs，一些插件随之改了依赖，轻则拖进一整个 properdocs，重则构建失败。不可用的：`mkdocs-recently-updated-docs`（构建崩溃 `AttributeError: 'int' object has no attribute 'get'`）、`mkdocs-redirects`（依赖 `properdocs>=1.6.5`）、`mkdocs-code-validator`（同上）。

要用「最近更新」功能请自己写 —— 用 `git log` 生成列表，十行代码，不依赖任何插件。**URL 重定向直接写在 Caddy 里**，两行配置，同样不受生态变动影响。判断一个插件是否还有效，可以在装之前先看一眼依赖：

```bash
pip install --dry-run <插件名> 2>&1 | grep -i properdocs
```

### 排错

**确认线上是否为最新**

```bash
git -C ~/Mind-City-Course log --oneline -1                    # 部署目录的 HEAD
curl -sS https://mind-city.com/ | grep -c '<关键字>'           # 线上内容
stat -c '%y' /var/www/mind-city/index.html                    # 静态文件更新时间
```

**查看 GitHub 投递是否成功** —— 只看服务器日志会漏掉这类问题：

```bash
gh api repos/EthanCaol/Mind-City-Course/hooks/678947351/deliveries \
  --jq '.[] | "\(.delivered_at)  \(.event)  \(.status)  HTTP \(.status_code)"'
```

**常见问题**

| 症状 | 原因与处理 |
|---|---|
| 日志报 `mkdocs: command not found`（退出码 127） | systemd 的 `PATH` 不含 miniconda。部署脚本开头已显式 `PATH="$HOME/miniconda3/bin:$PATH"`，**改动脚本时不要删掉这行**。交互式 shell 里因为 conda base 激活着，不会复现 |
| GitHub 投递显示 `FAILED` / `context deadline exceeded` | **GitHub webhook 超时只有 10 秒**。接收器必须验签后立刻返回（现为 202），部署丢到后台线程跑。**不要把它改回同步执行** —— 失败的投递不会自动重试，push 会静默丢失 |
| 构建失败但站点还在 | 预期行为。脚本先构建到 staging，成功才同步，构建失败时线上保持旧版 |
| 日志报 `Cannot fast-forward to multiple branches`（退出码 128） | 部署的 `git pull` 和**别人在同一个仓库里跑的 `git fetch`/`git pull` 撞了**，两个进程同时写 `.git/FETCH_HEAD`，同一条 `main` 被写了两遍，`merge --ff-only` 见到多个 head 就拒绝。本地 `git pull` 看起来一切正常，重跑一次部署脚本即可。**不要在可能触发部署的时间窗口里手动对这个仓库跑 fetch/pull** |
| 中文标题锚点变成 `_1`/`_2` | `mkdocs.yml` 的 `toc.slugify` 配置被改动了。待修：`toc` 下加 `slugify: !!python/name:pymdownx.slugs.uslugify` |

## 在线评测（judge/）

作业页上的代码编辑框：学生粘代码 → 服务器用 isolate 沙箱编译运行 → 把每个测试点的输入、期望输出、实际输出都告诉他。全部测试点通过，「作业完成情况」页就显示绿勾。

同一个服务还提供**阅读登记**：实验课文档末尾让学生填学号点一下「我已读完」，`docs/reading.md` 按「行是学生、列是文档」汇总，助教据此判断文档更新节奏和学生是否能跟上进度。不计分。接口和表结构见 `judge/README.md` 的「阅读登记」一节。

日常使用和排错见 `judge/README.md`；下面记的是服务器上的配置过程与关键取舍。

### 组件

| 组件 | 位置 |
|---|---|
| 前端 | 作业页里的 `<div id="judge" data-homework="...">` + `docs/assets/javascripts/judge.js`（全站加载，找不到挂载点就退出） |
| 判题后端 | `judge/` 目录（公开仓库），systemd 用户服务 `mind-city-judge`，监听 `127.0.0.1:9100` |
| 沙箱 | `isolate` 2.7，源码编译装在 `/usr/local`；**system 级 `isolate.service` 必须常驻** |
| 数据 | `judge/data/`（本机目录，被外层仓库 gitignore）；花名册的权威副本在 COS 上 |

### 安装 isolate（一次性）

isolate 不在 apt 源里，要源码编译。标 `[sudo]` 的必须在自己的终端执行。

```bash
# 1. 依赖  [sudo]
#    本机 build-essential / pkg-config / libcap-dev / libsystemd-dev / git 已有，
#    实际只补装了 libseccomp-dev —— v2.7 起必需，缺了报 seccomp.h not found。
sudo apt install -y build-essential pkg-config libcap-dev libsystemd-dev libseccomp-dev git

# 2. 编译（不需要 sudo）
git clone https://github.com/ioi/isolate.git ~/isolate
cd ~/isolate && git checkout v2.7 && make isolate

# 3. 安装  [sudo]
sudo make install

# 4. 建 isolate 用户  [sudo]   ← 漏了这步 isolate 直接起不来
#    config.c 里 subid_user=isolate 找不到用户就是 die()，没有回退分支。
#    必须是普通用户（不能加 --system）：adduser 只给普通用户分配 subuid 段，
#    而 config.c 拿这个段给每个 box 分独立 uid。
sudo addgroup --quiet --system isolate
sudo adduser --quiet --disabled-login --ingroup isolate \
  --home /nonexistent --no-create-home --shell /bin/false --comment "" isolate

# 5. 启用 cgroup 委派守护进程  [sudo]
sudo systemctl daemon-reload
sudo systemctl enable --now isolate
```

unit 由 `make install` 装到 `/usr/local/lib/systemd/system/`（这个目录本来就在 systemd 的搜索路径里，**不需要** cp 到 `/etc/systemd/system`）。编译用的源码放在 `~/isolate`，运行时用不到，可以删。

自检：

```bash
isolate --version           # 应输出 2.7
isolate --print-cg-root     # 退出码 0 才算就绪，见下面「注意点 ②」
```

`isolate-check-environment` 会报几项 FAIL/CAUTION（swap enabled、SMT enabled、ASLR enabled、THP），**都不是阻断项**，别去改 —— 尤其不要把 SMT 关掉，本机只有 2 核，关了判题吞吐减半。它退出码是 1，别拿退出码当失败判据。

### 数据

`judge/data/` 是本机目录，学生源码判完即从数据库删除，不落盘。数据本身两样：

| 文件 | 说明 |
|---|---|
| `judge.sqlite3` | 权威数据源：结论、通过数、逐测试点判定。WAL 模式 |
| `roster.csv` | 花名册。**权威副本在 COS 桶根**，服务启动时拉一次覆盖本地 |

`judge/data/` 被外层公开仓库 gitignore。这是硬要求：里面有学生姓名学号；而且数据一旦提交进外层仓库，本地就有未推送的 commit，部署脚本的 `git pull --ff-only` 会失败，**整个文档站静默停止更新**。

改名单：改好本地那份 → `coscmd upload` 到桶根 → 重启判题服务。完整步骤见 `judge/README.md`（含必须带 `x-cos-acl: private` 的原因）。

### 备份

`mind-city-backup.timer` 每周一 04:00 跑 `judge/tools/backup_to_cos.py`，把**数据库快照和 `roster.csv` 覆盖式**传到 COS 的 `backup/` 前缀下。这是助教不用 git、不用装 sqlite3 就能直接下载的那份。两个要点：

- **每个对象都带 `x-cos-acl: private`。** 那个桶是公开读的（站点的图挂在上面），漏了这个头就等于把学生姓名学号暴露在公网上。传完拿不带签名的 curl 验一下，应当 403：

  ```bash
  curl -sI https://image-1379176255.cos.ap-shanghai.myqcloud.com/backup/roster.csv
  ```

- **数据库不能直接 cp。** 库是 WAL 模式，主文件可能只有几十 KB，直接拷主文件拿到的未必是全量。脚本走 sqlite3 的在线备份 API，源库同时在写也能拿到一致的快照；想确认传对了，比较两边 `SELECT COUNT(*) FROM submissions` 的行数即可。

### 验证

```bash
python3 judge/tools/selftest_logic.py   # 纯逻辑，不需要沙箱、不需要 sudo
python3 judge/tools/selfcheck.py        # 真沙箱：七种判题结论各造一个程序
curl -s https://mind-city.com/judge/api/health
```

`selfcheck.py` 需要 `isolate.service` 在跑，否则开头就会提示并退出码 2。

### 三个注意点

**① `--mem` 必须取 `--cg-mem` 的 2 倍，不能同值。**

`RLIMIT_AS >= RSS` 恒成立，两者同值时 `RLIMIT_AS` 必然先触发：程序一次 `malloc(400MB)` 在 256 MB 限制下直接返回 NULL，若它打印错误信息退出 1，就会被判成 **RE（运行错误）而不是 MLE**，而 cgroup 的 `cg-mem` 停在 6.7 MB，根本达不到 MLE 判据。

实测（同一个只申请 400 MB 的程序）：

| `--mem` / `--cg-mem` | 结论 | meta 里的 `cg-mem` |
|---|---|---|
| 256 MB / 256 MB（同值） | RE ← 错 | 6784 KB |
| 512 MB / 256 MB（2 倍） | MLE ← 对 | 262144 KB |

测这类程序时**必须让编译器无法消除内存操作**：`memset` 之后再也不读那块内存的话，`-O2` 会把整个 memset 当死代码删掉，程序根本没有访问那块内存，测出来的结果不能反映实际内存占用。

**② `isolate.service` 停掉后 `--cg` 失效，但报错信息会误导。**

`/run/isolate/cgroup` 这个文件**不会**跟着清理，它留着一条已经不存在的路径，所以报错看起来像配置写错了，实际只是服务没起。判题层的 `judge_ready()` 就是为此写的：读那个文件之后还要确认路径下真的有 `cgroup.procs`。

**③ 关掉 Nagle，否则每个响应多花 40 ms。**

`http.server` 的 `wfile` 是无缓冲的，响应头和响应体分两次 write，Nagle 会推迟发送第二个包以等待对端的 ACK，而客户端此时在延迟确认。实测首字节从 56 ms 降到 14 ms。一个 `disable_nagle_algorithm = True` 就够（`StreamRequestHandler` 现成的开关）。

### 接口改动要两边一起换

`judge.js` 是静态文件，push 后十几秒自动部署；`mind-city-judge` 要 `systemctl --user restart` 才加载新代码，两边的接口结构必须同时换（新前端按新字段读、旧服务返回旧字段，错开的那段时间页面直接报错）。顺序是**先 push、确认线上文件已出现新代码，再重启服务**：推在前，构建失败时站点和接口都还是旧的，状态一致；重启在前，构建一旦失败就停在「新接口 + 旧前端」的不匹配组合上，而且不会自动恢复。

## 外部接口备忘

**B 站封面抓取**：先取 buvid —— `GET https://api.bilibili.com/x/frontend/finger/spi` → `data.b_3` / `data.b_4`，分别当 `buvid3` / `buvid4` cookie；再 `GET https://api.bilibili.com/x/web-interface/wbi/view?bvid=<BV>` 并带上该 cookie，封面在 `data.pic`。不带 cookie 走老的 `/x/web-interface/view` 会被风控拦截为 HTTP 412（返回一页「出错啦」HTML）；换 `wbi/view` 且不加 `w_rid` 签名也能通。付费课程走 `GET https://api.bilibili.com/pugv/view/web/season?ep_id=<ep>`，封面在 `data.episodes[].cover`。`i*.hdslb.com` / `archive.biliimg.com` 有防盗链：请求带任何别站 Referer 都是 403，只有不带 Referer（`curl -H 'Referer;'`）才能下载完整图片。所以封面不能直接热链进文档，需要先下载再上传到腾讯云 COS。

**公有代码执行 API**（调研过，最终没用上）：只有 **ce.judge0.com** 现实可用 —— 无需认证，GCC 14.1.0 / Clang 18 / Clang 19 可选，连发 12 次零限流，平均 2.92s/次；但对 python-urllib 的默认 User-Agent 返回 403，必须自设 UA 头。**必须用批量接口** `/submissions/batch`（上限 20）：单发约 2.9s/点，批量 10 个测试点共 4.58s（0.46s/点），漏算 batch 会严重高估成本。执行限制：CPU 默认 5s / 最大 20s，内存默认 256MB / 最大 2GB，墙钟默认 10s / 最大 30s，禁网，`wait=true` 被忽略必须轮询。

其余都不可用：Piston（emkc.org）已转白名单制，返回 401；Wandbox 的 gcc 只有 7.5/8.4/9.3，版本过低；glot.io DNS 不解析；paiza.io 401。关键结论：自建 Judge0 CE 与公有实例是同一套 API，所以按 Judge0 API 写网站、先连公有实例，需要时自建只改一个 base URL。

## 注意事项

- **不要升级 MkDocs 2.0**。Material 官方公告称 2.0 会移除插件系统、主题覆盖全部失效、无迁移路径。当前锁定 mkdocs 1.6.1 + mkdocs-material 9.7.7（conda base，Python 3.14.7）。
- **不要用 `gh api -f` 传布尔字段**，`-f` 一律按字符串发送，会报 422；布尔要用 `-F`。
- webhook 密钥位于 `~/.config/mind-city/webhook-secret`（权限 700/600），**不要提交进仓库**。
- **本地有未推送的 commit 会让 `git pull --ff-only` 失败，整个文档站静默停止更新。**

## 协作偏好

**先说结论**。Ethan 问「放哪比较好」这类问题时，要的是落点，不是权衡分析 —— 复述背景和铺陈选项是在讲他已经知道的东西（他是助教，课程怎么排比助手清楚）。结论放第一句，理由压到两三句；没有分歧就别论证。需要拍板时只问一个决定，不要一次抛多个维度。

**代码要精简，不要防御性设计**。写新模块前先问「这条分支现实中会发生吗」，不会就不写。错误提示只要一条、能照着改就行，不要为每种失败模式定制文案。被要求简化时直接砍，不要辩护。这是面向学生的教学工具，输入是学生的 C 作业，取值范围很窄；为想象中的边界写代码和测试，既增加阅读负担，也掩盖了真正要表达的那条规则。

具体尺度：学号解析只要一条规则 ——「第一行 `//` 之后 strip 掉空格，必须正好 11 位数字」，不要跨行块注释、全角数字归一化、多学号冲突检测，也不要给每种失败模式单独写文案。输出比对只做归一化（CRLF、行末空白、末尾空行），不提供浮点容差、token 模式、忽略大小写这类可配置项。测试不要覆盖不会发生的输入（12 位学号、BOM、未闭合字符串字面量）。

## 提交方式

1. 触发：用户说 `push`，若无其他疑问，直接提交到远程仓库
2. 范围：只提交用户点名的内容；临时文件、草稿、临时图片一律先列出问过再动，不主动 `git add`
3. 格式：统一格式 `[26/9/29 0:14] 中文一句话简要概括`
   - 方括号内是提交时刻，**年/月/日 时:分 四段一个都不能少**，年份是 `26` 这种两位缩写，漏掉年份（写成 `[10/2 2:30]`）就是错的
   - 除分钟补两位外都不补零：`0:14`、`9/29 0:14`、`2:30` 对，`00:14`、`09/29`、`02:30` 错
   - 时间别自己拼格式串，直接用 `$(date '+%y/%-m/%-d %-H:%M')` 取本地时间
   - 概述压到一句话；压不下时空一行再补正文
4. 执行：一条命令走完 add/commit/push，命令要短，不先单独跑 status/diff/date 再回来确认
