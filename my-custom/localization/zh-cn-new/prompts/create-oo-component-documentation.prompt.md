---
mode: 'agent'
description: '为面向对象组件创建全面的、标准化的文档，遵循行业最佳实践和架构文档标准。'
tools: ['changes', 'codebase', 'edit/editFiles', 'extensions', 'fetch', 'githubRepo', 'openSimpleBrowser', 'problems', 'runTasks', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI']
---
# 生成标准面向对象组件文档

为位于 `${input:ComponentPath}` 的面向对象组件创建全面文档。

通过检查提供路径中的代码来分析组件。如果是文件夹，分析所有源文件。如果是单个文件，将其视为主组件并分析同一目录中的相关文件。

## 文档标准

- DOC-001: 遵循C4模型文档级别（上下文、容器、组件、代码）
- DOC-002: 与Arc42软件架构文档模板保持一致
- DOC-003: 符合IEEE 1016软件设计描述标准
- DOC-004: 使用敏捷文档原则（足够增加价值的文档）
- DOC-005: 以开发人员和维护人员为主要受众

## 分析指令

- ANA-001: 确定路径类型（文件夹 vs 单个文件）并识别主组件
- ANA-002: 检查源代码文件的类结构和继承关系
- ANA-003: 识别设计模式和架构决策
- ANA-004: 记录公共API、接口和依赖项
- ANA-005: 识别创建型/结构型/行为型模式
- ANA-006: 记录方法参数、返回值、异常
- ANA-007: 评估性能、安全性、可靠性、可维护性
- ANA-008: 推断集成模式和数据流

## 特定语言优化

- LNG-001: **C#/.NET** - async/await、依赖注入、配置、释放
- LNG-002: **Java** - Spring框架、注解、异常处理、打包
- LNG-003: **TypeScript/JavaScript** - 模块、异步模式、类型、npm
- LNG-004: **Python** - 包、虚拟环境、类型提示、测试

## 错误处理

- ERR-001: 路径不存在 - 提供正确格式指导
- ERR-002: 未找到源文件 - 建议替代位置
- ERR-003: 结构不清晰 - 记录发现并请求澄清
- ERR-004: 非标准模式 - 记录自定义方法
- ERR-005: 代码不足 - 专注于可用信息，突出差距

## 输出格式

生成结构良好的Markdown，具有清晰的标题层次、代码块、表格、项目符号和适当的格式，以确保可读性和可维护性。

## 文件位置

文档应保存在 `/docs/components/` 目录中，并按照约定命名：`[component-name]-documentation.md`。

## 必需的文档结构

文档文件必须遵循以下模板，确保所有部分都得到适当填写。markdown的前置内容应根据以下示例正确构建：

```md
---
title: [组件名称] - 技术文档
component_path: `${input:ComponentPath}`
version: [可选：例如 1.0, 日期]
date_created: [YYYY-MM-DD]
last_updated: [可选：YYYY-MM-DD]
owner: [可选：负责此组件的团队/个人]
tags: [可选：相关标签或类别列表，例如 `component`,`service`,`tool`,`infrastructure`,`documentation`,`architecture` 等]
---

# [组件名称] 文档

[对组件及其在系统中目的的简明介绍。]

## 1. 组件概述

### 目的/职责
- OVR-001: 陈述组件的主要职责
- OVR-002: 定义范围（包含/排除的功能）
- OVR-003: 描述系统上下文和关系

## 2. 架构部分

- ARC-001: 记录使用的设计模式（Repository、Factory、Observer等）
- ARC-002: 列出内部和外部依赖项及其用途
- ARC-003: 记录组件交互和关系
- ARC-004: 包含可视化图表（UML类图、序列图、组件图）
- ARC-005: 创建显示组件结构、关系和依赖项的mermaid图

### 组件结构和依赖项图

包含一个全面的mermaid图，显示：
- **组件结构** - 主要类、接口及其关系
- **内部依赖项** - 系统内组件如何交互
- **外部依赖项** - 外部库、服务、数据库、API
- **数据流** - 依赖项和交互的方向
- **继承/组合** - 类层次结构和组合关系

```mermaid
graph TD
    subgraph "组件系统"
        A[主组件] --> B[内部服务]
        A --> C[内部仓储]
        B --> D[业务逻辑]
        C --> E[数据访问层]
    end

    subgraph "外部依赖项"
        F[外部API]
        G[数据库]
        H[第三方库]
        I[配置服务]
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

## 3. 接口文档

- INT-001: 记录所有公共接口和使用模式
- INT-002: 创建方法/属性引用表
- INT-003: 记录事件/回调/通知机制

| 方法/属性 | 目的 | 参数 | 返回类型 | 使用说明 |
|-----------|------|------|----------|----------|
| [名称] | [目的] | [参数] | [类型] | [说明] |

## 4. 实现细节

- IMP-001: 记录主要实现类和职责
- IMP-002: 描述配置要求和初始化
- IMP-003: 记录关键算法和业务逻辑
- IMP-004: 注意性能特征和瓶颈

## 5. 使用示例

### 基本使用

```csharp
// 基本使用示例
var component = new ComponentName();
component.DoSomething();
```

### 高级使用

```csharp
// 高级配置模式
var options = new ComponentOptions();
var component = ComponentFactory.Create(options);
await component.ProcessAsync(data);
```

- USE-001: 提供基本使用示例
- USE-002: 显示高级配置模式
- USE-003: 记录最佳实践和推荐模式

## 6. 质量属性

- QUA-001: 安全性（身份验证、授权、数据保护）
- QUA-002: 性能（特征、可扩展性、资源使用）
- QUA-003: 可靠性（错误处理、容错、恢复）
- QUA-004: 可维护性（标准、测试、文档）
- QUA-005: 可扩展性（扩展点、自定义选项）

## 7. 参考信息

- REF-001: 列出依赖项及其版本和用途
- REF-002: 完整的配置选项参考
- REF-003: 测试指南和模拟设置
- REF-004: 故障排除（常见问题、错误消息）
- REF-005: 相关文档链接
- REF-006: 更改历史和迁移说明

```