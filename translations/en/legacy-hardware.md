# AlohaMini 1 Materials and Assembly

This page corresponds to the **generation SO-ARM100 / SO-ARM101 dual-arm robot**. Second generation users please use [AlohaMini 2 Bill of Materials](bom.md) and [Second generation assembly](assembly.md).

## 1. Check the procurement scope first

The first generation is prepared separately according to the mobile chassis, computing and power supply, double follower arms, and double leader arms. The Host/Client expressions in the original BOM are used interchangeably. This manual uses the **Pi robot terminal/PC operating terminal** uniformly, and check according to the actual connection relationship of the equipment.

| module | Main materials | Quantity and description |
| --- | --- | --- |
| Chassis and lifting | STS3215-C018 12V, 1/345 servo | 4 pieces, used for tricycle and lifting |
| Omni wheel | Approx. 100 mm / 4 inches | 3 pieces |
| chassis camera | 720p、2.4 mm、36×36 mm | 3 pieces |
| Lift bearing | 4×13×5 mm | 8 |
| Optional wheel bearings | 12×18×4 mm | 3 |
| double follower arm | 12V, 1/345 STS3215 servo | 12 pieces, plus two control boards and two wrist cameras |
| Double leader arm | The original BOM is simplified to 1/147 servo | 12 pieces, need to confirm the actual rated voltage and robot arm version |
| standalone module | Pi 5, 12V → 5V/5A buck module, screen | Optional according to whether to disconnect from PC wired control |

The voltages marked on the leader arm servo and the battery in the original BOM are not consistent, and the power supply cannot be directly determined based on this. Confirm the wiring according to the purchase kit, servo nameplate and allowable voltage of the control board.

For the complete quantity of fasteners, wire lengths and purchasing links, see [Generation BOM](upstream/hardware--alohamini1-docs-bom.md). The original price is a historical record, please recheck the specifications and quantity before purchasing.

## 2. Preparation of printouts

The chassis print size recorded in the source material is at least approximately **385 × 345 × 64 mm**. Confirm the model bounding box and the available space on the printer. The printing requirements of the second-generation segmented chassis cannot be used instead.

| Print file group | Quantity |
| --- | --- |
| `OB_Chassis_Bearing_Cover` | 3 |
| `OB_Chassis_Servo_Mount` | 3 |
| `OB_Chassis_Side_Panel` | 3 |
| `OB_Chassis_Wheel_Axle_Connector` | 3 |
| `OB_Chassis_Wheel_Guard` | 3 |
| `OB_Top_Camera_Back_Cover` | 2 |
| `OB_Chassis_Shaft_Sleeve_12_24` | 3 |
| `O_Chassis_Dowel_Pin_12_37` | 3 |
| Other chassis documents | 1 each from original list, verified as fully assembled |
| Two follower arms `D_*` / `F_*` | 2 copies of each document |
| Two leader arms `D_*` / `L_*` | 2 copies of each document |

The chassis and robotic arm use their own printing lists to avoid mixing "one copy each of other files" in different directories for calculation.

## 3. Servo number and bus

1. Only connect one servo to be set at a time, and identify the model and serial port in the official debugging tool.
2. The chassis-related IDs are 8, 9, 10, and 11; the actual wheel positions are checked according to the [Generation assembly photos](upstream/hardware--alohamini1-docs-hardware_assembly.md).
3. Use 20 cm servo cable to connect 8, 9, and 10, and use 90 cm cable to connect 10 and 11.
4. After installation is complete, check the ID, connection sequence, movement direction and cable margin.

The wheel position table and lifting STS3095 configuration of the second generation cannot be directly applied to the first generation.

## 4. Assemble by module

The complete photo has been retained in the full text of the [The full text of a generation of graphic and text assembly](upstream/hardware--alohamini1-docs-hardware_assembly.md). Complete while looking at the photos in the following order:

1. **servo bracket**: Install the heat-set inserts, fix the servo, and install the wheel shaft connector; if the fit is too tight, check the printing tolerance first.
2. **Chassis wheel set**: Fix the bracket to the bottom plate and install the omnidirectional wheel; confirm the difference between the M3×14 assembly steps and the BOM M3×12 table items according to the actual object.
3. **optional wheel shaft support**: Install the bearing, pin and sleeve, and then fix the bearing cap.
4. **side panels and columns**: Install the inserts, assemble the four main sections of the columns, and proceed with subsequent assembly after confirming that they are vertical and firm.
5. **lifting mechanism**: Assemble the shaft, gear, servo bracket and T-shaped connector, and check manually for no interference.
6. **camera and display screen**: Install the top, rear and front cameras, use internal wire troughs, and fix the display screen.
7. **robotic arm**: Complete the leader and follower arms according to the matching SO-100 / SO-101 tutorial respectively, and fix the double follower arms to both sides of the T-shaped bracket.
8. **power supply and control board**: Confirm the actual connections of the chassis bus, left arm control board, Pi buck module and arm branch wires according to the original diagram.
9. **wiring and inspection**: Check the full lifting stroke, robot arm movement range, joint stress and power supply specifications before entering calibration.

## 5. leader and follower arms assembly

- [SO-100 tutorial full text](upstream/software--docs-source-so100.md)
- [SO-101 Tutorial Full Text](upstream/software--docs-source-so101.md)
- [First-generation robotic arm resource description](upstream/hardware--alohamini1-hardware-arms-readme.md)

Different joints of the SO-101 leader arm may use different reduction ratios; the simplified scheme of the first-generation BOM and the SO-101 standard scheme need to be checked separately, and the same set of calibration assumptions cannot be used after mixing.

## 6. Software process after assembly

Use the [First generation software description](legacy.md). First complete device discovery, calibration and single module motion inspection, and then collect 16-dimensional robot data.

The full text of the [Full text of the entrance to a generation of old software](upstream/hardware--alohamini1-docs-software_setup.md) has been retained; the external entrance and historical commands need to correspond to the current unified software version.
