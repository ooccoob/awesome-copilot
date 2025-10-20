---
post_title: 'folder-structure-blueprint-generator.prompt.md Use Cases'
author1: 'github-copilot'
post_slug: 'folder-structure-blueprint-generator-prompt-use-cases'
microsoft_alias: 'copilot'
featured_image: ''
categories: []
tags: ['use-cases', 'architecture', 'documentation', 'folder-structure', 'blueprint']
ai_note: 'Generated with AI assistance.'
summary: 'Use case scenarios for analyzing and documenting project folder structures, including visualizations, conventions, templates, and enforcement guidance.'
post_date: '2025-10-20'
---

<!-- markdownlint-disable MD041 -->

## What

* 利用“Project Folder Structure Blueprint Generator”提示词，自动检测项目类型，输出带可视化、命名规则、目录模板的结构蓝图文档。

## When

* 新接手代码库需快速理解目录组织时。
* 要统一团队交付的代码结构标准或审计现有项目时。
* 准备迁移/拆分/扩展大型仓库，需要现状蓝图作为基线时。

## Why

* 明确结构原则、命名约束与扩展模板，降低协作摩擦与认知负担。
* 用 Blueprint 记录演变历史，方便后续治理与培训。

## How

* 设置配置变量（项目类型、是否微服务、可视化风格、深度等）。
* 扫描关键文件自动推断技术栈、前后端/微服务/单仓状态。
* 生成结构概览、目录可视化、关键目录分析、命名与放置模式、扩展模板与治理策略。

## Key points (英文+中文对照)

* Auto-detect project types（自动识别项目类型）
* Provide visual hierarchy（输出可视化层级）
* Document file placement rules（记录文件放置规则）
* Include naming conventions（包含命名约定）
* Offer extension templates（提供扩展模板）

## 使用场景

### 1. 自动识别与现状盘点（Discovery & Detection）

* 用户故事：作为架构师，我要扫描仓库自动识别技术栈、微服务结构与前端模块，形成现状报告。
* 例1："/folder-structure-blueprint-generator `VISUALIZATION_STYLE=ASCII` `DEPTH_LEVEL=3` 请自动识别技术栈并生成结构蓝图。"
* 例2："/folder-structure-blueprint-generator [PROJECT_TYPE=Auto-detect] 输出检测到的 monorepo 与微服务证据。"
* 例3："/folder-structure-blueprint-generator [INCLUDES_FRONTEND=Auto-detect] 标注前端模块及其构建配置位置。"
* 例4："/folder-structure-blueprint-generator [INCLUDE_GENERATED_FOLDERS=false] 仅列出手写目录并说明排除项。"
* 例5："/folder-structure-blueprint-generator [INCLUDE_FILE_COUNTS=true] 统计各目录文件数量与复杂度集中区域。"

### 2. 结构可视化与导览（Visualization & Orientation）

* 用户故事：作为新加入的开发者，我需要一份可视化目录图与导航指南，快速定位切入点。
* 例1："/folder-structure-blueprint-generator `VISUALIZATION_STYLE=Markdown List` `DEPTH_LEVEL=4` 生成嵌套列表视图。"
* 例2："/folder-structure-blueprint-generator [VISUALIZATION_STYLE=Table] 输出包含 Path/Purpose/Content 的表格。"
* 例3："/folder-structure-blueprint-generator 标注各入口文件与常用脚本位置。"
* 例4："/folder-structure-blueprint-generator 为前后端各输出一份独立可视化。"
* 例5："/folder-structure-blueprint-generator 添加‘初学者路线’指引，说明先阅读哪些目录。"

### 3. 目录规则与命名约定（Conventions & Patterns）

* 用户故事：作为团队规范维护者，我需整理文件命名、目录命名、命名空间映射等约定。
* 例1："/folder-structure-blueprint-generator [INCLUDE_FILE_PATTERNS=true] 输出配置/实体/测试等文件的放置规则。"
* 例2："/folder-structure-blueprint-generator 记录命名大小写策略与前缀/后缀规范。"
* 例3："/folder-structure-blueprint-generator 说明 namespace/module 与目录对齐关系。"
* 例4："/folder-structure-blueprint-generator 列出跨领域共享代码的隔离策略。"
* 例5："/folder-structure-blueprint-generator 标识违反约定的目录并建议整改。"

### 4. 拓展模板与演进（Extension Templates & Evolution）

* 用户故事：作为特性 Owner，我要根据蓝图提供的模板创建新模块并保持一致性。
* 例1："/folder-structure-blueprint-generator [INCLUDE_TEMPLATES=true] 生成‘新功能’目录模板与必备文件。"
* 例2："/folder-structure-blueprint-generator 输出‘新增服务’模板，涵盖接口、实现、测试、配置。"
* 例3："/folder-structure-blueprint-generator 说明如何扩展微服务/前端模块并保持依赖隔离。"
* 例4："/folder-structure-blueprint-generator 提供拆分大型目录的渐进式重构步骤。"
* 例5："/folder-structure-blueprint-generator 描述结构演进历史与变更记录流程。"

### 5. 结构治理与合规（Governance & Enforcement）

* 用户故事：作为 DevOps，我需要记录结构校验工具、CI 检查与文档更新策略，确保蓝图持续有效。
* 例1："/folder-structure-blueprint-generator 列出 lint/脚本/CI 检查如何保证目录结构。"
* 例2："/folder-structure-blueprint-generator 标注结构决策记录位置（ADR/Blueprint 版本）。"
* 例3："/folder-structure-blueprint-generator 增加‘蓝图维护指南’，说明更新频率与责任人。"
* 例4："/folder-structure-blueprint-generator 记录结构变更回溯方法（git blame/commit hooks）。"
* 例5："/folder-structure-blueprint-generator 输出结构审核检查表与验收标准。"

## 原始文件

* [folder-structure-blueprint-generator.prompt.md](../../prompts/folder-structure-blueprint-generator.prompt.md)
