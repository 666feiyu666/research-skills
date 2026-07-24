---
name: paper-writing
description: Plan, draft, minimally rewrite, compress, audit, and convert academic papers using an explicit argument structure and the active project's shared state. Use for outline, section-draft, rewrite, argument-audit, citation-audit, compression, or latex-output modes; for separating central claims, subclaims, evidence, and inference; and for marking evidence or citation gaps in Markdown, LaTeX, or plain text. Do not use to invent citations, neutralize the researcher's strong claims, or change the research question without a recorded decision.
---

# Paper Writing

## 适用场景

按明确模式处理论文提纲、章节或全文。若用户未声明模式，根据动词判断并在输出开头注明；仍不确定时默认 `rewrite` 且采用最小修改。

## 不适用场景

不要用未经核查的阅读笔记生成确定性引文，不要替代项目状态管理，不要把强判断改写成中性文献综述。

## 输入文件

写作前必须读取 `ARGUMENT_MAP.md`、`TERMINOLOGY.md`、`DECISIONS.md`；同时读取目标草稿和相关 `PROJECT.md`、`RESEARCH_QUESTIONS.md`、`LITERATURE_NOTES.md`、`references.bib`。只加载当前论证所需材料。

## 标准工作流程

1. 声明模式、目标文件、读者、篇幅和输出格式。
2. 从共享状态提取中心命题、相关子命题、术语约定、被否定框架和未解决缺口。
3. 为每节写一个“论证任务”，并映射 `中心命题 → 子命题 → 证据 → 推论 → 限定/反例`。
4. 按模式执行：
   - `outline`：建立章节任务和依赖，不先写满正文。
   - `section-draft`：只起草指定部分，证据不足处写 `[需证据]` / `[需引用]`。
   - `rewrite`：保留命题强度、作者声音和术语，默认最小修改并给 diff。
   - `argument-audit`：检查跳步、循环论证、证据错配、替代解释和段落功能。
   - `citation-audit`：检查引文是否存在、是否支持附近命题、页码/键是否待核；不联网时只判内部一致性。
   - `compression`：先标记不可丢失的命题和证据，再删重复、背景和弱转折。
   - `latex-output`：转换结构与引用占位，保留原始命题；不伪造 BibTeX 条目。
5. 将实质性论点冲突列为候选决策，不擅自同步 `ARGUMENT_MAP.md`。
6. 写入 `drafts/` 的新候选版本或输出 diff，不覆盖原稿。

## 输出格式

支持 Markdown、LaTeX 和纯文本。默认包含：模式、论证任务、候选文本/diff、证据与引文缺口、与共享状态冲突、建议核查项。使用 `templates/section-plan.md` 或 `templates/audit.md`。

## 共享项目文件

- 必读：`ARGUMENT_MAP.md`、`TERMINOLOGY.md`、`DECISIONS.md`。
- 按需读：`PROJECT.md`、`RESEARCH_QUESTIONS.md`、`LITERATURE_NOTES.md`、`references.bib`。
- 候选输出：`drafts/` 下的新版本；论证层面的冲突或项目变化交给 `research-editor` 审查。

## 质量检查

- 每节只有明确可陈述的论证任务；每段能说明它服务哪个命题。
- 证据与命题匹配，推论没有被写成观察事实。
- 用户强判断的范围和力度未被无故削弱或加强。
- 新文字没有虚构引文、页码、DOI 或书目；缺口已显式标记。
- 改写 diff 足够小；LaTeX 可读且引用键来自已核实的 `references.bib`。

## 与其他 Skills 衔接

从 `research-editor` 接收编辑判断，从 `research-notes`/`critical-reading` 接收可追溯材料；发现研究设计或论证冲突时回交 `research-editor`；稳定稿件交给 `research-publishing` 转译。
