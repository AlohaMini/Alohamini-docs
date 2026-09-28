# How to contribute to 🤗 LeRobot

[← 教程资料库](../tutorial-library.md) · **开发与扩展 / 原文全文**

本文保留软件仓库的通用或进阶教程。示例中的机器人、数据集、路径和运行环境需按实际配置选择，不代表已经在 AlohaMini 2 / 2 Pro 上验证。

来源：[liyiteng/lerobot_alohamini · `CONTRIBUTING.md`](https://github.com/liyiteng/lerobot_alohamini/blob/7843e5888366eaa553630e2f9d5539505a62dddf/CONTRIBUTING.md) · 版本 `7843e588` · [下载未经改写的源文档](../_static/upstream-originals/software/CONTRIBUTING.md.txt)

本页保留原文语言及全部段落、表格和代码；仅调整标题层级、页面组件、代码围栏格式、相对链接和媒体路径。原文中的价格、性能和运行结果属于该版本记录。

---


Everyone is welcome to contribute, and we value everybody's contribution. Code is not the only way to help the community. Answering questions, helping others, reaching out, and improving the documentation are immensely valuable.

Whichever way you choose to contribute, please be mindful to respect our [code of conduct](https://github.com/huggingface/lerobot/blob/main/CODE_OF_CONDUCT.md) and our [AI policy](https://github.com/huggingface/lerobot/blob/main/AI_POLICY.md).

## Ways to Contribute

You can contribute in many ways:

- **Fixing issues:** Resolve bugs or improve existing code.
- **New features:** Develop new features.
- **Extend:** Implement new models/policies, robots, or simulation environments and upload datasets to the Hugging Face Hub.
- **Documentation:** Improve examples, guides, and docstrings.
- **Feedback:** Submit tickets related to bugs or desired new features.

If you are unsure where to start, join our [Discord Channel](https://discord.gg/q8Dzzpym3f).

## Development Setup

To contribute code, you need to set up a development environment.

### 1. Fork and Clone

Fork the repository on GitHub, then clone your fork:

```bash
git clone https://github.com/<your-handle>/lerobot.git
cd lerobot
git remote add upstream https://github.com/huggingface/lerobot.git
```

### 2. Environment Installation

Please follow our [Installation Guide](https://huggingface.co/docs/lerobot/installation) for the environment setup & installation from source.

## Running Tests & Quality Checks

### Code Style (Pre-commit)

Install `pre-commit` hooks to run checks automatically before you commit:

```bash
pre-commit install
```

To run checks manually on all files:

```bash
pre-commit run --all-files
```

### Running Tests

We use `pytest`. First, ensure you have test artifacts by installing **git-lfs**:

```bash
git lfs install
git lfs pull
```

Run the full suite (this may require extras installed):

```bash
pytest -sv ./tests
```

Or run a specific test file during development:

```bash
pytest -sv tests/test_specific_feature.py
```

## Submitting Issues & Pull Requests

Use the templates for required fields and examples.

- **Issues:** Follow the [ticket template](https://github.com/huggingface/lerobot/blob/main/.github/ISSUE_TEMPLATE/bug-report.yml).
- **Pull requests:** Rebase on `upstream/main`, use a descriptive branch (don't work on `main`), run `pre-commit` and tests locally, and follow the [PR template](https://github.com/huggingface/lerobot/blob/main/.github/PULL_REQUEST_TEMPLATE.md).

> [!IMPORTANT]
> Community Review Policy: To help scale our efforts and foster a collaborative environment, we ask contributors to review at least one other person's open PR before their own receives attention. This shared responsibility multiplies our review capacity and helps everyone's code get merged faster!

Once you have submitted your PR and completed a peer review, a member of the LeRobot team will review your contribution.

Thank you for contributing to LeRobot!
