# AlohaMini 2 Hardware Assembly

**applicable model: Standard AlohaMini 2.** Pro users please read the [2 Pro hardware](hardware-pro.md) first; the material quantity, printouts and assembly photos on this page correspond to the standard version.

This guide provides a complete introduction to the body assembly of the **AlohaMini 2 / Mobile Base 2**. The leader arm and follower arm need to be completed independently according to [AM-ARM200 Assembly Guide](https://github.com/liyiteng/AM-ARM/tree/main/am-arm200), and then installed on the console and fuselage. The metal chassis of the 2 Pro is not included in the assembly scope of this page.

## Before starting

Prepare the parts in [Bill of materials](bom.md) and [Print list](printing.md). Dry install first, confirm the direction and fit, and then glue; the glue shall be fully cured according to the product instructions before loading. The following photos are from the second-generation assembly data of the project.

| stage | When finished you should see |
| --- | --- |
| Servo number and chassis | The three wheel servos are in the correct position and the bus connection sequence is clear. |
| Omnidirectional wheels and columns | The wheel set is fixed and the column flange completely fits the chassis. |
| Shoulders and lifts | Eight rail bearings are in place so the shoulders slide smoothly |
| Arms and camera | The left and right arms are fixed, and the camera direction and purpose are recorded. |
| Cabling and power supply | There is margin for the entire lifting stroke, and the power path is clear |
| Module debugging | The chassis, lifting and robotic arms are inspected separately before linking them. |

## 1. Set servo ID

Before **installation, only connect one servo to be configured at a time.** records the current ID first and then writes the target ID to avoid duplicate numbers on the bus.

| location | Target ID |
| --- | ---: |
| left rear wheel | 10 |
| front wheel | 9 |
| right rear wheel | 8 |
| shoulder lift | 11 |

First press the [Software installation](software.md) and configure `lerobot_alohamini`. Run the following example in the root directory of the software repository to change the servo with the current ID of 1 to 8:

```bash
python examples/debug/motors.py configure_motor_id \
  --id 1 \
  --set_id 8 \
  --port /dev/ttyACM0
```

`--id` is the current number, `--set_id` is the target number, and the serial port needs to be replaced with the actual control board path. Repeat for the remaining servos. You can also use Feite FD Debug Tool to scan and write at the baud rate of **1000000** through the Waveshare control panel; after completing one, disconnect it and then connect the next one.

## 2. Assemble the chassis

1. Clean the three chassis supports, especially the wheel wells, wire ducts, and pin holes.
2. Apply epoxy glue after the joint interview is complete.
3. Place `OB_Chassis_Locking_Wedge.stl` into the locking slot. The wedge has a taper, pay attention to the direction, and will be used to lock the column base later.
4. Apply glue to the `OB_Chassis_Frame_Joiner.stl` connector, press the chassis block tightly, and confirm that the joint is in place.


```{figure} _static/media/assembly/chassis-kit.jpg
:alt: Chassis prints and fasteners
:width: 560px

Chassis prints and fasteners
```

```{figure} _static/media/assembly/chassis-epoxy-surfaces.jpg
:alt: The glue application position of the chassis joint surface
:width: 560px

The glue application position of the chassis joint surface
```

```{figure} _static/media/assembly/chassis-locking-wedge.jpg
:alt: Locking wedge installation position
:width: 560px

Locking wedge installation position
```

```{figure} _static/media/assembly/chassis-frame-joiner.jpg
:alt: Chassis connector
:width: 560px

Chassis connector
```

```{figure} _static/media/assembly/chassis-joined-frame.jpg
:alt: The structure of three chassis spliced together
:width: 560px

The structure of three chassis spliced together
```

### Install wheel servo and bus

Install the three-wheel servo with the ID set in the direction of the photo, and fix it with the screws provided with the servo. The connection sequence is:

```text
右后轮 8 → 前轮 9 → 左后轮 10 → 升降舵机 11
```

ID 10 to ID 11 are further away, and the three-needle line is at least **90 cm**, and the original guide recommends **140 cm**. Before fixing, confirm that it can pass through the column and leave margin for lifting.


```{figure} _static/media/assembly/wheel-servos.jpg
:alt: Three wheel servo
:width: 560px

Three wheel servo
```

```{figure} _static/media/assembly/wheel-servo-id-layout.jpg
:alt: Chassis servo position and ID assignment
:width: 560px

Chassis servo position and ID assignment
```

```{figure} _static/media/assembly/wheel-servo-cable-routing.jpg
:alt: Bus wiring between wheels and servos
:width: 560px

Bus wiring between wheels and servos
```

## 3. Install omnidirectional wheels

1. Each axle connection piece comes pre-installed with four M3×10 screws.
2. Press the connector onto the servo output plate and confirm that the four mounting holes are aligned.
3. Tighten the screws through the reserved operating holes.
4. Install the omni wheel, axle, 12×18×4 mm bearing, gasket and bearing cap.
5. Check the fixation and rotation of the wheel set to prevent cables from entering the wheel movement range.


```{figure} _static/media/assembly/wheel-connectors-and-screws.jpg
:alt: Axle connector and M3×10 screws
:width: 560px

Axle connector and M3×10 screws
```

```{figure} _static/media/assembly/wheel-connector-on-servo-disc.jpg
:alt: Align the connector with the servo output disk
:width: 560px

Align the connector with the servo output disk
```

```{figure} _static/media/assembly/wheel-connector-tightening.jpg
:alt: Tighten the connection piece from the operating hole
:width: 560px

Tighten the connection piece from the operating hole
```

```{figure} _static/media/assembly/omni-wheel-hardware.jpg
:alt: Shafts, bearings and fasteners for omnidirectional wheels
:width: 560px

Shafts, bearings and fasteners for omnidirectional wheels
```

```{figure} _static/media/assembly/omni-wheel-axle-install.jpg
:alt: Install omnidirectional axle
:width: 560px

Install omnidirectional axle
```

```{figure} _static/media/assembly/omni-wheel-cover-installed.jpg
:alt: Wheel bearing cap after installation
:width: 560px

Wheel bearing cap after installation
```

## 4. Assemble the lifting column

Connect from bottom to top:

```text
O_POST4_Connector_Base.stl
  → O_Main_Assembly_Post4.stl
  → OB_Main_Assembly_Post3.stl
  → OB_Main_Assembly_Post2.stl
  → OB_Main_Assembly_Post1.stl
```

Apply glue to the contact surface section by section and press it together. Wipe off excess glue before curing to keep the surface of the rack and guide rail clean.


```{figure} _static/media/assembly/lift-tower-parts.jpg
:alt: Lifting column segmented parts
:width: 560px

Lifting column segmented parts
```

```{figure} _static/media/assembly/lift-tower-assembled.jpg
:alt: Assembled lifting column
:width: 560px

Assembled lifting column
```

### Attach the uprights to the chassis

Let the front wheel servo of **ID 9 face the operator and the column rack also face the operator**. Press the hex base into the chassis seat hole, turn the chassis over, and tap evenly on the six sides until the flange completely fits the chassis.

Lead the wheel servo cable through the center hole and side cable grooves, and then turn the chassis back to the front. Check that the wiring is not pinched by the upright base or splice surfaces.


```{figure} _static/media/assembly/tower-in-chassis-orientation.jpg
:alt: The directional relationship between the column rack and the front wheel
:width: 560px

The directional relationship between the column rack and the front wheel
```

```{figure} _static/media/assembly/tower-base-locking.jpg
:alt: Column base fixed position
:width: 560px

Column base fixed position
```

```{figure} _static/media/assembly/tower-cable-center-hole.jpg
:alt: Cables pass through the center hole of the chassis
:width: 560px

Cables pass through the center hole of the chassis
```

```{figure} _static/media/assembly/tower-cable-side-channels.jpg
:alt: Cables pass through side trunking
:width: 560px

Cables pass through side trunking
```

## 5. Assemble the shoulder lifting mechanism

Press **eight 4×13×5 mm bearings** into the shoulder bearing seat. Each bearing should be seated in place and able to rotate freely.

Pre-install four M3×10 screws on the lifting gear and insert the **12×25 mm shaft** from the right side. Turn the gear so that the tip of the screw is aligned with the hole of the servo output plate, and then tighten it from the side operation window.


```{figure} _static/media/assembly/shoulder-bearing-kit.jpg
:alt: Shoulder housings and rail bearings
:width: 560px

Shoulder housings and rail bearings
```

```{figure} _static/media/assembly/shoulder-bearing-install.jpg
:alt: Guide rail bearing press-in position
:width: 560px

Guide rail bearing press-in position
```

```{figure} _static/media/assembly/lift-gear-hardware.jpg
:alt: Lifting gears and fasteners
:width: 560px

Lifting gears and fasteners
```

```{figure} _static/media/assembly/lift-gear-on-servo.jpg
:alt: The lifting gear cooperates with the servo output plate
:width: 560px

The lifting gear cooperates with the servo output plate
```

```{figure} _static/media/assembly/lift-axis-shaft.jpg
:alt: Lift shaft installation position
:width: 560px

Lift shaft installation position
```

Glue the shoulder T-frame and allow it to fully solidify before carrying the robotic arm. Slide the T frame into the column guide rail and confirm that the movement is smooth and there is no jamming; if it is jammed, first check the support residue, glue overflow, and the bearing position and structural fit.


```{figure} _static/media/assembly/shoulder-t-frame.jpg
:alt: Shoulder T-frame construction
:width: 560px

Shoulder T-frame construction
```

```{figure} _static/media/assembly/shoulder-block-on-tower.jpg
:alt: Shoulder lift blocks mounted to column rails
:width: 560px

Shoulder lift blocks mounted to column rails
```

## 6. Install the camera

The second-generation hardware configuration includes five viewing angles: forward, backward, chest, left wrist, and right wrist. First install the two top and one chest parts on the fuselage; the wrist camera is installed along with the robotic arm.

### Two cameras on top

Remove the camera back cover, place the printing bracket/cover between the camera body and the back cover, and secure each with two **M2×12** screws. Record which one is forward and which one is backward, which will be used for software mapping later.


```{figure} _static/media/assembly/top-camera-parts.jpg
:alt: Top camera mount parts
:width: 560px

Top camera mount parts
```

```{figure} _static/media/assembly/top-camera-back-cover.jpg
:alt: Top camera back cover installation method
:width: 560px

Top camera back cover installation method
```

```{figure} _static/media/assembly/top-camera-mount-installed.jpg
:alt: Installed top camera mount
:width: 560px

Installed top camera mount
```

### chest camera

The chest camera uses the same back cover fixing method and is installed on the front bracket. Check that the lens is not obscured by structural parts or cables.


```{figure} _static/media/assembly/chest-camera-parts.jpg
:alt: Chest camera with stand
:width: 560px

Chest camera with stand
```

```{figure} _static/media/assembly/chest-camera-back-cover.jpg
:alt: Chest camera back cover installation method
:width: 560px

Chest camera back cover installation method
```

```{figure} _static/media/assembly/chest-camera-installed.jpg
:alt: Chest camera installation location
:width: 560px

Chest camera installation location
```

## 7. Install the follower arm and organize the wiring harness

Fix the left and right follower arms to both sides of the shoulder T-frame respectively, using the corresponding long M3 hexagon socket screws and M3 nuts. Check the left and right positions first, and then tighten gradually.


```{figure} _static/media/assembly/follower-arms-mounted.jpg
:alt: Shoulder T frame and robot arm installation area
:width: 560px

Shoulder T frame and robot arm installation area
```

```{figure} _static/media/assembly/follower-arm-fasteners.jpg
:alt: Robotic arm mounting fasteners
:width: 560px

Robotic arm mounting fasteners
```

```{figure} _static/media/assembly/tower-cable-port.jpg
:alt: Column wiring hole
:width: 560px

Column wiring hole
```

```{figure} _static/media/assembly/arm-camera-cables-routed.jpg
:alt: The robotic arm and camera lines pass through the column
:width: 560px

The robotic arm and camera lines pass through the column
```

Connect the three-pin wire of the **ID 11 elevator servo to the left arm servo drive board**. Check the cable length allowance at the highest and lowest positions of the shoulder, and do not let the plug take the strain on the cable.

| Wiring harness | Contains lines |
| --- | --- |
| left side | Left arm power supply, left arm Type-C, left wrist camera USB, chest camera USB, elevator servo cable |
| right side | Right arm power supply, right arm Type-C, right wrist camera USB |

After threading the cable, put on the protective cable cover to leave space for connector inspection and replacement.


```{figure} _static/media/assembly/left-cable-bundle.jpg
:alt: Left harness
:width: 560px

Left harness
```

```{figure} _static/media/assembly/right-cable-bundle.jpg
:alt: Right harness
:width: 560px

Right harness
```

```{figure} _static/media/assembly/cable-sleeves-installed.jpg
:alt: Wiring harness with protective cover installed
:width: 560px

Wiring harness with protective cover installed
```

## 8. Install display, computing and power supply modules

The display is fixed to the printing bracket using four **M3×6** screws, then slid into the dovetail groove on the rear of the fuselage to connect the short Micro HDMI cable and Type-C power supply cable. The display model and counterweight quality are not fully listed in the original BOM, please check with your own configuration.


```{figure} _static/media/assembly/display-bracket-parts.jpg
:alt: Display and printing bracket
:width: 560px

Display and printing bracket
```

```{figure} _static/media/assembly/display-mounted.jpg
:alt: The display is mounted in the rear dovetail groove
:width: 560px

The display is mounted in the rear dovetail groove
```

```{figure} _static/media/assembly/compute-power-rear-bay.jpg
:alt: Raspberry Pi, buck module, battery and counterweight layout in the rear space
:width: 560px

Raspberry Pi, buck module, battery and counterweight layout in the rear space
```

Install the Raspberry Pi 5, buck module, battery and counterweight in the rear support. The original assembly diagram uses the following power supply shunt:

| path | Connection method |
| --- | --- |
| double follower arm | Battery 1 → One-to-two power cord → Left and right arm DC lines |
| Computing end | Battery 2 → Buck module → Raspberry Pi Type-C power port |

Before powering on, check the voltage, polarity and connection position according to the component identification, and then power on after completing the wiring. The leader arm is on the PC side and uses its own power supply configuration.


```{figure} _static/media/assembly/power-wiring.jpg
:alt: Second generation robot power supply connection diagram
:width: 560px

Second generation robot power supply connection diagram
```

## 9. Module inspection

The first robot inspection uses the Host and keyboard client that matches the second-generation model. On Pi:

```bash
python -m lerobot.robots.alohamini.alohamini_host \
  --robot_model alohamini2 \
  --no_follower
```

On PC:

```bash
python examples/alohamini/teleoperate_bi.py \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2 \
  --no_leader
```

This step requires first completing the subsequent [Software installation](software.md) and [Device configuration](configuration.md). First use short, one-way input to check the chassis, and then use U/J to check the lifting. For complete keys, see [Teleoperation](teleoperation.md).

The original assembly guide also references `examples/debug/wheels.py` and `axis.py`. Currently, these independent scripts retain their own servo models and geometric constants. In particular, the lifting script defaults to STS3215, while the second generation uses STS3095; it must be checked and adapted before running directly. For details, see [Debugging and troubleshooting](troubleshooting.md).

The inspection results should include: no interference in the movement of the wheel set, no jamming in lifting and lowering, no pulling on the wiring harness, reliable fixation of the left and right arms, camera recognition, and stable power supply connection. If an exception is found, return to the corresponding assembly step before entering the next stage.

## Next step: Configuration and calibration

Complete [Device configuration](configuration.md) → [Arm calibration](calibration.md) → [Teleoperation](teleoperation.md) in sequence. After the hardware is installed, you still need the correct model, serial port, and calibration data, and you cannot jump directly to policy execution.
