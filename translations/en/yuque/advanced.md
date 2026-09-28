# Advanced reference

[Return to official manual](../official-manual.md)

(yq-kqoe86xa8ghhw9de-IGlfQ)=

## How to confirm which robot arm the port corresponds to

(yq-kqoe86xa8ghhw9de-ua4a5e25d)=

> (yq-kqoe86xa8ghhw9de-u259b14bb)=
> 
> 
> 
> The number ⚠️ `/dev/ttyACM0` and `/dev/ttyACM1` **is not fixed**. It is assigned by the kernel according to the order in which USB devices are inserted. If the same two wires are plugged in in a different order today, the port numbers may be reversed. **After each rewiring, it is recommended to reconfirm the port ownership** before executing calibration or teleoperation commands.

(yq-kqoe86xa8ghhw9de-xhkID)=

### Plug and unplug confirmation method

(yq-kqoe86xa8ghhw9de-uf7126401)=

This is the most direct and reliable way and requires no additional tools to be installed.

(yq-kqoe86xa8ghhw9de-ue44f81d0)=

**Step 1: Unplug all USB devices and confirm that there are currently no ports**

```bash
ls /dev/ttyACM*
# 预期输出：ls: cannot access '/dev/ttyACM*': No such file or directory
```

(yq-kqoe86xa8ghhw9de-u9ec9f4b1)=

**Step 2: Insert only the Leader Arm and record the new ports**

```bash
ls /dev/ttyACM*
# 例如输出：/dev/ttyACM0
# → 记录：Leader Arm = /dev/ttyACM0
```

(yq-kqoe86xa8ghhw9de-u060065ff)=

**Step 3: Keep the Leader Arm connected, insert a new robotic arm, and record the new port**

```bash
ls /dev/ttyACM*
# 例如输出：/dev/ttyACM0  /dev/ttyACM1
# → 新增的 /dev/ttyACM1 就是新插入的机械臂的
```

(yq-kqoe86xa8ghhw9de-u0b5f9a8f)=

Use the same method to confirm the ports of the chassis driver board one by one.

(yq-kqoe86xa8ghhw9de-odx44)=

## Calibration file description

(yq-kqoe86xa8ghhw9de-hl9Dl)=

### Where are the calibration files saved?

(yq-kqoe86xa8ghhw9de-uba994c37)=

After executing `lerobot-calibrate`, the calibration data will be saved locally in JSON format. The default path is:

```text
~/.cache/huggingface/lerobot/calibration/
```

(yq-kqoe86xa8ghhw9de-ud79e9ef4)=

Taking the commands in the "First Calibration and teleoperation" chapter as an example, the calibration files of the two arms are saved as:

```text
~/.cache/huggingface/lerobot/calibration/teleop/so101_leader/leader_arm_0218.json
~/.cache/huggingface/lerobot/calibration/robots/so101_follower/follower_arm_0218.json
```

(yq-kqoe86xa8ghhw9de-ufcf175a6)=

Among them, `leader_arm_0218` and `follower_arm_0218` are the custom names you filled in `--teleop.id` / `--robot.id`.
