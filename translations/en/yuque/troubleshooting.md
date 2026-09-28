# Exception handling

[Return to official manual](../official-manual.md)

Check in order of power supply, wiring, serial port and configuration. For the complete process, see [Robot troubleshooting](../support.md).

(yq-phx3zdv7indeo98e-XabvX)=

## E001 ·Error when calibrating the robot arm: the prompt values are the same

(yq-phx3zdv7indeo98e-uf77ccc29)=

**recurrence command**

```bash
python -m lerobot.robots.alohamini.alohamini_host  --robot_model xxxxx
```

(yq-phx3zdv7indeo98e-ud6064b8d)=

**error message**

```text
ValueError: Some motors have the same min and max values
```

(yq-phx3zdv7indeo98e-ue0be39b4)=

**fault reason**

(yq-phx3zdv7indeo98e-ua317a5e7)=

Pressing `C` during the calibration process triggered recalibration, but no joint movement was actually performed, resulting in the same Min/Max values being written and the calibration file being invalid.

(yq-phx3zdv7indeo98e-u09828a48)=

**solution**

(yq-phx3zdv7indeo98e-ua9c26770)=

Read the novice tutorial and re-execute the complete calibration process to ensure that each joint has moved to the corresponding physical limit position before pressing OK.

(yq-phx3zdv7indeo98e-u7b4bf001)=

(yq-phx3zdv7indeo98e-X33bp)=

## E002 · Left arm missing servos 8–11

(yq-phx3zdv7indeo98e-u9b1458d8)=

**recurrence command**

```bash
python -m lerobot.robots.alohamini.alohamini_host --robot_model xxxxx
```

(yq-phx3zdv7indeo98e-uf5131a77)=

**error message**

```text
Missing motor IDs:
8 (expected model: 777)
9 (expected model: 777)
10 (expected model: 777)
11 (expected model: 777)

Full expected motor list (id: model):
1:777, 2:777, 3:777, 4:777, 5:777, 6:777,
8:777, 9:777, 10:777, 11:777
```

(yq-phx3zdv7indeo98e-u47b4a409)=

**fault reason**

(yq-phx3zdv7indeo98e-u3977c307)=

1. The left arm servo drive board needs to be connected to two buses: one to the robotic arm (connected to servos No. 1-6), and one to the lifting axis (connected to servos No. 8-11). If the bus on the lifting axis side is missing, the drive board will not be able to enumerate servos No. 8–11.

(yq-phx3zdv7indeo98e-uc15df730)=

2. The left and right arms are reversed. The left arm corresponds to servos No. 1-11, and the right arm corresponds to servos No. 1-7. Re-modify the port number in the code to correspond to the correct robot arm

(yq-phx3zdv7indeo98e-u0779d974)=

**solution**

1. Check the left arm servo driver board to confirm that the bus from the lift axis is plugged in correctly.

1. After reconnecting, use `get_motors_states` to verify whether all servos on the bus can be enumerated normally:

(yq-phx3zdv7indeo98e-ud5b49591)=

After confirming that all servos 1–11 appear, start the host again.

(yq-phx3zdv7indeo98e-u7da7ed1d)=

(yq-phx3zdv7indeo98e-k8RjX)=

## E003 · Raspberry Pi voltage or current is insufficient

(yq-phx3zdv7indeo98e-u5be9957a)=

(yq-phx3zdv7indeo98e-u28a0a6ce)=

**recurrence command**

```bash
python -m lerobot.robots.alohamini.alohamini_host --robot_model xxxxx
```

(yq-phx3zdv7indeo98e-u0bb53cf6)=

**error message**

```text
TimeoutError: Timed out waiting for frame from camera OpenCVCamera(/dev/am_camera_wrist_left) after 1000 ms. Read thread alive: True.
FATAL: exception not rethrown
Aborted
```

(yq-phx3zdv7indeo98e-u961dba9a)=

**fault reason**

(yq-phx3zdv7indeo98e-u02c67d85)=

The voltage or current input of Raspberry Pi is insufficient and cannot activate more than 2 cameras at the same time.

(yq-phx3zdv7indeo98e-ua5b38be4)=

**solution**

1. Check the battery level, fully charge the battery and try again.

(yq-phx3zdv7indeo98e-u5fccd10f)=

(yq-phx3zdv7indeo98e-sD0bI)=

## E004 · Unable to read the status of the robotic arm/the servo light does not light up

(yq-phx3zdv7indeo98e-u77ec1a6e)=

(yq-phx3zdv7indeo98e-u84ba3c65)=

**recurrence command**

```bash
python examples/debug/motors.py get_motors_states \
  --port /dev/ttyACM0
```

(yq-phx3zdv7indeo98e-udb438f25)=

**error message**

```text
No motors found in ID range [1, 22] on COM12.FATAL: exception not rethrown
```

(yq-phx3zdv7indeo98e-uf65b18a6)=

**fault reason**

(yq-phx3zdv7indeo98e-u02a8019f)=

1. There is no power supply to the driver board or the battery power is extremely low.

(yq-phx3zdv7indeo98e-u4be0910c)=

2. Connect the gripper directly to the servo drive board, and then execute the get_motors_states command. If the servo status still cannot be read, it can be determined that the servo drive board is damaged.

(yq-phx3zdv7indeo98e-ub7b03dfb)=

(yq-phx3zdv7indeo98e-u9bdf8e68)=

![Exception handling · Figure 1](../_static/yuque-assets/2a578fe30ade4b950011.jpeg)

(yq-phx3zdv7indeo98e-ucfd1d047)=

3. If the gripper can be read normally but other servos cannot be read, it may be that the serial port line of other joints is loose or the joint servos are damaged. You need to connect the driver boards one by one to troubleshoot.

(yq-phx3zdv7indeo98e-ufe0cfb5d)=

**solution**

1. Check whether the 5521 interface of the driver board is powered normally

1. Replace with a new servo drive board

1. Tighten the serial cables of all joints and check one by one to see if any servos are damaged.
