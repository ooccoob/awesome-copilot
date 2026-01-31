---
代理人：“代理人”
描述：“遵循行业最佳实践和架构文档标准，为面向对象的组件创建全面、标准化的文档。”
工具：['更改'、'搜索/代码库'、'编辑/编辑文件'、'扩展'、'web/fetch'、'githubRepo'、'openSimpleBrowser'、'问题'、'runTasks'、'搜索'、'搜索/searchResults'、'runCommands/terminalLastCommand'、'runCommands/terminalSelection'、'testFailure'、 '用法'，'vscodeAPI']
---
# 生成标准 OO 组件文档

为面向对象的组件创建全面的文档：`${input:ComponentPath}`。

通过检查提供的路径中的代码来分析组件。如果是文件夹，则分析所有源文件。如果是单个文件，则视为主要组件并分析同一目录中的相关文件。

## 文件标准

- DOC-001：遵循 C4 模型文档级别（上下文、容器、组件、代码）
- DOC-002：与 Arc42 软件架构文档模板保持一致
- DOC-003：符合 IEEE 1016 软件设计描述标准
- DOC-004：使用敏捷文档原则（足够的文档来增加价值）
- DOC-005：将开发人员和维护人员作为主要受众

## 分析说明

- ANA-001：确定路径类型（文件夹与单个文件）并识别主要组件
- ANA-002：检查源代码文件的类结构和继承
- ANA-003：识别设计模式和架构决策
- ANA-004：记录公共 API、接口和依赖项
- ANA-005：识别创造/结构/行为模式
- ANA-006：记录方法参数、返回值、异常
- ANA-007：评估性能、安全性、可靠性、可维护性
- ANA-008：推断集成模式和数据流

## 特定于语言的优化

- LNG-001：**C#/.NET** - 异步/等待、依赖项注入、配置、处置
- LNG-002：**Java** - Spring 框架、注释、异常处理、打包
- LNG-003：**TypeScript/JavaScript** - 模块、异步模式、类型、npm
- LNG-004：**Python** - 包、虚拟环境、类型提示、测试

## 错误处理

- ERR-001：路径不存在 - 提供正确的格式指导
- ERR-002：未找到源文件 - 建议替代位置
- ERR-003：结构不清晰 - 记录调查结果并请求澄清
- ERR-004：非标准模式 - 记录自定义方法
- ERR-005：代码不足 - 关注可用信息，突出显示差距

## 输出格式

生成结构良好的 Markdown，具有清晰的标题层次结构、代码块、表格、项目符号点以及适当的格式，以提高可读性和可维护性。

## 文件位置

文档应保存在 `/docs/components/` 目录中，并按照约定命名：`[component-name]-documentation.md`。

## 所需的文档结构

文档文件必须遵循以下模板，确保所有部分均正确填写。降价的正面内容应按照以下示例正确构建：

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
图解TD
    子图“组件系统”
        A[主要组件] --> B[内部服务]
        A --> C[内部存储库]
        B --> D[业务逻辑]
C --> E[数据访问层]
    结束

    子图“外部依赖关系”
        F[外部API]
        G[数据库]
        H[第三方库]
        一、【配置服务】
    结束

    一个-->F
    E-->G
    B --> H
    一个-->我

    类图
        类主组件{
            +属性：类型
            +method(): 返回类型
            +asyncMethod(): Promise~类型~
        }
        类内部服务{
            +businessOperation()：结果
        }
        类外部API {
            <<外部>>
            +apiCall()：数据
        }

        主要组件 --> 内部服务
        主要组件 --> 外部API
```

## 3. Interface Documentation

- INT-001: Document all public interfaces and usage patterns
- INT-002: Create method/property reference table
- INT-003: Document events/callbacks/notification mechanisms

| Method/Property | Purpose | Parameters | Return Type | Usage Notes |
|-----------------|---------|------------|-------------|-------------|
| [Name] | [Purpose] | [Parameters] | [Type] | [Notes] |

## 4. Implementation Details

- IMP-001: Document main implementation classes and responsibilities
- IMP-002: Describe configuration requirements and initialization
- IMP-003: Document key algorithms and business logic
- IMP-004: Note performance characteristics and bottlenecks

## 5. Usage Examples

### Basic Usage

```csharp
// 基本使用示例
var 组件 = new 组件名称();
组件.DoSomething();
```

### Advanced Usage

```csharp
// 高级配置模式
var options = new ComponentOptions();
var 组件 = ComponentFactory.Create(选项);
等待组件.ProcessAsync(数据);
```

- USE-001: Provide basic usage examples
- USE-002: Show advanced configuration patterns
- USE-003: Document best practices and recommended patterns

## 6. Quality Attributes

- QUA-001: Security (authentication, authorization, data protection)
- QUA-002: Performance (characteristics, scalability, resource usage)
- QUA-003: Reliability (error handling, fault tolerance, recovery)
- QUA-004: Maintainability (standards, testing, documentation)
- QUA-005: Extensibility (extension points, customization options)

## 7. Reference Information

- REF-001: List dependencies with versions and purposes
- REF-002: Complete configuration options reference
- REF-003: Testing guidelines and mock setup
- REF-004: Troubleshooting (common issues, error messages)
- REF-005: Related documentation links
- REF-006: Change history and migration notes

```
