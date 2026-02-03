---
agent: 'agent'
description: 'Update existing object-oriented component documentation following industry best practices and architectural documentation standards.'
tools: ['changes', 'search/codebase', 'edit/editFiles', 'extensions', 'web/fetch', 'githubRepo', 'openSimpleBrowser', 'problems', 'runTasks', 'search', 'search/searchResults', 'runCommands/terminalLastCommand', 'runCommands/terminalSelection', 'testFailure', 'usages', 'vscodeAPI']
---
# 更新标准 OO 组件文档

通过分析相应的组件代码来更新位于 `${file}` 的现有文档文件。

从现有文档的前面内容（`component_path` 字段）中提取组件路径或从文档内容中推断它。分析当前组件的实现并相应地更新文档。

**文件标准：**

- DOC-001：遵循 C4 模型文档级别（上下文、容器、组件、代码）
- DOC-002：与 Arc42 软件架构文档模板保持一致
- DOC-003：符合 IEEE 1016 软件设计描述标准
- DOC-004：使用敏捷文档原则（足够的文档来增加价值）
- DOC-005：将开发人员和维护人员作为主要受众

**分析说明：**

- ANA-001：阅读现有文档以了解组件上下文和结构
- ANA-002：从头条内容或内容分析中识别组件路径
- ANA-003：检查当前源代码文件的类结构和继承
- ANA-004：将现有文档与当前实施进行比较
- ANA-005：识别设计模式和架构变更
- ANA-006：更新公共 API、接口和依赖项
- ANA-007：识别新的/改变的创造/结构/行为模式
- ANA-008：更新方法参数、返回值、异常
- ANA-009：重新评估性能、安全性、可靠性、可维护性
- ANA-010：更新集成模式和数据流

**特定于语言的优化：**

- LNG-001：**C#/.NET** - 异步/等待、依赖项注入、配置、处置
- LNG-002：**Java** - Spring 框架、注释、异常处理、打包
- LNG-003：**TypeScript/JavaScript** - 模块、异步模式、类型、npm
- LNG-004：**Python** - 包、虚拟环境、类型提示、测试

**更新策略：**

- UPD-001：保留现有文档结构和格式
- UPD-002：将 `last_updated` 字段更新为当前日期
- UPD-003：维护前面的版本历史记录（如果存在）
- UPD-004：如果组件已显着扩展，则添加新部分
- UPD-005：标记已弃用的功能或重大更改
- UPD-006：更新示例以反映当前 API
- UPD-007：刷新依赖项列表和版本
- UPD-008：更新美人鱼图以反映当前架构

**错误处理：**

- ERR-001：文档文件不存在 - 提供有关文件位置的指导
- ERR-002：在文档中找不到组件路径 - 请求澄清
- ERR-003：源代码已移动 - 建议更新路径
- ERR-004：主要架构更改 - 突出显示重大更改
- ERR-005：对源文件的访问权限不足 - 文档限制

**输出格式：**

更新现有 Markdown 文件，保持其结构，同时刷新内容以匹配当前实现。保留格式、标题层次结构和现有的组织决策。

**所需的文档结构：**

按照相同的模板结构更新现有文档，确保所有部分都反映当前的实现：

```md
---
title: [Component Name] - Technical Documentation
component_path: [Current component path]
version: [Updated version if applicable]
date_created: [Original creation date - preserve]
last_updated: [YYYY-MM-DD - update to current date]
owner: [Preserve existing or update if changed]
tags: [Update tags as needed based on current functionality]
---

# [Component Name] Documentation

[Update introduction to reflect current component purpose and capabilities]

## 1. Component Overview

### Purpose/Responsibility
- OVR-001: Update component's primary responsibility
- OVR-002: Refresh scope (included/excluded functionality)
- OVR-003: Update system context and relationships

## 2. Architecture Section

- ARC-001: Update design patterns used (Repository, Factory, Observer, etc.)
- ARC-002: Refresh internal and external dependencies with current purposes
- ARC-003: Update component interactions and relationships
- ARC-004: Update visual diagrams (UML class, sequence, component)
- ARC-005: Refresh mermaid diagram showing current component structure, relationships, and dependencies

### Component Structure and Dependencies Diagram

Update the mermaid diagram to show current:
- **Component structure** - Current classes, interfaces, and their relationships
- **Internal dependencies** - How components currently interact within the system
- **External dependencies** - Current external libraries, services, databases, APIs
- **Data flow** - Current direction of dependencies and interactions
- **Inheritance/composition** - Current class hierarchies and composition relationships

```mermaid
[更新图表以反映当前架构]
```

## 3. Interface Documentation

- INT-001: Update all public interfaces and current usage patterns
- INT-002: Refresh method/property reference table with current API
- INT-003: Update events/callbacks/notification mechanisms

| Method/Property | Purpose | Parameters | Return Type | Usage Notes |
|-----------------|---------|------------|-------------|-------------|
| [Update table with current API] | | | | |

## 4. Implementation Details

- IMP-001: Update main implementation classes and current responsibilities
- IMP-002: Refresh configuration requirements and initialization patterns
- IMP-003: Update key algorithms and business logic
- IMP-004: Update performance characteristics and bottlenecks

## 5. Usage Examples

### Basic Usage

```csharp
// 将基本使用示例更新为当前 API
```

### Advanced Usage

```csharp
// 将高级配置模式更新为当前实现
```

- USE-001: Update basic usage examples
- USE-002: Refresh advanced configuration patterns
- USE-003: Update best practices and recommended patterns

## 6. Quality Attributes

- QUA-001: Update security (authentication, authorization, data protection)
- QUA-002: Refresh performance (characteristics, scalability, resource usage)
- QUA-003: Update reliability (error handling, fault tolerance, recovery)
- QUA-004: Refresh maintainability (standards, testing, documentation)
- QUA-005: Update extensibility (extension points, customization options)

## 7. Reference Information

- REF-001: Update dependencies with current versions and purposes
- REF-002: Refresh configuration options reference
- REF-003: Update testing guidelines and mock setup
- REF-004: Refresh troubleshooting (common issues, error messages)
- REF-005: Update related documentation links
- REF-006: Add change history and migration notes for this update

```
