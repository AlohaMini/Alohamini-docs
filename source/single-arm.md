# AM-ARM200 单臂教程

如果还没有整机底盘，可以先用 **一台 PC、一只主臂和一只从臂**完成校准、遥操作和采集。这条路径不需要树莓派 Host，适合单独验证机械臂。

## 1. 准备环境与端口

先完成 [软件安装](software.md)，将主臂和从臂分别接到 PC。逐只接入并记录串口：

```bash
lerobot-find-port
lerobot-find-cameras
```

本页示例约定主臂 `/dev/ttyACM0`、从臂 `/dev/ttyACM1`，相机索引为 0 和 1，运行前换成自己的实际值。

## 2. 校准主臂

```bash
lerobot-calibrate \
  --teleop.type=so101_leader \
  --teleop.port=/dev/ttyACM0 \
  --teleop.id=my_leader \
  --teleop.arm_profile=am-leader-6dof
```

虽然入口类型名包含 `so101`，这里通过 `am-leader-6dof` 选择 AM 主臂的硬件 profile。按提示完成范围记录。

## 3. 校准从臂

```bash
lerobot-calibrate \
  --robot.type=so101_follower \
  --robot.port=/dev/ttyACM1 \
  --robot.id=my_follower \
  --robot.arm_profile=am-follower-6dof
```

Pro 从臂使用 `am-follower-6dof-hd`。完成后按原始教程对两只臂断电重启。

## 4. 遥操作

```bash
lerobot-teleoperate \
  --teleop.type=so101_leader \
  --teleop.port=/dev/ttyACM0 \
  --teleop.id=my_leader \
  --teleop.arm_profile=am-leader-6dof \
  --robot.type=so101_follower \
  --robot.port=/dev/ttyACM1 \
  --robot.id=my_follower \
  --robot.arm_profile=am-follower-6dof
```

缓慢移动主臂，检查从臂跟随、关节方向与夹爪。确认正常后退出遥操作，再启动录制。

## 5. 录制一条演示

```bash
export HF_USER="your-hf-username"
lerobot-record \
  --robot.type=so101_follower \
  --robot.port=/dev/ttyACM1 \
  --robot.id=my_follower \
  --robot.arm_profile=am-follower-6dof \
  --robot.cameras="{cam_wrist: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}, cam_top: {type: opencv, index_or_path: 1, width: 640, height: 480, fps: 30}}" \
  --teleop.type=so101_leader \
  --teleop.port=/dev/ttyACM0 \
  --teleop.id=my_leader \
  --teleop.arm_profile=am-leader-6dof \
  --dataset.repo_id=$HF_USER/am_arm_test \
  --dataset.num_episodes=1 \
  --dataset.fps=30 \
  --dataset.episode_time_s=45 \
  --dataset.reset_time_s=8 \
  --dataset.single_task="Pick up the object and place it in the tray" \
  --dataset.push_to_hub=false \
  --display_data=true
```

只有一只相机时删除 `cam_top` 条目。`cam_wrist` 与 `cam_top` 会成为数据集字段名，后续续录、训练和部署保持一致。

单臂入口续录使用 `--resume=true`，并指向相同数据集；它与整机 `record_bi.py` 的参数形式不同，以当前入口帮助为准。

## 6. 查看和回放

离线查看：

```bash
lerobot-dataset-viz \
  --repo-id $HF_USER/am_arm_test \
  --episode-index 0 \
  --display-compressed-images
```

真机回放会移动从臂：

```bash
lerobot-replay \
  --robot.type=so101_follower \
  --robot.port=/dev/ttyACM1 \
  --robot.id=my_follower \
  --robot.arm_profile=am-follower-6dof \
  --dataset.repo_id=$HF_USER/am_arm_test \
  --dataset.episode=0
```

## 7. 训练与迁移到整机

训练可按 [ACT 训练](training.md) 将数据集替换为单臂数据集，并使用独立输出目录。单臂策略的动作和观测结构与整机不同，不能直接把单臂模型交给双臂整机评估脚本。

从单臂扩展到整机时，重新完成左右主从臂、Host、底盘、升降和整机相机配置，再重新采集与训练对应的整机数据。

## 8. 单臂 ACT 训练示例

将采集数据保持在同一命名空间；以下命令关闭模型上传：

```bash
lerobot-train \
  --dataset.repo_id=$HF_USER/am_arm_test \
  --policy.type=act \
  --output_dir=outputs/train/act_am_arm_test \
  --job_name=act_am_arm_test \
  --policy.device=cuda \
  --policy.push_to_hub=false \
  --wandb.enable=false \
  --dataset.video_backend=pyav
```

自定义数据目录时加上正确的 `--dataset.root`。训练机与控制机分开时，完整迁移数据和检查点。单臂 Pro 数据建议使用独立的 `am_arm_pro_test` 数据集与模型目录。

## 9. 单臂真机评估

评估使用 `lerobot-rollout`，在 PC 上直接控制单从臂。先停止遥操作与录制，核对相机与模型输入一致；下面的 `020000` 改为实际保存的步数。

**AM-ARM200 标准从臂**

```bash
lerobot-rollout \
  --strategy.type=base \
  --robot.type=so101_follower \
  --robot.port=/dev/ttyACM1 \
  --robot.id=my_follower \
  --robot.arm_profile=am-follower-6dof \
  --robot.cameras="{cam_wrist: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}, cam_top: {type: opencv, index_or_path: 1, width: 640, height: 480, fps: 30}}" \
  --policy.path=outputs/train/act_am_arm_test/checkpoints/020000/pretrained_model \
  --task="Pick up the object and place it in the tray"
```

**AM-ARM200 Pro 从臂**

```bash
lerobot-rollout \
  --strategy.type=base \
  --robot.type=so101_follower \
  --robot.port=/dev/ttyACM1 \
  --robot.id=my_follower \
  --robot.arm_profile=am-follower-6dof-hd \
  --robot.cameras="{cam_wrist: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}, cam_top: {type: opencv, index_or_path: 1, width: 640, height: 480, fps: 30}}" \
  --policy.path=outputs/train/act_am_arm_pro_test/checkpoints/020000/pretrained_model \
  --task="Pick up the object and place it in the tray"
```

这里的相机配置与本页录制示例对应；如果训练只用一只相机，评估也按相同名称配置。设备 ID 必须加载该从臂的真实校准，Pro 检查点必须由对应数据训练得到。

完整参数与评估行为见 [推理配置](upstream/software--docs-source-inference.md)；单臂工作流、续录命令和参考说明见 [单臂操作教程](upstream/software--docs-alohamini-am-arm200.md)。
