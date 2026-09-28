# 文档语言维护

- 中文正文：`source/`。
- 英文正文：`translations/en/`，文件路径与中文一一对应。
- 英文侧栏名称：`translations/en/navigation.json`。
- 修改教程时同步更新两种语言；代码块、命令参数和资源路径应保持一致。
- 图片和视频共用现有资源，图片内文字和视频音轨保持原样。

```bash
python tools/build_docs.py
python tools/verify_docs.py
python tools/verify_languages.py
```

构建输出：中文为 `build/html/`，英文为 `build/html/en/`。英文页面保留中文页面的章节锚点，旧链接和语言切换均可定位到对应章节。新增页面缺少英文文件、章节结构不同或命令发生变化时，构建或检查会失败。

初版英文正文使用机器翻译辅助生成，并统一机器人术语；后续直接维护 Markdown，不依赖在线翻译服务。技术内容变更时应复核两种语言的步骤、型号、单位及参数。
