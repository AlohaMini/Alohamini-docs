# 迁移清单与版本

GitHub 部分迁入的范围为两仓固定提交内的 Markdown / MDX / RST 教程，包括独立示例、通用 LeRobot 文档与开发说明。源文档中的外部项目链接仍指向对应项目，不表示这些外部仓库也全部复制到了本站。

| 来源 | 固定版本 | 独立正文 |
|---|---|---:|
| AlohaMini 硬件 | `17c6a98d79881a45ab869c1f392ed89c0723a298` | 13 |
| lerobot_alohamini 软件 | `7843e5888366eaa553630e2f9d5539505a62dddf` | 114 |
| 合计 | 核对日期 2026-09-28 | 127 |

另有 26 个符号链接别名已对应到正文，9 个治理或模板文件不作为教程收录。该数字包含贡献开发说明，独立正文已去除符号链接重复。

## 语雀使用手册

已收录公开目录中的 13 篇正文、65 段代码及 108 处图片引用，图片按内容去重后本地保存。完整入口：[官方使用手册](official-manual.md)。每篇提供来源链接，未作勘误的网页转写保存在项目中，`yuque-manifest.json` 记录页面、图片校验值与修正项。

- 网页正文通过浏览器读取，代码块逐一加载核对；不使用付费 API。
- 《模型Policy.pdf》需登录下载，仅保留入口，未取得附件正文。
- 「看看新闻 Knews」和「魔都眼」两段视频已保存到本站并支持页内播放。Bilibili 使用嵌入播放器；飞书课件及扩展 GitHub 仓库未全文迁入。
- Pro 命令型号、校准续行符、仓库拼写和 Host 模块名已勘误；原文副本保留原有写法。
- GitHub 缺少的 Pro 零件级装配说明，不能用交付开箱照片替代。

## 各部分完成状态

| 部分 | 内容迁移状态 | 仍需注意 |
|---|---|---|
| 标准 2 与 Pro 主线 | 中文教程、原始全文均在站内 | Pro 独立装配资料仍待上游提供 |
| 一代硬件 | 中文步骤、BOM 与全部原文装配照片已收录 | 原文供电与紧固件表述有差异，按实物核对 |
| 单臂训练评估 | 中文命令与原始工作流已补齐 | 需要真实机械臂验证 |
| 调试、Docker、开发 | 中文说明与完整原文已收录 | 运行条件按设备和环境选择 |
| OpenPI | 完整配置、历史命令与中文适配说明已收录 | 旧客户端和缺少服务入口的问题未修复 |
| video2sim / ManiSkill | 中文工作流、原始全文与技能说明已收录 | 外部环境、模型资产及数据维度需核对 |
| 其他策略、数据集、处理器与机器人 | 完整原文已收录并分类 | 原文保留原语言，尚非逐篇完整中文翻译；非整机适配保证 |

## 文档与资产说明

正文中的外部图片及动图已保存到本站，来源地址和文件校验值记录在 `external-images.json`。首页和原文中的徽章也使用本地快照，Stars 等数字代表下载时的状态。

每篇原文的下载文件保留原始字节内容，并在仓库的 `upstream-manifest.json` 中记录 SHA-256。展示页只转换网页组件、链接与媒体路径；原文中的错误或旧接口不会因为导入而自动修复。中文主线对已核对的差异另作说明。

本次没有执行实际机械臂运动、GPU 训练或仿真管线。站点构建与链接检查只能验证文档显示和连接，不能替代这些运行验证。

## 来源与许可

原文归原作者所有。两仓根许可证为 Apache-2.0，源文档中的版权与额外说明保留；第三方引用与外部资源仍适用各自条款。

- [硬件仓库许可证](_static/upstream-licenses/hardware-LICENSE.txt)
- [软件仓库许可证](_static/upstream-licenses/software-LICENSE.txt)
- [返回教程资料库](tutorial-library.md)

## 全文对应表

