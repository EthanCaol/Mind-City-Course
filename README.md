# Mind-City-Course

课程文档站点，基于 [MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)。

在线访问：<https://mind-city.com>

---

# 第一部分：如何添加新文档页面

## 目录结构

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
└── README.md          # 本文件，仅面向仓库，不会出现在网站上
```

`site/`（构建产物）与 `.cache/`（`privacy` 插件抓取外部资源的缓存）都已 gitignore；
页面里引用的 `assets/external/` 是构建时由 `privacy` 插件生成的，仓库里没有。

## 新增页面

**1. 在 `docs/` 下创建 Markdown 文件**

文件名用英文短横线风格，便于 URL 可读，例如 `docs/lesson-01-intro.md`。

```markdown
# 第一课：课程简介

正文内容。
```

**2. 在 `mkdocs.yml` 的 `nav` 中登记**

```yaml
nav:
  - 首页: index.md
  - 第一课: lesson-01-intro.md
```

`nav` 支持嵌套，用二级缩进即可生成侧边栏分组：

```yaml
nav:
  - 首页: index.md
  - 基础篇:
      - 第一课: lesson-01-intro.md
      - 第二课: lesson-02-basics.md
  - 进阶篇:
      - 第一课: advanced-01.md
```

> 未登记在 `nav` 中的文件仍会被构建（可通过 URL 访问），但不会出现在侧边栏里。

**3. 本地预览**

```bash
cd ~/Mind-City-Course
mkdocs serve
```

打开 <http://127.0.0.1:8000>，保存 Markdown 后浏览器自动刷新。

**4. 发布**

```bash
git add -A && git commit -m "添加第一课" && git push
```

推送后约十几秒，<https://mind-city.com> 自动更新，无需任何手动操作。

> 构建使用 `--strict` 模式：存在坏链接或非法语法会导致构建失败，**此时线上保持上一版内容**，不会出现半成品页面。构建失败的原因见本文第二部分的排错小节。

## 可用的 Markdown 语法

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

**图片点击放大**：由 `mkdocs-glightbox` 提供，点击图片会在浮层中放大查看，手机上看实验截图尤其方便。语法就是标准 Markdown：

```markdown
![](assets/images/lab-01-step-1.png)
```

**每页底部显示最后更新时间**：由 `mkdocs-git-revision-date-localized-plugin` 根据 git 记录生成「X 天前」，学生能一眼判断内容是否对应当前学期。**注意它读的是 git 历史**——新建的文件要先 commit 并 push，时间戳才会更新。

**中文全文搜索**：`lang: zh` 配合 jieba 分词，搜「镜像」这类词能命中词中的片段，而不是要求整句匹配。

---

# 第二部分：部署流程（供 Agent 参考）

本节描述站点在服务器上的实际运行方式，用于排查问题或手动重新部署。

## 环境

| 项 | 值 |
|---|---|
| 仓库 | `github.com/EthanCaol/Mind-City-Course`（public，默认分支 `main`） |
| 服务器部署目录 | `~/Mind-City-Course` |
| 公网地址 | `https://mind-city.com` |
| 网站根目录 | `/var/www/mind-city`（静态文件） |
| 工具链 | conda **base** 环境，Python 3.14.7，`mkdocs` 位于 `~/miniconda3/bin/` |

## 自动部署链路

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

## 手动重新部署

正常情况不需要手动操作——push 就会触发。需要强制重建时，直接跑部署脚本：

```bash
~/Mind-City-Course                     # 确认在部署目录
~/.local/bin/mind-city-deploy.sh       # 拉取 + 构建 + 发布
```

脚本是幂等的，重复执行安全。它会自行处理 `flock` 锁，并发调用时后到的会直接跳过。

## 服务管理

三个 **systemd 用户级服务**（均设了 `linger`，断 SSH 不死、开机自启）：

```bash
systemctl --user status  mind-city-docs      # 本地写作预览，127.0.0.1:8000
systemctl --user status  mind-city-webhook   # 部署接收器，127.0.0.1:9000
systemctl --user status  mind-city-judge     # 在线评测判题后端，127.0.0.1:9100

systemctl --user restart mind-city-webhook
systemctl --user restart mind-city-judge

journalctl --user -u mind-city-webhook -f    # 实时看部署日志
journalctl --user -u mind-city-judge -f      # 实时看判题日志
```

