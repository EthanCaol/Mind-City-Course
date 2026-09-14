# Mind-City-Course

欢迎来到 Mind City Course 的文档站点。这里是首页，直接把 `docs/index.md` 的内容替换成你的课程内容即可。

## 本地预览

```bash
cd ~/Mind-City-Course
mkdocs serve
```

默认监听 `http://127.0.0.1:8000`，改 Markdown 后浏览器会自动刷新。

## 新增页面

1. 在 `docs/` 下新建 `.md` 文件，比如 `docs/lesson-01.md`
2. 在 `mkdocs.yml` 的 `nav` 里登记：

```yaml
nav:
  - 首页: index.md
  - 第一课: lesson-01.md
```

## 主题能力速查

!!! note "提示框"
    用 `!!! note` 开头，配合 `admonition` 扩展。还有 `tip` / `warning` / `danger` 等类型。

=== "Tab A"

    用 `=== "标题"` 做内容分页，左侧可切换。

=== "Tab B"

    同样支持代码块：

    ```python
    def hello(name: str) -> str:
        return f"Hello, {name}!"
    ```

- [x] 已完成的待办
- [ ] 未完成的待办

支持 `#!python print("行内高亮")` 和 :material-city: 图标 emoji。
