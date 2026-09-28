# AlohaMini 官方文档

AlohaMini 官方文档与教程，涵盖硬件组装、软件安装、遥操作、数据采集、策略训练和真机部署。

![AlohaMini 一代机器人](source/_static/media/assembled2.png)

*图为 AlohaMini 一代实机。*

[硬件项目](https://github.com/liyiteng/AlohaMini) · [机器人软件](https://github.com/liyiteng/lerobot_alohamini) · [Discord 社区](https://discord.gg/CacMUBaFgJ)

## 文档内容

- **硬件搭建**：物料清单、3D 打印、组装与走线。
- **安装与操作**：软件配置、机械臂校准、遥操作。
- **数据与训练**：数据采集、回放检查、策略训练与真机评估。
- **进阶与支持**：单臂教程、OpenPI、仿真、常见问题。

## 本地预览

使用 **Sphinx + PyData Sphinx Theme + MyST Parser** 构建，需要 Python 3.11 或更新版本。

在本目录运行（macOS / Linux）：

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python tools/build_docs.py
python -m http.server 8765 --bind 127.0.0.1 --directory build/html
```

打开 [http://127.0.0.1:8765/](http://127.0.0.1:8765/) 查看网站。修改内容后，重新运行构建命令并刷新页面。

## 修改内容

- **修改教程**：编辑 `source/` 下对应的 `.md` 文件。
- **英文内容**：编辑 `translations/en/` 下同名的 `.md` 文件；新增页面时同时添加英文版。构建后中文位于网站根目录，英文位于 `/en/`，顶部按钮切换到同一篇教程。
- **添加图片**：放入 `source/_static/media/`，在文档中引用。
- **新增页面**：创建 `.md` 文件，并加入 `source/index.md` 的 `toctree` 和 `source/conf.py` 的 `navigation_groups`。
- **调整样式**：编辑 `source/_static/alohamini.css`。

欢迎提交 Issue 或 Pull Request，一起完善 AlohaMini 文档。