另有一个**定时任务** `mind-city-backup.timer`，每周一 04:00 把判题数据同步到 COS
（细节见「在线评测 → 备份」）：

```bash
systemctl --user list-timers mind-city-backup.timer   # 下次触发时间
systemctl --user start mind-city-backup.service       # 手动跑一次
journalctl --user -u mind-city-backup.service         # 看上次跑的结果
```

`mind-city-docs` 只绑本地回环，**不对公网提供内容**，仅供在服务器上写文档时预览。公网由 Caddy 直接托管 `/var/www/mind-city` 的静态文件。

**找不到的地址一律 302 回首页**，配置在 `/etc/caddy/Caddyfile` 的 `handle_errors` 里
（题库改过名、以后章节再调整都会留下旧地址）。两个要点：用 `temporary` 而不是
`permanent`，301 会被浏览器长期缓存，将来真在那个路径放了页面老访客也回不来；
必须 `not path /judge/*`，判题接口用 404 表达「没有这份提交」这类正常结果，被重定向掉
前端就拿不到提示了。

另外还有一个 **system 级服务** `isolate.service`，是在线评测的沙箱依赖，**必须常驻**：

```bash
systemctl is-active isolate                  # 应为 active
sudo systemctl enable --now isolate          # 没起就拉起来
```

## 在线评测（OJ）

作业页上的代码编辑框：学生粘代码 → 服务器用 isolate 沙箱编译运行 → 把每个测试点的
输入、期望输出、实际输出都告诉他。全部测试点通过，「作业完成情况」页就点亮绿勾。

同一个服务还提供**阅读登记**：实验课文档末尾让学生填学号点一下「我已读完」，
`docs/reading.md` 按「行是学生、列是文档」汇总，助教据此判断文档更新节奏和学生跟不跟得上。
不计分。接口和表结构见 `judge/README.md` 的「阅读登记」一节。

日常使用和排错见 `judge/README.md`，下面只记服务器上的配置过程。

### 组件

| 组件 | 位置 |
|---|---|
| 前端 | 作业页里的 `<div id="judge" data-homework="...">` + `docs/assets/javascripts/judge.js` |
| 判题后端 | `judge/` 目录（公开仓库），systemd 用户服务 `mind-city-judge`，监听 `127.0.0.1:9100` |
| 沙箱 | `isolate` 2.7，源码编译装在 `/usr/local` |
| 数据 | `judge/data/`，独立的 **private** 仓库 `EthanCaol/Mind-City-Course-OJ` |

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

unit 由 `make install` 装到 `/usr/local/lib/systemd/system/`（这个目录本来就在
systemd 的搜索路径里，**不需要** cp 到 `/etc/systemd/system`）。

自检：

```bash
isolate --version           # 应输出 2.7
isolate --print-cg-root     # 退出码 0 才算就绪，见下面「坑 ②」
```

`isolate-check-environment` 会报几项 FAIL/CAUTION（swap enabled、SMT enabled、
ASLR enabled、THP），**都不是阻断项**，别去改 —— 尤其不要把 SMT 关掉，本机只有
2 核，关了判题吞吐减半。它退出码是 1，别拿退出码当失败判据。

编译用的源码放在 `~/isolate`，运行时用不到，可以删。

### 数据仓库

`judge/data/` 是一个独立的 private 仓库，**只有 `roster.csv` 和 `grades/<作业>.csv`**
—— 学生源码判完即从数据库抹掉，一行都不落盘，也从不写进 git。

```bash
gh repo create EthanCaol/Mind-City-Course-OJ --private
```

它同时被外层公开仓库 gitignore。这是硬要求：里面有学生姓名学号；而且数据一旦提交
进外层仓库，本地就有未推送的 commit，部署脚本的 `git pull --ff-only` 会失败，
**整个文档站静默停止更新**。

### 备份

`mind-city-backup.timer` 每周一 04:00 跑 `judge/tools/backup_to_cos.py`，把**数据库快照
和 `roster.csv` 覆盖式**传到 COS 的 `backup/` 前缀下（`grades/` 平时是空的就跳过）。
这是除了数据仓库之外的第二份异地副本，也是助教不用 git 就能直接下载的那份。

