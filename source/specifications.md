# 机型与参数

AlohaMini 2 在一代的双臂移动架构上升级了机械臂、升降机构和底盘。

## 两代机器人对比

| 项目 | AlohaMini 1 | AlohaMini 2 |
|---|---|---|
| 机械臂 | SO-ARM100 / SO-ARM101 | AM-ARM200 |
| 单臂自由度 | 5+1 | 6+1 |
| 臂展 | 40 cm | 52 cm |
| 单臂负载 | 0.3 kg | 1 kg |
| 底盘最大负载 | 10 kg | 70 kg |
| 升降能力 | 5 kg | 30 kg |
| 摄像头 | 5 路 | 5 路 |
| 打印机要求 | 大幅面 FDM，打印床 ≥ 380 mm | Bambu P2S 级消费打印机 |

以上为项目 README 的标称参数，具体负载能力与组装、材料和运行条件有关。

## AlohaMini 2 与 2 Pro

| 型号 | 舵机方案 | 底盘 | 项目定位 |
|---|---|---|---|
| AlohaMini 2 | STS-3215 等标准舵机 | 3D 打印底盘 | 自行搭建与研发 |
| AlohaMini 2 Pro | STS-3250 工业级舵机方案 | 金属强化底盘 | 更高强度的实验室使用 |

这里的打印和组装指南针对标准 AlohaMini 2。Pro 的配置应以对应硬件说明为准。

## 获取设计资源

- [Mobile Base 2 结构文件](https://github.com/liyiteng/AlohaMini/tree/main/AlohaMini2/hardware/mobile_base2)
- [AM-ARM200 机械臂](https://github.com/liyiteng/AM-ARM/tree/main/am-arm200)
- [项目原始参数说明](https://github.com/liyiteng/AlohaMini#whats-new-in-alohamini2)


## 软件硬件配置对应表

| `robot_model` | 从臂 profile | 底盘轮舵机 | 升降舵机 | 升降传动参数 |
|---|---|---|---|---|
| `alohamini1` | `so-arm-5dof` | STS3215 × 3 | STS3215 | 84 mm/rev |
| `alohamini2` | `am-follower-6dof` | STS3215 × 3 | STS3095 | 131 mm/rev |
| `alohamini2pro` | `am-follower-6dof-hd` | STS3250 × 3 | STS3095 | 131 mm/rev |

表中 mm/rev 是软件 profile 的传动参数，不是升降速度或总行程。Pro 的整机选择由 `robot_model` 完成，PC 上的 AM 主臂仍使用 `am-leader-6dof`。

## 自由度与数据维度

“6+1 自由度”表示单臂六个运动关节加夹爪。整机的数据接口还包含底盘与升降：

| 机型 | 双臂维度 | 底盘 | 升降 | 总 state/action 维度 |
|---|---:|---:|---:|---:|
| 一代 | 6 × 2 = 12 | 3 | 1 | 16 |
| 二代／Pro | 7 × 2 = 14 | 3 | 1 | 18 |

底盘三个分量为 `x.vel`、`y.vel`、`theta.vel`，升降使用 `lift_axis.height_mm`。这些是控制接口维度，不应把它们全部称为旋转关节。模型与数据集除了维度相同，还必须核对字段顺序与单位。

## 相机与观测

硬件布局包含前向、后向、胸部和左右手腕共五路相机。当前软件默认启用前向与右腕两路，其他视角通过配置启用。相机的物理规格、当前采集分辨率、模型输入大小是三个不同概念，不能仅凭 BOM 的“720p”判断训练输入。

启用相机时先按 [设备配置](configuration.md) 确认名称与视角，并保持录制和评估一致。

## 参数该怎样使用

标称负载描述项目设计能力，不代表每种材料、姿态和打印替代件都经过同样验证。自行搭建时记录材料、金属件替代情况和实际负载；带负载运行前先完成空载装配与运动检查。

一代与二代的机械臂、升降传动和接口不同。已有一代用户不能只修改机型字符串就获得二代配置，也不能直接复用不同维度的训练检查点。

软件配置来源：[Hardware Profiles](https://github.com/liyiteng/lerobot_alohamini/blob/main/docs/alohamini/profiles.md)、[整机型号定义](https://github.com/liyiteng/lerobot_alohamini/blob/main/src/lerobot/robots/alohamini/model_specs.py)。
