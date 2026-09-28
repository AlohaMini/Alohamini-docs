# 调试与排错

按“环境 → 设备 → 配置 → 校准 → 通信 → 数据 → 策略”的顺序排查。每次只改变一项配置，并保留 Host 与 PC 的原始错误信息，避免多个问题叠加。

## 快速定位

| 现象 | 优先检查 | 对应章节 |
|---|---|---|
| 命令不存在、模块导入失败 | 环境是否激活，是否在正确仓库安装 | [软件安装](software.md) |
| 找不到机械臂 | USB 数据线、端口、权限、设备别名 | [设备配置](configuration.md) |
| 启动后反复要求校准 | 设备 ID、profile、左右映射是否变化 | [校准](calibration.md) |
| 从臂动作方向或范围错误 | 机型、左右端口、校准与装配 | [遥操作](teleoperation.md) |
| 相机缺失或画面接反 | 启用列表、设备路径、实际视角 | [相机配置](configuration.md) |
| 连接超时或运动暂停 | Host、IP、反馈、控制权、保护日志 | [运行机制](runtime.md) |
| 续录失败 | 原数据目录、repo_id、特征与 FPS | [数据采集](learning.md) |
| 模型维度不匹配 | 一代／二代接口、相机名、训练数据 | [策略训练](training.md) |

## 1. 确认当前软件环境

```bash
pwd
python --version
python -c "import sys; print(sys.executable)"
python -c "import av, cv2, torch; print('av', av.__version__); print('cv2', cv2.__version__); print('torch', torch.__version__)"
git rev-parse --short HEAD
```

预期：当前目录是软件仓库；Python 来自已激活的项目环境；关键依赖可以导入。两台机器提交版本不一致时，先确认协议是否兼容，再定位通信层问题。

## 2. 串口找不到或无权限

```bash
lerobot-find-port
ls -l /dev/ttyACM*
ls -l /dev/serial/by-id/
ls -l /dev/am_arm_*
groups
```

### 找不到设备节点

逐个接入控制板，检查数据线、USB 连接和控制板供电。只充电的 Type-C 线不能提供串口通信；旧的 `/dev/ttyACM0` 编号也可能已经改变。

### 设备存在，但程序没有权限

检查当前用户是否属于 `dialout` 组；添加组后重新登录。不要用长期以 root 运行整个机器人程序来替代权限配置。

### 别名存在，但左右不对

回到 udev 规则，对照每块板子的序列号和物理位置。校准文件、遥操作和录制必须始终使用同一左右映射。

### 端口被占用

停止先前运行的 Host、校准、遥操作或硬件调试程序。一个程序仍在使用串口时，另一个程序可能无法正常连接。

## 3. 舵机状态与编号

查看连接总线上的舵机状态：

```bash
python examples/debug/motors.py get_motors_states \
  --port /dev/ttyACM0
```

检查读到的 ID、型号和状态是否符合实际接线。写入新 ID 时每次只连接目标舵机：

```bash
python examples/debug/motors.py configure_motor_id \
  --id 1 \
  --set_id 8 \
  --port /dev/ttyACM0
```

二代底盘目标 ID 为右后轮 8、前轮 9、左后轮 10、升降 11，物理位置以 [组装图](assembly.md) 为准。

### 使用旧硬件调试脚本前先核对

`examples/debug/wheels.py` 和 `axis.py` 是直接访问总线的工具。当前文件中的舵机型号常量仍为 `sts3215`，`axis.py` 不会根据整机二代配置自动选择 STS3095；轮组脚本也有自己的轮位命名与运动学常量。

因此，**二代／Pro 首次整机检查优先采用匹配 `robot_model` 的 Host + 键盘客户端**，见 [仅底盘与升降遥操作](teleoperation.md)。只有确认脚本的型号、ID 与结构匹配后，才直接运行独立调试脚本。

改相位、重设中位、释放扭矩和执行动作脚本会改变硬件状态，不属于通用的“修复所有问题”操作。用途及入口见 [命令参考](commands.md)。

