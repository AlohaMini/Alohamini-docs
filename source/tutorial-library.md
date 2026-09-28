# 教程资料库

这里汇总 GitHub 硬件、软件教程与语雀官方使用手册。首次操作机器人，建议先进入 [官方使用手册](official-manual.md)，按开箱、机型、操作和训练顺序阅读。

本次收录 **127 篇 GitHub 独立原文 + 13 篇语雀文档**；语雀图片已保存到本地，PDF 与外部视频的可用范围见 [收录说明](official-manual.md#本次收录范围)。

## 官方交付教程

[开箱图解](unboxing.md) · [Pro 交付快速入门](yuque/pro-quickstart.md) · [开发者手册](yuque/developer-manual.md) · [整机排错](support.md) · [视频合集](yuque/videos.md)

## 按主题浏览

[整机与硬件](library-alohamini.md) · [策略与模型](library-policies.md) · [数据集与编码](library-data.md) · [仿真与基准](library-simulation.md) · [开发与扩展](library-development.md) · [环境与训练工具](library-environment.md) · [其他硬件与遥操作](library-hardware.md)

## 先按目标进入

| 你要完成的工作 | 中文教程 | 完整原始资料 |
|---|---|---|
| 组装与运行 AlohaMini 2 / 2 Pro | [选择机型](quickstart.md) | [整机与硬件](library-alohamini.md) |
| 组装一代机器人 | [一代物料与装配](legacy-hardware.md) | [一代图文装配全文](upstream/hardware--alohamini1-docs-hardware_assembly.md) |
| 单臂训练与评估 | [AM-ARM200](single-arm.md) | [单臂完整工作流](upstream/software--docs-alohamini-am-arm200.md) |
| 调试舵机与性能 | [调试工具详解](debug-tools.md) | [原始调试命令](upstream/software--examples-debug-readme.md) |
| 微调与部署 OpenPI | [OpenPI 接入](pi05.md) | [完整适配代码与历史命令](upstream/hardware--examples-pi0-5_openpi-readme.md) |
| 从手机视频重建场景 | [video2sim](video2sim.md) | [重建管线全文](upstream/software--alohamini_sim-video2sim-readme.md) |
| 生成与转换仿真数据 | [仿真数据工作流](sim-data.md) | [仿真与技能库](library-simulation.md) |
| 使用 Docker | [Docker 环境](docker.md) | [上游 Docker 全文](upstream/software--docker-readme.md) |
| 学习其他策略与训练方式 | [策略教程导航](policies.md) | [策略原文](library-policies.md) |
| 扩展软件和硬件接口 | [开发指南](development.md) | [开发原文](library-development.md) |

## 收录范围与阅读方式

- **127 篇独立原文**已迁入站内，包含原来的段落、表格、参数与代码，可直接阅读和搜索。
- **26 个符号链接入口**已映射到对应正文，避免同一篇内容重复出现。
- 80 篇 MDX 教程已适配为本站页面；标签页改为依次展示的带标题内容，折叠内容展开保留。
- 中文主线解释操作顺序和机型适用范围；资料库保留原文语言，**原文收录完成不等于全文中文翻译完成，也不等于硬件验证完成**。
- 各原文页提供固定提交来源和未经改写的文件下载，方便核对；装配图、教程插图和动图已保存到本站，Bilibili 视频使用嵌入播放器。
- 仓库治理文件与文档模板不作为操作教程收录。版本与文件对应关系见 [迁移清单](migration-status.md)。

## 使用原文命令前

原文中的用户名、串口、服务器路径和数据集名称多为示例。先确认所在仓库、Python 环境和目标机器人，再替换为自己的值。通用 LeRobot 教程还涵盖 SO-101、其他机器人和仿真环境，不应将这些命令直接当作 AlohaMini 整机参数。

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
migration-status
```
