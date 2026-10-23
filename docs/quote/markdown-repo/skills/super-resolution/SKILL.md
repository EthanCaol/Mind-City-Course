---
name: super-resolution
description: 用 SwinIR-L realSR GAN 对本地图片做 4 倍超分. 当用户要求放大图片, 超分, 提高分辨率, 让笔记里的图更清晰, 或需要处理低分辨率插图时使用
user-invocable: true
---

# 超分任务

模型: SwinIR-L realSR GAN, 4 倍放大
注意: 输入先 reflect padding 到 32 的倍数, 输出再裁回原尺寸, 否则 window attention 处报 reshape 错

推理脚本: 本 skill 目录下的 `scripts/sr.py`

## 环境准备

```bash
# 确认 torch 是 CUDA 版
python -c "import torch; print(torch.__version__, torch.cuda.is_available())"

# 安装依赖
pip install spandrel

# 下载权重到 torch.hub 默认目录
mkdir -p ~/.cache/torch/hub/checkpoints
curl -L -o ~/.cache/torch/hub/checkpoints/SwinIR-L_x4_GAN.pth https://github.com/JingyunLiang/SwinIR/releases/download/v0.0/003_realSR_BSRGAN_DFOWMFC_s64w8_SwinIR-L_x4_GAN.pth
```

## 运行

```bash
python .claude/skills/super-resolution/scripts/sr.py 输入图.png 输出图.png
```

第三个参数可省略
省略时用 `torch.hub` 默认目录下的 `SwinIR-L_x4_GAN.pth`
也可以传别的 `.pth` 路径

## 实测数据

本机配置: RTX 4070 Ti SUPER 16G, torch 2.14.1+cu132, Python 3.14
- 权重 135.9M, 下载约 3 秒
- `540×400 → 2160×1600`, 推理约 6 秒
- 输出 PNG 约 412K
- 运行时有一条 `torch.meshgrid` 弃用警告, 出自 torch 自身的 `functional.py`, 不影响结果

## 注意事项

- 权重路径由 `torch.hub.get_dir()` 推导
  - Windows 上是 `C:\Users\16770\.cache\torch\hub\checkpoints`
  - 与 HuggingFace 的 `~/.cache/huggingface/hub` 无关
- 显存占用随输入像素数迅速上升
  - 输入 `2160×1600` 时单次注意力张量要 3.11 GiB, 16G 显卡会 OOM
  - 不要对已经超分过的图重复处理
- 中间产物放在仓库外的临时目录, 不要写进笔记仓库
- 输出保持 PNG 格式, 与图床上的原始文件一致
- 超分后图片字节数明显变大, 图床容量占用相应上升
