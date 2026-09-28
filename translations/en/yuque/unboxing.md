# AlohaMini 2 / 2 Pro Unboxing Guide

[Return to official manual](../official-manual.md)

(yq-dhberyv5btq9hhv1-uf5dabc36)=

Thanks for ordering the AlohaMini.

(yq-dhberyv5btq9hhv1-u6a573778)=

AlohaMini is a set of two-arm elevating robots used for algorithm teaching and reproduction. When packaging and shipping, try not to remove the wires. In terms of hardware, you only need to connect the battery and turn it on.

(yq-dhberyv5btq9hhv1-u853e957d)=

(yq-dhberyv5btq9hhv1-1df7dbbd)=

## Hardware installation

(yq-dhberyv5btq9hhv1-ce199d35)=

### Robot side:

(yq-dhberyv5btq9hhv1-u8c3b000d)=

1. Find the charger and battery in the box, two 12V lithium batteries and their charger, two 5V lithium batteries and their charger. When charging the 12V lithium battery, the charger will have a constant red light, and the green light will stay on after it is fully charged. After 5V is fully charged, 4 white lights will light up on the battery.

(yq-dhberyv5btq9hhv1-u60a22799)=

(yq-dhberyv5btq9hhv1-u07705a22)=

```{raw} html
<div class="yq-rotated-image" style="aspect-ratio:1707/1280"><img src="../_static/yuque-assets/7db0816e0f3650cca772.jpeg" alt="AlohaMini 2 / 2 Pro Unboxing Guide · Figure 1" style="width:74.9854%;transform:translate(-50%,-50%) rotate(270deg)"></div>
```

(yq-dhberyv5btq9hhv1-ua8892051)=

(yq-dhberyv5btq9hhv1-u197eaef3)=

2. Put a 12V battery into the bottom compartment of the robot, connect it to the DC line interface in the picture, and power the Follower Arms and lifting chassis.

(yq-dhberyv5btq9hhv1-u2e9d873e)=

(yq-dhberyv5btq9hhv1-ub634a949)=

![AlohaMini 2 / 2 Pro Unboxing Guide · Figure 2](../_static/yuque-assets/ff635586511091d98504.jpeg)

(yq-dhberyv5btq9hhv1-u7db13cef)=

3. Insert the power board into the card slot and connect it to the Raspberry Pi using the PD 5V5A socket.

(yq-dhberyv5btq9hhv1-u7bc549cf)=

(yq-dhberyv5btq9hhv1-u211461a9)=

![AlohaMini 2 / 2 Pro Unboxing Guide · Figure 3](../_static/yuque-assets/9b3ffee1eb7bff8f0442.jpeg)

(yq-dhberyv5btq9hhv1-ufddea5ac)=

(yq-dhberyv5btq9hhv1-uf3021dc4)=

![AlohaMini 2 / 2 Pro Unboxing Guide · Figure 4](../_static/yuque-assets/3c48272706dd58d09e1f.jpeg)

(yq-dhberyv5btq9hhv1-u58d1153a)=

4. Place another 12V battery into the bottom compartment to power the power strip.

(yq-dhberyv5btq9hhv1-uf88cce31)=

(yq-dhberyv5btq9hhv1-u227ecb5d)=

![AlohaMini 2 / 2 Pro Unboxing Guide · Figure 5](../_static/yuque-assets/8b6b7a675f693f292f8b.png)

(yq-dhberyv5btq9hhv1-u80a2ae89)=

4. After success, the Raspberry Pi screen will light up. The screen is touch screen. You can connect to a 5G band wifi and record the current Raspberry Pi IP address, such as: 192.168.50.88.

(yq-dhberyv5btq9hhv1-u88249dd7)=

(If it is inconvenient to operate, you can also connect the keyboard and mouse via Bluetooth.)

(yq-dhberyv5btq9hhv1-ua2c2dc82)=

(yq-dhberyv5btq9hhv1-3fc02fce)=

### teleoperation terminal:

(yq-dhberyv5btq9hhv1-u0e589181)=

Connect the 5V power supply to the DC line to power the two robotic arms. Both of the following methods will work:

(yq-dhberyv5btq9hhv1-ub080bd30)=

(yq-dhberyv5btq9hhv1-uc3a0c312)=

```{raw} html
<div class="yq-rotated-image" style="aspect-ratio:1707/1280"><img src="../_static/yuque-assets/f9d82b0b03617ae3cf67.jpeg" alt="AlohaMini 2 / 2 Pro Unboxing Guide · Figure 6" style="width:74.9854%;transform:translate(-50%,-50%) rotate(270deg)"></div>
```

(yq-dhberyv5btq9hhv1-u90a66c26)=

(yq-dhberyv5btq9hhv1-u4cde75e8)=

![AlohaMini 2 / 2 Pro Unboxing Guide · Figure 7](../_static/yuque-assets/3b37f35214e5fb1c9d28.jpeg)

(yq-dhberyv5btq9hhv1-u74abb6c6)=

Then connect the USB-C ports of the two robotic arms to the PC

(yq-dhberyv5btq9hhv1-ue76b7978)=

(yq-dhberyv5btq9hhv1-u823879ea)=

(yq-dhberyv5btq9hhv1-812f6a22)=

## Software installation and debugging

(yq-dhberyv5btq9hhv1-u0cc139a3)=

(yq-dhberyv5btq9hhv1-u80107a5d)=

If you have some experience in lerobot development, you can quickly start rocking through the following "[AlohaMini Pro Quick Start Guide](pro-quickstart.md)". If you have never come into contact with lerobot, please refer to "[AlohaMini_beginner tutorial](developer-manual.md)"

(yq-dhberyv5btq9hhv1-uf62692cd)=
