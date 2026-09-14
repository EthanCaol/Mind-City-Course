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
````

标题会自动生成锚点，**中文标题保留中文锚点**（如 `#部署`），可直接分享该链接。

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

依赖重装（conda base）：

```bash
pip install mkdocs-material
```

## 注意事项

- **不要升级 MkDocs 2.0。** Material 官方公告称 2.0 会移除插件系统、主题覆盖全部失效、无迁移路径，且当前未授权不适合生产使用。当前锁定 mkdocs 1.6.1 + mkdocs-material 9.7.7。
- **不要用 `gh api -f` 传布尔字段**，`-f` 一律按字符串发送，会报 422；布尔要用 `-F`。
- webhook 密钥位于 `~/.config/mind-city/webhook-secret`（权限 700/600），**不要提交进仓库**。
- `/var/www/mind-city` 归 `ethan` 所有，部署脚本无需 root 即可写入；Caddy 以 `caddy` 用户读取。
