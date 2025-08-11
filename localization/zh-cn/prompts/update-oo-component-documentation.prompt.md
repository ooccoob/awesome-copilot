---
mode: 'agent'
description: '基于行业最佳实践与架构文档标准，更新现有面向对象组件文档。'
tools: ['changes', 'codebase', 'editFiles', 'extensions', 'fetch', 'githubRepo', 'openSimpleBrowser', 'problems', 'runTasks', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI']
---
# 更新标准 OO 组件文档

分析并更新位于 `${file}` 的现有组件文档。

从 front matter (`component_path`) 字段或内容中提取组件路径，分析当前实现并同步文档。

**文档标准：**
- DOC-001: 采用 C4 模型（Context / Containers / Components / Code）
- DOC-002: 对齐 Arc42 架构文档模板
- DOC-003: 符合 IEEE 1016 软件设计说明规范
- DOC-004: 遵循敏捷文档原则（只写有价值的部分）
- DOC-005: 目标读者为开发与维护人员

**分析指引：**
- ANA-001: 阅读现有文档理解上下文
- ANA-002: 获取组件路径
- ANA-003: 检查源码：类、接口、继承层次
- ANA-004: 对比文档与实现差异
- ANA-005: 识别设计模式与架构演进
- ANA-006: 更新公共 API、接口、依赖
- ANA-007: 标注新增/变更的模式
- ANA-008: 更新方法参数、返回值、异常
- ANA-009: 评估性能/安全/可靠/可维护性
- ANA-010: 更新集成模式与数据流

**语言特定优化：**
- LNG-001: C#/.NET — async/await、DI、配置、释放
- LNG-002: Java — Spring 注解、异常、包结构
- LNG-003: TS/JS — 模块化、异步模式、类型
- LNG-004: Python — 包、虚拟环境、类型提示、测试

**更新策略：**
- UPD-001: 保留结构与格式
- UPD-002: 更新 `last_updated`
- UPD-003: 保留版本历史（若有）
- UPD-004: 组件扩展显著时增加新节
- UPD-005: 标记弃用或破坏性变更
- UPD-006: 更新示例与当前 API 对齐
- UPD-007: 刷新依赖与版本
- UPD-008: 重绘 mermaid 图反映现状

**错误处理：**
- ERR-001: 文档不存在 → 提示路径
- ERR-002: 未找到组件路径 → 请求澄清
- ERR-003: 源码迁移 → 建议新路径
- ERR-004: 架构大改 → 高亮破坏性变更
- ERR-005: 访问不足 → 记录限制

**输出格式：**
保持既有 Markdown 结构与层级，仅同步内容与状态。

**必备结构模板：**
```md
---
title: [Component Name] - Technical Documentation
component_path: [Current component path]
version: [Updated version]
date_created: [Original date]
last_updated: [YYYY-MM-DD]
owner: [...]
tags: [...]
---

# [Component Name] Documentation
[简介]

## 1. Component Overview
### Purpose/Responsibility
- OVR-001: …

## 2. Architecture Section
- ARC-001: …

### Component Structure and Dependencies Diagram
```mermaid
[Diagram]
```

## 3. Interface Documentation
| Method/Property | Purpose | Parameters | Return Type | Usage Notes |
|-----------------|---------|------------|-------------|-------------|
| … | | | | |

## 4. Implementation Details
- IMP-001: …

## 5. Usage Examples
### Basic Usage
```csharp
// 示例
```
### Advanced Usage
```csharp
// 示例
```

## 6. Quality Attributes
- QUA-001: …

## 7. Reference Information
- REF-001: …
```

---
本地化文件。若发现翻译问题或需改进，请提交 Issue。
