# Mind-City-Course

课程文档站点，基于 [MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)。

在线访问：<https://mind-city.com>

## 本地预览

```bash
pip install mkdocs-material
mkdocs serve
```

默认监听 <http://127.0.0.1:8000>，修改 `docs/` 下的 Markdown 后浏览器自动刷新。

## 构建静态站

```bash
mkdocs build          # 输出到 site/
mkdocs build --strict # 有警告即报错，用于 CI
```

## 目录结构

```
.
├── mkdocs.yml    # 站点配置：主题、导航、Markdown 扩展
└── docs/
    └── index.md  # 首页
```

新增页面：在 `docs/` 下创建 `.md` 文件，再到 `mkdocs.yml` 的 `nav` 中登记。
