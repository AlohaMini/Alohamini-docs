# Real-Time Chunking (RTC)

[← Tutorial Library](../tutorial-library.md) · **policies and Models**

This section introduces the general functions of LeRobot. Please configure the example according to the target robot, data set and operating environment; before using it with AlohaMini 2 / 2 Pro, you need to confirm the hardware and interface compatibility.

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
