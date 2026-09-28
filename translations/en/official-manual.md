# User manual

Starting from receiving the robot, complete the power supply, software connection, teleoperation, and then enter the data collection and policy training. Follow the directions below to choose the tutorial that suits your current progress.

## First time use, start here

```{raw} html
<div class="am-paths">
<a class="am-path" href="unboxing.html"><span class="am-model-label">01 · Received the robot</span><strong>Unboxing and first power on ↗</strong><p>Check the battery and power supply interface, and connect the Raspberry Pi, leader arm and network.</p></a>
<a class="am-path" href="quickstart.html"><span class="am-model-label">02 · Select model</span><strong>Enter 2 / 2 Pro Tutorial ↗</strong><p>Complete the environment, equipment configuration, calibration and teleoperation according to the actual model.</p></a>
<a class="am-path" href="learning.html"><span class="am-model-label">03 · Complete a task</span><strong>Collection, training and evaluation ↗</strong><p>Check out a demo first, then train the model and conduct a short real-device test.</p></a>
<a class="am-path" href="support.html"><span class="am-model-label">04 · Encountering a problem</span><strong>Troubleshooting the whole machine ↗</strong><p>Check each item by power supply, serial port, calibration, camera and network.</p></a>
</div>
```

## Read at your own pace

| current situation | reading order |
| --- | --- |
| Just received the assembled 2 / 2 Pro | [Unboxing illustration](unboxing.md) → [Select model](quickstart.md) → [Device configuration](configuration.md) |
| Never come into contact with LeRobot | [Developer Manual](yuque/developer-manual.md) → [Software installation](software.md) → [Calibration](calibration.md) |
| Already have experience with LeRobot, using 2 Pro | [Quick Start with Pro Delivery](yuque/pro-quickstart.md) → [2 Pro complete process](alohamini2pro.md) |
| Build your own standard 2 | [Bill of materials](bom.md) → [Print](printing.md) → [Assemble](assembly.md) → [2 Getting Started](alohamini2.md) |
| Can be operated remotely and ready for training | [Data collection and review](learning.md) → [ACT / AM-ACT Training](training.md) → [Hardware evaluation](evaluation.md) |
| Need debugging or extension | [Robot troubleshooting](support.md) → [Debugging tools](debug-tools.md) → [Advanced reference](yuque/advanced.md) |

## Complete delivery tutorial

The user name, device serial number, IP, data directory and checkpoint path in the tutorial are examples. Please replace them with local values before operation.

| Tutorial | Content and scope of application |
| --- | --- |
| [2/2 Pro Unboxing Guide](yuque/unboxing.md) | Assembled battery, power supply board and teleoperation arm wiring diagram |
| [2 Pro Quick Start](yuque/pro-quickstart.md) | From SSH, port binding to acquisition, ACT/AM-ACT and local inference |
| [Developer Manual v1.3](yuque/developer-manual.md) | Structure, environment, single arm, chassis, lifting and camera instructions for novices |
| [FAQ](yuque/faq.md) | Update code and network access |
| [Exception handling](yuque/troubleshooting.md) | Error reports, causes and processing steps of E001–E004 |
| [Advanced reference](yuque/advanced.md) | Serial port confirmation and calibration file location |
| [Optional accessories](yuque/accessories.md) | Accessories specifications and purchase entrance |
| [Information package](yuque/resources.md) | Policy PDF, first-generation simulation and second-generation SLAM extension entrance |

## Products, Education & Videos

- [Chinese product description](yuque/product.md) · [English product overview](yuque/product-en.md)
- [Embodied intelligent education solutions](yuque/education.md) · [K12 product description](yuque/education-k12.md)
- [Demo video collection](yuque/videos.md)

Please confirm the device model, package configuration and installed software version before operation. The schedule of courses and competitions shall be subject to the latest notice of the corresponding activities.

## How to deal with version differences

1. The model of **is the same as**: 2 uses `alohamini2`, 2 Pro uses `alohamini2pro`; the Raspberry Pi Host and PC must match.
2. The **robot arm numbers are divided into generations**: SO-ARM is 1–6; AM-ARM is 1–7. The overall chassis is 8–10 and the lift is 11.
3. **camera names are consistent with**: some delivery examples use `head_top`, and other software configurations use `forward`. Collection, conversion, training and inference should be configured according to the actual data characteristics, and you cannot just change the display name.
4. **debugs chassis** according to model: The default servo configuration of the old version `wheels.py` / `axis.py` is not suitable for direct application on 2 Pro, see [Debugging tools](debug-tools.md).
5. **save changes first and then update**: Save the local configuration before updating the software, and use [Update steps](support.md#更新软件与网络访问).

[Browse more special tutorials](tutorial-library.md)

```{toctree}
:hidden:
:maxdepth: 1

unboxing
support
yuque/unboxing
yuque/pro-quickstart
yuque/developer-manual
yuque/faq
yuque/troubleshooting
yuque/advanced
yuque/resources
yuque/accessories
yuque/product
yuque/product-en
yuque/education
yuque/education-k12
yuque/videos
```
