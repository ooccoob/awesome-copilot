---
post_title: "code-exemplars-blueprint-generator.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "code-exemplars-blueprint-generator-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "code-quality"]
ai_note: "Generated with AI assistance."
summary: "Use cases for generating exemplar catalogs that surface high-quality code patterns across diverse tech stacks." 
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 扫描代码库并生成 `exemplars.md`，整理跨技术栈的高质量代码样例与最佳实践。

## When

- 建立团队统一编码标准、模式库或做知识传承时。
- 准备重构、审计或基线质量评估。
- 新成员加入或需要快速定位参考实现。

## Why

- 将优质样式显性化，避免重复造轮子。
- 巩固架构层次、模式分类与命名规范。
- 支持跨团队协作与持续质量提升。

## How

- 设置技术类型、扫描深度、分类方式、示例数量等变量。
- 依据标准评估命名、错误处理、分层、文档与测试。
- 生成有层次的 `exemplars.md`，附带描述、代码片段与维护建议。

## Key points (英文+中文对照)

- Technology-aware exemplar mapping（按技术识别范例）
- Pattern-based categorization（基于模式的分类）
- Architecture layer coverage（覆盖架构各层）
- Actionable documentation output（生成可执行文档）
- Continuous quality reinforcement（强化持续质量）

## 使用场景

**文件名:取源文件相对路径，然后读取文件名，不包含 .prompt.md，例如 my-custom\\my-prompt\\my-api-create.prompt.md 生成的文件名为 my-api-create**

### 1. 质量基线盘点（Quality Baseline Audit）

- 用户故事：作为代码守护者，我要梳理现有项目的最佳实现，用于质量基准对比。
- 例 1："/code-exemplars-blueprint-generator [selection=repo-root] 生成 .NET 服务层与测试的高质量示例。"
- 例 2："/code-exemplars-blueprint-generator 调整 `SCAN_DEPTH=Comprehensive` 获取架构观察与反模式提示。"
- 例 3："/code-exemplars-blueprint-generator 仅关注 Java/Kotlin 模块的仓储与实体范例。"
- 例 4："/code-exemplars-blueprint-generator 输出每类示例不超过 2 个，便于审核。"
- 例 5："/code-exemplars-blueprint-generator 标注共性命名、日志与异常处理模式。"

### 2. 新成员入职指南（Onboarding Playbook）

- 用户故事：作为技术负责人，我要为新成员提供示例目录，展示项目写法与规范。
- 例 1："/code-exemplars-blueprint-generator 分类为 Pattern Type，生成可读示例索引。"
- 例 2："/code-exemplars-blueprint-generator `INCLUDE_CODE_SNIPPETS=true`，方便新人快速理解。"
- 例 3："/code-exemplars-blueprint-generator 强调前端状态管理与 API 调用的最佳实践。"
- 例 4："/code-exemplars-blueprint-generator 提供结合测试与实现的成对范例。"
- 例 5："/code-exemplars-blueprint-generator 在结尾加入维护指南与后续更新建议。"

### 3. 多栈协作对齐（Polyglot Alignment）

- 用户故事：作为架构师，我要同步不同技术栈的标准，实现跨团队一致性。
- 例 1："/code-exemplars-blueprint-generator `PROJECT_TYPE=Auto-detect` 收集前端/后端/脚本范例。"
- 例 2："/code-exemplars-blueprint-generator 区分 Architecture Layer 展示全栈流程。"
- 例 3："/code-exemplars-blueprint-generator 标注依赖注入、配置与安全的范例。"
- 例 4："/code-exemplars-blueprint-generator 输出多语言下共通的日志与错误治理模式。"
- 例 5："/code-exemplars-blueprint-generator 结合 `MAX_EXAMPLES_PER_CATEGORY=3` 避免信息过载。"

### 4. 重构/迁移参考（Refactor & Migration Guide）

- 用户故事：作为重构负责人，我要找到最优代码样式，指导遗留系统升级。
- 例 1："/code-exemplars-blueprint-generator [selection=legacy-module] 找出现代化可复用的范本。"
- 例 2："/code-exemplars-blueprint-generator 提炼抗腐败层、仓储与服务重构的案例。"
- 例 3："/code-exemplars-blueprint-generator 记录需要避免的反模式供迁移对照。"
- 例 4："/code-exemplars-blueprint-generator 为云原生部署提供 Docker/CI exemplars。"
- 例 5："/code-exemplars-blueprint-generator 输出后续维护建议与质量守护计划。"

### 5. 审查与评估（Review & Assessment）

- 用户故事：作为审计团队，我要评估代码是否遵循标准，并汇总得分示例。
- 例 1："/code-exemplars-blueprint-generator 生成各层质量指标与推荐范例。"
- 例 2："/code-exemplars-blueprint-generator `INCLUDE_COMMENTS=false` 聚焦文件引用，便于手动审核。"
- 例 3："/code-exemplars-blueprint-generator 在附录列出需要改进的警示案例。"
- 例 4："/code-exemplars-blueprint-generator 记录测试覆盖率与断言写法示例。"
- 例 5："/code-exemplars-blueprint-generator 输出合规与安全相关的范例清单。"

### 6. 模板与知识库建设（Template & Knowledge Base）

- 用户故事：作为知识库维护者，我要定期更新示例文档，为 Prompt/Doc 模板提供素材。
- 例 1："/code-exemplars-blueprint-generator 定期扫描并更新知识库中的示例链接。"
- 例 2："/code-exemplars-blueprint-generator 将优秀模式转为指导文档的引用源。"
- 例 3："/code-exemplars-blueprint-generator 提供多语言、跨项目的示例集合。"
- 例 4："/code-exemplars-blueprint-generator 输出提醒，提示何时需要重新跑扫描。"
- 例 5："/code-exemplars-blueprint-generator 结合 `CATEGORIZATION=File Type` 支持模板生成器使用。"

## 原始文件

- [code-exemplars-blueprint-generator.prompt.md](../../prompts/code-exemplars-blueprint-generator.prompt.md)
