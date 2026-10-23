---
name: pdf-bookmark
description: "给扫描版教材 PDF 制作书签目录: 读图找目录页, 定每章的书页到 PDF 页偏移量, 从后往前核对, 写入书签"
user-invocable: true
---

# 扫描版教材的书签目录

总思路是读图定页码, 不是 OCR
渲染页面复用 `pdf-page-image` 的脚本

## 环境准备

```powershell
python -m pip install pymupdf
```

先看这本书现在有没有书签, 决定是新建还是修订

```bash
python .claude/skills/pdf-bookmark/scripts/bookmark.py toc "<pdf>"
```

## 第一步 读图找目录页

纸质书的总目录在正文之前
先逐页渲染前 30 到 40 页, 找到总目录所在的页
定位之后再细读目录上的条目

```bash
python .claude/skills/pdf-page-image/scripts/render.py render "<pdf>" --pages 17 \
    --dpi 160 --out "$tmp/p0017-d160.png"
```

把目录上的条目记录下来, 记的是**书上印的页号**, 不是 PDF 页号

## 第二步 定每章的偏移量

渲染一页, 看页眉或页脚上印的页码, 与它的 PDF 页号相减

```
偏移量 = PDF 页号 - 书页号
```

**偏移量按章可能不同**
扫描时删掉的空白页会让后面的章整体前移
每章要单独定一次, 不要只算一章就沿用到其他章

页码的位置不固定, 有的在页眉, 有的在页脚
偶数页在左奇数页在右的书也不少, 多渲染两页确认

## 第三步 从后往前核对

从最后一章往前逐章核对, 每章取正文首页

```bash
python .claude/skills/pdf-page-image/scripts/render.py render "<pdf>" --pages 486 --dpi 150 --out "$tmp/p0486.png"
```

看渲染出的页眉页码与章节标题是否属于这一章

**最后一章对得上, 说明偏移量没有累积误差, 前面各章一般也正确**
对不上就在附近几页重试, 找到这一章的首页之后, 再往前核对下一章

核对过的章记下偏移量, 遇到相同的值就合并成一个默认值

## 第四步 写 spec 并写入书签

把条目整理成 json

```json
{
  "default_offset": 14,
  "offsets": {"第1章": 16, "第2章": 16, "第3章": 15},
  "entries": [
    ["第1章", 1, 21, "第1章  化学基础知识"],
    ["第1章", 2, 21, "1.1  气体"],
    ["第1章", 3, 21, "1.1.1  气体的状态方程"]
  ]
}
```

- `entries` 每行是 `[章标识, 层级, 书页, 标题]`
- 章标识用来查 `offsets`, 查不到就用 `default_offset`
- 层级取 1 到 3
- 标题里的空格保留教材原样, 章标题与节号之间是两个空格

先试算, 核对换算结果, 这一步不写文件

```bash
python .claude/skills/pdf-bookmark/scripts/bookmark.py plan "<pdf>" --spec "$tmp/书签.json"
```

确认后写入, 输出到另一个文件

```bash
python .claude/skills/pdf-bookmark/scripts/bookmark.py set "<pdf>" \
    --spec "$tmp/书签.json" --out "<pdf 同目录>/<原名>(带书签).pdf"
```

书签核对无误之后, 再决定是否用它替换原文件

## 注意事项

- **书签从第一章开始, 前言, 总目录, 序之类不写进书签**
- 输出路径不能与原 PDF 相同, 脚本会拒绝
- 换算结果超出 1 到总页数, 或层级不在 1 到 3 之间时, 脚本列出问题并拒绝写入
- 已有的书签先用 `toc` 看一眼, 决定是覆盖还是补进 spec
- 80 MB 的 PDF 写入一次约 5 秒
- 仓库路径含 `[ ] ( )` 和中文, 参数一律加引号
- 前 30 到 40 页逐页渲染, 不要几页拼一张, 拼出的图在低 dpi 下正文无法辨认
