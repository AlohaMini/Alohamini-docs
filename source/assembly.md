# AlohaMini 2 硬件组装

**适用型号：标准 AlohaMini 2。** Pro 用户请先阅读 [2 Pro 硬件说明](hardware-pro.md)；本页的物料数量、打印件和装配照片对应标准版。

本指南完整介绍 **AlohaMini 2 / Mobile Base 2** 的机身装配。主臂和从臂需要先按 [AM-ARM200 组装指南](https://github.com/liyiteng/AM-ARM/tree/main/am-arm200) 独立完成，再安装到操作台与机身。2 Pro 的金属底盘不属于本页装配范围。

## 开始前

备齐 [物料清单](bom.md) 和 [打印清单](printing.md) 中的零件。先干装、确认方向与配合，再胶接；胶水按其产品说明充分固化后再加载。以下照片均来自项目的二代组装资料。

| 阶段 | 完成后应该看到 |
|---|---|
| 舵机编号与底盘 | 三个轮舵机位置正确，总线连接顺序明确 |
| 全向轮与立柱 | 轮组固定，立柱法兰完全贴合底盘 |
| 肩部与升降 | 八只导轨轴承就位，肩部可顺畅滑动 |
| 双臂与摄像头 | 左右臂固定，相机方向与用途有记录 |
| 走线与供电 | 升降全行程有余量，电源路径明确 |
| 分模块调试 | 底盘、升降与机械臂分别检查后再联动 |

## 1. 设置舵机 ID

**安装前每次只连接一只待配置舵机。** 先记录当前 ID，再写入目标 ID，避免总线上出现重复编号。

| 位置 | 目标 ID |
|---|---:|
| 左后轮 | 10 |
| 前轮 | 9 |
| 右后轮 | 8 |
| 肩部升降 | 11 |

先按 [软件安装](software.md) 配置 `lerobot_alohamini`。在软件仓库根目录运行以下示例，将当前 ID 为 1 的舵机改为 8：

```bash
python examples/debug/motors.py configure_motor_id \
  --id 1 \
  --set_id 8 \
  --port /dev/ttyACM0
```

`--id` 是当前编号，`--set_id` 是目标编号，串口需替换成实际控制板路径。对其余舵机分别重复。也可使用飞特 FD Debug Tool，经 Waveshare 控制板以 **1000000** 波特率扫描和写入；完成一只后断开，再接下一只。

## 2. 拼装底盘

1. 清理三块底盘的支撑，特别是轮舱、线槽和销孔。
2. 接合面试配无误后涂环氧胶。
3. 将 `OB_Chassis_Locking_Wedge.stl` 放入锁紧槽。楔块有锥度，注意方向，后续用于锁紧立柱底座。
4. 在 `OB_Chassis_Frame_Joiner.stl` 连接件上涂胶，压紧底盘分块，确认接合到位。


```{figure} _static/media/assembly/chassis-kit.jpg
:alt: 底盘打印件与紧固件
:width: 560px

底盘打印件与紧固件
```

```{figure} _static/media/assembly/chassis-epoxy-surfaces.jpg
:alt: 底盘接合面的涂胶位置
:width: 560px

底盘接合面的涂胶位置
```

```{figure} _static/media/assembly/chassis-locking-wedge.jpg
:alt: 锁紧楔块安装位置
:width: 560px

锁紧楔块安装位置
```

```{figure} _static/media/assembly/chassis-frame-joiner.jpg
:alt: 底盘连接件
:width: 560px

底盘连接件
```

```{figure} _static/media/assembly/chassis-joined-frame.jpg
:alt: 三块底盘拼接后的结构
:width: 560px

三块底盘拼接后的结构
```

### 安装轮舵机与总线

按照片方向安装已设置 ID 的三只轮舵机，并使用舵机随附螺丝固定。连接顺序为：

```text
右后轮 8 → 前轮 9 → 左后轮 10 → 升降舵机 11
```

ID 10 到 ID 11 距离较远，三针线至少 **90 cm**，原始指南推荐 **140 cm**。固定前确认后续能够穿过立柱，并为升降保留余量。


```{figure} _static/media/assembly/wheel-servos.jpg
:alt: 三只轮舵机
:width: 560px

三只轮舵机
```

```{figure} _static/media/assembly/wheel-servo-id-layout.jpg
:alt: 底盘舵机位置与 ID 分配
:width: 560px

底盘舵机位置与 ID 分配
```

```{figure} _static/media/assembly/wheel-servo-cable-routing.jpg
:alt: 轮舵机之间的总线走线
:width: 560px

轮舵机之间的总线走线
```

## 3. 安装全向轮

1. 每个轮轴连接件预装四颗 M3×10 螺丝。
2. 将连接件压在舵机输出盘上，确认四个安装孔对齐。
3. 通过预留操作孔拧紧螺丝。
4. 安装全向轮、轮轴、12×18×4 mm 轴承、垫片与轴承盖。
5. 检查轮组固定和转动情况，避免线缆进入轮子活动范围。


```{figure} _static/media/assembly/wheel-connectors-and-screws.jpg
:alt: 轮轴连接件与 M3×10 螺丝
:width: 560px

轮轴连接件与 M3×10 螺丝
```

```{figure} _static/media/assembly/wheel-connector-on-servo-disc.jpg
:alt: 连接件与舵机输出盘对齐
:width: 560px

连接件与舵机输出盘对齐
```

```{figure} _static/media/assembly/wheel-connector-tightening.jpg
:alt: 从操作孔拧紧连接件
:width: 560px

从操作孔拧紧连接件
```

```{figure} _static/media/assembly/omni-wheel-hardware.jpg
:alt: 全向轮的轴、轴承与紧固件
:width: 560px

全向轮的轴、轴承与紧固件
```

```{figure} _static/media/assembly/omni-wheel-axle-install.jpg
:alt: 安装全向轮轴
:width: 560px

安装全向轮轴
```

```{figure} _static/media/assembly/omni-wheel-cover-installed.jpg
:alt: 装好后的轮组轴承盖
:width: 560px

装好后的轮组轴承盖
```

## 4. 组装升降立柱

从底部向上依次连接：

```text
O_POST4_Connector_Base.stl
  → O_Main_Assembly_Post4.stl
  → OB_Main_Assembly_Post3.stl
  → OB_Main_Assembly_Post2.stl
  → OB_Main_Assembly_Post1.stl
```

逐段在接触面涂胶并压合，在固化前擦去多余胶水，保持齿条与导轨表面干净。


```{figure} _static/media/assembly/lift-tower-parts.jpg
:alt: 升降立柱分段零件
:width: 560px

升降立柱分段零件
```

```{figure} _static/media/assembly/lift-tower-assembled.jpg
:alt: 组装后的升降立柱
:width: 560px

组装后的升降立柱
```

### 将立柱装到底盘

让 **ID 9 的前轮舵机朝向操作者，立柱齿条也朝向操作者**。把六角底座压入底盘座孔，翻转底盘，在六个侧面均匀轻敲，直到法兰完全贴合底盘。

轮舵机线经中心孔与侧边线槽引出，再将底盘翻回正面。检查线路没有被立柱底座或拼接面夹住。


```{figure} _static/media/assembly/tower-in-chassis-orientation.jpg
:alt: 立柱齿条与前轮的方向关系
:width: 560px

立柱齿条与前轮的方向关系
```

```{figure} _static/media/assembly/tower-base-locking.jpg
:alt: 立柱底座固定位置
:width: 560px

立柱底座固定位置
```

```{figure} _static/media/assembly/tower-cable-center-hole.jpg
:alt: 线缆通过底盘中心孔
:width: 560px

线缆通过底盘中心孔
```

```{figure} _static/media/assembly/tower-cable-side-channels.jpg
:alt: 线缆通过侧边线槽
:width: 560px

线缆通过侧边线槽
```

## 5. 组装肩部升降机构

将 **八只 4×13×5 mm 轴承**压入肩部轴承座。每只轴承应安装到位并能够自由转动。

在升降齿轮上预装四颗 M3×10 螺丝，从右侧插入 **12×25 mm 轴**。转动齿轮，让螺丝尖端对齐舵机输出盘孔位，再从侧面操作窗口拧紧。


```{figure} _static/media/assembly/shoulder-bearing-kit.jpg
:alt: 肩部轴承座与导轨轴承
:width: 560px

肩部轴承座与导轨轴承
```

```{figure} _static/media/assembly/shoulder-bearing-install.jpg
:alt: 导轨轴承压入位置
:width: 560px

导轨轴承压入位置
```

```{figure} _static/media/assembly/lift-gear-hardware.jpg
:alt: 升降齿轮及紧固件
:width: 560px

升降齿轮及紧固件
```

```{figure} _static/media/assembly/lift-gear-on-servo.jpg
:alt: 升降齿轮与舵机输出盘配合
:width: 560px

升降齿轮与舵机输出盘配合
```

```{figure} _static/media/assembly/lift-axis-shaft.jpg
:alt: 升降轴安装位置
:width: 560px

升降轴安装位置
```

胶接肩部 T 架，充分固化后再承载机械臂。将 T 架滑入立柱导轨，确认运动顺畅，没有卡滞；若卡滞，先检查支撑残留、胶水溢出、轴承位置与结构配合。


```{figure} _static/media/assembly/shoulder-t-frame.jpg
:alt: 肩部 T 架结构
:width: 560px

肩部 T 架结构
```

```{figure} _static/media/assembly/shoulder-block-on-tower.jpg
:alt: 肩部升降块安装到立柱导轨
:width: 560px

肩部升降块安装到立柱导轨
```

## 6. 安装摄像头

二代硬件配置包含前向、后向、胸部、左腕、右腕五个视角。机身部分先安装顶部两只与胸部一只；腕部相机随机械臂安装。

### 顶部两只相机

拆下相机后盖，把打印支架／盖板放在相机本体与后盖之间，每只使用两颗 **M2×12** 螺丝固定。记录哪只是前向、哪只是后向，后续用于软件映射。


```{figure} _static/media/assembly/top-camera-parts.jpg
:alt: 顶部相机支架零件
:width: 560px

顶部相机支架零件
```

```{figure} _static/media/assembly/top-camera-back-cover.jpg
:alt: 顶部相机后盖安装方式
:width: 560px

顶部相机后盖安装方式
```

```{figure} _static/media/assembly/top-camera-mount-installed.jpg
:alt: 安装完成的顶部相机支架
:width: 560px

安装完成的顶部相机支架
```

### 胸部相机

胸部相机采用相同后盖固定方法，安装到前部支架。检查镜头不会被结构件或线缆遮挡。


```{figure} _static/media/assembly/chest-camera-parts.jpg
:alt: 胸部相机与支架
:width: 560px

胸部相机与支架
```

```{figure} _static/media/assembly/chest-camera-back-cover.jpg
:alt: 胸部相机后盖安装方式
:width: 560px

胸部相机后盖安装方式
```

```{figure} _static/media/assembly/chest-camera-installed.jpg
:alt: 胸部相机安装位置
:width: 560px

胸部相机安装位置
```

## 7. 安装从臂与整理线束

把左右从臂分别固定到肩部 T 架两侧，使用对应的长 M3 内六角螺丝与 M3 螺母。先核对左右位置，再逐步紧固。


```{figure} _static/media/assembly/follower-arms-mounted.jpg
:alt: 肩部 T 架与机械臂安装区域
:width: 560px

肩部 T 架与机械臂安装区域
```

```{figure} _static/media/assembly/follower-arm-fasteners.jpg
:alt: 机械臂安装紧固件
:width: 560px

机械臂安装紧固件
```

```{figure} _static/media/assembly/tower-cable-port.jpg
:alt: 立柱走线孔
:width: 560px

立柱走线孔
```

```{figure} _static/media/assembly/arm-camera-cables-routed.jpg
:alt: 机械臂与相机线穿过立柱
:width: 560px

机械臂与相机线穿过立柱
```

将 **ID 11 升降舵机的三针线连接到左臂舵机驱动板**。检查肩部最高与最低位置的线长余量，不要让插头承担线缆拉力。

| 线束 | 包含线路 |
|---|---|
| 左侧 | 左臂电源、左臂 Type-C、左腕相机 USB、胸部相机 USB、升降舵机线 |
| 右侧 | 右臂电源、右臂 Type-C、右腕相机 USB |

穿好线后套上保护线套，保留接头检查与更换空间。


```{figure} _static/media/assembly/left-cable-bundle.jpg
:alt: 左侧线束
:width: 560px

左侧线束
```

```{figure} _static/media/assembly/right-cable-bundle.jpg
:alt: 右侧线束
:width: 560px

右侧线束
```

```{figure} _static/media/assembly/cable-sleeves-installed.jpg
:alt: 装好保护套的线束
:width: 560px

装好保护套的线束
```

## 8. 安装显示、计算与供电模块

显示屏使用四颗 **M3×6** 螺丝固定到打印支架，再滑入机身后部燕尾槽，连接短 Micro HDMI 线与 Type-C 供电线。显示屏型号与配重质量未在原始 BOM 中完整列出，请结合自己的配置核对。


```{figure} _static/media/assembly/display-bracket-parts.jpg
:alt: 显示屏与打印支架
:width: 560px

显示屏与打印支架
```

```{figure} _static/media/assembly/display-mounted.jpg
:alt: 显示屏安装在后侧燕尾槽
:width: 560px

显示屏安装在后侧燕尾槽
```

```{figure} _static/media/assembly/compute-power-rear-bay.jpg
:alt: 后部空间中的树莓派、降压模块、电池与配重布局
:width: 560px

后部空间中的树莓派、降压模块、电池与配重布局
```

在后部支撑中安装树莓派 5、降压模块、电池与配重。原始组装图采用以下供电分路：

| 路径 | 连接方式 |
|---|---|
| 双从臂 | 电池 1 → 一分二电源线 → 左右臂 DC 线 |
| 计算端 | 电池 2 → 降压模块 → 树莓派 Type-C 电源口 |

上电前按元件标识核对电压、极性和连接位置，完成接线后再供电。主臂位于 PC 侧，使用自己的电源配置。


```{figure} _static/media/assembly/power-wiring.jpg
:alt: 二代机器人供电连接示意
:width: 560px

二代机器人供电连接示意
```

## 9. 分模块检查

首次整机检查采用与二代型号匹配的 Host 和键盘客户端。Pi 上：

```bash
python -m lerobot.robots.alohamini.alohamini_host \
  --robot_model alohamini2 \
  --no_follower
```

PC 上：

```bash
python examples/alohamini/teleoperate_bi.py \
  --robot.remote_ip <Pi_IP> \
  --robot.robot_model alohamini2 \
  --no_leader
```

该步骤需要先完成后续 [软件安装](software.md) 与 [设备配置](configuration.md)。先用短暂、单方向输入检查底盘，再用 U/J 检查升降，完整按键见 [遥操作](teleoperation.md)。

原始装配指南还引用 `examples/debug/wheels.py` 与 `axis.py`。当前这些独立脚本保留自己的舵机型号和几何常量，尤其升降脚本默认 STS3215，而二代使用 STS3095；直接运行前必须核对和适配，详见 [调试与排错](troubleshooting.md)。

检查结果应包括：轮组运动无干涉、升降无卡滞、线束无拉扯、左右臂固定可靠、相机可识别、供电连接稳定。发现异常先返回对应装配步骤，再进入下一阶段。

## 下一步：配置与校准

依次完成 [设备配置](configuration.md) → [机械臂校准](calibration.md) → [遥操作](teleoperation.md)。硬件装好后仍需要正确的机型、串口与校准数据，不能直接跳到策略执行。

来源：[原始完整组装指南](https://github.com/liyiteng/AlohaMini/blob/main/AlohaMini2/docs/assembly_guide.md)。
