# -*- coding: utf-8 -*-
"""读写扫描版教材 PDF 的书签目录

用法:
  python bookmark.py toc  <pdf>
  python bookmark.py plan <pdf> --spec 书签.json
  python bookmark.py set  <pdf> --spec 书签.json --out <输出.pdf>

换算约定: PDF 页 = 书页 + 该章偏移量
上册偏移为正, 下册沿用上册页号时偏移为负

spec.json 结构:
  {
    "default_offset": 14,
    "offsets": {"第1章": 16, "第2章": 16, "第3章": 15},
    "entries": [
      ["第1章", 1, 21, "第1章  化学基础知识"],
      ["第1章", 2, 21, "1.1  气体"]
    ]
  }
entries 每行是 [章标识, 层级, 书页, 标题]
章标识用来查 offsets, 查不到就用 default_offset

依赖: pymupdf
"""

import argparse
import json
import os
import sys

# 两个流都切一遍, 只切 stdout 的话 stderr 上的 fail() 在代码页 936 下会乱码
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8")


def fail(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


def load_pymupdf():
    try:
        import pymupdf
        return pymupdf
    except ImportError:
        pass
    try:
        import fitz
        return fitz
    except ImportError:
        fail("缺少 pymupdf, 先执行: python -m pip install pymupdf")


def open_pdf(path):
    if not os.path.isfile(path):
        fail("找不到 PDF: " + path)
    return load_pymupdf().open(path)


def load_spec(path):
    if not os.path.isfile(path):
        fail("找不到 spec: " + path)
    with open(path, encoding='utf-8') as fh:
        try:
            spec = json.load(fh)
        except ValueError as exc:
            fail("spec 不是合法 json: %s" % exc)
    offsets = spec.get('offsets', {})
    default = spec.get('default_offset')
    if default is None and offsets:
        values = set(offsets.values())
        if len(values) == 1:
            default = next(iter(values))
    if default is None:
        fail("spec 缺 default_offset, 且 offsets 里没有唯一值可以推断")
    entries = spec.get('entries')
    if not entries:
        fail("spec 里 entries 为空")
    return offsets, default, entries


def build_toc(entries, offsets, default, total):
    toc = []
    problems = []
    for row in entries:
        if len(row) != 4:
            fail("entries 每行要四个元素 [章, 层级, 书页, 标题], 收到: %r" % (row,))
        chapter, level, book_page, title = row
        offset = offsets.get(chapter, default)
        pdf_page = int(book_page) + int(offset)
        if not 1 <= int(level) <= 3:
            problems.append("层级越界 %r: %s" % (level, title))
        if not 1 <= pdf_page <= total:
            problems.append("换算到 PDF 第 %d 页, 超出 1..%d: %s"
                            % (pdf_page, total, title))
        toc.append([int(level), str(title), pdf_page])
    return toc, problems


def cmd_toc(args):
    doc = open_pdf(args.pdf)
    toc = doc.get_toc()
    print("页数: %d" % doc.page_count)
    print("现有书签: %d 条" % len(toc))
    for level, title, pno in toc:
        print("  %s%s  ->  PDF %d" % ("  " * (level - 1), title, pno))
    doc.close()


def cmd_plan(args):
    doc = open_pdf(args.pdf)
    offsets, default, entries = load_spec(args.spec)
    toc, problems = build_toc(entries, offsets, default, doc.page_count)
    print("默认偏移: %+d" % default)
    for chapter, offset in offsets.items():
        print("  %s: %+d" % (chapter, offset))
    print("书签 %d 条, 换算后前几条:" % len(toc))
    for level, title, pno in toc[:12]:
        print("  %s%s  ->  PDF %d" % ("  " * (level - 1), title, pno))
    if len(toc) > 12:
        print("  ...")
        for level, title, pno in toc[-3:]:
            print("  %s%s  ->  PDF %d" % ("  " * (level - 1), title, pno))
    if problems:
        print("问题 %d 处:" % len(problems))
        for p in problems[:20]:
            print("  " + p)
    else:
        print("换算全部落在页数范围内")
    doc.close()


def cmd_set(args):
    doc = open_pdf(args.pdf)
    offsets, default, entries = load_spec(args.spec)
    toc, problems = build_toc(entries, offsets, default, doc.page_count)
    if problems:
        print("换算有问题, 没有写入")
        for p in problems[:20]:
            print("  " + p)
        doc.close()
        sys.exit(1)

    out = os.path.abspath(args.out)
    if out == os.path.abspath(args.pdf):
        doc.close()
        fail("输出路径不能与原 PDF 相同, 另存一份再替换")

    doc.set_toc(toc)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    doc.save(out, garbage=4, deflate=True)
    doc.close()
    print("已写入 %d 条书签: %s" % (len(toc), out))
    print("检查无误后再替换原文件")


def main():
    ap = argparse.ArgumentParser(description="扫描版教材 PDF 的书签目录读写")
    sub = ap.add_subparsers(dest='cmd', required=True)

    p = sub.add_parser('toc', help='打印现有书签')
    p.add_argument('pdf')
    p.set_defaults(func=cmd_toc)

    p = sub.add_parser('plan', help='试算换算结果, 不写文件')
    p.add_argument('pdf')
    p.add_argument('--spec', required=True)
    p.set_defaults(func=cmd_plan)

    p = sub.add_parser('set', help='写入书签并另存')
    p.add_argument('pdf')
    p.add_argument('--spec', required=True)
    p.add_argument('--out', required=True)
    p.set_defaults(func=cmd_set)

    args = ap.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
