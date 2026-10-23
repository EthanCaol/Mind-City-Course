# -*- coding: utf-8 -*-
"""按给定像素矩形从页面图里裁出插图

用法:
  # 直接在拼图上裁, 坐标就是看图时量到的像素, 不做任何换算
  python crop.py crop <拼图.png> --box 120,340,980,760 --out fig.png [--pad 12]

  # 拼图 dpi 偏低时, 按 manifest 换算回源页, 用更高 dpi 重渲后再裁
  python crop.py crop <拼图.png> --box 120,340,980,760 --manifest 拼图.json \
                        --from-page --dpi 300 --out fig.png [--pad 12]

坐标一律由调用方给定, 本脚本不做自动识别, 不接 OCR
依赖: pillow; --from-page 时额外需要 pymupdf
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


def parse_box(spec):
    parts = [p.strip() for p in spec.split(',')]
    if len(parts) != 4:
        fail("--box 要写 x1,y1,x2,y2 四个数, 收到: " + spec)
    try:
        x1, y1, x2, y2 = (int(float(p)) for p in parts)
    except ValueError:
        fail("--box 里有非数字: " + spec)
    if x2 <= x1 or y2 <= y1:
        fail("--box 的右下角必须大于左上角, 顺序固定为 x1,y1,x2,y2, 收到: " + spec)
    return x1, y1, x2, y2


def locate_page(manifest, box):
    """找出 box 落在哪一页, 返回 (条目, 页内 y 偏移)"""
    x1, y1, x2, y2 = box
    inside = [e for e in manifest['pages'] if y1 >= e['y0'] and y2 <= e['y1']]
    if not inside:
        spans = ", ".join("PDF %d: y %d..%d" % (e['pdf_page'], e['y0'], e['y1']) for e in manifest['pages'])
        fail("box 的 y 区间跨页或越界, 无法归属到单页\n拼图内各页范围: " + spans)
    return inside[0]


def cmd_crop(args):
    from PIL import Image

    if not os.path.isfile(args.image):
        fail("找不到图片: " + args.image)
    box = parse_box(args.box)
    x1, y1, x2, y2 = box

    if args.from_page:
        if not args.manifest:
            fail("--from-page 必须同时给 --manifest")
        if not os.path.isfile(args.manifest):
            fail("找不到 manifest: " + args.manifest)
        with open(args.manifest, encoding='utf-8') as fh:
            manifest = json.load(fh)
        entry = locate_page(manifest, box)
        src_dpi = manifest['dpi']
        scale = args.dpi / float(src_dpi)

        # 拼图坐标 -> 源页坐标: 减掉该块起始位置与页号标签条, 再按 dpi 比缩放
        top = entry['y0'] + manifest['label_h']
        px1 = max(0, (x1 - 0) * scale)
        py1 = max(0, (y1 - top) * scale)
        px2 = min(entry['w'] * scale, x2 * scale)
        py2 = min(entry['h'] * scale, (y2 - top) * scale)

        try:
            import pymupdf as fitz
        except ImportError:
            try:
                import fitz
            except ImportError:
                fail("--from-page 需要 pymupdf, 先执行: python -m pip install pymupdf")
        if not os.path.isfile(manifest['pdf']):
            fail("manifest 里记录的 PDF 不在了: " + manifest['pdf'])
        doc = fitz.open(manifest['pdf'])
        zoom = args.dpi / 72.0
        pix = doc[entry['pdf_page'] - 1].get_pixmap(matrix=fitz.Matrix(zoom, zoom))
        page_img = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
        doc.close()
        print("换算回 PDF %d, %.0f dpi, 页内框 %d,%d,%d,%d"
              % (entry['pdf_page'], args.dpi, px1, py1, px2, py2))
        pad = int(args.pad * scale)
        out_img = page_img.crop((
            max(0, px1 - pad), max(0, py1 - pad),
            min(page_img.width, px2 + pad), min(page_img.height, py2 + pad),
        ))
    else:
        src = Image.open(args.image)
        if x2 > src.width or y2 > src.height:
            fail("box 超出图片范围, 图尺寸 %dx%d" % (src.width, src.height))
        out_img = src.crop((
            max(0, x1 - args.pad), max(0, y1 - args.pad),
            min(src.width, x2 + args.pad), min(src.height, y2 + args.pad),
        ))

    out = os.path.abspath(args.out)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    out_img.save(out, 'PNG')
    print("插图: %s  %dx%d" % (out, out_img.width, out_img.height))


def main():
    ap = argparse.ArgumentParser(description="按给定矩形裁出插图")
    sub = ap.add_subparsers(dest='cmd', required=True)

    p = sub.add_parser('crop', help='裁一张插图')
    p.add_argument('image', help='待裁的图, 一般是 pdf-page-image 产出的拼图')
    p.add_argument('--box', required=True, help='x1,y1,x2,y2, 半角逗号分隔')
    p.add_argument('--out', required=True, help='输出 png 路径')
    p.add_argument('--pad', type=int, default=12, help='四周外扩像素, 默认 12')
    p.add_argument('--manifest', help='拼图对应的坐标清单, --from-page 时必填')
    p.add_argument('--from-page', action='store_true', help='换算回源页并按 --dpi 重渲后裁')
    p.add_argument('--dpi', type=int, default=300, help='--from-page 时的重渲 dpi, 默认 300')
    p.set_defaults(func=cmd_crop)

    args = ap.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
