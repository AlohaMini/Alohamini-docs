# AlohaMini 2 Pro: Getting started

For an assembled robot, complete [Unboxing and first power-on](unboxing.md) before continuing. Experienced LeRobot users can also use the [Pro quickstart](yuque/pro-quickstart.md) for port-binding screenshots and recording/training examples.

This guide covers **AlohaMini 2 Pro with two AM-ARM200 leader arms, a Linux PC and a Raspberry Pi 5**. Complete device setup, calibration, teleoperation and your first recording in order.

**Current model: `alohamini2pro`** · Switch to [AlohaMini 2 Tutorial](alohamini2.md) · [Return to model selection](quickstart.md)

Run all commands from the **root of the `lerobot_alohamini` software repository**, with the project Python environment activated. Replace `<Pi_IP>` with the Raspberry Pi’s actual IP address.

## Choose your starting point

| Current status | where to start |
| --- | --- |
| Verify Pro hardware or prepare to build | First read the [2 Pro hardware](hardware-pro.md) to confirm the actual package and data range |
| Already assembled robot | This page "Installation and device configuration" |
| Already capable of teleoperation and ready for training | [Data collection](learning.md) → [training](training.md) → [Assessment](evaluation.md) |
| There is only one set of leader and follower arms | [AM-ARM200 single arm tutorial](single-arm.md) |
| Already a generation of robots | [generation description](legacy.md), then use the corresponding model parameters |
| First check the model and joints | [Simulation and visualization](simulation.md) |

## What do you need to prepare

First, check the follower arm and chassis according to [2 Pro hardware](hardware-pro.md). Standard 2 printouts, material quantities, and assembly photos cannot be used directly as assembly lists for Pro.

### Robot side

- Correctly assembled chassis, lifting mechanism and double follower arms.
- Raspberry Pi 5, memory card, power supply and cooling.
- follower arm bus control board and data lines.
- Installed camera and its cables.

### Operator PC

- A Linux PC that can run the project software.
- Two assembled leader arms, control board, data cables and matching power supply.
- A LAN that allows PC and Raspberry Pi to communicate with each other.
- Storage space used to save data sets; training also requires computing resources that match the policy.

The operator moves the leader arms by hand; the follower arms on the robot execute those movements. **Host runs on the robot, and Client runs on the PC.** Each command below identifies where to run it.

## Step 1: Confirm your model

| Check items | AlohaMini 2 Pro Configuration |
| --- | --- |
| Pi machine parameters `--robot_model` | `alohamini2pro` |
| PC parameters `--robot.robot_model` | `alohamini2pro` |
| follower arm profile (selected by model) | `am-follower-6dof-hd` |
| PC leader arm `--teleop.arm_profile` | `am-leader-6dof` |
| leader arm Device ID Example | `am_leader_bi` |
| Chassis wheel servo | STS3250 × 3 |
| Elevator servo/transmission parameters | STS3095 / 131 mm/rev |
| Overall machine state/action dimension | 18 |

Select the same robot model on both machines. Leader and follower profiles serve different roles. Use the same leader ID for calibration, teleoperation and recording. `am_leader_bi` is an example; assign a distinct ID and calibration files to each leader-arm set.

For complete differences, see [Models and specifications](specifications.md). 131 mm/rev is the software transmission parameter, not the lifting speed or total stroke.

## Step 2: Installation and device configuration

Press [Software installation](software.md) to complete the environment. Then press [Device configuration](configuration.md) to establish port mapping and check the camera.

After completion you should be able to confirm:

| Check object | result |
| --- | --- |
| PC leader arm | The left and right leader arm device names point to the correct control panel respectively. |
| Pi follower arm | The left and right follower arm buses are separately accessible |
| camera | Each enabled name corresponds to the correct screen; two channels are enabled by default |
| network | The PC has access to the actual IP of the Pi |
| Software | Both versions are compatible and the project environment has been activated |

Use the discovery tools to identify each serial port and camera on first connection; do not guess their indexes.

## Step 3: Calibrate the arms

**Pi: Robot side calibration**

```bash
python -m lerobot.robots.alohamini.alohamini_calibrate --robot_model alohamini2pro
```

**PC: Dual leader arm calibration**

```bash
python examples/alohamini/calibrate_bi.py \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof
```

Follow the interactive prompts to complete the range recording of the left and right arms. See the [Calibration Tutorial](calibration.md) for complete instructions. After the calibration is completed, power off the master and follower arms and restart them according to the original process.

## Step 4: First teleoperation

**Pi: Start Host and keep** running

```bash
python -m lerobot.robots.alohamini.alohamini_host --robot_model alohamini2pro
```

**PC: Start control program**

```bash
python examples/alohamini/teleoperate_bi.py \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2pro \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof \
  --fps 50 \
  --camera-fps 30
```

Replace `<Pi_IP>`. First move the leader arm unilaterally and in a small range, then check the grippers, and finally check the chassis and lifting. Machine buttons: W/S forward and backward, Z/X horizontal shift, A/D rotation, U/J lift. For more parameters and control rights description, see [Teleoperation](teleoperation.md).

## Step 5: Record the first piece of data

Exit the teleoperation program on the PC and leave the Pi Host running. Record a short test first:

```bash
export HF_USER="your-hf-username"
python examples/alohamini/record_bi.py \
  --dataset.repo_id $HF_USER/am2pro_first_episode \
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

This is a collection link test. First replace `HF_USER` with your own namespace, and change the task description to this actual action; the example turns off automatic uploading.

View the first piece of data after recording:

```bash
lerobot-dataset-viz \
  --repo-id $HF_USER/am2pro_first_episode \
  --episode-index 0 \
  --display-compressed-images
```

Confirm that the camera angle is correct, the movements are complete, and there is no long-term screen freeze before entering [Formal collection](learning.md).

## How to tell if getting started is complete

- Be able to describe your robot model, leader arm profile, and left and right ports.
- The left and right follower arms correspond to the leader arm, and the direction and gripper movement are normal.
- The chassis and lift responded as expected, with no cable interference.
- Each enabled camera perspective is correct.
- A piece of data has been saved, the local location is known, and review has been completed.

For the formal experiment, enter [Data collection](learning.md) first, and use the official recording example of **AlohaMini 2 Pro** on the page; the entry short test is only used to check the link and cannot be used to judge the effect of the policy. It is recommended that the data set name be prefixed with `am2pro` to make it easier to distinguish it from other models.

Then press [training](training.md) → [Assessment](evaluation.md) to complete the policy closed loop. When a certain step fails, check [Debugging and troubleshooting](troubleshooting.md) first, and do not enter the training phase with device mapping or calibration errors.


## Tutorial basis
