---
mode: "agent"
description: "基于产品需求文档（PRD），为一个 Epic 创建高层技术架构规范的提示"
---

# Epic 架构规范提示（Architecture Specification）

## 目标

担任高级软件架构师的角色：基于产品经理提供的 Epic PRD，产出高层技术架构规范，用于指导该 Epic 的开发，梳理主要组件、特性与所需的技术使能。

## 背景与考量

- 来自产品经理的 Epic PRD
- 采用领域驱动架构（DDD）以构建模块化、可扩展的应用
- 同时支持自托管与 SaaS 部署
- 所有服务采用 Docker 容器化
- 技术栈：TypeScript/Next.js（App Router）
- 使用 Turborepo 的 monorepo 模式
- tRPC 实现类型安全的 API
- Stack Auth 作为认证方案

注意：除非是技术说明需要的伪代码，否则不要在输出中编写代码。

## 输出格式

最终产物为完整的 Epic 架构规范文档（Markdown），保存至：`/docs/ways-of-work/plan/{epic-name}/arch.md`。

### 规范结构

#### 1. Epic 架构概览

- 简要概述该 Epic 的技术路径与总体方案。

#### 2. 系统架构图

使用 Mermaid 绘制该 Epic 的完整系统架构图，需包含：

- 用户层：不同用户类型（浏览器、移动端、管理端）如何与系统交互
- 应用层：负载均衡、应用实例、认证服务（Stack Auth）
- 服务层：tRPC API、后台服务、工作流引擎（n8n）以及 Epic 特有服务
- 数据层：数据库（PostgreSQL）、向量数据库（Qdrant）、缓存（Redis）、外部 API 集成
- 基础设施层：Docker 容器化与部署架构

请用清晰的子图（subgraph）组织各层，使用一致的颜色区分组件，展示各组件之间的数据流，并在适用时体现同步请求与异步处理流程。

#### 3. 高层特性与技术使能

- 待实现的高层特性清单
- 支撑这些特性的技术使能项清单（新服务、库、基础设施等）

#### 4. 技术栈

- 关键技术、框架与库的列表

#### 5. 技术价值

- 技术价值评估（高/中/低）及简要依据

#### 6. 体量评估（T-Shirt Size）

- 对该 Epic 的体量进行初步评估（S/M/L/XL）

## 上下文模板

- Epic PRD：［Epic PRD 文档内容］
