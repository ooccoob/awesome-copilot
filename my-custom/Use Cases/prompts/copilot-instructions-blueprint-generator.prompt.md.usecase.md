---
post_title: "copilot-instructions-blueprint-generator.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "copilot-instructions-blueprint-generator-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "copilot-governance"]
ai_note: "Generated with AI assistance."
summary: "Use cases for deriving copilot instruction blueprints that enforce architecture, versioning, and quality standards from actual codebases." 
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 根据现有代码模式生成 `copilot-instructions.md` 蓝图，指导 GitHub Copilot 输出与项目标准一致的代码。

## When

- 需要统一 Copilot 行为，避免使用超出项目版本的特性。
- 启动新项目或重构时，希望明确架构、质量、测试与文档规范。
- 多团队协作，需要共享 Copilot 指南以保持一致性。

## Why

- 确保 Copilot 生成的代码严格匹配实际架构与技术栈。
- 显性化代码库中的命名、模式、测试与文档标准。
- 降低上下文遗漏与假设风险，提升自动生成质量。

## How

- 配置技术类型、架构风格、质量关注点、文档/测试要求与版本策略。
- 扫描代码库抽取真实的版本、模式、命名、测试与质量实践。
- 生成结构化 `copilot-instructions.md`，强调“只依据实际模式，不做假设”。

## Key points (英文+中文对照)

- Version-accurate guidance（基于真实版本的指引）
- Architecture fidelity（保持架构一致性）
- Quality priority alignment（对齐质量优先级）
- Documentation and testing mandates（规定文档与测试要求）
- Pattern-driven governance（基于现有模式的治理）

## 使用场景

**文件名:取源文件相对路径，然后读取文件名，不包含 .prompt.md，例如 my-custom\\my-prompt\\my-api-create.prompt.md 生成的文件名为 my-api-create**

### 1. 新项目标准制定（New Project Standardization）

- 用户故事：作为架构师，我要为新项目生成 Copilot 指南，确保自动化生成符合架构与质量要求。
- 例 1："/copilot-instructions-blueprint-generator [selection=repo-root] 输出 `.github/copilot/copilot-instructions.md`。"
- 例 2："/copilot-instructions-blueprint-generator 设置 `ARCHITECTURE_STYLE=Layered` 强调分层边界。"
- 例 3："/copilot-instructions-blueprint-generator 指定 `CODE_QUALITY_FOCUS=All` 覆盖维护性/性能/安全/可测性。"
- 例 4："/copilot-instructions-blueprint-generator 列出真实版本与依赖，禁止使用未支持的特性。"
- 例 5："/copilot-instructions-blueprint-generator 生成测试、文档与命名的具体准则。"

### 2. 遗留系统守护（Legacy System Governance）

- 用户故事：作为技术负责人，我要确保 Copilot 不引入超出遗留系统能力的代码。
- 例 1："/copilot-instructions-blueprint-generator [selection=legacy-app] 捕捉旧版框架与 API 限制。"
- 例 2："/copilot-instructions-blueprint-generator `DOCUMENTATION_LEVEL=Minimal` 匹配遗留注释风格。"
- 例 3："/copilot-instructions-blueprint-generator 强调历史上的错误模式需避免。"
- 例 4："/copilot-instructions-blueprint-generator 指出常见日志、安全、配置写法。"
- 例 5："/copilot-instructions-blueprint-generator 约束测试策略，防止引入未使用的框架。"

### 3. 多团队协作统一（Cross-team Alignment）

- 用户故事：作为平台团队，我要让多个子团队遵循统一的 Copilot 指南。
- 例 1："/copilot-instructions-blueprint-generator `PROJECT_TYPE=Multiple` 适配前后端/脚本的不同标准。"
- 例 2："/copilot-instructions-blueprint-generator 输出 `.github/copilot` 目录关注文件列表。"
- 例 3："/copilot-instructions-blueprint-generator 规定冲突模式如何优先最新或测试覆盖更高的实现。"
- 例 4："/copilot-instructions-blueprint-generator 添加命名、日志、配置的跨团队要求。"
- 例 5："/copilot-instructions-blueprint-generator 整合版本策略，减少分支间差异。"

### 4. 架构迁移与守护（Architecture Migration Checkpoint）

- 用户故事：作为迁移负责人，我要在重构前生成指南，提醒 Copilot 维持现有边界并记录新要求。
- 例 1："/copilot-instructions-blueprint-generator 分析新旧模块的接口与通信模式。"
- 例 2："/copilot-instructions-blueprint-generator 指定 `TESTING_REQUIREMENTS=All` 强制覆盖测试。"
- 例 3："/copilot-instructions-blueprint-generator 强调新旧系统间的数据与安全策略。"
- 例 4："/copilot-instructions-blueprint-generator 写入迁移期间的暂时例外与 TODO。"
- 例 5："/copilot-instructions-blueprint-generator 在指南中加入后续审核建议。"

### 5. 外包/合作方协作（Vendor Coordination）

- 用户故事：作为合作项目负责人，我要确保外包团队使用 Copilot 时保持代码一致性。
- 例 1："/copilot-instructions-blueprint-generator 明确可用/不可用的语言特性与库版本。"
- 例 2："/copilot-instructions-blueprint-generator 规定提交的测试、文档与日志标准。"
- 例 3："/copilot-instructions-blueprint-generator 强调敏感信息与安全策略。"
- 例 4："/copilot-instructions-blueprint-generator 提供可参考的 exemplar 文件列表。"
- 例 5："/copilot-instructions-blueprint-generator 指示当缺少信息时需回顾代码库并提问。"

### 6. 持续治理与审计（Governance & Audit）

- 用户故事：作为质量经理，我要定期更新指南，记录架构或版本变更并追踪执行情况。
- 例 1："/copilot-instructions-blueprint-generator 定期扫描 repo 更新新版本与模式。"
- 例 2："/copilot-instructions-blueprint-generator 在说明中加入变更日志与审核节点。"
- 例 3："/copilot-instructions-blueprint-generator 配置 `CODE_QUALITY_FOCUS=Security` 时强化安全策略。"
- 例 4："/copilot-instructions-blueprint-generator 记录实际使用的测试框架与覆盖要求，便于审计。"
- 例 5："/copilot-instructions-blueprint-generator 定义何时需要再次执行扫描与更新。"

## 原始文件

- [copilot-instructions-blueprint-generator.prompt.md](../../prompts/copilot-instructions-blueprint-generator.prompt.md)
