---
mode: 'agent'
description: '用于创建详细功能实施计划的提示，遵循Epoch单一代码库结构。'
---

# 功能实施计划提示

## 目标

担任负责为大规模SaaS公司制作高接触功能的高级软件工程师。擅长根据功能PRD创建详细的实施计划。
审查提供的上下文并输出彻底、全面的实施计划。
**注意：** 输出中不要编写代码，除非它是技术情况的伪代码。

## 输出格式

输出应该是完整的实施计划，采用Markdown格式，保存到`/docs/ways-of-work/plan/{epic-name}/{feature-name}/implementation-plan.md`。

### 文件系统

遵循Epoch单一代码库结构的前端和后端代码库的文件夹和文件结构：

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

描述功能目标（3-5句话）

#### 需求

- 详细功能需求（项目符号列表）
- 实施计划细节

#### 技术考虑

##### 系统架构概览

使用Mermaid创建展示此功能如何集成到整体系统的综合系统架构图。该图应包括：

- **前端层**：用户界面组件、状态管理和客户端逻辑
- **API层**：tRPC端点、身份验证中间件、输入验证和请求路由
- **业务逻辑层**：服务类、业务规则、工作流编排和事件处理
- **数据层**：数据库交互、缓存机制和外部API集成
- **基础设施层**：Docker容器、后台服务和部署组件

使用子图清晰组织这些层。显示层间的数据流，使用标记的箭头指示请求/响应模式、数据转换和事件流。包含此实现独有的任何功能特定组件、服务或数据结构。

- **技术堆栈选择**：记录每层选择的理由
```

- **技术堆栈选择**：记录每层选择的理由
- **集成点**：定义清晰的边界和通信协议
- **部署架构**：Docker容器化策略
- **可扩展性考虑**：水平和垂直扩展方法

##### 数据库模式设计

使用Mermaid创建显示功能数据模型的实体关系图：

- **表规范**：带类型和约束的详细字段定义
- **索引策略**：性能关键索引及其理由
- **外键关系**：数据完整性和引用约束
- **数据库迁移策略**：版本控制和部署方法

##### API设计

- 带完整规范的端点
- 带TypeScript类型的请求/响应格式
- 使用Stack Auth的身份验证和授权
- 错误处理策略和状态代码
- 速率限制和缓存策略

##### 前端架构

###### 组件层次结构文档

组件结构将利用`shadcn/ui`库实现一致和可访问的基础。

**布局结构：**

```
食谱库页面
├── 标题部分 (shadcn: Card)
│   ├── 标题 (shadcn: Typography `h1`)
│   ├── 添加食谱按钮 (shadcn: Button with DropdownMenu)
│   │   ├── 手动输入 (DropdownMenuItem)
│   │   ├── 从URL导入 (DropdownMenuItem)
│   │   └── 从PDF导入 (DropdownMenuItem)
│   └── 搜索输入 (shadcn: Input with icon)
├── 主内容区域 (flex container)
│   ├── 筛选侧边栏 (aside)
│   │   ├── 筛选标题 (shadcn: Typography `h4`)
│   │   ├── 类别筛选器 (shadcn: Checkbox group)
│   │   ├── 菜系筛选器 (shadcn: Checkbox group)
│   │   └── 难度筛选器 (shadcn: RadioGroup)
│   └── 食谱网格 (main)
│       └── 食谱卡片 (shadcn: Card)
│           ├── 食谱图像 (img)
│           ├── 食谱标题 (shadcn: Typography `h3`)
│           ├── 食谱标签 (shadcn: Badge)
│           └── 快速操作 (shadcn: Button - 查看、编辑)
```

- **状态流图**：使用Mermaid的组件状态管理
- 可重用组件库规范
- 使用Zustand/React Query的状态管理模式
- TypeScript接口和类型

##### 安全性能

- 身份验证/授权需求
- 数据验证和清理
- 性能优化策略
- 缓存机制

## 上下文模板

- **功能PRD：** [功能PRD markdown文件的内容]