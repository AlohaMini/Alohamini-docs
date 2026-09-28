# Debugging and troubleshooting

This page provides troubleshooting steps for software environment, power supply, serial port, servo, calibration, camera, network and data acquisition faults. First find the corresponding phenomenon, then operate in sequence, adjust only one configuration at a time, and keep the error logs of the robot and PC.

When wiring is involved, first stop the control program and disconnect power from the actuator. The servo number and model parameters are as described for AlohaMini 2 / 2 Pro; for other hardware, please use the corresponding configuration.

## Quick positioning

| phenomenon | Priority check | Steps to process this page |
| --- | --- | --- |
| The command does not exist and the module import failed. | Python environment, installation location and version | [software environment](#ts-environment) |
| The robotic arm cannot be found and the serial port has no permissions. | Data cables, device nodes, permissions and port occupancy | [Serial port check](#ts-serial) |
| Servos No. 8-11 are missing and the servo lights are not on. | Supply, bus branches and numbering | [E002 / E004](#ts-motors) |
| The calibration range is the same and calibration is required repeatedly after startup. | Actual activity scope, device ID and profile | [E001: Calibration check](#ts-calibration) |
| Camera missing, picture connection reversed, frame acquisition timed out | Power delivery, paths, formats and USB bandwidth | [E003: Camera inspection](#ts-cameras) |
| Connection timeout, picture and motion lags | Host, IP, network and compute load | [Network and performance](#ts-network) |
| Recording resumption failed, video encoding failed | Data Catalog, Characteristics and Coding Environment | [Recording and video](#ts-recording) |
| Model dimensions do not match, evaluation paused | Data characteristics, models and protection logs | [strategic assessment](#ts-policy) |
| Update failed or unable to connect to the code repository | Local changes, branch status and network | [Software updates](#ts-update) |

(ts-environment)=

## 1. Confirm the current software environment

```bash
pwd
python --version
python -c "import sys; print(sys.executable)"
python -c "import av, cv2, torch; print('av', av.__version__); print('cv2', cv2.__version__); print('torch', torch.__version__)"
git rev-parse --short HEAD
```

Expectation: The current directory is the software repository; Python comes from the activated project environment; key dependencies can be imported. When the versions submitted by two machines are inconsistent, first confirm whether the protocols are compatible, and then locate the communication layer problem.

(ts-serial)=

## 2. The serial port cannot be found or has no permissions

```bash
lerobot-find-port
ls -l /dev/ttyACM*
ls -l /dev/serial/by-id/
ls -l /dev/am_arm_*
groups
```

### Device node not found

Plug in the control boards one by one, checking the data cables, USB connections, and control board power supply. The charging-only Type-C cable does not provide serial communication; the old `/dev/ttyACM0` number may also have been changed.

### The device exists, but the program does not have permission

Check whether the current user belongs to the `dialout` group; log in again after adding the group. Do not override permission configuration by permanently running the entire bot as root.

### The alias exists, but the left and right are wrong

Return to the udev rules and compare the serial number and physical location of each board. Calibration files, teleoperation and recording must always use the same left and right mapping.

### Port is occupied

Stop a previously running host, calibration, teleoperation, or hardware debugger. While one program is still using the serial port, another program may not be able to connect properly.

(ts-motors)=

## 3. servo status and number

Check the servo status on the connection bus:

```bash
python examples/debug/motors.py get_motors_states \
  --port /dev/ttyACM0
```

Check whether the read ID, model number and status match the actual wiring. When writing a new ID, only connect to the target servo each time:

```bash
python examples/debug/motors.py configure_motor_id \
  --id 1 \
  --set_id 8 \
  --port /dev/ttyACM0
```

The target IDs of the second-generation chassis are 8 for the right rear wheel, 9 for the front wheel, 10 for the left rear wheel, and 11 for the lift; the left and right are based on the direction of the robot itself.

### Check before debugging scripts using old hardware

`examples/debug/wheels.py` and `axis.py` are tools for direct access to the bus. The servo model constant in the current file is still `sts3215`. `axis.py` will not automatically select STS3095 based on the second-generation configuration of the whole machine; the wheel set script also has its own wheel position naming and kinematic constants.

Therefore, for the first robot inspection of **second generation/Pro, the Host + keyboard client** that matches `robot_model` is given priority. Only after confirming that the script's model, ID, and structure match, run the independent debugging script directly.

Changing phases, resetting neutral, releasing torque, and executing action scripts change the state of the hardware and are not general "fix all problems" operations. Do not modify phase or reset neutral without confirming the cause.

### E002: Left bus missing servos 8–11

The joints of the second generation AM-ARM are **1–7**; the chassis wheels are **8, 9, 10**; the lift is **11**. The left bus needs to connect the robotic arm and the chassis/elevating branch at the same time, while the right bus only connects the robotic arm. The robot arm servo numbers of SO-ARM are 1–6.

1. Stop the Host and disconnect the actuator power supply, and check whether the two buses on the left arm driver board are firmly connected.
2. Check the connection from the chassis to the lift and then to the left drive board to avoid missing branch circuits.
3. After repowering, read the left bus status on the Raspberry Pi:

```bash
python examples/debug/motors.py get_motors_states \
  --port /dev/am_arm_follower_left
```

4. If it only reads 1–7, check whether the left and right USB ports are reversed, and then check the chassis/lift branch circuit.
5. Rebind the left and right serial port aliases according to the serial number of each control board; confirm that the required servos can be read before starting the Host of the matching model.

### E004: The servo status cannot be read or the indicator light does not light up.

1. Confirm that the driver board has an independent power supply and check the voltage corresponding to the arm; the USB connection itself does not mean that the servo is powered.
2. Check the data cable, port permissions and serial port alias, and close other programs occupying the same serial port.
3. After the power is turned off, recheck the connectors and check the series wiring section by section.
4. When it is necessary to isolate a fault, only connect one confirmed compatible servo after each power outage, and then perform a reading test.
5. If the power supply, data cable, port and known normal servo are all verified and still fails, contact support to determine whether the driver board needs to be replaced.

The compatible gripper servo can be connected to the drive board separately for troubleshooting. A communication failure alone does not prove that the control board is damaged.

(ts-calibration)=

## 4. Match the calibration range to the equipment (E001)

**Common reasons**: After triggering recalibration, the saved range is confirmed without actually moving the joint.

1. Stop teleoperation and confirm that the current terminal connected is indeed the target robotic arm.
2. Check leader arm `am-leader-6dof`; standard 2 follower arm `am-follower-6dof`; Pro follower arm `am-follower-6dof-hd`.
3. Start the calibration process of the corresponding device and re-record the zero position and range of motion. When the program requires manual collection of the range, slowly move each joint to the allowed stroke range to avoid forcibly resisting the mechanical limit.
4. Confirm that changes are recorded in all joints, and then save according to the program prompts.
5. Using the same device path and ID as for calibration, first verify the small movements of the single arm before enabling the entire machine.

Calibration data cannot be copied directly from another robot arm. When the range is abnormal, complete the measurement again. Do not fill in the value manually to bypass the check.

### Start recalibration

First exit the Host, teleoperation and debugging programs that occupy the serial port. On the Raspberry Pi, select a command to calibrate the follower arm by model:

**AlohaMini 2**

```bash
python -m lerobot.robots.alohamini.alohamini_calibrate --robot_model alohamini2
```

**AlohaMini 2 Pro**

```bash
python -m lerobot.robots.alohamini.alohamini_calibrate --robot_model alohamini2pro
```

To calibrate the AM dual leader arm on PC:

```bash
python examples/alohamini/calibrate_bi.py \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof
```

Follow the terminal prompts to select recalibration and complete the recording of the median and range of motion. After completion, power off the leader and follower arms and restart it, and use the same device ID and profile to check small movements.

### Repeated requests for calibration or abnormal follower arm orientation

1. Check that the current device ID, left and right serial ports are consistent with those during calibration.
2. The leader arm uses `am-leader-6dof`; the 2 follower arm uses `am-follower-6dof`, and the 2 Pro follower arm uses `am-follower-6dof-hd`.
3. The Raspberry Pi is consistent with the PC's `robot_model`: `alohamini2` for the 2 and `alohamini2pro` for the 2 Pro.
4. After replacing the servo, adjusting the assembly or profile, re-measure the calibration range of the corresponding equipment.
5. Start checking with small movements of the single-sided robotic arm, and make sure the left and right, direction, and stroke are correct before starting the whole machine.

(ts-cameras)=

## 5. The camera cannot be opened or the picture is missing (E003)

```bash
lerobot-find-cameras
v4l2-ctl --list-devices
v4l2-ctl -d /dev/video0 --list-formats-ext
```

Check in the following order:

1. Whether the camera is recognized by the system and whether `index_or_path` is pointed at it.
2. Whether the resolution and frame rate required by the configuration are supported by the device.
3. The camera is occupied by another program.
4. Host configures which cameras are enabled and whether the devices are all connected.
5. Which physical position does the current screen correspond to, and whether the left and right wrists are connected reversely.
6. Are there issues with USB bandwidth, power delivery, or sharing the Hub with multiple devices.

After modifying the camera configuration, restart the related programs on both ends. Only two channels are enabled by default. Seeing five physical cameras does not mean that the program will automatically use five channels.

### Multiple camera startup timeout

Insufficient power supply may prevent multiple cameras from starting at the same time. `Timed out waiting for frame` can also come from the wrong port, used by another process, USB bandwidth, or an unsupported resolution.

1. Check the battery power, power board interface and cables, and verify that the power supply voltage is consistent with the device nameplate.
2. Stop the Host first and confirm that the camera is not occupied by other preview programs.
3. Use the camera discovery and format query commands in this section to check each device individually.
4. Enable one camera first, then increase the number of cameras one by one after stabilization; record which camera or combination triggers the error.
5. The Raspberry Pi and PC use the same camera configuration. After modification, restart the programs on both ends.

`head_top` and `forward` are camera naming in different software configurations, and the actual data keys and device aliases must be checked. You cannot directly hand over the data of one set of names to another set of configuration training or inference.

(ts-network)=

## 6. Network connection and performance

PC Check Pi:

```bash
ping <Pi_IP>
```

Check the link on the machine using the wireless network:

```bash
iw dev
iw dev wlan0 link
```

`wlan0` needs to be replaced with the actual wireless network card name. When you need to measure throughput and iperf3 is installed, run on the Host:

```bash
iperf3 -s
```

Run on PC:

```bash
iperf3 -c <Pi_IP>
```

Exit the iperf3 service after the test is completed. Normal network delay or throughput does not mean that the entire control link is normal. Device collection and CPU load must also be combined.

### Observe compute load

```bash
top
```

If the training PC uses NVIDIA GPU, you can view:

```bash
nvidia-smi
```

When teleoperation freezes, first set the startup parameters to `--fps 10 --camera-fps 10` to temporarily reduce the frequency of control and camera requests. Check the CPU, network and camera before restoring the official acquisition configuration.

(ts-recording)=

## 7. Recording and video issues

### The dataset directory already exists

Check whether this is a new entry or a renewal. Continued recordings use the same data identifier and directory and add `--resume`; new experiments use new names. Do not directly delete old data to eliminate errors.

### Multi-frequency acquisition time is longer than set

This entry needs to collect enough fresh frames, which will take longer when the actual camera frame rate is slightly lower. If explicitly aborted, check the logs for camera freezes, cross-camera time differences, state alignment, or framerate deficiencies.

### Video encoding/decoding failed

```bash
ffmpeg -version
ffmpeg -hide_banner -encoders
python -c "import av; print(av.__version__)"
```

Confirm that the environment is consistent and the video file has been completely saved, and then locate the missing encoder or backend according to the error. Do not copy a work-in-progress data set while writing has not yet completed.

(ts-policy)=

## 8. policy evaluation and model dimensions

### Model input or action dimension mismatch

1. Confirm that the data set used for model training corresponds to the current model. 2 / 2 Pro The entire machine interface is 18-dimensional; single arms or simulation data of different dimensions cannot be used directly.
2. Check the camera name, order and enabled quantity. Names such as `head_top` and `forward` must be consistent with the training features.
3. Check joint order, units, profile and calibration configuration; the same number of dimensions is still not enough to prove compatibility.
4. After completing the configuration matching, run a short test to confirm that the observation is valid and the action direction is correct.

### Assessment inactivity or sudden pause

- First make sure that no teleoperation or recording client still holds control.
- Check whether the models of Pi and PC are consistent and whether the model directory is correct.
- Check whether the Host triggers current protection, watchdog or restarts.
- Check whether the client is lacking fresh feedback, or policy inference is taking too long to cause the Host to time out.
- ACT uses `sync`; RTC must be supported by the model interface.

Old action queues will not automatically resume execution after being paused. After handling the fault, restart according to the program flow to avoid mistaking "no further action" for simple network packet loss.

(ts-update)=

## 9. Software updates and network access

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

## 10. Submit reproducible issues

Submit the following content together to [Software Issues](https://github.com/liyiteng/lerobot_alohamini/issues):

```text
机型：AlohaMini 1 / 2 / 2 Pro
主臂与从臂型号：
PC 系统、CPU/GPU：
Pi 系统与架构：
两端软件提交版本：
操作阶段：安装 / 校准 / 遥操作 / 录制 / 训练 / 评估
完整命令（移除访问令牌等秘密）：
预期结果：
实际结果：
Host 日志：
PC 日志：
最近修改过的配置：
```

For hardware assembly issues, please add partial photos, part names and materials, and submit them to [Hardware Issues](https://github.com/liyiteng/AlohaMini/issues).
