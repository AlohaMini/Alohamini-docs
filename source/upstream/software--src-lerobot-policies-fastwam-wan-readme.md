# FastWAM `wan` package

[← 教程资料库](../tutorial-library.md) · **策略与模型 / 原文全文**

本文保留软件仓库的通用或进阶教程。示例中的机器人、数据集、路径和运行环境需按实际配置选择，不代表已经在 AlohaMini 2 / 2 Pro 上验证。

来源：[liyiteng/lerobot_alohamini · `src/lerobot/policies/fastwam/wan/README.md`](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/src/lerobot/policies/fastwam/wan/README.md) · 版本 `7843e588` · [下载未经改写的源文档](../_static/upstream-originals/software/src/lerobot/policies/fastwam/wan/README.md.txt)

本页保留原文语言及全部段落、表格和代码；仅调整标题层级、页面组件、代码围栏格式、相对链接和媒体路径。原文中的价格、性能和运行结果属于该版本记录。

---


This package holds FastWAM's model implementation. It mixes a small **vendored
subset of the official Wan2.2 source tree** with FastWAM's own code, kept flat in
a single directory.

## Vendored from Wan2.2

- Upstream repository: https://github.com/Wan-Video/Wan2.2
- Upstream commit: `42bf4cfaa384bc21833865abc2f9e6c0e67233dc`
- License: Apache-2.0, matching the license in `LICENSE.txt` from the upstream repository

Copied files:

- `model.py` (was `wan/modules/model.py`), trimmed: the flash-attention path
  (the vendored `attention.py` and the block/model `forward`s) was removed.
  FastWAM's DiT uses SDPA instead (see `video_dit.py`).
- `get_sampling_sigmas` in `video_dit.py` (was `wan/utils/fm_solvers.py`), inlined
  next to its only caller.

This subset only backs FastWAM's **custom MoT video DiT**. The Wan2.2 VAE,
UMT5 text encoder, and tokenizer are no longer vendored - they come from
`diffusers.AutoencoderKLWan`, `transformers.UMT5EncoderModel`, and
`transformers.AutoTokenizer` (see `components.py` and `adapters.py`).

## FastWAM's own code

- `video_dit.py` builds on `model` (`sinusoidal_embedding_1d`, `rope_params`,
  `rope_apply`, …) and computes attention with SDPA (`fastwam_masked_attention`). Its
  `WanContinuousFlowMatchScheduler` uses `get_sampling_sigmas` for Wan-compatible
  inference timesteps.
- `components.py` / `adapters.py` load the VAE, text encoder, tokenizer, and the
  custom DiT weights.
- `modular.py` defines the FastWAM model (`ActionDiT`, `MoT`, `FastWAM`, …).
