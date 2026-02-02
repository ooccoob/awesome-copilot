---
agent: 'agent'
description: 'Create time-boxed technical spike documents for researching and resolving critical development decisions before implementation.'
tools: ['runCommands', 'runTasks', 'edit', 'search', 'extensions', 'usages', 'vscodeAPI', 'think', 'problems', 'changes', 'testFailure', 'openSimpleBrowser', 'web/fetch', 'githubRepo', 'todos', 'Microsoft Docs', 'search']
---

# 创建技术尖峰文档

创建有时限的技术峰值文档，用于研究在开发继续之前必须回答的关键问题。每个峰值都侧重于具有明确可交付成果和时间表的特定技术决策。

## 文件结构

在 `${input:FolderPath|docs/spikes}` 目录中创建单独的文件。使用以下模式命名每个文件：`[category]-[short-description]-spike.md`（例如，`api-copilot-integration-spike.md`、`performance-realtime-audio-spike.md`）。

```md
---
title: "${input:SpikeTitle}"
category: "${input:Category|Technical}"
status: "🔴 Not Started"
priority: "${input:Priority|High}"
timebox: "${input:Timebox|1 week}"
created: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
owner: "${input:Owner}"
tags: ["technical-spike", "${input:Category|technical}", "research"]
---

# ${input:SpikeTitle}

## Summary

**Spike Objective:** [Clear, specific question or decision that needs resolution]

**Why This Matters:** [Impact on development/architecture decisions]

**Timebox:** [How much time allocated to this spike]

**Decision Deadline:** [When this must be resolved to avoid blocking development]

## Research Question(s)

**Primary Question:** [Main technical question that needs answering]

**Secondary Questions:**

- [Related question 1]
- [Related question 2]
- [Related question 3]

## Investigation Plan

### Research Tasks

- [ ] [Specific research task 1]
- [ ] [Specific research task 2]
- [ ] [Specific research task 3]
- [ ] [Create proof of concept/prototype]
- [ ] [Document findings and recommendations]

### Success Criteria

**This spike is complete when:**

- [ ] [Specific criteria 1]
- [ ] [Specific criteria 2]
- [ ] [Clear recommendation documented]
- [ ] [Proof of concept completed (if applicable)]

## Technical Context

**Related Components:** [List system components affected by this decision]

**Dependencies:** [What other spikes or decisions depend on resolving this]

**Constraints:** [Known limitations or requirements that affect the solution]

## Research Findings

### Investigation Results

[Document research findings, test results, and evidence gathered]

### Prototype/Testing Notes

[Results from any prototypes, spikes, or technical experiments]

### External Resources

- [Link to relevant documentation]
- [Link to API references]
- [Link to community discussions]
- [Link to examples/tutorials]

## Decision

### Recommendation

[Clear recommendation based on research findings]

### Rationale

[Why this approach was chosen over alternatives]

### Implementation Notes

[Key considerations for implementation]

### Follow-up Actions

- [ ] [Action item 1]
- [ ] [Action item 2]
- [ ] [Update architecture documents]
- [ ] [Create implementation tasks]

## Status History

| Date   | Status         | Notes                      |
| ------ | -------------- | -------------------------- |
| [Date] | 🔴 Not Started | Spike created and scoped   |
| [Date] | 🟡 In Progress | Research commenced         |
| [Date] | 🟢 Complete    | [Resolution summary]       |

---

_Last updated: [Date] by [Name]_
```

## 技术尖峰类别

### API集成

- 第三方 API 功能和限制
- 集成模式和身份验证
- 速率限制和性能特征

### 建筑与设计

- 系统架构决策
- 设计模式适用性
- 组件交互模型

### 性能和可扩展性

- 性能要求和限制
- 可扩展性瓶颈及解决方案
- 资源利用模式

### 平台与基础设施

- 平台功能和限制
- 基础设施要求
- 部署和托管注意事项

### 安全与合规性

- 安全要求和实施
- 合规性限制
- 身份验证和授权方法

### 用户体验

- 用户交互模式
- 无障碍要求
- 界面设计决策

## 文件命名约定

使用描述性的、短横线大小写的名称来指示类别和特定的未知数：

**API/集成示例：**

- __代码0__
- __代码0__
- __代码0__

**性能示例：**

- __代码0__
- __代码0__
- __代码0__

**架构示例：**

- __代码0__
- __代码0__
- __代码0__

## AI 代理的最佳实践

1. **每个峰值一个问题：** 每个文档都重点关注一个技术决策或研究问题

2. **限时研究：** 为每个峰值定义具体的时间限制和可交付成果

3. **基于证据的决策：** 在标记为完整之前需要具体证据（测试、原型、文档）

4. **明确的建议：** 记录具体建议和实施理由

5. **依赖性跟踪：**确定峰值如何相互关联并影响项目决策

6. **以结果为中心：** 每次峰值都必须产生可行的决策或建议

## 研究策略

### 第一阶段：信息收集

1. **使用搜索/获取工具搜索现有文档**
2. **分析代码库**现有模式和约束
3. **研究外部资源**（API、库、示例）

### 第 2 阶段：验证和测试

1. **创建有针对性的原型**来测试特定假设
2. **运行有针对性的实验**以验证假设
3. **记录测试结果**以及支持证据

### 第 3 阶段：决策和记录

1. **综合调查结果**形成明确的建议
2. **开发团队的文档实施指南**
3. **创建后续任务**以供实施

## 工具使用

- **搜索/搜索结果：** 研究现有的解决方案和文档
- **fetch/githubRepo:** 分析外部 API、库和示例
- **代码库：**了解现有的系统约束和模式
- **runTasks：** 执行原型和验证测试
- **editFiles：**更新研究进展和发现
- **vscodeAPI：** 测试 VS Code 扩展功能和限制

专注于有时限的研究，以解决关键的技术决策并解锁开发进展。
