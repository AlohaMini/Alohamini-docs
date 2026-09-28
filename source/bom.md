# AlohaMini 2 物料清单

**适用型号：标准 AlohaMini 2。** Pro 用户请先阅读 [2 Pro 硬件说明](hardware-pro.md)；本页的物料数量、打印件和装配照片对应标准版。

本页面向 **标准 AlohaMini 2**，按移动底盘、双从臂、双主臂和耗材拆分。数量、规格与参考报价整理自项目 BOM；2 Pro 的舵机和金属底盘需按对应配置单独核对。

## 先明确采购范围

| 部分 | 所在位置 | 用途 |
|---|---|---|
| 移动底盘、升降、树莓派、相机 | 机器人端 Host | 驱动机器人并回传状态、图像 |
| 两只 AM-ARM200 从臂 | 机器人肩部 | 执行抓取与双臂任务 |
| 两只主臂、控制板、主臂电源 | 电脑端 Client | 由操作者手动示教 |
| PC 工作站 | 操作台 | 遥操作、录制；训练还需要相应计算资源 |

**原始报价不包含 PC、打印机、常用工具及约 5 kg 的打印耗材成本。** 海外与国内价格是原始 BOM 的独立估算，不是按实时汇率换算的售价；采购链接也不代表已核实库存。

## 预算汇总

| 模块 | 人民币参考 | 美元参考 |
|---|---:|---:|
| 移动底盘与机器人端 | ¥2,475 | 约 $344 |
| 双从臂 | ¥3,320 | 约 $461 |
| 双主臂 | ¥1,646 | 约 $277 |
| 紧固件与耗材 | ¥107 | 约 $15 |
| **自打印方案合计** | **¥7,548** | **约 $1,097** |

模块汇总沿用原始 BOM；其中存在整包购买、估算价与不同地区采购差异，不能将每一列都当作精确结算单。最终预算以实际选型、运费与购物车为准。

## 移动底盘与机器人端

