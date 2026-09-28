# 仿真数据生成与转换

本页对应软件仓库的 `alohamini_sim/`，与 [一代 ROS 2 可视化](simulation.md) 是两套用途不同的流程。前者生成场景和数据，后者查看 URDF 与关节结构。

## 1. 先理解三个环节

| 环节 | 输入与输出 | 运行环境 |
|---|---|---|
| video2sim | 手机视频 → 场景外观、碰撞体与 Isaac USD | 独立 GPU 工具链 |
| 数据引擎 | 任务、机器人和环境 → episode 字典 | ManiSkill / SAPIEN 等执行环境 |
| LeRobot bridge | episode 字典 → LeRobotDataset v3 | `lerobot_alohamini` 的 uv 环境 |

场景重建完成不会自动生成抓取演示。需要在数据引擎里准备任务、控制器、技能和相机，生成轨迹，再交给 bridge 转换。

## 2. 当前机器人与维度限制

```{important}
当前 `lerobot_bridge.py` 使用 `SIM_ARM_PROFILE = "so-arm-5dof"`，输出 **16 维** state/action。输入仿真 `qpos` 的 18 个值不等于 AlohaMini 2 / 2 Pro 的 18 维接口。它不能直接作为二代整机的混合训练数据。
```

| 数据 | 原始含义 | 转换后 |
|---|---|---|
| `qpos` | 18 维仿真状态 | 取对应关节、夹爪、底盘与升降，生成 16 维状态 |
| `action` | 16 维控制目标 | 转换为 16 维动作 |
| 双臂关节 | 弧度 | 当前保持原值，需要自行与真机归一化或角度语义对齐 |
| 夹爪 | 指关节位移，单位米 | 默认保留；可用闭合/张开范围转换到 0–100 |
| 底盘 x/y | 世界坐标位置或目标 | 转为机体坐标系速度，单位 m/s |
| 底盘旋转 | yaw 或目标角度 | 转为角速度，单位 deg/s |
| 升降 | 米 | 转为毫米 |

即使特征名称相同，也要检查单位、夹爪范围、相机、动作时序和校准。输出数据集可被读取，仅说明格式成立。

## 3. 准备执行环境和模型资产

数据引擎目录包含 `aspire_engine`、`intern_engine` 和机器人 agent。执行 rollout 需要外部 ManiSkill、SAPIEN、Torch、GPU 与 Vulkan；本站的软件安装环境不自动具备这些条件。

原文提到的 `aloha_mini_pro_v2.urdf`、`aloha_mini_pro_v3.urdf`、`maniskill_so100_version.urdf` 在本次固定提交中未找到。先补齐与 agent 匹配的模型及网格；必要时通过 `ALOHAMINI_URDF_DIR` 指定模型目录。不要把“Pro”文件名直接等同于当前 2 Pro 的 AM 从臂配置。

技能组织、触发和元数据见 [技能库原文](upstream/software--alohamini_sim-data_engine-data_gen-intern_engine-skills-library-readme.md)。该资料没有提供适用于所有任务的一条生成命令，应按实际环境注册与任务定义配置执行器。

## 4. 准备 bridge 环境

在软件仓库根目录运行：

```bash
uv sync --locked --extra test --extra dataset
uv run pytest tests/test_alohamini_sim_bridge.py tests/test_alohamini_sim_engine_imports.py -svv
```

这些测试用小型合成 episode 检查转换、特征和读写。没有安装 ManiSkill 时，执行器导入测试可能跳过；这不代表真实仿真 rollout 已验证。

## 5. 核对 episode 结构

```python
episode = {
    "steps": [
        {
            "qpos": qpos,       # float32[18]
            "action": action,   # float32[16]
            "rgb": {"front": image},  # uint8[H, W, 3]，RGB
        }
    ],
    "annotation": "Pick up the object and place it in the tray",
}
```

上面是结构示意，`qpos`、`action`、`image` 需由引擎提供真实数组。同一个数据集中的相机名称、分辨率和字段要一致，FPS 与生成轨迹的时间间隔保持一致。

## 6. 转成 LeRobotDataset

将自己生成的可信 episode 保存为列表形式的 pickle 文件后，在软件仓库根目录执行：

```bash
uv run python -m alohamini_sim.data_engine.lerobot_bridge \
  --episodes out/episodes.pkl \
  --repo-id local/alohamini_sim_pick \
  --root out/lerobot_ds \
  --fps 20
```

pickle 会在加载时执行对象反序列化，只读取你自己生成或确认可信的文件。`root` 指向本次输出位置，不要覆盖已有实验。

也可以在同一环境中调用：

```python
from alohamini_sim.data_engine.lerobot_bridge import write_episodes

write_episodes(
    episodes,
    repo_id="local/alohamini_sim_pick",
    root="out/lerobot_ds",
    fps=20,
)
```

仿真种子、技能 traces、command 和 final 等信息不会全部写入 LeRobot 标准字段；保留引擎原始结果，便于复现与排错。

## 7. 转换后的检查

```bash
uv run lerobot-dataset-viz \
  --repo-id local/alohamini_sim_pick \
  --root out/lerobot_ds \
  --episode-index 0 \
  --display-compressed-images
```

逐项检查任务描述、帧数、相机颜色、动作连续性、关节顺序和单位。若目标是二代混训，需要先完成桥接器的 18 维适配，并验证真机校准映射；单纯修改 `robot_type` 标签不会改变数据结构。

来源：[仿真工作流全文](upstream/software--alohamini_sim-readme.md)、[bridge 源码](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/alohamini_sim/data_engine/lerobot_bridge.py)。
