# Real-Time Chunking (RTC)

[← 教程资料库](../tutorial-library.md) · **策略与模型**

本节介绍 LeRobot 的通用功能。请按目标机器人、数据集和运行环境配置示例；用于 AlohaMini 2 / 2 Pro 前，需要确认硬件与接口兼容性。

---


This module contains the LeRobot implementation of **Real-Time Chunking (RTC)**, an inference-time technique for flow-matching based policies.

**Note**: RTC is not a policy itself, but rather an inference enhancement that works with flow-matching based policies including [π₀](https://github.com/liyiteng/lerobot_alohamini/tree/7843e5888366eaa553630e2f9d5539505a62dddf/docs/pi0), [π₀.₅](https://github.com/liyiteng/lerobot_alohamini/tree/7843e5888366eaa553630e2f9d5539505a62dddf/docs/pi05), and [SmolVLA](https://github.com/liyiteng/lerobot_alohamini/tree/7843e5888366eaa553630e2f9d5539505a62dddf/docs/smolvla).

---

## Citation

If you use Real-Time Chunking in your work, please cite:

```bibtex
@misc{openpi2024,
  author       = {Physical Intelligence Lab},
  title        = {OpenPI: PyTorch Implementation of π0 and π0.5 Policies},
  year         = {2024},
  publisher    = {GitHub},
  howpublished = {\url{https://github.com/Physical-Intelligence/openpi}},
  license      = {Apache-2.0}
}

@misc{black2025realtimeexecutionactionchunking,
      title={Real-Time Execution of Action Chunking Flow Policies},
      author={Kevin Black and Manuel Y. Galliker and Sergey Levine},
      year={2025},
      eprint={2506.07339},
      archivePrefix={arXiv},
      primaryClass={cs.RO},
      url={https://arxiv.org/abs/2506.07339},
}
```

---

## License

This implementation follows the **Apache 2.0 License**, consistent with the LeRobot project.
