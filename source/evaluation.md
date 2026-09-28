# 真机评估

适用型号：**AlohaMini 2 / 2 Pro**。只执行与你的机器人型号对应的示例。

评估脚本读取策略检查点，根据当前观测生成动作，并保存评估数据。**本章命令会控制真实机器人。** 先确认遥操作正常，再用匹配的数据、模型与机型评估。

## 1. 评估前准备

1. 在 Pi 启动正确机型的 Host。
2. 停止遥操作、录制和其他命令客户端，释放控制权。
3. 核对策略来自哪种机器人、相机配置与任务。
4. 确认检查点目录实际存在，且文件完整。
5. 为本次评估准备新的 `dataset.repo_id`，设置场景起始状态。
6. 保持可以及时结束程序的操作位置，先做少量试验。

## 2. ACT 同步评估

**AlohaMini 2**

```bash
python examples/alohamini/evaluate_bi.py \
  --eval.n_episodes 3 \
  --fps 20 \
  --eval.episode_time_s 45 \
  --dataset.single_task "Pick up the object and place it in the tray" \
  --policy.path outputs/train/act_am2_pick_place/checkpoints/020000/pretrained_model \
  --dataset.repo_id $HF_USER/eval_act_am2_run01 \
  --dataset.push_to_hub=false \
  --robot.remote_ip <Pi_IP> \
  --robot.id my_alohamini \
  --robot.robot_model alohamini2 \
  --inference.type sync \
  --interpolation_multiplier 3
```

**AlohaMini 2 Pro**

```bash
python examples/alohamini/evaluate_bi.py \
  --eval.n_episodes 3 \
  --fps 20 \
  --eval.episode_time_s 45 \
  --dataset.single_task "Pick up the object and place it in the tray" \
  --policy.path outputs/train/act_am2pro_pick_place/checkpoints/020000/pretrained_model \
  --dataset.repo_id $HF_USER/eval_act_am2pro_run01 \
  --dataset.push_to_hub=false \
  --robot.remote_ip <Pi_IP> \
  --robot.id my_alohamini \
  --robot.robot_model alohamini2pro \
  --inference.type sync \
  --interpolation_multiplier 3
```

替换检查点步数和 Pi IP。`eval.n_episodes=3` 是示例试验次数，不是效果保证；每次试验之间按程序提示复位环境。

## 3. 理解评估参数

| 参数 | 说明 |
|---|---|
| `eval.n_episodes` | 本次评估的任务次数 |
| `eval.episode_time_s` | 单次评估时长 |
| `fps` | 评估循环的目标频率 |
| `policy.path` | 本地模型目录或入口支持的模型标识 |
| `dataset.single_task` | 本次执行的任务描述 |
| `dataset.repo_id` | 评估结果数据集标识，与训练数据分开 |
| `dataset.push_to_hub=false` | 仅保留本地评估数据 |
| `robot.id` | 机器人设备标识 |
| `robot.robot_model` | 与 Host 和模型对应的整机型号 |
| `inference.type` | `sync` 同步推理，或支持策略的 `rtc` |
| `interpolation_multiplier` | 动作插值倍数 |

首次使用某个结果标识时，目标数据目录应尚未存在。新一轮实验换成 `run02` 等新名称，保留上一轮结果用于比较。

### 插值频率不等于模型推理频率

示例中 20 Hz 与 3 倍插值对应在首个动作之后以目标 60 Hz 输出插值动作；这不会把模型本身变成每秒推理 60 次。实际执行还受推理耗时、网络与控制循环影响。

## 4. RTC 评估：仅限支持的策略

项目提供 SmolVLA 等支持 RTC 接口的策略示例。ACT 不支持这一 RTC 路径，应使用 `sync`。

已准备好兼容策略检查点时，评估命令的相关部分可改为：

```text
--inference.type rtc
--inference.rtc.execution_horizon 10
--inference.rtc.max_guidance_weight 10.0
--inference.rtc.queue_threshold 30
--interpolation_multiplier 1
```

其余机器人、模型路径与数据集参数仍然需要完整传入。RTC 使用后台推理与动作队列，策略必须提供所需的 action chunk 接口；不能通过单独更改参数让任意模型兼容。

## 5. 反馈过期或保护暂停

当前客户端要求用于发命令的完整反馈来自最近 250 ms 内发送的请求。同步推理结束后会刷新过期反馈，并丢弃推理前预取的旧响应。

**250 ms 是反馈新鲜度限制，不是模型推理必须完成的时限。** 但 Host 的看门狗仍然生效；看门狗事件、关节保护、Host 重启或控制权变化会暂停评估并丢弃动作队列，直到明确恢复。程序不会通过空心跳绕过看门狗。

遇到暂停，先查看 Host 与 PC 两边日志，确定是推理耗时、网络、设备保护还是控制权问题。不要直接把超时阈值增大作为第一步修复。

## 6. 记录结果与复盘

| 记录项 | 示例内容 |
|---|---|
| 数据与模型 | 数据集名称、检查点、训练配置 |
| 硬件 | 机型、相机布局、校准是否变更 |
| 场景 | 物体、起始位置、光照与背景 |
| 结果 | 是否完成目标、用时、人工干预情况 |
| 失败阶段 | 接近、抓取、搬运、放置或结束 |
| 运行异常 | 缺图、超时、保护触发、控制权变化 |

比较不同检查点时尽量保持同一套场景定义和成功标准。先区分运行问题与策略问题，再决定修复配置、补充演示或重新训练。
