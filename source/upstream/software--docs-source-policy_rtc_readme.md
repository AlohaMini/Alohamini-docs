# Real-Time Chunking (RTC)

[← 教程资料库](../tutorial-library.md) · **策略与模型 / 原文全文**

本文保留软件仓库的通用或进阶教程。示例中的机器人、数据集、路径和运行环境需按实际配置选择，不代表已经在 AlohaMini 2 / 2 Pro 上验证。

来源：[liyiteng/lerobot_alohamini · `docs/source/policy_rtc_README.md`](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_rtc_README.md) · 版本 `7843e588` · [下载未经改写的源文档](../_static/upstream-originals/software/docs/source/policy_rtc_README.md.txt)

本页保留原文语言及全部段落、表格和代码；仅调整标题层级、页面组件、代码围栏格式、相对链接和媒体路径。原文中的价格、性能和运行结果属于该版本记录。

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
