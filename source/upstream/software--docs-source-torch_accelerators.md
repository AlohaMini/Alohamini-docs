# PyTorch accelerators

[← 教程资料库](../tutorial-library.md) · **环境与训练工具 / 原文全文**

本文保留软件仓库的通用或进阶教程。示例中的机器人、数据集、路径和运行环境需按实际配置选择，不代表已经在 AlohaMini 2 / 2 Pro 上验证。

来源：[liyiteng/lerobot_alohamini · `docs/source/torch_accelerators.mdx`](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/torch_accelerators.mdx) · 版本 `7843e588` · [下载未经改写的源文档](../_static/upstream-originals/software/docs/source/torch_accelerators.mdx.txt)

本页保留原文语言及全部段落、表格和代码；仅调整标题层级、页面组件、代码围栏格式、相对链接和媒体路径。原文中的价格、性能和运行结果属于该版本记录。

---


LeRobot supports multiple hardware acceleration options for both training and inference.

These options include:

- **CPU**: CPU executes all computations, no dedicated accelerator is used
- **CUDA**: acceleration with NVIDIA & AMD GPUs
- **MPS**: acceleration with Apple Silicon GPUs
- **XPU**: acceleration with Intel integrated and discrete GPUs

## Getting Started

To use particular accelerator, a suitable version of PyTorch should be installed.

For CPU, CUDA, and MPS backends follow instructions provided on [PyTorch installation page](https://pytorch.org/get-started/locally).
For XPU backend, follow instructions from [PyTorch documentation](https://docs.pytorch.org/docs/stable/notes/get_start_xpu.html).

### Verifying the installation

After installation, accelerator availability can be verified by running

```python
import torch
print(torch.<backend_name>.is_available())  # <backend_name> is cuda, mps, or xpu
```

## How to run training or evaluation

To select the desired accelerator, use the `--policy.device` flag when running `lerobot-train` or `lerobot-eval`. For example, to use MPS on Apple Silicon, run:

```bash
lerobot-train
    --policy.device=mps ...
```

```bash
lerobot-eval \
    --policy.device=mps ...
```

However, in most cases, presence of an accelerator is detected automatically and `policy.device` parameter can be omitted from CLI commands.
