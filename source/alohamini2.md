---
html_theme.sidebar_secondary.remove: true
---

# AlohaMini 2：首次使用

**目标：让机器人跟随你的操作，并保存一条 10 秒的任务演示。**

准备好已组装的机器人、AM 双主臂、Linux PC 和树莓派 5。按下面六步完成，已经做好的步骤可以直接跳过。

```{raw} html
<nav class="am-step-route" aria-label="本页步骤"><a href="#step-prepare">1 接线与准备</a><a href="#step-install">2 安装软件</a><a href="#step-configure">3 配置设备</a><a href="#step-calibrate">4 校准机械臂</a><a href="#step-teleoperate">5 第一次遥操作</a><a href="#step-record">6 保存第一条演示</a></nav>
```

(step-prepare)=

::::{admonition} 01 · 接线与准备
:class: am-step

**先核对供电，再开机。** 接线时保持断电。下面的供电方式适用于对应交付套件；以随箱说明和设备标识为准。

1. 机器人上的**从臂、底盘与升降**连接匹配的 **12 V** 电源。
2. 树莓派通过电源板的 **PD 5 V / 5 A** 接口供电。**不能将 12 V 直接接入树莓派的 5 V 输入。**
3. 操作台上的两只**主臂**使用匹配的 **5 V** 电源，再将各自的 USB-C 数据线连接 PC。
4. 开机后，让 PC 和 Pi 连接同一可互通的局域网。在 Pi 上记录当前 IP，后文的 `<Pi_IP>` 都替换为这个地址。

**分清两端：** Pi 控制机器人上的从臂、底盘、升降与相机；PC 连接你用手推动的主臂。后面的每组命令都会标明在哪一端执行。

:::{admonition} 需要对照接线照片？
:class: am-extra

以下照片用于识别接口；不同批次的电池和线束可能不同。

**机器人电源接口**

![Power connection](_static/yuque-assets/ff635586511091d98504.jpeg)

**电源板与树莓派接口**

![Power board](_static/yuque-assets/9b3ffee1eb7bff8f0442.jpeg)

![Pi connection](_static/yuque-assets/3c48272706dd58d09e1f.jpeg)

**主臂供电**

![Leader-arm power](_static/yuque-assets/3b37f35214e5fb1c9d28.jpeg)
:::

检查机械臂、底盘和升降周围有足够空间，线束不会卷入运动部件。屏幕不亮时先检查电池、电源板接口和线缆，不要启动运动程序来测试供电。

```{raw} html
<p class="am-step-done">完成标志：Pi 已开机；两只主臂已连接 PC；你已记下 Pi 的 IP。</p><a class="am-next" href="#step-install">下一步：安装软件 →</a>
```
::::

(step-install)=

::::{admonition} 02 · 安装软件
:class: am-step

**PC 和 Pi 两端都需要安装。** 本教程使用 Linux、Python 3.12 和 Conda。已配置好环境时，直接运行本步末尾的检查命令。

:::{admonition} 还没有安装 Conda？
:class: am-extra

