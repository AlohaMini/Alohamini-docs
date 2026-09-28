# Development and extensions

This page is intended for developers who modify the `lerobot_alohamini` software. If you only need to use the robot, start with the [Getting started with models](quickstart.md).

## 1. Create a development environment

Use the project to lock dependencies in the root directory of the software repository:

```bash
uv sync --locked --extra test --extra dev
```

Install only the extras needed for the current job. When it comes to data sets, policies, simulations, or specific hardware, follow the corresponding tutorials to add dependencies. When you need Git LFS test assets:

```bash
git lfs install
git lfs pull
```

## 2. Find the module to be modified

| path | Responsibilities |
| --- | --- |
| `src/lerobot/scripts/` | Command entrances for training, evaluation, recording, etc. |
| `src/lerobot/configs/` | Parameters and dataclass configuration |
| `src/lerobot/robots/alohamini/` | AlohaMini configuration, host and client |
| `src/lerobot/motors/` | Bus, servo configuration and reading and writing |
| `src/lerobot/cameras/` | camera interface |
| `src/lerobot/policies/` | Various policies and factory registration |
| `src/lerobot/processor/` | Input and output processing flow |
| `src/lerobot/datasets/` | LeRobot data set reading and writing |
| `examples/alohamini/` | Arm calibration, teleoperation, acquisition, evaluation |
| `tests/` | Automated testing and fixtures |

When adding a new piece of hardware, first define fields, units, joint sequences, calibration and connection behaviors, and then implement control; changing observations or action definitions will also affect historical data and models.

## 3. Read by stretch goals

| target | Complete tutorial |
| --- | --- |
| Add a new robot, camera or teleoperation device | [Hardware integration](upstream/software--docs-source-integrate_hardware.md) |
| Custom policy | [Integrate your own policy](upstream/software--docs-source-bring_your_own_policies.md) |
| Understanding processors | [Processor introduction](upstream/software--docs-source-introduction_processors.md) |
| Implement new processing steps | [Custom Processor](upstream/software--docs-source-implement_your_own_processor.md) |
| Debug data transformation | [Process debugging](upstream/software--docs-source-debug_processor_pipeline.md) |
| Extended evaluation environment | [New Benchmark](upstream/software--docs-source-adding_benchmarks.md) |
| Compatible with old data and interfaces | [backwards compatible](upstream/software--docs-source-backwardcomp.md) |
| Submit a contribution | [Contribution Statement](upstream/software--contributing.md) |

## 4. Verify changes

First run the tests related to the modified module, for example:

```bash
uv run pytest tests/test_alohamini_sim_bridge.py -svv
```

Complete test entry and format check:

```bash
uv run pytest tests -svv --maxfail=10
pre-commit run --all-files
```

Hardware testing, GPU testing, and integration testing may require additional equipment, assets, or dependencies. Record the actual execution scope, and skipped tests cannot be counted as passed real machine verification.

## 5. Improve documentation

The documentation is written in Markdown and is located in the `source/` directory of the documentation warehouse. When modifying, please indicate the applicable model, check the device parameters in the command, and add a navigation entry for the new page.

Build and preview locally before submitting to confirm that images, videos and links are normal. Changes involving hardware operation should be documented with both verification equipment and software versions.

[View development topics](library-development.md) · [Participate in document contribution](community.md)
