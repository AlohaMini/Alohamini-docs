from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent / "_ext"))

project = "AlohaMini"
author = "Li Yiteng & Wu Zhiyong"
copyright = "2026, AlohaMini Contributors"
language = "zh_CN"
extensions = ["myst_parser", "sphinx_copybutton", "am_languages"]
myst_enable_extensions = ["colon_fence", "deflist"]
myst_heading_anchors = 3
templates_path = ["_templates"]
exclude_patterns = ["_ext"]
html_theme = "pydata_sphinx_theme"
html_title = "AlohaMini 文档"
html_static_path = ["_static"]
html_css_files = ["alohamini.css"]
html_js_files = ["language-switcher.js", "reading-guide.js"]
html_favicon = "_static/favicon.svg"
html_show_sourcelink = False
html_copy_source = False
html_show_sphinx = False
html_search_language = "zh"
html_sidebars = {"index": [], "**": ["am-sidebar.html"]}
html_theme_options = {
    "navbar_start": ["am-brand.html"],
    "navbar_center": ["am-navbar.html"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "navbar_persistent": ["am-language-switcher.html", "search-button-field"],
    "navbar_align": "content",
    "icon_links": [{"name": "GitHub", "url": "https://github.com/liyiteng/AlohaMini", "icon": "fa-brands fa-github"}],
    "primary_sidebar_end": ["am-sidebar-footer.html"],
    "secondary_sidebar_items": ["page-toc"],
    "footer_start": ["copyright"],
    "footer_end": ["am-footer.html"],
    "show_prev_next": True,
    "navigation_with_keys": False,
    "search_bar_text": "搜索文档…",
    "show_toc_level": 2,
    "back_to_top_button": True,
}
html_context = {'default_mode': 'auto',
 'navigation_groups': [('开始使用',
                        [('quickstart', '选择型号', ''),
                         ('alohamini2', 'AlohaMini 2 入门', ''),
                         ('alohamini2pro', 'AlohaMini 2 Pro 入门', '')]),
                       ('数据与训练',
                        [('learning', '数据采集与检查', ''),
                         ('training', '策略训练', ''),
                         ('evaluation', '真机评估', '')]),
                       ('硬件搭建',
                        [('bom', '物料清单', ''),
                         ('printing', '3D 打印', ''),
                         ('assembly', '硬件组装', ''),
                         ('hardware-pro', '2 Pro 硬件说明', ''),
                         ('unboxing', '开箱与首次通电', '')]),
                       ('专题与进阶',
                        [('software', '软件安装', ''),
                         ('configuration', '设备与机型配置', ''),
                         ('calibration', '机械臂校准', ''),
                         ('teleoperation', '遥操作', ''),
                         ('single-arm', 'AM-ARM200 单臂', ''),
                         ('pi05', 'Pi 0.5 / OpenPI', ''),
                         ('simulation', '仿真与模型可视化', ''),
                         ('video2sim', '手机视频重建场景', ''),
                         ('sim-data', '仿真数据生成与转换', ''),
                         ('runtime', '运行机制与保护', ''),
                         ('debug-tools', '舵机与性能调试', ''),
                         ('policies', '策略与训练教程', ''),
                         ('docker', 'Docker 环境', ''),
                         ('development', '开发与扩展', '')]),
                       ('资料与支持',
                        [('troubleshooting', '调试与排错', ''),
                         ('commands', '命令参考', ''),
                         ('specifications', '机型与参数', ''),
                         ('tutorial-library', '教程资料库', ''),
                         ('yuque/videos', '演示视频', ''),
                         ('legacy', 'AlohaMini 1', ''),
                         ('legacy-hardware', '一代物料与装配', ''),
                         ('community', '社区与贡献', '')])]}
