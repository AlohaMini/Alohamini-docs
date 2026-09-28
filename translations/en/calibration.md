# Arm calibration

Calibration establishes the correspondence between the raw servo readings and the range of motion of the robotic arm. The left and right leader arms and the robot-side follower arms are calibrated separately, and then the same set of device identifiers and profiles are used for teleoperation and recording.

## Confirm before calibration

1. The [Device configuration](configuration.md) has been completed and the left and right ports can be identified.
2. The servo, robotic arm and power supply model correspond to each other, and the installation structure has no jamming.
3. Exit the Host, teleoperation and debugging programs that occupy the same serial port.
4. There is space in the robot arm's activity area, and the joints can be manually swung according to the terminal prompts.

## 1. Calibrate the robot side on Pi

Select a command to execute based on the model.

### AlohaMini 2

```bash
python -m lerobot.robots.alohamini.alohamini_calibrate --robot_model alohamini2
```

### AlohaMini 2 Pro

```bash
python -m lerobot.robots.alohamini.alohamini_calibrate --robot_model alohamini2pro
```

### AlohaMini 1

```bash
python -m lerobot.robots.alohamini.alohamini_calibrate --robot_model alohamini1
```

The portal exits after completing calibration. The Host will also check the calibration when it starts. If it is missing, it will prompt the corresponding prompt. However, it is recommended to complete this step separately for the first time to confirm each robot arm.

### How to follow interactive prompts

The sequence described in the original workflow is: move to the middle position, confirm, and then complete the range recording in the left and right directions. The specific joints, angles, and confirmation timing that need to be moved are subject to the calibration prompts and mechanical structure of the selected robotic arm. Do not directly apply the attitude diagram of the SO robot arm to the AM-ARM200.

During calibration, the movement should cover the range required by the prompt, and avoid forcibly crossing the mechanical limit. When encountering a joint that cannot move, check the assembly and wiring first, and do not skip it by writing an error range.

## 2. Calibrate the dual leader arms on PC

leader arm calibration can be done independently, **does not require a Pi Host to be running**. The default left and right leader arm paths are `/dev/am_arm_leader_left` and `/dev/am_arm_leader_right`.

### AM Main Boom: Second Generation and Pro

```bash
python examples/alohamini/calibrate_bi.py \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof
```

### SO Main Boom: First Generation

```bash
python examples/alohamini/calibrate_bi.py \
  --teleop.id so101_leader_bi \
  --teleop.arm_profile so-arm-5dof
```

The script processes both leader arms in sequence. `teleop.id` is the device identifier used for calibration configuration, not the servo ID. The corresponding calibration data can only be read after maintaining the same value for subsequent remote operations and recording.

## 3. Reuse or recalibrate

If it is found that calibration has already been performed, follow the terminal prompts to select reuse or recalibrate. In the original process, Enter can be reused, and `c` enters recalibration; the actual prompts of the current running version shall prevail.

| situation | Recommended treatment |
| --- | --- |
| The same robotic arm, ports and structure remain unchanged | Check the logo and reuse the existing calibration. |
| Change leader arm model or profile | Use matching profile, recheck and calibrate |
| Posture changes after disassembly and assembly of joints and replacement of servos | Recheck installation and calibration |
| Calibration required on every startup | Check whether `teleop.id`, left and right ports, profile and running user have changed |
| Abnormal direction or range of leader and follower arms | Stop teleoperation and review the model, left and right mapping and calibration process |

## 4. Inspection after completion

According to the original workflow, after the calibration is completed, power off the leader arm and the follower arm and restart them. Then start the Host, and then use [Teleoperation](teleoperation.md) to check the correspondence between the left and right arms, the direction of movement, the gripper and the joint range in a small range.

Successful calibration does not mean that all agencies have verified it. The chassis, lift, and camera should still be confirmed according to their respective inspection procedures; strategic evaluation should be carried out after manual teleoperation is normal.
