---
post_title: "breakdown-plan.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "breakdown-plan-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "project-management"]
ai_note: "Generated with AI assistance."
summary: "Use cases for generating GitHub project plans with automated epic/feature/story breakdown, dependencies, and issue checklists."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 生产 GitHub 项目计划与 Issue 自动化蓝图，覆盖 Epic→Feature→Story/Enabler→Test 层级、依赖与看板配置。

## When

- Feature 产物齐备（PRD、设计、技术拆解、测试计划）后准备执行。
- 需要自动化创建 Issue、配置依赖、优先级与看板流程。
- 准备 Sprint 规划与跨团队协调时。

## Why

- 将需求与技术实现映射到 GitHub 项目，实现全流程可追踪。
- 统一 Issue 模板、优先级、估算策略，提高协作效率。
- 自动化看板更新、依赖跟踪，减少人工操作。

## How

- 输入完整特性 artefacts（PRD、技术拆解、实施计划等）。
- 输出 `/project-plan.md` 和 `/issues-checklist.md`，包含工作层级、模板、优先矩阵、估算与自动化配置。
- 按最佳实践构建 Mermaid 图、Issue 模板、GitHub Actions。
- 集成 Sprint 规划、看板列与自定义字段建议。

## Key points (英文+中文对照)

- Hierarchical planning automation（分层规划自动化）
- Dependency orchestration（依赖编排）
- GitHub workflow integration（GitHub 工作流整合）
- Value-based prioritization（基于价值的优先级）
- Metrics-driven governance（指标驱动治理）

## 使用场景

**文件名:取源文件相对路径，然后读取文件名，不包含 .prompt.md，例如 my-custom\\my-prompt\\my-api-create.prompt.md 生成的文件名为 my-api-create**

### 1. Feature 开发启动（Feature Kickoff）

- 用户故事：作为项目经理，我要把新特性的所有 artefacts 转化为 GitHub 项目计划与 Issue 清单。
- 例 1："/breakdown-plan [selection=docs/ways-of-work/plan/epic-x/feature-y] 生成完整项目计划与 Issue 模板。"
- 例 2："/breakdown-plan 自动构建 Epic→Feature→Story/Enabler Mermaid 图。"
- 例 3："/breakdown-plan 输出依赖关系与阻塞路径。"
- 例 4："/breakdown-plan 提供优先级与价值矩阵，指导排期。"
- 例 5："/breakdown-plan 生成 Issues checklist，确保故事、使能项、测试项被创建。"

### 2. Sprint 规划与容量评估（Sprint Planning）

- 用户故事：作为 Scrum Master，我要在计划会议前准备好故事、估算与看板配置。
- 例 1："/breakdown-plan 生成 Sprint 容量估算与目标模板。"
- 例 2："/breakdown-plan 提供故事点与 T-Shirt 估算指南。"
- 例 3："/breakdown-plan 列出需优先进入 Sprint 的高价值任务。"
- 例 4："/breakdown-plan 指导如何配置看板列与自定义字段。"
- 例 5："/breakdown-plan 输出自动化脚本片段便于更新状态。"

### 3. 跨团队协作同步（Cross-team Alignment）

- 用户故事：作为项目总监，我要让多个团队共享相同的工作层级与依赖视图。
- 例 1："/breakdown-plan 生成依赖图示，说明各团队交付顺序。"
- 例 2："/breakdown-plan 描述不同标签、组件字段的配置，方便筛选。"
- 例 3："/breakdown-plan 制定自动化 Issue 创建策略，减少重复劳动。"
- 例 4："/breakdown-plan 输出风险与缓解措施供周会跟踪。"
- 例 5："/breakdown-plan 给出成功指标与监控建议。"

### 4. DevOps 自动化建设（DevOps Automation）

- 用户故事：作为 DevOps 工程师，我要构建 GitHub Actions 以自动创建/更新 Issue 状态。
- 例 1："/breakdown-plan 提供自动化 Issue 创建工作流示例。"
- 例 2："/breakdown-plan 生成 PR 触发的看板状态转换脚本。"
- 例 3："/breakdown-plan 指出各自动化任务的触发条件与权限要求。"
- 例 4："/breakdown-plan 列出持续监控指标与报表需求。"
- 例 5："/breakdown-plan 包含质量、安全相关的自动化检查建议。"

### 5. 复盘与流程改进（Retrospective & Improvement）

- 用户故事：作为流程改进负责人，我要分析项目执行数据并持续优化。
- 例 1："/breakdown-plan 输出执行度量指标：Velocity、Cycle Time 等。"
- 例 2："/breakdown-plan 根据指标提供流程优化建议。"
- 例 3："/breakdown-plan 列出 Definition of Ready/Done 审查项。"
- 例 4："/breakdown-plan 指导如何记录回顾结论并更新模板。"
- 例 5："/breakdown-plan 制定下一轮计划前的准备 checklist。"

### 6. 客户/伙伴交付透明化（Stakeholder Visibility）

- 用户故事：作为客户成功经理，我要让客户透明了解 Epic 进度与依赖。
- 例 1："/breakdown-plan 生成面向客户的计划概要与成功指标。"
- 例 2："/breakdown-plan 输出关键里程碑与阻塞态势。"
- 例 3："/breakdown-plan 提供 Issue 标签与自定义字段说明，便于客户筛选。"
- 例 4："/breakdown-plan 建议自动化通知机制（如状态更新）。"
- 例 5："/breakdown-plan 给出共享给客户的报告格式。"

## 原始文件

- [breakdown-plan.prompt.md](../../prompts/breakdown-plan.prompt.md)
