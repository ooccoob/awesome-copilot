---
mode: 'agent'
description: '为面向对象组件创建符合行业最佳实践与架构文档标准的、全面且规范化的文档。'
tools: ['changes', 'codebase', 'editFiles', 'extensions', 'fetch', 'githubRepo', 'openSimpleBrowser', 'problems', 'runTasks', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI']
---
# 生成标准的 OO 组件文档

为路径 `${input:ComponentPath}` 下的面向对象组件创建完整文档。

分析给定路径中的代码：若提供的是文件夹，则分析其中所有源码；若是单个文件，则将其视为主要组件，并分析同目录下相关文件。

## 文档标准

- DOC-001：遵循 C4 模型文档层级（Context、Containers、Components、Code）
- DOC-002：对齐 Arc42 软件架构文档模板
- DOC-003：符合 IEEE 1016 软件设计说明标准
- DOC-004：采用敏捷文档原则（提供“恰到好处”的有价值文档）
- DOC-005：以开发者与维护者为主要受众

## 分析说明

- ANA-001：判定路径类型（文件夹 vs 单文件），识别主组件
- ANA-002：检查源码文件中的类结构与继承关系
- ANA-003：识别设计模式与架构决策
- ANA-004：记录公共 API、接口与依赖
- ANA-005：识别创建型/结构型/行为型模式
- ANA-006：记录方法参数、返回值与异常
- ANA-007：评估性能、安全性、可靠性、可维护性
- ANA-008：推断集成模式与数据流

## 语言特定优化

- LNG-001：C#/.NET——async/await、依赖注入、配置、释放
- LNG-002：Java——Spring 框架、注解、异常处理、打包
- LNG-003：TypeScript/JavaScript——模块化、异步模式、类型、npm
- LNG-004：Python——包管理、虚拟环境、类型提示、测试

## 错误处理

- ERR-001：路径不存在——提供正确格式指引
- ERR-002：未发现源码文件——建议替代位置
- ERR-003：结构不清晰——记录发现并指出需澄清处
- ERR-004：非标准模式——记录自定义做法
- ERR-005：代码不足——聚焦可得信息并标出缺口

## 输出格式

生成结构良好的 Markdown，包含清晰的标题层级、代码块、表格与要点列表，便于阅读与维护。

## 文件位置

文档应保存在 `/docs/components/` 目录下，命名遵循约定：`[component-name]-documentation.md`。

## 必需的文档结构

文档文件必须遵循下列模板，确保各部分均被恰当填充。Markdown 的 front matter 参考示例如下：

```md
---
title: [Component Name] - Technical Documentation
component_path: `${input:ComponentPath}`
version: [Optional: e.g., 1.0, Date]
date_created: [YYYY-MM-DD]
last_updated: [Optional: YYYY-MM-DD]
owner: [Optional: Team/Individual responsible for this component]
tags: [Optional: List of relevant tags or categories, e.g., `component`,`service`,`tool`,`infrastructure`,`documentation`,`architecture` etc]
---

# [Component Name] Documentation

[A short concise introduction to the component and its purpose within the system.]

## 1. Component Overview

### Purpose/Responsibility
- OVR-001: State component's primary responsibility
- OVR-002: Define scope (included/excluded functionality)
- OVR-003: Describe system context and relationships

## 2. Architecture Section

- ARC-001: Document design patterns used (Repository, Factory, Observer, etc.)
- ARC-002: List internal and external dependencies with purposes
- ARC-003: Document component interactions and relationships
- ARC-004: Include visual diagrams (UML class, sequence, component)
- ARC-005: Create mermaid diagram showing component structure, relationships, and dependencies

### Component Structure and Dependencies Diagram

Include a comprehensive mermaid diagram that shows:
- **Component structure** - Main classes, interfaces, and their relationships
- **Internal dependencies** - How components interact within the system
- **External dependencies** - External libraries, services, databases, APIs
- **Data flow** - Direction of dependencies and interactions
- **Inheritance/composition** - Class hierarchies and composition relationships

```mermaid
graph TD
    subgraph "Component System"
        A[Main Component] --> B[Internal Service]
        A --> C[Internal Repository]
        B --> D[Business Logic]
        C --> E[Data Access Layer]
    end

    subgraph "External Dependencies"
        F[External API]
        G[Database]
        H[Third-party Library]
        I[Configuration Service]
    end

    A --> F
    E --> G
    B --> H
    A --> I

    classDiagram
        class MainComponent {
            +property: Type
            +method(): ReturnType
            +asyncMethod(): Promise~Type~
        }
        class InternalService {
            +businessOperation(): Result
        }
        class ExternalAPI {
            <<external>>
            +apiCall(): Data
        }

        MainComponent --> InternalService
        MainComponent --> ExternalAPI
```

## 3. Interface Documentation

- INT-001: Document all public interfaces and usage patterns
- INT-002: Create method/property reference table
- INT-003: Document events/callbacks/notification mechanisms

| Method/Property | Purpose | Parameters | Return Type | Usage Notes |
|-----------------|---------|------------|-------------|-------------|
| [Name] | [Purpose] | [Parameters] | [Type] | [Notes] |

## 4. Implementation Details

- IMP-001：记录主要实现类与职责
- IMP-002：描述配置需求与初始化
- IMP-003：记录关键算法与业务逻辑
- IMP-004：标注性能特征与潜在瓶颈

## 5. Usage Examples

### Basic Usage

```csharp
// Basic usage example
var component = new ComponentName();
component.DoSomething();
```

### Advanced Usage

```csharp
// Advanced configuration patterns
var options = new ComponentOptions();
var component = ComponentFactory.Create(options);
await component.ProcessAsync(data);
```

- USE-001：提供基础用法示例
- USE-002：展示高级配置模式
- USE-003：记录最佳实践与推荐模式

## 6. Quality Attributes

- QUA-001：安全（认证、授权、数据保护）
- QUA-002：性能（特性、可扩展性、资源占用）
- QUA-003：可靠性（错误处理、容错、恢复）
- QUA-004：可维护性（规范、测试、文档）
- QUA-005：可扩展性（扩展点与定制能力）

## 7. Reference Information

- REF-001：依赖清单（含版本与用途）
- REF-002：完整的配置项参考
- REF-003：测试指南与 Mock 搭建
- REF-004：故障排查（常见问题与错误信息）
- REF-005：相关文档链接
- REF-006：变更历史与迁移说明

```
