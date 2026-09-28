# Data collection and inspection

Applicable models: **AlohaMini 2 / 2 Pro**. Run only the example for your robot.

Through leader arm teaching, camera images, robot status and actions are recorded as data sets. By recording a short test first and reviewing it before expanding it to a formal demonstration, errors in camera mapping, task description or save paths can be discovered earlier.

## Preparation before collection

- Pi Host is running normally, and `robot_model` is consistent at both ends.
- The leader arm calibration is completed, and the teleoperation can complete the task stably.
- The separate teleoperation client has been exited to avoid contention for control.
- Confirm the enabled camera name, angle of view, frame rate and resolution.
- Set `HF_USER` in the current terminal of the PC and prepare enough local storage space.

All commands are run from the `lerobot_alohamini` root directory:

```bash
conda activate lerobot_alohamini
export HF_USER="your-hf-username"
```

## 1. First record a short test

The following second-generation example collects 1 test data of 10 seconds each and 10 FPS, and only saves it locally:

**AlohaMini 2**

```bash
python examples/alohamini/record_bi.py \
  --dataset.repo_id $HF_USER/am2_smoke_test \
  --dataset.num_episodes 1 \
  --dataset.fps 10 \
  --dataset.episode_time_s 10 \
  --dataset.reset_time_s 3 \
  --dataset.single_task "Pick up the object and place it in the tray" \
  --dataset.push_to_hub=false \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2 \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof
```

**AlohaMini 2 Pro**

```bash
python examples/alohamini/record_bi.py \
  --dataset.repo_id $HF_USER/am2pro_smoke_test \
  --dataset.num_episodes 1 \
  --dataset.fps 10 \
  --dataset.episode_time_s 10 \
  --dataset.reset_time_s 3 \
  --dataset.single_task "Pick up the object and place it in the tray" \
  --dataset.push_to_hub=false \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2pro \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof
```

After starting, follow the terminal prompts to operate the leader arm to complete the task. Record the local data set path for log printing; after recording, wait for the data to be saved, and then review the image and status.

This test is used to check the entire acquisition link. The formal data set should use the new name and adopt the fixed sampling configuration from the experimental plan.

## 2. Understand the collection parameters

| parameters | Example | Description |
| --- | --- | --- |
| `dataset.repo_id` | `用户名/am2_pick_place` | Dataset ID; not equivalent to local directory |
| `dataset.num_episodes` | `1` | The number of episodes collected this time |
| `dataset.fps` | `30` | Data set sampling frequency; the single-frequency recorder is controlled at this frequency at the same time |
| `dataset.episode_time_s` | `45` | Recording time of each task |
| `dataset.reset_time_s` | `8` | Scene reset time between two tasks |
| `dataset.single_task` | Natural language task description | Keep consistent with actual teaching goals |
| `dataset.push_to_hub` | `false` | Save locally; the default script will be uploaded, and the example is explicitly closed |
| `dataset.root` | local directory | Optional; specifies where the dataset is created or continued |
| `--resume` | No value switch | Continue recording on existing data sets |

**Episode** is a complete mission demonstration. The reset phase is used to restore the object and robot starting conditions; task actions should occur during the recording phase.

## 3. Formal recording example

After confirming that the short test is normal, record a complete demonstration at 30 FPS and 45 seconds:

**AlohaMini 2**

```bash
python examples/alohamini/record_bi.py \
  --dataset.repo_id $HF_USER/am2_pick_place \
  --dataset.num_episodes 1 \
  --dataset.fps 30 \
  --dataset.episode_time_s 45 \
  --dataset.reset_time_s 8 \
  --dataset.single_task "Pick up the object and place it in the tray" \
  --dataset.push_to_hub=false \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2 \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof
```

**AlohaMini 2 Pro**

```bash
python examples/alohamini/record_bi.py \
  --dataset.repo_id $HF_USER/am2pro_pick_place \
  --dataset.num_episodes 1 \
  --dataset.fps 30 \
  --dataset.episode_time_s 45 \
  --dataset.reset_time_s 8 \
  --dataset.single_task "Pick up the object and place it in the tray" \
  --dataset.push_to_hub=false \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2pro \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof
```

`num_episodes` can be increased according to the task plan. This guide does not set a number of demonstrations to ensure successful training; first judge whether the data covers the task through review and small-scale training, and then increase the number of demonstrations to make it easier to locate the direction of improvement.

The two examples use independent data set names; the names will not automatically set the model, and still need to be checked `robot.robot_model`. The first generation also needs to switch to the SO leader arm profile and use independent data set names to avoid mixing data of different dimensions.

## 4. Custom catalog and renewal

