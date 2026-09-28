# Software installation

AlohaMini's overall machine control, calibration, teleoperation and data workflow use [lerobot_alohamini](https://github.com/liyiteng/lerobot_alohamini). This guide uses the Linux + Python 3.12 + Conda path from the project documentation.

## First understand the division of labor between the two ends

| Equipment | Connected hardware | Tasks to run |
| --- | --- | --- |
| Robot Host | Dual follower arms, chassis, lift and camera; typically Raspberry Pi 5 | Read status and images, receive control commands, and execute protection logic |
| PC Client | Double leader arms and keyboard | teleoperation, recording, playback, policy evaluation |
| training machine | Collected data set | Training policy; can be on the same machine as the computer |

The PC and Raspberry Pi need to install software separately and be on a network that can access each other. The steps marked "PC" or "Pi" below are only performed on the corresponding device; cloning and installing dependencies are required on both ends.

## 1. Prepare the Python environment manager

When Conda or Miniforge is already installed, proceed directly to the next section. Below are examples from the original installation guide for two Linux architectures.

### PC：Linux x86_64

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
~/miniconda3/bin/conda init bash
source ~/.bashrc
```

### Raspberry Pi: Linux ARM64

First confirm that the system is 64-bit ARM; the following installation package is not the x86_64 version.

```bash
mkdir -p ~/miniforge3
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-aarch64.sh -O ~/miniforge3/miniforge.sh
bash ~/miniforge3/miniforge.sh -b -u -p ~/miniforge3
~/miniforge3/bin/conda init bash
source ~/.bashrc
```

The above initialization commands are for Bash. If you use another shell, use the corresponding Conda initialization method and then reopen the terminal.

## 2. Get the code and install dependencies

Execute on PC and Pi respectively:

```bash
git clone https://github.com/liyiteng/lerobot_alohamini.git
cd lerobot_alohamini
conda create -y -n lerobot_alohamini python=3.12
conda activate lerobot_alohamini
pip install -e ".[all]"
pip install pyzmq feetech-servo-sdk
conda install -y ffmpeg=7.1.1 -c conda-forge
```

| Commands/Dependencies | Purpose |
| --- | --- |
| Standalone Conda environment | Avoid mixing with system Python or other project dependencies |
| `pip install -e ".[all]"` | Install according to the project's complete installation plan and allow local code changes to take effect |
| `pyzmq` | Communication between PC and Host |
| `feetech-servo-sdk` | Feite bus servo access |
| FFmpeg | Data video encoding and processing |

Full dependency installation may involve larger machine learning packages. If there is an error that a dependency is not supported on a specific platform, keep the complete error and device architecture, and refer to the corresponding version of the software repository for processing. You should not directly skip the error report and continue to control the robot.

Developers can also use the `uv sync --locked` workflow provided by the project; choose a management method for a set of environments to avoid mixing different interpreters in the same debugging.

## 3. Configure serial port permissions

On a Linux machine with the control board connected, execute:

```bash
sudo usermod -a -G dialout $USER
```

The new user group permissions will not be applied until you log in again or restart. Both the PC's master control board and the Pi's slave control board need to check permissions individually.

## 4. Verification environment

After activating the environment, execute:

```bash
python --version
python -c "import av, cv2, torch; print('av', av.__version__); print('cv2', cv2.__version__); print('torch', torch.__version__)"
ffmpeg -version
lerobot-find-cameras --help
```

Confirm that the Python version, dependency imports and command entries are normal. Training machines can also check:

```bash
python -c "import torch; print('CUDA available:', torch.cuda.is_available())"
```

When the Raspberry Pi is used for Host control, it does not need to pass the CUDA check; `--policy.device=cuda` in the training chapter requires that the corresponding GPU environment is already available.

## 5. Set the dataset namespace

The data set uses the form `用户名/数据集名`. Each new terminal used for acquisition, training, or evaluation first sets up:

```bash
export HF_USER="your-hf-username"
```

Replace `your-hf-username` with your Hugging Face username. Log in again when you need to upload data or models:

```bash
hf auth login
hf auth whoami
```

Follow the interactive prompts to complete the login. Subsequent introductory recording and training examples explicitly turn off uploading to facilitate verification of the local process first. `repo_id` is still used to identify the data set, and `root` is the optional local directory.

## 6. Reopen the terminal every time

```bash
cd /path/to/lerobot_alohamini
conda activate lerobot_alohamini
export HF_USER="your-hf-username"
```

Replace `/path/to/lerobot_alohamini` with your own warehouse path. All `python examples/...` commands in this manual are run from the root directory of this software repository, with exceptions noted in the OpenPI topic.

## Next step

Enter [Device configuration](configuration.md), fix the left and right arm ports, confirm the camera angle, and then [Calibration](calibration.md). PC and Host should use the same version of software that is compatible with each other, especially after the control session and feedback protocol are updated.