| 上游文件 | 站内全文 |
|---|---|
| `liyiteng/AlohaMini/AlohaMini1/README.md` | [AlohaMini](upstream/hardware--alohamini1-readme.md) |
| `liyiteng/AlohaMini/AlohaMini1/docs/BOM.md` | [Bill of Materials](upstream/hardware--alohamini1-docs-bom.md) |
| `liyiteng/AlohaMini/AlohaMini1/docs/hardware_assembly.md` | [Assembly](upstream/hardware--alohamini1-docs-hardware_assembly.md) |
| `liyiteng/AlohaMini/AlohaMini1/docs/software_setup.md` | [software_setup](upstream/hardware--alohamini1-docs-software_setup.md) |
| `liyiteng/AlohaMini/AlohaMini1/hardware/arms/README.md` | [项目说明](upstream/hardware--alohamini1-hardware-arms-readme.md) |
| `liyiteng/AlohaMini/AlohaMini1/simulation/README.md` | [AlohaMini-Simulation](upstream/hardware--alohamini1-simulation-readme.md) |
| `liyiteng/AlohaMini/AlohaMini2/docs/BOM.md` | [Bill of Materials — AlohaMini2](upstream/hardware--alohamini2-docs-bom.md) |
| `liyiteng/AlohaMini/AlohaMini2/docs/assembly_guide.md` | [AlohaMini2 Assembly Guide](upstream/hardware--alohamini2-docs-assembly_guide.md) |
| `liyiteng/AlohaMini/AlohaMini2/docs/print_guide.md` | [AlohaMini2 Print Guide](upstream/hardware--alohamini2-docs-print_guide.md) |
| `liyiteng/AlohaMini/AlohaMini2/hardware/am_arm200/README.md` | [AM-ARM200](upstream/hardware--alohamini2-hardware-am_arm200-readme.md) |
| `liyiteng/AlohaMini/README.md` | [AlohaMini2](upstream/hardware--readme.md) |
| `liyiteng/AlohaMini/examples/pi0.5_openpi/README.md` | [Pi-0.5 for Alohamini](upstream/hardware--examples-pi0-5_openpi-readme.md) |
| `liyiteng/AlohaMini/software/README.md` | [Software (LeRobot Integration)](upstream/hardware--software-readme.md) |
| `liyiteng/lerobot_alohamini/AGENT_GUIDE.md` | [AGENT_GUIDE.md — LeRobot Helper for AI Agents & Users](upstream/software--agent_guide.md) |
| `liyiteng/lerobot_alohamini/CONTRIBUTING.md` | [How to contribute to 🤗 LeRobot](upstream/software--contributing.md) |
| `liyiteng/lerobot_alohamini/README.md` | [lerobot_alohamini](upstream/software--readme.md) |
| `liyiteng/lerobot_alohamini/alohamini_sim/README.md` | [alohamini_sim](upstream/software--alohamini_sim-readme.md) |
| `liyiteng/lerobot_alohamini/alohamini_sim/data_engine/data_gen/intern_engine/skills/library/README.md` | [Skill Library (ASPIRE-style)](upstream/software--alohamini_sim-data_engine-data_gen-intern_engine-skills-library-readme.md) |
| `liyiteng/lerobot_alohamini/alohamini_sim/video2sim/README.md` | [video2sim](upstream/software--alohamini_sim-video2sim-readme.md) |
| `liyiteng/lerobot_alohamini/docker/README.md` | [Docker](upstream/software--docker-readme.md) |
| `liyiteng/lerobot_alohamini/docs/README.md` | [Generating the documentation](upstream/software--docs-readme.md) |
| `liyiteng/lerobot_alohamini/docs/alohamini/alohamini.md` | [AlohaMini — Full Workflow](upstream/software--docs-alohamini-alohamini.md) |
| `liyiteng/lerobot_alohamini/docs/alohamini/am-arm200.md` | [AM-ARM200 — Full Workflow](upstream/software--docs-alohamini-am-arm200.md) |
| `liyiteng/lerobot_alohamini/docs/alohamini/commands.md` | [AlohaMini Command Cheat Sheet](upstream/software--docs-alohamini-commands.md) |
| `liyiteng/lerobot_alohamini/docs/alohamini/install.md` | [Installation & Configuration](upstream/software--docs-alohamini-install.md) |
| `liyiteng/lerobot_alohamini/docs/alohamini/profiles.md` | [Hardware Profile Reference](upstream/software--docs-alohamini-profiles.md) |
| `liyiteng/lerobot_alohamini/docs/source/act.mdx` | [ACT (Action Chunking with Transformers)](upstream/software--docs-source-act.md) |
| `liyiteng/lerobot_alohamini/docs/source/action_representations.mdx` | [Action Representations](upstream/software--docs-source-action_representations.md) |
| `liyiteng/lerobot_alohamini/docs/source/adding_benchmarks.mdx` | [Adding a New Benchmark](upstream/software--docs-source-adding_benchmarks.md) |
| `liyiteng/lerobot_alohamini/docs/source/annotation_pipeline.mdx` | [Annotation Pipeline](upstream/software--docs-source-annotation_pipeline.md) |
| `liyiteng/lerobot_alohamini/docs/source/async.mdx` | [Asynchronous Inference](upstream/software--docs-source-async.md) |
| `liyiteng/lerobot_alohamini/docs/source/backwardcomp.mdx` | [Backward compatibility](upstream/software--docs-source-backwardcomp.md) |
| `liyiteng/lerobot_alohamini/docs/source/bring_your_own_policies.mdx` | [Adding a Policy](upstream/software--docs-source-bring_your_own_policies.md) |
| `liyiteng/lerobot_alohamini/docs/source/cameras.mdx` | [Cameras](upstream/software--docs-source-cameras.md) |
| `liyiteng/lerobot_alohamini/docs/source/cheat-sheet.mdx` | [Cheat sheet](upstream/software--docs-source-cheat-sheet.md) |
| `liyiteng/lerobot_alohamini/docs/source/damiao.mdx` | [Damiao Motors and CAN Bus](upstream/software--docs-source-damiao.md) |
| `liyiteng/lerobot_alohamini/docs/source/debug_processor_pipeline.mdx` | [Debug Your Processor Pipeline](upstream/software--docs-source-debug_processor_pipeline.md) |
| `liyiteng/lerobot_alohamini/docs/source/earthrover_mini_plus.mdx` | [EarthRover Mini Plus](upstream/software--docs-source-earthrover_mini_plus.md) |
| `liyiteng/lerobot_alohamini/docs/source/env_processor.mdx` | [Environment Processors](upstream/software--docs-source-env_processor.md) |
| `liyiteng/lerobot_alohamini/docs/source/envhub.mdx` | [Loading Environments from the Hub](upstream/software--docs-source-envhub.md) |
| `liyiteng/lerobot_alohamini/docs/source/envhub_isaaclab_arena.mdx` | [NVIDIA IsaacLab Arena & LeRobot](upstream/software--docs-source-envhub_isaaclab_arena.md) |
| `liyiteng/lerobot_alohamini/docs/source/envhub_leisaac.mdx` | [LeIsaac × LeRobot EnvHub](upstream/software--docs-source-envhub_leisaac.md) |
| `liyiteng/lerobot_alohamini/docs/source/eo1.mdx` | [EO-1](upstream/software--docs-source-eo1.md) |
| `liyiteng/lerobot_alohamini/docs/source/evo1.mdx` | [EVO1](upstream/software--docs-source-evo1.md) |
| `liyiteng/lerobot_alohamini/docs/source/fastwam.mdx` | [FastWAM](upstream/software--docs-source-fastwam.md) |
| `liyiteng/lerobot_alohamini/docs/source/feetech.mdx` | [Feetech Motor Firmware Update](upstream/software--docs-source-feetech.md) |
| `liyiteng/lerobot_alohamini/docs/source/groot.mdx` | [GR00T Policy](upstream/software--docs-source-groot.md) |
| `liyiteng/lerobot_alohamini/docs/source/hardware_guide.mdx` | [Compute HW Guide for LeRobot Training](upstream/software--docs-source-hardware_guide.md) |
| `liyiteng/lerobot_alohamini/docs/source/hil_data_collection.mdx` | [Human-In-the-Loop Data Collection](upstream/software--docs-source-hil_data_collection.md) |
| `liyiteng/lerobot_alohamini/docs/source/hilserl.mdx` | [HIL-SERL Real Robot Training Workflow Guide](upstream/software--docs-source-hilserl.md) |
| `liyiteng/lerobot_alohamini/docs/source/hilserl_sim.mdx` | [Train RL in Simulation](upstream/software--docs-source-hilserl_sim.md) |
| `liyiteng/lerobot_alohamini/docs/source/hope_jr.mdx` | [HopeJR](upstream/software--docs-source-hope_jr.md) |
| `liyiteng/lerobot_alohamini/docs/source/il_robots.mdx` | [Imitation Learning on Real-World Robots](upstream/software--docs-source-il_robots.md) |
| `liyiteng/lerobot_alohamini/docs/source/implement_your_own_processor.mdx` | [Implement your own Robot Processor](upstream/software--docs-source-implement_your_own_processor.md) |
| `liyiteng/lerobot_alohamini/docs/source/index.mdx` | [LeRobot](upstream/software--docs-source-index.md) |
| `liyiteng/lerobot_alohamini/docs/source/inference.mdx` | [Policy Deployment (lerobot-rollout)](upstream/software--docs-source-inference.md) |
| `liyiteng/lerobot_alohamini/docs/source/installation.mdx` | [Installation](upstream/software--docs-source-installation.md) |
| `liyiteng/lerobot_alohamini/docs/source/integrate_hardware.mdx` | [Bring Your Own Hardware](upstream/software--docs-source-integrate_hardware.md) |
| `liyiteng/lerobot_alohamini/docs/source/introduction_processors.mdx` | [Introduction to Processors](upstream/software--docs-source-introduction_processors.md) |
| `liyiteng/lerobot_alohamini/docs/source/isaac_teleop.mdx` | [Isaac Teleop](upstream/software--docs-source-isaac_teleop.md) |
| `liyiteng/lerobot_alohamini/docs/source/koch.mdx` | [Koch v1.1](upstream/software--docs-source-koch.md) |
| `liyiteng/lerobot_alohamini/docs/source/language_and_recipes.mdx` | [Language columns and recipes](upstream/software--docs-source-language_and_recipes.md) |
| `liyiteng/lerobot_alohamini/docs/source/lekiwi.mdx` | [LeKiwi](upstream/software--docs-source-lekiwi.md) |
| `liyiteng/lerobot_alohamini/docs/source/lelab.mdx` | [LeLab - LeRobot Guide](upstream/software--docs-source-lelab.md) |
| `liyiteng/lerobot_alohamini/docs/source/lerobot-dataset-v3.mdx` | [LeRobotDataset v3.0](upstream/software--docs-source-lerobot-dataset-v3.md) |
| `liyiteng/lerobot_alohamini/docs/source/libero.mdx` | [LIBERO](upstream/software--docs-source-libero.md) |
| `liyiteng/lerobot_alohamini/docs/source/libero_plus.mdx` | [LIBERO-plus](upstream/software--docs-source-libero_plus.md) |
| `liyiteng/lerobot_alohamini/docs/source/lingbot_va.mdx` | [LingBot-VA](upstream/software--docs-source-lingbot_va.md) |
| `liyiteng/lerobot_alohamini/docs/source/metaworld.mdx` | [Meta-World](upstream/software--docs-source-metaworld.md) |
| `liyiteng/lerobot_alohamini/docs/source/molmoact2.mdx` | [MolmoAct2 Policy](upstream/software--docs-source-molmoact2.md) |
| `liyiteng/lerobot_alohamini/docs/source/multi_gpu_training.mdx` | [Multi-GPU Training](upstream/software--docs-source-multi_gpu_training.md) |
| `liyiteng/lerobot_alohamini/docs/source/multi_task_dit.mdx` | [Multitask DiT Policy](upstream/software--docs-source-multi_task_dit.md) |
| `liyiteng/lerobot_alohamini/docs/source/notebooks.mdx` | [🤗 LeRobot Notebooks](upstream/software--docs-source-notebooks.md) |
| `liyiteng/lerobot_alohamini/docs/source/omx.mdx` | [omx](upstream/software--docs-source-omx.md) |
| `liyiteng/lerobot_alohamini/docs/source/openarm.mdx` | [OpenArm](upstream/software--docs-source-openarm.md) |
| `liyiteng/lerobot_alohamini/docs/source/peft_training.mdx` | [Parameter efficient fine-tuning with 🤗 PEFT](upstream/software--docs-source-peft_training.md) |
| `liyiteng/lerobot_alohamini/docs/source/phone_teleop.mdx` | [Phone](upstream/software--docs-source-phone_teleop.md) |
| `liyiteng/lerobot_alohamini/docs/source/pi0.mdx` | [π₀ (Pi0)](upstream/software--docs-source-pi0.md) |
| `liyiteng/lerobot_alohamini/docs/source/pi05.mdx` | [π₀.₅ (Pi05) Policy](upstream/software--docs-source-pi05.md) |
| `liyiteng/lerobot_alohamini/docs/source/pi0fast.mdx` | [π₀-FAST (Pi0-FAST)](upstream/software--docs-source-pi0fast.md) |
| `liyiteng/lerobot_alohamini/docs/source/policy_act_README.md` | [policy_act_README](upstream/software--docs-source-policy_act_readme.md) |
| `liyiteng/lerobot_alohamini/docs/source/policy_diffusion_README.md` | [policy_diffusion_README](upstream/software--docs-source-policy_diffusion_readme.md) |
| `liyiteng/lerobot_alohamini/docs/source/policy_evo1_README.md` | [EVO1](upstream/software--docs-source-policy_evo1_readme.md) |
| `liyiteng/lerobot_alohamini/docs/source/policy_fastwam_README.md` | [policy_fastwam_README](upstream/software--docs-source-policy_fastwam_readme.md) |
| `liyiteng/lerobot_alohamini/docs/source/policy_groot_README.md` | [Resolve a local checkpoint (GR00T-N1.7-LIBERO / libero_10)](upstream/software--docs-source-policy_groot_readme.md) |
| `liyiteng/lerobot_alohamini/docs/source/policy_molmoact2_README.md` | [MolmoAct2](upstream/software--docs-source-policy_molmoact2_readme.md) |
| `liyiteng/lerobot_alohamini/docs/source/policy_multi_task_dit_README.md` | [Multitask DiT Policy](upstream/software--docs-source-policy_multi_task_dit_readme.md) |
| `liyiteng/lerobot_alohamini/docs/source/policy_pi05_README.md` | [π₀.₅ (pi05)](upstream/software--docs-source-policy_pi05_readme.md) |
| `liyiteng/lerobot_alohamini/docs/source/policy_pi0_README.md` | [π₀ (pi0)](upstream/software--docs-source-policy_pi0_readme.md) |
| `liyiteng/lerobot_alohamini/docs/source/policy_rtc_README.md` | [Real-Time Chunking (RTC)](upstream/software--docs-source-policy_rtc_readme.md) |
| `liyiteng/lerobot_alohamini/docs/source/policy_sarm_README.md` | [policy_sarm_README](upstream/software--docs-source-policy_sarm_readme.md) |
| `liyiteng/lerobot_alohamini/docs/source/policy_smolvla_README.md` | [policy_smolvla_README](upstream/software--docs-source-policy_smolvla_readme.md) |
| `liyiteng/lerobot_alohamini/docs/source/policy_tdmpc_README.md` | [policy_tdmpc_README](upstream/software--docs-source-policy_tdmpc_readme.md) |
| `liyiteng/lerobot_alohamini/docs/source/policy_vla_jepa_README.md` | [VLA-JEPA](upstream/software--docs-source-policy_vla_jepa_readme.md) |
| `liyiteng/lerobot_alohamini/docs/source/policy_vqbet_README.md` | [policy_vqbet_README](upstream/software--docs-source-policy_vqbet_readme.md) |
| `liyiteng/lerobot_alohamini/docs/source/policy_walloss_README.md` | [WALL-OSS](upstream/software--docs-source-policy_walloss_readme.md) |
| `liyiteng/lerobot_alohamini/docs/source/porting_datasets_v3.mdx` | [Porting Large Datasets to LeRobot Dataset v3.0](upstream/software--docs-source-porting_datasets_v3.md) |
| `liyiteng/lerobot_alohamini/docs/source/processors_robots_teleop.mdx` | [Processors for Robots and Teleoperators](upstream/software--docs-source-processors_robots_teleop.md) |
| `liyiteng/lerobot_alohamini/docs/source/reachy2.mdx` | [Reachy 2](upstream/software--docs-source-reachy2.md) |
| `liyiteng/lerobot_alohamini/docs/source/rebot_b601.mdx` | [reBot B601-DM](upstream/software--docs-source-rebot_b601.md) |
| `liyiteng/lerobot_alohamini/docs/source/rename_map.mdx` | [Rename Map and Empty Cameras](upstream/software--docs-source-rename_map.md) |
| `liyiteng/lerobot_alohamini/docs/source/robocasa.mdx` | [RoboCasa365](upstream/software--docs-source-robocasa.md) |
| `liyiteng/lerobot_alohamini/docs/source/robocerebra.mdx` | [RoboCerebra](upstream/software--docs-source-robocerebra.md) |
| `liyiteng/lerobot_alohamini/docs/source/robometer.mdx` | [ROBOMETER](upstream/software--docs-source-robometer.md) |
| `liyiteng/lerobot_alohamini/docs/source/robomme.mdx` | [RoboMME](upstream/software--docs-source-robomme.md) |
| `liyiteng/lerobot_alohamini/docs/source/robotwin.mdx` | [RoboTwin 2.0](upstream/software--docs-source-robotwin.md) |
| `liyiteng/lerobot_alohamini/docs/source/rtc.mdx` | [Real-Time Chunking (RTC)](upstream/software--docs-source-rtc.md) |
| `liyiteng/lerobot_alohamini/docs/source/sarm.mdx` | [SARM: Stage-Aware Reward Modeling](upstream/software--docs-source-sarm.md) |
| `liyiteng/lerobot_alohamini/docs/source/smolvla.mdx` | [SmolVLA](upstream/software--docs-source-smolvla.md) |
| `liyiteng/lerobot_alohamini/docs/source/so100.mdx` | [SO-100](upstream/software--docs-source-so100.md) |
| `liyiteng/lerobot_alohamini/docs/source/so101.mdx` | [SO-101](upstream/software--docs-source-so101.md) |
| `liyiteng/lerobot_alohamini/docs/source/streaming_video_encoding.mdx` | [Streaming Video Encoding Guide](upstream/software--docs-source-streaming_video_encoding.md) |
| `liyiteng/lerobot_alohamini/docs/source/tools.mdx` | [Tools](upstream/software--docs-source-tools.md) |
| `liyiteng/lerobot_alohamini/docs/source/topreward.mdx` | [TOPReward](upstream/software--docs-source-topreward.md) |
| `liyiteng/lerobot_alohamini/docs/source/torch_accelerators.mdx` | [PyTorch accelerators](upstream/software--docs-source-torch_accelerators.md) |
| `liyiteng/lerobot_alohamini/docs/source/unitree_g1.mdx` | [Unitree G1](upstream/software--docs-source-unitree_g1.md) |
| `liyiteng/lerobot_alohamini/docs/source/using_dataset_tools.mdx` | [Using Dataset Tools](upstream/software--docs-source-using_dataset_tools.md) |
| `liyiteng/lerobot_alohamini/docs/source/video_encoding_parameters.mdx` | [Video encoding parameters](upstream/software--docs-source-video_encoding_parameters.md) |
| `liyiteng/lerobot_alohamini/docs/source/vla_jepa.mdx` | [VLA-JEPA](upstream/software--docs-source-vla_jepa.md) |
| `liyiteng/lerobot_alohamini/docs/source/vlabench.mdx` | [VLABench](upstream/software--docs-source-vlabench.md) |
| `liyiteng/lerobot_alohamini/docs/source/walloss.mdx` | [WALL-OSS](upstream/software--docs-source-walloss.md) |
| `liyiteng/lerobot_alohamini/docs/source/xvla.mdx` | [X-VLA: The First Soft-Prompted Robot Foundation Model for Any Robot, Any Task](upstream/software--docs-source-xvla.md) |
| `liyiteng/lerobot_alohamini/examples/debug/README.md` | [项目说明](upstream/software--examples-debug-readme.md) |
| `liyiteng/lerobot_alohamini/examples/isaac_teleop_to_so101/README.md` | [Isaac Teleop → SO-101](upstream/software--examples-isaac_teleop_to_so101-readme.md) |
| `liyiteng/lerobot_alohamini/examples/omx/README.md` | [OMX Follower — Cube Pick And Place Example](upstream/software--examples-omx-readme.md) |
| `liyiteng/lerobot_alohamini/src/lerobot/policies/am_act/README.md` | [AM-ACT](upstream/software--src-lerobot-policies-am_act-readme.md) |
| `liyiteng/lerobot_alohamini/src/lerobot/policies/fastwam/wan/README.md` | [FastWAM `wan` package](upstream/software--src-lerobot-policies-fastwam-wan-readme.md) |

