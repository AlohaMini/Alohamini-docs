# 教程资料库

查阅 AlohaMini 的硬件、软件、训练与开发教程。首次使用请从 [官方使用手册](official-manual.md) 开始，依次完成开箱、配置、操作和训练。

## 官方交付教程

[开箱图解](unboxing.md) · [Pro 交付快速入门](yuque/pro-quickstart.md) · [开发者手册](yuque/developer-manual.md) · [整机排错](support.md) · [视频合集](yuque/videos.md)

## 按主题浏览

[整机与硬件](library-alohamini.md) · [策略与模型](library-policies.md) · [数据集与编码](library-data.md) · [仿真与基准](library-simulation.md) · [开发与扩展](library-development.md) · [环境与训练工具](library-environment.md) · [其他硬件与遥操作](library-hardware.md)

## 先按目标进入

| 你要完成的工作 | 中文教程 | 专题参考 |
|---|---|---|
| 组装与运行 AlohaMini 2 / 2 Pro | [选择机型](quickstart.md) | [整机与硬件](library-alohamini.md) |
| 组装一代机器人 | [一代物料与装配](legacy-hardware.md) | [一代图文装配全文](upstream/hardware--alohamini1-docs-hardware_assembly.md) |
| 单臂训练与评估 | [AM-ARM200](single-arm.md) | [单臂完整工作流](upstream/software--docs-alohamini-am-arm200.md) |
| 调试舵机与性能 | [调试工具详解](debug-tools.md) | [调试命令](upstream/software--examples-debug-readme.md) |
| 微调与部署 OpenPI | [OpenPI 接入](pi05.md) | [完整适配代码与历史命令](upstream/hardware--examples-pi0-5_openpi-readme.md) |
| 从手机视频重建场景 | [video2sim](video2sim.md) | [重建管线全文](upstream/software--alohamini_sim-video2sim-readme.md) |
| 生成与转换仿真数据 | [仿真数据工作流](sim-data.md) | [仿真与技能库](library-simulation.md) |
| 使用 Docker | [Docker 环境](docker.md) | [Docker 参考](upstream/software--docker-readme.md) |
| 学习其他策略与训练方式 | [策略教程导航](policies.md) | [策略参考](library-policies.md) |
| 扩展软件和硬件接口 | [开发指南](development.md) | [开发参考](library-development.md) |

## 使用说明

先按机型完成中文入门教程，再查阅专题参考。部分 LeRobot 专题使用英文，涵盖 SO-101、其他机器人与仿真环境；操作前应确认适用硬件，并替换示例中的用户名、串口、服务器路径和数据集名称。

当前特别需要注意：OpenPI 历史部署接口存在版本差异；仿真桥接器当前输出 16 维数据，不能直接替代 2 / 2 Pro 的 18 维整机数据。详见相应中文教程。

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
