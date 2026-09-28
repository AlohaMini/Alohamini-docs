# Policy training

For other policies and advanced training methods, see the [Policies and training](policies.md), which includes configuration and usage instructions for each model.

Applicable models: **AlohaMini 2 / 2 Pro**. Please select one of the two examples with model numbers to execute. Complete entry process: [2 Tutorials](alohamini2.md) · [2 Pro Tutorial](alohamini2pro.md).

This chapter takes the **ACT** training entrance provided by the project as a starting point. Training reads saved data sets and does not require the robot Host or leader arm to be continuously online.

## 1. Check before training

- Completed [Data review](learning.md), task, action and camera data are complete.
- The training machine has the same software environment installed and can find the data set.
- Data comes from matching robot configurations; 16D interface for Gen 1, 18D interface for Gen 2 and Pro.
- The current terminal is set to the correct `HF_USER`.
- When using the CUDA examples, GPU and PyTorch CUDA environments are available.

```bash
python -c "import torch; print(torch.cuda.is_available())"
```

This only verifies that CUDA is accessible and does not guarantee that a specific batch size or policy will run in video memory.

## 2. Start ACT training

The following example reads the data set from the previous chapter, outputs the model to a separate directory, and closes W&B and model upload:

**AlohaMini 2**

```bash
lerobot-train \
  --dataset.repo_id=$HF_USER/am2_pick_place \
  --policy.type=act \
  --output_dir=outputs/train/act_am2_pick_place \
  --job_name=act_am2_pick_place \
  --policy.device=cuda \
  --policy.push_to_hub=false \
  --wandb.enable=false \
  --dataset.video_backend=pyav
```

**AlohaMini 2 Pro**

```bash
lerobot-train \
  --dataset.repo_id=$HF_USER/am2pro_pick_place \
  --policy.type=act \
  --output_dir=outputs/train/act_am2pro_pick_place \
  --job_name=act_am2pro_pick_place \
  --policy.device=cuda \
  --policy.push_to_hub=false \
  --wandb.enable=false \
  --dataset.video_backend=pyav
```

If a local data directory is specified when recording, add:

**AlohaMini 2**

```text
--dataset.root=/absolute/path/to/am2_pick_place
```

**AlohaMini 2 Pro**

```text
--dataset.root=/absolute/path/to/am2pro_pick_place
```

When using a custom path, don't mistakenly change `repo_id` to a local directory; these two fields serve different purposes.

## 3. Parameter description

| parameters | function | Pay attention when adjusting |
| --- | --- | --- |
| `dataset.repo_id` | Identify the training data set | Must correspond to actual data |
| `dataset.root` | Point to local data directory | Confirm that the data has been completely copied during cross-machine training |
| `policy.type=act` | Use ACT policies | Changing policies will change the model and dependency requirements |
| `policy.device=cuda` | Train on CUDA devices | Need to correspond to the operating environment |
| `output_dir` | Checkpoint and training product directory | Use new directories for new experiments to avoid confusing results |
| `job_name` | Experiment name | Suggestions include task or configuration differences |
| `policy.push_to_hub=false` | Close model upload | Local checkpoints are retained after training is completed |
| `wandb.enable=false` | Turn off W&B log integration | Does not affect local training output |
| `dataset.video_backend=pyav` | Video decoding using PyAV | When decoding an error, first check the data video and dependencies. |

The training command reads the data set features without adding the `robot.robot_model` parameter. The two examples read corresponding data respectively and use independent model directories; the same 18-dimensional interface does not mean that the policy can be directly deployed across models.

This example follows the training defaults of the policy and does not provide additional learning rate, number of steps, or success rate that have not been verified for this task. When it is necessary to adjust the training hyperparameters, the current training entry and policy configuration shall prevail, and the changes shall be recorded.

## 4. Find evaluable checkpoints

The project example uses the following path structure:

**AlohaMini 2**

```text
outputs/train/act_am2_pick_place/
└── checkpoints/
    └── 020000/
        └── pretrained_model/
```

**AlohaMini 2 Pro**

```text
outputs/train/act_am2pro_pick_place/
└── checkpoints/
    └── 020000/
        └── pretrained_model/
```

`020000` is just an example step number. Please check the actual output, select the `pretrained_model` directory that has been saved completely, and then pass it to the evaluation script. Do not copy a sample path that has not been generated yet.

To resume training after it is interrupted, see the current `lerobot-train --help` and software repository recovery training instructions. The **training recovery parameters and the `--resume` recorded in the data set are not in the same workflow.** Do not directly delete the existing output directory to bypass the error.

## 5. Upload and cross-machine training

When you need to upload a model, complete the Hugging Face login first and use it in the training configuration:

```text
--policy.push_to_hub=true
--policy.repo_id=你的用户名/模型名称
```

The data set and the policy model are different warehouses. When copying the recording data to another training machine, keep the video, metadata and numerical data migrated together; after training, bring the complete model directory back to the evaluation machine.

## 6. How to determine the direction of the next round of improvements

| Observations | Priority check |
| --- | --- |
| Feature dimension error reported when training starts | Dataset model, camera name, state/action features |
| Video cannot be decoded | Whether the data is saved completely, PyAV and FFmpeg environment |
| Insufficient video memory | Current policy, batch size, image configuration and device memory |
| The training can be completed, but the real action is wrong | Calibration, preprocessing, model and evaluation scenarios |
| Only successful at a few object locations | Whether teaching covers actual changes in tasks |
| Fetching succeeded but subsequent placement failed | Complete task chain and final stage demonstration quality in the data |

