# Quickstart

If your robot arrived assembled, complete [Unboxing and first power-on](unboxing.md) first. The [User manual](official-manual.md) walks through the full setup process.

Choose your robot model before running commands. Both models use the same software repository, but their follower-arm and chassis configurations differ. Use the matching model parameters on both the Raspberry Pi and the PC.

```{raw} html
<div class="am-paths am-models" aria-label="Select tutorials by robot model">
<a class="am-path" href="alohamini2.html"><span class="am-model-label">Standard · Build it yourself</span><strong>AlohaMini 2 <span aria-hidden="true">↗</span></strong><p>3D printed chassis · STS3215 wheel servo<br>From parts and assembly to calibration, teleoperation and your first recording.</p><span class="am-model-entry">AlohaMini 2 guide →</span></a>
<a class="am-path" href="alohamini2pro.html"><span class="am-model-label">Pro · Metal reinforced chassis</span><strong>AlohaMini 2 Pro <span aria-hidden="true">↗</span></strong><p>HD follower arm configuration · STS3250 wheel servo<br>Check your Pro hardware and use the matching setup commands.</p><span class="am-model-entry">AlohaMini 2 Pro guide →</span></a>
</div>
```

## Which model do you have?

| Check | AlohaMini 2 | AlohaMini 2 Pro |
|---|---|---|
| Chassis | 3D printed | Reinforced metal |
| Wheel servos | STS3215 × 3 | STS3250 × 3 |
| Follower-arm profile | `am-follower-6dof` | `am-follower-6dof-hd` |
| Pi / PC robot model | `alohamini2` | `alohamini2pro` |
| PC leader-arm profile | `am-leader-6dof` | `am-leader-6dof` |
| Hardware guide | [BOM](bom.md), [printing](printing.md), [assembly](assembly.md) | [Pro hardware](hardware-pro.md) |
| Getting started | [AlohaMini 2](alohamini2.md) | [AlohaMini 2 Pro](alohamini2pro.md) |

Check the actual model, servo labels and kit configuration. Modified robots may not match a preset exactly: verify the [device configuration](configuration.md) rather than relying on appearance. See [Models and specifications](specifications.md) for details.

## Choose your starting point

| Your current setup | Next step |
|---|---|
| Building a standard AlohaMini 2 | [Bill of materials](bom.md) → [3D printing](printing.md) → [Assembly](assembly.md) |
| An assembled 2 / 2 Pro | Follow the matching guide above to install the environment, configure devices and calibrate the arms |
| Teleoperation already works | [Data collection](learning.md) → [Policy training](training.md) → [Hardware evaluation](evaluation.md), using commands for your model |
| AlohaMini 1 | [First-generation guide](legacy.md) |
| One leader/follower arm pair | [AM-ARM200 single-arm guide](single-arm.md) |
| Exploring models and joints | [Simulation and visualization](simulation.md); check which generation each asset supports |

## How to read these tutorials

- **Pi / robot side**: connects to the follower arms, chassis, lift and cameras, and runs the Host service.
- **PC / operator side**: connects to the leader arms and runs teleoperation, recording and evaluation.
- Each model guide includes complete commands. When a shared tutorial shows commands for both models, run only the set that matches your robot.
- Dataset names use `am2_` and `am2pro_` prefixes to distinguish models. A dataset name does not select a hardware configuration.
- Both robots expose an 18-dimensional interface. Matching dimensions alone do not make datasets or policies interchangeable: check feature order, units, calibration, cameras and physical hardware as well.
