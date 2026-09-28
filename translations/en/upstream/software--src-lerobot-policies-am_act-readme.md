# AM-ACT

[← Tutorial Library](../tutorial-library.md) · **policies and Models**

This section introduces the general functions of LeRobot. Please configure the example according to the target robot, data set and operating environment; before using it with AlohaMini 2 / 2 Pro, you need to confirm the hardware and interface compatibility.

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
