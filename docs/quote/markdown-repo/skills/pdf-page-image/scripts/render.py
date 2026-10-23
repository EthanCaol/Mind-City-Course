# -*- coding: utf-8 -*-
"""教材 PDF 页面渲染与拼接

用法:
  python render.py info   <pdf>
  python render.py search <pdf> <关键词>
  python render.py render <pdf> --pages 122-125 --out 拼图.png [--manifest 同名.json]
                            [--dpi 160] [--gap 16] [--label-h 22] [--no-label]

render 的产物是一张纵向拼图, 以及一份 manifest.json
manifest 记录每页在拼图中的像素区间, 供 pdf-figure-crop 换算回源页

依赖: pymupdf, pillow
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
    fitz = load_pymupdf()
    if not os.path.isfile(path):
        fail("找不到 PDF: " + path)
    return fitz.open(path)


def parse_pages(spec, total):
    pages = []
    for part in spec.split(','):
        part = part.strip()
        if not part:
            continue
        if '-' in part:
            a, b = part.split('-', 1)
            try:
                a, b = int(a), int(b)
            except ValueError:
                fail("页码范围写错: " + part)
            if a > b:
                fail("页码范围起止颠倒: " + part)
            pages.extend(range(a, b + 1))
        else:
            try:
                pages.append(int(part))
            except ValueError:
                fail("页码写错: " + part)
    bad = [p for p in pages if p < 1 or p > total]
    if bad:
        fail("页码越界, 该 PDF 共 %d 页: %s" % (total, bad))
    if not pages:
        fail("没有解析出任何页码")
    return pages


def load_font(size):
    from PIL import ImageFont
    try:
        return ImageFont.load_default(size=size)
    except TypeError:
        return ImageFont.load_default()


def label_bar(width, height, text, font):
    from PIL import Image, ImageDraw
    bar = Image.new('RGB', (width, height), (238, 238, 238))
    ImageDraw.Draw(bar).text((6, 2), text, fill=(40, 40, 40), font=font)
    return bar


def count_cjk(text):
    """统计中日韩汉字数, 既给人看, 也参与判定中文书的文字层是否可信"""
    return sum(1 for ch in text if '一' <= ch <= '鿿')


def count_chars(text):
    """判定用的字符总数: 空白字符不计

    换行, 制表, 全角空格不承载正文, 却能把分母撑得很大
    语文教材一个汉字一行, 一行拼音, 换行能占抽取结果的三成
    算进分母会把正常文字层判成乱码
    """
    return sum(1 for ch in text if not ch.isspace())


def count_readable(text):
    """统计可读字符数, 判文字层能不能用就看它

    口径是非空白字符里, 控制字符与 U+0080 到 U+00FF 之外都算可读
    排除那一段是因为缺 ToUnicode 映射时, 中文字节会被当成 Latin-1 解释
    整篇正文恰好落进这一段, 这正是要判出来的那种乱码
    正经的欧洲语言里带音标的字母只是零星几个, 占不到一成, 由阈值吸收

    这个口径不认中文字符数
    所以中日韩, 英文, 西里尔, 希腊文的教材用同一套阈值, 不必按语种分支
    """
    return sum(1 for ch in text
               if not ch.isspace() and ord(ch) >= 0x20
               and not 0x80 <= ord(ch) <= 0xFF)


# 低于 0.8 判乱码, 平均每页可读字符低于 50 判文字层太薄
# 两个阈值与 SKILL.md 那张四情形表一致, 改一处要一起改
# 实测余量: 一本中文数学教材 0.94 左右, 缺的那几个百分点是 × ± ° 这类
# 落在 U+0080 到 U+00FF 的符号, 而当成 Latin-1 解出来的中文只有 0.08
READABLE_RATIO_MIN = 0.8
PER_PAGE_MIN = 50

# 中文书里汉字占可读字符的比例低于这个数就判文字层不可用
# 防的是 OCR 写回文字层的扫描件: 乱码落在 ASCII 段, 上面的判据看不见它们
# 实测一份 502 页的无机化学扫描件, 可读占比 98%, 汉字占比 0
CJK_RATIO_MIN = 0.05


def expects_cjk(pdf_path, toc, head):
    """判这本书是不是中文书

    证据只取文件名, 书签标题与首页正文, 不取文字层本身
    文字层本身就是待判定的对象, 拿它当证据会形成循环
    """
    sample = os.path.basename(pdf_path) + ''.join(t for _, t, _ in toc) + head
    return count_cjk(sample) >= 8


def verdict_of(total, chars, readable, cjk=0, chinese=False):
    """返回 (判定代号, 说明), 代号取值 scanned / garbled / thin / ok"""
    if chars == 0:
        return 'scanned', '扫描版, 无文字层, 只能渲染候选页人工看图, 按关键词搜索不可用'
    ratio = readable / float(chars) if chars else 0
    cjk_ratio = cjk / float(readable) if readable else 1
    if ratio < READABLE_RATIO_MIN:
        return 'garbled', ('文字层抽出来是乱码, 可读字符只占 %.0f%%, '
                           '多半缺 ToUnicode 映射' % (ratio * 100))
    if chinese and cjk_ratio < CJK_RATIO_MIN:
        return 'garbled', ('有文字层但汉字只占 %.1f%%, 像是 OCR 写回的结果, '
                           '正文要读图核对' % (cjk_ratio * 100))
    per_page = readable / float(total) if total else 0
    if per_page < PER_PAGE_MIN:
        return 'thin', '文字层很薄, 平均每页只有 %.0f 个可读字符, 按无文字层处理' % per_page
    return 'ok', '可读字符占 %.0f%%, 平均每页 %.0f 个, 可以按关键词搜索定位页码' % (
        ratio * 100, per_page)


def cmd_info(args):
    doc = open_pdf(args.pdf)
    total = doc.page_count
    texts = []
    for page in doc:
        texts.append(page.get_text().strip())
    full = '\n'.join(texts)
    chars = count_chars(full)
    readable = count_readable(full)
    cjk = count_cjk(full)
    toc = doc.get_toc()
    head = texts[0] if texts else ''
    chinese = expects_cjk(args.pdf, toc, head)
    code, verdict = verdict_of(total, chars, readable, cjk, chinese)

    if args.json:
        print(json.dumps({
            'path': os.path.abspath(args.pdf),
            'pages': total,
            'chars': chars,
            'readable': readable,
            'readable_ratio': round(readable / float(chars), 3) if chars else 0,
            'per_page_readable': round(readable / float(total), 1) if total else 0,
            'cjk': cjk,
            'cjk_ratio': round(cjk / float(readable), 3) if readable else 0,
            'expects_cjk': chinese,
            'verdict': code,
            'verdict_text': verdict,
            'toc': [[level, title, pno] for level, title, pno in toc],
        }, ensure_ascii=False))
        doc.close()
        return

    print("文件: %s" % os.path.abspath(args.pdf))
    print("页数: %d" % total)
    print("文字层字符总数(不含空白): %d" % chars)
    print("其中可读字符: %d" % readable)
    print("其中中文字符: %d" % cjk)
    print("平均每页可读字符: %.0f" % (readable / float(total) if total else 0))
    print("判定(%s): %s" % (code, verdict))
    print("书签条目: %d" % len(toc))
    limit = args.toc_limit if args.toc_limit > 0 else len(toc)
    for level, title, pno in toc[:limit]:
        print("  %s%s  ->  PDF %d" % ("  " * (level - 1), title, pno))
    if len(toc) > limit:
        print("  ... 共 %d 条, 只列前 %d, 要看全部把 --toc-limit 设为 0" % (len(toc), limit))
    print("首页文本片段: %s" % (head[:200].replace('\n', ' ') or "(空)"))
    doc.close()


def normalize(text):
    """去掉所有空白, 中文 PDF 的字间常有间隙, 直接搜会匹配不上"""
    return ''.join(text.split())


def cmd_search(args):
    doc = open_pdf(args.pdf)
    hits = []
    texts = []
    needle = normalize(args.keyword)
    for i, page in enumerate(doc, start=1):
        text = page.get_text().strip()
        texts.append(text)
        if needle and needle in normalize(text):
            hits.append(i)
    full = '\n'.join(texts)
    toc = doc.get_toc()
    chinese = expects_cjk(args.pdf, toc, texts[0] if texts else '')
    code, _ = verdict_of(doc.page_count, count_chars(full),
                         count_readable(full), count_cjk(full), chinese)
    if hits:
        head = hits[:40]
        tail = "" if len(hits) <= 40 else "  ... 共 %d 页" % len(hits)
        print("命中 %d 页: %s%s" % (len(hits), ", ".join(str(h) for h in head), tail))
        if code != 'ok':
            print("但文字层判定为 %s, 命中结果只能当候选, 页范围要读图确认" % code)
    elif code == 'scanned':
        print("该 PDF 没有文字层(扫描版), 搜索不可用, 改渲染候选页人工看图定范围")
    elif code == 'garbled':
        print("该 PDF 的文字层抽不出可用正文, 搜索不可用, 改渲染候选页人工看图定范围")
    else:
        print("文字层可用, 但没有命中: %s" % args.keyword)
        print("教材原文可能与关键词不完全一致, 换一个更短的片段再试")
    doc.close()


def cmd_render(args):
    fitz = load_pymupdf()
    from PIL import Image
    doc = open_pdf(args.pdf)
    pages = parse_pages(args.pages, doc.page_count)

    zoom = args.dpi / 72.0
    mat = fitz.Matrix(zoom, zoom)
    blocks = []
    for pno in pages:
        pix = doc[pno - 1].get_pixmap(matrix=mat)
        img = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
        blocks.append((pno, img))
    doc.close()

    label_h = 0 if args.no_label else args.label_h
    font = load_font(max(12, label_h - 8)) if label_h else None
    width = max(img.width for _, img in blocks)
    total_h = sum(label_h + img.height for _, img in blocks) + args.gap * (len(blocks) - 1)

    canvas = Image.new('RGB', (width, total_h), (255, 255, 255))
    entries = []
    y = 0
    for pno, img in blocks:
        if label_h:
            canvas.paste(label_bar(width, label_h, "PDF %d" % pno, font), (0, y))
            y += label_h
        canvas.paste(img, (0, y))
        entries.append({
            'pdf_page': pno,
            'y0': y - label_h,
            'y1': y + img.height,
            'w': img.width,
            'h': img.height,
        })
        y += img.height + args.gap

    out = os.path.abspath(args.out)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    canvas.save(out)

    manifest_path = os.path.abspath(args.manifest) if args.manifest else os.path.splitext(out)[0] + '.json'
    os.makedirs(os.path.dirname(manifest_path), exist_ok=True)
    manifest = {
        'pdf': os.path.abspath(args.pdf),
        'dpi': args.dpi,
        'gap': args.gap,
        'label_h': label_h,
        'width': width,
        'height': total_h,
        'pages': entries,
    }
    with open(manifest_path, 'w', encoding='utf-8') as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=1)

    print("拼图: %s  %dx%d  %d 页" % (out, width, total_h, len(entries)))
    print("坐标清单: %s" % manifest_path)
    for e in entries:
        print("  PDF %d  在拼图 y %d..%d" % (e['pdf_page'], e['y0'], e['y1']))


def main():
    ap = argparse.ArgumentParser(description="教材 PDF 页面渲染与拼接")
    sub = ap.add_subparsers(dest='cmd', required=True)

    p = sub.add_parser('info', help='打印页数, 文字层可信度, 书签目录')
    p.add_argument('pdf')
    p.add_argument('--toc-limit', type=int, default=0,
                   help='书签最多打印几条, 0 表示全部, 默认全部')
    p.add_argument('--json', action='store_true', help='输出一行 JSON')
    p.set_defaults(func=cmd_info)

    p = sub.add_parser('search', help='按关键词定位页码, 仅对有文字层的 PDF 有效')
    p.add_argument('pdf')
    p.add_argument('keyword')
    p.set_defaults(func=cmd_search)

    p = sub.add_parser('render', help='渲染并纵向拼成一张图')
    p.add_argument('pdf')
    p.add_argument('--pages', required=True, help='单页 122, 范围 122-125, 列表 122,130')
    p.add_argument('--out', required=True, help='输出拼图路径')
    p.add_argument('--manifest', help='坐标清单路径, 默认与拼图同名 .json')
    p.add_argument('--dpi', type=int, default=160, help='渲染 dpi, 默认 160')
    p.add_argument('--gap', type=int, default=16, help='页与页之间的空白像素, 默认 16')
    p.add_argument('--label-h', type=int, default=22, help='页号标签条高度, 默认 22')
    p.add_argument('--no-label', action='store_true', help='不画页号标签条')
    p.set_defaults(func=cmd_render)

    args = ap.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
