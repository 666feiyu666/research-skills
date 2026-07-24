---
name: critical-reading
description: Extract and critically read academic PDFs, scanned documents, images, EPUB, DOCX, Markdown, or plain text while preserving page or location mappings. Use when Codex needs to assess a document's text layer, invoke OCR only as fallback, identify structure, concepts, argument chains, evidence, footnotes, tables and captions, collect verifiable passages, develop questions or counterarguments, and relate a source to the active research project. Do not use for unsupported citation verification or for synthesizing many already-processed notes.
---

# Critical Reading

## 适用场景

处理一篇或一组需要逐篇阅读的新材料，并产出可回查的阅读记录。PDF 版面影响含义时，同时查看渲染页，不只依赖抽取文本。

## 不适用场景

不要把抽取结果当作出版级文本，不要凭文件名补齐书目信息，不要用 OCR 猜测难以辨认的引文。多文献主题综合转给 `research-notes`。

## 输入文件

接受原生文本 PDF、扫描 PDF、图片、EPUB、DOCX、Markdown 和纯文本。读取项目的 `PROJECT.md`、`RESEARCH_QUESTIONS.md`、`ARGUMENT_MAP.md`、`TERMINOLOGY.md`、`DECISIONS.md`，按需读取已有 `LITERATURE_NOTES.md`。

## 标准工作流程

1. 识别格式：PDF 先执行 `scripts/pdf_text.py inspect`；DOCX/EPUB/Markdown/文本优先读取原生结构；图片视为需 OCR。
2. 优先使用已有文本层。逐页/逐章提取并保留 `page`、章节或段落定位。
3. 检查文本质量：空页比例、字符密度、替换字符、乱码、抽取顺序和明显缺段。只有缺失、乱码或显著不完整时才运行 `scripts/ocr_fallback.py`。
4. OCR 默认考虑简体中文、繁体中文和英文（`chi_sim+chi_tra+eng`）。把 OCR 结果标为“机器识别，可能有误，引用前核对原页”。
5. 用标题层级、字体/位置线索或文本模式识别章节；单独记录脚注、表格、图注及其页码。识别不可靠时明确说明。
6. 分离作者问题、概念定义、论证步骤、证据类型和推论；避免把摘要复述当作论证分析。
7. 可引用段落必须短、带页码/定位，并与原页核对。未核对的 OCR 片段只能列为候选。
8. 使用 `templates/reading-record.md` 输出，再以候选 diff 追加到 `LITERATURE_NOTES.md`；概念候选交给 `research-notes`。

## 输出格式

输出文献基本信息、处理说明、章节结构、核心问题、核心概念、论证链、关键证据、可引用段落及页码、疑问和反驳、与当前研究的关系、可发展的随笔/评论方向。逐页机器结果保存为 JSON，阅读记录保存为 Markdown。

## 共享项目文件

- 读取：`PROJECT.md`、`RESEARCH_QUESTIONS.md`、`ARGUMENT_MAP.md`、`TERMINOLOGY.md`、`DECISIONS.md`、已有 `LITERATURE_NOTES.md`。
- 候选更新：`LITERATURE_NOTES.md`；经核实后可建议更新 `references.bib`。
- 原始材料和抽取/OCR 中间件放入 `readings/`，不覆盖原文件。

## 质量检查

- 明确记录使用文本层还是 OCR、工具、语言和失败页。
- 页码映射没有在清理时丢失；PDF 页序号与印刷页码差异已说明。
- 引文、脚注、表格和图注均可回到原页；无法可靠解析的元素已标记。
- 不虚构 DOI、页码、书目信息或作者未说过的概念。
- 反驳与延伸标为 **[用户判断]** 或 **[模型建议]**，不混入 **[文献观点]**。

## 与其他 Skills 衔接

把阅读记录交给 `research-notes` 做跨文献整理；把证据/文献缺口交给 `research-editor`；把经核查的论证和引文候选交给 `paper-writing`；把适于传播的案例候选交给 `research-publishing`。
