---
name: research-publishing
description: Translate an academic paper or research argument into a conference slide deck, Beamer deck, Chinese oral presentation, academic abstract, poster structure, or WeChat public article without merely compressing the source. Use when Codex needs to adapt argument, examples, pacing, screen text, speaker notes, transitions, information density, or conceptual accessibility for a specific audience and medium. Do not use to change core research claims, fabricate engaging cases, or turn scholarship into entertainment or inspirational prose.
---

# Research Publishing

## 适用场景

把稳定的研究构思或论文转译为特定媒介。先确定受众、场合、时长/字数和媒介约束，再重组入口、节奏与证据。

## 不适用场景

不要替代论文论证审查，不要为了传播性修改核心命题，不要使用未经核实的轶事或数据。

## 输入文件

读取目标论文/构思及 `PROJECT.md`、`RESEARCH_QUESTIONS.md`、`ARGUMENT_MAP.md`、`TERMINOLOGY.md`、`DECISIONS.md`。需要案例和引文时读取相关 `LITERATURE_NOTES.md` 与 `references.bib`。

## 标准工作流程

1. 声明输出类型：学术会议 PPT、Beamer、中文口头报告、学术摘要、海报结构或公众号文章；记录受众、时长/篇幅与目的。
2. 抽取必须保留的核心问题、中心命题、关键证据、限定条件与术语。
3. 重新设计媒介叙事：选择入口、展开顺序、证据节奏和结尾行动；不要按原文章节机械压缩。
4. PPT/Beamer 使用“一页一个中心判断”。标题写问题或命题；分离屏幕文字与演讲者备注；每页给出到下一页的过渡。
5. 检查中文字号、行数、信息密度、图文层级和可访问性。不能生成真实幻灯片时，输出明确的页面规格。
6. 口头报告写可说出口的句子、时间标记和过渡，不把论文句子直接搬上讲台。
7. 摘要保留问题、材料/方法、中心发现/论点和贡献，未知结果不伪装为已完成。
8. 公众号文章从具体问题、案例或经验进入，解释概念而不鸡汤化、娱乐化；保留证据边界和研究核心。
9. 将输出保存到 `presentations/` 的候选文件；发现核心论点需变更时停止并交给 `research-editor`。

## 输出格式

PPT/Beamer 默认使用 `templates/slide-plan.md`；公众号使用 `templates/public-article.md`。输出还应包含受众假设、被保留/改写/省略的内容及理由、事实核查清单。

## 共享项目文件

- 读取：`PROJECT.md`、`RESEARCH_QUESTIONS.md`、`ARGUMENT_MAP.md`、`TERMINOLOGY.md`、`DECISIONS.md`，按需读取文献与书目。
- 候选输出：`presentations/`。
- 不直接改动研究状态；核心变化交给 `research-editor`，论文层面的缺口交给 `paper-writing`。

## 质量检查

- 输出是媒介转译而非删短版论文；核心命题和限定条件没有变形。
- 每页只有一个中心判断，标题可独立表达问题/命题，备注与屏幕文字分开。
- 过渡说明为什么下一页此时出现；中文字号和密度适合现场阅读。
- 公共写作有具体入口、概念解释和证据边界，不伪造案例、不煽情替代论证。
- 所有数字、引文、图表来源和书目信息可核查；不确定项明确标记。

## 与其他 Skills 衔接

接收 `paper-writing` 的稳定论证与 `research-editor` 的编辑判断；从 `research-notes` 获取经核实的案例/概念；传播格式暴露出的论证缺口回交 `paper-writing`，核心研究冲突回交 `research-editor`。
