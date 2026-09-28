# 命令参考

适用型号：**AlohaMini 2 / 2 Pro**。标注型号的两组示例请选择一组执行。完整入门流程：[2 教程](alohamini2.md) · [2 Pro 教程](alohamini2pro.md)。

本页用于已经完成教程后的快速查阅。完整步骤、参数解释和预期结果请进入对应章节。除另行注明，命令都在 `lerobot_alohamini` 根目录、激活环境后执行。

## 占位符约定

| 写法 | 替换成什么 |
|---|---|
| `<Pi_IP>` | 机器人端实际局域网 IP |
| `/dev/ttyACM0` | 当前硬件对应的真实串口 |
| `$HF_USER` | 当前终端已设置的 Hugging Face 用户名 |
| `/absolute/path/...` | 本机实际存在或准备创建的绝对路径 |
| `020000` | 实际已保存的检查点步数 |

不要原样执行带尖括号的占位符。为减少参数遗漏，机型、主臂 profile 和设备标识均建议显式填写。

## 环境与发现设备

```bash
conda activate lerobot_alohamini
lerobot-find-port
lerobot-find-cameras
ls -l /dev/am_arm_*
```

详见 [安装](software.md) 与 [设备配置](configuration.md)。

## 校准入口

Pi：

**AlohaMini 2**

```bash
python -m lerobot.robots.alohamini.alohamini_calibrate --robot_model alohamini2
```

**AlohaMini 2 Pro**

```bash
python -m lerobot.robots.alohamini.alohamini_calibrate --robot_model alohamini2pro
```

PC：

```bash
python examples/alohamini/calibrate_bi.py \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof
```

详见 [校准](calibration.md)。

## Host 与遥操作

Pi：

**AlohaMini 2**

```bash
python -m lerobot.robots.alohamini.alohamini_host --robot_model alohamini2
```

**AlohaMini 2 Pro**

```bash
python -m lerobot.robots.alohamini.alohamini_host --robot_model alohamini2pro
```

PC：

**AlohaMini 2**

```bash
python examples/alohamini/teleoperate_bi.py \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2 \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof \
  --fps 50 \
  --camera-fps 30
```

**AlohaMini 2 Pro**

```bash
python examples/alohamini/teleoperate_bi.py \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2pro \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof \
  --fps 50 \
  --camera-fps 30
```

详见 [遥操作](teleoperation.md)。

## 数据与策略入口

| 任务 | 入口 | 完整教程 |
|---|---|---|
| 标准双臂录制 | `python examples/alohamini/record_bi.py` | [数据采集](learning.md) |
| 多频双臂录制 | `python examples/alohamini/record_bi_multirate.py` | [数据采集](learning.md) |
| 真机回放 | `python examples/alohamini/replay_bi.py` | [数据检查与回放](learning.md) |
| 离线查看 | `lerobot-dataset-viz` | [数据检查](learning.md) |
| ACT 训练 | `lerobot-train` | [训练](training.md) |
| 整机评估 | `python examples/alohamini/evaluate_bi.py` | [评估](evaluation.md) |

表中是程序入口，仍需传入对应教程中的完整参数。可先运行 `--help` 查看当前安装版本接受的参数。

## 机型参数速查

| 机型 | `robot_model` | 主臂 profile | 常用主臂 ID |
|---|---|---|---|
| 一代 | `alohamini1` | `so-arm-5dof` | `so101_leader_bi` |
| 二代 | `alohamini2` | `am-leader-6dof` | `am_leader_bi` |
| Pro | `alohamini2pro` | `am-leader-6dof` | `am_leader_bi` |

Host 使用 `--robot_model`，PC 使用 `--robot.robot_model`；主臂 ID 要与实际校准时使用的值一致。

## 舵机调试工具

### 查看状态

```bash
python examples/debug/motors.py get_motors_states --port /dev/ttyACM0
```

### 修改单个 ID

每次只连接一只待配置舵机：

```bash
python examples/debug/motors.py configure_motor_id \
  --id 1 --set_id 8 --port /dev/ttyACM0
```

### 其他高级操作

下列子命令会修改状态或引起运动，使用前需核对硬件和参数。此处提供含义，避免把与设备无关的目标位置当作通用调试值。

| 子命令 | 作用 | 参数注意 |
|---|---|---|
| `move_motor_to_position` | 将指定舵机移到目标位置 | `--position` 为原始 tick，不是角度或毫米 |
| `configure_motor_phase` | 修改相位 | `--id` 指定对象；不应随意批量修改 |
| `reset_motors_to_midpoint` | 把当前位置设为中位相关配置 | 先确认实际姿态和后续校准影响 |
| `reset_motors_torque` | 关闭扭矩 | 失去保持力后需承托可能下落的机构 |
| `move_motors_by_script` | 执行动作脚本 | 核对脚本中的全部动作与适用硬件 |

读取具体参数：

```bash
python examples/debug/motors.py --help
```

独立 `wheels.py`、`axis.py` 有自己的舵机与几何常量，不能仅传入串口就认为已经适配二代或 Pro。详见 [调试与排错](troubleshooting.md)。
