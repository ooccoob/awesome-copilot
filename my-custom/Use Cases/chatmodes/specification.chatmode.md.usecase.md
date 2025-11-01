---
post_title: "specification.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "specification-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "specification"]
ai_note: "Generated with AI assistance."
summary: "AI 可读的规范文档生成与维护：结构化模板、接口与约束、验收标准与依赖管理。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 面向新功能或存量功能的“规范文档”模式，输出机器可解析的、结构化的规范说明。

## When

- 启动新能力、重构现有功能、对外接口变更、需要清晰定义数据契约与验收标准时。

## Why

- 以明确的要求/约束/接口/验收标准为中心，避免歧义与口头传达偏差，支撑自动化实现与验证。

## How

- 使用固定模板（前言/Purpose/Definitions/Requirements/Interfaces/Acceptance/Testing/Dependencies/Examples…）；区分 REQ/CON/GUD/PAT 等前缀；保存到 /spec/，文件名遵循 `spec-[purpose]-[topic].md` 规范。

## Key points (英文+中文对照)

- Precise and unambiguous.（精确且无歧义）
- Structured and self-contained.（结构化且自包含）
- Clear acceptance criteria.（明确的验收标准）
- Interfaces and contracts.（接口与契约清晰）
- Purpose-first naming.（以目的前缀命名）

## 使用场景

### 1. 新功能规范（New feature specification）

- 用户故事：作为产品/架构，我要为新功能定义清晰边界、数据契约与验收标准，以便团队并行推进。
- 例 1："按照模板生成一个 spec-process-user-invite.md，包含 REQ/CON/AC。"
- 例 2："为接口提供 JSON Schema 与示例 payload，并列出错误码。"
- 例 3："把业务词汇表补全到 Definitions，并消除同义词歧义。"
- 例 4："补充 Given-When-Then 的 AC 覆盖边界条件。"
- 例 5："列出 External Integrations 与合规依赖，并避免实现细节。"

### 2. 存量功能补规范（Backfill specification）

- 用户故事：作为维护者，我需要为既有模块补充规范文档，便于迁移与重构。
- 例 1："扫描模块，输出 spec-design-legacy-module.md 的初稿。"
- 例 2："从代码与测试中抽取事实，填充 Requirements 与 Interfaces。"
- 例 3："按现状校准 AC，并提出缺失测试建议。"
- 例 4："梳理外部依赖与版本约束，写入 Dependencies。"
- 例 5："把临时约束与长期目标分级记录。"

### 3. 变更驱动的更新（Change-driven updates）

- 用户故事：作为负责人，我要将需求变更同步到规范，并保持机器可读。
- 例 1："根据变更说明，更新 REQ-xxx 与 AC-xxx，并新增示例。"
- 例 2："标记废弃接口，添加迁移路径与弃用时间线。"
- 例 3："对变更影响的上下游接口添加提醒。"
- 例 4："根据新约束，补充 CON-xxx 与 PAT-xxx。"
- 例 5："更新 last_updated 与变更摘要。"

### 4. 合规与安全要求（Compliance and security）

- 用户故事：作为安全/合规角色，我要把强制性要求纳入规范并量化验证项。
- 例 1："添加安全前缀条目 SEC-xxx 并解释验证方法。"
- 例 2："把数据最小化、留存、脱敏要求写入并示例。"
- 例 3："记录第三方合规（如 GDPR）影响的实现边界。"
- 例 4："增补性能/可用性/可观测性标准。"
- 例 5："将规范与流水线校验脚本关联。"

### 5. 与计划/实现协作（Handoff to planning/implementation）

- 用户故事：作为团队协调者，我希望规范可直接驱动实现计划与测试设计。
- 例 1："从 REQ/AC 派生实现计划骨架。"
- 例 2："基于接口契约生成契约测试草案。"
- 例 3："把 Examples/Edge cases 转为测试用例集。"
- 例 4："导出依赖清单给架构评审。"
- 例 5："将规范链接到相关 issue 与 PR。"

## 原始文件

- chatmodes/specification.chatmode.md
