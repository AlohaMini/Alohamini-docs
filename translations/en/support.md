# Robot troubleshooting

Suitable for: **AlohaMini 2 / 2 Pro**. Troubleshoot E001-E004 and common faults one by one.

## First determine where the fault occurs

| phenomenon | location to check first | Continue reading |
| --- | --- | --- |
| Raspberry Pi does not light up and restarts during operation | Robot power supply, power board and battery | [Unboxing power supply diagram](unboxing.md) |
| PC cannot find leader arm | PC USB, driver board power supply, serial port alias | [Device configuration](configuration.md) |
| Host is missing servos 8–11 | Robot left bus, left and right follower arm ports | This page E002 |
| The upper and lower limits of the calibration prompt are the same | Calibration file corresponding to the current device | This page E001 |
| Timeout or exit after starting camera | Pi Power, USB, Camera Path and Enable Configuration | This page E003 |
| The direction or amplitude of the movement of the follower arm is wrong | profile, calibration, robot models at both ends | [Calibration](calibration.md) , [Teleoperation](teleoperation.md) |

## E001: Calibration minimum and maximum values are the same

**Common reasons**: After triggering recalibration, the saved range is confirmed without actually moving the joint.

1. Stop teleoperation and confirm that the current terminal connected is indeed the target robotic arm.
2. Check leader arm `am-leader-6dof`; standard 2 follower arm `am-follower-6dof`; Pro follower arm `am-follower-6dof-hd`.
3. Follow [Calibration steps](calibration.md) to re-record the zero position and active range. When the program requires manual collection of the range, slowly move each joint to the allowed stroke range to avoid forcibly resisting the mechanical limit.
4. Confirm that changes are recorded in all joints, and then save according to the program prompts.
5. Using the same device path and ID as for calibration, first verify the small movements of the single arm before enabling the entire machine.

Calibration data cannot be copied directly from another robot arm. When the range is abnormal, complete the measurement again. Do not fill in the value manually to bypass the check.

## E002: Left bus missing servos 8–11

The joints of the second generation AM-ARM are **1–7**; the chassis wheels are **8, 9, 10**; the lift is **11**. The left bus needs to connect the robotic arm and the chassis/elevating branch at the same time, while the right bus only connects the robotic arm. The robot arm servo numbers of SO-ARM are 1–6.

1. Stop the Host and disconnect the actuator power supply, and check whether the two buses on the left arm driver board are firmly connected.
2. Check the connection from the chassis to the lift and then to the left drive board to avoid missing branch circuits.
3. After repowering, read the left bus status on the Raspberry Pi:

```bash
python examples/debug/motors.py get_motors_states \
  --port /dev/am_arm_follower_left
```

4. If it only reads 1–7, check whether the left and right USB ports are reversed, and then check the chassis/lift branch circuit.
5. Compare the [Device configuration](configuration.md) and rebind the left and right aliases; confirm that the required servos can be read before starting the Host of the matching model.

## E003: Raspberry Pi times out when launching multiple cameras

Insufficient power supply may prevent multiple cameras from starting at the same time. `Timed out waiting for frame` can also come from the wrong port, used by another process, USB bandwidth, or an unsupported resolution.

1. Check the battery power, power board interface and cables according to the [Power supply diagram](unboxing.md).
2. Stop the Host first and confirm that the camera is not occupied by other preview programs.
3. Use [Camera discovery steps](configuration.md) to individually check each device and supported formats.
4. Enable one camera first, then increase the number of cameras one by one after stabilization; record which camera or combination triggers the error.
5. The Raspberry Pi and PC use the same camera configuration. After modification, restart the programs on both ends.

`head_top` and `forward` are camera naming in different software configurations, and the actual data keys and device aliases must be checked. You cannot directly hand over the data of one set of names to another set of configuration training or inference.

## E004: The servo status cannot be read or the indicator light does not light up.

1. Confirm that the driver board has an independent power supply and check the voltage corresponding to the arm; the USB connection itself does not mean that the servo is powered.
2. Check the data cable, port permissions and serial port alias, and close other programs occupying the same serial port.
3. After the power is turned off, recheck the connectors and check the series wiring section by section.
4. When it is necessary to isolate a fault, only connect one confirmed compatible servo after each power outage, and then perform a reading test.
5. If the power supply, data cable, port and known normal servo are all verified and still fails, contact support to determine whether the driver board needs to be replaced.

The compatible gripper servo can be connected to the drive board separately for troubleshooting. A communication failure alone does not prove that the control board is damaged.

## Update software and network access

Save the local configuration first and then update. Do not treat `git restore .` as a regular update step, it will discard uncommitted workspace modifications.

```bash
cd lerobot_alohamini
git status
git diff
```

If there are changes to the local configuration, back it up or submit it first and confirm the purpose; execute it after the workspace is ready:

```bash
git pull --ff-only
```

When prompted that fast forwarding is not possible, first handle the differences between the local submission and the remote submission to avoid direct overwriting. After the update is completed, check the software version, model and camera configuration of the Pi and PC.

If you use the proxy in your own LAN, you can set it in the current terminal:

```bash
# 替换为你自己的代理服务器地址和端口
export http_proxy=http://192.168.50.XXX:7890
export https_proxy=http://192.168.50.XXX:7890
curl -I https://github.com
```

The agent needs to allow this LAN client to connect. The above placeholder IP cannot be run directly, nor should it be inherited from other people's addresses in the screenshot.

## Provide this information when submitting your question

- Model: 2 / 2 Pro, leader arm and follower arm profiles.
- Error location: Pi Host, PC teleoperation, acquisition, training or evaluation.
- Complete command, replace private directory and other information that does not need to be disclosed.
- At the end of the error report, left and right device aliases, enabled camera names, and recent changes.
- Can the fault be reproduced with a single arm or single camera.
