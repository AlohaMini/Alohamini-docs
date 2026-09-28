# 遥操作

适用型号：**AlohaMini 2 / 2 Pro**。标注型号的两组示例请选择一组执行。完整入门流程：[2 教程](alohamini2.md) · [2 Pro 教程](alohamini2pro.md)。

本章完成 PC 主臂驱动机器人从臂、键盘控制底盘与升降的整机流程。前提是 [安装](software.md)、[配置](configuration.md) 和 [校准](calibration.md) 已完成。

## 1. 在 Pi 启动 Host

按实际机型启动：

**AlohaMini 2**

```bash
python -m lerobot.robots.alohamini.alohamini_host --robot_model alohamini2
```

**AlohaMini 2 Pro**

```bash
python -m lerobot.robots.alohamini.alohamini_host --robot_model alohamini2pro
```

一代使用 `alohamini1`，详见 [一代说明](legacy.md)。保持该终端运行，检查启动日志中的端口、校准与相机信息；出现设备错误时先解决，再启动客户端。

## 2. 在 PC 启动双臂遥操作

按实际机型与 AM 主臂配置启动：

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

| 参数 | 含义 |
|---|---|
| `robot.remote_ip` | Pi 的实际局域网 IP |
| `robot.robot_model` | 与 Host 相同的整机型号 |
| `teleop.id` | 与主臂校准时相同的设备标识 |
| `teleop.arm_profile` | 主臂硬件 profile |
| `fps` | 控制命令与状态循环目标频率 |
| `camera-fps` | 相机观测请求频率，应不大于控制频率 |

两款 AM 主臂 profile 相同；整机型号必须与 Pi Host 一致。一代使用 `alohamini1`、`so101_leader_bi` 和 `so-arm-5dof`。

## 3. 先检查机械臂

缓慢移动一侧主臂，检查对应从臂是否跟随；再检查另一侧。分别验证关节与夹爪，不要一开始同时移动双臂、底盘和升降。

如果左右相反、关节方向异常或出现明显跳动，先退出遥操作，检查左右串口、机型与校准标识。不要在不匹配的配置下继续采集数据。

## 4. 键盘控制

当前整机客户端的默认按键如下：

| 按键 | 动作 |
|---|---|
| `W` / `S` | 底盘前进／后退 |
| `Z` / `X` | 底盘向左／向右横移 |
| `A` / `D` | 底盘向左／向右旋转 |
| `T` / `G` | 提高／降低移动速度档位 |
| `U` / `J` | 升降向上／向下 |
| `Ctrl+C` | 在运行终端中断遥操作程序 |

当前配置表虽保留 `Q` 退出映射，但所核对的遥操作主循环未处理该退出分支，因此本教程使用终端 `Ctrl+C` 结束程序。

保证控制程序能接收到键盘输入。首次检查只短暂触发单一方向，观察运动与释放后的响应；可使用终端中断结束程序。

## 5. 低负载排查

若画面或运动不稳定，可以先降低控制和相机请求频率，以区分 CPU、USB、网络或配置问题：

**AlohaMini 2**

```bash
python examples/alohamini/teleoperate_bi.py \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2 \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof \
  --fps 10 \
  --camera-fps 10
```

**AlohaMini 2 Pro**

```bash
python examples/alohamini/teleoperate_bi.py \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2pro \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof \
  --fps 10 \
  --camera-fps 10
```

这个设置用于定位问题，不代表应该长期使用低频数据训练。查明原因后恢复任务需要的配置，并在正式采集前保持一致。

## 6. 仅调试底盘与升降

项目提供跳过机械臂的入口。Pi：

**AlohaMini 2**

```bash
python -m lerobot.robots.alohamini.alohamini_host \
  --robot_model alohamini2 \
  --no_follower
```

**AlohaMini 2 Pro**

```bash
python -m lerobot.robots.alohamini.alohamini_host \
  --robot_model alohamini2pro \
  --no_follower
```

PC：

**AlohaMini 2**

```bash
python examples/alohamini/teleoperate_bi.py \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2 \
  --no_leader
```

**AlohaMini 2 Pro**

```bash
python examples/alohamini/teleoperate_bi.py \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2pro \
  --no_leader
```

`--no_follower` 与 `--no_leader` 分别控制两端。使用前仍需确认底盘、升降总线和相机配置正确。

## 7. 控制权与退出

Host 同一时刻只接受一个控制客户端。开始录制或评估前，先停止当前遥操作客户端，避免另一进程持续占用控制权。

当前 Host 在超过 1 秒未收到命令时会停止运动并释放控制权。网络断开、反馈过期或电流保护可能使运行暂停；应确认原因后显式恢复。详细行为见 [运行机制与保护](runtime.md)。

## 进入数据采集

在以下条件满足后进入 [数据采集](learning.md)：左右机械臂对应正确、底盘和升降正常、启用相机画面正确、网络稳定，且能够重复完成计划采集的任务。

来源：[整机工作流](https://github.com/liyiteng/lerobot_alohamini/blob/main/docs/alohamini/alohamini.md)、[按键与网络配置](https://github.com/liyiteng/lerobot_alohamini/blob/main/src/lerobot/robots/alohamini/config_alohamini.py)。
