# 仿真与模型可视化

另有软件仓库的 [video2sim 场景重建](video2sim.md) 与 [仿真数据生成/转换](sim-data.md)。完整 [一代仿真原文](upstream/hardware--alohamini1-simulation-readme.md) 也已迁入本站。

硬件仓库的现有模型资源位于 **AlohaMini1/simulation**，对应一代机器人。本页以当前包实际采用的 **ROS 2 / ament_cmake / colcon** 构建方式为主。

```{image} _static/media/simulation.png
:alt: AlohaMini 一代机器人在模型可视化环境中的展示
:width: 100%
```

## 资源包含什么

| 路径（相对仿真工作空间） | 内容 |
|---|---|
| `src/Aloha/urdf/Aloha.urdf` | 一代机器人模型与关节结构 |
| `src/Aloha/meshes/` | 机器人各部件网格 |
| `src/Aloha/rviz/urdf.rviz` | RViz 可视化配置 |
| `src/Aloha/launch/display.launch.py` | ROS 2 模型显示入口 |
| `src/Aloha/launch/display.launch` | 保留的 ROS 1 显示文件 |
| `src/Aloha/launch/gazebo.launch` | 保留的 Gazebo 启动文件 |

当前显示入口启动 `robot_state_publisher`、`joint_state_publisher` 与 `rviz2`。模型展示不等同于真机控制，也不代表二代动力学与控制器已经适配完成。

## 1. 准备 ROS 2 环境

先在 Linux 上安装适合自己系统的 ROS 2 版本，并加载环境。以下 `<distro>` 需要替换成实际发行版名称：

```bash
source /opt/ros/<distro>/setup.bash
```

原始教程采用 Ubuntu 系的依赖工具：

```bash
sudo apt update
sudo apt install -y python3-colcon-common-extensions python3-rosdep
```

已经初始化过 rosdep 的系统不要重复初始化。未初始化时，按 rosdep 安装流程完成初始化与索引更新。

## 2. 进入正确工作空间

以下目录位于 **AlohaMini 硬件仓库**，与整机控制的 `lerobot_alohamini` 是两个仓库：

```bash
cd /path/to/AlohaMini/AlohaMini1/simulation
rosdep install --from-paths src --ignore-src -r -y
colcon build
source install/setup.bash
```

当前包名保留大写 `Aloha`，启动命令需要与其一致。

## 3. 启动模型可视化

```bash
ros2 launch Aloha display.launch.py
```

预期打开 RViz2，加载一代机器人模型。若只看到空场景，检查模型加载日志、TF、固定坐标系，以及 robot_state_publisher 是否成功启动。

每次新终端都需先加载 ROS 2 环境和该工作空间的 `install/setup.bash`。

## 4. 常见问题

| 现象 | 检查方向 |
|---|---|
| 找不到包 `Aloha` | 是否构建成功、是否 source 工作空间、包名大小写 |
| 找不到 meshes | 资源路径是否完整，安装产物是否包含 meshes 目录 |
| 找不到 ROS 依赖 | 在工作空间重新检查 rosdep 输出与系统发行版 |
| 模型不显示 | 发布节点、TF、RViz 固定坐标系、URDF 加载日志 |
| 与真机形态不同 | 当前 URDF 对应一代，不能直接当作二代模型 |

## ROS 1 与 Gazebo 资源的范围

原始 README 同时介绍 ROS 1 和 ROS 2，但当前 `CMakeLists.txt` 与 `package.xml` 实际采用 ROS 2 的 `ament_cmake`。保留 ROS 1 launch 文件不等于当前目录可以直接使用 `catkin_make` 构建。

若需要 ROS 1／Gazebo，应先核对包构建配置、Gazebo 版本、插件和控制器适配；本教程暂不把未验证的 ROS 1 命令列为直接可运行的主线。

## 二代适配需要核对

二代更换了机械臂与升降结构，适配时至少需要检查：几何尺寸、关节链、关节限位、质量与惯量、碰撞几何、相机位置，以及与真机控制字段的对应关系。完成这些之前，不应使用一代模型推断二代的碰撞范围或运动能力。

来源：[仿真目录](https://github.com/liyiteng/AlohaMini/tree/main/AlohaMini1/simulation)、[ROS 2 显示入口](https://github.com/liyiteng/AlohaMini/blob/main/AlohaMini1/simulation/src/Aloha/launch/display.launch.py)。
