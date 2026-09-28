# 项目说明

[← 教程资料库](../tutorial-library.md) · **AlohaMini 原始教程 / 原文全文**

本文是 AlohaMini 项目资料，具体代际以原文路径和硬件配置为准。

来源：[liyiteng/lerobot_alohamini · `examples/debug/README.md`](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/examples/debug/README.md) · 版本 `7843e588` · [下载未经改写的源文档](../_static/upstream-originals/software/examples/debug/README.md.txt)

本页保留原文语言及全部段落、表格和代码；仅调整标题层级、页面组件、代码围栏格式、相对链接和媒体路径。原文中的价格、性能和运行结果属于该版本记录。

---

## View all motor states
```
python examples/debug/motors.py get_motors_states \
  --port /dev/ttyACM0
```
## Control the mobile base only
```
python examples/debug/wheels.py \
   --port /dev/ttyACM0
```

## Control the lift axis only
```
python examples/debug/axis.py \
   --port /dev/ttyACM0
```


## Rotate a specific motor by ID
```
python examples/debug/motors.py move_motor_to_position \
  --id 1 \
  --position 2 \
  --port /dev/ttyACM0
```


## Set a new motor ID
```
python examples/debug/motors.py configure_motor_id \
  --id 1 \
  --set_id 8 \
  --port /dev/ttyACM0
```

## Set the phase of a specified servo
```
python examples/debug/motors.py configure_motor_phase \
  --id 1 \
  --set_phase 12 \
  --port /dev/ttyACM0
```


## Set the phase for all servos
```
python examples/debug/motors.py configure_motor_phase \
  --set_phase 12 \
  --port /dev/ttyACM0
```

## Reset current position as the motor midpoint
```
python examples/debug/motors.py reset_motors_to_midpoint \
  --port /dev/ttyACM1
```

## Disable torque for all arm motors
```
python examples/debug/motors.py reset_motors_torque  \
  --port /dev/ttyACM0
```

## Execute an action script on the robot arm
```
python examples/debug/motors.py move_motors_by_script \
   --script_path action_scripts/test_dance.txt  \
   --port /dev/ttyACM0
```

