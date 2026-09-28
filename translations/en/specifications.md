# Models and specifications

AlohaMini 2 upgrades the robotic arm, lifting mechanism and chassis on the first-generation dual-arm mobile architecture.

## Comparison of two generations of robots

| Project | AlohaMini 1 | AlohaMini 2 |
| --- | --- | --- |
| Robotic arm | SO-ARM100 / SO-ARM101 | AM-ARM200 |
| Degrees of freedom per arm | 5+1 | 6+1 |
| Wingspan | 40 cm | 52 cm |
| Payload per arm | 0.3 kg | 1 kg |
| Maximum load of chassis | 10 kg | 70 kg |
| lifting capacity | 5 kg | 30 kg |
| camera | 5 way | 5 way |
| Printer requirements | Large format FDM, print bed ≥ 380 mm | Bambu P2S-class consumer printer |

The above are nominal parameters in the project README. The specific load capacity is related to assembly, materials and operating conditions.

## AlohaMini 2 and 2 Pro

| Model | servo solution | Chassis | Project positioning |
| --- | --- | --- | --- |
| AlohaMini 2 | STS-3215 and other standard servos | 3D printed chassis | Self-built and developed |
| AlohaMini 2 Pro | STS-3250 industrial grade servo solution | Metal reinforced chassis | More intensive laboratory use |

Enter the [AlohaMini 2 Getting Started Tutorial](alohamini2.md) or the [AlohaMini 2 Pro Getting Started Tutorial](alohamini2pro.md) respectively. The printing and assembly guide is for Standard 2; for Pro confirmed configurations and missing assembly information, see [2 Pro hardware](hardware-pro.md).

## Get design resources

- [Mobile Base 2 Structure File](https://github.com/liyiteng/AlohaMini/tree/main/AlohaMini2/hardware/mobile_base2)
- [AM-ARM200 robotic arm](https://github.com/liyiteng/AM-ARM/tree/main/am-arm200)
- [Project original parameter description](https://github.com/liyiteng/AlohaMini#whats-new-in-alohamini2)


## Software and hardware configuration correspondence table

| `robot_model` | follower arm profile | Chassis wheel servo | elevator servo | Lifting transmission parameters |
| --- | --- | --- | --- | --- |
| `alohamini1` | `so-arm-5dof` | STS3215 × 3 | STS3215 | 84 mm/rev |
| `alohamini2` | `am-follower-6dof` | STS3215 × 3 | STS3095 | 131 mm/rev |
| `alohamini2pro` | `am-follower-6dof-hd` | STS3250 × 3 | STS3095 | 131 mm/rev |

mm/rev in the table is the transmission parameter of the software profile, not the lifting speed or total stroke. The overall machine selection for Pro is completed by `robot_model`, and the AM leader arm on PC still uses `am-leader-6dof`.

## Degrees of freedom and data dimensions

"6+1 degrees of freedom" means six motion joints of a single arm plus a gripper. The data interface of the whole machine also includes chassis and lifting:

| Model | Arm dimensions | Chassis | lifting | Total state/action dimensions |
| --- | ---: | ---: | ---: | ---: |
| generation | 6 × 2 = 12 | 3 | 1 | 16 |
| Second generation/Pro | 7 × 2 = 14 | 3 | 1 | 18 |

The three components of the chassis are `x.vel`, `y.vel`, and `theta.vel`, and `lift_axis.height_mm` is used for lifting. These are control interface dimensions, and they should not all be called rotating joints. In addition to having the same dimensions, the model and data set must also check the field order and units.

## Camera and Observation

The hardware layout includes a total of five cameras including forward, backward, chest, and left and right wrist cameras. The current software enables forward and right wrist viewing by default, and other viewing angles are enabled through configuration. The physical specifications of the camera, the current acquisition resolution, and the model input size are three different concepts. The training input cannot be judged solely by the "720p" of the BOM.

When enabling the camera, first press [Device configuration](configuration.md) to confirm the name and angle of view, and keep the recording and evaluation consistent.

## How to use parameters

Nominal loads describe project design capabilities and do not imply that every material, pose, and printed alternative has been equally validated. When building by yourself, record the replacement of materials, metal parts and actual load; complete the no-load assembly and motion inspection before running with load.

The mechanical arms, lifting transmissions and interfaces of the first generation and the second generation are different. Existing first-generation users cannot obtain second-generation configurations by simply modifying the model string, nor can they directly reuse training checkpoints in different dimensions.
