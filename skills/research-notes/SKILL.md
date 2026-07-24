---
name: research-notes
description: Organize traceable academic notes, literature claims, concepts, methods, cases, and open questions for digital humanities, computational social science, or anthropology projects. Use when Codex needs to consolidate scattered reading notes, distinguish author claims from the researcher's judgments and model suggestions, deduplicate without losing sources, update LITERATURE_NOTES.md or TERMINOLOGY.md, or produce a concept map or literature matrix. Do not use for close reading of a new full text, managing the whole research plan, or drafting polished paper prose.
---

# Research Notes

## 适用场景

整理零散笔记、综合多篇文献、消除有来源的重复项、维护术语，或生成概念图/文献矩阵。若输入是一篇尚未处理的全文，先用 `critical-reading`。

## 不适用场景

不要负责最终引文核实、整篇论文写作或研究问题的重大变更。不要把未解决笔记自动升级为成熟结论。

## 输入文件

读取用户指定笔记和项目中的 `PROJECT.md`、`RESEARCH_QUESTIONS.md`、`LITERATURE_NOTES.md`、`TERMINOLOGY.md`、`DECISIONS.md`。需要论证关系时再读 `ARGUMENT_MAP.md`。缺文件时从 `workspace-template/` 建议创建，不虚构内容。

## 标准工作流程

1. 先确认项目目录并读取现状；不得把 Skill 目录当项目状态。
2. 把每个原子笔记标为 **[文献观点]**、**[用户判断]**、**[模型建议]** 或 **[未解决问题]**。无法判断时标记待确认。
3. 为文献观点保留 citation key、页码/章节/段落或原始文件定位。OCR 来源加“需核对原页”。
4. 按主题、概念、方法、案例和论证功能建立多个视图；不要强迫每条只属于一个分类。
5. 合并仅在含义等价时进行，合并项列出全部来源。冲突观点并列保留。
6. 先输出候选 diff，再经确认更新 `LITERATURE_NOTES.md` 与 `TERMINOLOGY.md`。
7. 若整理产生研究方向、缺口或状态变化，把它作为建议交给 `research-editor`，不要自行覆盖研究问题。

## 输出格式

默认使用 `templates/note-batch.md`。概念图优先 Mermaid；文献矩阵使用 Markdown 表格或 CSV，至少包含文献、问题、概念、方法/案例、证据、论证功能、分歧和定位。

## 共享项目文件

- 读取：`PROJECT.md`、`RESEARCH_QUESTIONS.md`、`DECISIONS.md`，按需读取 `ARGUMENT_MAP.md`。
- 候选更新：`LITERATURE_NOTES.md`、`TERMINOLOGY.md`。
- 不直接更新：`references.bib`，除非书目信息已由用户或可靠来源核实。

## 质量检查

- 每个实质判断都有来源标签；文献观点可回到原始位置。
- 重复项合并后没有丢失来源、异议和限定条件。
- 模型解释没有冒充作者观点或用户判断。
- 新概念写明工作定义、来源和争议，不制造虚假共识。
- 输出仍保留“不知道什么”，而非用流畅措辞掩盖缺口。

## 与其他 Skills 衔接

接收 `critical-reading` 的逐篇阅读记录；把概念分歧、证据缺口和新问题交给 `research-editor`；为 `paper-writing` 提供可追溯材料；为 `research-publishing` 提供经核实的概念与案例入口。
