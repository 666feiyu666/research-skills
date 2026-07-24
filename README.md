# Research Skills

本仓库保存个人学术研究工作流 skills 的唯一源码。

## 当前范围

- `critical-reading`
- `literature-scout`
- `notes-writing`
- `paper-writing`
- `research-editor`
- `research-notes`
- `research-problem`
- `research-publishing`

## 目录

```text
Research-Skills/
├── skills/             # 可被 Codex 调用的 skill 源码
└── skill-use-log/      # 极简使用记录
```

`skills/` 是唯一编辑位置。`/Users/paimon/Research/.agents/skills/` 中的同名入口使用符号链接指向这里，使这些 skills 可用于 `Research` 下的研究项目。

当前阶段不建立评分标准、benchmark 或正式 eval。先通过真实研究项目跑通完整闭环，并在 `skill-use-log/` 中记录实际调用，再依据累积问题决定哪些环节需要修改和测试。

## 使用日志原则

每次任务只记录：

- 日期；
- 项目或任务；
- 实际调用的本仓库 skills；
- 主要产物路径。

不保存完整 prompt、回复文本或评分。系统 skills、插件 skills 和临时工具不纳入本日志。
