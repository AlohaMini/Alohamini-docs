# lerobot_alohamini

[← 教程资料库](../tutorial-library.md) · **环境与训练工具**

本节介绍 LeRobot 的通用功能。请按目标机器人、数据集和运行环境配置示例；用于 AlohaMini 2 / 2 Pro 前，需要确认硬件与接口兼容性。

[项目参考：liyiteng/lerobot_alohamini](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/README.md)

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
