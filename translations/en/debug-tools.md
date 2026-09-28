# Servo and performance debugging

This page explains how to read servo status, set numbers, and check network and computational load. The port, ID, phase and position values need to be filled in according to the actual hardware. First end the Host or client occupying the same bus, and then connect the debugger.

## 1. Read status and confirmation ID

```bash
python examples/debug/motors.py get_motors_states \
  --port /dev/ttyACM0
```

Confirm that the servo model and ID read are consistent with the wiring. When only one numbered servo is connected, modify its ID:

```bash
python examples/debug/motors.py configure_motor_id \
  --id 1 --set_id 8 --port /dev/ttyACM0
```

`1` and `8` are example values. The chassis number is based on the assembly drawing of the corresponding model, and the robot arm number is defined on its joints; re-read and verify after modification.

## 2. Move the designated servo

```bash
python examples/debug/motors.py move_motor_to_position \
  --id <motor_id> \
  --position <target_tick> \
  --port /dev/ttyACM0
```

`position` is the raw tick, not the angle or millimeters. `2` is only an example of position values and cannot be used as a test target for all joints. Only execute small range motion after confirming the current value, zero position, mechanical range and surrounding space.

## 3. Modify phase

Specify a servo:

```bash
python examples/debug/motors.py configure_motor_phase \
  --id <motor_id> \
  --set_phase <phase_value> \
  --port /dev/ttyACM0
```

Omitting `--id` will act on multiple servos found by the script:

```bash
python examples/debug/motors.py configure_motor_phase \
  --set_phase <phase_value> \
  --port /dev/ttyACM0
```

Confirm the connection object before batch operation. Do not regard example values such as `12` as universally correct values; keep the old configuration and confirm whether recalibration is needed after changes.

## 4. Neutral position, torque and action script

Related configurations for setting the current position to the median:

```bash
python examples/debug/motors.py reset_motors_to_midpoint \
  --port /dev/ttyACM0
```

Parts of the front support that will fall due to gravity when the torque is closed:

```bash
python examples/debug/motors.py reset_motors_torque \
  --port /dev/ttyACM0
```

Execute after confirming that each target position in the script matches the actual object:

```bash
python examples/debug/motors.py move_motors_by_script \
  --script_path /path/to/checked_action_script.txt \
  --port /dev/ttyACM0
```

These operations change the hardware status and do not replace the [Calibration process](calibration.md). Full parameter help:

```bash
python examples/debug/motors.py --help
```

## 5. Independent entrance for chassis and lift

The old independent debugging entrance is as follows:

```bash
python examples/debug/wheels.py --port /dev/ttyACM0
python examples/debug/axis.py --port /dev/ttyACM0
```

The current script retains the `sts3215` model constants and independent wheel positions and geometric parameters, and will not automatically read the second-generation or Pro machine profile. **second generation/Pro is preferred for first time debugging. [Only chassis and lift teleoperation](teleoperation.md)**; do not think that replacing the serial port completes model adaptation.

## 6. Network and Wi-Fi

```bash
ping <Pi_IP>
iw dev
iw dev wlan0 link
```

`wlan0` should be replaced with the interface listed by `iw dev`. Observe packet loss, delay fluctuations and link information; a single low delay does not mean stable continuous video transmission.

When iperf3 is already available, run the service on the Pi:

```bash
iperf3 -s
```

Connect on PC:

```bash
iperf3 -c <Pi_IP>
```

The bandwidth test will occupy the link and be performed during the independent debugging phase; the results are mainly used to judge the current network conditions.

## 7. CPU, GPU and video encoding

```bash
top
htop
nvidia-smi
ffmpeg -hide_banner -encoders
python -c "import av, cv2, torch; print('av', av.__version__); print('cv2', cv2.__version__); print('torch', torch.__version__)"
```

`htop` may require additional installation, `nvidia-smi` is only available on devices with NVIDIA drivers. Just because the encoder is listed in the list does not mean that the current hardware and dependencies can be executed smoothly. It needs to be confirmed with real recording logs.

## 8. Comparison after reducing load

Press [Teleoperation low load example](teleoperation.md) and [Short data test](learning.md) Use native model, temporarily reduce FPS or enable camera number. Only change one item at a time and record the network, CPU, camera missing frames and recording results. After the problem disappears, restore the configuration one by one to avoid mistaking low-load troubleshooting settings for formal training data specifications.
