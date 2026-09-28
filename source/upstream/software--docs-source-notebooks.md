# 🤗 LeRobot Notebooks

[← 教程资料库](../tutorial-library.md) · **环境与训练工具 / 原文全文**

本文保留软件仓库的通用或进阶教程。示例中的机器人、数据集、路径和运行环境需按实际配置选择，不代表已经在 AlohaMini 2 / 2 Pro 上验证。

来源：[liyiteng/lerobot_alohamini · `docs/source/notebooks.mdx`](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/notebooks.mdx) · 版本 `7843e588` · [下载未经改写的源文档](../_static/upstream-originals/software/docs/source/notebooks.mdx.txt)

本页保留原文语言及全部段落、表格和代码；仅调整标题层级、页面组件、代码围栏格式、相对链接和媒体路径。原文中的价格、性能和运行结果属于该版本记录。

---


This repository contains example notebooks for using LeRobot. These notebooks demonstrate how to train policies on real or simulation datasets using standardized policies.

---

## Training ACT

[ACT](https://huggingface.co/papers/2304.13705) (Action Chunking Transformer) is a transformer-based policy architecture for imitation learning that processes robot states and camera inputs to generate smooth, chunked action sequences.

We provide a ready-to-run Google Colab notebook to help you train ACT policies using datasets from the Hugging Face Hub, with optional logging to Weights & Biases.

| Notebook                                                                                                | Colab                                                                                                                                                                             |
| :------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Train ACT with LeRobot](https://github.com/huggingface/notebooks/blob/main/lerobot/training-act.ipynb) | [![Open in Colab](../_static/external-images/a590b05e22690c59d120.svg)](https://colab.research.google.com/github/huggingface/notebooks/blob/main/lerobot/training-act.ipynb) |

Expected training time for 100k steps: ~1.5 hours on an NVIDIA A100 GPU with batch size of `64`.

## Training SmolVLA

[SmolVLA](https://huggingface.co/papers/2506.01844) is a small but efficient Vision-Language-Action model. It is compact in size with 450 M-parameter and is developed by Hugging Face.

We provide a ready-to-run Google Colab notebook to help you train SmolVLA policies using datasets from the Hugging Face Hub, with optional logging to Weights & Biases.

| Notebook                                                                                                        | Colab                                                                                                                                                                                 |
| :-------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Train SmolVLA with LeRobot](https://github.com/huggingface/notebooks/blob/main/lerobot/training-smolvla.ipynb) | [![Open in Colab](../_static/external-images/a590b05e22690c59d120.svg)](https://colab.research.google.com/github/huggingface/notebooks/blob/main/lerobot/training-smolvla.ipynb) |

Expected training time for 20k steps: ~5 hours on an NVIDIA A100 GPU with batch size of `64`.
