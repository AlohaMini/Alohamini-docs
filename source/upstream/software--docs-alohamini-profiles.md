# Hardware Profile Reference

[← 教程资料库](../tutorial-library.md) · **AlohaMini 原始教程 / 原文全文**

本文是 AlohaMini 项目资料，具体代际以原文路径和硬件配置为准。

来源：[liyiteng/lerobot_alohamini · `docs/alohamini/profiles.md`](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/docs/alohamini/profiles.md) · 版本 `7843e588` · [下载未经改写的源文档](../_static/upstream-originals/software/docs/alohamini/profiles.md.txt)

本页保留原文语言及全部段落、表格和代码；仅调整标题层级、页面组件、代码围栏格式、相对链接和媒体路径。原文中的价格、性能和运行结果属于该版本记录。

---


The host-side `--robot_model` flag and PC-side `--robot.robot_model` / `--teleop.arm_profile`
flags select your hardware variant.

Use the same model value for host-side `--robot_model` and PC-side `--robot.robot_model`.
Use `--teleop.arm_profile` only for the leader arm connected to the PC.

## AlohaMini host-side (`--robot_model`)

| `--robot_model` | Follower arm | Base wheels | Lift motor | Lead screw |
|-----------------|--------------|-------------|------------|------------|
| `alohamini1` | `so-arm-5dof` | STS3215 ×3 | STS3215 | 84 mm/rev |
| `alohamini2` | `am-follower-6dof` | STS3215 ×3 | STS3095 | 131 mm/rev |
| `alohamini2pro` | `am-follower-6dof-hd` | STS3250 ×3 | STS3095 | 131 mm/rev |

## AM-ARM200 arm profiles (`--teleop.arm_profile`)

| Product SKU | Role | `--teleop.arm_profile` |
|-------------|------|-----------------|
| AM-ARM200 | Leader (5V) | `am-leader-6dof` |
| AM-ARM200 | Follower (12V) | `am-follower-6dof` |
| AM-ARM200 Pro | Leader (5V) | `am-leader-6dof` |
| AM-ARM200 Pro | Follower (12V HD) | `am-follower-6dof-hd` |
