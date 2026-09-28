# 官方使用手册

从收到机器人开始，完成供电、软件连接、遥操作，再进入数据采集与策略训练。按下面的路线选择适合当前进度的教程。

## 第一次使用，从这里开始

```{raw} html
<div class="am-paths">
<a class="am-path" href="unboxing.html"><span class="am-model-label">01 · 收到整机</span><strong>开箱与首次通电 ↗</strong><p>核对电池与供电接口，连接树莓派、主臂和网络。</p></a>
<a class="am-path" href="quickstart.html"><span class="am-model-label">02 · 选择型号</span><strong>进入 2 / 2 Pro 教程 ↗</strong><p>根据实物型号完成环境、设备配置、校准和遥操作。</p></a>
<a class="am-path" href="learning.html"><span class="am-model-label">03 · 完成一个任务</span><strong>采集、训练与评估 ↗</strong><p>先检查一条演示，再训练模型并进行短时真机测试。</p></a>
<a class="am-path" href="support.html"><span class="am-model-label">04 · 遇到问题</span><strong>整机排错 ↗</strong><p>按供电、串口、校准、相机与网络逐项排查。</p></a>
</div>
```

## 按你的进度阅读

| 当前情况 | 阅读顺序 |
|---|---|
| 刚收到已组装好的 2 / 2 Pro | [开箱图解](unboxing.md) → [选择型号](quickstart.md) → [设备配置](configuration.md) |
| 没有接触过 LeRobot | [开发者手册](yuque/developer-manual.md) → [软件安装](software.md) → [校准](calibration.md) |
| 已有 LeRobot 经验，使用 2 Pro | [Pro 交付快速入门](yuque/pro-quickstart.md) → [2 Pro 完整流程](alohamini2pro.md) |
| 自行搭建标准 2 | [物料清单](bom.md) → [打印](printing.md) → [组装](assembly.md) → [2 入门](alohamini2.md) |
| 可以遥操作，准备训练 | [数据采集与回看](learning.md) → [ACT / AM-ACT 训练](training.md) → [真机评估](evaluation.md) |
| 需要调试或扩展 | [整机排错](support.md) → [调试工具](debug-tools.md) → [进阶参考](yuque/advanced.md) |

## 完整交付教程

教程中的用户名、设备序列号、IP、数据目录和检查点路径均为示例，操作前请替换为本机值。

| 教程 | 内容与适用范围 |
|---|---|
| [2 / 2 Pro 开箱指南](yuque/unboxing.md) | 已组装整机的电池、供电板与遥操臂接线图 |
| [2 Pro 快速入门](yuque/pro-quickstart.md) | 从 SSH、端口绑定到采集、ACT / AM-ACT 和本地推理 |
| [开发者手册 v1.3](yuque/developer-manual.md) | 面向新手的结构、环境、单臂、底盘、升降及相机说明 |
| [常见问题](yuque/faq.md) | 更新代码与网络访问 |
| [异常处理](yuque/troubleshooting.md) | E001–E004 的报错、原因和处理步骤 |
| [进阶参考](yuque/advanced.md) | 串口确认与校准文件位置 |
| [选购配件](yuque/accessories.md) | 配件规格和购买入口 |
| [资料包](yuque/resources.md) | Policy PDF、一代仿真与二代 SLAM 扩展入口 |

## 产品、教育与视频

- [中文产品说明](yuque/product.md) · [English product overview](yuque/product-en.md)
- [具身智能教育解决方案](yuque/education.md) · [K12 产品说明](yuque/education-k12.md)
- [演示视频合集](yuque/videos.md)

操作前请确认设备型号、套件配置和已安装的软件版本。课程与赛事安排以对应活动的最新通知为准。

## 版本差异怎么处理

1. **整机型号一致**：2 使用 `alohamini2`，2 Pro 使用 `alohamini2pro`；树莓派 Host 与 PC 必须匹配。
2. **机械臂编号分代际**：SO-ARM 为 1–6；AM-ARM 为 1–7。整机底盘为 8–10，升降为 11。
3. **相机名称一致**：部分交付示例使用 `head_top`，其他软件配置使用 `forward`。采集、转换、训练与推理都应按实际数据特征配置，不能只改显示名称。
4. **按机型调试底盘**：旧版 `wheels.py` / `axis.py` 的默认舵机配置不适合直接套在 2 Pro 上，见 [调试工具](debug-tools.md)。
5. **先保存改动再更新**：更新软件前保存本机配置，使用 [更新步骤](support.md#更新软件与网络访问)。

[浏览更多专题教程](tutorial-library.md)

```{toctree}
:hidden:
:maxdepth: 1

unboxing
support
yuque/unboxing
yuque/pro-quickstart
yuque/developer-manual
yuque/faq
yuque/troubleshooting
yuque/advanced
yuque/resources
yuque/accessories
yuque/product
yuque/product-en
yuque/education
yuque/education-k12
yuque/videos
```
