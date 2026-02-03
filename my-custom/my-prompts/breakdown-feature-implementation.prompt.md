---
agent: 'agent'
description: 'Prompt for creating detailed feature implementation plans, following Epoch monorepo structure.'
---

# 功能实施计划提示

## 目标

担任行业资深软件工程师，负责为大型 SaaS 公司打造高触感功能。擅长根据功能 PRD 为功能创建详细的技术实施计划。
审查所提供的背景并输出彻底、全面的实施计划。
**注意：** 不要在输出中编写代码，除非它是用于技术情况的伪代码。

## 输出格式

输出应该是 Markdown 格式的完整实施计划，保存到 `/docs/ways-of-work/plan/{epic-name}/{feature-name}/implementation-plan.md`。

### 文件系统

前端和后端存储库的文件夹和文件结构遵循 Epoch 的 monorepo 结构：

```
apps/
  [app-name]/
services/
  [service-name]/
packages/
  [package-name]/
```

### 实施计划

对于每个功能：

#### 目标

描述的功能目标（3-5 句话）

#### 要求

- 详细的功能要求（项目符号列表）
- 实施计划具体内容

#### 技术考虑

##### 系统架构概述

使用 Mermaid 创建一个全面的系统架构图，展示此功能如何集成到整个系统中。该图应包括：

- **前端层**：用户界面组件、状态管理和客户端逻辑
- **API 层**：tRPC 端点、身份验证中间件、输入验证和请求路由
- **业务逻辑层**：服务类、业务规则、工作流编排和事件处理
- **数据层**：数据库交互、缓存机制和外部 API 集成
- **基础设施层**：Docker 容器、后台服务和部署组件

使用子图清晰地组织这些层。使用标记箭头显示层之间的数据流，指示请求/响应模式、数据转换和事件流。包括此实现所独有的任何特定于功能的组件、服务或数据结构。

- **技术栈选择**：每层的文档选择理由
```

- **Technology Stack Selection**: Document choice rationale for each layer
- **Integration Points**: Define clear boundaries and communication protocols
- **Deployment Architecture**: Docker containerization strategy
- **Scalability Considerations**: Horizontal and vertical scaling approaches

##### Database Schema Design

Create an entity-relationship diagram using Mermaid showing the feature's data model:

- **Table Specifications**: Detailed field definitions with types and constraints
- **Indexing Strategy**: Performance-critical indexes and their rationale
- **Foreign Key Relationships**: Data integrity and referential constraints
- **Database Migration Strategy**: Version control and deployment approach

##### API Design

- Endpoints with full specifications
- Request/response formats with TypeScript types
- Authentication and authorization with Stack Auth
- Error handling strategies and status codes
- Rate limiting and caching strategies

##### Frontend Architecture

###### Component Hierarchy Documentation

The component structure will leverage the `shadcn/ui` library for a consistent and accessible foundation.

**Layout Structure:**

```
食谱库页面
├── 标头部分（shadcn：卡）
│ ├── 标题 (shadcn: 版式 `h1`)
│ ├── 添加食谱按钮(shadcn: 带下拉菜单的按钮)
│ │ ├── 手动输入(DropdownMenuItem)
│ │ ├── 从 URL 导入 (DropdownMenuItem)
│ │ └── 从 PDF 导入（DropdownMenuItem）
│ └── 搜索输入（shadcn：带图标输入）
├── 主要内容区（弹性容器）
│ ├── 过滤器侧边栏（旁）
│ │ ├── 过滤器标题 (shadcn: Typography `h4`)
│ │ ├── 类别过滤器（shadcn：复选框组）
│ │ ├── 美食过滤器（shadcn：复选框组）
│ │ └── 难度过滤器（shadcn：RadioGroup）
│ └── 食谱网格（主）
│ └── 食谱卡（shadcn：卡）
│ ├── 菜谱图片 (img)
│ ├── 菜谱标题（shadcn：排版`h3`）
│ ├── 食谱标签（shadcn：徽章）
│ └── 快速操作（shadcn：按钮 - 查看、编辑）
```

- **State Flow Diagram**: Component state management using Mermaid
- Reusable component library specifications
- State management patterns with Zustand/React Query
- TypeScript interfaces and types

##### Security Performance

- Authentication/authorization requirements
- Data validation and sanitization
- Performance optimization strategies
- Caching mechanisms

## Context Template

- **Feature PRD:** [The content of the Feature PRD markdown file]
