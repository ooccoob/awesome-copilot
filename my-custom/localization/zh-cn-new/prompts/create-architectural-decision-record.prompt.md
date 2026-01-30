---
mode: 'agent'
description: '为AI优化的决策文档创建架构决策记录（ADR）文档。'
tools: ['changes', 'codebase', 'edit/editFiles', 'extensions', 'fetch', 'githubRepo', 'openSimpleBrowser', 'problems', 'runTasks', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI']
---
# 创建架构决策记录

使用结构化格式为`${input:DecisionTitle}`创建一个ADR文档，该格式针对AI消费和人类可读性进行了优化。

## 输入

- **上下文**：`${input:Context}`
- **决策**：`${input:Decision}`
- **替代方案**：`${input:Alternatives}`
- **利益相关者**：`${input:Stakeholders}`

## 输入验证

如果任何必需的输入未提供或无法从对话历史中确定，请在继续ADR生成之前要求用户提供缺失的信息。

## 需求

- 使用精确、明确的语言
- 遵循带有前置元数据的标准化ADR格式
- 包括正面和负面后果
- 用拒绝理由记录替代方案
- 为机器解析和人类参考构建结构
- 对多项目部分使用编码的项目符号点（3-4个字母代码 + 3位数字）

ADR必须保存在`/docs/adr/`目录中，使用命名约定：`adr-NNNN-[title-slug].md`，其中NNNN是下一个顺序4位数字（例如，`adr-0001-database-selection.md`）。

## 必需的文档结构

文档文件必须遵循下面的模板，确保所有部分都适当填写。markdown的前置元数据应按照后面的示例正确结构化：

```md
---
title: "ADR-NNNN: [决策标题]"
status: "Proposed"
date: "YYYY-MM-DD"
authors: "[利益相关者姓名/角色]"
tags: ["architecture", "decision"]
supersedes: ""
superseded_by: ""
---

# ADR-NNNN: [决策标题]

## 状态

**Proposed** | Accepted | Rejected | Superseded | Deprecated

## 上下文

[问题陈述、技术约束、业务需求和需要此决策的环境因素。]

## 决策

[选择的解决方案及选择理由的清晰说明。]

## 后果

### 正面

- **POS-001**：[有益结果和优势]
- **POS-002**：[性能、可维护性、可扩展性改进]
- **POS-003**：[与架构原则的一致性]

### 负面

- **NEG-001**：[权衡、限制、缺点]
- **NEG-002**：引入的技术债务或复杂性]
- **NEG-003**：[风险和未来挑战]

## 考虑的替代方案

### [替代方案1名称]

- **ALT-001**：**描述**：[简要技术描述]
- **ALT-002**：**拒绝原因**：[为什么未选择此选项]

### [替代方案2名称]

- **ALT-003**：**描述**：[简要技术描述]
- **ALT-004**：**拒绝原因**：[为什么未选择此选项]

## 实施说明

- **IMP-001**：[关键实施考虑]
- **IMP-002**：[如适用的迁移或推广策略]
- **IMP-003**：[监控和成功标准]

## 参考

- **REF-001**：[相关ADR]
- **REF-002**：[外部文档]
- **REF-003**：[引用的标准或框架]
```