两个要点：

- **每个对象都带 `x-cos-acl: private`。** 那个桶是公开读的（站点的图挂在上面），漏了
  这个头就等于把学生姓名学号摊在公网上。传完拿不带签名的 curl 验一下，应当 403：

  ```bash
  curl -sI https://image-1379176255.cos.ap-shanghai.myqcloud.com/backup/roster.csv
  ```

- **数据库不能直接 cp。** 库是 WAL 模式，主文件可能只有几十 KB，直接拷主文件拿到的
  未必是全量。脚本走 sqlite3 的在线备份 API，源库同时在写也能拿到一致的快照；想确认
  传对了，比较两边 `SELECT COUNT(*) FROM submissions` 的行数即可。

### 验证

```bash
python3 judge/tools/selftest_logic.py   # 纯逻辑，不需要沙箱、不需要 sudo
python3 judge/tools/selfcheck.py        # 真沙箱：七种判题结论各造一个程序
curl -s https://mind-city.com/judge/api/health
```

`selfcheck.py` 需要 `isolate.service` 在跑，否则开头就会提示并退出码 2。

### 三个坑

**① `--mem` 必须取 `--cg-mem` 的 2 倍，不能同值。**

`RLIMIT_AS >= RSS` 恒成立，两者同值时 `RLIMIT_AS` 必然先触发：程序一次
`malloc(400MB)` 在 256 MB 限制下直接返回 NULL，若它打印错误信息退出 1，就会被判成
**RE（运行错误）而不是 MLE**，而 cgroup 的 `cg-mem` 停在 6.7 MB，根本达不到 MLE 判据。

实测（同一个只申请 400 MB 的程序，2026-09-21）：

| `--mem` / `--cg-mem` | 结论 | meta 里的 `cg-mem` |
|---|---|---|
| 256 MB / 256 MB（同值） | RE ← 错 | 6784 KB |
| 512 MB / 256 MB（2 倍） | MLE ← 对 | 262144 KB |

测这类程序时**必须让编译器消不掉内存操作**：`memset` 之后再也不读那块内存的话，
`-O2` 会把整个 memset 当死代码删掉，程序根本没碰内存，测出来的结果全是假的
（第一版测试程序就踩了这个，两种配法都「通过」）。

**② `isolate.service` 停掉后 `--cg` 失效，但报错信息会误导。**

`/run/isolate/cgroup` 这个文件**不会**跟着清理，它留着一条已经不存在的路径，所以
报错看起来像配置写错了，实际只是服务没起。判题层的 `judge_ready()` 就是为此写的：
读那个文件之后还要确认路径下真的有 `cgroup.procs`。

**③ 关掉 Nagle，否则每个响应白等 40 ms。**

`http.server` 的 `wfile` 是无缓冲的，响应头和响应体分两次 write，Nagle 会压住第二个
包等对端的 ACK，而客户端此时在延迟确认。实测首字节从 56 ms 降到 14 ms。一个
`disable_nagle_algorithm = True` 就够（`StreamRequestHandler` 现成的开关）。

## 排错

**确认线上是否为最新**

```bash
git -C ~/Mind-City-Course log --oneline -1                    # 部署目录的 HEAD
curl -sS https://mind-city.com/ | grep -c '<关键字>'           # 线上内容
stat -c '%y' /var/www/mind-city/index.html                    # 静态文件更新时间
```

**查看 GitHub 是否真的投递成功**——只看服务器日志会漏掉这类问题：

```bash
gh api repos/EthanCaol/Mind-City-Course/hooks/678947351/deliveries \
  --jq '.[] | "\(.delivered_at)  \(.event)  \(.status)  HTTP \(.status_code)"'
```

**常见问题**

