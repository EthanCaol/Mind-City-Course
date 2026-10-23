import sys
from pathlib import Path

import numpy as np
import torch
from PIL import Image
from spandrel import ModelLoader

WEIGHTS = Path(torch.hub.get_dir()) / "checkpoints" / "SwinIR-L_x4_GAN.pth"

def upscale(src, dst, weights=WEIGHTS, pad=32):
    if not Path(weights).exists():
        sys.exit(f"权重不存在: {weights}")

    img = Image.open(src).convert("RGB")
    x = torch.from_numpy(np.asarray(img).astype(np.float32) / 255).permute(2, 0, 1)[None]
    x = x.cuda() if torch.cuda.is_available() else x
    h, w = x.shape[-2:]

    x = torch.nn.functional.pad(x, (0, (-w) % pad, 0, (-h) % pad), mode="reflect")
    desc = ModelLoader().load_from_file(weights)
    with torch.no_grad():
        out = desc.model.to(x.device).eval()(x)[:, :, : h * desc.scale, : w * desc.scale]

    out = (out.clamp(0, 1)[0].permute(1, 2, 0).cpu().numpy() * 255).round().astype(np.uint8)
    Image.fromarray(out).save(dst)
    print(f"{src} {w}x{h} -> {dst} {w * desc.scale}x{h * desc.scale}")

if __name__ == "__main__":
    upscale(*sys.argv[1:])
