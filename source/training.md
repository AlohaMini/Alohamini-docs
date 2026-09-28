# 策略训练

适用型号：**AlohaMini 2 / 2 Pro**。只执行与你的机器人型号对应的示例。

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


## 7. AM-ACT：移动任务与纯视觉训练

[Pro 快速入门](yuque/pro-quickstart.md) 给出了一套“右臂操作、左臂静止、底盘参与运动”的 AM-ACT 示例。AM-ACT 在 ACT 基础上支持固定动作维度、部分动作维度的离散分类，以及纯视觉输入。是否使用这些选项，取决于实际采集的任务。

### 7.1 先核对数据特征

1. 确认来自本机的 18 维整机数据，检查 `meta/info.json` 中的动作名称和顺序。
2. 确认哪些关节参与任务、哪些始终不动。不要因为示例固定了左臂，就对自己的双臂任务照搬。
3. 核对相机键。下例使用 `forward` 与 `wrist_right`；如果你的交付配置使用 `head_top`，应先检查数据集中实际的 `observation.images.*`。
4. 确认移动动作的单位、取值和统计分布，再考虑离散分类参数。

### 7.2 创建独立的纯视觉数据集

下面以 Pro 数据集为例。标准 2 同样可以使用转换工具，但源数据、目标目录和模型目录应保持独立。

```bash
python -m lerobot.scripts.create_alohamini_visual_only_dataset \
  --source "$HOME/user/am2pro_pick_place" \
  --target "$HOME/user/am2pro_pick_place_visual_only" \
  --keep-camera forward \
  --keep-camera wrist_right \
  --drop-state \
  --mode copy \
  --dry-run
```

先检查预览列出的保留相机和删除特征。确认后移除最后一行 `--dry-run`，同时移除它上一行末尾的续行符，再执行转换。

- `--source` 必须指向实际存在的 LeRobot v3 数据集。
- `--target` 必须是尚不存在的新目录。
- `--drop-state` 移除 `observation.state`，保留动作标签。AM-ACT 支持该输入方式，其他策略未必支持。
- `--mode copy` 使用独立文件副本；工具默认的自动模式会优先建立硬链接。
- 转换完成后再次检查目标数据集，确认图像、动作和 episode 数量符合预期。

### 7.3 从不固定动作维度的配置开始

以下示例先保留全部动作的连续回归，避免尚未核对数据就固定左臂或强行划分类别。步数和 batch size 是可调整的示例，不代表特定成功率。

```bash
lerobot-train \
  --dataset.repo_id=local/am2pro_pick_place_visual_only \
  --dataset.root="$HOME/user/am2pro_pick_place_visual_only" \
  --dataset.video_backend=pyav \
  --policy.type=am_act \
  --policy.device=cuda \
  --policy.fixed_action_dims='[]' \
  --policy.discrete_action_dims='[]' \
  --policy.push_to_hub=false \
  --save_checkpoint_to_hub=false \
  --output_dir=outputs/train/am_act_am2pro_pick_place \
  --job_name=am_act_am2pro_pick_place \
  --steps=100000 \
  --batch_size=2 \
  --wandb.enable=false
```

### 7.4 理解交付教程中的分类参数

| 参数 | 任务示例 | 使用条件 |
|---|---|---|
| `fixed_action_dims` | `[0,1,2,3,4,5,6]` | 该任务中左臂始终静止；这些维度不参与训练，在归一化空间输出零 |
| `discrete_action_dims` | `[14,15,16]` | 必须先核对数据特征顺序；此处用于二代底盘运动 |
| `discrete_action_values` | `[[-0.15,0,0.15],[-0.15,0,0.15],[-45,0,45]]` | 使用数据集的物理单位，与采集动作取值匹配 |
| `discrete_action_class_weights` | `[[3,1,1.5],[3,1,2],[2,1,2]]` | 每一组权重与该维度的类别顺序一一对应 |
| `discrete_action_loss_weight` | `1.0` | 分类损失的权重，需要结合实验调整 |

**归一化空间的零不等于物理关节角度零。** 不要把 `fixed_action_dims` 当作机械急停或硬件锁定机制。

如需采用上述离散设置，在训练命令中替换相应空列表，并补充类别与权重参数；先在少量数据上检查配置是否符合任务。

### 7.5 出现 `zero std` 怎么办

`Action dimension 15 has zero std and cannot be classified` 表示被选为离散分类的动作维度在统计中没有变化。任务示例中可能是采集时没有左右平移，但也应检查数据转换和维度选择是否正确。

1. 核对动作 15 对应的真实特征，而不是只按编号猜测。
2. 检查原始数据与统计信息，确认该维度是否恒定。
3. 任务需要这类运动时，补采包含相应动作的数据并重新生成统计。
4. 任务本来不需要这类运动时，重新设计离散维度和固定维度配置，保持类别列表长度一致。

不要直接修改统计数值来让报错消失。训练完成后按 [真机评估](evaluation.md) 使用实际生成的检查点，并保持机器人型号、相机名称与训练数据一致。

完整参数定义：[AM-ACT 参数说明](upstream/software--src-lerobot-policies-am_act-readme.md)。
