# PyTorch accelerators

[← 教程资料库](../tutorial-library.md) · **环境与训练工具**

本节介绍 LeRobot 的通用功能。请按目标机器人、数据集和运行环境配置示例；用于 AlohaMini 2 / 2 Pro 前，需要确认硬件与接口兼容性。

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
