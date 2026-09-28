# 进阶参考

[返回官方使用手册](../official-manual.md)

(yq-kqoe86xa8ghhw9de-IGlfQ)=

## 如何确认端口对应哪个机械臂

(yq-kqoe86xa8ghhw9de-ua4a5e25d)=

> (yq-kqoe86xa8ghhw9de-u259b14bb)=
> 
> 
> 
> ⚠️ `/dev/ttyACM0`、`/dev/ttyACM1` 的编号**不是固定的**，它由内核按照 USB 设备插入的先后顺序分配。同样两根线，今天插的顺序不同，端口号就可能对调。**每次重新接线后，都建议重新确认端口归属**，再执行校准或遥操作命令。

(yq-kqoe86xa8ghhw9de-xhkID)=

### 插拔确认法

(yq-kqoe86xa8ghhw9de-uf7126401)=

这是最直接、最可靠的方式，无需安装额外工具。

(yq-kqoe86xa8ghhw9de-ue44f81d0)=

**第一步：拔掉所有 USB 设备，确认当前无端口**

```bash
ls /dev/ttyACM*
# 预期输出：ls: cannot access '/dev/ttyACM*': No such file or directory
```

(yq-kqoe86xa8ghhw9de-u9ec9f4b1)=

**第二步：只插入 Leader Arm，记录新出现的端口**

```bash
ls /dev/ttyACM*
# 例如输出：/dev/ttyACM0
# → 记录：Leader Arm = /dev/ttyACM0
```

(yq-kqoe86xa8ghhw9de-u060065ff)=

**第三步：保持 Leader Arm 连接，再插入一条新的机械臂，记录新增端口**

```bash
ls /dev/ttyACM*
# 例如输出：/dev/ttyACM0  /dev/ttyACM1
# → 新增的 /dev/ttyACM1 就是新插入的机械臂的
```

(yq-kqoe86xa8ghhw9de-u0b5f9a8f)=

用同样方法可以逐一确认底盘驱动板的端口。

(yq-kqoe86xa8ghhw9de-odx44)=

## 校准文件说明

(yq-kqoe86xa8ghhw9de-hl9Dl)=

### 校准文件保存在哪里？

(yq-kqoe86xa8ghhw9de-uba994c37)=

执行 `lerobot-calibrate` 后，校准数据会以 JSON 格式保存在本地，默认路径为：

```text
~/.cache/huggingface/lerobot/calibration/
```

(yq-kqoe86xa8ghhw9de-ud79e9ef4)=

以「第一次校准与遥操作」章节中的命令为例，两个臂的校准文件分别保存为：

```text
~/.cache/huggingface/lerobot/calibration/teleop/so101_leader/leader_arm_0218.json
~/.cache/huggingface/lerobot/calibration/robots/so101_follower/follower_arm_0218.json
```

(yq-kqoe86xa8ghhw9de-ufcf175a6)=

其中 `leader_arm_0218` 和 `follower_arm_0218` 就是你在 `--teleop.id` / `--robot.id` 中填写的自定义名称。
