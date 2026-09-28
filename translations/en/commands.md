# Command reference

Applicable models: **AlohaMini 2 / 2 Pro**. Please select one of the two examples with model numbers to execute. Complete entry process: [2 Tutorials](alohamini2.md) · [2 Pro Tutorial](alohamini2pro.md).

This page is for quick reference after you have completed the tutorial. For complete steps, parameter explanations and expected results, please enter the corresponding chapters. Unless otherwise noted, commands are executed in the `lerobot_alohamini` root directory and after activating the environment.

## placeholder convention

| Writing method | What to replace with |
| --- | --- |
| `<Pi_IP>` | Actual LAN IP on the robot side |
| `/dev/ttyACM0` | The real serial port corresponding to the current hardware |
| `$HF_USER` | The Hugging Face username that has been set on the current terminal |
| `/absolute/path/...` | The absolute path that actually exists on this machine or is to be created |
| `020000` | Actual number of checkpoint steps saved |

Do not execute placeholders with angle brackets as-is. In order to reduce parameter omissions, it is recommended to fill in the model, leader arm profile and equipment identification explicitly.

## Environment and Discovery Devices

```bash
conda activate lerobot_alohamini
lerobot-find-port
lerobot-find-cameras
ls -l /dev/am_arm_*
```

For details, see [Installation](software.md) and [Device configuration](configuration.md).

## Calibration entry

Pi：

**AlohaMini 2**

```bash
python -m lerobot.robots.alohamini.alohamini_calibrate --robot_model alohamini2
```

**AlohaMini 2 Pro**

```bash
python -m lerobot.robots.alohamini.alohamini_calibrate --robot_model alohamini2pro
```

PC：

```bash
python examples/alohamini/calibrate_bi.py \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof
```

See [Calibration](calibration.md) for details.

## Host and teleoperation

Pi：

**AlohaMini 2**

```bash
python -m lerobot.robots.alohamini.alohamini_host --robot_model alohamini2
```

**AlohaMini 2 Pro**

```bash
python -m lerobot.robots.alohamini.alohamini_host --robot_model alohamini2pro
```

PC：

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

For details, see [Teleoperation](teleoperation.md).

## Data and policy portal

| Task | entrance | Complete tutorial |
| --- | --- | --- |
| Standard double-arm recording | `python examples/alohamini/record_bi.py` | [Data collection](learning.md) |
| Multi-frequency dual-arm recording | `python examples/alohamini/record_bi_multirate.py` | [Data collection](learning.md) |
| Real machine playback | `python examples/alohamini/replay_bi.py` | [Data inspection and playback](learning.md) |
| View offline | `lerobot-dataset-viz` | [Data check](learning.md) |
| ACT training | `lerobot-train` | [training](training.md) |
| Whole machine evaluation | `python examples/alohamini/evaluate_bi.py` | [Assessment](evaluation.md) |

The table is the program entry, and you still need to pass in the complete parameters in the corresponding tutorial. You can run `--help` first to view the parameters accepted by the currently installed version.

## Quick check of model parameters

| Model | `robot_model` | leader arm profile | Common leader arm ID |
| --- | --- | --- | --- |
| generation | `alohamini1` | `so-arm-5dof` | `so101_leader_bi` |
| second generation | `alohamini2` | `am-leader-6dof` | `am_leader_bi` |
| Pro | `alohamini2pro` | `am-leader-6dof` | `am_leader_bi` |

The Host uses `--robot_model` and the PC uses `--robot.robot_model`; the leader arm ID must be consistent with the value used during actual calibration.

## Servo debugging tool

### View status

```bash
python examples/debug/motors.py get_motors_states --port /dev/ttyACM0
```

### Modify a single ID

Only connect one servo to be configured at a time:

```bash
python examples/debug/motors.py configure_motor_id \
  --id 1 --set_id 8 --port /dev/ttyACM0
```

### Other advanced operations

The following subcommands will modify the status or cause motion. Please check the hardware and parameters before use. Meaning is provided here to avoid treating device-independent target locations as generic debugging values.

| subcommand | function | Parameter attention |
| --- | --- | --- |
| `move_motor_to_position` | Move the specified servo to the target position | `--position` is the original tick, not the angle or millimeters |
| `configure_motor_phase` | Modify phase | `--id` Specified object; should not be modified in batches at will |
| `reset_motors_to_midpoint` | Set the current position as the median related configuration | First confirm the actual attitude and subsequent calibration impact |
| `reset_motors_torque` | off torque | A mechanism that needs to support a possible fall after losing its holding power |
| `move_motors_by_script` | Execute action script | Check all actions in the script against applicable hardware |

Read specific parameters:

```bash
python examples/debug/motors.py --help
```

The independent `wheels.py` and `axis.py` have their own servos and geometric constants. They cannot be considered to be adapted to the second generation or Pro just by passing them through the serial port. For details, see [Debugging and troubleshooting](troubleshooting.md).