在 **Linux x86_64 PC** 上：

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
~/miniconda3/bin/conda init bash
source ~/.bashrc
```

在 **64 位 ARM Linux 的 Pi** 上：

```bash
mkdir -p ~/miniforge3
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-aarch64.sh -O ~/miniforge3/miniforge.sh
bash ~/miniforge3/miniforge.sh -b -u -p ~/miniforge3
~/miniforge3/bin/conda init bash
source ~/.bashrc
```

这些初始化命令面向 Bash；其他 shell 使用对应初始化方式。不要将 PC 安装包用于 Pi。
:::

**在两端分别获取代码并安装环境：**

```bash
git clone https://github.com/liyiteng/lerobot_alohamini.git
cd lerobot_alohamini
conda create -y -n lerobot_alohamini python=3.12
conda activate lerobot_alohamini
pip install -e ".[all]"
pip install pyzmq feetech-servo-sdk
conda install -y ffmpeg=7.1.1 -c conda-forge
```

两端使用兼容的同版代码。安装报错时先保留错误信息并解决，不要跳过失败的依赖继续控制机器人。

**为两端的控制板配置串口权限：**

```bash
sudo usermod -a -G dialout $USER
```

执行后重新登录，权限才会生效。重新打开终端时进入 `lerobot_alohamini` 仓库目录，并执行 `conda activate lerobot_alohamini`。本页后续命令都在这个目录和环境中运行。

**检查两端环境：**

```bash
python --version
python -c "import av, cv2, torch; print('av', av.__version__); print('cv2', cv2.__version__); print('torch', torch.__version__)"
ffmpeg -version
lerobot-find-cameras --help
```

```{raw} html
<p class="am-step-done">完成标志：依赖导入成功，FFmpeg 和相机发现命令可用。Pi 不需要具备 CUDA。</p><a class="am-next" href="#step-configure">下一步：配置设备 →</a>
```
::::

(step-configure)=

::::{admonition} 03 · 配置设备
:class: am-step

**先固定左右端口，再确认相机。** 本教程后面的命令已经选定你的机型，不需要在多组型号命令之间做选择。

`robot_model=alohamini2` · 主臂 `am-leader-6dof` · 从臂 `am-follower-6dof`

**1. 在对应机器上识别每块控制板**

```bash
lerobot-find-port
ls /dev/ttyACM*
ls /dev/serial/by-id/
```

按工具提示，每次只拔下一块板子的 USB，确认端口后接回。分别记录 PC 的左右主臂、Pi 的左右从臂。`ttyACM0` 只是示例，编号可能在重新插拔后变化。

**2. 读取每块板子的序列号**

```bash
udevadm info --attribute-walk --name=/dev/ttyACM0 | awk -F'"' '/ATTRS{serial}/{print $2; exit}'
```

把命令中的端口换成刚识别的端口。若板子没有可区分的唯一序列号，这组规则不能唯一识别设备，应先解决映射，不能填入重复序列号。

**3. 在两端分别编辑 `/etc/udev/rules.d/90-mydevice.rules`**

Pi 填入从臂的真实序列号：

```text
SUBSYSTEM=="tty", ATTRS{serial}=="<follower_left_serial>", SYMLINK+="am_arm_follower_left"
SUBSYSTEM=="tty", ATTRS{serial}=="<follower_right_serial>", SYMLINK+="am_arm_follower_right"
```

PC 填入主臂的真实序列号：

```text
SUBSYSTEM=="tty", ATTRS{serial}=="<leader_left_serial>", SYMLINK+="am_arm_leader_left"
SUBSYSTEM=="tty", ATTRS{serial}=="<leader_right_serial>", SYMLINK+="am_arm_leader_right"
```

在两端重新加载，并核对别名指向正确的左右设备：

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
ls -l /dev/am_arm_*
```

Pi 应出现 `/dev/am_arm_follower_left`、`/dev/am_arm_follower_right`；PC 应出现 `/dev/am_arm_leader_left`、`/dev/am_arm_leader_right`。重新插拔后再核对一次。

**4. 在 Pi 上识别相机**

```bash
lerobot-find-cameras
v4l2-ctl --list-devices
v4l2-ctl -d /dev/video0 --list-formats-ext
```

`v4l2-ctl` 由 `v4l-utils` 提供；缺少该命令时先安装对应系统软件包。逐个检查实际画面和支持格式。

在 `src/lerobot/robots/alohamini/config_alohamini.py` 的 `alohamini_cameras_config()` 中设置实际路径。当前默认启用 `forward` 与 `wrist_right` 两路，640×480、30 FPS。下面展示其中一路：

```python
"forward": OpenCVCameraConfig(
    index_or_path="/dev/video0",
    fps=30,
    width=640,
    height=480,
    rotation=Cv2Rotation.NO_ROTATION,
),
```

`/dev/video0` 仅是示例，把每个启用条目改为对应相机的真实路径。机械臂别名规则不会自动创建相机别名。若现有配置使用 `head_top` 等其他名称，保留其实际名称并同步两端配置；后续数据与训练也必须使用相同名称。

**5. 在 PC 上确认能访问 Pi**

```bash
ping <Pi_IP>
```

```{raw} html
<p class="am-step-done">完成标志：左右端口固定；启用相机的路径和视角已核对；PC 能访问 Pi。</p><a class="am-next" href="#step-calibrate">下一步：校准 →</a>
```
::::

