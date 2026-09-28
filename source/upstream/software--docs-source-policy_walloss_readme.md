# WALL-OSS

[← 教程资料库](../tutorial-library.md) · **策略与模型 / 原文全文**

本文保留软件仓库的通用或进阶教程。示例中的机器人、数据集、路径和运行环境需按实际配置选择，不代表已经在 AlohaMini 2 / 2 Pro 上验证。

来源：[liyiteng/lerobot_alohamini · `docs/source/policy_walloss_README.md`](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_walloss_README.md) · 版本 `7843e588` · [下载未经改写的源文档](../_static/upstream-originals/software/docs/source/policy_walloss_README.md.txt)

本页保留原文语言及全部段落、表格和代码；仅调整标题层级、页面组件、代码围栏格式、相对链接和媒体路径。原文中的价格、性能和运行结果属于该版本记录。

---


This repository contains the Hugging Face port of [**WALL-OSS**](https://x2robot.com/en/research/68bc2cde8497d7f238dde690), a Vision-Language-Action model for cross-embodiment robotic control based on Qwen2.5-VL with flow matching/FAST action prediction.

---

## Model Overview

| Feature            | Description                                           |
| ------------------ | ----------------------------------------------------- |
| Base Model         | Qwen2.5-VL (Vision-Language Model)                    |
| Action Prediction  | Flow Matching (diffusion) or FAST (discrete tokens)   |
| Architecture       | Mixture of Experts (MoE) with action-specific routing |
| Multi-Modal Inputs | Vision (images/videos), Language, Proprioception      |

---

## Additional Resources

Paper: https://arxiv.org/pdf/2509.11766

Official Repository: https://github.com/X-Square-Robot/wall-x

Hugging Face: https://huggingface.co/x-square-robot

---

## Citation

If you use this work, please cite:

```bibtex
@article{zhai2025igniting,
    title   = {Igniting VLMs Toward the Embodied Space},
    author  = {Zhai, Andy and Liu, Brae and Fang, Bruno and Cai, Chalse and Ma, Ellie and Yin, Ethan and Wang, Hao and Zhou, Hugo and Wang, James and Shi, Lights and Liang, Lucy and Wang, Make and Wang, Qian and Gan, Roy and Yu, Ryan and Li, Shalfun and Liu, Starrick and Chen, Sylas and Chen, Vincent and Xu, Zach},
    journal = {arXiv preprint arXiv:2509.11766},
    year    = {2025}
}
```

---

## License

This model follows the **Apache 2.0 License**, consistent with the original [WallX repository](https://github.com/X-Square-Robot/wall-x).
