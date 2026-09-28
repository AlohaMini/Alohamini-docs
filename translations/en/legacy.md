# AlohaMini 1

[First generation hardware tutorial](legacy-hardware.md) provides a bill of materials, assembly steps and assembly photos.

The first generation uses SO-ARM100 / SO-ARM101 double arms, with wheeled chassis and electric lifting mechanism. The hardware, software and simulation entrances of the first generation are reserved here.

```{image} _static/media/alohamini_git.png
:alt: AlohaMini first-generation robot actual machine
:width: 100%
```

## Hardware information

- [Introduction to the Generation Project](https://github.com/liyiteng/AlohaMini/tree/main/AlohaMini1)
- [Generation BOM](https://github.com/liyiteng/AlohaMini/blob/main/AlohaMini1/docs/BOM.md)
- [Generation Assembly Guide](https://github.com/liyiteng/AlohaMini/blob/main/AlohaMini1/docs/hardware_assembly.md)
- [Structural design documents](https://github.com/liyiteng/AlohaMini/tree/main/AlohaMini1/hardware)

## Software and Simulation

The current unified software entrance is [lerobot_alohamini](https://github.com/liyiteng/lerobot_alohamini). Please select the hardware configuration corresponding to the generation.

For simulation resources, please view the [Simulation Guide](simulation.md).

## The difference from the second generation

The second generation replaced the mechanical arm and strengthened the chassis and lifting mechanism. Check the [Models and specifications](specifications.md) and confirm the design differences before deciding whether to upgrade.


## First generation software parameters

| parameters | generation value |
| --- | --- |
| Machine model | `alohamini1` |
| leader arm profile | `so-arm-5dof` |
| Commonly used leader arm calibration IDs | `so101_leader_bi` |
| Data interface | 16 dimensions |
| Wheelset and elevator servo | STS3215 |
| Lifting transmission parameters | 84 mm/rev |

Boot on the Pi:

```bash
python -m lerobot.robots.alohamini.alohamini_host --robot_model alohamini1
```

Start on PC:

```bash
python examples/alohamini/teleoperate_bi.py \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini1 \
  --teleop.id so101_leader_bi \
  --teleop.arm_profile so-arm-5dof \
  --fps 50 \
  --camera-fps 30
```

## What to replace when using the unified tutorial

For installation, device discovery and data workflow, please refer to the unified tutorial on this site. Steps involving hardware use a generation structure and parameters:

1. The calibration command is changed to the first generation model and SO leader arm profile.
2. Teleoperation, recording, playback and evaluation remain `alohamini1`.
3. The dataset uses an independent name to record its 16-dimensional state/action definition.
4. The model uses checkpoints that match one generation of data.
5. The camera name is based on the current actual configuration and existing data.

Keep records of calibrations, datasets, models and camera configurations before migrating from older versions. Old data may also involve angle/normalized representation differences. You should check the `use_degrees` compatibility option in the configuration and the original data semantics. Do not judge compatibility based only on the array length.

## Keep and upgrade

The first generation can still be used for teleoperation, data acquisition and model experiments. The second generation upgrade involves the robotic arm, lifting and chassis structure, as well as the profile and data interface in the software; this is a set of hardware and configuration changes that require re-examination of assembly, calibration and training data.
