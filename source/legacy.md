# AlohaMini 1

一代使用 SO-ARM100 / SO-ARM101 双臂，具有轮式底盘与电动升降机构。这里保留一代的硬件、软件和仿真入口。

```{image} _static/media/alohamini_git.png
:alt: AlohaMini 一代机器人实机
:width: 100%
```

## 硬件资料

- [一代项目介绍](https://github.com/liyiteng/AlohaMini/tree/main/AlohaMini1)
- [一代 BOM](https://github.com/liyiteng/AlohaMini/blob/main/AlohaMini1/docs/BOM.md)
- [一代组装指南](https://github.com/liyiteng/AlohaMini/blob/main/AlohaMini1/docs/hardware_assembly.md)
- [结构设计文件](https://github.com/liyiteng/AlohaMini/tree/main/AlohaMini1/hardware)

## 软件与仿真

当前统一软件入口为 [lerobot_alohamini](https://github.com/liyiteng/lerobot_alohamini)。请选择与一代对应的硬件配置。

仿真资源请查看 [仿真指南](simulation.md)。

## 与二代的区别

二代更换了机械臂并强化底盘和升降机构。查看 [机型与参数](specifications.md)，确认设计差异后再决定是否升级。


## 一代软件参数

| 参数 | 一代取值 |
|---|---|
| 整机型号 | `alohamini1` |
| 主臂 profile | `so-arm-5dof` |
| 常用主臂校准 ID | `so101_leader_bi` |
| 数据接口 | 16 维 |
| 轮组与升降舵机 | STS3215 |
| 升降传动参数 | 84 mm/rev |

在 Pi 启动：

```bash
python -m lerobot.robots.alohamini.alohamini_host --robot_model alohamini1
```

在 PC 启动：

```bash
python examples/alohamini/teleoperate_bi.py \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini1 \
  --teleop.id so101_leader_bi \
  --teleop.arm_profile so-arm-5dof \
  --fps 50 \
  --camera-fps 30
```

## 使用统一教程时替换哪些内容

安装、设备发现与数据工作流可参考本站统一教程。涉及硬件的步骤使用一代结构与参数：

1. 校准命令改为一代机型和 SO 主臂 profile。
2. 遥操作、录制、回放和评估保持 `alohamini1`。
3. 数据集使用独立名称，记录其 16 维 state/action 定义。
4. 模型使用与一代数据匹配的检查点。
5. 摄像头名称以当前实际配置和已有数据为准。

从旧版本迁移前，保留校准、数据集、机型与相机配置记录。旧数据可能还涉及角度／归一化表示差异，应检查配置中的 `use_degrees` 兼容选项及原数据语义，不要只根据数组长度判断兼容性。

## 保留与升级

一代仍可用于遥操作、数据采集和模型实验。升级二代涉及机械臂、升降与底盘结构，以及软件中的 profile 和数据接口；这是一组硬件与配置变更，需要重新检查装配、校准与训练数据。
