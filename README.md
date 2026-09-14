# Mind-City-Course

课程文档站点，基于 [MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)。

在线访问：<https://mind-city.com>

---

# 第一部分：如何添加新文档页面

## 目录结构

```
.
├── mkdocs.yml         # 站点配置：主题、导航(nav)、Markdown 扩展
├── docs/
│   ├── index.md       # 首页
│   └── assets/        # 图片等静态资源（需自行创建）
└── README.md          # 本文件，仅面向仓库，不会出现在网站上
```

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

两个 **systemd 用户级服务**（均设了 `linger`，断 SSH 不死、开机自启）：

```bash
systemctl --user status  mind-city-docs      # 本地写作预览，127.0.0.1:8000
systemctl --user status  mind-city-webhook   # 部署接收器，127.0.0.1:9000

systemctl --user restart mind-city-docs
systemctl --user restart mind-city-webhook

journalctl --user -u mind-city-webhook -f    # 实时看部署日志
```

`mind-city-docs` 只绑本地回环，**不对公网提供内容**，仅供在服务器上写文档时预览。公网由 Caddy 直接托管 `/var/www/mind-city` 的静态文件。

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
```

装完可以这样自查是否齐全：

```bash
python3 -c "import jieba, mkdocs_glightbox, mkdocs_git_revision_date_localized_plugin; print('ok')"
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

## 注意事项

- **不要升级 MkDocs 2.0。** Material 官方公告称 2.0 会移除插件系统、主题覆盖全部失效、无迁移路径，且当前未授权不适合生产使用。当前锁定 mkdocs 1.6.1 + mkdocs-material 9.7.7。
- **不要用 `gh api -f` 传布尔字段**，`-f` 一律按字符串发送，会报 422；布尔要用 `-F`。
- webhook 密钥位于 `~/.config/mind-city/webhook-secret`（权限 700/600），**不要提交进仓库**。
- `/var/www/mind-city` 归 `ethan` 所有，部署脚本无需 root 即可写入；Caddy 以 `caddy` 用户读取。
