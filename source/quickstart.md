# 快速开始

先选择你的机器人型号，再按对应教程操作。两款共用软件仓库，但从臂与底盘配置不同，Pi 和 PC 必须使用匹配的机型参数。

```{raw} html
<div class="am-paths am-models" aria-label="按机器人型号选择教程">
<a class="am-path" href="alohamini2.html"><span class="am-model-label">标准版 · 自行搭建</span><strong>AlohaMini 2 <span aria-hidden="true">↗</span></strong><p>3D 打印底盘 · STS3215 轮舵机<br>从物料与组装，到校准、遥操作和首条数据。</p><span class="am-model-entry">进入 2 教程 →</span></a>
<a class="am-path" href="alohamini2pro.html"><span class="am-model-label">Pro · 金属强化底盘</span><strong>AlohaMini 2 Pro <span aria-hidden="true">↗</span></strong><p>HD 从臂配置 · STS3250 轮舵机<br>核对 Pro 硬件，按专属命令完成软件入门。</p><span class="am-model-entry">进入 2 Pro 教程 →</span></a>
</div>
```

## 不确定选哪一个？

| 核对项 | AlohaMini 2 | AlohaMini 2 Pro |
|---|---|---|
| 底盘结构 | 3D 打印底盘 | 金属强化底盘 |
| 底盘轮舵机 | STS3215 × 3 | STS3250 × 3 |
| 从臂 profile | `am-follower-6dof` | `am-follower-6dof-hd` |
| Pi / PC 整机型号 | `alohamini2` | `alohamini2pro` |
| PC 主臂 profile | `am-leader-6dof` | `am-leader-6dof` |
| 硬件教程 | [BOM](bom.md)、[打印](printing.md)、[组装](assembly.md) | [Pro 硬件说明与资料范围](hardware-pro.md) |
| 入门教程 | [AlohaMini 2](alohamini2.md) | [AlohaMini 2 Pro](alohamini2pro.md) |

以实物型号、舵机标签与套件配置为准。改装设备可能不完全匹配预设，需要逐项核对 [设备配置](configuration.md)，不要仅凭外观选择。详细参数见 [机型与参数](specifications.md)。

## 选择你的进度

| 当前状态 | 下一步 |
|---|---|
| 准备组装标准 2 | [物料清单](bom.md) → [3D 打印](printing.md) → [硬件组装](assembly.md) |
| 已有组装好的 2 / 2 Pro | 进入上方对应入门教程，完成环境、配置与校准 |
| 已经能够遥操作 | [数据采集](learning.md) → [策略训练](training.md) → [真机评估](evaluation.md)，选择本机型号的命令 |
| 已有 AlohaMini 1 | [一代说明](legacy.md) |
| 只有一套主从臂 | [AM-ARM200 单臂教程](single-arm.md) |
| 希望查看模型与关节 | [仿真与模型可视化](simulation.md)，注意资源适用代际 |

## 阅读约定

- **Pi / 机器人端**：连接从臂、底盘、升降和相机，运行 Host 服务。
- **PC / 操作端**：连接主臂，运行遥操作、录制和评估程序。
- 两款的入门页分别给出完整命令。共用专题中，标注型号的两组命令只执行与你实物相符的一组。
- 数据集示例使用 `am2_` 和 `am2pro_` 前缀区分来源；名称本身不会自动选择硬件配置。
- 两款均为 18 维整机接口，但相同维度不能证明数据集和策略可以直接互换；还需核对特征顺序、单位、校准、相机及实际硬件。

来源：[GitHub 硬件 Profiles](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/alohamini/profiles.md)。
