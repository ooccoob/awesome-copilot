---
post_title: "kusto-assistant.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "kusto-assistant-chatmode-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: ["use-cases","chatmode","kusto"]
tags: ["use-cases","kql","kusto","data-explorer"]
ai_note: "Generated with AI assistance from chatmodes/kusto-assistant.chatmode.md"
summary: "Use cases for Kusto Assistant: KQL query engineering, schema discovery, sampling, and result presentation for Azure Data Explorer." 
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- An expert KQL (Kusto) assistant focused on helping users write, execute, and interpret Kusto queries against Azure Data Explorer via MCP tooling.

## When

- When analysts and engineers need to explore data, write performant KQL, or convert SQL-like analytics into Kusto queries and results.

## Why

- To accelerate data exploration, reduce query errors, and provide reproducible, well-formed KQL for operational analysis.

## How

- Follow a multi-step approach: schema discovery → query construction → execution with ingestion-delay-aware time windows → results summarization.
- Use fully qualified table names and account for ingestion delays by default (queries ending 5 minutes ago). 
- Prefer returning small tables or single-number summaries inline; offer CSV export for large results.

## Key points (英文+中文对照)

- Use ingestion-aware time windows（使用考虑摄取延迟的时间窗口）
- Prefer fully-qualified table names（优先使用完全限定表名）
- Display small result sets inline; export large sets（小结果集内联展示，大结果导出为 CSV）

## 使用场景

### 1. 快速生成分析查询

- 用户故事：作为数据分析师，我希望把业务问题转换为 KQL 查询并得到可复现的分析结果。
- 例 1："[问题] 请用 KQL 计算过去 1 小时内的错误率，并返回 top 5 的错误类型。"
- 例 2："[转换] 把下面的 SQL 查询改写为 KQL 并解释差异。"
- 例 3："[优化] 请提供索引/聚合建议以优化此 KQL 查询的性能。"
- 例 4："[抽样] 请返回表的代表性样本并描述采样方法。"
- 例 5："[可视化] 请给出生成时间序列图的建议聚合粒度。"

### 2. Schema 探索与自动修正

- 用户故事：作为工程师，我需要自动发现表结构并用正确字段替换时间列或外键字段。
- 例 1："[发现] 列出数据库中所有表与主时间列。"
- 例 2："[替换] 在查询失败时自动检测时间字段并重写查询。"
- 例 3："[字段映射] 请生成字段到含义的映射文档以供业务使用。"
- 例 4："[采样] 提供字段值的频率分布样例以指导索引选择。"
- 例 5："[类型转换] 当列类型不匹配时，建议安全的转换函数并示例化。"

### 3. 生产级查询与测量

- 用户故事：作为 SRE，我要在严格的时间窗口内运行生产查询并导出指标用于告警。
- 例 1："[稳定] 请写出一个在过去 10 分钟内、考虑摄取延迟的心跳计数查询示例。"
- 例 2："[报警] 请根据错误增长率设计告警规则并给出示例 KQL。"
- 例 3："[性能] 请建议查询缓存或重写策略以降低成本。"
- 例 4："[导出] 请示例化如何将大结果集导出为 CSV 并保存到工作区。"
- 例 5："[合规] 请给出在查询中屏蔽敏感字段的合规性建议。"

### 4. 教学与迁移支持

- 用户故事：作为数据工程主管，我需要把 SQL 团队培训成 KQL 专家并迁移常用报表。
- 例 1："[教学] 请把下面的 SQL 语句分解并用 KQL 重写，解释每一步。"
- 例 2："[迁移] 给出把常见 SQL 报表迁移到 KQL 的分阶段计划。"
- 例 3："[范例] 提供 5 个常见报表模板及其 KQL 版本。"
- 例 4："[评价] 为一组查询给出可维护性与成本评级。"
- 例 5："[练习] 生成练习题库并附上参考答案与解析。"

## 原始文件

- ../../../../chatmodes/kusto-assistant.chatmode.md
---
post_title: "kusto-assistant.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "kusto-assistant-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases","kusto","kql"]
ai_note: "Generated with AI assistance."
summary: "Kusto Assistant 用例：KQL 查询构造、性能优化与仪表板集成示例。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 提供 Kusto (Azure Data Explorer) 的查询构造、性能优化与仪表板集成用例。

## When

- 在进行日志分析、事件查询或构建监控仪表板时使用。

## Why

- 快速构建高效 KQL 查询并整合到监控/报告流程。

## How

- 提供示例查询、优化模式与结果可视化建议。

## Key points (英文+中文对照)

- Efficient KQL patterns（高效 KQL 模式）
- Ingestion & schema（摄取与模式）
- Time series analysis（时序分析）
- Dashboard integration（仪表板集成）
- Performance tuning（性能调优）

## 使用场景

### 1. 日志探索与异常检测

- 用户故事：作为 SRE，我要构造高效查询以查找异常事件。
- 例 1：示例 group by / summarize 模式。
- 例 2：使用 timechart 与 time series 函数的示例。
- 例 3：生成异常检测规则的查询模版。
- 例 4：示例查询优化建议（列裁剪/early filtering）。
- 例 5：定时任务与告警集成。

### 2. 仪表板与指标追踪

- 用户故事：作为监控工程师，我要把查询嵌入仪表板并保持低延迟。
- 例 1：为常用视图创建物化视图或 summary 表。
- 例 2：优化查询以适应实时仪表盘。
- 例 3：示例数据转换与聚合策略。
- 例 4：仪表板加载性能监控示例。
- 例 5：仪表板参数化示例。

### 3. 数据摄取与模式设计

- 用户故事：作为数据工程师，我要设计高效的摄取管道与架构模式。
- 例 1：示例映射原始日志到 Kusto schema。
- 例 2：摄取批次与实时摄取示例。
- 例 3：数据保留策略与分区建议。
- 例 4：CTA/ETL 处理示例。
- 例 5：摄取错误处理样例。

### 4. 性能调优与资源控制

- 用户故事：作为 DBA，我要识别慢查询并优化资源使用。
- 例 1：示例查询剖析与 rewrite 建议。
- 例 2：建议使用合适的数据类型与索引策略。
- 例 3：控制并发查询的建议。
- 例 4：示例成本估算与优化策略。
- 例 5：监控资源使用的查询样例。

### 5. 报告自动化与导出

- 用户故事：作为分析师，我要定期导出报告并共享给团队。
- 例 1：导出 CSV/JSON 的查询样例。
- 例 2：自动化报告生成与分发示例。
- 例 3：权限与数据脱敏建议。
- 例 4：历史对比与趋势分析示例。
- 例 5：合规性与审计日志导出示例。

## 原始文件

- [chatmodes/kusto-assistant.chatmode.md](../../../chatmodes/kusto-assistant.chatmode.md)
