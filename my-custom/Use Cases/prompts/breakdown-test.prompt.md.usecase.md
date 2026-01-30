---
post_title: "breakdown-test.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "breakdown-test-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "quality-assurance"]
ai_note: "Generated with AI assistance."
summary: "Use cases for crafting ISTQB- and ISO 25010-aligned test strategies, QA plans, and issue checklists." 
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 依据 ISTQB 与 ISO 25010 标准生成测试策略、QA 计划及 Issue 清单，覆盖功能、非功能与风险验证。

## When

- Feature artefacts（PRD、技术拆解、实施计划、项目计划）齐备，准备进入测试规划阶段。
- 需要将质量保障工作映射到 GitHub Issues 与自动化流程。

## Why

- 系统化规划测试范围、技术与质量门禁，降低漏测风险。
- 明确测试文档与 Issue 模板，提升协作与可追踪性。
- 提供量化指标与质量度量，支撑验收与改进。

## How

- 输入 PRD、技术拆解、实施计划、项目计划，输出 Test Strategy、Test Issues Checklist、QA Plan。
- 应用 ISTQB 测试设计技术、ISO 25010 质量特性矩阵、风险评估与环境策略。
- 生成 GitHub Issue 模板及自动化建议，覆盖各测试层级与指标。

## Key points (英文+中文对照)

- ISTQB technique orchestration（统筹 ISTQB 测试技术）
- ISO 25010 quality mapping（映射 ISO 25010 质量特性）
- Risk-driven prioritization（风险驱动优先级）
- GitHub-integrated QA governance（GitHub 集成质量治理）
- Metrics-based validation（以度量驱动验证）

## 使用场景

**文件名:取源文件相对路径，然后读取文件名，不包含 .prompt.md，例如 my-custom\\my-prompt\\my-api-create.prompt.md 生成的文件名为 my-api-create**

### 1. Feature 测试规划启动（Feature Test Kickoff）

- 用户故事：作为测试负责人，我要为新功能制定完整测试策略与任务分解，确保上线质量。
- 例 1："/breakdown-test [selection=docs/ways-of-work/plan/epic-x/feature-y] 生成测试策略、QA 计划与 Issue 清单。"
- 例 2："/breakdown-test 列出各测试类型（功能、性能、安全、回归）的覆盖方案。"
- 例 3："/breakdown-test 识别高风险场景并制定缓解措施。"
- 例 4："/breakdown-test 提供测试环境、数据与工具配置建议。"
- 例 5："/breakdown-test 生成与 GitHub 看板联动的任务分解与估算。"

### 2. 质量门禁与度量设定（Quality Gate Definition）

- 用户故事：作为质量经理，我要定义质量门禁、指标与审核流程，确保交付达标。
- 例 1："/breakdown-test 提供符合 ISO 25010 的质量特性优先级矩阵。"
- 例 2："/breakdown-test 生成质量门禁的入口/出口标准与升级流程。"
- 例 3："/breakdown-test 列出需要跟踪的质量指标（覆盖率、缺陷密度等）。"
- 例 4："/breakdown-test 提示如何在 GitHub Issue 中落地模板与标签。"
- 例 5："/breakdown-test 规划质量评审会议与复盘安排。"

### 3. 自动化测试路线设计（Automation Roadmap）

- 用户故事：作为自动化工程师，我要落地从单元到 E2E 的自动化策略与任务。
- 例 1："/breakdown-test 细化单元、集成、E2E、性能、安全测试的自动化任务。"
- 例 2："/breakdown-test 制定 Playwright、API、性能脚本的实现步骤。"
- 例 3："/breakdown-test 给出 CI/CD 集成与触发策略。"
- 例 4："/breakdown-test 规划测试数据管理与隔离策略。"
- 例 5："/breakdown-test 输出自动化覆盖与估算指南。"

### 4. 风险驱动回归策略（Risk-based Regression）

- 用户故事：作为测试架构师，我要构建风险驱动的回归测试范围与优先级。
- 例 1："/breakdown-test 标注高、中、低风险场景与对应测试策略。"
- 例 2："/breakdown-test 分配回归测试频次与资源需求。"
- 例 3："/breakdown-test 输出缺陷趋势监控与预警方案。"
- 例 4："/breakdown-test 将回归任务映射到 GitHub Issues 与依赖。"
- 例 5："/breakdown-test 提供风险缓解与应急处理流程。"

### 5. 多团队质量协作（Cross-team QA Alignment）

- 用户故事：作为项目经理，我要让开发、测试、DevOps、业务共享质量目标与动作计划。
- 例 1："/breakdown-test 汇总质量目标、关键里程碑和责任划分。"
- 例 2："/breakdown-test 生成跨团队依赖与阻塞可视化。"
- 例 3："/breakdown-test 提供协作标签、优先级和通知机制建议。"
- 例 4："/breakdown-test 制定知识传递与培训计划。"
- 例 5："/breakdown-test 输出日报/周报质量指标模板。"

### 6. 合规与审计准备（Compliance & Audit Readiness）

- 用户故事：作为合规负责人，我要确保测试活动满足行业法规与审计要求。
- 例 1："/breakdown-test 列出安全、隐私、可用性等法规相关测试项。"
- 例 2："/breakdown-test 规划审计所需的测试文档与证据。"
- 例 3："/breakdown-test 指出需记录的审批、变更与缺陷处理流程。"
- 例 4："/breakdown-test 给出合规标签与质量门禁配置。"
- 例 5："/breakdown-test 提供审计前的自检清单与风险提示。"

## 原始文件

- [breakdown-test.prompt.md](../../prompts/breakdown-test.prompt.md)
