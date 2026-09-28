# 软件安装

AlohaMini 的整机控制、校准、遥操作和数据工作流统一使用 [lerobot_alohamini](https://github.com/liyiteng/lerobot_alohamini)。本指南采用项目文档中的 Linux + Python 3.12 + Conda 路径。

## 先理解两端分工

| 设备 | 连接的硬件 | 运行的任务 |
|---|---|---|
| 机器人端 Host | 双从臂、底盘、升降与摄像头；通常为树莓派 5 | 读取状态和图像，接收控制命令，执行保护逻辑 |
| 电脑端 Client | 双主臂与键盘 | 遥操作、录制、回放、策略评估 |
| 训练机器 | 已采集的数据集 | 训练策略；可与电脑端为同一台机器 |

PC 与树莓派需要分别安装软件，并处于能够互相访问的网络中。下文中标注“PC”或“Pi”的步骤，只在对应设备执行；克隆和安装依赖则两端都需要。

## 1. 准备 Python 环境管理器

已经安装 Conda 或 Miniforge 时，直接进入下一节。下面是原始安装指南针对两种 Linux 架构的示例。

### PC：Linux x86_64

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
~/miniconda3/bin/conda init bash
source ~/.bashrc
```

### 树莓派：Linux ARM64

先确认系统为 64 位 ARM；以下安装包不是 x86_64 版本。

```bash
mkdir -p ~/miniforge3
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-aarch64.sh -O ~/miniforge3/miniforge.sh
bash ~/miniforge3/miniforge.sh -b -u -p ~/miniforge3
~/miniforge3/bin/conda init bash
source ~/.bashrc
```

以上初始化命令面向 Bash。如果使用其他 shell，使用对应的 Conda 初始化方式后重新打开终端。

## 2. 获取代码并安装依赖

在 PC 和 Pi 上分别执行：

```bash
git clone https://github.com/liyiteng/lerobot_alohamini.git
cd lerobot_alohamini
conda create -y -n lerobot_alohamini python=3.12
conda activate lerobot_alohamini
pip install -e ".[all]"
pip install pyzmq feetech-servo-sdk
conda install -y ffmpeg=7.1.1 -c conda-forge
```

| 命令／依赖 | 用途 |
|---|---|
| 独立 Conda 环境 | 避免与系统 Python 或其他项目依赖混用 |
| `pip install -e ".[all]"` | 按项目完整安装方案安装，并让本地代码改动生效 |
| `pyzmq` | PC 与 Host 之间的通信 |
| `feetech-servo-sdk` | 飞特总线舵机访问 |
| FFmpeg | 数据视频的编码与处理 |

完整依赖安装可能涉及较大的机器学习包。若特定平台出现依赖不支持的错误，保留完整错误与设备架构，参考软件仓库对应版本处理，不应直接跳过报错后继续控制机器人。

开发者也可使用项目提供的 `uv sync --locked` 工作流；一套环境选择一种管理方式，避免在同一次排错中混用不同解释器。

## 3. 配置串口权限

在连接了控制板的 Linux 设备上执行：

```bash
sudo usermod -a -G dialout $USER
```

重新登录或重启后，新的用户组权限才会应用。PC 的主臂控制板和 Pi 的从臂控制板都需要各自检查权限。

## 4. 验证环境

激活环境后执行：

```bash
python --version
python -c "import av, cv2, torch; print('av', av.__version__); print('cv2', cv2.__version__); print('torch', torch.__version__)"
ffmpeg -version
lerobot-find-cameras --help
```

确认 Python 版本、依赖导入和命令入口正常。训练机器还可检查：

```bash
python -c "import torch; print('CUDA available:', torch.cuda.is_available())"
```

树莓派用于 Host 控制时，不需要通过 CUDA 检查；训练章节中的 `--policy.device=cuda` 则要求相应 GPU 环境已经可用。

## 5. 设置数据集命名空间

数据集使用 `用户名/数据集名` 形式。每个用于采集、训练或评估的新终端先设置：

```bash
export HF_USER="your-hf-username"
```

把 `your-hf-username` 替换为自己的 Hugging Face 用户名。需要上传数据或模型时再登录：

```bash
hf auth login
hf auth whoami
```

按交互提示完成登录。后续入门录制和训练示例显式关闭上传，方便先验证本地流程。`repo_id` 仍用于标识数据集，`root` 才是可选的本地目录。

## 6. 每次重新打开终端

```bash
cd /path/to/lerobot_alohamini
conda activate lerobot_alohamini
export HF_USER="your-hf-username"
```

`/path/to/lerobot_alohamini` 替换为自己的仓库路径。本手册所有 `python examples/...` 命令均从该软件仓库根目录运行，OpenPI 专题中会另行注明例外。

## 下一步

进入 [设备配置](configuration.md)，固定左右臂端口、确认相机视角，然后 [校准](calibration.md)。PC 与 Host 应使用彼此兼容的同版软件，尤其是控制会话和反馈协议更新后。
