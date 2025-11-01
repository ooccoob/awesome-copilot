---
mode: 'agent'
description: '为研究关键开发决策创建有时间限制的技术探索文档，在实施之前解决关键问题。'
tools: ['runCommands', 'runTasks', 'edit', 'search', 'extensions', 'usages', 'vscodeAPI', 'think', 'problems', 'changes', 'testFailure', 'openSimpleBrowser', 'fetch', 'githubRepo', 'todos', 'Microsoft Docs', 'search']
---

# 创建技术探索文档

为研究关键问题创建有时间限制的技术探索文档，这些问题必须在开发开始之前得到解答。每个探索都专注于一个特定的技术决策，具有明确的交付成果和时间表。

## 文档结构

在 `${input:FolderPath|docs/spikes}` 目录中创建单独的文件。使用模式命名每个文件：`[category]-[short-description]-spike.md`（例如 `api-copilot-integration-spike.md`、`performance-realtime-audio-spike.md`）。

```md
---
title: "${input:SpikeTitle}"
category: "${input:Category|Technical}"
status: "🔴 未开始"
priority: "${input:Priority|High}"
timebox: "${input:Timebox|1 week}"
created: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
owner: "${input:Owner}"
tags: ["technical-spike", "${input:Category|technical}", "research"]
---

# ${input:SpikeTitle}

## 摘要

**探索目标：** [需要解决的清晰、具体的问题或决策]

**重要性：** [对开发/架构决策的影响]

**时间限制：** [分配给此探索的时间]

**决策截止日期：** [为避免阻塞开发必须解决此问题的时间]

## 研究问题

**主要问题：** [需要回答的主要技术问题]

**次要问题：**

- [相关问题1]
- [相关问题2]
- [相关问题3]

## 调查计划

### 研究任务

- [ ] [具体研究任务1]
- [ ] [具体研究任务2]
- [ ] [具体研究任务3]
- [ ] [创建概念验证/原型]
- [ ] [记录发现和建议]

### 成功标准

**此探索完成时：**

- [ ] [具体标准1]
- [ ] [具体标准2]
- [ ] [记录明确的建议]
- [ ] [完成概念验证（如适用）]

## 技术背景

**相关组件：** [受此决策影响的系统组件列表]

**依赖关系：** [哪些其他探索或决策依赖于解决此问题]

**约束条件：** [影响解决方案的已知限制或要求]

## 研究发现

### 调查结果

[记录研究发现、测试结果和收集的证据]

### 原型/测试笔记

[来自任何原型、探索或技术实验的结果]

### 外部资源

- [相关文档链接]
- [API参考链接]
- [社区讨论链接]
- [示例/教程链接]

## 决策

### 建议

[基于研究结果提出明确建议]

### 理由

[为什么选择这种方法而不是其他方法]

### 实施说明

[实施的关键考虑因素]

### 后续行动

- [ ] [行动项1]
- [ ] [行动项2]
- [ ] [更新架构文档]
- [ ] [创建实施任务]

## 状态历史

| 日期   | 状态         | 说明                      |
| ------ | -------------- | -------------------------- |
| [日期] | 🔴 未开始 | 创建并确定探索范围        |
| [日期] | 🟡 进行中 | 开始研究                  |
| [日期] | 🟢 完成    | [解决摘要]                |

---

_最后更新：[日期] 由[姓名]_
```

## 技术探索类别

### API集成

- 第三方API功能和限制
- 集成模式和身份验证
- 速率限制和性能特征

### 架构与设计

- 系统架构决策
- 设计模式适用性
- 组件交互模型

### 性能与可扩展性

- 性能要求和约束
- 可扩展性瓶颈和解决方案
- 资源利用模式

### 平台与基础设施

- 平台功能和限制
- 基础设施要求
- 部署和托管考虑

### 安全与合规

- 安全要求和实施
- 合规约束
- 身份验证和授权方法

### 用户体验

- 用户交互模式
- 可访问性要求
- 界面设计决策

## 文件命名约定

使用描述性的kebab-case名称，指明类别和具体未知问题：

**API/集成示例：**

- `api-copilot-chat-integration-spike.md`
- `api-azure-speech-realtime-spike.md`
- `api-vscode-extension-capabilities-spike.md`

**性能示例：**

- `performance-audio-processing-latency-spike.md`
- `performance-extension-host-limitations-spike.md`
- `performance-webrtc-reliability-spike.md`

**架构示例：**

- `architecture-voice-pipeline-design-spike.md`
- `architecture-state-management-spike.md`
- `architecture-error-handling-strategy-spike.md`

## AI智能体最佳实践

1. **每个探索一个问题：** 每个文档专注于单一技术决策或研究问题

2. **有时间限制的研究：** 为每个探索定义具体的时间限制和交付成果

3. **基于证据的决策：** 在标记完成之前需要具体证据（测试、原型、文档）

4. **明确的建议：** 记录具体的建议和实施理由

5. **依赖关系跟踪：** 识别探索如何相互关联并影响项目决策

6. **结果导向：** 每个探索必须产生可操作的决策或建议

## 研究策略

### 阶段1：信息收集

1. **使用search/fetch工具搜索现有文档**
2. **分析代码库**以查找现有模式和约束
3. **研究外部资源**（API、库、示例）

### 阶段2：验证与测试

1. **创建专注的原型**来测试特定假设
2. **运行有针对性的实验**来验证假设
3. **记录测试结果**并提供支持证据

### 阶段3：决策与文档

1. **综合研究结果**形成明确建议
2. **记录实施指导**供开发团队使用
3. **创建后续任务**用于实施

## 工具使用

- **search/searchResults：** 研究现有解决方案和文档
- **fetch/githubRepo：** 分析外部API、库和示例
- **codebase：** 理解现有系统约束和模式
- **runTasks：** 执行原型和验证测试
- **editFiles：** 更新研究进度和发现
- **vscodeAPI：** 测试VS Code扩展功能和限制

专注于有时间限制的研究，解决关键技术决策并解除开发阻塞。