## 4. 相机无法打开或缺图

```bash
lerobot-find-cameras
v4l2-ctl --list-devices
v4l2-ctl -d /dev/video0 --list-formats-ext
```

按以下顺序检查：

1. 相机是否被系统识别，`index_or_path` 是否指向它。
2. 配置要求的分辨率和帧率是否受设备支持。
3. 相机是否被另一个程序占用。
4. Host 配置启用了哪些相机，设备是否都已连接。
5. 当前画面对应哪个物理位置，左右腕是否接反。
6. 是否存在 USB 带宽、供电或多设备共用 Hub 的问题。

修改相机配置后重启两端相关程序。默认仅启用两路，看到五只物理相机不代表程序会自动使用五路。

## 5. 网络连接与性能

PC 检查 Pi：

```bash
ping <Pi_IP>
```

在使用无线网络的机器上检查链路：

```bash
iw dev
iw dev wlan0 link
```

`wlan0` 需换为实际无线网卡名称。需要测量吞吐量且已安装 iperf3 时，在 Host 上运行：

```bash
iperf3 -s
```

在 PC 上运行：

```bash
iperf3 -c <Pi_IP>
```

测试结束后退出 iperf3 服务。网络延迟或吞吐正常仍不代表整个控制链路正常，还需结合设备采集和 CPU 负载。

### 观察计算负载

```bash
top
```

训练 PC 若使用 NVIDIA GPU，可查看：

```bash
nvidia-smi
```

遥操作卡顿先尝试 10 Hz 控制与 10 Hz 相机请求的排查配置，见 [遥操作](teleoperation.md)。检查 CPU、网络与相机后再恢复正式采集配置。

## 6. 录制与视频问题

### 数据集目录已经存在

核对这是新建还是续录。续录使用同一数据标识和目录并加入 `--resume`；新实验使用新名称。不要直接删除旧数据来消除报错。

### 多频采集时间比设定更长

该入口需要收集足够的新鲜帧，实际相机帧率稍低时会延长时间。如果明确中止，检查日志是相机停滞、跨相机时间差、状态对齐还是帧率不足。

### 视频编码／解码失败

```bash
ffmpeg -version
ffmpeg -hide_banner -encoders
python -c "import av; print(av.__version__)"
```

确认环境一致、视频文件已完整保存，再按错误定位缺少的编码器或后端。不要在写入尚未结束时复制半成品数据集。

## 7. 评估不动作或突然暂停

- 先确认没有遥操作或录制客户端仍持有控制权。
- 核对 Pi 与 PC 的机型是否一致，模型目录是否正确。
- 查看 Host 是否触发电流保护、看门狗或发生重启。
- 查看客户端是否缺少新鲜反馈，或策略推理耗时使 Host 超时。
- ACT 使用 `sync`；RTC 必须由模型接口支持。

暂停后的旧动作队列不会自动继续执行。处理故障后按程序流程重新开始，避免把“没有继续动作”误当作单纯网络丢包。

## 8. 提交可复现问题

将以下内容一起提交到 [软件 Issues](https://github.com/liyiteng/lerobot_alohamini/issues)：

```text
机型：AlohaMini 1 / 2 / 2 Pro
主臂与从臂型号：
PC 系统、CPU/GPU：
Pi 系统与架构：
两端软件提交版本：
操作阶段：安装 / 校准 / 遥操作 / 录制 / 训练 / 评估
完整命令（移除访问令牌等秘密）：
预期结果：
实际结果：
Host 日志：
PC 日志：
最近修改过的配置：
```

硬件装配问题请补充局部照片、零件名称和材料，并提交到 [硬件 Issues](https://github.com/liyiteng/AlohaMini/issues)。

来源：[调试工具](https://github.com/liyiteng/lerobot_alohamini/tree/main/examples/debug)、[命令速查](https://github.com/liyiteng/lerobot_alohamini/blob/main/docs/alohamini/commands.md)。
