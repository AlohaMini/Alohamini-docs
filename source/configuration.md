# 设备与机型配置

本页把“能找到设备”推进到“程序使用的是正确设备”。先区分机器人机型、主臂型号、左右串口和相机名称，再开始校准。

## 1. 选择整机与主臂配置

| 实际机器人 | Host `--robot_model` | PC `--robot.robot_model` | PC `--teleop.arm_profile` |
|---|---|---|---|
| AlohaMini 1 + SO 主臂 | `alohamini1` | `alohamini1` | `so-arm-5dof` |
| AlohaMini 2 + AM 主臂 | `alohamini2` | `alohamini2` | `am-leader-6dof` |
| AlohaMini 2 Pro + AM 主臂 | `alohamini2pro` | `alohamini2pro` | `am-leader-6dof` |

**整机型号两端必须一致。** `robot_model` 决定从臂、底盘与升降配置；`teleop.arm_profile` 描述 PC 上的主臂。Pro 仍使用 AM 主臂配置，不把从臂的 `am-follower-6dof-hd` 填入主臂参数。

当前部分客户端脚本默认一代，而 Host 配置默认二代。因此本手册命令都显式指定机型，避免依赖不一致的默认值。

## 2. 找到每只机械臂的串口

在对应机器上逐个接入控制板并记录端口：

```bash
lerobot-find-port
ls /dev/ttyACM*
ls /dev/serial/by-id/
```

| 机器 | 需要区分的设备 |
|---|---|
| PC | 左主臂、右主臂 |
| Pi | 左从臂总线、右从臂总线 |

`lerobot-find-port` 会先记录设备列表，再提示拔下目标控制板的 USB 并按 Enter，最后根据变化找到端口。完成后重新接回该板。每次只拔下一块板，避免出现多个候选端口。

`ttyACM0`、`ttyACM1` 的编号可能在重启或重新插拔后变化。不要仅凭第一次观察到的顺序长期使用。

## 3. 固定左右臂设备名

项目双臂脚本使用固定路径。可以创建以下 udev 别名，也可以修改脚本中的真实端口；同一设备在校准、遥操作和录制中必须一致。

### 读取控制板序列号

```bash
udevadm info --attribute-walk --name=/dev/ttyACM0 | awk -F'"' '/ATTRS{serial}/{print $2; exit}'
```

分别读取每块板子，记录其物理位置。如果不同板子没有可区分的唯一序列号，下面基于序列号的规则不能唯一识别它们，需要进一步按实际 USB 设备信息配置。

### Pi：从臂规则

编辑 `/etc/udev/rules.d/90-mydevice.rules`，填入真实序列号：

```text
SUBSYSTEM=="tty", ATTRS{serial}=="<follower_left_serial>", SYMLINK+="am_arm_follower_left"
SUBSYSTEM=="tty", ATTRS{serial}=="<follower_right_serial>", SYMLINK+="am_arm_follower_right"
```

### PC：主臂规则

在 PC 上的同名规则文件中填写：

```text
SUBSYSTEM=="tty", ATTRS{serial}=="<leader_left_serial>", SYMLINK+="am_arm_leader_left"
SUBSYSTEM=="tty", ATTRS{serial}=="<leader_right_serial>", SYMLINK+="am_arm_leader_right"
```

### 重新加载并核对

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
ls -l /dev/am_arm_*
```

核对别名指向的控制板后，重新插拔一次确认稳定。Pi 的配置文件是：

```text
src/lerobot/robots/alohamini/config_alohamini.py
```

其中从臂字段应指向：

```python
left_port: str = "/dev/am_arm_follower_left"
right_port: str = "/dev/am_arm_follower_right"
```

PC 上 `calibrate_bi.py`、`teleoperate_bi.py`、`record_bi.py` 等双臂入口应使用左、右主臂对应路径。优先采用稳定别名，减少多处改动带来的不一致。

## 4. 找到相机及支持的格式

在 Pi 上执行：

```bash
lerobot-find-cameras
v4l2-ctl --list-devices
v4l2-ctl -d /dev/video0 --list-formats-ext
```

`v4l2-ctl` 来自 Linux 的 `v4l-utils` 工具包；未安装时需先安装。逐一确认画面对应哪个位置，记录设备路径、分辨率与帧率。

| 硬件视角 | 当前配置中的名称 |
|---|---|
| 前向 | `forward` |
| 后向 | `backward` |
| 胸部 | `chest` |
| 左腕 | `wrist_left` |
| 右腕 | `wrist_right` |

### 五路硬件不等于默认启用五路

当前 `alohamini_cameras_config()` 默认启用 **`forward` 与 `wrist_right` 两路**，其他三路被注释。默认采集参数为 **640×480、30 FPS**；这与 BOM 中相机的硬件分辨率描述是不同层面的参数。

默认路径使用 `/dev/am_camera_forward` 等别名。如果设备上没有这些别名，需根据相机发现结果修改 `index_or_path`，或自行建立稳定的相机设备映射。相机别名不会因为完成机械臂 udev 规则而自动产生。

### 配置示例

在已有配置文件的 `alohamini_cameras_config()` 中按实物修改条目，例如：

```python
"forward": OpenCVCameraConfig(
    index_or_path="/dev/video0",
    fps=30,
    width=640,
    height=480,
    rotation=Cv2Rotation.NO_ROTATION,
),
```

`/dev/video0` 只是示例，不能代替设备发现。需要其他视角时取消对应条目的注释，并确认其路径有效。两端如果使用该函数生成特征，应保持相机名称与配置一致，修改后重启 Host 和客户端。

软件原始指南建议相机分别连接 USB 端口，避免多个相机共用同一个 USB Hub。若实际带宽不足，先减少启用路数、降低采集负载并检查画面稳定性。

## 5. 确认网络与端口

记录 Pi 的实际局域网 IP，将命令中的 `<Pi_IP>` 替换为该地址。PC 上检查：

```bash
ping <Pi_IP>
```

| TCP 端口 | 用途 |
|---|---|
| 5555 | 控制命令 |
| 5556 | 状态、观测与元数据 |
| 5557 | 可选的独立相机流；需 Host 显式启用 |

`ping` 成功只证明基本连通，还需确认 Host 正常启动、对应端口未被占用且网络允许访问。详细的控制频率与反馈机制见 [运行机制](runtime.md)。

## 配置完成检查

- 两端整机型号一致，主臂 profile 与实物一致。
- 四只机械臂的左右端口可稳定识别。
- 配置中每一路启用相机都有正确画面。
- 相机名称与后续数据集、策略所需名称对应。
- PC 可以访问 Pi，软件版本彼此兼容。

完成后进入 [机械臂校准](calibration.md)。


## 交付教程中的相机命名差异

不同软件配置可能使用 `head_top`、`head_back`、`head_front`，或 `forward`、`backward`、`chest`。这些名称不能在采集后随意互换。

1. 查看本机 `alohamini_cameras_config()` 的实际启用项。
2. 核对设备路径与实际画面，再把相同配置同步到 Pi 和 PC。
3. 数据集中的 `observation.images.*`、训练输入和评估观测保持一致。
4. 使用纯视觉转换脚本时，`--keep-camera` 也填写数据集中真实存在的名称。
