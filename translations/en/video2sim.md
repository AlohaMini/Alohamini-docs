# Mobile phone video reconstruction of Isaac Sim scene

`video2sim` converts indoor videos captured by mobile phones into renderable Gaussian scenes and colliders with realistic scales, and then assembles them into Isaac Sim scenes. This page is based on the README and the current `cli.py` to supplement the differences in local paths, run endpoints and model files.

## 1. Preparation before operation

Sample test environment is NVIDIA RTX 4060 8 GB, ~32 GB RAM, and Isaac Sim 5.x. This is a test configuration under a specific scenario. There is no guarantee that any resolution or video duration can be completed with the same resources.

| environment | Required components |
| --- | --- |
| main environment | CUDA Torch、gsplat、pycolmap、open3d、scipy、PIL、ninja、PyYAML |
| NuRec export environment | pxr, Torch, msgpack, ncore and 3dgrut export dependencies |
| Isaac Environment | Isaac Sim 5.x, pxr and NuRec schema |
| External tools and models | ffmpeg, ffprobe, matching LingBot-Map fork and weights |

The reconstruction environment is separate from the UV environment controlled by the whole machine. Prepare the components first before checking them below; this tutorial does not automatically create these complex environments.

## 2. Set the local path

`/home/perelman/...` is an example path, direct copying cannot be used on other machines. Enter the module directory in the software repository:

```bash
cd /path/to/lerobot_alohamini/alohamini_sim/video2sim
```

Create your own `local.yaml`, replacing all example absolute paths:

```yaml
main_python: /path/to/main-env/bin/python
nurec_python: /path/to/nurec-env/bin/python
isaac_python: /path/to/isaac-env/bin/python
lingbot_repo: /path/to/LingBot-Map
lingbot_model: /path/to/lingbot-map-long.pt
stage_args:
  train:
    iters: 10000
```

`cli.py` uses `stage_args` to pass phase parameters. The values written by top-level groups such as `extract` and `train` in warehouse `configs/default.yaml` also include recipe records. It cannot be assumed that any top-level field will become a command line parameter. The underscores and hyphens in the parameters must be consistent with the entrances of each stage.

## 3. Check the environment

```bash
python3 -m video2sim.check_env \
  --main-python /path/to/main-env/bin/python \
  --nurec-python /path/to/nurec-env/bin/python \
  --isaac-python /path/to/isaac-env/bin/python \
  --lingbot-repo /path/to/LingBot-Map \
  --model /path/to/lingbot-map-long.pt
```

Checkers verify dependencies in their respective interpreters, displaying PASS, WARN, FAIL. Handle failed items first. In an 8 GB video memory environment, the GPU needs to be released during inference and training to avoid having the Isaac GUI occupying video memory at the same time.

## 4. Perform a rebuild

```bash
/path/to/main-env/bin/python -m video2sim run /path/to/room.mp4 \
  --config local.yaml \
  --workdir runs/room1
```

**ends at `scene_prep`** by default, and the scene appearance, alignment parameters and collision data will be prepared; the final `scene` stage will not be run by default.

| stage | Main products | Check the key points |
| --- | --- | --- |
| extract | `frames/f_*.jpg` | Image orientation and clarity |
| lingbot_infer | `lingbot/pred-*.pt` | Are the pose and depth complete? |
| fuse | `fuse/mvtsdf.ply` and mesh | Surface, noise and memory |
| refine | `final_mesh.ply`、`final_cloud.ply`、`final_align.npz` | Ground orientation, scale and coordinate transformation |
| to_colmap | `sparse/0/` | Cameras and dense initialization data |
| train | `splat.pt` | Appearance, floating points, training log |
| export | `export/scene.usdz` | Is NuRec export successful? |
| scene_prep | `collider.npz` | collision mesh |
| scene (explicitly enabled) | `scene/scene.usd` | Whether the appearance is aligned with the collision body |

The current process uses LingBot pose and depth, and does not take COLMAP SfM solution as the main line; `to_colmap` is the format needed to generate subsequent training.

## 5. Assembling and viewing the Isaac scene

Currently `scene.py` reads `alohamini2pro_parallel.usd` in the warehouse by default, and the USD assets provided with the warehouse can be used. The URDF with the same name mentioned in the README was not found in this submission, but this does not block the default USD scene entry; when you need to import the URDF or run ManiSkill, the corresponding model must be completed separately.

After the environment and assets are complete, execute the final phase explicitly:

```bash
/path/to/main-env/bin/python -m video2sim run \
  --config local.yaml \
  --workdir runs/room1 \
  --until scene
```

When a GUI is required:

```bash
/path/to/main-env/bin/python -m video2sim run \
  --config local.yaml \
  --workdir runs/room1 \
  --gui
```

When a stage output already exists, the runner will skip the corresponding stage. Use a new working directory after changing models, videos, or key parameters to avoid mistaking old results for new results.

## 6. Recipe parameters and troubleshooting

The complete parameter list, parameter reasons, v10/v11 comparison and troubleshooting have been retained in the [video2sim configuration reference](upstream/software--alohamini_sim-video2sim-readme.md). The scale assumptions of 2.4 m from floor to ceiling and 1.35 m hand-held height must conform to the actual shooting environment.

| phenomenon | Priority check |
| --- | --- |
| Insufficient video memory | Other GPU processes, Isaac GUI, input resolution, LingBot window and number of Gaussians |
| Wrong direction of ground | floor detection, camera trajectory filtering, `final_align.npz` |
| The scene is foggy or has too many floating points | Camera pose, scale, training parameters and initialization point cloud |
| The collision does not match the screen | Whether export and scene assembly use the same alignment transform |
| NuRec export import failed | Whether to use the specified NuRec/Isaac interpreter with schema |
| Can’t see `scene.usd` | Whether to run `--until scene` explicitly and whether the assets are complete |

After completing the scene check, enter [Synthetic data generation and conversion](sim-data.md). Scenes can be displayed, trajectories can be generated, and data can be trained are three independent checkpoints.
