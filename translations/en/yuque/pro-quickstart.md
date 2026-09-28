# AlohaMini2 Pro Quick Start Guide (Minimalist)

[Return to official manual](../official-manual.md)

Applicable models: AlohaMini 2 Pro. Both Raspberry Pi and PC use `alohamini2pro`. The camera name is subject to the actual configuration. Collection, conversion, training and inference must use consistent data feature names. IP, device serial number and checkpoint path need to be replaced with local values. For AM-ACT parameter configuration, see [training instructions](../training.md).

(yq-nyk0n5c9brbh2l4a-v7ZpE)=

## 1. Start the robot (Raspberry Pi)

(yq-nyk0n5c9brbh2l4a-u9c64f6dd)=

1. Power on the robot, click on the screen to find the Raspberry Pi IP address

(yq-nyk0n5c9brbh2l4a-u905dbc62)=

(yq-nyk0n5c9brbh2l4a-u97813f26)=

![AlohaMini2 Pro Quick Start Guide (Minimalist) · Figure 1](../_static/yuque-assets/1d0aa360e6a82bb866ac.png)

(yq-nyk0n5c9brbh2l4a-ub4b758b9)=

(yq-nyk0n5c9brbh2l4a-u167cec8b)=

![AlohaMini2 Pro Quick Start Guide (Minimalist) · Figure 2](../_static/yuque-assets/7829b5282005fe99c0c0.png)

(yq-nyk0n5c9brbh2l4a-ua764b270)=

2. Open the Terminal of the PC and run the SSH login robot (ssh password: 123456):

(yq-nyk0n5c9brbh2l4a-u2e6cf64d)=

(yq-nyk0n5c9brbh2l4a-u631caf59)=

![AlohaMini2 Pro Quick Start Guide (Minimalist) · Figure 3](../_static/yuque-assets/aa57870237cf27999416.png)

(yq-nyk0n5c9brbh2l4a-u49d53336)=

(yq-nyk0n5c9brbh2l4a-u708219e2)=

Log in to the robot via SSH:

```bash
ssh pi5@192.168.xx.xx # 替换为机器人树莓派的IP 
# 密码123456
```

(yq-nyk0n5c9brbh2l4a-ucd4641b0)=

Enter the conda environment and start the main program:

```bash
conda activate lerobot_alohamini
cd lerobot_alohamini

# AlohaMini 2 Pro (AM‑ARM 6‑DoF, sts3250 upgrade)
python -m lerobot.robots.alohamini.alohamini_host \
  --robot_model alohamini2pro
```

(yq-nyk0n5c9brbh2l4a-ufcd21544)=

After the program is started, since the device has been calibrated before leaving the factory, it will automatically skip the calibration process, directly enter the startup state, and start outputting the current information of each joint.

(yq-nyk0n5c9brbh2l4a-ua99f272a)=

(yq-nyk0n5c9brbh2l4a-u5jDr)=

![AlohaMini2 Pro Quick Start Guide (Minimalist) · Figure 4](../_static/yuque-assets/87d7a5a7d571bc31efac.png)

(yq-nyk0n5c9brbh2l4a-ua56e8aa5)=

At this point, the robot body has been started.

(yq-nyk0n5c9brbh2l4a-41ac6baa)=

## 2. Start teleoperation (PC side)

(yq-nyk0n5c9brbh2l4a-u518928bb)=

