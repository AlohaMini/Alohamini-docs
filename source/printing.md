# AlohaMini 2 · 3D 打印

**适用型号：标准 AlohaMini 2。** Pro 用户请先阅读 [2 Pro 硬件说明](hardware-pro.md)；本页的物料数量、打印件和装配照片对应标准版。

二代 Mobile Base 2 采用分块打印方案，面向 Bambu P2S 级消费打印机。本页列出机身全部推荐打印文件、数量、材料与装配前检查；机械臂打印件请使用 AM-ARM200 对应版本。

## 获取正确文件

在硬件仓库根目录查找：

```text
AlohaMini2/hardware/mobile_base2/stl/
```

[打开 STL 目录](https://github.com/liyiteng/AlohaMini/tree/main/AlohaMini2/hardware/mobile_base2/stl)。目录中同时包含普通底盘分块与 `PrintOptimized` 版本，下面的清单使用优化版本，不需要把两套底盘都打印。

## 推荐切片参数

| 参数 | 原始指南建议 | 使用说明 |
|---|---|---|
| 材料 | PLA、PETG、ABS 等 FDM 材料 | 根据设备能力、结构用途与打印经验选择 |
| 墙层数 | 4–6 层 | 承载结构优先使用 6 层 |
| 填充率 | 15–25% | 与墙层、打印方向一起影响成品强度 |
| 支撑 | 按切片器判断启用 | 检查轴孔、齿条、线槽与安装腔的支撑可清理性 |

原始指南没有固定喷嘴直径、层高、喷嘴温度或打印速度。请使用你所选材料与打印机的已验证配置，不把这里的墙层、填充建议当作完整材料配置。

## 材料选择

| 材料 | 适用考虑 | 打印时关注 |
|---|---|---|
| PLA | 容易打印，适合验证装配与一般测试 | 耐热性较低，注意使用环境 |
| PETG | 韧性较好 | 易拉丝，齿条与齿轮附近支撑可能粘连；可考虑 PLA 或专用支撑界面材料 |
| ABS | 原始指南作为较高耐热需求的选项 | 更易翘曲，需要封闭打印环境与适合材料的温控 |

最终强度还取决于层间结合、零件方向、胶接和紧固质量。承载部件打印后应先检查裂纹、翘曲和装配间隙。

## 完整打印清单

除表中注明数量外，每个 STL 打印一件。使用金属钢销或铝型材时，跳过相应的打印替代件。

| STL 文件 | 数量 | 用途／说明 |
|---|---:|---|
| `O_Chassis_Dowel_Pin_12_80.stl` | 3 | 底盘钢销的打印替代件 |
| `O_Main_Assembly_Post4.stl` | 1 |  |
| `O_POST4_Connector_Base.stl` | 1 |  |
| `O_T_Connector_Cross_Bar.stl` | 1 | T 架铝型材的打印替代件 |
| `O_T_Connector_Dowel_Pin_12_25.stl` | 1 | 升降轴钢销的打印替代件 |
| `OB_Buck_Converter_Mount.stl` | 1 |  |
| `OB_Chassis_Bearing_Cover.stl` | 3 |  |
| `OB_Chassis_Frame_Joiner.stl` | 3 |  |
| `OB_Chassis_Locking_Wedge.stl` | 3 |  |
| `OB_Chassis_Segment_1of3_PrintOptimized.stl` | 3 | 推荐的底盘分块版本 |
| `OB_Chassis_Wheel_Axle_Connector.stl` | 3 |  |
| `OB_Main_Assembly_Post1.stl` | 1 |  |
| `OB_Main_Assembly_Post2.stl` | 1 |  |
| `OB_Main_Assembly_Post3.stl` | 1 |  |
| `OB_Main_Monitor_Connector.stl` | 1 |  |
| `OB_POST4_Mount_Adapter.stl` | 1 |  |
| `OB_POST4_RPi_Mount.stl` | 1 |  |
| `OB_T_Camera_Mount.stl` | 1 |  |
| `OB_T_Connector_Left.stl` | 1 |  |
| `OB_T_Connector_Middle.stl` | 1 |  |
| `OB_T_Connector_Right.stl` | 1 |  |
| `OB_Top_Camera_Back_Cover.stl` | 2 |  |
| `OB_Top_Camera_Mount.stl` | 1 |  |
| `OB_Z_Axis_Servo_Gear.stl` | 1 |  |


## 底盘与承载件

底盘分块面积较大，打印前查看首层接触、支撑、接合面和翘曲风险。推荐文件：

```text
OB_Chassis_Segment_1of3_PrintOptimized.stl
```

三块底盘之间依靠连接件、锁紧楔块和胶接形成整体。组装前先干装，确认拼缝和立柱底座孔配合正常，再进入胶接步骤。

T 架横梁、底盘钢销、升降轴钢销均提供打印替代件。原始指南明确指出这些替代件会显著降低结构强度；最终承载版本优先采用 BOM 中的金属件。

## 打印盘布局参考

```{figure} _static/media/bambu-studio-plate-layout.jpg
:alt: AlohaMini 2 结构件在 Bambu Studio 中的分盘布局
:width: 100%

原始指南中的分盘示意。实际支撑与摆放请结合当前 STL 和切片结果检查。
```

## 装配前逐项检查

- **底盘：** 清理轮舱、线槽、销孔和锁紧楔块槽，拼接面无支撑残留。
- **立柱：** 各段接合面平整，齿条连续，走线孔贯通。
- **肩部：** 轴承安装孔无毛刺，压入后轴承能自由转动。
- **齿轮：** 齿面完整，没有支撑粘连或明显变形。
- **相机与显示支架：** 螺孔、盖板和滑槽先试配，不强行拧入不匹配的螺丝。
- **热熔螺母位置：** 按机械臂与结构图确认规格，避免安装后遮挡装配路径。

打印件齐备后，按照 [硬件组装](assembly.md) 从舵机 ID 与底盘开始。

来源：[原始打印指南](https://github.com/liyiteng/AlohaMini/blob/main/AlohaMini2/docs/print_guide.md)。
