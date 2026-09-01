# Research Skills

本目录同时保存个人学术研究工作流 skills 的唯一源码，并作为 Codex 在 `Research` 工作区中的发现入口。

## 当前范围

- `research-reading`
- `research-thinking`
- `research-analysis`
- `research-writing`
- `research-manuscript-development`
- `research-managing`
- `research-publishing`

`research-reading`、`research-thinking`、`research-analysis`、`research-writing` 与 `research-managing` 构成日常研究循环：

```text
reading ⇄ thinking ⇄ analysis ⇄ writing
                    ↘            ↙
              manuscript-development
                         ↓
                     publishing

managing 按已确认的证据记录项目状态与下一步
```

`research-manuscript-development` 根据稿件阶段和受众协调发展性审阅、投稿场所校准、模拟评审与修订。`research-publishing` 在研究论证和写作产物相对稳定后，将成果转化为演示、摘要、海报、口头报告或公共表达。

各角色的核心边界：

- `reading` 处理学术文献；
- `thinking` 处理研究问题、设计、论证构思和项目层反思；
- `analysis` 处理实际研究对象与经验材料；
- `writing` 创建并持续修改学术文本；
- `manuscript-development` 处理稿件阶段、受众、投稿标准和反馈驱动的修订；
- `managing` 记录已完成、进行中、未完成、下一步和阻碍，不代替研究判断；
- `publishing` 面向特定媒介与受众转化稳定研究成果。

RWS 与 Research 默认独立。只有在用户为具体任务指出材料关系时才跨工作区使用输入；不设置自动晋升、回流、复制或同步机制。

## 目录

```text
.agents/
├── skills/             # skill 源码与 Codex 发现目录
├── skill-use-log/      # 极简使用记录
└── requirements-dev.txt
```

`skills/` 是唯一编辑位置，也是 `Research` 下各研究项目共同使用的发现目录；不再维护另一份源码或符号链接层。

当前阶段不建立评分标准、benchmark 或正式 eval。先通过真实研究项目跑通完整闭环，并在 `skill-use-log/` 中记录实际调用，再依据累积问题决定哪些环节需要修改和测试。

## 使用日志原则

每次任务只记录：

- 日期；
- 项目或任务；
- 实际调用的本仓库 skills；
- 主要产物路径。

不保存完整 prompt、回复文本或评分。系统 skills、插件 skills 和临时工具不纳入本日志。

2026-07-24 以前的日志保留当时实际调用的旧 skill 名称，不追溯改写为合并后的名称。
