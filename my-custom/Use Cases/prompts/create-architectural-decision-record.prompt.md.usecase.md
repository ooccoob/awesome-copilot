---
post_title: "create-architectural-decision-record.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "create-architectural-decision-record-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "architecture-governance"]
ai_note: "Generated with AI assistance."
summary: "Use cases for producing machine- and human-friendly Architectural Decision Records with coded traceability." 
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 基于结构化输入生成符合 ADR 标准、易于 AI 解析的 `adr-NNNN-*.md` 文档。

## When

- 需要记录架构决策、权衡与影响，形成团队共识。
- 引入新技术、架构变更或重要平台选择时。
- 审查、合规、知识传承或交接阶段。

## Why

- 提供可追踪、标准化的架构决策历史。
- 清晰呈现上下文、方案、正负影响与替代方案。
- 结合编码的条目（POS/NEG/ALT/IMP/REF）支持自动化分析。

## How

- 接受标题、上下文、决策、替代方案、干系人等输入；缺失则提示补充。
- 按模板生成注释头（front matter）、状态、背景、决策、正/负结果、替代方案、实施与引用。
- 自动决定 `adr-NNNN` 序号并存放于 `/docs/adr/`。

## Key points (英文+中文对照)

- Structured ADR format（结构化 ADR 格式）
- Positive/negative coded impacts（编码化正负影响）
- Alternatives with rejection rationale（替代方案与拒绝理由）
- Implementation guidance（实施指引）
- Traceable references（可追溯引用）

## 使用场景

**文件名:取源文件相对路径，然后读取文件名，不包含 .prompt.md，例如 my-custom\\my-prompt\\my-api-create.prompt.md 生成的文件名为 my-api-create**

### 1. 新技术引入评审（New Technology Adoption）

- 用户故事：作为架构师，我要记录采用新数据库的决策与影响。
- 例 1："/create-architectural-decision-record [selection=context.md] 生成 `adr-0007-distributed-db.md`。"
- 例 2："/create-architectural-decision-record 记录性能提升与成本增加的正负影响。"
- 例 3："/create-architectural-decision-record 描述备选方案及拒绝原因。"
- 例 4："/create-architectural-decision-record 加入迁移步骤与监控指标。"
- 例 5："/create-architectural-decision-record 引用相关标准或基线文档。"

### 2. 架构重大调整（Architecture Refactoring）

- 用户故事：作为平台负责人，我要记录单体拆分为微服务的决策。
- 例 1："/create-architectural-decision-record 梳理当前痛点与业务驱动。"
- 例 2："/create-architectural-decision-record 输出正面收益（扩展性）、负面影响（复杂度）。"
- 例 3："/create-architectural-decision-record 比较延迟拆分或保持现状的替代方案。"
- 例 4："/create-architectural-decision-record 给出分阶段实施与回滚策略。"
- 例 5："/create-architectural-decision-record 关联现有 ADR 与路线图。"

### 3. 合规与审批流程（Governance & Compliance）

- 用户故事：作为合规经理，我要把安全相关的架构决定记录成 ADR 供审计。
- 例 1："/create-architectural-decision-record 描述安全上下文与监管要求。"
- 例 2："/create-architectural-decision-record 列正面收益（合规、风险降低）与负面成本。"
- 例 3："/create-architectural-decision-record 记录拒绝其他安全方案的理由。"
- 例 4："/create-architectural-decision-record 加入实施注意事项与监控项。"
- 例 5："/create-architectural-decision-record 指明负责岗位与审计链接。"

### 4. 项目交接与知识传承（Handoff & Knowledge Transfer）

- 用户故事：作为技术负责人，我要把历史决策整理给新团队理解背景。
- 例 1："/create-architectural-decision-record 将旧系统遗留的关键决定补档。"
- 例 2："/create-architectural-decision-record 填写 Stakeholders 说明责任人。"
- 例 3："/create-architectural-decision-record 添加正负影响，帮助新人理解 trade-off。"
- 例 4："/create-architectural-decision-record 记录如何监控成功与避免失败。"
- 例 5："/create-architectural-decision-record 引用相关文档与设计图。"

### 5. 多团队对齐与评审（Cross-team Alignment）

- 用户故事：作为技术委员会成员，我要审阅多个团队的决策，确保一致性。
- 例 1："/create-architectural-decision-record 在评审会前根据输入生成标准 ADR。"
- 例 2："/create-architectural-decision-record 标注被拒绝的替代方案与原因。"
- 例 3："/create-architectural-decision-record 添加实施依赖与协调事项。"
- 例 4："/create-architectural-decision-record 记录影响范围与风险缓解计划。"
- 例 5："/create-architectural-decision-record 关联需要更新的标准或指南。"

### 6. 自动化流水线集成（Automation & CI Integration）

- 用户故事：作为 DevOps，我要在流水线中自动生成 ADR 草稿并供人工补充。
- 例 1："/create-architectural-decision-record 接收流水线输入生成草稿文件。"
- 例 2："/create-architectural-decision-record 确保文件命名遵循序号并存于 `/docs/adr/`。"
- 例 3："/create-architectural-decision-record 使用编码条目便于解析。"
- 例 4："/create-architectural-decision-record 加入提醒以保证缺失字段需人工补充。"
- 例 5："/create-architectural-decision-record 输出后通知评审与合并流程。"

## 原始文件

- [create-architectural-decision-record.prompt.md](../../prompts/create-architectural-decision-record.prompt.md)
