# AlohaMini

```{raw} html
<div class="am-project-links" aria-label="Project resources">
<a href="https://github.com/liyiteng/AlohaMini" aria-label="GitHub: AlohaMini project"><img src="_static/external-images/551432bacb6b817efe56.svg" alt="GitHub AlohaMini" height="24"></a>
<a href="https://github.com/liyiteng/AlohaMini/stargazers" aria-label="Check out AlohaMini’s GitHub Stars"><img src="_static/external-images/889a2f18c066ae68827c.svg" alt="GitHub Stars" height="24"></a>
<a href="https://x.com/liyitengx" aria-label="Follow @liyitengx on X"><img src="_static/external-images/08ffe2473ce53b7e3838.svg" alt="Follow @liyitengx" height="24"></a>
<a href="https://github.com/liyiteng/AlohaMini/blob/main/LICENSE" aria-label="Apache 2.0 Open Source License"><img src="_static/external-images/96ae2a5e24552c3ad0ae.svg" alt="License Apache 2.0" height="24"></a>
<a href="https://discord.gg/CacMUBaFgJ" aria-label="Join the AlohaMini Discord community"><img src="_static/external-images/5f408227afa1a4f9eae3.svg" alt="Discord Join Chat" height="24"></a>
</div>
<figure class="am-hero"><img src="_static/media/assembled2.png" width="1344" height="768" alt="AlohaMini is a first-generation white double-arm mobile robot equipped with lifting columns and wheeled chassis." fetchpriority="high"><figcaption>AlohaMini 1. The second generation uses AM-ARM200 arms and a reinforced mobile chassis.</figcaption></figure>
```

## Introduction

**AlohaMini is an open-source mobile robot with two arms, built for embodied AI research and education.**

Build your robot, teleoperate it, collect demonstrations, train a policy and deploy it on hardware. Public CAD models, print files and software source code support both assembly and further development.

