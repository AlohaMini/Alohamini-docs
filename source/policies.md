# 策略与训练教程

本页汇总可供学习和开发的策略与模型。AlohaMini 初次训练仍可先沿 [ACT 主线](training.md) 验证数据和设备；其他策略按各自依赖、输入格式与运行接口配置。

## 1. 选择阅读入口

| 策略 / 专题 | 教程入口 | 阅读重点 |
|---|---|---|
| ACT | [完整教程](upstream/software--docs-source-act.md) | action chunk、训练与评估 |
| AM-ACT | [定制实现说明](upstream/software--src-lerobot-policies-am_act-readme.md) | 离散动作维度、固定维度、损失组和输出缩放 |
| Diffusion | [实现说明](upstream/software--docs-source-policy_diffusion_readme.md) | 实现与参数说明 |
| SmolVLA | [完整教程](upstream/software--docs-source-smolvla.md) | 模型依赖、微调、推理与数据 |
| Pi0 / Pi0.5 | [Pi0](upstream/software--docs-source-pi0.md)、[Pi0.5](upstream/software--docs-source-pi05.md) | LeRobot 内置实现，区别于 [独立 OpenPI](pi05.md) |
| Pi0 FAST | [完整教程](upstream/software--docs-source-pi0fast.md) | 动作表示与模型使用 |
| GR00T | [完整教程](upstream/software--docs-source-groot.md) | 模态、配置与训练 |
| RTC | [完整教程](upstream/software--docs-source-rtc.md) | 异步动作块与兼容策略 |
| 多任务 DiT | [完整教程](upstream/software--docs-source-multi_task_dit.md) | 多任务配置与数据 |
| FastWAM | [完整教程](upstream/software--docs-source-fastwam.md) | 模型与专属依赖 |
| MolmoAct2 | [完整教程](upstream/software--docs-source-molmoact2.md) | 模型输入、微调与使用 |
| VLA-JEPA | [完整教程](upstream/software--docs-source-vla_jepa.md) | 配置、训练与部署 |
| EO-1 / Evo-1 | [EO-1](upstream/software--docs-source-eo1.md)、[Evo-1](upstream/software--docs-source-evo1.md) | 对应实现版本与依赖 |
| LingBot-VA / Wall-OSS / XVLA | [LingBot-VA](upstream/software--docs-source-lingbot_va.md)、[Wall-OSS](upstream/software--docs-source-walloss.md)、[XVLA](upstream/software--docs-source-xvla.md) | 各模型专属数据和接口 |
| TD-MPC / VQ-BeT / SARM | [TD-MPC](upstream/software--docs-source-policy_tdmpc_readme.md)、[VQ-BeT](upstream/software--docs-source-policy_vqbet_readme.md)、[SARM](upstream/software--docs-source-sarm.md) | 部分 README 为实现引用，详读对应正文与代码 |

[查看全部策略教程](library-policies.md)。使用其他策略前，请确认 AlohaMini 的输入、动作维度与推理接口，并完成真机验证。

## 2. 从 ACT 数据转向其他策略前

1. 保留一份已验证的数据集和 ACT 基线，记录相机、特征顺序、动作单位与校准。
2. 按模型教程安装对应 extras，并核对基础权重与使用条件。
3. 确认图像名称、语言任务字段、state/action 维度、归一化统计与模型要求一致。
4. 选择独立输出目录和实验名称，避免覆盖已有检查点。
5. 先运行小规模数据加载与训练检查，确认日志、损失和保存结果正常。
6. 部署时核对推理接口、控制频率和动作块策略；ACT 不使用 RTC 路径。

示例 batch size、训练步数和显存记录取决于具体模型与训练任务，不能作为对所有设备的资源承诺。

## 3. AM-ACT 的特有参数

AM-ACT 可让部分动作维度采用分类，其余维度仍按连续值训练。

| 参数 | 作用 |
|---|---|
| `fixed_action_dims` | 排除训练并在归一化空间固定为零的维度 |
| `discrete_action_dims` | 采用分类预测的维度索引 |
| `discrete_action_values` | 每个分类对应的物理动作值，顺序与分类一致 |
| `discrete_action_class_weights` | 对应类别权重 |
| `discrete_action_loss_weight` | 分类损失倍率 |
| `action_loss_groups` / `action_loss_weights` | 连续维度分组与组权重 |
| `observation_state_dims` | 选择输入状态的子集 |
| `inference_action_scale_dims` / `inference_action_scale` | 反归一化之后缩放指定输出 |

示例配置将 `[14,15,16]` 作为离散维度例子；是否对应底盘要以实际数据特征顺序判断。归一化空间中的零也不必然等于物理零动作。完整训练命令和加载方式见 [AM-ACT 详细配置](upstream/software--src-lerobot-policies-am_act-readme.md)。

## 4. 数据与训练工具

- [数据集 v3 格式](upstream/software--docs-source-lerobot-dataset-v3.md)、[迁移旧数据](upstream/software--docs-source-porting_datasets_v3.md)
- [数据集编辑工具](upstream/software--docs-source-using_dataset_tools.md)、[动作表示](upstream/software--docs-source-action_representations.md)
- [PEFT 训练](upstream/software--docs-source-peft_training.md)、[多 GPU 训练](upstream/software--docs-source-multi_gpu_training.md)
- [推理教程](upstream/software--docs-source-inference.md)、[异步推理](upstream/software--docs-source-async.md)
- [人在回路数据采集](upstream/software--docs-source-hil_data_collection.md)、[HIL-SERL](upstream/software--docs-source-hilserl.md)

[教程资料库] 汇总各专题(tutorial-library.md)，包括其他机器人和仿真基准示例。
