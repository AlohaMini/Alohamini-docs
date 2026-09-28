# 策略训练

适用型号：**AlohaMini 2 / 2 Pro**。标注型号的两组示例请选择一组执行。完整入门流程：[2 教程](alohamini2.md) · [2 Pro 教程](alohamini2pro.md)。

本章以项目提供的 **ACT** 训练入口为起点。训练读取已保存的数据集，不需要机器人 Host 或主臂持续在线。

## 1. 训练前核对

- 已完成 [数据回看](learning.md)，任务、动作与相机数据完整。
- 训练机器安装了相同软件环境，能找到数据集。
- 数据来自匹配的机器人配置；一代为 16 维接口，二代与 Pro 为 18 维接口。
- 当前终端设置了正确的 `HF_USER`。
- 使用 CUDA 示例时，GPU 与 PyTorch CUDA 环境可用。

```bash
python -c "import torch; print(torch.cuda.is_available())"
```

这只验证 CUDA 可访问，不保证特定 batch size 或策略一定能在显存中运行。

## 2. 启动 ACT 训练

以下示例读取前一章的数据集，模型输出到独立目录，关闭 W&B 和模型上传：

**AlohaMini 2**

```bash
lerobot-train \
  --dataset.repo_id=$HF_USER/am2_pick_place \
  --policy.type=act \
  --output_dir=outputs/train/act_am2_pick_place \
  --job_name=act_am2_pick_place \
  --policy.device=cuda \
  --policy.push_to_hub=false \
  --wandb.enable=false \
  --dataset.video_backend=pyav
```

**AlohaMini 2 Pro**

```bash
lerobot-train \
  --dataset.repo_id=$HF_USER/am2pro_pick_place \
  --policy.type=act \
  --output_dir=outputs/train/act_am2pro_pick_place \
  --job_name=act_am2pro_pick_place \
  --policy.device=cuda \
  --policy.push_to_hub=false \
  --wandb.enable=false \
  --dataset.video_backend=pyav
```

如果录制时指定了本地数据目录，增加：

**AlohaMini 2**

```text
--dataset.root=/absolute/path/to/am2_pick_place
```

**AlohaMini 2 Pro**

```text
--dataset.root=/absolute/path/to/am2pro_pick_place
```

使用自定义路径时不要误把 `repo_id` 改成本地目录；这两个字段负责不同用途。

## 3. 参数说明

| 参数 | 作用 | 调整时注意 |
|---|---|---|
| `dataset.repo_id` | 标识训练数据集 | 必须与实际数据对应 |
| `dataset.root` | 指向本地数据目录 | 跨机器训练时确认数据已复制完整 |
| `policy.type=act` | 使用 ACT 策略 | 更换策略会改变模型与依赖需求 |
| `policy.device=cuda` | 在 CUDA 设备上训练 | 需要对应运行环境 |
| `output_dir` | 检查点与训练产物目录 | 新实验使用新目录，避免混淆结果 |
| `job_name` | 实验名称 | 建议包含任务或配置差异 |
| `policy.push_to_hub=false` | 关闭模型上传 | 训练完成仍保留本地检查点 |
| `wandb.enable=false` | 关闭 W&B 日志集成 | 不影响本地训练输出 |
| `dataset.video_backend=pyav` | 使用 PyAV 视频解码 | 解码报错先检查数据视频与依赖 |

训练命令读取数据集特征，无需增加 `robot.robot_model` 参数。两款示例分别读取对应数据，使用独立模型目录；18 维接口相同不代表策略可以直接跨机型部署。

本示例沿用策略的训练预设，不额外给出未经本任务验证的学习率、步数或成功率。需要调整训练超参数时，以当前训练入口和策略配置为准，并记录改动。

## 4. 找到可评估的检查点

项目示例采用以下路径结构：

**AlohaMini 2**

```text
outputs/train/act_am2_pick_place/
└── checkpoints/
    └── 020000/
        └── pretrained_model/
```

**AlohaMini 2 Pro**

```text
outputs/train/act_am2pro_pick_place/
└── checkpoints/
    └── 020000/
        └── pretrained_model/
```

`020000` 只是示例步数。请查看实际输出，选择已经保存完整的 `pretrained_model` 目录，再传给评估脚本。不要复制一个尚未生成的示例路径。

训练中断后若要恢复，查看当前 `lerobot-train --help` 与软件仓库恢复训练说明。**训练恢复参数与数据集续录的 `--resume` 不是同一条工作流。** 不要直接删除已有输出目录来绕过错误。

## 5. 上传与跨机器训练

需要上传模型时，先完成 Hugging Face 登录，并在训练配置中使用：

```text
--policy.push_to_hub=true
--policy.repo_id=你的用户名/模型名称
```

数据集和策略模型是不同的仓库。把录制数据复制到另一台训练机器时，保持视频、元数据和数值数据一起迁移；训练结束后再把完整的模型目录带回评估机器。

## 6. 如何判断下一轮改进方向

| 观察结果 | 优先检查 |
|---|---|
| 训练启动即报特征维度错误 | 数据集机型、相机名称、state/action 特征 |
| 视频无法解码 | 数据是否保存完整、PyAV 与 FFmpeg 环境 |
| 显存不足 | 当前策略、batch size、图像配置与设备显存 |
| 训练能完成，但真机动作不对 | 校准、预处理、机型与评估场景 |
| 只在少数物体位置成功 | 示教是否覆盖任务实际变化 |
| 抓取成功但后续放置失败 | 数据中完整任务链条与末段演示质量 |

训练 loss 下降只能说明优化过程中的一个指标，任务效果要通过 [真机评估](evaluation.md) 检查。记录失败阶段，再决定补数据或调整训练配置。

来源：[ACT 训练示例](https://github.com/liyiteng/lerobot_alohamini/blob/main/docs/alohamini/commands.md)、[训练配置](https://github.com/liyiteng/lerobot_alohamini/blob/main/src/lerobot/configs/train.py)。