## 符号链接去重记录

| 原入口 | 收录正文 |
|---|---|
| `docs/source/contributing.md` | [CONTRIBUTING.md](upstream/software--contributing.md) |
| `src/lerobot/policies/act/README.md` | [docs/source/policy_act_README.md](upstream/software--docs-source-policy_act_readme.md) |
| `src/lerobot/policies/diffusion/README.md` | [docs/source/policy_diffusion_README.md](upstream/software--docs-source-policy_diffusion_readme.md) |
| `src/lerobot/policies/eo1/README.md` | [docs/source/eo1.mdx](upstream/software--docs-source-eo1.md) |
| `src/lerobot/policies/evo1/README.md` | [docs/source/policy_evo1_README.md](upstream/software--docs-source-policy_evo1_readme.md) |
| `src/lerobot/policies/fastwam/README.md` | [docs/source/policy_fastwam_README.md](upstream/software--docs-source-policy_fastwam_readme.md) |
| `src/lerobot/policies/groot/README.md` | [docs/source/policy_groot_README.md](upstream/software--docs-source-policy_groot_readme.md) |
| `src/lerobot/policies/lingbot_va/README.md` | [docs/source/lingbot_va.mdx](upstream/software--docs-source-lingbot_va.md) |
| `src/lerobot/policies/molmoact2/README.md` | [docs/source/molmoact2.mdx](upstream/software--docs-source-molmoact2.md) |
| `src/lerobot/policies/multi_task_dit/README.md` | [docs/source/policy_multi_task_dit_README.md](upstream/software--docs-source-policy_multi_task_dit_readme.md) |
| `src/lerobot/policies/pi0/README.md` | [docs/source/policy_pi0_README.md](upstream/software--docs-source-policy_pi0_readme.md) |
| `src/lerobot/policies/pi05/README.md` | [docs/source/policy_pi05_README.md](upstream/software--docs-source-policy_pi05_readme.md) |
| `src/lerobot/policies/rtc/README.md` | [docs/source/policy_rtc_README.md](upstream/software--docs-source-policy_rtc_readme.md) |
| `src/lerobot/policies/smolvla/README.md` | [docs/source/policy_smolvla_README.md](upstream/software--docs-source-policy_smolvla_readme.md) |
| `src/lerobot/policies/tdmpc/README.md` | [docs/source/policy_tdmpc_README.md](upstream/software--docs-source-policy_tdmpc_readme.md) |
| `src/lerobot/policies/vla_jepa/README.md` | [docs/source/policy_vla_jepa_README.md](upstream/software--docs-source-policy_vla_jepa_readme.md) |
| `src/lerobot/policies/vqbet/README.md` | [docs/source/policy_vqbet_README.md](upstream/software--docs-source-policy_vqbet_readme.md) |
| `src/lerobot/policies/wall_x/README.md` | [docs/source/policy_walloss_README.md](upstream/software--docs-source-policy_walloss_readme.md) |
| `src/lerobot/robots/earthrover_mini_plus/earthrover_mini_plus.mdx` | [docs/source/earthrover_mini_plus.mdx](upstream/software--docs-source-earthrover_mini_plus.md) |
| `src/lerobot/robots/hope_jr/hope_jr.mdx` | [docs/source/hope_jr.mdx](upstream/software--docs-source-hope_jr.md) |
| `src/lerobot/robots/koch_follower/koch.mdx` | [docs/source/koch.mdx](upstream/software--docs-source-koch.md) |
| `src/lerobot/robots/lekiwi/lekiwi.mdx` | [docs/source/lekiwi.mdx](upstream/software--docs-source-lekiwi.md) |
| `src/lerobot/robots/so_follower/so100.md` | [docs/source/so100.mdx](upstream/software--docs-source-so100.md) |
| `src/lerobot/robots/so_follower/so101.md` | [docs/source/so101.mdx](upstream/software--docs-source-so101.md) |
| `src/lerobot/teleoperators/so_leader/so100.md` | [docs/source/so100.mdx](upstream/software--docs-source-so100.md) |
| `src/lerobot/teleoperators/so_leader/so101.md` | [docs/source/so101.mdx](upstream/software--docs-source-so101.md) |