| 物料 | 规格 | 数量 | 美元单价 | 海外采购参考 | 人民币单价 | 国内采购参考 |
|------|------|----:|---------:|----------|--------:|----------|
| 轮式舵机 STS-3215 | ST-3215-C018, 12V, 1/345 减速比 | 3 | $15.97 | [Alibaba](https://www.alibaba.com/product-detail/Lerobot-360-Degree-Smart-Servo-for_1601563310522.html) | ¥110 | [Taobao](https://e.tb.cn/h.64H9u3maGWzIp5Q?tk=T5liexkG6Yz) |
| 升降舵机 STS-3095 | ST-3095-C002, 12V, 95 kg·cm | 1 | $50.37 | [Alibaba](https://www.alibaba.com/product-detail/FEETECH-STS3095-12V-95KG-servo-AI_1601045980686.html) | ¥345 | [Taobao](https://item.taobao.com/item.htm?abbucket=18&id=764857479703) |
| 全向轮 | 127 mm (74A) | 3 | $40 | [omniawheel.com](https://www.omniawheel.com/) | ¥289 | [Taobao](http://e.tb.cn/h.R5jm5Xlk56vjQRJ) |
| T 架铝型材 | 20×40×2 mm, L=400 mm *(或打印 `O_T_Connector_Cross_Bar.stl`)* | 1 | ~$1.50 | — | ¥10 | — |
| 底盘钢销 | Φ12×80 mm *(或打印 `O_Chassis_Dowel_Pin_12_80.stl`)* | 3 | ~$0.50 | Amazon | ¥3.28 | [Taobao](https://e.tb.cn/h.ivppuOirL8K8zsH?tk=IKNy5kRfNCm) |
| 升降轴钢销 | Φ12×25 mm *(或打印 `O_T_Connector_Dowel_Pin_12_25.stl`)* | 1 | ~$0.50 | Amazon | ¥3.28 | [Taobao](https://e.tb.cn/h.ivppuOirL8K8zsH?tk=IKNy5kRfNCm) |
| 升降导轨轴承 | 4×13×5 mm | 8 | ~$0.40 | Amazon | ¥3 | [Taobao](https://item.taobao.com/item.htm?id=565418362178) |
| 底盘／机械臂／升降轴承 | 12×18×4 mm | 8 | ~$0.80 | [Amazon](https://www.amazon.com/XIKE-6701-2RS-Bearings-12x18x4mm-Pre-Lubricated/dp/B09D2RQ4Y1) | ¥6 | [Tmall](https://detail.tmall.com/item.htm?id=824704356695) |
| 前向摄像头 | H65V1, 720p, 2.4 mm, 1 m 线长 | 1 | ~$17 | Amazon | ¥122 | [Taobao](https://item.taobao.com/item.htm?id=666278411821) |
| 后向摄像头 | H65V1, 720p, 2.4 mm, 1 m 线长 | 1 | ~$17 | Amazon | ¥122 | [Taobao](https://item.taobao.com/item.htm?id=666278411821) |
| 胸部摄像头 | H65V1, 720p, 2.4 mm, 2 m 线长 | 1 | ~$17 | Amazon | ¥122 | [Taobao](https://item.taobao.com/item.htm?id=666278411821) |
| 树莓派 5 | 2 GB RAM | 1 | ~$93 | [Adafruit](https://www.adafruit.com/product/5812) | ¥669 | [Taobao](https://item.taobao.com/item.htm?id=688878446695) |
| 直流降压模块 | 12V→5V 5A (PD 协议) | 1 | ~$9 | [Amazon](https://www.amazon.com/Klnuoxj-Converter-Interface-Waterproof-Compatible/dp/B0CRVW7N2J) | ¥66 | [Taobao](https://item.taobao.com/item.htm?id=800698078303) |
| 散热片 | 树莓派 5 被动散热片 | 1 | ~$2.50 | Amazon | ¥18 | [Taobao](https://item.taobao.com/item.htm?id=755560852039) |
| microSD 存储卡 | 32 GB | 1 | ~$14 | Amazon | ¥99.9 | — |
| HDMI 转 Micro HDMI 线 | 1 m, 4K60Hz | 1 | ~$1 | Amazon | ¥7 | [pinduoduo](https://mobile.yangkeduo.com/goods.html?ps=9DevREvDAj) |
| 总线舵机控制板 | Waveshare Bus Servo Adapter A | 1 | $5.00 | [Waveshare](https://www.waveshare.com/bus-servo-adapter-a.htm) | ¥27 | [Tmall](https://detail.tmall.com/item.htm?id=738817173460) |
| 12V 电池 | 11200 mAh, DC 5521 | 2 | ~$16 | [Amazon](https://www.amazon.com/KBT-Rechargeable-Connector-Replacement-Security/dp/B0C242DYT1/) | ¥114 | [Taobao](https://item.taobao.com/item.htm?id=890828103056) |
| DC 一分二电源线 | 1-to-2, 30 cm | 1 | ~$0.60 | Amazon | ¥4.5 | [Taobao](https://e.tb.cn/h.ivLJNFtMOZ50iFx?tk=GN8V5ki58UN) |
| DC 电源延长线 | 1 m | 2 | ~$0.30 | Amazon | ¥2.3 | [Taobao](https://e.tb.cn/h.iucAEva43LkxQz1?tk=INAY5k79Qyz) |
| 舵机延长线 | 90 cm, Feetech 3-pin | 2 | ~$0.30 | [Alibaba](https://www.alibaba.com/product-detail/3P-5264-Interface-Bus-Actuator-Connection_1601635790774.html) | ¥2 | 飞特渠道 |
| 3D 打印件 | PLA/PETG/ABS, Bambu P2S | — | 约 4 kg 耗材 | — | — | `/AlohaMini2/hardware/mobile_base2/stl/` |

---

## 双从臂（两只合计）

每只从臂基于 AM-ARM200，标称 **6+1 自由度、52 cm 臂展、1 kg 负载**。以下数量为两只从臂的合计。

| 物料 | 规格 | 数量 | 美元单价 | 海外采购参考 | 人民币单价 | 国内采购参考 |
|------|------|----:|---------:|----------|--------:|----------|
| 舵机 STS-3215 | ST-3215-C018, 12V, 1/345 减速比 | 8 | $15.97 | [Alibaba](https://www.alibaba.com/product-detail/Lerobot-360-Degree-Smart-Servo-for_1601563310522.html) | ¥110 | [Taobao](https://e.tb.cn/h.64H9u3maGWzIp5Q?tk=T5liexkG6Yz) |
| 舵机 STS-3095 | ST-3095-C002, 12V, 95 kg·cm | 6 | $50.37 | [Alibaba](https://www.alibaba.com/product-detail/FEETECH-STS3095-12V-95KG-servo-AI_1601045980686.html) | ¥345 | [Taobao](https://item.taobao.com/item.htm?abbucket=18&id=764857479703) |
| M3×10 内六角螺丝 | 100 只／包 | 2 包 | — | — | ¥6 | [Taobao](https://e.tb.cn/h.R0nMFj8y9riNyJl?tk=HNii5rHz4NJ) |
| 热熔螺母 | M3×5×4 | 1 包 | — | Amazon | ¥5 | [Taobao](https://item.taobao.com/item.htm?id=809241671998) |
| 舵机延长线 | SCS 3-pin, 26 cm | 12 | $0.43 | [AliExpress](https://www.aliexpress.com/item/1005008074862037.html) | ¥3 | [Taobao](https://item.taobao.com/item.htm?id=616460581906) |
| 腕部摄像头 | H65V1, 720p, 2.4 mm, 2 m 线长 | 2 | ~$17 | Amazon | ¥122 | [Taobao](https://item.taobao.com/item.htm?id=666278411821) |
| 总线舵机控制板 | Waveshare Bus Servo Adapter A | 2 | $5.00 | [Waveshare](https://www.waveshare.com/bus-servo-adapter-a.htm) | ¥27 | [Tmall](https://detail.tmall.com/item.htm?id=738817173460) |
| USB Type-C 数据线 | 1 m (机械臂 → 树莓派 5) | 4 | — | — | ¥4.8 | [pinduoduo](https://mobile.yangkeduo.com/goods1.html?ps=fDPvH0kvgs) |
| 3D 打印件 | PLA/PETG/ABS, Bambu P2S | — | — | — | — | [AM-ARM200 打印文件](https://github.com/liyiteng/AM-ARM/tree/main/am-arm200) |

---

## 双主臂（两只合计）

| 物料 | 规格 | 数量 | 美元单价 | 海外采购参考 | 人民币单价 | 国内采购参考 |
|------|------|----:|---------:|----------|--------:|----------|
| 舵机 STS-3215 | ST-3215-C046, 7.4V, 1/147 减速比 | 14 | $15.97 | [Alibaba](https://www.alibaba.com/product-detail/Lerobot-360-Degree-Smart-Servo-for_1601563310522.html) | ¥110 | [Taobao](https://e.tb.cn/h.64H9u3maGWzIp5Q?tk=T5liexkG6Yz) |
| 热熔螺母 | M3×5×4 | 1 包 | — | Amazon | ¥5 | [Taobao](https://item.taobao.com/item.htm?id=809241671998) |
| 总线舵机控制板 | Waveshare | 2 | $12.47 | [Amazon](https://www.amazon.com/Waveshare-Integrates-Control-Circuit-Supports/dp/B0CTMM4LWK/) | ¥27 | [Tmall](https://detail.tmall.com/item.htm?id=738817173460) |
| 5V 电源适配器 | DC 5V AC adapter | 1 | $12.99 | [Amazon](https://www.amazon.com/Facmogu-Switching-Transformer-Compatible-5-5x2-1mm/dp/B087LY41PV/) | — | — |
| USB Type-C 数据线 | 1 m (机械臂 → PC) | 2 | $7.19 | [Amazon](https://www.amazon.com/Charging-etguuds-Charger-Braided-Compatible/dp/B0B8NWLLW2/) | ¥20 | [Tmall](https://detail.tmall.com/item.htm?id=754024805047) |
| DC 一分二电源线 | 1-to-2, 70 cm | 1 | — | — | ¥6.5 | [Taobao](https://e.tb.cn/h.ivLJNFtMOZ50iFx?tk=GN8V5ki58UN) |
| 3D 打印件 | PLA/PETG/ABS, Bambu P2S | — | — | — | — | [AM-ARM200 打印文件](https://github.com/liyiteng/AM-ARM/tree/main/am-arm200) |

---

## 紧固件与耗材

| 物料 | 规格 | 数量 | 美元单价 | 海外采购参考 | 人民币单价 | 国内采购参考 |
|------|------|----:|---------:|----------|--------:|----------|
| M3 热熔螺母 | M3×5×4 mm, 50 只／包 | 1 包 | ~$0.30 | Amazon | ¥2.2 | — |
| M3×10 内六角螺丝 | 100 只／包，蓝色螺纹锁固 | 3 包 | ~$1.20 | — | ¥8.5 | — |
| M3×18 内六角螺丝 | 50 只／包 | 1 包 | ~$0.65 | — | ¥4.72 | — |
| 环氧胶 | Loctite E-120HP 50 mL | 1 | ~$10 | Amazon | ¥74.9 | — |

---


## 容易买错的规格

1. **区分主臂和从臂舵机。** 主臂 BOM 是 ST-3215-C046、7.4V、1/147 减速比；从臂中的 STS-3215 是 C018、12V、1/345。主臂工作流采用 5V 供电配置，不能直接套用从臂 12V 电源。
2. **升降舵机选 STS-3095。** 二代的升降结构和机型配置与一代不同，不能只因为接口相同就替换成一代的 STS-3215。
3. **核对轴承尺寸。** 4×13×5 mm 导轨轴承与 12×18×4 mm 轴承用途不同，采购时保留尺寸记录。
4. **检查 USB 线是否支持数据。** 主从臂控制板需要数据连接；只有充电功能的线不能完成串口通信。
5. **升降走线预留长度。** 组装指南要求 ID 10 到 ID 11 的三针线至少 90 cm，推荐 140 cm；按机器人全行程布线确认后再定长度。
6. **确认金属件还是打印替代件。** 钢销与 T 架铝型材均有打印替代方案，但替代后结构强度会降低。

## 工具与到货检查

准备适配紧固件的内六角工具、螺丝刀、清理支撑的工具、环氧胶和热熔螺母安装工具。原始 BOM 未列出桌夹、烙铁和通用工具，主臂操作台也需要稳定固定。

到货后先按模块分袋：轮组、升降组、相机组、左右臂、电源。逐一核对舵机型号、控制板、线长和紧固件数量；原始组装还使用 M2×12 相机螺丝与 M3×6 显示屏螺丝，应检查配件包是否包含。

显示屏与配重出现在组装指南中，但原始 BOM 没有完整给出其型号、质量与独立报价。需要采用这套布局时，先核对实物安装尺寸与对应结构图，避免把表中总价误认为已覆盖所有附件。

## 设计文件与下一步

- [移动底盘 STL 与 CAD](https://github.com/liyiteng/AlohaMini/tree/main/AlohaMini2/hardware/mobile_base2)
- [AM-ARM200 机械臂结构与组装](https://github.com/liyiteng/AM-ARM/tree/main/am-arm200)
- [原始完整 BOM](https://github.com/liyiteng/AlohaMini/blob/main/AlohaMini2/docs/BOM.md)

备齐物料后，继续 [3D 打印](printing.md) 与 [硬件组装](assembly.md)。
