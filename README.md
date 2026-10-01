# Mind-City-Course

复旦大学《程序设计》课程的实验文档站，基于 [MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) 构建。

在线访问：<https://mind-city.com>

## 目录结构

```
.
├── mkdocs.yml         # 站点配置：主题、导航(nav)、Markdown 扩展、hooks
├── hooks/
│   └── revision_notice.py   # 构建钩子：把「最后更新」提示从页脚挪到标题下方
├── docs/              # 站点内容
│   ├── index.md       # 首页
│   ├── material.md    # 课程资料：网站、书目、课件链接、每周课程安排
│   ├── plan.md        # 站点计划
│   ├── question/      # C 语言题库，按讲课顺序编号的 13 个知识点文件
│   ├── setup/         # 实验课文档：环境搭建与工具链，共 9 篇
│   ├── code/          # 正文用 snippet 引入的示例代码
│   └── assets/        # 字体、样式表、图片
├── judge/             # 在线评测后端
└── README.md
```

`site/`（构建产物）和 `.cache/`（`privacy` 插件抓取外部资源的缓存）都已 gitignore。

## 本地构建与预览

依赖装在 conda `base` 环境：

```bash
pip install mkdocs-material jieba mkdocs-glightbox \
  mkdocs-git-revision-date-localized-plugin mkdocs-open-in-new-tab
```

```bash
cd ~/Mind-City-Course
mkdocs serve     # 打开 http://127.0.0.1:8000，保存后自动刷新
```

## 发布

```bash
git add -A && git commit -m "..." && git push
```

推送后约十几秒自动上线。构建使用 `--strict`，存在坏链接或非法语法会失败，此时线上保持上一版内容。

---

新增页面的步骤、Markdown 语法、写作规范、部署与运维细节见 [CLAUDE.md](CLAUDE.md)。
