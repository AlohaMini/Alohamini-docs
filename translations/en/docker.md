# Docker environment

Docker tutorials are suitable for preparing a training or development environment in a standalone container. The robot still needs to correctly configure the serial port, camera and network; starting the container does not mean that these hardware are accessible.

## 1. Select image source

The project provides two Dockerfiles:

| File | Basic environment | Purpose |
| --- | --- | --- |
| `docker/Dockerfile.user` | Python 3.12 slim | CPU development and tool usage |
| `docker/Dockerfile.internal` | NVIDIA CUDA / Ubuntu | GPU training and CI |

The `huggingface/lerobot-cpu` and `huggingface/lerobot-gpu` listed in the README are Hugging Face images, and it cannot be assumed that they contain custom modifications of `liyiteng/lerobot_alohamini`. AlohaMini exclusive scripts are recommended to be built from the current software source code.

## 2. Build from software repository

The following command is executed in the `lerobot_alohamini` root directory:

```bash
# CPU 镜像
docker build -f docker/Dockerfile.user -t alohamini-cpu .

# GPU 镜像
docker build -f docker/Dockerfile.internal -t alohamini-gpu .
```

The build will download the base image and dependencies. GPU operation requires that the host has compatible NVIDIA drivers and container GPU support. The current Dockerfile will install project extras and will not automatically prepare all external environments in the simulation tutorial.

## 3. Start the training container and retain the data

First prepare the data and output directory on the host machine, for example:

```bash
mkdir -p "$PWD/container-data" "$PWD/container-output"
docker run -it --rm --gpus all --shm-size 16gb \
  -v "$PWD/container-data:/workspace/data" \
  -v "$PWD/container-output:/workspace/output" \
  alohamini-gpu
```

Put the complete data set into host machine `container-data`. Use the actual subdirectory of `/workspace/data` as `dataset.root` in the container and point `output_dir` to `/workspace/output`. The sample mount directory must be writable by users within the container; do not treat checkpoints that are only saved in the temporary container layer as persistent backups.

The container uses [ACT training](training.md). Check the GPU first:

```bash
nvidia-smi
python -c "import torch; print(torch.cuda.is_available())"
```

## 4. CPU and designated GPU

```bash
docker run -it --rm alohamini-cpu
```

Specify the visible GPU via `CUDA_VISIBLE_DEVICES`:

```bash
docker run -it --rm --gpus all --shm-size 16gb \
  -e CUDA_VISIBLE_DEVICES=0,1 \
  alohamini-gpu
```

The fact that two GPUs are visible to the container does not mean that multiple cards are automatically used for training; see [Multi-GPU training](upstream/software--docs-source-multi_gpu_training.md) for startup methods and distributed training parameters.

## 5. Serial port, camera and network

Before mapping devices, first record the devices actually required by the container, and confirm user permissions, udev aliases can be resolved within the container, and the IP and port of the Pi can be accessed by the container.

Robot USB is not required when training saved data with containers. When you really want to connect to a real machine, first complete the device discovery and calibration check on the host, and then verify the serial port, video device and network in the container one by one to avoid troubleshooting environmental and hardware problems at the same time.

## 6. FAQ

| question | Check items |
| --- | --- |
| `--gpus` Invalid | Host driver, Docker GPU support, whether to use GPU image |
| AlohaMini module not found | Whether the image is built from this custom repository |
| Data set does not exist | Are the host directory and container mounting path consistent? |
| The output directory has no permissions | Mount directory owner and container user write permissions |
| File disappears after container exits | Whether the file is written to the persistent mount directory |
| The camera or serial port cannot be opened | Device mapping, permissions, aliases and occupied processes |
