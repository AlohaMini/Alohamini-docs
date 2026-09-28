# 机械臂校准

校准建立舵机原始读数与机械臂运动范围之间的对应关系。左右主臂与机器人端从臂分别校准，之后遥操作和录制使用同一套设备标识与 profile。

## 校准前确认

1. 已完成 [设备配置](configuration.md)，能识别左右端口。
2. 舵机、机械臂与电源型号对应，安装结构无卡滞。
3. 退出占用相同串口的 Host、遥操作和调试程序。
4. 机械臂活动区域留有空间，并可按终端提示手动摆动关节。

## 1. 在 Pi 校准机器人端

根据机型选择一条命令执行。

### AlohaMini 2

```bash
python -m lerobot.robots.alohamini.alohamini_calibrate --robot_model alohamini2
```

### AlohaMini 2 Pro

```bash
python -m lerobot.robots.alohamini.alohamini_calibrate --robot_model alohamini2pro
```

### AlohaMini 1

```bash
python -m lerobot.robots.alohamini.alohamini_calibrate --robot_model alohamini1
```

该入口完成校准后退出。Host 启动时也会检查校准，如果缺失会进入相应提示，但首次搭建建议先单独完成这一步，便于确认每只机械臂。

### 如何跟随交互提示

原始工作流描述的顺序为：摆到中位、确认，再完成左右方向的范围记录。具体需要移动哪些关节、角度和确认时机，以所选机械臂的校准提示与机械结构为准。不要把 SO 机械臂的姿态图直接套用到 AM-ARM200。

校准时动作应覆盖提示要求的范围，同时避免强行越过机械限位。遇到无法活动的关节，先检查装配和线路，不能靠写入错误范围跳过。

## 2. 在 PC 校准双主臂

主臂校准可以独立完成，**不需要 Pi Host 正在运行**。左右主臂路径默认是 `/dev/am_arm_leader_left` 与 `/dev/am_arm_leader_right`。

### AM 主臂：二代与 Pro

```bash
python examples/alohamini/calibrate_bi.py \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof
```

### SO 主臂：一代

```bash
python examples/alohamini/calibrate_bi.py \
  --teleop.id so101_leader_bi \
  --teleop.arm_profile so-arm-5dof
```

脚本依次处理双主臂。`teleop.id` 是校准配置使用的设备标识，并不是舵机 ID。后续遥操作与录制保持相同值，才能读取对应校准数据。

## 3. 复用还是重新校准

如果发现已有校准，按终端提示选择复用或重新校准。原始流程中 Enter 可复用，`c` 进入重新校准；以当前运行版本实际提示为准。

| 情况 | 建议处理 |
|---|---|
| 同一机械臂、端口与结构未改变 | 核对标识后复用已有校准 |
| 更换主臂型号或 profile | 使用匹配的 profile，重新检查并校准 |
| 拆装关节、更换舵机后姿态变化 | 重新检查安装并校准 |
| 每次启动都要求校准 | 检查 `teleop.id`、左右端口、profile 与运行用户是否变化 |
| 主从臂方向或范围异常 | 停止遥操作，回查型号、左右映射与校准过程 |

## 4. 完成后的检查

按照原始工作流，校准完成后对主臂和从臂断电重启。随后启动 Host，再以 [遥操作](teleoperation.md) 小范围检查左右臂对应关系、运动方向、夹爪和关节范围。

校准成功不代表所有机构都已验证。底盘、升降、相机仍应按各自检查流程确认；策略评估应在手动遥操作正常后进行。

来源：[AlohaMini 校准工作流](https://github.com/liyiteng/lerobot_alohamini/blob/main/docs/alohamini/alohamini.md)、[双主臂校准脚本](https://github.com/liyiteng/lerobot_alohamini/blob/main/examples/alohamini/calibrate_bi.py)。