When you need to fix the local location, add the following to the first recording command:

**AlohaMini 2**

```text
--dataset.root /absolute/path/to/am2_pick_place
```

**AlohaMini 2 Pro**

```text
--dataset.root /absolute/path/to/am2pro_pick_place
```

When continuing to record, keep the same `repo_id`, `root`, model, camera characteristics and sampling configuration, and add: at the end of the complete recording command:

```text
--resume
```

Passing just `--resume` will not automatically select the data set you want. Misusing a new path may result in the original data not being found, and misusing an existing but incompatible data set may result in feature mismatches; first check the path in the log before collecting.

## 5. Choose single or multi-channel recorder

| entrance | Control and sampling methods | Applicable situations |
| --- | --- | --- |
| `record_bi.py` | Both control and data sampling use `dataset.fps` | Go through the standard process first |
| `record_bi_multirate.py` | 50 Hz control, fresh and aligned frames delivered at data set frequency | It is necessary to separate the control frequency and camera sampling |

Multi-frequency recording uses the same main parameters, just change the entrance, for example:

**AlohaMini 2**

```bash
python examples/alohamini/record_bi_multirate.py \
  --dataset.repo_id $HF_USER/am2_multirate_test \
  --dataset.num_episodes 1 \
  --dataset.fps 30 \
  --dataset.episode_time_s 45 \
  --dataset.reset_time_s 8 \
  --dataset.single_task "Pick up the object and place it in the tray" \
  --dataset.push_to_hub=false \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2 \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof
```

**AlohaMini 2 Pro**

```bash
python examples/alohamini/record_bi_multirate.py \
  --dataset.repo_id $HF_USER/am2pro_multirate_test \
  --dataset.num_episodes 1 \
  --dataset.fps 30 \
  --dataset.episode_time_s 45 \
  --dataset.reset_time_s 8 \
  --dataset.single_task "Pick up the object and place it in the tray" \
  --dataset.push_to_hub=false \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2pro \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof
```

The recorder collects data at a target frame rate, so if the actual camera is only 29.5 Hz, the wall clock recording time may be slightly longer than the nominal time corresponding to 30 FPS. The current documentation lists abort conditions as camera stalling, multi-camera time difference exceeding 50 ms, state alignment error exceeding 100 ms, or fresh frame rate falling below 90% of target. If you encounter an abort, you should check the logs for the specific reason. There is no need to repeat old images to get the frame rate.

## 6. Review the data set

Under the default data location, view episode 0:

**AlohaMini 2**

```bash
lerobot-dataset-viz \
  --repo-id $HF_USER/am2_pick_place \
  --episode-index 0 \
  --display-compressed-images
```

**AlohaMini 2 Pro**

```bash
lerobot-dataset-viz \
  --repo-id $HF_USER/am2pro_pick_place \
  --episode-index 0 \
  --display-compressed-images
```

Visualization is used to view recorded data and does not send robot actions. When using a custom directory, add `--root /absolute/path/to/am2_pick_place` to the full visualization command above. Note that the visualization tool uses `--root` and the recording script uses `--dataset.root`.

### What to check for each batch of data

| Check items | Check specifically |
| --- | --- |
| Camera name and angle of view | The left and right wrists are not connected backwards, and the task object is within the required field of view. |
| picture continuity | No long freezes, black screens or error placeholder images |
| Action integrity | Including task phases such as approach, grabbing, carrying and placing |
| Status and Action | There are no missing dimensions or abnormal jumps due to model errors. |
| Task text | The description is consistent with the actual goal of this teaching |
| reset | The starting scene can be reproduced without mistakenly recording the reset action as a task. |

It is recommended to establish collection records: date, model, software version, camera configuration, task text, success and failure clips, and on-site changes. When a training problem occurs, it can be traced back to which configuration the data came from.

## 7. Playback on real device

**playback drives real robots.** first checks the movement trajectory, initial position and surrounding space, starts the Host that matches the model, and then runs it on the PC:

**AlohaMini 2**

```bash
python examples/alohamini/replay_bi.py \
  --dataset.repo_id $HF_USER/am2_pick_place \
  --dataset.episode 0 \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2
```

**AlohaMini 2 Pro**

```bash
python examples/alohamini/replay_bi.py \
  --dataset.repo_id $HF_USER/am2pro_pick_place \
  --dataset.episode 0 \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2pro
```

When using a custom recording directory, add the same `--dataset.root /absolute/path/to/am2_pick_place`. If you just want to check the data content, use the visualization in the previous section.

## Next step

After passing the data review, enter the [ACT policy training](training.md), and then use the [Hardware evaluation](evaluation.md) to verify the training results.