| 症状 | 原因与处理 |
|---|---|
| 日志报 `mkdocs: command not found`（退出码 127） | systemd 的 `PATH` 不含 miniconda。部署脚本开头已显式 `PATH="$HOME/miniconda3/bin:$PATH"`，**改动脚本时不要删掉这行** |
| GitHub 投递显示 `FAILED` / `context deadline exceeded` | **GitHub webhook 超时只有 10 秒**。接收器必须验签后立刻返回（现为 202），部署丢到后台线程跑。**不要把它改回同步执行**——失败的投递不会自动重试，push 会静默丢失 |
| 构建失败但站点还在 | 预期行为。脚本先构建到 staging，成功才同步，构建失败时线上保持旧版 |
| 日志报 `Cannot fast-forward to multiple branches`（退出码 128） | 部署的 `git pull` 和**别人在同一个仓库里跑的 `git fetch`/`git pull` 撞了**，两个进程抢着写 `.git/FETCH_HEAD`，同一条 `main` 被写了两遍，`merge --ff-only` 见到多个 head 就拒绝。本地 `git pull` 看起来一切正常，重跑一次部署脚本即可。**不要在可能触发部署的时间窗口里手动对这个仓库跑 fetch/pull** |
| 中文标题锚点变成 `_1`/`_2` | `mkdocs.yml` 的 `toc.slugify` 配置被改动了，见下 |

## 灾难恢复：从零重建

若 `~/Mind-City-Course` 丢失，部署目录可重新克隆（**不要**把 `/var/www/mind-city` 当源码）：

```bash
git clone git@github.com:EthanCaol/Mind-City-Course.git ~/Mind-City-Course
~/.local/bin/mind-city-deploy.sh
```

依赖重装（conda base）。**这些包一个都不能少**——缺任何一个都不会报错，只会静默降级：

```bash
pip install mkdocs-material                              # 主题本体
pip install jieba                                        # 中文搜索分词；缺了搜「镜像」搜不到
pip install mkdocs-glightbox                             # 图片点击放大
pip install mkdocs-git-revision-date-localized-plugin    # 页面底部「最后更新于 X 天前」
pip install mkdocs-open-in-new-tab                       # 站外链接新标签页打开
```

装完可以这样自查是否齐全（注意 `mkdocs-open-in-new-tab` 装出来的模块名是
`open_in_new_tab`，不带 `mkdocs_` 前缀）：

```bash
python3 -c "import jieba, mkdocs_glightbox, mkdocs_git_revision_date_localized_plugin, open_in_new_tab; print('ok')"
```

两点补充：

- **`privacy` 插件是 Material 自带的**，不需要单独 pip 安装，但**首次构建必须能联网**——它要去 Google Fonts 和 unpkg 抓资源。抓完缓存在 `.cache/plugin/privacy`（已 gitignore），之后离线也能构建。
- **Cascadia Code 字体已随仓库提交**（`docs/assets/fonts/`），克隆下来就有，不需要额外下载。

`mermaid` 流程图**不需要装包**——Material 自带渲染逻辑，只需 `mkdocs.yml` 里 `pymdownx.superfences` 的 `custom_fences` 配置（已配好）。但注意 Material 是从 `unpkg.com` 加载 mermaid 脚本的，国内网络可能较慢，详见下方「已知问题」。

## 字体与外部资源自托管

`privacy` 插件在构建时把所有外部资源抓下来本地化，学生**无需访问任何境外域名**：

```
assets/external/
├── fonts.googleapis.com/     44K   Roboto 样式表
├── fonts.gstatic.com/       808K   Roboto / Roboto Mono 字体（30 个 woff2）
├── unpkg.com/               3.5M   mermaid（懒加载，仅含流程图的页面才请求）
└── image-...myqcloud.com/   2.3M   教程里的 19 张截图
```

顺带解决了原本截图托管在腾讯云 COS 上的隐患——现在是本地副本，不怕对方开防盗链或欠费。

**构建时必须能联网**（服务器在香港，访问 Google/Cloudflare 无障碍）。首次构建约 7 秒，之后走 `.cache/plugin/privacy` 缓存，2 秒左右。缓存目录已加入 `.gitignore`。

### 正文字体

Material 默认用 Google 的 Roboto + Roboto Mono，现由 `privacy` 自托管。注意 **Roboto 不含中文字形**——中文始终由系统字体渲染（Windows 上通常是微软雅黑，macOS 是苹方）。自托管只是消掉了那个被墙的请求让首屏不卡住，中文的显示效果本来就由系统决定，不需要额外配。

### 代码字体：Cascadia Code

自托管在 `docs/assets/fonts/`（3 个 woff2，共 100 KB，**只含 latin 子集**——代码块是纯 ASCII，不需要中文字形，体积因此从 3 MB 降到 100 KB），由 `docs/assets/stylesheets/fonts.css` 定义 `@font-face` 并覆盖 `--md-code-font`。

