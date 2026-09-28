# lerobot_alohamini

[← 教程资料库](../tutorial-library.md) · **环境与训练工具 / 原文全文**

本文保留软件仓库的通用或进阶教程。示例中的机器人、数据集、路径和运行环境需按实际配置选择，不代表已经在 AlohaMini 2 / 2 Pro 上验证。

来源：[liyiteng/lerobot_alohamini · `README.md`](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/README.md) · 版本 `7843e588` · [下载未经改写的源文档](../_static/upstream-originals/software/README.md.txt)

本页保留原文语言及全部段落、表格和代码；仅调整标题层级、页面组件、代码围栏格式、相对链接和媒体路径。原文中的价格、性能和运行结果属于该版本记录。

---


Shared software layer for the AlohaMini product line, built on HuggingFace LeRobot. Supports both the full AlohaMini robot (dual-arm + mobile base + lift) and the AM-ARM200 arm.

> Haven't assembled your hardware yet? Start here: [AlohaMini](https://github.com/liyiteng/alohamini) · [AM-ARM200](https://github.com/liyiteng/AM-ARM)

## Updates
- **[2025-07-11]** merge upstream LeRobot v0.6

## Documentation

Start with setup, then follow the workflow for your hardware. Use the reference pages when you need exact flags, commands, or low-level debug tools.

### Recommended Path

1. [Install](software--docs-alohamini-install.md) — prepare the environment, serial port permissions, and Hugging Face login.
2. Pick your robot workflow:
   - [AM-ARM200](software--docs-alohamini-am-arm200.md) — single-arm workflow on one PC: calibration, teleoperation, dataset recording, training, and evaluation.
   - [AlohaMini 1 / 2 / 2 Pro](software--docs-alohamini-alohamini.md) — dual-arm workflow with Pi + PC: calibration, teleoperation, dataset recording, training, and evaluation.

### References

| Reference | Use it for |
|-----------|------------|
| [Hardware Profiles](software--docs-alohamini-profiles.md) | `--arm_profile` and `--robot_model` flag meanings |
| [Command Cheat Sheet](software--docs-alohamini-commands.md) | Copy-paste commands for setup, host, teleoperation, recording, training, evaluation, and common checks |
| [Debug Tools](software--examples-debug-readme.md) | Low-level motor, wheel, lift axis, servo ID, phase, midpoint, torque, and scripted-action debug functions |

---

## Team & Contact

AlohaMini is created by **Li Yiteng** and **Wu Zhiyong**.

- Email: liyiteng+github@gmail.com
- WeChat: liyiteng

## Acknowledgements

- [LeRobot](https://github.com/huggingface/lerobot) — the software stack this repository targets
- [ALOHA](https://tonyzhaozh.github.io/aloha/) — the bimanual teleoperation paradigm
- [SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100) — pioneered the low-cost open arm design pattern
