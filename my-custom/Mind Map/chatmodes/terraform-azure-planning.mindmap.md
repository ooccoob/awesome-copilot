## What / When / Why / How

- What: Azure Terraform 实施规划（写入 .terraform-planning-files/INFRA.{goal}.md）
- When: 在实现前形成机器可读、可追踪的实施计划
- Why: 以 WAF 与官方文档为依据，提升一致性
- How: 检索既有规格→分类项目类型→列资源清单→阶段化计划

## Key Points

- 只在 .terraform-planning-files/ 下写入
- 结构：frontmatter→WAF(成本/可靠/安全/性能/运维)→资源(YAML块)→分阶段计划
- 资源条目：AVM 或 Raw、变量/输出、依赖、Docs/AVM 引用
- 参考：microsoft-docs、AVM 最新版本、cloudarchitect 产物
- 输出：INFRA.{goal}.md，确定性语言，AI 可解析

## Compact Map

- 盘点规格→评价类型→WAF对齐→资源→阶段任务

## Example Questions (10+)

- 目标 goal 与范围界定？
- WAF 各维度的关键约束？
- 资源采用 AVM 还是 Raw？版本？
- 私有连接/网络与安全基线？
- 变量/输出设计与示例？
- 依赖顺序与跨阶段里程碑？
- 引用的官方文档链接？
- 成本/可靠性/性能取舍？
- 缺失规格如何补齐？
- 与现有 *.tf 的差异与迁移？

---
Source: d:\mycode\awesome-copilot\chatmodes\terraform-azure-planning.chatmode.md
Generated: {{timestamp}}
