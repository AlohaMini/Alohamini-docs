# 数据采集与检查

通过主臂示教，将相机图像、机器人状态与动作记录为数据集。先录制一条短测试并回看，再扩大到正式演示，能更早发现相机映射、任务描述或保存路径错误。

## 采集前准备

- Pi Host 正常运行，两端 `robot_model` 一致。
- 主臂校准完成，遥操作能够稳定完成任务。
- 已退出单独的遥操作客户端，避免争用控制权。
- 确认启用的相机名称、视角、帧率与分辨率。
- 在 PC 的当前终端设置 `HF_USER`，并准备足够的本地存储空间。

所有命令从 `lerobot_alohamini` 根目录运行：

```bash
conda activate lerobot_alohamini
export HF_USER="your-hf-username"
```

## 1. 先录制一条短测试

以下二代示例采集 1 条、每条 10 秒、10 FPS 的测试数据，仅保存到本地：

```bash
python examples/alohamini/record_bi.py \
  --dataset.repo_id $HF_USER/am2_smoke_test \
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

开始后按终端提示操作主臂，完成任务。记录日志打印的本地数据集路径；录制结束后等待数据保存完成，再回看图像与状态。

该测试用于检查整条采集链路。正式数据集应使用新名称，并采用实验计划中的固定采样配置。

## 2. 理解采集参数

| 参数 | 示例 | 说明 |
|---|---|---|
| `dataset.repo_id` | `用户名/am2_pick_place` | 数据集标识；不等同于本地目录 |
| `dataset.num_episodes` | `1` | 本次采集的 episode 数量 |
| `dataset.fps` | `30` | 数据集采样频率；单频录制器同时以此频率控制 |
| `dataset.episode_time_s` | `45` | 每条任务录制时间 |
| `dataset.reset_time_s` | `8` | 两条任务之间的场景复位时间 |
| `dataset.single_task` | 自然语言任务描述 | 保持与实际示教目标一致 |
| `dataset.push_to_hub` | `false` | 本地保存；默认脚本会上传，示例显式关闭 |
| `dataset.root` | 本地目录 | 可选；指定数据集创建或续录的位置 |
| `--resume` | 无值开关 | 在已有数据集上继续录制 |

**Episode** 是一次完整任务演示。复位阶段用来恢复物体和机器人起始条件；任务动作应发生在录制阶段。

## 3. 正式录制示例

确认短测试正常后，以 30 FPS、45 秒录制一条完整演示：

```bash
python examples/alohamini/record_bi.py \
  --dataset.repo_id $HF_USER/am2_pick_place \
  --dataset.num_episodes 1 \
  --dataset.fps 30 \
  --dataset.episode_time_s 45 \
  --dataset.reset_time_s 8 \
  --dataset.single_task "Pick up the object and place it in the tray" \
  --dataset.push_to_hub=false \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2 \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof
```

可按任务计划增大 `num_episodes`。本指南不设定一个保证训练成功的演示数量；先通过回看与小规模训练判断数据是否覆盖任务，再增加演示更容易定位改进方向。

Pro 将 `robot.robot_model` 改为 `alohamini2pro`。一代还需改用 SO 主臂 profile，并使用独立数据集名称，避免混入不同维度的数据。

## 4. 自定义目录与续录

需要固定本地位置时，在首次录制命令中增加：

```text
--dataset.root /absolute/path/to/am2_pick_place
```

续录时保留相同的 `repo_id`、`root`、机型、相机特征与采样配置，并在完整录制命令末尾增加：

```text
--resume
```

只传 `--resume` 不会自动选择你想要的数据集。误用新的路径会找不到原数据，误用已有但不兼容的数据集则可能产生特征不匹配；先核对日志中的路径再采集。

## 5. 选择单频或多频录制器

| 入口 | 控制与采样方式 | 适用情境 |
|---|---|---|
| `record_bi.py` | 控制与数据采样均使用 `dataset.fps` | 先跑通标准流程 |
| `record_bi_multirate.py` | 50 Hz 控制，按数据集频率提交新鲜且对齐的帧 | 需要把控制频率和相机采样分开 |

多频录制使用相同的主要参数，只需更换入口，例如：

```bash
python examples/alohamini/record_bi_multirate.py \
  --dataset.repo_id $HF_USER/am2_multirate_test \
  --dataset.num_episodes 1 \
  --dataset.fps 30 \
  --dataset.episode_time_s 45 \
  --dataset.reset_time_s 8 \
  --dataset.single_task "Pick up the object and place it in the tray" \
  --dataset.push_to_hub=false \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2 \
  --teleop.id am_leader_bi \
  --teleop.arm_profile am-leader-6dof
```

该录制器按目标帧数收集数据，所以实际相机若只有 29.5 Hz，墙钟录制时长可能略长于 30 FPS 对应的标称时间。当前文档列出的中止条件包括：相机停滞、多相机时间差超过 50 ms、状态对齐误差超过 100 ms，或新鲜帧率低于目标的 90%。遇到中止应检查日志中的具体原因，不用重复旧图像来凑帧数。

## 6. 回看数据集

默认数据位置下，查看第 0 条 episode：

```bash
lerobot-dataset-viz \
  --repo-id $HF_USER/am2_pick_place \
  --episode-index 0 \
  --display-compressed-images
```

可视化用于查看已录数据，不发送机器人动作。使用自定义目录时，在上面的完整可视化命令中增加 `--root /absolute/path/to/am2_pick_place`。注意可视化工具使用 `--root`，录制脚本使用 `--dataset.root`。

### 每批数据检查什么

| 检查项 | 具体查看 |
|---|---|
| 相机名称与视角 | 左右腕没有接反，任务物体在所需视野内 |
| 画面连续性 | 没有长时间冻结、黑屏或错误占位图 |
| 动作完整性 | 包含接近、抓取、搬运与放置等任务阶段 |
| 状态与动作 | 没有因型号错误造成缺失维度或异常跳变 |
| 任务文本 | 描述与本条示教的实际目标一致 |
| 复位 | 起始场景可复现，没有把复位动作误录成任务 |

建议建立采集记录：日期、机型、软件版本、相机配置、任务文本、成功与失败片段、现场改动。出现训练问题时可追溯数据来自哪一次配置。

## 7. 在真机回放

**回放会驱动真实机器人。** 先检查动作轨迹、初始位置与周围空间，启动匹配机型的 Host，再在 PC 上运行：

```bash
python examples/alohamini/replay_bi.py \
  --dataset.repo_id $HF_USER/am2_pick_place \
  --dataset.episode 0 \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2
```

使用自定义录制目录时，补上同一 `--dataset.root /absolute/path/to/am2_pick_place`。若只是检查数据内容，使用上一节的可视化即可。

## 下一步

数据回看通过后进入 [ACT 策略训练](training.md)，训练结果再用 [真机评估](evaluation.md) 验证。

来源：[采集工作流](https://github.com/liyiteng/lerobot_alohamini/blob/main/docs/alohamini/alohamini.md)、[多频采集说明](https://github.com/liyiteng/lerobot_alohamini/blob/main/docs/alohamini/commands.md)。
