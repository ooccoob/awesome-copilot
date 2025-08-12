---
mode: "agent"
description: "为 AI 优化的决策文档创建一份架构决策记录（ADR）。"
tools: ["changes", "codebase", "editFiles", "extensions", "fetch", "githubRepo", "openSimpleBrowser", "problems", "runTasks", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI"]
---

# 创建架构决策记录（ADR）

为 `${input:DecisionTitle}` 创建一份 ADR 文档，使用适合 AI 消费与人工阅读的结构化格式。

## 输入

- **上下文**: `${input:Context}`
- **决策**: `${input:Decision}`
- **备选方案**: `${input:Alternatives}`
- **干系人**: `${input:Stakeholders}`

## 输入校验

如缺少任何必填输入，且无法从对话历史中推断，请在生成 ADR 前先请求用户补充缺失信息。

## 要求

- 使用精确且无歧义的语言
- 遵循带有 front matter 的标准 ADR 模板
- 同时包含正面与负面影响
- 记录备选方案及其被拒原因
- 结构化，便于机器解析与人工查阅
- 多项列表使用编码型要点（3-4 字母代码 + 3 位编号）

ADR 必须保存在 `/docs/adr/` 目录，命名规则：`adr-NNNN-[title-slug].md`，其中 NNNN 为顺序 4 位编号（例：`adr-0001-database-selection.md`）。

## 必要的文档结构

文档必须遵循以下模板，确保所有章节被正确填写。Markdown 的 front matter 应按示例结构：

```md
---
title: "ADR-NNNN: [Decision Title]"
status: "Proposed"
date: "YYYY-MM-DD"
authors: "[Stakeholder Names/Roles]"
tags: ["architecture", "decision"]
supersedes: ""
superseded_by: ""
---

# ADR-NNNN: [Decision Title]

## Status

**Proposed** | Accepted | Rejected | Superseded | Deprecated

## Context

[Problem statement, technical constraints, business requirements, and environmental factors requiring this decision.]

## Decision

[Chosen solution with clear rationale for selection.]

## Consequences

### Positive

- **POS-001**: [Beneficial outcomes and advantages]
- **POS-002**: [Performance, maintainability, scalability improvements]
- **POS-003**: [Alignment with architectural principles]

### Negative

- **NEG-001**: [Trade-offs, limitations, drawbacks]
- **NEG-002**: [Technical debt or complexity introduced]
- **NEG-003**: [Risks and future challenges]

## Alternatives Considered

### [Alternative 1 Name]

- **ALT-001**: **Description**: [Brief technical description]
- **ALT-002**: **Rejection Reason**: [Why this option was not selected]

### [Alternative 2 Name]

- **ALT-003**: **Description**: [Brief technical description]
- **ALT-004**: **Rejection Reason**: [Why this option was not selected]

## Implementation Notes

- **IMP-001**: [Key implementation considerations]
- **IMP-002**: [Migration or rollout strategy if applicable]
- **IMP-003**: [Monitoring and success criteria]

## References

- **REF-001**: [Related ADRs]
- **REF-002**: [External documentation]
- **REF-003**: [Standards or frameworks referenced]
```