(step-calibrate)=

::::{admonition} 04 · 校准机械臂
:class: am-step

**先停止 Host、遥操作或调试程序，避免占用串口。** 给关节留出活动空间；校准时按提示缓慢移动，不能强行越过机械限位。

**在 Pi 校准从臂：**

```bash
python -m lerobot.robots.alohamini.alohamini_calibrate --robot_model alohamini2
```

**在 PC 校准两只主臂：**

```bash
python examples/alohamini/calibrate_bi.py \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof
```

按终端提示完成中位和关节范围记录。记录范围时，实际移动每个要求校准的关节，确认最小值与最大值确实变化；不要没有移动就保存。`teleop.id` 后续始终使用 `am_leader_bi`。

:::{admonition} 已经有校准文件，是否需要重做？
:class: am-extra

同一机械臂、设备标识、profile 和结构未改变时，可按提示复用。拆装关节、更换部件、修改 profile 或出现方向／范围异常时，重新核查并校准。出厂已校准并不代表任意配置都能直接复用。
:::

校准完成后对主从臂断电重启，再进入下一步的小幅运动检查。

```{raw} html
<p class="am-step-done">完成标志：两端校准均已保存，设备 ID 与 profile 没有改变。</p><a class="am-next" href="#step-teleoperate">下一步：遥操作 →</a>
```
::::

(step-teleoperate)=

::::{admonition} 05 · 第一次遥操作
:class: am-step

**Pi：启动 Host，保持这个终端运行。**

```bash
python -m lerobot.robots.alohamini.alohamini_host --robot_model alohamini2
```

先确认日志中没有串口、校准或相机错误，再在 PC 启动客户端。

**PC：替换 `<Pi_IP>` 后启动控制程序。**

```bash
python examples/alohamini/teleoperate_bi.py \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2 \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof \
  --fps 50 \
  --camera-fps 30
```

先缓慢移动一侧主臂，确认对应从臂跟随，再检查另一侧和夹爪。确认左右和方向正确后，短暂测试底盘与升降。

| 按键 | 动作 |
|---|---|
| W / S | 前进 / 后退 |
| Z / X | 左移 / 右移 |
| A / D | 左转 / 右转 |
| U / J | 升高 / 降低 |
| T / G | 提高 / 降低速度档位 |
| Ctrl+C | 在运行终端退出遥操作 |

出现左右相反、方向异常或跳动时，立即退出，回查本页第三、四步的端口映射与校准。不要在异常状态下录制。

```{raw} html
<p class="am-step-done">完成标志：双臂、夹爪、底盘与升降响应正确；你能用 Ctrl+C 退出。</p><a class="am-next" href="#step-record">下一步：录制演示 →</a>
```
::::

(step-record)=

::::{admonition} 06 · 保存第一条演示
:class: am-step

**退出 PC 遥操作程序，保持 Pi Host 运行。** 一次只运行一个控制客户端。下面先录制一条 10 秒演示，验证整个采集流程。

在 PC 上把 `HF_USER` 改为自己的 Hugging Face 用户名，将任务描述改成实际动作，再运行：

```bash
export HF_USER="your-hf-username"
python examples/alohamini/record_bi.py \
  --dataset.repo_id $HF_USER/am2_first_episode \
  --dataset.num_episodes 1 \
  --dataset.fps 10 \
  --dataset.episode_time_s 10 \
  --dataset.reset_time_s 3 \
  --dataset.single_task "Pick up the object and place it in the tray" \
  --dataset.push_to_hub=false \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2 \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof
```

示例关闭自动上传，先保存在本地。进入录制阶段后手动完成动作，结束后回看：

```bash
lerobot-dataset-viz \
  --repo-id $HF_USER/am2_first_episode \
  --episode-index 0 \
  --display-compressed-images
```

检查每个相机视角是否正确、动作是否完整、画面是否有长时间冻结。这条短演示用于验证流程，不足以判断训练效果。

通过后再进入 [正式数据采集](learning.md)，收集一致的任务演示。入门至此完成。

```{raw} html
<p class="am-step-done">完成标志：已保存并回看第一条演示。</p>
```
::::
