# 舵机与性能调试

本页补齐上游 `examples/debug/README.md` 和命令参考中的调试入口。端口、ID、相位和位置值需要按实际硬件填写。先结束占用相同总线的 Host 或客户端，再连接调试程序。

## 1. 读取状态与确认 ID

```bash
python examples/debug/motors.py get_motors_states \
  --port /dev/ttyACM0
```

确认读到的舵机型号、ID 与接线一致。只有一只待编号舵机接入时，修改其 ID：

```bash
python examples/debug/motors.py configure_motor_id \
  --id 1 --set_id 8 --port /dev/ttyACM0
```

`1` 和 `8` 是原文示例。底盘编号按对应机型装配图，机械臂编号按其关节定义；修改后重新读取验证。

## 2. 移动指定舵机

```bash
python examples/debug/motors.py move_motor_to_position \
  --id <motor_id> \
  --position <target_tick> \
  --port /dev/ttyACM0
```

`position` 是原始 tick，不是角度或毫米。原文中的 `2` 仅是演示值，不能作为所有关节的测试目标。确认当前值、零位、机械范围和周边空间后才执行小范围运动。

## 3. 修改相位

指定一只舵机：

```bash
python examples/debug/motors.py configure_motor_phase \
  --id <motor_id> \
  --set_phase <phase_value> \
  --port /dev/ttyACM0
```

省略 `--id` 的原文形式会作用于脚本找到的多个舵机：

```bash
python examples/debug/motors.py configure_motor_phase \
  --set_phase <phase_value> \
  --port /dev/ttyACM0
```

批量操作前确认连接对象。不要把 `12` 等原文示例当作通用正确值；保留旧配置，确认改动后是否需要重新校准。

## 4. 中位、扭矩与动作脚本

设置当前位置为中位相关配置：

```bash
python examples/debug/motors.py reset_motors_to_midpoint \
  --port /dev/ttyACM0
```

关闭扭矩前承托会因重力下落的部件：

```bash
python examples/debug/motors.py reset_motors_torque \
  --port /dev/ttyACM0
```

确认脚本内每个目标位置与实物匹配后执行：

```bash
python examples/debug/motors.py move_motors_by_script \
  --script_path /path/to/checked_action_script.txt \
  --port /dev/ttyACM0
```

这些操作改变硬件状态，不替代 [校准流程](calibration.md)。完整参数帮助：

```bash
python examples/debug/motors.py --help
```

## 5. 底盘与升降独立入口

原文还提供：

```bash
python examples/debug/wheels.py --port /dev/ttyACM0
python examples/debug/axis.py --port /dev/ttyACM0
```

当前脚本内部保留 `sts3215` 型号常量及独立轮位、几何参数，不会自动读取二代或 Pro 的整机 profile。**二代 / Pro 首次调试优先使用 [仅底盘与升降遥操作](teleoperation.md)**；不要以为更换串口就完成了型号适配。

## 6. 网络与 Wi-Fi

```bash
ping <Pi_IP>
iw dev
iw dev wlan0 link
```

`wlan0` 应替换成 `iw dev` 列出的接口。观察丢包、延迟波动与链路信息；单次低延迟不代表连续视频传输稳定。

已有 iperf3 时，在 Pi 运行服务：

```bash
iperf3 -s
```

在 PC 连接：

```bash
iperf3 -c <Pi_IP>
```

带宽测试会占用链路，在独立调试阶段进行；结果主要用于判断当前网络条件。

## 7. CPU、GPU 与视频编码

```bash
top
htop
nvidia-smi
ffmpeg -hide_banner -encoders
python -c "import av, cv2, torch; print('av', av.__version__); print('cv2', cv2.__version__); print('torch', torch.__version__)"
```

`htop` 可能需要额外安装，`nvidia-smi` 只用于具备 NVIDIA 驱动的设备。编码器列在列表中还不等于当前硬件和依赖能顺利执行，需结合真实录制日志确认。

## 8. 降低负载后对比

按 [遥操作低负载示例](teleoperation.md) 与 [短数据测试](learning.md) 使用本机型号，临时降低 FPS 或启用相机数量。每次只改一项，记录网络、CPU、相机缺帧与录制结果。问题消失后逐项恢复配置，避免把低负载排错设置误作正式训练数据规范。

来源：[完整调试原文](upstream/software--examples-debug-readme.md)、[性能调试与命令原文](upstream/software--docs-alohamini-commands.md)。
