# policy_fastwam_README

[← 教程资料库](../tutorial-library.md) · **策略与模型 / 原文全文**

本文保留软件仓库的通用或进阶教程。示例中的机器人、数据集、路径和运行环境需按实际配置选择，不代表已经在 AlohaMini 2 / 2 Pro 上验证。

来源：[liyiteng/lerobot_alohamini · `docs/source/policy_fastwam_README.md`](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_fastwam_README.md) · 版本 `7843e588` · [下载未经改写的源文档](../_static/upstream-originals/software/docs/source/policy_fastwam_README.md.txt)

本页保留原文语言及全部段落、表格和代码；仅调整标题层级、页面组件、代码围栏格式、相对链接和媒体路径。原文中的价格、性能和运行结果属于该版本记录。

---

## Research Paper

Paper: https://arxiv.org/abs/2603.16666

## Repository

Code: https://github.com/yuantianyuan01/FastWAM

Project page: https://yuantianyuan01.github.io/FastWAM/

## Citation

```bibtex
@article{yuan2026fastwam,
  title = {Fast-WAM: Do World Action Models Need Test-time Future Imagination?},
  author = {Tianyuan Yuan and Zibin Dong and Yicheng Liu and Hang Zhao},
  journal = {arXiv preprint arXiv:2603.16666},
  year = {2026},
  url = {https://arxiv.org/abs/2603.16666}
}
```

## Additional Resources

Base video model: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B

Released upstream checkpoints: https://huggingface.co/yuanty/fastwam

## Results

Evaluated on LIBERO with [`ZibinDong/fastwam_libero_uncond_2cam224`](https://huggingface.co/ZibinDong/fastwam_libero_uncond_2cam224):

| Suite          | Success rate | n_episodes |
| -------------- | -----------: | ---------: |
| libero_spatial |        97.6% |        500 |
| libero_object  |        99.0% |        500 |
| libero_goal    |        95.0% |        500 |
| libero_10      |        94.0% |        500 |
| **average**    |    **96.4%** |       2000 |

Reproduce: `lerobot-eval --policy.path=ZibinDong/fastwam_libero_uncond_2cam224 --policy.device=cuda --policy.torch_dtype=float32 --policy.n_action_steps=10 --env.type=libero --env.task=libero_spatial --env.observation_height=256 --env.observation_width=256 --eval.batch_size=1 --eval.n_episodes=50 --seed=0 --env.episode_length=300`.

For LIBERO-10, use `--env.task=libero_10 --env.episode_length=600`:

```bash
lerobot-eval \
    --policy.path=ZibinDong/fastwam_libero_uncond_2cam224 \
    --policy.device=cuda \
    --policy.torch_dtype=float32 \
    --policy.n_action_steps=10 \
    --env.type=libero \
    --env.task=libero_10 --env.observation_height=256 --env.observation_width=256 \
    --eval.batch_size=1 \
    --eval.n_episodes=50 \
    --seed=0 --env.episode_length=600
```
