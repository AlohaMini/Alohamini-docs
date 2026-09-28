# LeLab - LeRobot Guide

[← 教程资料库](../tutorial-library.md) · **环境与训练工具 / 原文全文**

本文保留软件仓库的通用或进阶教程。示例中的机器人、数据集、路径和运行环境需按实际配置选择，不代表已经在 AlohaMini 2 / 2 Pro 上验证。

来源：[liyiteng/lerobot_alohamini · `docs/source/lelab.mdx`](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/lelab.mdx) · 版本 `7843e588` · [下载未经改写的源文档](../_static/upstream-originals/software/docs/source/lelab.mdx.txt)

本页保留原文语言及全部段落、表格和代码；仅调整标题层级、页面组件、代码围栏格式、相对链接和媒体路径。原文中的价格、性能和运行结果属于该版本记录。

---


LeLab is a graphical user interface built on top of the LeRobot library, designed to make robotics accessible without needing to memorize CLI commands. From a single app you can configure your robot, teleoperate it, collect datasets, train policies locally or on cloud GPUs via HF Jobs, and deploy trained models back onto your robot. It's the easiest way to go from an unboxed SO-101 to a working policy, and a great companion for anyone learning the LeRobot workflow. Source code and issues live on GitHub: [huggingface/leLab](https://github.com/huggingface/leLab).

> [!TIP]
> For now LeLab is compatible only with SO-ARM101

[观看原文视频](https://www.youtube.com/watch?v=VqyKUuW9V1g)

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
