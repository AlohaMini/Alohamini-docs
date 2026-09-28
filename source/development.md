# 开发与扩展

本页面向修改 `lerobot_alohamini` 软件的开发者。若只需要使用机器人，从 [机型入门](quickstart.md) 开始。

## 1. 创建开发环境

在软件仓库根目录使用项目锁定依赖：

```bash
uv sync --locked --extra test --extra dev
```

只安装当前工作需要的 extras。涉及数据集、策略、仿真或特定硬件时，按对应教程添加依赖。需要 Git LFS 测试资产时：

```bash
git lfs install
git lfs pull
```

## 2. 找到要修改的模块

| 路径 | 职责 |
|---|---|
| `src/lerobot/scripts/` | 训练、评估、录制等命令入口 |
| `src/lerobot/configs/` | 参数与 dataclass 配置 |
| `src/lerobot/robots/alohamini/` | AlohaMini 配置、Host 与客户端 |
| `src/lerobot/motors/` | 总线、舵机配置与读写 |
| `src/lerobot/cameras/` | 相机接口 |
| `src/lerobot/policies/` | 各种策略及工厂注册 |
| `src/lerobot/processor/` | 输入输出处理流程 |
| `src/lerobot/datasets/` | LeRobot 数据集读写 |
| `examples/alohamini/` | 双臂校准、遥操作、采集、评估 |
| `tests/` | 自动化测试与夹具 |

新增一种硬件时，先定义字段、单位、关节顺序、校准与连接行为，再实现控制；更改观测或动作定义也会影响历史数据与模型。

## 3. 按扩展目标阅读

| 目标 | 完整教程 |
|---|---|
| 新增机器人、相机或遥操作设备 | [硬件集成](upstream/software--docs-source-integrate_hardware.md) |
| 自定义策略 | [接入自己的策略](upstream/software--docs-source-bring_your_own_policies.md) |
| 理解处理器 | [Processor 介绍](upstream/software--docs-source-introduction_processors.md) |
| 实现新处理步骤 | [自定义 Processor](upstream/software--docs-source-implement_your_own_processor.md) |
| 调试数据变换 | [处理流程调试](upstream/software--docs-source-debug_processor_pipeline.md) |
| 扩展评测环境 | [新增 Benchmark](upstream/software--docs-source-adding_benchmarks.md) |
| 兼容旧数据与接口 | [向后兼容](upstream/software--docs-source-backwardcomp.md) |
| 提交贡献 | [贡献说明](upstream/software--contributing.md) |

## 4. 验证改动

先运行与修改模块有关的测试，例如：

```bash
uv run pytest tests/test_alohamini_sim_bridge.py -svv
```

完整测试入口与格式检查：

```bash
uv run pytest tests -svv --maxfail=10
pre-commit run --all-files
```

硬件测试、GPU 测试和集成测试可能需要额外设备、资产或依赖。记录实际执行范围，不能将跳过的测试算作通过的真机验证。

## 5. 调整本站文档

本站与软件仓库分别维护。中文教程在本站 `source/`，原文资料页在 `source/upstream/`；原文文件下载位于 `source/_static/upstream-originals/`。

后续上游更新时，先核对固定版本与差异，再用本站 `tools/import_upstream_docs.py` 重新生成原文资料页；中文主线需要同步人工核对，不能把导入成功当作教程仍然正确。

[查看开发资料全文目录](library-development.md) · [查看来源与迁移清单](migration-status.md)
