# AlohaMini 2 Pro Hardware Description

The official [2/2 Pro unboxing wiring photos](unboxing.md) has been added, covering the battery, power board, Raspberry Pi and leader arm connections of the delivered robot; the component-level Pro assembly information is still explained within the scope below.

This page is used to check the hardware and software configuration of **AlohaMini 2 Pro**. If you already have a complete robot, check the table below and enter the [2 Pro Getting Started Tutorial](alohamini2pro.md).

## Confirmed configuration

| part | Pro configuration | Impact on software |
| --- | --- | --- |
| Chassis | Metal reinforced chassis | Check the assembly based on the actual Pro object and kit information |
| Chassis wheel servo | STS3250 × 3 | Host uses `alohamini2pro` |
| follower arm | `am-follower-6dof-hd` | Selected by Pro machine profile |
| elevator servo | STS3095 | The first generation STS3215 lifting configuration should not be applied |
| Lifting transmission parameters | 131 mm/rev | Software conversion parameters, not stroke or speed |
| PC leader arm | `am-leader-6dof` | Same as standard 2; do not fill in the slave HD profile |
| state/action interface | 18 dimensions | Still need to check feature names, order and units |

The "STS3250 servo solution" in the product description cannot be understood to mean that all joints use STS3250. Different parts should be checked separately. STS3095 is still used for lifting.

## Where does the current hardware information cover?

As of **2026-09-28**, the checked hardware warehouse `AlohaMini2/docs` provides `BOM.md`, `print_guide.md` and `assembly_guide.md`. No independent Pro BOM, metal chassis assembly drawing or Pro-exclusive printing list was found this time.

| information | How this site handles |
| --- | --- |
| Standard 2 Materials and Purchase Quantities | Placed in [Standard 2 Bill of Materials](bom.md), not as Pro’s purchase list |
| Standard 2 Printing Files and Slicing Recommendations | Placed in [Standard 2 Printing Guide](printing.md) |
| Standard 2 graphic assembly steps | Placed in [Standard 2 Hardware Assembly](assembly.md) |
| Pro software configuration and complete workflow | It has been organized according to official Profiles into [Pro Getting Started Tutorial](alohamini2pro.md) |
| Pro independent assembly information | The current version does not provide part-level assembly processes |

Therefore, this page does not provide unconfirmed Pro fastener quantities, hardware dimensions, print alternatives, or load values. When preparing to build the Pro yourself, obtain the assembly and wiring instructions that match your kit.

## Already have a Pro machine: Check before connecting to the software

1. **Check the robot and actuator**: record the machine model, check the wheel servo and elevator servo labels, and confirm that the follower arm belongs to the corresponding HD configuration.
2. **checks the control board and left and right ports**: According to the [Device configuration](configuration.md) identifies the left and right follower arm buses and the left and right leader arms, regardless of the USB insertion sequence.
3. **Check the power supply and wiring**: Confirm the power supply, interface and cable fixation of each device according to the actual kit instructions; the software profile will not replace the hardware wiring check.
4. **Check camera**: Confirm the name and screen one by one. The default software enables both forward and right wrist channels. The actual enabled range is subject to configuration.
5. **is ready to calibrate**: use `alohamini2pro` on the Pi and `am-leader-6dof` on the PC leader arm; do not apply the calibration file of another machine.
6. **sub-module verification**: first check the robotic arm, then check the chassis and lifting, and finally enter complete teleoperation and acquisition.

[Continue: AlohaMini 2 Pro Getting Started Tutorial →](alohamini2pro.md)

## Source

- [Hardware Warehouse Product Series Description](https://github.com/liyiteng/AlohaMini/blob/17c6a98d79881a45ab869c1f392ed89c0723a298/README.md#product-line)
- [Hardware tutorial directory for this review](https://github.com/liyiteng/AlohaMini/tree/17c6a98d79881a45ab869c1f392ed89c0723a298/AlohaMini2/docs)
- [Software and Hardware Profiles](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/alohamini/profiles.md)
