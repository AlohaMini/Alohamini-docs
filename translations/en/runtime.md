# Runtime and safety

This page explains the current software's control frequency, feedback checks, command ownership and current protection to help analyze "why it stopped sending actions" or "why another client couldn't take over". The value comes from the current software description and needs to be rechecked after modifying the configuration or upgrading the version.

## Control, Image and Data Frequency

| link | current behavior |
| --- | --- |
| Host control | Command handling, feedback, watchdog and protection checks target 50 Hz |
| Native teleoperation | Control target 50 Hz, camera request default 30 Hz |
| Single channel recording | Both control and sampling use `dataset.fps` |
| Multi-channel recording | 50 Hz control, writes freshly aligned samples at data set frequency |
| Camera independent release | Publish via TCP 5557 when enabled explicitly |

The robot arm position control uses the speed and acceleration configuration on the servo side. The current configuration fields `arm_goal_velocity` and `arm_acceleration` use the original register unit of the servo, and the values cannot be directly interpreted as universal degrees/seconds or meters/seconds.

## network interface

| port | data |
| --- | --- |
| 5555 | control command |
| 5556 | Observations, state, and metadata; traditional requests retain state vs. image responses |
| 5557 | Optional standalone camera stream |

Pure status is returned when the status request token ends with `:state`. ROS compatible camera streaming requires Host to be explicitly enabled:

```bash
python -m lerobot.robots.alohamini.alohamini_host \
  --robot_model alohamini2 \
  --camera-stream
```

Enabling camera streaming will not automatically change the default two-channel camera to five-channel. The activation list is still determined by the camera configuration.

## A single client has control

The first client to send a valid command takes control, and the host rejects other writers. Pure state observers do not take control.

When the current controller exceeds the default **1 second and** does not send a command, the Host first stops moving and then releases control. When switching between teleoperation, recording and evaluation, you should first stop the current controller and wait for release before starting the new controller.

The new client binds commands to the Host session and control epoch to distinguish commands before and after a restart or takeover. Host and PC should be upgraded together; legacy unidentified commands are handled as a shared legacy controller, lack the same session replay protection, and multiple legacy command clients should not be running simultaneously.

## Feedback must be current enough

Before the PC sends a command, complete feedback from the request issued within the last **250 ms** is required. Stop sending new commands when the response is missing to prevent continued execution based on expired status.

Expired feedback will be updated after synchronization policy inference; this limit is not equal to the inference time limit. After watchdog, joint protection, Host restart or control change, the evaluation will be paused and cleared of pending actions, waiting for explicit recovery.

## Current protection parameters

The following are the current parameters listed in the software documentation, in A:

| servo | Rated | stalled | collision hold | Sustained overload stops | Close to stalled stop |
| --- | ---: | ---: | ---: | ---: | ---: |
| STS3215 | 0.9 | 2.7 | 1.35 | 1.8 | 2.16 |
| STS3095 | 2.2 | 9.8 | 3.3 | 4.4 | 7.84 |
| STS3250 | 1.4 | 4.2 | 2.1 | 2.8 | 3.36 |

### collision hold

The current logic needs to simultaneously meet the current threshold, a target error of at least **2°**, and **150 ms** insufficient inward target advance of **0.2°**. Position differences are converted to angles by calibration, including with normalized coordinates.

The hold can be released by moving the target in the opposite direction past the hold position. Host monitors active targets every control cycle, even if there are no new commands in that cycle; corresponding protection modifications are written only when the target changes.

### Overload and near stall

It stops after the continuous overload reaches **650 ms**; it stops after the near-lock reaches **80 ms**. The duration is judged based on the actual elapsed time, and trigger detection occurs at the next feedback sample, so it is not a hardware power-off commitment accurate to milliseconds.

The grippers also have **0.5 A** contact thresholds. The motor current in the observation metadata uses **mA**. Pay attention to unit conversion when analyzing the log.

These software mechanisms are used to limit abnormal movements and cannot replace reasonable mechanical assembly, movement space and actual testing. When triggering repeatedly, check the load, jamming, calibration and control targets first.

## Camera timestamps and missing images

The missing image alarm is generated based on the host's enabled camera list and is prompted according to the missing image stage. Pure status responses will not be falsely reported as missing images; when the old host does not have camera metadata, the client uses the local camera configuration.

Cached images and placeholder images do not get new acquisition timestamps. Multi-frequency recording can therefore distinguish new images from repeated old images, avoiding the misunderstanding that "there are still images in the window" as the camera is continuously collecting.

## Check order

When an action pause occurs, first determine: whether the Host is still online → whether the control belongs to the current client → whether the feedback is fresh → whether joint protection is triggered → whether the camera meets the recording requirements. For specific check commands, see [Debugging and troubleshooting](troubleshooting.md).
