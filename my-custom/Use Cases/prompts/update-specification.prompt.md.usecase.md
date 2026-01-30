---
post_title: 'update-specification.prompt.md Use Cases'
author1: 'github-copilot'
post_slug: 'update-specification-prompt-use-cases'
microsoft_alias: 'copilot'
featured_image: ''
categories: []
tags: ['use-cases', 'specification', 'documentation', 'requirements']
ai_note: 'Generated with AI assistance.'
summary: 'Use case scenarios for updating AI-ready specifications with precise requirements, interfaces, and compliance context.'
post_date: '2025-10-20'
---

<!-- markdownlint-disable MD041 -->

## What

* 使用“Update Specification”提示词，根据最新需求与代码变更更新现有规格文档，确保结构、术语与验证标准适配 AI。

## When

* 业务需求、接口合同、合规约束发生变化时。
* 代码或系统架构调整影响规格内容，需要重新同步文档时。

## Why

* 保持规格文档最新、可解析、可执行，使团队与 AI 工具对需求理解一致。
* 通过结构化更新，减少歧义和遗漏，提升交付质量与审计透明度。

## How

* 指定 `${file}` 或提供上下文，按模板更新 front matter、需求/接口/验收标准等章节。
* 使用标准化 ID（REQ-/CON-/SEC-/AC- 等），提供清晰定义、例子和验证策略。
* 输出 Markdown，命名遵循 `spec/` 目录规范 `[purpose]-*.md`。

## Key points (英文+中文对照)

* Precise requirements mapping（精确映射需求）
* Structured interfaces（结构化接口描述）
* Explicit acceptance criteria（明确验收标准）
* Compliance & dependency capture（捕捉合规与依赖）
* Self-contained updates（输出自包含更新）

## 使用场景

### 1. 基线对齐与前言更新（Baseline & Introduction）

* 用户故事：作为规格维护者，我要快速更新概述、日期、状态标签，让文档反映当前版本。
* 例1："/update-specification [file=spec/process-release.md] 更新 front matter 的 last_updated 与 owner。"
* 例2："/update-specification [file=spec/data-sync.md] 重写 Introduction，说明新业务动机。"
* 例3："/update-specification [file=spec/design-mobile-shell.md] 增加状态徽章描述，强调当前进度。"
* 例4："/update-specification [file=spec/process-ai-handbook.md] 引入新的 tags 标记（`ai`, `governance`）。"
* 例5："/update-specification [file=spec/architecture-edge-gateway.md] 标注版本号与审阅人。"

### 2. 需求、约束与指南（Requirements & Constraints）

* 用户故事：作为产品/安全负责人，我要映射新增需求、约束、指南，并确保编号体系完整。
* 例1："/update-specification [file=spec/process-release.md] 新增 REQ-00X 和 CON-00X 对应变更。"
* 例2："/update-specification [file=spec/security-auth.md] 补充 SEC-00X 条目与加固细节。"
* 例3："/update-specification [file=spec/data-ingest.md] 加入 PAT-00X 与 GUD-00X 指引。"
* 例4："/update-specification [file=spec/toolchain-ci.md] 对弃用条目增加 Deprecated 说明。"
* 例5："/update-specification [file=spec/infrastructure-aks.md] 将旧约束迁移到新章节并标注来源。"

### 3. 接口与数据契约（Interfaces & Contracts）

* 用户故事：作为集成工程师，我要更新 API、消息、数据模型，保证示例一致且具备边界情况。
* 例1："/update-specification [file=spec/api-orders.md] 更新 REST 端点表格与字段说明。"
* 例2："/update-specification [file=spec/data-sync.md] 增加 JSON Schema 示例与边界值。"
* 例3："/update-specification [file=spec/toolchain-ci.md] 补充 GitHub Actions workflow 接口描述。"
* 例4："/update-specification [file=spec/architecture-edge-gateway.md] 记录新消息队列 Topic 合约。"
* 例5："/update-specification [file=spec/process-ai-handbook.md] 给出 AI 推理输入/输出样例与格式约束。"

### 4. 验收标准与测试策略（Acceptance & Testing）

* 用户故事：作为测试负责人，我要同步验收条目、Given-When-Then 格式、自动化策略，确保覆盖新需求。
* 例1："/update-specification [file=spec/process-release.md] 为新流程添加 AC-00X 条目。"
* 例2："/update-specification [file=spec/security-auth.md] 描述新的安全测试与渗透测试计划。"
* 例3："/update-specification [file=spec/data-ingest.md] 更新测试数据管理策略与清理流程。"
* 例4："/update-specification [file=spec/toolchain-ci.md] 增加 CI/CD 自动化验证步骤表。"
* 例5："/update-specification [file=spec/architecture-edge-gateway.md] 说明负载与性能测试基线。"

### 5. 依赖、合规与附录（Dependencies & Compliance）

* 用户故事：作为合规或外部集成负责人，我要更新外部依赖、法规要求、参考文献，确保落地可行。
* 例1："/update-specification [file=spec/security-auth.md] 添加新的 OAuth 提供商依赖条目。"
* 例2："/update-specification [file=spec/data-sync.md] 记录新增数据来源与访问频率。"
* 例3："/update-specification [file=spec/process-ai-handbook.md] 添加合规 COM-00X 与监管说明。"
* 例4："/update-specification [file=spec/infrastructure-aks.md] 列出平台依赖与 SLA 更新。"
* 例5："/update-specification [file=spec/api-orders.md] 引用相关外部文档与内部规范链接。"

## 原始文件

* [update-specification.prompt.md](../../prompts/update-specification.prompt.md)
