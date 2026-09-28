# Synthetic data generation and conversion

This page corresponds to `alohamini_sim/` of the software repository, and [Generation ROS 2 Visualization](simulation.md) are two sets of processes with different purposes. The former generates scenes and data, the latter looks at URDFs and joint structures.

## 1. First understand the three links

| link | input and output | Operating environment |
| --- | --- | --- |
| video2sim | Mobile Video → Scene Appearance, Colliders and Isaac USD | Discrete GPU toolchain |
| data engine | Tasks, robots and environments → episode dictionary | Execution environments such as ManiSkill / SAPIEN |
| LeRobot bridge | episode dictionary → LeRobotDataset v3 | `lerobot_alohamini`’s uv environment |

The capture demo will not be automatically generated after the scene reconstruction is completed. You need to prepare tasks, controllers, skills and cameras in the data engine, generate trajectories, and then hand them over to the bridge for conversion.

## 2. Current robot and dimension restrictions

```{important}
Currently `lerobot_bridge.py` uses `SIM_ARM_PROFILE = "so-arm-5dof"` and outputs **16 dimension** state/action. The 18 values of the input emulation `qpos` are not equal to the 18-dimensional interface of the AlohaMini 2 / 2 Pro. It cannot be directly used as mixed training data for the second-generation machine.
```

| data | original meaning | After conversion |
| --- | --- | --- |
| `qpos` | 18-dimensional simulation status | Get the corresponding joints, grippers, chassis and lifting to generate a 16-dimensional state |
| `action` | 16-dimensional control objectives | Convert to 16D action |
| Arm joints | radians | Currently, the original value is maintained and needs to be normalized or aligned with the real machine or angle semantics. |
| Gripper | Finger joint displacement, unit meter | Leave by default; available closed/open range conversion to 0–100 |
| Chassis x/y | World coordinate position or target | Convert to body coordinate system speed, unit m/s |
| Chassis rotation | yaw or target angle | Convert to angular velocity in deg/s |
| lifting | meters | Convert to millimeters |

Even if the feature names are the same, check the units, gripper range, camera, motion timing, and calibration. The output data set can be read, which simply means that the format holds.

## 3. Prepare execution environment and model assets

The data engine directory contains `aspire_engine`, `intern_engine` and robot agents. Executing rollout requires external ManiSkill, SAPIEN, Torch, GPU and Vulkan; the software installation environment of this site does not automatically meet these conditions.

The example uses `aloha_mini_pro_v2.urdf`, `aloha_mini_pro_v3.urdf`, `maniskill_so100_version.urdf` which are not provided with the current version. First complete the model and grid that match the agent; if necessary, specify the model directory through `ALOHAMINI_URDF_DIR`. Do not equate the "Pro" filename directly with the current 2 Pro AM follower arm configuration.

Skill organization, triggering and metadata can be found in the [Skill library](upstream/software--alohamini_sim-data_engine-data_gen-intern_engine-skills-library-readme.md). Different tasks require executor configuration based on actual environment registration and task definition.

## 4. Prepare bridge environment

Run in the root directory of the software repository:

```bash
uv sync --locked --extra test --extra dataset
uv run pytest tests/test_alohamini_sim_bridge.py tests/test_alohamini_sim_engine_imports.py -svv
```

These tests use small synthetic episodes to check transformations, features, and reading and writing. When ManiSkill is not installed, the executor import test may be skipped; this does not mean that the real simulation rollout is verified.

## 5. Check the episode structure

```python
episode = {
    "steps": [
        {
            "qpos": qpos,       # float32[18]
            "action": action,   # float32[16]
            "rgb": {"front": image},  # uint8[H, W, 3]，RGB
        }
    ],
    "annotation": "Pick up the object and place it in the tray",
}
```

The above is a structural diagram. `qpos`, `action`, and `image` require real arrays provided by the engine. Camera names, resolutions, and fields in the same data set should be consistent, and FPS should be consistent with the time interval for generating trajectories.

## 6. Convert to LeRobotDataset

After saving the trusted episodes you generated as a pickle file in the form of a list, execute the following in the root directory of the software repository:

```bash
uv run python -m alohamini_sim.data_engine.lerobot_bridge \
  --episodes out/episodes.pkl \
  --repo-id local/alohamini_sim_pick \
  --root out/lerobot_ds \
  --fps 20
```

pickle will perform object deserialization at load time and only read files that you generate or confirm are trusted. `root` points to this output location, do not overwrite existing experiments.

Can also be called in the same environment:

```python
from alohamini_sim.data_engine.lerobot_bridge import write_episodes

write_episodes(
    episodes,
    repo_id="local/alohamini_sim_pick",
    root="out/lerobot_ds",
    fps=20,
)
```

Information such as simulation seeds, skill traces, command and final will not all be written to LeRobot standard fields; the original results of the engine are retained to facilitate reproduction and troubleshooting.

## 7. Post-conversion inspection

```bash
uv run lerobot-dataset-viz \
  --repo-id local/alohamini_sim_pick \
  --root out/lerobot_ds \
  --episode-index 0 \
  --display-compressed-images
```

Check task descriptions, frame numbers, camera colors, motion continuity, joint order, and units one by one. If the target is second-generation mixed training, you need to complete the 18-dimensional adaptation of the bridge first and verify the real machine calibration mapping; simply modifying the `robot_type` label will not change the data structure.
