# Docker 环境

Docker 教程适合在独立容器中准备训练或开发环境。机器人端依然需要正确配置串口、相机和网络；启动容器不等于这些硬件已经可访问。

## 1. 选择镜像来源

项目提供两种 Dockerfile：

| 文件 | 基础环境 | 用途 |
|---|---|---|
| `docker/Dockerfile.user` | Python 3.12 slim | CPU 开发与工具使用 |
| `docker/Dockerfile.internal` | NVIDIA CUDA / Ubuntu | GPU 训练与 CI |

README 列出的 `huggingface/lerobot-cpu` 和 `huggingface/lerobot-gpu` 是 Hugging Face 镜像，不能假设其中包含 `liyiteng/lerobot_alohamini` 的定制修改。AlohaMini 专属脚本建议从当前软件源码构建。

## 2. 从软件仓库构建

以下命令在 `lerobot_alohamini` 根目录执行：

```bash
# CPU 镜像
docker build -f docker/Dockerfile.user -t alohamini-cpu .

# GPU 镜像
docker build -f docker/Dockerfile.internal -t alohamini-gpu .
```

构建会下载基础镜像和依赖。GPU 运行要求宿主机已有兼容 NVIDIA 驱动和容器 GPU 支持。当前 Dockerfile 会安装项目 extras，不会自动准备仿真教程中的所有外部环境。

## 3. 启动训练容器并保留数据

先在宿主机准备数据和输出目录，例如：

```bash
mkdir -p "$PWD/container-data" "$PWD/container-output"
docker run -it --rm --gpus all --shm-size 16gb \
  -v "$PWD/container-data:/workspace/data" \
  -v "$PWD/container-output:/workspace/output" \
  alohamini-gpu
```

把完整数据集放进宿主机 `container-data`。在容器里用 `/workspace/data` 的实际子目录作为 `dataset.root`，将 `output_dir` 指向 `/workspace/output`。示例挂载目录必须对容器内用户可写；不要把只保存在临时容器层里的检查点当作持久备份。

容器内沿用 [ACT 训练](training.md) 的对应机型数据集参数。先检查 GPU：

```bash
nvidia-smi
python -c "import torch; print(torch.cuda.is_available())"
```

## 4. CPU 与指定 GPU

```bash
docker run -it --rm alohamini-cpu
```

通过 `CUDA_VISIBLE_DEVICES` 指定可见 GPU：

```bash
docker run -it --rm --gpus all --shm-size 16gb \
  -e CUDA_VISIBLE_DEVICES=0,1 \
  alohamini-gpu
```

两块 GPU 对容器可见，不代表训练自动采用多卡；启动方式与分布式训练参数见 [多 GPU 训练](upstream/software--docs-source-multi_gpu_training.md)。

## 5. 串口、相机和网络

映射设备前，先记录容器实际需要的设备，并确认用户权限、udev 别名在容器内可解析，以及容器可以访问 Pi 的 IP 和端口。

用容器训练已保存的数据时不需要机器人 USB。确实要接入真机时，先在宿主机完成设备发现和校准检查，再逐一验证容器内串口、视频设备和网络，避免同时排查环境与硬件两类问题。

## 6. 常见问题

| 问题 | 检查项 |
|---|---|
| `--gpus` 无效 | 宿主驱动、Docker GPU 支持、是否使用 GPU 镜像 |
| 找不到 AlohaMini 模块 | 镜像是否由该定制仓库构建 |
| 数据集不存在 | 宿主机目录与容器挂载路径是否一致 |
| 输出目录无权限 | 挂载目录属主与容器用户写权限 |
| 容器退出后文件消失 | 文件是否写进了持久挂载目录 |
| 相机或串口打不开 | 设备映射、权限、别名和占用进程 |
