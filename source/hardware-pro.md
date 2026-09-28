# AlohaMini 2 Pro 硬件说明

已补充官方 [2 / 2 Pro 开箱接线照片](unboxing.md)，覆盖交付整机的电池、电源板、树莓派和主臂连接；零件级 Pro 装配资料仍按下文范围说明。

本页用于核对 **AlohaMini 2 Pro** 的硬件与软件配置。已有完整机器人时，核对下表后进入 [2 Pro 入门教程](alohamini2pro.md)。

## 已确认的配置

| 部分 | Pro 配置 | 对软件的影响 |
|---|---|---|
| 底盘 | 金属强化底盘 | 按 Pro 实物与套件资料核对装配 |
| 底盘轮舵机 | STS3250 × 3 | Host 使用 `alohamini2pro` |
| 从臂 | `am-follower-6dof-hd` | 由 Pro 整机 profile 选择 |
| 升降舵机 | STS3095 | 不应套用一代 STS3215 升降配置 |
| 升降传动参数 | 131 mm/rev | 软件换算参数，不是行程或速度 |
| PC 主臂 | `am-leader-6dof` | 与标准 2 相同；不要填入从臂 HD profile |
| state/action 接口 | 18 维 | 仍需核对特征名、顺序与单位 |

产品说明中的“STS3250 舵机方案”不能理解为所有关节都使用 STS3250。不同部位应分别核对，升降使用的仍是 STS3095。

## 当前硬件资料覆盖到哪里

截至 **2026-09-28**，核对的硬件仓库 `AlohaMini2/docs` 提供 `BOM.md`、`print_guide.md` 和 `assembly_guide.md`，本次未找到独立的 Pro BOM、金属底盘装配图或 Pro 专属打印清单。

| 资料 | 本站处理方式 |
|---|---|
| 标准 2 物料与采购数量 | 放在 [标准 2 物料清单](bom.md)，不作为 Pro 的采购清单 |
| 标准 2 打印文件与切片建议 | 放在 [标准 2 打印指南](printing.md) |
| 标准 2 图文装配步骤 | 放在 [标准 2 硬件组装](assembly.md) |
| Pro 软件配置与完整工作流 | 已按官方 Profiles 整理为 [Pro 入门教程](alohamini2pro.md) |
| Pro 独立装配资料 | 待上游提供后补充到本页 |

因此，本页不提供未经资料确认的 Pro 紧固件数量、金属件尺寸、打印替换方案或负载数值。准备自行装配 Pro 时，先取得与你套件匹配的装配与接线说明。

## 已有 Pro 整机：接入软件前检查

1. **核对整机和执行器**：记录机器型号，检查轮舵机与升降舵机标签，确认从臂属于对应 HD 配置。
2. **核对控制板与左右端口**：按 [设备配置](configuration.md) 识别左右从臂总线与左右主臂，不依赖 USB 插入顺序。
3. **核对供电与接线**：按实际套件说明确认各设备供电、接口与线缆固定；软件 profile 不会代替硬件接线检查。
4. **核对相机**：逐一确认名称与画面，默认软件启用前向和右腕两路。实际启用范围以配置为准。
5. **准备校准**：在 Pi 使用 `alohamini2pro`，PC 主臂使用 `am-leader-6dof`；不要套用另一台机器的校准文件。
6. **分模块验证**：先检查机械臂，再检查底盘与升降，最后进入完整遥操作和采集。

[继续：AlohaMini 2 Pro 入门教程 →](alohamini2pro.md)

## 资料来源

- [硬件仓库产品系列说明](https://github.com/liyiteng/AlohaMini/blob/17c6a98d79881a45ab869c1f392ed89c0723a298/README.md#product-line)
- [本次核对的硬件教程目录](https://github.com/liyiteng/AlohaMini/tree/17c6a98d79881a45ab869c1f392ed89c0723a298/AlohaMini2/docs)
- [软件硬件 Profiles](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/alohamini/profiles.md)
