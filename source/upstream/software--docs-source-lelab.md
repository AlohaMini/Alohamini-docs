# LeLab - LeRobot Guide

[← 教程资料库](../tutorial-library.md) · **环境与训练工具**

本节介绍 LeRobot 的通用功能。请按目标机器人、数据集和运行环境配置示例；用于 AlohaMini 2 / 2 Pro 前，需要确认硬件与接口兼容性。

[项目参考：liyiteng/lerobot_alohamini](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/lelab.mdx)

---


LeLab is a graphical user interface built on top of the LeRobot library, designed to make robotics accessible without needing to memorize CLI commands. From a single app you can configure your robot, teleoperate it, collect datasets, train policies locally or on cloud GPUs via HF Jobs, and deploy trained models back onto your robot. It's the easiest way to go from an unboxed SO-101 to a working policy, and a great companion for anyone learning the LeRobot workflow. Source code and issues live on GitHub: [huggingface/leLab](https://github.com/huggingface/leLab).

> [!TIP]
> For now LeLab is compatible only with SO-ARM101

[观看视频](https://www.youtube.com/watch?v=VqyKUuW9V1g)

## Installation

Requires [`uv`](https://docs.astral.sh/uv/getting-started/installation/). Install and launch in one command:

```
uv tool install git+https://github.com/huggingface/leLab.git && lelab
```

After install, run `lelab` from your terminal anytime to start the app.

## Features

- **Add robots** — Select arm type (leader/follower), calibrate each joint from the middle position, and attach cameras.
- **Teleoperation** — Control the follower arm with the leader and see a live 3D visualization of the arms.
- **Dataset recording** — Define a task description, number of episodes, and episode/reset durations. Press spacebar to advance between episodes. 30+ episodes recommended.
- **Local training** — Train a policy directly on your own machine with a selected dataset, policy type, batch size, and step count.
- **Cloud training with HF Jobs** — Train on powerful GPUs via [HF Jobs](https://huggingface.co/docs/huggingface_hub/en/guides/jobs) with transparent pricing. Run `hf auth login` first. See the [Compute HW Guide](software--docs-source-hardware_guide.md) for hardware/batch size tips.
- **Training visualization** — Watch progress live in the app, with checkpoints saved automatically.
- **Run trained policies** — Pick any model from your jobs list and run inference on your robot with one click.
- **Use community datasets** — Provide any Hugging Face dataset ID to train on datasets you didn't record yourself.
