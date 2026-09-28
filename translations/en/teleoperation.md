# Teleoperation

Applicable models: **AlohaMini 2 / 2 Pro**. Please select one of the two examples with model numbers to execute. Complete entry process: [2 Tutorials](alohamini2.md) · [2 Pro Tutorial](alohamini2pro.md).

This chapter completes the entire process of PC leader arm driving the robot follower arm and keyboard controlling the chassis and lifting. The premise is that [Installation](software.md), [Configuration](configuration.md) and [Calibration](calibration.md) have been completed.

## 1. Start Host on Pi

Start according to actual model:

**AlohaMini 2**

```bash
python -m lerobot.robots.alohamini.alohamini_host --robot_model alohamini2
```

**AlohaMini 2 Pro**

```bash
python -m lerobot.robots.alohamini.alohamini_host --robot_model alohamini2pro
```

The first generation uses `alohamini1`. For details, please refer to the [generation description](legacy.md). Keep the terminal running and check the startup log for port, calibration, and camera information; resolve any device errors before launching the client.

## 2. Start dual-arm teleoperation on PC

Start according to the actual model and AM leader arm configuration:

**AlohaMini 2**

```bash
python examples/alohamini/teleoperate_bi.py \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2 \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof \
  --fps 50 \
  --camera-fps 30
```

**AlohaMini 2 Pro**

```bash
python examples/alohamini/teleoperate_bi.py \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2pro \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof \
  --fps 50 \
  --camera-fps 30
```

| parameters | meaning |
| --- | --- |
| `robot.remote_ip` | Pi's actual LAN IP |
| `robot.robot_model` | The same machine model as Host |
| `teleop.id` | The same equipment identification as when calibrating the leader arm |
| `teleop.arm_profile` | leader arm hardware profile |
| `fps` | Control command and status loop target frequency |
| `camera-fps` | Camera observation request frequency should not be greater than the control frequency |

The two AM leader arm profiles are the same; the model of the entire machine must be consistent with the Pi Host. One generation uses `alohamini1`, `so101_leader_bi` and `so-arm-5dof`.

## 3. Check the robotic arm first

Slowly move the leader arm on one side and check whether the corresponding follower arm is following; then check the other side. Verify the joints and jaws separately, do not initially move the arms, chassis, and lift at the same time.

If the left and right are opposite, the joint direction is abnormal or there is obvious jump, exit the teleoperation first and check the left and right serial ports, model and calibration marks. Do not continue to collect data with mismatched configurations.

## 4. Keyboard control

The current default buttons of the whole machine client are as follows:

| Button | action |
| --- | --- |
| `W` / `S` | Chassis forward/reverse |
| `Z` / `X` | Chassis moves sideways left/right |
| `A` / `D` | Chassis rotates left/right |
| `T` / `G` | Increase/decrease movement speed level |
| `U` / `J` | Lift up/down |
| `Ctrl+C` | Interrupt the teleoperation program in the running terminal |

Although the current configuration table retains the `Q` exit mapping, the checked teleoperation main loop does not handle this exit branch, so this tutorial uses the terminal `Ctrl+C` to end the program.

Ensure that the control program can receive keyboard input. The first check only triggers a single direction briefly to observe the movement and response after release; you can use the terminal interrupt to end the program.

## 5. Low load troubleshooting

If the picture or motion is unstable, you can first reduce the frequency of control and camera requests to isolate CPU, USB, network or configuration issues:

**AlohaMini 2**

```bash
python examples/alohamini/teleoperate_bi.py \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2 \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof \
  --fps 10 \
  --camera-fps 10
```

**AlohaMini 2 Pro**

```bash
python examples/alohamini/teleoperate_bi.py \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2pro \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof \
  --fps 10 \
  --camera-fps 10
```

This setting is used to locate problems and does not mean that low-frequency data training should be used for a long time. After identifying the cause, restore the configuration required for the task and keep it consistent before official collection.

## 6. Only debug the chassis and lifting

The project provides access to jump over the robotic arm. Pi:

**AlohaMini 2**

```bash
python -m lerobot.robots.alohamini.alohamini_host \
  --robot_model alohamini2 \
  --no_follower
```

**AlohaMini 2 Pro**

```bash
python -m lerobot.robots.alohamini.alohamini_host \
  --robot_model alohamini2pro \
  --no_follower
```

PC：

**AlohaMini 2**

```bash
python examples/alohamini/teleoperate_bi.py \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2 \
  --no_leader
```

**AlohaMini 2 Pro**

```bash
python examples/alohamini/teleoperate_bi.py \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2pro \
  --no_leader
```

`--no_follower` and `--no_leader` control both ends respectively. It is still necessary to confirm that the chassis, lift bus and camera are configured correctly before use.

## 7. Control and opt-out

Host only accepts one control client at a time. Before starting recording or evaluation, stop the current teleoperation client to prevent another process from continuing to occupy control.

The current Host will stop moving and release control if it does not receive a command for more than 1 second. Network disconnection, expired feedback, or current protection may cause operation to be suspended; the cause should be confirmed and explicitly resumed. For detailed behavior, see [Runtime and safety](runtime.md).

## Enter data collection

Enter [Data collection](learning.md) after the following conditions are met: the left and right robotic arms correspond correctly, the chassis and lifting are normal, the enabled camera screen is correct, the network is stable, and the planned collection tasks can be repeated.