## 不作为教程的文件

- `liyiteng/lerobot_alohamini/.github/PULL_REQUEST_TEMPLATE.md`：仓库治理、代理指令或模板，不属于教程。
- `liyiteng/lerobot_alohamini/AGENTS.md`：仓库治理、代理指令或模板，不属于教程。
- `liyiteng/lerobot_alohamini/AI_POLICY.md`：仓库治理、代理指令或模板，不属于教程。
- `liyiteng/lerobot_alohamini/CLAUDE.md`：仓库治理、代理指令或模板，不属于教程。
- `liyiteng/lerobot_alohamini/CODE_OF_CONDUCT.md`：仓库治理、代理指令或模板，不属于教程。
- `liyiteng/lerobot_alohamini/SECURITY.md`：仓库治理、代理指令或模板，不属于教程。
- `liyiteng/lerobot_alohamini/src/lerobot/datasets/card_template.md`：仓库治理、代理指令或模板，不属于教程。
- `liyiteng/lerobot_alohamini/src/lerobot/templates/lerobot_modelcard_template.md`：仓库治理、代理指令或模板，不属于教程。
- `liyiteng/lerobot_alohamini/src/lerobot/templates/lerobot_rewardmodel_modelcard_template.md`：仓库治理、代理指令或模板，不属于教程。
