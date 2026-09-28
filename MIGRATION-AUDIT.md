# 上游教程迁移核查

核查日期：2026-09-28。本文件记录迁移前的来源范围与兼容性问题，不把文档收录等同于硬件、训练或仿真验证通过。

> 实际迁入范围以 `upstream-manifest.json` 为准：在下面审计建议基础上，增加 `CONTRIBUTING.md` 正文及其 `docs/source/contributing.md` 别名，最终为 **127 篇正文、26 个别名、9 个排除项**。下表保留迁移前的审计口径。

## 来源与覆盖口径

通过 GitHub API 读取两个仓库的 `main` 提交，均与本地源仓库一致：

- 硬件仓库：[`17c6a98`](https://github.com/liyiteng/AlohaMini/tree/17c6a98d79881a45ab869c1f392ed89c0723a298)。
- 软件仓库：[`7843e588`](https://github.com/liyiteng/lerobot_alohamini/tree/7843e5888366eaa553630e2f9d5539505a62dddf)。

清单由 `git ls-files '*.md' '*.mdx' '*.rst'` 得到，避免把硬件仓库中未跟踪的旧 `website/` 当成上游教程。

| 范围 | 原始文档路径 | 排除治理/模板 | 去重的别名 | 唯一正文 |
|---|---:|---:|---:|---:|
| AlohaMini | 13 | 0 | 0 | 13 |
| lerobot_alohamini | 149 | 11 | 25 | 113 |
| 合计 | 162 | 11 | 25 | 126 |

软件仓库的 149 个路径由 65 个 `.md` 和 84 个 `.mdx` 组成；84 个 MDX 中 4 个为机器人文档别名。不能只扫描 Markdown 后缀而漏掉 Hugging Face MDX 教程。

建议：126 篇正文全部收录，25 个符号链接记录其规范来源；原文下载、哈希和固定提交来源并存。AlohaMini 教程提供中文阅读主线，其他机器人与通用 LeRobot 内容归入拓展参考并标注适用范围。英文原文收录不能宣称为完整中文翻译。

`AGENT_GUIDE.md` 虽含面向 agent 的文字，也含用户使用教程，因此纳入资料清单；其强制问答等内容作为原文展示，不作为本次任务指令。治理、许可、模板单独保留必要归属，不混入教程。

## 迁移前网站缺口

已有网站覆盖标准 2 BOM/打印/装配、2/2 Pro 入门、安装配置校准遥操作、采集 ACT 训练评估和少量进阶说明。缺口包括：一代完整硬件教程、单臂独立评估、完整调试命令、AM-ACT、OpenPI 原始配置、Isaac/ManiSkill 数据链、video2sim、Docker、通用 LeRobot 策略/数据/开发教程、其他机器人示例。检查范围为本地 `source/` 中 24 篇 Markdown；其中一些页面仅引用上游链接，不能算正文已迁入。

## 操作兼容性：必须在中文入口说明

### 仿真数据不是二代真机的 18 维数据

桥接器输入 qpos 为 18 维、控制目标为 16 维，但输出 observation.state/action 均为 16 维，SIM_ARM_PROFILE 为 so-arm-5dof。臂角度仍是弧度，真机归一化与标定对齐由调用者完成；夹爪可选映射 0–100。相同 LeRobotDataset v3 格式不代表可直接与 2/2 Pro 数据混训。

来源：[alohamini_sim/data_engine/lerobot_bridge.py](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/alohamini_sim/data_engine/lerobot_bridge.py)。

### ManiSkill 所需 URDF 未随当前提交提供

git ls-files 的固定提交中没有任何 URDF；agent 引用 aloha_mini_pro_v2.urdf、aloha_mini_pro_v3.urdf、maniskill_so100_version.urdf。resolve_urdf 搜索 ALOHAMINI_URDF_DIR、包内 assets、旧 ~/.maniskill/data/robots/aloha_mini。已有 meshes 不等于完整模型。需要用户自行取得匹配模型并配置路径。

来源：[alohamini_sim/data_engine/agents/aloha_mini/base_agent.py](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/alohamini_sim/data_engine/agents/aloha_mini/base_agent.py)；[alohamini_sim/README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/alohamini_sim/README.md)。

### video2sim 有实现，但原教程工作目录需更新

模块实际位于 alohamini_sim/video2sim/video2sim/，应从 alohamini_sim/video2sim 运行 python -m video2sim。原教程 /home/perelman/AlohaMini/video2sim 和三个解释器路径为作者机器配置。外部 LingBot 分支、权重、3dgrut/NuRec/Isaac 环境仍需准备；仓库的普通 uv 环境不能替代这些环境。

来源：[alohamini_sim/video2sim/README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/alohamini_sim/video2sim/README.md)；[alohamini_sim/video2sim/video2sim/cli.py](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/alohamini_sim/video2sim/video2sim/cli.py)。

### video2sim 默认不生成最终 scene.usd

cli.DEFAULT_UNTIL 为 scene_prep；必须显式 --until scene 或 --gui 才执行 scene 阶段。README 中默认一条命令输出 scene/scene.usd 的概括不能作为当前保证。

来源：[alohamini_sim/video2sim/video2sim/cli.py](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/alohamini_sim/video2sim/video2sim/cli.py)。

### video2sim 配置格式要与代码一致

runner 参数覆盖读取 main_python/nurec_python/isaac_python 等顶层键和 stage_args。configs/default.yaml 的 extract/train 等顶层字段为参数记录，与 runner 的 stage_args 覆盖格式不同。check_env 独立接受 --main-python、--nurec-python、--isaac-python、--lingbot-repo、--model 等；不要假设它读取同一 YAML。

来源：[alohamini_sim/video2sim/video2sim/cli.py](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/alohamini_sim/video2sim/video2sim/cli.py)；[alohamini_sim/video2sim/video2sim/check_env.py](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/alohamini_sim/video2sim/video2sim/check_env.py)。

### video2sim 模型路径也要确认

README 中的 assets/am2pro_parallel/alohamini2pro_parallel.urdf 未在该提交跟踪；scene.py 实际默认加载同目录已提供的 alohamini2pro_parallel.usd，因此缺 URDF 不直接阻断该场景组装入口。需要 URDF 的后续流程需另外补齐；ManiSkill 与 Isaac 模型关节命名不同，不能直接互换。

来源：[alohamini_sim/video2sim/video2sim/scene.py](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/alohamini_sim/video2sim/video2sim/scene.py)；[alohamini_sim/README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/alohamini_sim/README.md)。

### 资源与性能数字是上游测试条件

video2sim 的 8 GiB 显存、32 GB 内存、约 20 分钟训练等来自作者 RTX 4060/room3 样例，不能作为任意房间、机器的承诺。GPU 独占、frame stride、同一轨迹位姿与深度、SH3 导出均与该流程有关。迁入全文时保留上下文。

来源：[alohamini_sim/video2sim/README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/alohamini_sim/video2sim/README.md)。

### Docker 预构建镜像未保证包含 AlohaMini fork

原 README 镜像为 huggingface/lerobot-cpu 与 -gpu。它们是通用 LeRobot 上游镜像，不能据此保证含此 fork 的 AlohaMini/AM-ACT 改动。要运行 fork 功能，应从当前 checkout 构建并核对导入/命令。CPU 镜像无 CUDA；GPU 使用 NVIDIA runtime，数据与输出需挂载保存。

来源：[docker/README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docker/README.md)；[docker/Dockerfile.user](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docker/Dockerfile.user)；[docker/Dockerfile.internal](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docker/Dockerfile.internal)。

### AM-ACT 索引与物理单位不能照搬

am_act 已在工厂和配置注册；原 README 的 discrete_action_dims=[14,15,16] 对应示例数据，分类值及权重需与实际数据的字段顺序/单位匹配。fixed_action_dims 在归一化空间归零，不代表真实电机物理零位。策略 README 的 lerobot_eval 示例是仿真环境入口，真机使用机器人匹配的评估入口。

来源：[src/lerobot/policies/am_act/README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/src/lerobot/policies/am_act/README.md)；[src/lerobot/policies/factory.py](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/src/lerobot/policies/factory.py)。

### Isaac Teleop 教程适用 SO-101/SO-100

XR 路径依赖 Linux Isaac Teleop、CloudXR、IK、特定关节模型与标定；leader 路径依赖已编译插件。不能通过替换 robot.type 就声称已支持 AlohaMini 双臂或 AM-ARM200 关节链。录制示例继承标准数据参数，发布行为需明确。

来源：[examples/isaac_teleop_to_so101/README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/examples/isaac_teleop_to_so101/README.md)；[docs/source/isaac_teleop.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/isaac_teleop.mdx)。

### OMX 是另一台机器人且自动动作针对固定装置

OMX README 自述 WIP、内部装置专用。自动采集/复位使用写死动作与工作空间，不能映射到 AlohaMini 直接执行；push_to_hub=true 和 sentry 自动上传需在介绍中说清。

来源：[examples/omx/README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/examples/omx/README.md)。

### RTC 不是另一种策略，也不默认适用于 ACT

RTC 原文明确是 flow-matching 策略的推理机制（Pi0/Pi05/SmolVLA 等）。不要给 ACT/AM-ACT 教程统一添加 RTC 参数。

来源：[docs/source/policy_rtc_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_rtc_README.md)。

### 旧调试脚本配置与 2/Pro 不一致

examples/debug 的 wheels/axis 为旧设备配置，尤其 axis 的 STS3215 与二代 STS3095 不同。官方中文步骤应先说明适用型号、旧示例默认值，控制底盘/升降优先使用机型配置驱动入口。

来源：[examples/debug/README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/examples/debug/README.md)；[examples/debug/axis.py](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/examples/debug/axis.py)；[examples/debug/wheels.py](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/examples/debug/wheels.py)。

### OpenPI 适配与当前机器人接口不一致

硬件示例 README 引用 scripts/serve_policy_http.py，但该文件未提供；客户端还引用旧 LeKiwi 接口。相机映射、16/18 维适配、动作增量掩码均需匹配实际版本。迁入原文与完整配置，并将部署标为需完成兼容适配。

来源：[examples/pi0.5_openpi/README.md](https://github.com/liyiteng/AlohaMini/blob/17c6a98d79881a45ab869c1f392ed89c0723a298/examples/pi0.5_openpi/README.md)；[examples/pi0.5_openpi/evaluate_bi.py](https://github.com/liyiteng/AlohaMini/blob/17c6a98d79881a45ab869c1f392ed89c0723a298/examples/pi0.5_openpi/evaluate_bi.py)。

### 旧 ROS 1 文字不等于当前可构建

一代 simulation README 包含 ROS 1/2 描述，当前包使用 ament_cmake；保留 ROS 1 launch 文件不能证明 catkin_make 当前可用。

来源：[AlohaMini1/simulation/README.md](https://github.com/liyiteng/AlohaMini/blob/17c6a98d79881a45ab869c1f392ed89c0723a298/AlohaMini1/simulation/README.md)；[AlohaMini1/simulation/src/Aloha/CMakeLists.txt](https://github.com/liyiteng/AlohaMini/blob/17c6a98d79881a45ab869c1f392ed89c0723a298/AlohaMini1/simulation/src/Aloha/CMakeLists.txt)。

## 全量正文清单

以下全部建议迁入；按原目录分组可保持清单可复核。

### AlohaMini

- [AlohaMini1/README.md](https://github.com/liyiteng/AlohaMini/blob/17c6a98d79881a45ab869c1f392ed89c0723a298/AlohaMini1/README.md)
- [AlohaMini1/docs/BOM.md](https://github.com/liyiteng/AlohaMini/blob/17c6a98d79881a45ab869c1f392ed89c0723a298/AlohaMini1/docs/BOM.md)
- [AlohaMini1/docs/hardware_assembly.md](https://github.com/liyiteng/AlohaMini/blob/17c6a98d79881a45ab869c1f392ed89c0723a298/AlohaMini1/docs/hardware_assembly.md)
- [AlohaMini1/docs/software_setup.md](https://github.com/liyiteng/AlohaMini/blob/17c6a98d79881a45ab869c1f392ed89c0723a298/AlohaMini1/docs/software_setup.md)
- [AlohaMini1/hardware/arms/README.md](https://github.com/liyiteng/AlohaMini/blob/17c6a98d79881a45ab869c1f392ed89c0723a298/AlohaMini1/hardware/arms/README.md)
- [AlohaMini1/simulation/README.md](https://github.com/liyiteng/AlohaMini/blob/17c6a98d79881a45ab869c1f392ed89c0723a298/AlohaMini1/simulation/README.md)
- [AlohaMini2/docs/BOM.md](https://github.com/liyiteng/AlohaMini/blob/17c6a98d79881a45ab869c1f392ed89c0723a298/AlohaMini2/docs/BOM.md)
- [AlohaMini2/docs/assembly_guide.md](https://github.com/liyiteng/AlohaMini/blob/17c6a98d79881a45ab869c1f392ed89c0723a298/AlohaMini2/docs/assembly_guide.md)
- [AlohaMini2/docs/print_guide.md](https://github.com/liyiteng/AlohaMini/blob/17c6a98d79881a45ab869c1f392ed89c0723a298/AlohaMini2/docs/print_guide.md)
- [AlohaMini2/hardware/am_arm200/README.md](https://github.com/liyiteng/AlohaMini/blob/17c6a98d79881a45ab869c1f392ed89c0723a298/AlohaMini2/hardware/am_arm200/README.md)
- [README.md](https://github.com/liyiteng/AlohaMini/blob/17c6a98d79881a45ab869c1f392ed89c0723a298/README.md)
- [examples/pi0.5_openpi/README.md](https://github.com/liyiteng/AlohaMini/blob/17c6a98d79881a45ab869c1f392ed89c0723a298/examples/pi0.5_openpi/README.md)
- [software/README.md](https://github.com/liyiteng/AlohaMini/blob/17c6a98d79881a45ab869c1f392ed89c0723a298/software/README.md)

### lerobot_alohamini

- [AGENT_GUIDE.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/AGENT_GUIDE.md)
- [README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/README.md)
- [alohamini_sim/README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/alohamini_sim/README.md)
- [alohamini_sim/data_engine/data_gen/intern_engine/skills/library/README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/alohamini_sim/data_engine/data_gen/intern_engine/skills/library/README.md)
- [alohamini_sim/video2sim/README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/alohamini_sim/video2sim/README.md)
- [docker/README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docker/README.md)
- [docs/README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/README.md)
- [docs/alohamini/alohamini.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/alohamini/alohamini.md)
- [docs/alohamini/am-arm200.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/alohamini/am-arm200.md)
- [docs/alohamini/commands.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/alohamini/commands.md)
- [docs/alohamini/install.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/alohamini/install.md)
- [docs/alohamini/profiles.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/alohamini/profiles.md)
- [docs/source/act.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/act.mdx)
- [docs/source/action_representations.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/action_representations.mdx)
- [docs/source/adding_benchmarks.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/adding_benchmarks.mdx)
- [docs/source/annotation_pipeline.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/annotation_pipeline.mdx)
- [docs/source/async.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/async.mdx)
- [docs/source/backwardcomp.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/backwardcomp.mdx)
- [docs/source/bring_your_own_policies.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/bring_your_own_policies.mdx)
- [docs/source/cameras.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/cameras.mdx)
- [docs/source/cheat-sheet.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/cheat-sheet.mdx)
- [docs/source/damiao.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/damiao.mdx)
- [docs/source/debug_processor_pipeline.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/debug_processor_pipeline.mdx)
- [docs/source/earthrover_mini_plus.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/earthrover_mini_plus.mdx)
- [docs/source/env_processor.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/env_processor.mdx)
- [docs/source/envhub.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/envhub.mdx)
- [docs/source/envhub_isaaclab_arena.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/envhub_isaaclab_arena.mdx)
- [docs/source/envhub_leisaac.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/envhub_leisaac.mdx)
- [docs/source/eo1.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/eo1.mdx)
- [docs/source/evo1.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/evo1.mdx)
- [docs/source/fastwam.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/fastwam.mdx)
- [docs/source/feetech.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/feetech.mdx)
- [docs/source/groot.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/groot.mdx)
- [docs/source/hardware_guide.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/hardware_guide.mdx)
- [docs/source/hil_data_collection.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/hil_data_collection.mdx)
- [docs/source/hilserl.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/hilserl.mdx)
- [docs/source/hilserl_sim.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/hilserl_sim.mdx)
- [docs/source/hope_jr.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/hope_jr.mdx)
- [docs/source/il_robots.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/il_robots.mdx)
- [docs/source/implement_your_own_processor.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/implement_your_own_processor.mdx)
- [docs/source/index.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/index.mdx)
- [docs/source/inference.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/inference.mdx)
- [docs/source/installation.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/installation.mdx)
- [docs/source/integrate_hardware.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/integrate_hardware.mdx)
- [docs/source/introduction_processors.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/introduction_processors.mdx)
- [docs/source/isaac_teleop.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/isaac_teleop.mdx)
- [docs/source/koch.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/koch.mdx)
- [docs/source/language_and_recipes.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/language_and_recipes.mdx)
- [docs/source/lekiwi.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/lekiwi.mdx)
- [docs/source/lelab.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/lelab.mdx)
- [docs/source/lerobot-dataset-v3.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/lerobot-dataset-v3.mdx)
- [docs/source/libero.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/libero.mdx)
- [docs/source/libero_plus.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/libero_plus.mdx)
- [docs/source/lingbot_va.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/lingbot_va.mdx)
- [docs/source/metaworld.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/metaworld.mdx)
- [docs/source/molmoact2.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/molmoact2.mdx)
- [docs/source/multi_gpu_training.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/multi_gpu_training.mdx)
- [docs/source/multi_task_dit.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/multi_task_dit.mdx)
- [docs/source/notebooks.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/notebooks.mdx)
- [docs/source/omx.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/omx.mdx)
- [docs/source/openarm.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/openarm.mdx)
- [docs/source/peft_training.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/peft_training.mdx)
- [docs/source/phone_teleop.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/phone_teleop.mdx)
- [docs/source/pi0.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/pi0.mdx)
- [docs/source/pi05.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/pi05.mdx)
- [docs/source/pi0fast.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/pi0fast.mdx)
- [docs/source/policy_act_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_act_README.md)
- [docs/source/policy_diffusion_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_diffusion_README.md)
- [docs/source/policy_evo1_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_evo1_README.md)
- [docs/source/policy_fastwam_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_fastwam_README.md)
- [docs/source/policy_groot_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_groot_README.md)
- [docs/source/policy_molmoact2_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_molmoact2_README.md)
- [docs/source/policy_multi_task_dit_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_multi_task_dit_README.md)
- [docs/source/policy_pi05_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_pi05_README.md)
- [docs/source/policy_pi0_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_pi0_README.md)
- [docs/source/policy_rtc_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_rtc_README.md)
- [docs/source/policy_sarm_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_sarm_README.md)
- [docs/source/policy_smolvla_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_smolvla_README.md)
- [docs/source/policy_tdmpc_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_tdmpc_README.md)
- [docs/source/policy_vla_jepa_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_vla_jepa_README.md)
- [docs/source/policy_vqbet_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_vqbet_README.md)
- [docs/source/policy_walloss_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_walloss_README.md)
- [docs/source/porting_datasets_v3.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/porting_datasets_v3.mdx)
- [docs/source/processors_robots_teleop.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/processors_robots_teleop.mdx)
- [docs/source/reachy2.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/reachy2.mdx)
- [docs/source/rebot_b601.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/rebot_b601.mdx)
- [docs/source/rename_map.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/rename_map.mdx)
- [docs/source/robocasa.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/robocasa.mdx)
- [docs/source/robocerebra.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/robocerebra.mdx)
- [docs/source/robometer.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/robometer.mdx)
- [docs/source/robomme.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/robomme.mdx)
- [docs/source/robotwin.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/robotwin.mdx)
- [docs/source/rtc.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/rtc.mdx)
- [docs/source/sarm.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/sarm.mdx)
- [docs/source/smolvla.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/smolvla.mdx)
- [docs/source/so100.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/so100.mdx)
- [docs/source/so101.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/so101.mdx)
- [docs/source/streaming_video_encoding.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/streaming_video_encoding.mdx)
- [docs/source/tools.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/tools.mdx)
- [docs/source/topreward.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/topreward.mdx)
- [docs/source/torch_accelerators.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/torch_accelerators.mdx)
- [docs/source/unitree_g1.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/unitree_g1.mdx)
- [docs/source/using_dataset_tools.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/using_dataset_tools.mdx)
- [docs/source/video_encoding_parameters.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/video_encoding_parameters.mdx)
- [docs/source/vla_jepa.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/vla_jepa.mdx)
- [docs/source/vlabench.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/vlabench.mdx)
- [docs/source/walloss.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/walloss.mdx)
- [docs/source/xvla.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/xvla.mdx)
- [examples/debug/README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/examples/debug/README.md)
- [examples/isaac_teleop_to_so101/README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/examples/isaac_teleop_to_so101/README.md)
- [examples/omx/README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/examples/omx/README.md)
- [src/lerobot/policies/am_act/README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/src/lerobot/policies/am_act/README.md)
- [src/lerobot/policies/fastwam/wan/README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/src/lerobot/policies/fastwam/wan/README.md)

## 去重别名

| 原路径 | 规范正文 |
|---|---|
| `src/lerobot/policies/act/README.md` | [docs/source/policy_act_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_act_README.md) |
| `src/lerobot/policies/diffusion/README.md` | [docs/source/policy_diffusion_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_diffusion_README.md) |
| `src/lerobot/policies/eo1/README.md` | [docs/source/eo1.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/eo1.mdx) |
| `src/lerobot/policies/evo1/README.md` | [docs/source/policy_evo1_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_evo1_README.md) |
| `src/lerobot/policies/fastwam/README.md` | [docs/source/policy_fastwam_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_fastwam_README.md) |
| `src/lerobot/policies/groot/README.md` | [docs/source/policy_groot_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_groot_README.md) |
| `src/lerobot/policies/lingbot_va/README.md` | [docs/source/lingbot_va.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/lingbot_va.mdx) |
| `src/lerobot/policies/molmoact2/README.md` | [docs/source/molmoact2.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/molmoact2.mdx) |
| `src/lerobot/policies/multi_task_dit/README.md` | [docs/source/policy_multi_task_dit_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_multi_task_dit_README.md) |
| `src/lerobot/policies/pi0/README.md` | [docs/source/policy_pi0_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_pi0_README.md) |
| `src/lerobot/policies/pi05/README.md` | [docs/source/policy_pi05_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_pi05_README.md) |
| `src/lerobot/policies/rtc/README.md` | [docs/source/policy_rtc_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_rtc_README.md) |
| `src/lerobot/policies/smolvla/README.md` | [docs/source/policy_smolvla_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_smolvla_README.md) |
| `src/lerobot/policies/tdmpc/README.md` | [docs/source/policy_tdmpc_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_tdmpc_README.md) |
| `src/lerobot/policies/vla_jepa/README.md` | [docs/source/policy_vla_jepa_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_vla_jepa_README.md) |
| `src/lerobot/policies/vqbet/README.md` | [docs/source/policy_vqbet_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_vqbet_README.md) |
| `src/lerobot/policies/wall_x/README.md` | [docs/source/policy_walloss_README.md](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/policy_walloss_README.md) |
| `src/lerobot/robots/earthrover_mini_plus/earthrover_mini_plus.mdx` | [docs/source/earthrover_mini_plus.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/earthrover_mini_plus.mdx) |
| `src/lerobot/robots/hope_jr/hope_jr.mdx` | [docs/source/hope_jr.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/hope_jr.mdx) |
| `src/lerobot/robots/koch_follower/koch.mdx` | [docs/source/koch.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/koch.mdx) |
| `src/lerobot/robots/lekiwi/lekiwi.mdx` | [docs/source/lekiwi.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/lekiwi.mdx) |
| `src/lerobot/robots/so_follower/so100.md` | [docs/source/so100.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/so100.mdx) |
| `src/lerobot/robots/so_follower/so101.md` | [docs/source/so101.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/so101.mdx) |
| `src/lerobot/teleoperators/so_leader/so100.md` | [docs/source/so100.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/so100.mdx) |
| `src/lerobot/teleoperators/so_leader/so101.md` | [docs/source/so101.mdx](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/source/so101.mdx) |

## 排除的治理/模板路径

- `.github/PULL_REQUEST_TEMPLATE.md`
- `AGENTS.md`
- `AI_POLICY.md`
- `CLAUDE.md`
- `CODE_OF_CONDUCT.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `docs/source/contributing.md`
- `src/lerobot/datasets/card_template.md`
- `src/lerobot/templates/lerobot_modelcard_template.md`
- `src/lerobot/templates/lerobot_rewardmodel_modelcard_template.md`

## 验证范围

本次完成来源目录、脚本接口、文件存在性与当前文档范围核查。没有安装 GPU 工具链、启动真机、运行机械臂、执行训练或声称性能复现。站点迁移还需要独立验证：正文数量和别名一致、MDX 组件转写、图片/下载资源与链接、Sphinx 严格构建、站内导航和浏览器阅读效果。GitHub 来源中出现的 instructions/agent 问答文本均只作为待迁移材料。
