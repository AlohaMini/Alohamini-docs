# Policies and training

This page summarizes policies and models for learning and development. For the initial training of AlohaMini, you can still verify the data and equipment along the [ACT Main Line](training.md); other policies are configured according to their respective dependencies, input formats, and running interfaces.

## 1. Select the reading entrance

| policy/Topic | Tutorial entrance | Reading highlights |
| --- | --- | --- |
| ACT | [Complete tutorial](upstream/software--docs-source-act.md) | action chunk, training and evaluation |
| AM-ACT | [Custom implementation instructions](upstream/software--src-lerobot-policies-am_act-readme.md) | Discrete action dimensions, fixed dimensions, loss groups, and output scaling |
| Diffusion | [Implementation instructions](upstream/software--docs-source-policy_diffusion_readme.md) | Implementation and parameter description |
| SmolVLA | [Complete tutorial](upstream/software--docs-source-smolvla.md) | Model dependencies, fine-tuning, inference and data |
| Pi0 / Pi0.5 | [Pi0](upstream/software--docs-source-pi0.md)、[Pi0.5](upstream/software--docs-source-pi05.md) | LeRobot’s built-in implementation is different from [Standalone OpenPI](pi05.md) |
| Pi0 FAST | [Complete tutorial](upstream/software--docs-source-pi0fast.md) | Action representation and model use |
| GR00T | [Complete tutorial](upstream/software--docs-source-groot.md) | Modality, configuration and training |
| RTC | [Complete tutorial](upstream/software--docs-source-rtc.md) | Asynchronous action blocks and compatibility policies |
| Multitasking DiT | [Complete tutorial](upstream/software--docs-source-multi_task_dit.md) | Multitasking configuration and data |
| FastWAM | [Complete tutorial](upstream/software--docs-source-fastwam.md) | Models and exclusive dependencies |
| MolmoAct2 | [Complete tutorial](upstream/software--docs-source-molmoact2.md) | Model input, fine-tuning and use |
| VLA-JEPA | [Complete tutorial](upstream/software--docs-source-vla_jepa.md) | Configure, train and deploy |
| EO-1 / Evo-1 | [EO-1](upstream/software--docs-source-eo1.md)、[Evo-1](upstream/software--docs-source-evo1.md) | Corresponding implementation version and dependencies |
| LingBot-VA / Wall-OSS / XVLA | [LingBot-VA](upstream/software--docs-source-lingbot_va.md)、[Wall-OSS](upstream/software--docs-source-walloss.md)、[XVLA](upstream/software--docs-source-xvla.md) | Data and interfaces specific to each model |
| TD-MPC / VQ-BeT / SARM | [TD-MPC](upstream/software--docs-source-policy_tdmpc_readme.md)、[VQ-BeT](upstream/software--docs-source-policy_vqbet_readme.md)、[SARM](upstream/software--docs-source-sarm.md) | Part of the README is for reference, please read the corresponding text and code carefully. |

[View all policy tutorials](library-policies.md). Before using other policies, please confirm the input, action dimensions and inference interface of AlohaMini, and complete the real machine verification.

## 2. Before moving from ACT data to other policies

1. Keep a copy of the validated dataset and ACT baseline documenting cameras, feature order, action units, and calibration.
2. Install the corresponding extras according to the model tutorial, and check the basic weights and usage conditions.
3. Confirm that the image name, language task field, state/action dimension, and normalized statistics are consistent with the model requirements.
4. Choose independent output directories and experiment names to avoid overwriting existing checkpoints.
5. First run a small-scale data loading and training check to confirm that the log, loss, and save results are normal.
6. Check the inference interface, control frequency, and action block policy when deploying; ACT does not use the RTC path.

The example batch size, number of training steps, and memory records depend on the specific model and training tasks and cannot be used as resource commitments for all devices.

## 3. Unique parameters of AM-ACT

AM-ACT allows some action dimensions to be categorical, while the remaining dimensions are still trained as continuous values.

| parameters | function |
| --- | --- |
| `fixed_action_dims` | Dimensions that are excluded from training and fixed to zero in the normalized space |
| `discrete_action_dims` | Dimensional indexing using categorical predictions |
| `discrete_action_values` | The physical action values corresponding to each category are in the same order as the category. |
| `discrete_action_class_weights` | Corresponding category weight |
| `discrete_action_loss_weight` | Classification loss ratio |
| `action_loss_groups` / `action_loss_weights` | Continuous dimension grouping and group weights |
| `observation_state_dims` | Select a subset of input states |
| `inference_action_scale_dims` / `inference_action_scale` | Scale the specified output after denormalization |

The example configuration uses `[14,15,16]` as a discrete dimension example; whether it corresponds to the chassis should be judged based on the actual data feature sequence. Zero in normalized space also does not necessarily equal physical zero action. For complete training commands and loading methods, see [AM-ACT detailed configuration](upstream/software--src-lerobot-policies-am_act-readme.md).

## 4. Data and training tools

- [Dataset v3 format](upstream/software--docs-source-lerobot-dataset-v3.md), [Migrate old data](upstream/software--docs-source-porting_datasets_v3.md)
- [Dataset editing tools](upstream/software--docs-source-using_dataset_tools.md), [action expression](upstream/software--docs-source-action_representations.md)
- [PEFT training](upstream/software--docs-source-peft_training.md), [Multi-GPU training](upstream/software--docs-source-multi_gpu_training.md)
- [inference Tutorial](upstream/software--docs-source-inference.md), [Asynchronous inference](upstream/software--docs-source-async.md)
- [Human-in-the-loop data collection](upstream/software--docs-source-hil_data_collection.md), [HIL-SERL](upstream/software--docs-source-hilserl.md)

[Tutorial Library] Summarizes various topics (tutorial-library.md), including other robot and simulation benchmark examples.
