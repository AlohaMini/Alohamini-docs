# 手机视频重建 Isaac Sim 场景

`video2sim` 将手机拍摄的室内视频转换成可渲染的高斯场景与具有实际尺度的碰撞体，再组装为 Isaac Sim 场景。本页依据 README 与当前 `cli.py`，补充本地路径、运行终点和模型文件的差异。

## 1. 运行前准备

原文记录的测试环境为 NVIDIA RTX 4060 8 GB、约 32 GB 内存和 Isaac Sim 5.x。这是上游特定场景的记录，不保证任意分辨率、视频时长都能在同样资源下完成。

| 环境 | 所需组件 |
|---|---|
| 主环境 | CUDA Torch、gsplat、pycolmap、open3d、scipy、PIL、ninja、PyYAML |
| NuRec 导出环境 | pxr、Torch、msgpack、ncore 与 3dgrut 导出依赖 |
| Isaac 环境 | Isaac Sim 5.x、pxr 与 NuRec schema |
| 外部工具与模型 | ffmpeg、ffprobe、匹配的 LingBot-Map fork 与权重 |

重建环境与整机控制的 uv 环境分开。先准备各组件，再进行下面的检查；本教程不会自动创建这些复杂环境。

## 2. 设置本机路径

原文中的 `/home/perelman/...` 是作者机器路径，直接复制无法在其他机器上使用。进入软件仓库里的模块目录：

```bash
cd /path/to/lerobot_alohamini/alohamini_sim/video2sim
```

创建自己的 `local.yaml`，替换所有示例绝对路径：

```yaml
main_python: /path/to/main-env/bin/python
nurec_python: /path/to/nurec-env/bin/python
isaac_python: /path/to/isaac-env/bin/python
lingbot_repo: /path/to/LingBot-Map
lingbot_model: /path/to/lingbot-map-long.pt
stage_args:
  train:
    iters: 10000
```

`cli.py` 用 `stage_args` 传递阶段参数。仓库 `configs/default.yaml` 中按 `extract`、`train` 等顶层分组写的值还包含配方记录，不能假设任意顶层字段都会成为命令行参数。参数中的下划线与连字符需与各阶段入口一致。

## 3. 检查环境

```bash
python3 -m video2sim.check_env \
  --main-python /path/to/main-env/bin/python \
  --nurec-python /path/to/nurec-env/bin/python \
  --isaac-python /path/to/isaac-env/bin/python \
  --lingbot-repo /path/to/LingBot-Map \
  --model /path/to/lingbot-map-long.pt
```

检查器在各自解释器中验证依赖，显示 PASS、WARN、FAIL。先处理失败项。8 GB 显存环境下，原文要求推理和训练时释放 GPU，避免同时开着 Isaac GUI 占用显存。

## 4. 执行重建

```bash
/path/to/main-env/bin/python -m video2sim run /path/to/room.mp4 \
  --config local.yaml \
  --workdir runs/room1
```

**默认结束于 `scene_prep`**，会准备场景外观、对齐参数和碰撞数据；不会默认运行最后的 `scene` 阶段。

| 阶段 | 主要产物 | 检查重点 |
|---|---|---|
| extract | `frames/f_*.jpg` | 图像方向与清晰度 |
| lingbot_infer | `lingbot/pred-*.pt` | 位姿与深度是否完整 |
| fuse | `fuse/mvtsdf.ply` 与 mesh | 表面、噪点和内存 |
| refine | `final_mesh.ply`、`final_cloud.ply`、`final_align.npz` | 地面方向、尺度和坐标变换 |
| to_colmap | `sparse/0/` | 相机与稠密初始化数据 |
| train | `splat.pt` | 外观、漂浮点、训练日志 |
| export | `export/scene.usdz` | NuRec 导出是否成功 |
| scene_prep | `collider.npz` | 碰撞网格 |
| scene（显式启用） | `scene/scene.usd` | 外观与碰撞体是否对齐 |

当前流程使用 LingBot 位姿与深度，不把 COLMAP SfM 求解作为主线；`to_colmap` 是生成后续训练需要的格式。

## 5. 组装与查看 Isaac 场景

当前 `scene.py` 默认读取仓库内的 `alohamini2pro_parallel.usd`，可使用随仓提供的 USD 资产。README 提及的同名 URDF 在本次提交中未找到，但这不阻断默认 USD 场景入口；需要导入 URDF 或运行 ManiSkill 时，另行补齐对应模型。

环境与资产齐全后，显式执行最终阶段：

```bash
/path/to/main-env/bin/python -m video2sim run \
  --config local.yaml \
  --workdir runs/room1 \
  --until scene
```

需要 GUI 时：

```bash
/path/to/main-env/bin/python -m video2sim run \
  --config local.yaml \
  --workdir runs/room1 \
  --gui
```

已存在阶段输出时 runner 会跳过对应阶段。改变模型、视频或关键参数后使用新的工作目录，避免误把旧结果当作新结果。

## 6. 配方参数与排错

完整参数表、参数原因、v10/v11 比较和故障处理已保留在 [video2sim 配置参考](upstream/software--alohamini_sim-video2sim-readme.md)。其中地面到天花板 2.4 m、手持高度 1.35 m 等尺度假设必须符合实际拍摄环境。

| 现象 | 优先检查 |
|---|---|
| 显存不足 | 其他 GPU 进程、Isaac GUI、输入分辨率、LingBot 窗口与高斯数量 |
| 地面方向错误 | floor 检测、相机轨迹筛选、`final_align.npz` |
| 场景雾化或漂浮点过多 | 相机位姿、尺度、训练参数和初始化点云 |
| 碰撞与画面对不上 | 导出和场景组装是否使用同一对齐变换 |
| NuRec 导出导入失败 | 是否使用指定的 NuRec / Isaac 解释器与 schema |
| 看不到 `scene.usd` | 是否显式运行 `--until scene`，资产是否齐全 |

完成场景检查后再进入 [仿真数据生成与转换](sim-data.md)。场景可显示、轨迹可生成、数据可训练是三个独立检查点。

来源：[完整配置参考](upstream/software--alohamini_sim-video2sim-readme.md)、[runner 源码](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/alohamini_sim/video2sim/video2sim/cli.py)。