It is recommended to prepare an Ubuntu22.04 or 24.04 system and complete the environment installation (conda + dependencies) according to the [lerobot_alohamini](https://github.com/liyiteng/lerobot_alohamini) repository.

(yq-nyk0n5c9brbh2l4a-iEOpp)=

### Environment installation:

(yq-nyk0n5c9brbh2l4a-lqC4y)=

### Install Conda

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash
source ~/.bashrc
```

(yq-nyk0n5c9brbh2l4a-u9b48eafd)=

(yq-nyk0n5c9brbh2l4a-ZlAFR)=

### Clone the repository and install dependencies

```bash
git clone https://github.com/liyiteng/lerobot_alohamini.git
cd lerobot_alohamini
conda create -y -n lerobot_alohamini python=3.12
conda activate lerobot_alohamini
pip install -e ".[all]"
pip install pyzmq feetech-servo-sdk
conda install -y ffmpeg=7.1.1 -c conda-forge
```

(yq-nyk0n5c9brbh2l4a-hIwco)=

### Port authorization

```bash
sudo usermod -a -G dialout $USER
# 完成后重启电脑
```

(yq-nyk0n5c9brbh2l4a-rcacZ)=

### 1. Remote arm port query

(yq-nyk0n5c9brbh2l4a-uae015e37)=

a) Randomly select a teleoperation arm and mark it as the left arm with a marker

b) Connect the left arm to the Ubuntu computer and enter the command

```bash
ls /dev/ttyACM*
```

(yq-nyk0n5c9brbh2l4a-ub4420c97)=

Expected output:

(yq-nyk0n5c9brbh2l4a-u55308026)=

(yq-nyk0n5c9brbh2l4a-u99f9e6c6)=

![AlohaMini2 Pro Quick Start Guide (Minimalist) · Figure 5](../_static/yuque-assets/46c9c44e1785e2e0a379.png)

(yq-nyk0n5c9brbh2l4a-u653fa7aa)=

(yq-nyk0n5c9brbh2l4a-uc9501633)=

c) Find the serial number of the left arm driver board

```text
udevadm info --attribute-walk --name=/dev/ttyACM0 | awk -F'"' '/ATTRS{serial}/{print $2; exit}'
```

(yq-nyk0n5c9brbh2l4a-u99353a77)=

Expected output:

(yq-nyk0n5c9brbh2l4a-ufb2ae0fd)=

(yq-nyk0n5c9brbh2l4a-u1fc138ef)=

![AlohaMini2 Pro Quick Start Guide (Minimalist) · Figure 6](../_static/yuque-assets/c2437935a42b7c136ff6.png)

(yq-nyk0n5c9brbh2l4a-u6790971d)=

Among them, 5B3D040583 is the left arm serial number.

(yq-nyk0n5c9brbh2l4a-ua9f1ae66)=

(yq-nyk0n5c9brbh2l4a-u59107e7a)=

d) Use a marker pen to mark the other teleoperation arm as the right arm

(yq-nyk0n5c9brbh2l4a-u6531df06)=

(yq-nyk0n5c9brbh2l4a-u5e5c7f45)=

e) Connect the right arm to the Ubuntu computer and enter the command

```bash
ls /dev/ttyACM*
```

(yq-nyk0n5c9brbh2l4a-u6691eaf9)=

Expected output:

(yq-nyk0n5c9brbh2l4a-u17b88aa7)=

(yq-nyk0n5c9brbh2l4a-u11625bba)=

![AlohaMini2 Pro Quick Start Guide (Minimalist) · Figure 7](../_static/yuque-assets/9a8618c603d9513816eb.png)

(yq-nyk0n5c9brbh2l4a-u43f608d4)=

(yq-nyk0n5c9brbh2l4a-u61a8e900)=

f) Find the serial number of the right arm driver board

```bash
udevadm info --attribute-walk --name=/dev/ttyACM1 | awk -F'"' '/ATTRS{serial}/{print $2; exit}'
```

(yq-nyk0n5c9brbh2l4a-u69928c9d)=

Expected output:

(yq-nyk0n5c9brbh2l4a-u4f1a8584)=

(yq-nyk0n5c9brbh2l4a-u104a7a1a)=

![AlohaMini2 Pro Quick Start Guide (Minimalist) · Figure 8](../_static/yuque-assets/faefd72bf1f05025eb17.png)

(yq-nyk0n5c9brbh2l4a-uec433d06)=

Among them, 5B3D041923 is the right arm serial number.

(yq-nyk0n5c9brbh2l4a-ub1bf088f)=

(yq-nyk0n5c9brbh2l4a-ucbc9873f)=

g) Summary

(yq-nyk0n5c9brbh2l4a-u3e00b3cf)=

Through the above steps, we got the serial number of the left arm driver version (5B3D040583) and the serial number of the right arm driver version (5B3D041923)

(yq-nyk0n5c9brbh2l4a-Ms5KR)=

### 2. Port binding (write udev configuration file)

(yq-nyk0n5c9brbh2l4a-u3390fadb)=

a) Open the configuration file: 90-mydevice.rules

```text
sudo nano /etc/udev/rules.d/90-mydevice.rules
```

(yq-nyk0n5c9brbh2l4a-ud9e8582c)=

b) Write content

```text
SUBSYSTEM=="tty", ATTRS{serial}=="5B3D040583", SYMLINK+="am_arm_leader_left"
SUBSYSTEM=="tty", ATTRS{serial}=="5B3D041923", SYMLINK+="am_arm_leader_right"
```

(yq-nyk0n5c9brbh2l4a-u98fcc83d)=

c) Reload activation

```text
sudo udevadm control --reload-rules
sudo udevadm trigger
```

(yq-nyk0n5c9brbh2l4a-udaadd6f1)=

d) Verify whether it is effective

```text
ls -l /dev/am*
```

(yq-nyk0n5c9brbh2l4a-u475ab649)=

Expected output:

(yq-nyk0n5c9brbh2l4a-ue5ff96fa)=

![AlohaMini2 Pro Quick Start Guide (Minimalist) · Figure 9](../_static/yuque-assets/4c673c20aed96ebda739.png)

(yq-nyk0n5c9brbh2l4a-ub8d994fa)=

At this point, the port of the teleoperation arm is successfully bound to the PC.

(yq-nyk0n5c9brbh2l4a-kNQ28)=

### 3. Check whether the status of the two teleoperation arms is normal.

```text
# 进入conda环境
conda activate lerobot_alohamini
cd lerobot_alohamini

#执行获取舵机状态命令
python examples/debug/motors.py get_motors_states \
  --port /dev/am_arm_leader_left

  python examples/debug/motors.py get_motors_states \
  --port /dev/am_arm_leader_right
```

(yq-nyk0n5c9brbh2l4a-u2903067a)=

Expected output, and operating the leader arm, you can see changes in POS values

(yq-nyk0n5c9brbh2l4a-u9ecf752f)=

(yq-nyk0n5c9brbh2l4a-ueb2e6800)=

![AlohaMini2 Pro Quick Start Guide (Minimalist) · Figure 10](../_static/yuque-assets/e60f3bf117f818405f76.png)

(yq-nyk0n5c9brbh2l4a-P0qe5)=

### 4. Turn on teleoperation

(yq-nyk0n5c9brbh2l4a-u0fd52c12)=

a) When using the teleoperation arm for the first time, the robot arm needs to be calibrated.

(yq-nyk0n5c9brbh2l4a-u4722bed1)=

Remote arm calibration command:

```bash
python examples/alohamini/calibrate_bi.py \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof
```

(yq-nyk0n5c9brbh2l4a-ucf38e747)=

Complete the calibration process **by yourself according to the prompts (reference video:** [**https://b23.tv/Dd1xFYz**](https://b23.tv/Dd1xFYz)**)**.

(yq-nyk0n5c9brbh2l4a-u2b763b9d)=

(yq-nyk0n5c9brbh2l4a-u17394f10)=

b) After the calibration is completed, perform teleoperation

```bash
python examples/alohamini/teleoperate_bi.py \
  --robot.remote_ip 192.168.x.xx \
  --robot.robot_model alohamini2pro \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof
```

(yq-nyk0n5c9brbh2l4a-uf949f4d7)=

After automatically connecting to the remote robot, the terminal will continue to output real-time status information. Users can control the movement of the robot's chassis and lifting mechanism through the keyboard, and can also remotely operate the robotic arm through the teleoperation arm.

(yq-nyk0n5c9brbh2l4a-u5268bf0d)=

(yq-nyk0n5c9brbh2l4a-u69751080)=

![AlohaMini2 Pro Quick Start Guide (Minimalist) · Figure 11](../_static/yuque-assets/f16fbfb221ccad8ec296.png)

| Button | Function |
| --- | --- |
| `W` / `S` | Forward/Back |
| `A` / `D` | Turn left / turn right |
| `Z` / `X` | Pan left / pan right |

| Button | Function |
| --- | --- |
| `U` / `J` | rise/fall |

(yq-nyk0n5c9brbh2l4a-TKBmk)=

## 3. Configure the camera

(yq-nyk0n5c9brbh2l4a-udc745801)=

Modify configuration file:

```text
src/lerobot/robots/alohamini/config_alohamini.py
```

| The machine where it is located | function |
| --- | --- |
| Raspberry Pi (slave computer) | Control actual camera acquisition |
| PC (host computer) | Control which camera data the client subscribes to |

(yq-nyk0n5c9brbh2l4a-u80bff6b1)=

> (yq-nyk0n5c9brbh2l4a-u8119888d)=
> 
> 
> 
> ⚠️ Both ends of **must be consistent.** If a camera is enabled on the Raspberry Pi but not on the PC, or vice versa, it may cause connection abnormalities or data mismatch. After each modification, please update the files on both machines synchronously and restart the processes on both ends.

(yq-nyk0n5c9brbh2l4a-YcSjd)=

### Camera configuration instructions

(yq-nyk0n5c9brbh2l4a-u2a364288)=

In the configuration file, all cameras are managed uniformly through the `alohamini_cameras_config()` function.
If you need to disable a camera, just comment out the corresponding configuration.

```python
def alohamini_cameras_config() -> dict[str, CameraConfig]:
    return {
        "head_top": OpenCVCameraConfig(
            index_or_path="/dev/am_camera_head_top", fps=30, width=640, height=480, rotation=Cv2Rotation.NO_ROTATION
        ),
        # "head_back": OpenCVCameraConfig(
        #     index_or_path="/dev/am_camera_head_back", fps=30, width=640, height=480, rotation=Cv2Rotation.NO_ROTATION
        # ),
        # "head_front": OpenCVCameraConfig(
        #     index_or_path="/dev/am_camera_head_front", fps=30, width=640, height=480, rotation=Cv2Rotation.NO_ROTATION
        # ),
        # "wrist_left": OpenCVCameraConfig(
        #     index_or_path="/dev/am_camera_wrist_left", fps=30, width=640, height=480, rotation=Cv2Rotation.NO_ROTATION
        # ),
        # "wrist_right": OpenCVCameraConfig(
        #     index_or_path="/dev/am_camera_wrist_right", fps=30, width=640, height=480, rotation=Cv2Rotation.NO_ROTATION
        # ),
    }
```

(yq-nyk0n5c9brbh2l4a-u89e01820)=

---

(yq-nyk0n5c9brbh2l4a-FfSF4)=

## 4. Recording data set

(yq-nyk0n5c9brbh2l4a-fe6f4a4d)=

### Recording data set

(yq-nyk0n5c9brbh2l4a-uc73f874a)=

Enter the following command in the terminal to record a new data set (note to change the appropriate parameters):

```text
python examples/alohamini/record_bi.py \
  --dataset.repo_id user/am2_bi_test \
  --dataset.root "$HOME/user/am2_bi_test" \
  --dataset.num_episodes 1 \
  --dataset.fps 25 \
  --dataset.episode_time_s 60 \
  --dataset.reset_time_s 10 \
  --dataset.single_task "pickup1" \
  --robot.remote_ip 192.168.8.117 \
  --robot.robot_model alohamini2pro \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof \
  --dataset.push_to_hub=false \
  --display-data=true
```

(yq-nyk0n5c9brbh2l4a-uf9037d3a)=

Parameters:

(yq-nyk0n5c9brbh2l4a-u570f769f)=

--dataset.repo_id Data set logical name in the form of xxx/xxx

(yq-nyk0n5c9brbh2l4a-ua8f750dc)=

--dataset.root The actual location where the dataset is saved

(yq-nyk0n5c9brbh2l4a-ud677db3a)=

--dataset.num_episodes The number of data episodes recorded this time

(yq-nyk0n5c9brbh2l4a-u492e4e5d)=

--dataset.fps The frame rate of the dataset recorded this time (25 is recommended)

(yq-nyk0n5c9brbh2l4a-u47832297)=

--dataset.reset_time_s Rest time between each data round, used to restore state

(yq-nyk0n5c9brbh2l4a-u86daddd4)=

--display-data=true whether to display the returned screen

(yq-nyk0n5c9brbh2l4a-ucd8a13dc)=

(yq-nyk0n5c9brbh2l4a-u99443077)=

Default directory:

```text
~/.cache/huggingface/lerobot/
```

(yq-nyk0n5c9brbh2l4a-ub2fec7f1)=

Specify another save directory:

```bash
--dataset.root ~/user/am2_bi_test
```

(yq-nyk0n5c9brbh2l4a-uf8432008)=

`--dataset.root` only changes the local save location, not `dataset.repo_id`. The target directory should not exist when creating a new dataset.

(yq-nyk0n5c9brbh2l4a-d9edd818)=

### Resume data set

(yq-nyk0n5c9brbh2l4a-uce6d7f96)=

Add `--resume` to the original command and keep the same `repo_id` and `root`:

```text
python examples/alohamini/record_bi.py \
  --dataset.repo_id user/am2_bi_test \
  --dataset.root "$HOME/user/am2_bi_test" \
  --dataset.num_episodes 1 \
  --dataset.fps 25 \
  --dataset.episode_time_s 60 \
  --dataset.reset_time_s 10 \
  --dataset.single_task "pickup1" \
  --robot.remote_ip 192.168.8.117 \
  --robot.robot_model alohamini2pro \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof \
  --dataset.push_to_hub=false \
  --display-data=true \
  --resume
```

(yq-nyk0n5c9brbh2l4a-ud968786c)=

(yq-nyk0n5c9brbh2l4a-ub88bece8)=

Once you create a new data set, you need to add the --resume parameter when recording again, otherwise an error will be reported: The file already exists.

(yq-nyk0n5c9brbh2l4a-u1fb776e6)=

(yq-nyk0n5c9brbh2l4a-8a7a4375)=

## 5. Playback Data Set

(yq-nyk0n5c9brbh2l4a-u3d3bfd4e)=

There are two kinds of "playback" here:

1. View images, status, and actions in Rerun without controlling the robot.

1. `replay` to the real machine and let the robot perform the actions recorded in the data set.

(yq-nyk0n5c9brbh2l4a-f3d4e81c)=

### 1. Rerun visualization data set

```text
HF_HUB_OFFLINE=1 \
lerobot-dataset-viz \
  --repo-id user/am2_bi_test \
  --root "$HOME/user/am2_bi_test" \
  --episode-index 0 \
  --display-compressed-images
```

(yq-nyk0n5c9brbh2l4a-d9c69f54)=

### 2. `replay` to real machine

```text
HF_HUB_OFFLINE=1 \
python examples/alohamini/replay_bi.py \
  --dataset.repo_id user/am2_bi_test \
  --dataset.root "$HOME/user/am2_bi_test" \
  --dataset.episode 0 \
  --robot.remote_ip 192.168.8.117 \
  --robot.robot_model alohamini2pro
```

(yq-nyk0n5c9brbh2l4a-JbJBa)=

## 

(yq-nyk0n5c9brbh2l4a-22416fd2)=

## 6. Training data set

(yq-nyk0n5c9brbh2l4a-669b954f)=

### Example method 1. Locally train a common ACT model (easy to train, but has poor mobile support)

(yq-nyk0n5c9brbh2l4a-u9ac2eb81)=

Just execute the command directly from the terminal:

```text
HF_HUB_OFFLINE=1 \
HF_DATASETS_OFFLINE=1 \
TORCH_HOME="$HOME/.cache/torch" \
lerobot-train \
  --dataset.repo_id=user/am2_bi_test \
  --dataset.root="$HOME/user/am2_bi_test" \
  --dataset.video_backend=pyav \
  --policy.type=act \
  --policy.device=cuda \
  --policy.push_to_hub=false \
  --save_checkpoint_to_hub=false \
  --output_dir=outputs/train/act_am2_bi_test \
  --job_name=act_am2_bi_test \
  --steps=100000 \
  --batch_size=6 \
  --wandb.enable=false
```

(yq-nyk0n5c9brbh2l4a-a8c4493e)=

### Example method 2. Local training of AM-ACT model (suitable for mobile tasks)

(yq-nyk0n5c9brbh2l4a-udd2f4453)=

Step 1: Generate pure visual data set on PC

```text
python -m lerobot.scripts.create_alohamini_visual_only_dataset \
  --source "$HOME/user/am2_bi_test" \
  --target "$HOME/user/am2_bi_test_visual_only" \
  --keep-camera forward \
  --keep-camera wrist_right \
  --drop-state
```

(yq-nyk0n5c9brbh2l4a-ufb029b76)=

Step 2: Run the training command

```text
HF_HUB_OFFLINE=1 \
HF_DATASETS_OFFLINE=1 \
TORCH_HOME="$HOME/.cache/torch" \
lerobot-train \
  --dataset.repo_id=user/am2_bi_test_visual_only \
  --dataset.root="$HOME/user/am2_bi_test_visual_only" \
  --dataset.video_backend=pyav \
  --policy.type=am_act \
  --policy.device=cuda \
  --policy.fixed_action_dims='[0,1,2,3,4,5,6]' \
  --policy.discrete_action_dims='[14,15,16]' \
  --policy.discrete_action_values='[[-0.15,0,0.15],[-0.15,0,0.15],[-45,0,45]]' \
  --policy.discrete_action_class_weights='[[3,1,1.5],[3,1,2],[2,1,2]]' \
  --policy.discrete_action_loss_weight=1.0 \
  --policy.push_to_hub=false \
  --save_checkpoint_to_hub=false \
  --output_dir=outputs/train/am2_bi_test_visual_only \
  --job_name=am_act_am2_bi_test \
  --steps=100000 \
  --batch_size=6 \
  --wandb.enable=false
```

(yq-nyk0n5c9brbh2l4a-u85e0aaa6)=

Note that the above default policy parameters are only applicable to 1. The right arm is clamped, and the left arm is always stationary. 2. The chassis needs to have forward and backward, rotation, and translation operations in the data set. If there is no translation action in the data set, an error will be reported during training (ValueError: Action dimension 15 has zero std and cannot be classified.).

(yq-nyk0n5c9brbh2l4a-zyiLE)=

### 

(yq-nyk0n5c9brbh2l4a-uf6d2f191)=

(yq-nyk0n5c9brbh2l4a-x8hf8)=

## 7. Local inference

(yq-nyk0n5c9brbh2l4a-u43b7168a)=

Before inference, start the Raspberry Pi Host and clear the area around the robot.

```text
# 在PC的终端中运行命令
conda activate lerobot_alohamini
cd lerobot_alohamini

python examples/alohamini/evaluate_bi.py \
  --eval.n_episodes 1 \
  --fps 25 \
  --dataset.single_task "pick up the block and place it in the box" \
  --policy.path outputs/train/act_pick_test_01/checkpoints/020000/pretrained_model \
  --dataset.repo_id local/eval_act_pick_test_01 \
  --dataset.push_to_hub=false \
  --robot.remote_ip 192.168.8.117 \
  --robot.id my_alohamini \
  --robot.robot_model alohamini2pro \
  --inference.type sync \
  --interpolation_multiplier 3
```

(yq-nyk0n5c9brbh2l4a-u31567234)=

Key parameters:

- `--inference.type sync`: Each policy control step calls `select_action()` synchronously; policies such as ACT use this mode.

- `--fps 25`: policy action frequency. It is recommended to use 15~20 Hz for the first test, and then increase it after confirming that it is stable.

- `--interpolation_multiplier 1`: Turn off motion interpolation. When set to 3, an intermediate action is generated between every two policy actions.

(yq-nyk0n5c9brbh2l4a-ucd7d6269)=

The robot command frequency becomes `fps × 3`, but does not increase the model inference frequency.

- `--dataset.repo_id`: The name of this evaluation data set; `evaluate_bi.py` will record the observations and actual sent actions.

- `--dataset.push_to_hub=false`: Only saved on this machine, not uploaded to Hugging Face Hub.

- `--robot.robot_model`: must be completely consistent with the Raspberry Pi Host model, otherwise the status and action dimensions may be misaligned.

(yq-nyk0n5c9brbh2l4a-udb89a1d5)=

First time inference suggestions:

- `--eval.n_episodes 1`

- `--eval.episode_time_s 15`

- `--inference.type sync`

- `--interpolation_multiplier 1`

- Put your hand near the power switch

- Stop immediately when abnormal movement direction, amplitude or speed is found
