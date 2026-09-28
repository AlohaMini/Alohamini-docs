# 语雀公开页面快照

读取日期：2026-09-28。来源为 `alohamini.yuque.com/lq44as/tiv9xs/` 的公开使用手册目录。

- `index.json`：浏览器中观察到的文档链接。
- 文档 ID `.json`：已加载正文的精简 DOM、可见文本、链接和图片地址。不是语雀原生 Markdown 导出。
- `.codes.json`：逐个点击加载后取得的 65 个代码块，包括完整行文本和是否存在未呈现行的检查结果。
- `assets.json` / `.assets.json`：正文图片地址、本地路径和 SHA-256；文件保存在 `source/_static/yuque-assets`。
- `attachments.json`：《模型Policy.pdf》的公开下载入口，当前需登录；未获取附件内容。

正文卡片的图标、OCR 覆盖层、复制按钮等界面元素不参与转写。图片保留原始字节；来源页面旋转过的图片使用网页样式还原方向。原文备份保留视频来源入口；展示页使用 Bilibili 嵌入播放器，两段语雀新闻视频使用 `source/_static/yuque-videos` 中的本地文件。

在安装 BeautifulSoup 和 Pillow 的文档环境中运行 `python tools/import_yuque_docs.py`，可从这些快照重新生成 `source/yuque`、原始转写下载和 `yuque-manifest.json`。该过程不访问网络、不运行教程命令，不覆盖人工整合的入口和主线章节。

`yuque-manifest.json` 记录站内页的勘误。未作这些勘误的转写保存在 `source/_static/yuque-originals`，用于核对。网页可见文本可能含界面文字或截图 OCR，只作为核对辅助；页面结构和逐块保存的代码用于构建正文。
