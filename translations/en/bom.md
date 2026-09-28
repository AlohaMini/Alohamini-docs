# AlohaMini 2 Bill of Materials

**applicable model: Standard AlohaMini 2.** Pro users please read the [2 Pro hardware](hardware-pro.md) first; the material quantity, printouts and assembly photos on this page correspond to the standard version.

This page is based on the **standard AlohaMini 2**, split by mobile chassis, dual follower arms, dual leader arms and consumables. The quantity, specifications and reference quotation are compiled from the project BOM; the servos and metal chassis of the 2 Pro need to be checked separately according to the corresponding configuration.

## First clarify the scope of procurement

| part | location | Purpose |
| --- | --- | --- |
| Mobile chassis, lifting, Raspberry Pi, camera | Robot Host | Drive the robot and return status and images |
| Two AM-ARM200 follower arms | robot shoulder | Perform grasping and dual-arm tasks |
| Two leader arms, control board, leader arm power supply | PC Client | Manual teaching by operator |
| PC workstation | console | teleoperation and recording; training also requires corresponding computing resources |

**The original quotation does not include the cost of PC, printer, common tools and about 5 kg of printing supplies.** Overseas and domestic prices are independent estimates of the original BOM, not selling prices converted at real-time exchange rates; purchase links do not represent verified inventory.

## budget summary

| module | RMB reference | dollar reference |
| --- | ---: | ---: |
| Mobile chassis and robot end | ¥2,475 | About $344 |
| double follower arm | ¥3,320 | About $461 |
| Double leader arm | ¥1,646 | About $277 |
| Fasteners and consumables | ¥107 | About $15 |
| **Total self-printing solutions** | **¥7,548** | **About $1,097** |

The module summary follows the original BOM; there are differences in whole package purchases, estimated prices, and procurement in different regions, and each column cannot be regarded as an accurate settlement document. The final budget is based on actual selection, shipping costs and shopping cart.

## Mobile chassis and robot end

