# VLA-JEPA

[← 教程资料库](../tutorial-library.md) · **策略与模型 / 原文全文**

本文保留软件仓库的通用或进阶教程。示例中的机器人、数据集、路径和运行环境需按实际配置选择，不代表已经在 AlohaMini 2 / 2 Pro 上验证。

来源：[liyiteng/lerobot_alohamini · `docs/source/policy_vla_jepa_README.md`](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_vla_jepa_README.md) · 版本 `7843e588` · [下载未经改写的源文档](../_static/upstream-originals/software/docs/source/policy_vla_jepa_README.md.txt)

本页保留原文语言及全部段落、表格和代码；仅调整标题层级、页面组件、代码围栏格式、相对链接和媒体路径。原文中的价格、性能和运行结果属于该版本记录。

---


This repository contains the LeRobot port of **VLA-JEPA**, a Vision-Language-Action model that combines a Qwen3-VL language backbone with a self-supervised video world model (V-JEPA2) and a flow-matching DiT action head.

Converted from [ginwind/VLA-JEPA](https://huggingface.co/ginwind/VLA-JEPA).

---

## Architecture Overview

| Component               | Module                            | Role                                                    |
| ----------------------- | --------------------------------- | ------------------------------------------------------- |
| **Qwen3-VL backbone**   | `Qwen3VLInterface`                | Fuses images + language instruction into context tokens |
| **DiT-B action head**   | `VLAJEPAActionHead`               | Flow-matching diffusion over the action chunk           |
| **V-JEPA2 world model** | `ActionConditionedVideoPredictor` | Self-supervised video prediction loss (training only)   |

At inference time only the Qwen backbone and action head are used; the world model is not needed.

---

## Citation

```bibtex
@misc{sun2026vlajepaenhancingvisionlanguageactionmodel,
  title         = {VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model},
  author        = {Jingwen Sun and Wenyao Zhang and Zekun Qi and Shaojie Ren and Zezhi Liu and Hanxin Zhu and Guangzhong Sun and Xin Jin and Zhibo Chen},
  year          = {2026},
  eprint        = {2602.10098},
  archivePrefix = {arXiv},
  primaryClass  = {cs.RO},
  url           = {https://arxiv.org/abs/2602.10098},
}
```

---

## License

Weights are distributed under the license terms of the original [ginwind/VLA-JEPA](https://huggingface.co/ginwind/VLA-JEPA) repository (**Apache 2.0 License**). The LeRobot integration code follows the **Apache 2.0 License**.
