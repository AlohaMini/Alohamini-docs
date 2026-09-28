# Device and model configuration

This page advances "The device can be found" to "The program is using the correct device." First distinguish the robot model, leader arm model, left and right serial ports and camera names before starting calibration.

## 1. Select the robot and leader arm configuration

| actual robot | Host `--robot_model` | PC `--robot.robot_model` | PC `--teleop.arm_profile` |
| --- | --- | --- | --- |
| AlohaMini 1 + SO leader arm | `alohamini1` | `alohamini1` | `so-arm-5dof` |
| AlohaMini 2 + AM Main Boom | `alohamini2` | `alohamini2` | `am-leader-6dof` |
| AlohaMini 2 Pro + AM leader arm | `alohamini2pro` | `alohamini2pro` | `am-leader-6dof` |

**The robot model must be consistent at both ends.** `robot_model` determines the follower arm, chassis and lifting configuration; `teleop.arm_profile` describes the leader arm on the PC. Pro still uses the AM leader arm configuration and does not fill in the `am-follower-6dof-hd` of the follower arm into the leader arm parameters.

Currently, some client scripts default to the first generation, while Host configuration defaults to the second generation. Therefore, the commands in this manual explicitly specify the model to avoid relying on inconsistent default values.

## 2. Find the serial port of each robot arm

Connect to the control board one by one on the corresponding machine and record the ports:

```bash
lerobot-find-port
ls /dev/ttyACM*
ls /dev/serial/by-id/
```

| machine | Equipment that needs to be distinguished |
| --- | --- |
| PC | Left leader arm, right leader arm |
| Pi | Left follower arm bus, right follower arm bus |

`lerobot-find-port` will first record the device list, then prompt to unplug the USB of the target control board and press Enter, and finally find the port according to the changes. Reattach the board when finished. Unplug only one board at a time to avoid having multiple candidate ports.

The numbers of `ttyACM0` and `ttyACM1` may change after restarting or replugging. Do not rely solely on the order first observed for long term use.

## 3. Fixed left and right arm device names

Project arm scripts use fixed paths. The following udev aliases can be created, or the real ports in the script can be modified; the same device must be consistent across calibration, teleoperation, and recording.

### Read control board serial number

```bash
udevadm info --attribute-walk --name=/dev/ttyACM0 | awk -F'"' '/ATTRS{serial}/{print $2; exit}'
```

Read each board individually and record its physical location. If different boards do not have unique serial numbers that can be distinguished, the following serial number-based rules cannot uniquely identify them and require further configuration based on actual USB device information.

### Pi: follower arm rule

Edit `/etc/udev/rules.d/90-mydevice.rules` and fill in the real serial number:

```text
SUBSYSTEM=="tty", ATTRS{serial}=="<follower_left_serial>", SYMLINK+="am_arm_follower_left"
SUBSYSTEM=="tty", ATTRS{serial}=="<follower_right_serial>", SYMLINK+="am_arm_follower_right"
```

### PC: Main Boom Rules

Fill in the rules file with the same name on the PC:

```text
SUBSYSTEM=="tty", ATTRS{serial}=="<leader_left_serial>", SYMLINK+="am_arm_leader_left"
SUBSYSTEM=="tty", ATTRS{serial}=="<leader_right_serial>", SYMLINK+="am_arm_leader_right"
```

### Reload and check

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
ls -l /dev/am_arm_*
```

After checking the control board pointed by the alias, plug and unplug again to confirm stability. The Pi configuration file is:

```text
src/lerobot/robots/alohamini/config_alohamini.py
```

where the follower arm field should point to:

```python
left_port: str = "/dev/am_arm_follower_left"
right_port: str = "/dev/am_arm_follower_right"
```

On the PC, the two-arm entrances such as `calibrate_bi.py`, `teleoperate_bi.py`, and `record_bi.py` should use the corresponding paths of the left and right leader arms. Give priority to stable aliases to reduce inconsistencies caused by multiple changes.

## 4. Find the camera and supported formats

Execute on Pi:

```bash
lerobot-find-cameras
v4l2-ctl --list-devices
v4l2-ctl -d /dev/video0 --list-formats-ext
```

`v4l2-ctl` `v4l-utils` toolkit from Linux; needs to be installed if not installed. Confirm which position the picture corresponds to one by one, and record the device path, resolution and frame rate.

| Hardware perspective | name in current configuration |
| --- | --- |
| forward | `forward` |
| backward | `backward` |
| chest | `chest` |
| left wrist | `wrist_left` |
| right wrist | `wrist_right` |

### Five-way hardware does not mean that five-way is enabled by default.

Currently, `alohamini_cameras_config()` enables two **channels,**`forward` and `wrist_right`, by default, and the other three channels are commented. The default acquisition parameters are **640×480, 30 FPS**; these are parameters at different levels from the hardware resolution description of the camera in the BOM.

The default path uses aliases such as `/dev/am_camera_forward`. If these aliases are not available on the device, you need to modify `index_or_path` based on the camera discovery results, or establish a stable camera device mapping yourself. Camera aliases are not automatically generated by completing the robot udev rules.

### Configuration example

Modify the entries in `alohamini_cameras_config()` according to the existing configuration file, for example:

```python
"forward": OpenCVCameraConfig(
    index_or_path="/dev/video0",
    fps=30,
    width=640,
    height=480,
    rotation=Cv2Rotation.NO_ROTATION,
),
```

`/dev/video0` is just an example and does not replace device discovery. If you need another perspective, uncomment the corresponding entry and confirm that its path is valid. If both ends use this function to generate features, they should keep the camera name consistent with the configuration, and restart the Host and client after modification.

The original guide for the software recommends that cameras be connected to separate USB ports to avoid multiple cameras sharing the same USB Hub. If the actual bandwidth is insufficient, first reduce the number of enabled channels, reduce the collection load, and check the picture stability.

## 5. Confirm network and port

Note the Pi's actual LAN IP and replace `<Pi_IP>` in the command with that address. Check on PC:

```bash
ping <Pi_IP>
```

| TCP port | Purpose |
| --- | --- |
| 5555 | control command |
| 5556 | Status, Observations and Metadata |
| 5557 | Optional standalone camera stream; requires explicit enablement by Host |

`ping` success only proves basic connectivity. It is also necessary to confirm that the Host starts normally, the corresponding port is not occupied, and the network allows access. For detailed control frequency and feedback mechanism, see [Operating mechanism](runtime.md).

## Configuration completion check

- The model of the whole machine at both ends is the same, and the leader arm profile is consistent with the real thing.
- The left and right ports of the four robotic arms can be stably identified.
- Each enabled camera in the configuration has the correct picture.
- The camera name corresponds to the name required for subsequent data sets and policies.
- The PC can access the Pi and the software versions are compatible with each other.

After completion, enter [Arm calibration](calibration.md).


## Camera naming differences in delivery tutorial

Different software configurations may use `head_top`, `head_back`, `head_front`, or `forward`, `backward`, `chest`. These names cannot be freely interchanged after collection.

1. View the actual enabled items for this machine `alohamini_cameras_config()`.
2. Check the device path with the actual screen, and then synchronize the same configuration to Pi and PC.
3. `observation.images.*`, training input, and evaluation observations are consistent across the dataset.
4. When using a purely visual transformation script, `--keep-camera` also fills in the names that actually exist in the dataset.