Based on the [LeRobot](https://github.com/huggingface/lerobot) software ecosystem, it combines dual-arm operation, omnidirectional movement and electric lifting.

```{raw} html
<div class="am-actions"><a class="am-button primary" href="quickstart.html">Get started <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a><a class="am-text-link" href="specifications.html">Models and specifications</a></div>
```

## Choose your model

Choose the guide that matches your robot to check its hardware and configure the software.

```{raw} html
<div class="am-paths am-models" aria-label="Select tutorials by robot model">
<a class="am-path" href="alohamini2.html"><span class="am-model-label">Standard · Build it yourself</span><strong>AlohaMini 2 <span aria-hidden="true">↗</span></strong><p>3D printed chassis · STS3215 wheel servo<br>From parts and assembly to calibration, teleoperation and your first recording.</p><span class="am-model-entry">AlohaMini 2 guide →</span></a>
<a class="am-path" href="alohamini2pro.html"><span class="am-model-label">Pro · Metal reinforced chassis</span><strong>AlohaMini 2 Pro <span aria-hidden="true">↗</span></strong><p>HD follower arm configuration · STS3250 wheel servo<br>Check your Pro hardware and use the matching setup commands.</p><span class="am-model-entry">AlohaMini 2 Pro guide →</span></a>
</div>
```

## Meet the AlohaMini 2

AlohaMini 2 combines two arms, an omnidirectional base and a powered lift. Build it using the public CAD models and print files, then control it with software based on LeRobot.

```{raw} html
<div class="am-specs"><div class="am-spec"><strong>6+1 <small>DoF</small></strong><span>Degrees of freedom per arm</span></div><div class="am-spec"><strong>52 <small>cm</small></strong><span>Robotic arm reach</span></div><div class="am-spec"><strong>1 <small>kg</small></strong><span>Payload per arm</span></div><div class="am-spec"><strong>5 <small>views</small></strong><span>Camera views</span></div></div>
<p class="am-spec-note">Parameters are from the AlohaMini 2 project description.<a href="specifications.html">View model comparison and complete parameters</a></p>
```

## Start here

Follow the guides below to build and operate your first AlohaMini.

```{raw} html
<div class="am-paths">
<a class="am-path" href="assembly.html"><strong>Hardware assembly<span aria-hidden="true">↗</span></strong><p>Material procurement, 3D printing, and illustrated assembly guides for the chassis and arms.</p></a>
<a class="am-path" href="software.html"><strong>Software installation and operation<span aria-hidden="true">↗</span></strong><p>Install the software environment and complete device configuration, calibration and teleoperation.</p></a>
<a class="am-path" href="learning.html"><strong>Data collection and training<span aria-hidden="true">↗</span></strong><p>Record the task demonstration and enter the policy training and hardware evaluation process.</p></a>
<a class="am-path" href="simulation.html"><strong>Simulation resources<span aria-hidden="true">↗</span></strong><p>URDF, RViz and Gazebo resources for AlohaMini 1.</p></a>
</div>
```

## Tutorial roadmap

The [User manual](official-manual.md) covers the complete journey from unboxing to training. Start with [Unboxing and first power-on](unboxing.md) for an assembled robot, or use [Robot troubleshooting](support.md) when something goes wrong.

Begin with the [AlohaMini 2](alohamini2.md) or [2 Pro](alohamini2pro.md) guide. The topic guides below explain each stage in detail. Parts, printing and assembly instructions cover the standard 2; Pro users should first check [Pro hardware](hardware-pro.md).

| stage | Tutorial | The result after completion |
| --- | --- | --- |
| 01 · Prepare hardware | [Bill of materials](bom.md) , [Print guide](printing.md) | Check modules, quantities, printouts and procurement scope |
| 02 · Complete assembly | [Assembly](assembly.md) | Complete the chassis, columns, shoulders, cameras and wiring according to the photos |
| 03 · Connecting devices | [Software installation](software.md), [Device configuration](configuration.md) | Both ends of the environment are available, and the left and right ports are clearly mapped to the camera. |
| 04 · Manual control | [Calibration](calibration.md) , [Teleoperation](teleoperation.md) | The leader and follower arms follows normally, and the chassis and lifting are controllable. |
| 05 · Record tasks | [Data collection and inspection](learning.md) | Save the task demonstration and complete offline review |
| 06 · Learning and Verification | [Policy training](training.md), [Hardware evaluation](evaluation.md) | Train ACT and record real machine task results |

### How the software connects the entire robot

The robot side Host is responsible for the follower arm, chassis, lifting and camera; the PC side is connected to the leader arm to run teleoperation, recording and policy evaluation. Training reads the collected data and can be completed on a stand-alone computing device.

The first generation uses SO-ARM100 / SO-ARM101, and the second generation and Pro use the AM-ARM200 series. The hardware profiles and data dimensions of different models need to be configured separately. The commands in the tutorial will clearly indicate the applicable models.

### In-depth learning and problem solving

- There is only one set of leader and follower arms: start with the [AM-ARM200 single arm tutorial](single-arm.md).
- Want to understand control frequency, feedback and protection: View [Operating mechanism](runtime.md).
- Prepare to connect to OpenPI: Read the data mapping and version conditions of [Pi 0.5 Special Topic](pi05.md).
- For missing devices, camera frames or failed recordings, follow [Debugging and troubleshooting](troubleshooting.md).
- For quick access to commands, use the [Command reference](commands.md).

## Complete tutorials and advanced materials

- [Tutorial library](tutorial-library.md): View hardware, software and development tutorials by topic.
- [policy and Training](policies.md): AM-ACT, SmolVLA, Pi0.5, GR00T and other policies.
- [Scene reconstruction from video](video2sim.md) → [Simulation data conversion](sim-data.md): Understand the environment and data interface.
- [Docker](docker.md), [Development and extensions](development.md), [Servo and performance debugging](debug-tools.md).
- [First-generation BOM and assembly](legacy-hardware.md): first generation BOM, assembly process and complete pictures and texts.

## Project progress

```{raw} html
<div class="am-update"><time datetime="2026-06-06">2026.06.06</time><p><strong>AlohaMini 2 released</strong><br>Upgrade the AM-ARM200 robotic arm, lifting mechanism and mobile chassis to adapt to consumer-grade 3D printers.</p></div>
<div class="am-update"><time datetime="2026-02-26">2026.02.26</time><p><strong>Pi 0.5 Tuning and Deployment Guide</strong><br>View the OpenPI-based training and deployment process in the project example.</p></div>
```

## Build together

AlohaMini was created by **Li Yiteng** and **Wu Zhiyong**. Welcome to share your assembly experience, experimental results, or help improve the documentation.

```{raw} html
<div class="am-resource-row"><a href="community.html">Participate in projects</a><a href="https://discord.gg/CacMUBaFgJ">Join Discord</a><a href="https://github.com/liyiteng/AlohaMini/issues">Feedback question</a></div>
```


```{toctree}
:hidden:
:maxdepth: 2
:caption: Get started

quickstart
specifications
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Model tutorials

alohamini2
alohamini2pro
hardware-pro
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Build AlohaMini 2

bom
printing
assembly
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Setup and operation

software
configuration
calibration
teleoperation
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Data and learning

learning
training
evaluation
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Advanced tutorials

single-arm
pi05
simulation
runtime
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Reference and support

commands
troubleshooting
legacy
community
```

```{toctree}
:hidden:
:maxdepth: 1
:caption: Complete tutorials and advanced materials

legacy-hardware
debug-tools
policies
docker
development
video2sim
sim-data
tutorial-library
```

```{toctree}
:hidden:
:maxdepth: 1
:caption: Official delivery tutorial

official-manual
```
