# AM-ACT

[← 教程资料库](../tutorial-library.md) · **策略与模型 / 原文全文**

本文保留软件仓库的通用或进阶教程。示例中的机器人、数据集、路径和运行环境需按实际配置选择，不代表已经在 AlohaMini 2 / 2 Pro 上验证。

来源：[liyiteng/lerobot_alohamini · `src/lerobot/policies/am_act/README.md`](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/src/lerobot/policies/am_act/README.md) · 版本 `7843e588` · [下载未经改写的源文档](../_static/upstream-originals/software/src/lerobot/policies/am_act/README.md.txt)

本页保留原文语言及全部段落、表格和代码；仅调整标题层级、页面组件、代码围栏格式、相对链接和媒体路径。原文中的价格、性能和运行结果属于该版本记录。

---


AM-ACT extends ACT with optional per-dimension classification heads while keeping all other action dimensions as continuous L1 regression outputs. It also supports fixed action dimensions, optional loss groups, visual-only inputs, selecting a subset of `observation.state`, and post-unnormalization action scaling.

## Minimal training command

```bash
conda activate lerobot_alohamini

python -m lerobot.scripts.lerobot_train \
  --dataset.repo_id=local/my_dataset \
  --dataset.root=/path/to/my_dataset \
  --policy.type=am_act \
  --policy.device=cuda \
  --policy.fixed_action_dims='[]' \
  --policy.discrete_action_dims='[14,15,16]' \
  --policy.discrete_action_values='[[-0.15,0,0.15],[-0.15,0,0.15],[-45,0,45]]' \
  --policy.discrete_action_class_weights='[[3,1,1.5],[3,1,2],[2,1,2]]' \
  --policy.discrete_action_loss_weight=1.0 \
  --output_dir=outputs/am_act_run \
  --steps=100000 \
  --batch_size=2
```

The values above are only an example. Dimension indices, physical class values, and class weights must match the dataset.

## Main parameters

| Parameter | Meaning |
| --- | --- |
| `fixed_action_dims` | Action dimensions excluded from training and forced to zero in normalized space. |
| `discrete_action_dims` | Action dimensions trained with classification instead of L1 regression. Empty by default. |
| `discrete_action_values` | Physical class values for each discrete dimension. Their order defines the class order. |
| `discrete_action_class_weights` | Optional cross-entropy weights in the same order as `discrete_action_values`. |
| `discrete_action_loss_weight` | Multiplier applied to the mean classification loss. |
| `action_loss_groups` | Optional named groups used to calculate separately normalized continuous L1 losses. |
| `action_loss_weights` | Optional weights for the named continuous loss groups. |
| `observation_state_dims` | Optional subset of `observation.state`; omit `observation.state` from the dataset features for visual-only training. |
| `inference_action_scale_dims` | Physical action dimensions scaled after unnormalization during inference. |
| `inference_action_scale` | Scale applied to `inference_action_scale_dims`. |

`discrete_action_values` are specified in physical dataset units. AM-ACT converts them to normalized class centers using the active dataset statistics and decodes predicted classes before the standard action unnormalizer.

## Load a trained checkpoint

Use the saved policy like any other LeRobot policy:

```bash
conda activate lerobot_alohamini

python -m lerobot.scripts.lerobot_eval \
  --policy.path=outputs/am_act_run/checkpoints/last/pretrained_model \
  --env.type=<environment_type>
```

For robot-specific evaluation scripts, pass the same checkpoint path through their `--policy.path` option.