选它的理由：**Windows Terminal 和 VSCode 的默认等宽字体就是它**，学生看文档里代码和看自己编辑器里的是同一套字形。授权 SIL OFL 1.1，可自由分发。

**连字默认开着**：`!=` 显示为 `≠`，`>=` 显示为 `≥`，`=>` 显示为箭头。这与 VSCode 一致，所以保留了默认行为。如果认为一年级学生看 `≠` 会误以为要输入 `≠` 而不是 `!=`，取消 `fonts.css` 末尾那段注释即可全局关闭。

## 已知问题

**一、删掉 `site_url` 会让 mermaid 变成每页加载 3.4 MB**

`privacy` 插件里有这样一个特判：

```python
# If site URL is not given, ensure that Mermaid.js is always present.
if "mermaid.min.js" in url.path and not config.site_url:
    config.extra_javascript.append(script)
```

未配置 `site_url` 时，插件无法把 mermaid 的绝对 URL 正确改写成本地路径，于是走兜底——把它硬塞进 `extra_javascript`，**每个页面（含 404）都会加载 3.4 MB**，而且构建时间从 2 秒涨到 7 秒。

配上 `site_url: https://mind-city.com/` 之后，URL 被正确改写成 `assets/external/unpkg.com/mermaid@11/dist/mermaid.min.js`，恢复「只有含流程图的页面才请求」的懒加载行为。

**所以 `site_url` 这一行不能删。** 它本来也是该配的——`sitemap.xml` 里的链接依赖它。

**二、bash 代码块的命令名不着色**

这是 Pygments `BashLexer` 的固有行为，不是配置错误。它只给 shell **语法结构**着色（注释、字符串、变量、关键字、操作符、数字），**外部命令一律不着色**——`sudo`、`apt`、`wsl`、`cat`、`grep` 都是白的，因为词法分析器无法判断 `nginx` 是命令还是文件名。只有 `echo`、`cd` 这类 bash 内建才有颜色。

Material 的配色又叠加了一层：`.n`（Name）被映射成 `--md-code-fg-color`，**等于正文色**。所以实测 `sudo apt update && sudo apt upgrade -y` 渲染出来只有 `&&` 是淡灰。

**换 `pygments_style` 无效**——配色能换，但那些命令压根没有 token 类。真要改只能自定义 lexer。

**三、部分插件已倒向 ProperDocs，在本站的 mkdocs 1.6.1 下不可用**

MkDocs 上游放弃 1.x 转向 2.x 后，社区把 1.x 分叉成了 **ProperDocs**。一些插件随之改了依赖，
装上去轻则拖进一整个 properdocs，重则直接构建失败。已实测确认不可用的：

| 插件 | 症状 |
|---|---|
| `mkdocs-recently-updated-docs` | 构建崩溃：`AttributeError: 'int' object has no attribute 'get'`。它依赖的 `mkdocs-document-dates` 是照 ProperDocs API 写的 |
| `mkdocs-redirects` | 依赖 `properdocs>=1.6.5`，会拖进第二个静态站点生成器 |
| `mkdocs-code-validator` | 同上 |

**要用「最近更新」功能请自己写**——用 `git log` 生成列表即可，十行代码，不依赖任何插件，
也不会因为生态变动失效。**URL 重定向直接写在 Caddy 里**，两行配置，同样不受影响。

判断一个插件是否还有效，最快的办法是装之前先看一眼它的依赖：

```bash
pip install --dry-run <插件名> 2>&1 | grep -i properdocs
```

## 注意事项

- **不要升级 MkDocs 2.0。** Material 官方公告称 2.0 会移除插件系统、主题覆盖全部失效、无迁移路径，且当前未授权不适合生产使用。当前锁定 mkdocs 1.6.1 + mkdocs-material 9.7.7。
- **不要用 `gh api -f` 传布尔字段**，`-f` 一律按字符串发送，会报 422；布尔要用 `-F`。
- webhook 密钥位于 `~/.config/mind-city/webhook-secret`（权限 700/600），**不要提交进仓库**。
- `/var/www/mind-city` 归 `ethan` 所有，部署脚本无需 root 即可写入；Caddy 以 `caddy` 用户读取。
