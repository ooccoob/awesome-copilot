---
agent: 'agent'
description: 'Create an Architectural Decision Record (ADR) document for AI-optimized decision documentation.'
tools: ['changes', 'search/codebase', 'edit/editFiles', 'extensions', 'web/fetch', 'githubRepo', 'openSimpleBrowser', 'problems', 'runTasks', 'search', 'search/searchResults', 'runCommands/terminalLastCommand', 'runCommands/terminalSelection', 'testFailure', 'usages', 'vscodeAPI']
---
# 创建架构决策记录

使用针对 AI 消耗和人类可读性进行优化的结构化格式，为 `${input:DecisionTitle}` 创建 ADR 文档。

## 输入

- **上下文**：`${input:Context}`
- **决定**：`${input:Decision}`
- **替代方案**：`${input:Alternatives}`
- **利益相关者**：`${input:Stakeholders}`

## 输入验证
如果未提供任何所需的输入或无法从对话历史记录中确定任何所需的输入，请在继续生成 ADR 之前要求用户提供缺失的信息。

## 要求

- 使用精确、明确的语言
- 标题内容遵循标准化 ADR 格式
- 包括积极和消极的后果
- 记录替代方案并附上拒绝理由
- 机器解析和人类参考的结构
- 对多项目部分使用编码项目符号点（3-4 个字母代码 + 3 位数字）

ADR 必须使用命名约定保存在 `/docs/adr/` 目录中：`adr-NNNN-[title-slug].md`，其中 NNNN 是下一个连续的 4 位数字（例如 `adr-0001-database-selection.md`）。

## 所需的文档结构

文档文件必须遵循以下模板，确保所有部分均正确填写。降价的正面内容应按照以下示例正确构建：

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