| Material | Specifications | Quantity | USD unit price | Overseas purchasing reference | RMB unit price | Domestic purchasing reference |
| ------ | ------ | ----: | ---------: | ---------- | --------: | ---------- |
| Wheel servo STS-3215 | ST-3215-C018, 12V, 1/345 reduction ratio | 3 | $15.97 | [Alibaba](https://www.alibaba.com/product-detail/Lerobot-360-Degree-Smart-Servo-for_1601563310522.html) | ¥110 | [Taobao](https://e.tb.cn/h.64H9u3maGWzIp5Q?tk=T5liexkG6Yz) |
| Elevator servo STS-3095 | ST-3095-C002, 12V, 95 kg·cm | 1 | $50.37 | [Alibaba](https://www.alibaba.com/product-detail/FEETECH-STS3095-12V-95KG-servo-AI_1601045980686.html) | ¥345 | [Taobao](https://item.taobao.com/item.htm?abbucket=18&id=764857479703) |
| Omni wheel | 127 mm (74A) | 3 | $40 | [omniawheel.com](https://www.omniawheel.com/) | ¥289 | [Taobao](http://e.tb.cn/h.R5jm5Xlk56vjQRJ) |
| T frame aluminum profile | 20×40×2 mm, L=400 mm * (or print `O_T_Connector_Cross_Bar.stl` ) * | 1 | ~$1.50 | — | ¥10 | — |
| Chassis steel pin | Φ12×80 mm * (or print `O_Chassis_Dowel_Pin_12_80.stl` ) * | 3 | ~$0.50 | Amazon | ¥3.28 | [Taobao](https://e.tb.cn/h.ivppuOirL8K8zsH?tk=IKNy5kRfNCm) |
| Lifting shaft steel pin | Φ12×25 mm * (or print `O_T_Connector_Dowel_Pin_12_25.stl` ) * | 1 | ~$0.50 | Amazon | ¥3.28 | [Taobao](https://e.tb.cn/h.ivppuOirL8K8zsH?tk=IKNy5kRfNCm) |
| Lifting guide bearings | 4×13×5 mm | 8 | ~$0.40 | Amazon | ¥3 | [Taobao](https://item.taobao.com/item.htm?id=565418362178) |
| Chassis/robot arm/lift bearing | 12×18×4 mm | 8 | ~$0.80 | [Amazon](https://www.amazon.com/XIKE-6701-2RS-Bearings-12x18x4mm-Pre-Lubricated/dp/B09D2RQ4Y1) | ¥6 | [Tmall](https://detail.tmall.com/item.htm?id=824704356695) |
| forward facing camera | H65V1, 720p, 2.4 mm, 1 m cable length | 1 | ~$17 | Amazon | ¥122 | [Taobao](https://item.taobao.com/item.htm?id=666278411821) |
| rear facing camera | H65V1, 720p, 2.4 mm, 1 m cable length | 1 | ~$17 | Amazon | ¥122 | [Taobao](https://item.taobao.com/item.htm?id=666278411821) |
| boobs cam | H65V1, 720p, 2.4 mm, 2 m cable length | 1 | ~$17 | Amazon | ¥122 | [Taobao](https://item.taobao.com/item.htm?id=666278411821) |
| Raspberry Pi 5 | 2 GB RAM | 1 | ~$93 | [Adafruit](https://www.adafruit.com/product/5812) | ¥669 | [Taobao](https://item.taobao.com/item.htm?id=688878446695) |
| DC step-down module | 12V→5V 5A (PD protocol) | 1 | ~$9 | [Amazon](https://www.amazon.com/Klnuoxj-Converter-Interface-Waterproof-Compatible/dp/B0CRVW7N2J) | ¥66 | [Taobao](https://item.taobao.com/item.htm?id=800698078303) |
| heat sink | Raspberry Pi 5 passive heat sink | 1 | ~$2.50 | Amazon | ¥18 | [Taobao](https://item.taobao.com/item.htm?id=755560852039) |
| microSD memory card | 32 GB | 1 | ~$14 | Amazon | ¥99.9 | — |
| HDMI to Micro HDMI cable | 1 m, 4K60Hz | 1 | ~$1 | Amazon | ¥7 | [pinduoduo](https://mobile.yangkeduo.com/goods.html?ps=9DevREvDAj) |
| Bus servo control board | Waveshare Bus Servo Adapter A | 1 | $5.00 | [Waveshare](https://www.waveshare.com/bus-servo-adapter-a.htm) | ¥27 | [Tmall](https://detail.tmall.com/item.htm?id=738817173460) |
| 12V battery | 11200 mAh, DC 5521 | 2 | ~$16 | [Amazon](https://www.amazon.com/KBT-Rechargeable-Connector-Replacement-Security/dp/B0C242DYT1/) | ¥114 | [Taobao](https://item.taobao.com/item.htm?id=890828103056) |
| DC one-to-two power cord | 1-to-2, 30 cm | 1 | ~$0.60 | Amazon | ¥4.5 | [Taobao](https://e.tb.cn/h.ivLJNFtMOZ50iFx?tk=GN8V5ki58UN) |
| DC power extension cord | 1 m | 2 | ~$0.30 | Amazon | ¥2.3 | [Taobao](https://e.tb.cn/h.iucAEva43LkxQz1?tk=INAY5k79Qyz) |
| Servo extension cable | 90 cm, Feetech 3-pin | 2 | ~$0.30 | [Alibaba](https://www.alibaba.com/product-detail/3P-5264-Interface-Bus-Actuator-Connection_1601635790774.html) | ¥2 | Feite channel |
| 3D prints | PLA/PETG/ABS, Bambu P2S | — | Approx. 4 kg consumables | — | — | `/AlohaMini2/hardware/mobile_base2/stl/` |

---

## Double follower arms (two in total)

Each follower arm is based on AM-ARM200, with nominal **6+1 degree of freedom, 52 cm arm span, and 1 kg load**. The following quantities are the total of the two follower arms.

| Material | Specifications | Quantity | USD unit price | Overseas purchasing reference | RMB unit price | Domestic purchasing reference |
| ------ | ------ | ----: | ---------: | ---------- | --------: | ---------- |
| Servo STS-3215 | ST-3215-C018, 12V, 1/345 reduction ratio | 8 | $15.97 | [Alibaba](https://www.alibaba.com/product-detail/Lerobot-360-Degree-Smart-Servo-for_1601563310522.html) | ¥110 | [Taobao](https://e.tb.cn/h.64H9u3maGWzIp5Q?tk=T5liexkG6Yz) |
| Servo STS-3095 | ST-3095-C002, 12V, 95 kg·cm | 6 | $50.37 | [Alibaba](https://www.alibaba.com/product-detail/FEETECH-STS3095-12V-95KG-servo-AI_1601045980686.html) | ¥345 | [Taobao](https://item.taobao.com/item.htm?abbucket=18&id=764857479703) |
| M3×10 hexagon socket screws | 100 pieces/pack | 2 pack | — | — | ¥6 | [Taobao](https://e.tb.cn/h.R0nMFj8y9riNyJl?tk=HNii5rHz4NJ) |
| heat-set inserts | M3×5×4 | 1 pack | — | Amazon | ¥5 | [Taobao](https://item.taobao.com/item.htm?id=809241671998) |
| Servo extension cable | SCS 3-pin, 26 cm | 12 | $0.43 | [AliExpress](https://www.aliexpress.com/item/1005008074862037.html) | ¥3 | [Taobao](https://item.taobao.com/item.htm?id=616460581906) |
| wrist camera | H65V1, 720p, 2.4 mm, 2 m cable length | 2 | ~$17 | Amazon | ¥122 | [Taobao](https://item.taobao.com/item.htm?id=666278411821) |
| Bus servo control board | Waveshare Bus Servo Adapter A | 2 | $5.00 | [Waveshare](https://www.waveshare.com/bus-servo-adapter-a.htm) | ¥27 | [Tmall](https://detail.tmall.com/item.htm?id=738817173460) |
| USB Type-C data cable | 1 m (Robotic arm → Raspberry Pi 5) | 4 | — | — | ¥4.8 | [pinduoduo](https://mobile.yangkeduo.com/goods1.html?ps=fDPvH0kvgs) |
| 3D prints | PLA/PETG/ABS, Bambu P2S | — | — | — | — | [AM-ARM200 print file](https://github.com/liyiteng/AM-ARM/tree/main/am-arm200) |

---

## Double leader arms (two total)

| Material | Specifications | Quantity | USD unit price | Overseas purchasing reference | RMB unit price | Domestic purchasing reference |
| ------ | ------ | ----: | ---------: | ---------- | --------: | ---------- |
| Servo STS-3215 | ST-3215-C046, 7.4V, 1/147 reduction ratio | 14 | $15.97 | [Alibaba](https://www.alibaba.com/product-detail/Lerobot-360-Degree-Smart-Servo-for_1601563310522.html) | ¥110 | [Taobao](https://e.tb.cn/h.64H9u3maGWzIp5Q?tk=T5liexkG6Yz) |
| heat-set inserts | M3×5×4 | 1 pack | — | Amazon | ¥5 | [Taobao](https://item.taobao.com/item.htm?id=809241671998) |
| Bus servo control board | Waveshare | 2 | $12.47 | [Amazon](https://www.amazon.com/Waveshare-Integrates-Control-Circuit-Supports/dp/B0CTMM4LWK/) | ¥27 | [Tmall](https://detail.tmall.com/item.htm?id=738817173460) |
| 5V power adapter | DC 5V AC adapter | 1 | $12.99 | [Amazon](https://www.amazon.com/Facmogu-Switching-Transformer-Compatible-5-5x2-1mm/dp/B087LY41PV/) | — | — |
| USB Type-C data cable | 1 m (robot → PC) | 2 | $7.19 | [Amazon](https://www.amazon.com/Charging-etguuds-Charger-Braided-Compatible/dp/B0B8NWLLW2/) | ¥20 | [Tmall](https://detail.tmall.com/item.htm?id=754024805047) |
| DC one-to-two power cord | 1-to-2, 70 cm | 1 | — | — | ¥6.5 | [Taobao](https://e.tb.cn/h.ivLJNFtMOZ50iFx?tk=GN8V5ki58UN) |
| 3D prints | PLA/PETG/ABS, Bambu P2S | — | — | — | — | [AM-ARM200 print file](https://github.com/liyiteng/AM-ARM/tree/main/am-arm200) |

---

## Fasteners and consumables

| Material | Specifications | Quantity | USD unit price | Overseas purchasing reference | RMB unit price | Domestic purchasing reference |
| ------ | ------ | ----: | ---------: | ---------- | --------: | ---------- |
| M3 heat-set inserts | M3×5×4 mm, 50 pieces/pack | 1 pack | ~$0.30 | Amazon | ¥2.2 | — |
| M3×10 hexagon socket screws | 100 pieces/pack, blue thread lock | 3 pack | ~$1.20 | — | ¥8.5 | — |
| M3×18 hexagon socket screws | 50 pieces/pack | 1 pack | ~$0.65 | — | ¥4.72 | — |
| Epoxy glue | Loctite E-120HP 50 mL | 1 | ~$10 | Amazon | ¥74.9 | — |

---


## It’s easy to buy the wrong specifications

1. **distinguishes the leader arm and follower arm servos. The BOM of the** leader arm is ST-3215-C046, 7.4V, 1/147 reduction ratio; the STS-3215 in the follower arm is C018, 12V, 1/345. The leader arm workflow adopts 5V power supply configuration and cannot directly apply the 12V power supply of the follower arm.
2. For **elevator servo, choose STS-3095. The lifting structure and model configuration of the second generation** are different from those of the first generation. It cannot be replaced with the first generation STS-3215 just because the interface is the same.
3. **Check bearing size.** 4×13×5 mm guide rail bearings have different uses than 12×18×4 mm bearings. Keep dimensional records when purchasing.
4. **Checks whether the USB cable supports data.** leader and follower arms control board requires data connection; cables with only charging function cannot complete serial communication.
5. Reserved length for **lifting cables. The** assembly guide requires that the three-pin line from ID 10 to ID 11 be at least 90 cm, and 140 cm is recommended; the length can be determined after confirming the wiring of the entire robot stroke.
6. **Confirm whether the metal part is a printed replacement part. There are printing alternatives for** steel pins and T-frame aluminum profiles, but the structural strength will be reduced after replacement.

## Tools and arrival inspection

Prepare hexagonal socket tools for fasteners, screwdrivers, tools to clean supports, epoxy glue and heat-set inserts installation tools. The original BOM does not list table clamps, soldering irons, and general tools, and the leader arm console also needs to be stably fixed.

After arrival, the bags are divided into modules: wheel set, lifting set, camera set, left and right arms, and power supply. Check the servo model, control board, wire length and fastener quantity one by one; the original assembly also uses M2×12 camera screws and M3×6 display screws, so you should check whether the accessory package is included.

The display and counterweight appear in the assembly guide, but the original BOM does not fully provide its model number, quality, and independent quotation. When you need to adopt this layout, first check the physical installation dimensions and the corresponding structural diagram to avoid mistaking the total price in the table as covering all accessories.

## Design files and next steps

- [Mobile chassis STL and CAD](https://github.com/liyiteng/AlohaMini/tree/main/AlohaMini2/hardware/mobile_base2)
- [AM-ARM200 robotic arm structure and assembly](https://github.com/liyiteng/AM-ARM/tree/main/am-arm200)
- [Original complete BOM](https://github.com/liyiteng/AlohaMini/blob/main/AlohaMini2/docs/BOM.md)

After preparing the materials, proceed to [3D printing](printing.md) and [Assembly](assembly.md).
