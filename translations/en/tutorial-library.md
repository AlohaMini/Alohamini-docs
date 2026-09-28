# Tutorial library

Check out AlohaMini's hardware, software, training and development tutorials. For first-time use, please start from the [User manual](official-manual.md) and complete unboxing, configuration, operation and training in sequence.

## Official delivery tutorial

[Unboxing illustration](unboxing.md) · [Quick Start with Pro Delivery](yuque/pro-quickstart.md) · [Developer Manual](yuque/developer-manual.md) · [Robot troubleshooting](support.md) · [Video collection](yuque/videos.md)

## Browse by topic

[Machine and hardware](library-alohamini.md) · [policies and Models](library-policies.md) · [Datasets and Coding](library-data.md) · [Simulation and Benchmarking](library-simulation.md) · [Development and extensions](library-development.md) · [Environment and training tools](library-environment.md) · [Other hardware and teleoperation](library-hardware.md)

## Press the target first to enter

| the work you want to accomplish | Chinese tutorial | Topic reference |
| --- | --- | --- |
| Assembling and running AlohaMini 2 / 2 Pro | [Select model](quickstart.md) | [Machine and hardware](library-alohamini.md) |
| Assembling a new generation of robots | [First-generation BOM and assembly](legacy-hardware.md) | [The full text of the first generation graphics and text assembly](upstream/hardware--alohamini1-docs-hardware_assembly.md) |
| Single Arm Training and Assessment | [AM-ARM200](single-arm.md) | [Complete workflow for one arm](upstream/software--docs-alohamini-am-arm200.md) |
| Debugging servos and performance | [Detailed explanation of debugging tools](debug-tools.md) | [debug command](upstream/software--examples-debug-readme.md) |
| Fine-tuning and deploying OpenPI | [OpenPI access](pi05.md) | [Complete adaptation code and historical commands](upstream/hardware--examples-pi0-5_openpi-readme.md) |
| Reconstruct scene from mobile phone video | [video2sim](video2sim.md) | [Full text of reconstruction pipeline](upstream/software--alohamini_sim-video2sim-readme.md) |
| Generate and convert simulation data | [Simulation data workflow](sim-data.md) | [Simulation and Skills Library](library-simulation.md) |
| Using Docker | [Docker environment](docker.md) | [Docker reference](upstream/software--docker-readme.md) |
| Learn other policies and training methods | [policy Tutorial Navigation](policies.md) | [policy reference](library-policies.md) |
| Extended software and hardware interfaces | [Development Guide](development.md) | [Development reference](library-development.md) |

## Instructions for use

First complete the Chinese introductory tutorial according to the model, and then check the topic reference. Some LeRobot topics are in English, covering SO-101, other robots and simulation environments; you should confirm the applicable hardware before operation and replace the user name, serial port, server path and data set name in the examples.

Special attention needs to be paid at present: there are version differences in the OpenPI historical deployment interface; the simulation bridge currently outputs 16-dimensional data and cannot directly replace the 18-dimensional whole machine data of 2 / 2 Pro. See the corresponding Chinese tutorial for details.

```{toctree}
:hidden:
:maxdepth: 1

library-alohamini
library-policies
library-data
library-simulation
library-development
library-environment
library-hardware
```
