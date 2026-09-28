# AM-ARM200 single arm tutorial

If there is no robot chassis, you can first use **a PC, a leader arm and a follower arm** to complete calibration, teleoperation and acquisition. This path does not require a Raspberry Pi Host and is suitable for verifying the robotic arm alone.

## 1. Prepare environment and ports

First complete the [Software installation](software.md), and connect the leader arm and follower arm to the PC respectively. Access and record serial ports one by one:

```bash
lerobot-find-port
lerobot-find-cameras
```

The example on this page assumes that the leader arm is `/dev/ttyACM0`, the follower arm is `/dev/ttyACM1`, and the camera indexes are 0 and 1. Change them to their actual values before running.

## 2. Calibrate the leader arm

```bash
lerobot-calibrate \
  --teleop.type=so101_leader \
  --teleop.port=/dev/ttyACM0 \
  --teleop.id=my_leader \
  --teleop.arm_profile=am-leader-6dof
```

Although the entry type name contains `so101`, here the hardware profile of the AM leader arm is selected by `am-leader-6dof`. Follow the prompts to complete the range recording.

## 3. Calibrate the follower arm

```bash
lerobot-calibrate \
  --robot.type=so101_follower \
  --robot.port=/dev/ttyACM1 \
  --robot.id=my_follower \
  --robot.arm_profile=am-follower-6dof
```

The Pro follower arm uses `am-follower-6dof-hd`. After completion, follow the original tutorial to power off the two arms and restart them.

## 4. teleoperation

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

Move the leader arm slowly and check the follower arm following, joint direction and grippers. After confirming that it is normal, exit the teleoperation and start recording again.

## 5. Record a demo

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

Remove `cam_top` entry when there is only one camera. `cam_wrist` and `cam_top` will become the data set field names, and they will remain consistent in subsequent recording, training and deployment.

The single-arm entrance continuation uses `--resume=true` and points to the same data set; its parameter form is different from that of the whole machine `record_bi.py`, and the current entrance help shall prevail.

## 6. View and playback

View offline:

```bash
lerobot-dataset-viz \
  --repo-id $HF_USER/am_arm_test \
  --episode-index 0 \
  --display-compressed-images
```

Real machine playback will move the follower arm:

```bash
lerobot-replay \
  --robot.type=so101_follower \
  --robot.port=/dev/ttyACM1 \
  --robot.id=my_follower \
  --robot.arm_profile=am-follower-6dof \
  --dataset.repo_id=$HF_USER/am_arm_test \
  --dataset.episode=0
```

## 7. Training and migration to the whole machine

Training can be done as [ACT training](training.md) by replacing the dataset with a single-arm dataset and using a separate output directory. The action and observation structure of the single-arm policy is different from that of the whole machine. The single-arm model cannot be directly handed over to the two-arm whole machine evaluation script.

When expanding from a single arm to a robot, the left and right leader and follower arms, Host, chassis, lifting and camera configurations of the whole machine are re-completed, and then the whole machine data corresponding to the training is re-collected.

## 8. Single Arm ACT Training Example

Keep the collected data in the same namespace; the following command turns off model upload:

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

Add the correct `--dataset.root` when customizing the data directory. When the training machine is separated from the control machine, the data and checkpoints are completely migrated. It is recommended to use an independent `am_arm_pro_test` data set and model directory for single-arm Pro data.

## 9. Single-arm hardware evaluation

The evaluation uses `lerobot-rollout` to directly control a single follower arm on a PC. Stop teleoperation and recording first, and check that the camera and model inputs are consistent; the `020000` below is changed to the actual number of saved steps.

**AM-ARM200 standard follower arm**

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

**AM-ARM200 Pro follower arm**

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

The camera configuration here corresponds to the recording example on this page; if only one camera is used for training, the evaluation is also configured with the same name. The device ID must be loaded with the true calibration of the follower arm, and the Pro checkpoint must be trained from the corresponding data.

For complete parameters and evaluation behavior, see [Inference configuration](upstream/software--docs-source-inference.md); for single-arm workflow, recording resumption commands and reference instructions, see [Single arm operation tutorial](upstream/software--docs-alohamini-am-arm200.md).
