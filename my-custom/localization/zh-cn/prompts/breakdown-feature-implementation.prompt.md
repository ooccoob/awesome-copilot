---
mode: "agent"
description: "用于按照 Epoch monorepo 结构编写详细的功能实现方案（Implementation Plan）的提示。"
---

# 功能实现方案（Feature Implementation Plan）提示

## 目标

以资深软件工程师身份，为大型 SaaS 的关键功能制定详尽的技术实现方案。基于 Feature PRD，审阅上下文并输出全面的实现计划。
注意：除非技术说明需要的伪代码，否则不要在输出中直接编写代码。

## 输出格式

输出为完整的实现方案（Markdown），保存路径：`/docs/ways-of-work/plan/{epic-name}/{feature-name}/implementation-plan.md`。

### 文件系统

前后端同时遵循 Epoch monorepo 结构：

```
apps/
  [app-name]/
services/
  [service-name]/
packages/
  [package-name]/
```

### 实现计划

针对每个功能：

#### 目标（Goal）

- 用 3–5 句描述功能目标。

#### 需求（Requirements）

- 详细功能需求（项目清单）
- 实现步骤与方案细化

#### 技术考量（Technical Considerations）

##### 系统架构概览

使用 Mermaid 绘制该功能在整体系统中的集成架构，至少包含：

- 前端层：UI 组件、状态管理、客户端逻辑
- API 层：tRPC 端点、认证中间件、输入验证、路由
- 业务逻辑层：服务类、业务规则、流程编排、事件处理
- 数据层：数据库交互、缓存机制、外部 API 集成
- 基础设施层：Docker、后台服务、部署组件

通过子图组织各层，使用带标签的箭头表达请求/响应、数据转换与事件流；纳入该功能特有组件与数据结构。

- 技术栈选型：为各层的选择给出依据
- 集成点：定义边界与通信协议
- 部署架构：容器化策略
- 可扩展性：横向/纵向扩展思路

##### 数据库模式设计

用 Mermaid 定义实体关系图（ERD）：

- 表定义：字段/类型/约束
- 索引策略：关键索引与原因
- 外键关系：完整性与约束
- 迁移策略：版本控制与上线方案

##### API 设计

- 端点清单与规范
- 请求/响应格式（TypeScript 类型）
- 认证与授权（Stack Auth）
- 错误处理与状态码
- 限流与缓存策略

##### 前端架构

组件层级（示例，基于 shadcn/ui）：

```
Recipe Library Page
├── Header Section (shadcn: Card)
│   ├── Title (shadcn: Typography `h1`)
│   ├── Add Recipe Button (DropdownMenu)
│   │   ├── Manual Entry
│   │   ├── Import from URL
│   │   └── Import from PDF
│   └── Search Input (with icon)
├── Main Content (flex)
│   ├── Filter Sidebar (aside)
│   │   ├── Category Filters (Checkbox group)
│   │   ├── Cuisine Filters (Checkbox group)
│   │   └── Difficulty Filters (RadioGroup)
│   └── Recipe Grid (main)
│       └── Recipe Card (Card)
│           ├── Image
│           ├── Title (Typography `h3`)
│           ├── Tags (Badge)
│           └── Quick Actions (Button: View/Edit)
```

- 状态流图（Mermaid）
- 复用组件规范
- 状态管理（Zustand/React Query）
- TypeScript 接口与类型

##### 安全与性能

- 认证/授权需求
- 数据校验与净化
- 性能优化策略
- 缓存机制

## 上下文模板

- Feature PRD：［功能 PRD 文档内容］
