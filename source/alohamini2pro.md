# AlohaMini 2 Pro 入门教程

收到整机后先完成 [开箱图解](unboxing.md)。有 LeRobot 经验可另读 [Pro 交付快速入门](yuque/pro-quickstart.md)，其中保留端口绑定截图及采集、训练示例。

本页适用于 **AlohaMini 2 Pro + AM-ARM200 系列双主臂 + Linux PC + 树莓派 5**。按顺序完成设备配置、校准、遥操作和第一条数据录制。

**当前机型：`alohamini2pro`** · 切换到 [AlohaMini 2 教程](alohamini2.md) · [返回机型选择](quickstart.md)

下列命令在 **软件仓库 `lerobot_alohamini` 的根目录**运行；先激活安装时创建的 Python 环境。将 `<Pi_IP>` 替换为树莓派的真实 IP，再执行命令。

## 选择你的起点

| 当前状态 | 从哪里开始 |
|---|---|
| 核对 Pro 硬件或准备搭建 | 先看 [2 Pro 硬件说明](hardware-pro.md)，确认实际套件与资料范围 |
| 已有组装好的机器人 | 本页“安装与设备配置” |
| 已能遥操作，准备训练 | [数据采集](learning.md) → [训练](training.md) → [评估](evaluation.md) |
| 只有一套主从臂 | [AM-ARM200 单臂教程](single-arm.md) |
| 已有一代机器人 | [一代说明](legacy.md)，再使用对应机型参数 |
| 先查看模型与关节 | [仿真与模型可视化](simulation.md) |

## 你需要准备什么

先按 [2 Pro 硬件说明](hardware-pro.md) 核对从臂和底盘。标准 2 的打印件、物料数量和组装照片不能直接作为 Pro 的装配清单。

### 机器人端

- 已正确装配的底盘、升降机构与双从臂。
- 树莓派 5、存储卡、供电与散热。
- 从臂总线控制板和数据线。
- 已安装的相机及其连接线。

### 操作端

- 可运行项目软件的 Linux PC。
- 两只已组装的主臂、控制板、数据线和匹配电源。
- PC 与树莓派可互通的局域网。
- 用于保存数据集的存储空间；训练另需与策略匹配的计算资源。

主臂在操作台由人手推动，从臂安装在机器人上执行动作。**Host 是机器人端服务，Client 是 PC 上的控制程序。** 后面的命令会明确标注在哪一端运行。

## 第一步：确认机型

| 核对项 | AlohaMini 2 Pro 配置 |
|---|---|
| Pi 整机参数 `--robot_model` | `alohamini2pro` |
| PC 整机参数 `--robot.robot_model` | `alohamini2pro` |
| 从臂 profile（由机型选择） | `am-follower-6dof-hd` |
| PC 主臂 `--teleop.arm_profile` | `am-leader-6dof` |
| 主臂设备 ID 示例 | `am_leader_bi` |
| 底盘轮舵机 | STS3250 × 3 |
| 升降舵机 / 传动参数 | STS3095 / 131 mm/rev |
| 整机 state/action 维度 | 18 |

两端显式选择同一个型号。主臂 profile 与从臂 profile 用途不同；校准、遥操作和录制中的主臂 ID 保持一致。`am_leader_bi` 是示例标识，若有多套主臂，请各用独立标识和对应校准文件。

完整差异见 [机型与参数](specifications.md)。131 mm/rev 是软件传动参数，不是升降速度或总行程。

## 第二步：安装与设备配置

在 **PC 和 Pi 两端**按 [软件安装](software.md) 完成环境。随后按 [设备配置](configuration.md) 建立端口映射并核对相机。

完成后应能确认：

| 检查对象 | 结果 |
|---|---|
| PC 主臂 | 左右主臂设备名分别指向正确控制板 |
| Pi 从臂 | 左右从臂总线分别可访问 |
| 相机 | 每个启用名称对应正确画面；默认启用两路 |
| 网络 | PC 可访问 Pi 的实际 IP |
| 软件 | 两端版本兼容，项目环境已激活 |

第一次连接时不要猜串口和相机索引，使用发现工具逐个记录。

## 第三步：完成校准

**Pi：机器人端校准**

```bash
python -m lerobot.robots.alohamini.alohamini_calibrate --robot_model alohamini2pro
```

**PC：双主臂校准**

```bash
python examples/alohamini/calibrate_bi.py \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof
```

按交互提示完成左右臂的范围记录。完整说明见 [校准教程](calibration.md)。校准完成后按原始流程对主从臂断电重启。

## 第四步：第一次遥操作

**Pi：启动 Host 并保持运行**

```bash
python -m lerobot.robots.alohamini.alohamini_host --robot_model alohamini2pro
```

**PC：启动控制程序**

```bash
python examples/alohamini/teleoperate_bi.py \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2pro \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof \
  --fps 50 \
  --camera-fps 30
```

替换 `<Pi_IP>`。先单侧、小范围移动主臂，再检查夹爪，最后检查底盘与升降。整机按键：W/S 前后，Z/X 横移，A/D 旋转，U/J 升降。更多参数和控制权说明见 [遥操作](teleoperation.md)。

## 第五步：录制第一条数据

退出 PC 上的遥操作程序，保持 Pi Host 运行。先录制短测试：

```bash
export HF_USER="your-hf-username"
python examples/alohamini/record_bi.py \
  --dataset.repo_id $HF_USER/am2pro_first_episode \
  --dataset.num_episodes 1 \
  --dataset.fps 10 \
  --dataset.episode_time_s 10 \
  --dataset.reset_time_s 3 \
  --dataset.single_task "Pick up the object and place it in the tray" \
  --dataset.push_to_hub=false \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2pro \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof
```

这是采集链路测试。先把 `HF_USER` 换成自己的命名空间，把任务描述改为本次实际动作；示例关闭自动上传。

录制结束后查看第一条数据：

```bash
lerobot-dataset-viz \
  --repo-id $HF_USER/am2pro_first_episode \
  --episode-index 0 \
  --display-compressed-images
```

确认相机视角正确、动作完整、没有长时间画面冻结，再进入 [正式采集](learning.md)。

## 如何判断入门完成

- 能说明自己的机器人型号、主臂 profile 与左右端口。
- 左右从臂与主臂对应，方向和夹爪运动正常。
- 底盘与升降按预期响应，线缆没有干涉。
- 每个启用相机视角正确。
- 已保存一条数据，知道本地位置，并完成回看。

正式实验先进入 [数据采集](learning.md)，使用页面中 **AlohaMini 2 Pro** 的正式录制示例；入门短测试仅用于检查链路，不能据此判断策略效果。建议数据集名称带上 `am2pro` 前缀，便于与其他机型区分。

之后按 [训练](training.md) → [评估](evaluation.md) 完成策略闭环。某一步未通过时，优先查看 [调试与排错](troubleshooting.md)，不要带着设备映射或校准错误进入训练阶段。


## 教程依据

机型配置和操作顺序依据 [GitHub 硬件 Profiles](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/alohamini/profiles.md) 与 [整机工作流](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/alohamini/alohamini.md) 整理。核对日期：2026-09-28。命令已按源码核对，尚未在实体机器人上完成验证。