The decrease in training loss can only indicate an indicator in the optimization process, and the task effect must be checked through [Hardware evaluation](evaluation.md). Record the failure stage before deciding to supplement data or adjust training configuration.


## 7. AM-ACT: Mobile tasks and pure visual training

[Pro Quick Start](yuque/pro-quickstart.md) gives a set of AM-ACT examples of "right arm operation, left arm stationary, and chassis participating in motion". Based on ACT, AM-ACT supports fixed action dimensions, discrete classification of partial action dimensions, and pure visual input. Whether to use these options depends on the actual collection task.

### 7.1 Check the data characteristics first

1. Confirm the 18-dimensional full machine data from this machine and check the action name and sequence in `meta/info.json`.
2. Determine which joints are involved in the task and which ones remain immobile. Just because the left arm is fixed in the example, don't copy the tasks for your own arms.
3. Check camera keys. The example below uses `forward` and `wrist_right`; if your delivery configuration uses `head_top`, you should first check the actual `observation.images.*` in the data set.
4. Confirm the unit, value and statistical distribution of the movement action, and then consider the discrete classification parameters.

### 7.2 Create an independent pure visual data set

The following takes the Pro data set as an example. Standard 2 can also use conversion tools, but the source data, target directory, and model directory should remain separate.

```bash
python -m lerobot.scripts.create_alohamini_visual_only_dataset \
  --source "$HOME/user/am2pro_pick_place" \
  --target "$HOME/user/am2pro_pick_place_visual_only" \
  --keep-camera forward \
  --keep-camera wrist_right \
  --drop-state \
  --mode copy \
  --dry-run
```

First check the preview to list the Keep camera and Remove features. After confirmation, remove the last line `--dry-run`, remove the line continuation character at the end of the previous line, and then perform the conversion.

- `--source` must point to an actual existing LeRobot v3 dataset.
- `--target` must be a new directory that does not yet exist.
- `--drop-state` removes `observation.state`, keeping the action tag. AM-ACT supports this input method, but other policies may not support it.
- `--mode copy` uses a separate copy of the file; the tool's default automatic mode gives priority to creating hard links.
- After the conversion is complete, check the target dataset again to confirm that the number of images, actions, and episodes is as expected.

### 7.3 Starting from the configuration of non-fixed action dimensions

The following example first retains the continuous regression of all movements to avoid fixing the left arm or forcibly classifying the left arm before checking the data. The number of steps and batch size are adjustable examples and do not represent specific success rates.

```bash
lerobot-train \
  --dataset.repo_id=local/am2pro_pick_place_visual_only \
  --dataset.root="$HOME/user/am2pro_pick_place_visual_only" \
  --dataset.video_backend=pyav \
  --policy.type=am_act \
  --policy.device=cuda \
  --policy.fixed_action_dims='[]' \
  --policy.discrete_action_dims='[]' \
  --policy.push_to_hub=false \
  --save_checkpoint_to_hub=false \
  --output_dir=outputs/train/am_act_am2pro_pick_place \
  --job_name=am_act_am2pro_pick_place \
  --steps=100000 \
  --batch_size=2 \
  --wandb.enable=false
```

### 7.4 Understanding classification parameters in the delivery tutorial

| parameters | Task example | Conditions of use |
| --- | --- | --- |
| `fixed_action_dims` | `[0,1,2,3,4,5,6]` | The left arm is always stationary during this task; these dimensions are not involved in training and output zero in the normalized space. |
| `discrete_action_dims` | `[14,15,16]` | The data feature sequence must be checked first; here it is used for the second generation chassis movement |
| `discrete_action_values` | `[[-0.15,0,0.15],[-0.15,0,0.15],[-45,0,45]]` | Use the physical unit of the data set to match the value of the collection action |
| `discrete_action_class_weights` | `[[3,1,1.5],[3,1,2],[2,1,2]]` | Each set of weights corresponds to the category order of the dimension. |
| `discrete_action_loss_weight` | `1.0` | The weight of classification loss needs to be adjusted based on experiments |

Zero of the **normalized space is not equal to physical joint angle zero.** Do not treat `fixed_action_dims` as a mechanical emergency stop or hardware locking mechanism.

If you need to use the above discrete settings, replace the corresponding empty list in the training command, and add the category and weight parameters; first check whether the configuration meets the task on a small amount of data.

### 7.5 What should I do if `zero std` appears?

`Action dimension 15 has zero std and cannot be classified` means that the action dimension selected as a discrete classification has no statistical change. In the task example, there may be no left and right panning during collection, but you should also check whether the data conversion and dimension selection are correct.

1. Check the actual characteristics corresponding to action 15 rather than just guessing by number.
2. Check the raw data and statistics to confirm whether this dimension is constant.
3. When the task requires such movements, data containing the corresponding movements are supplemented and the statistics are regenerated.
4. When the task does not originally require such movements, the discrete and fixed dimension configurations are redesigned to keep the category list length consistent.

Do not modify statistical values directly to make the error disappear. After the training is completed, press [Hardware evaluation](evaluation.md) using the actual generated checkpoints, and keep the robot model, camera name and training data consistent.

Complete parameter definition: [AM-ACT parameter description](upstream/software--src-lerobot-policies-am_act-readme.md).
