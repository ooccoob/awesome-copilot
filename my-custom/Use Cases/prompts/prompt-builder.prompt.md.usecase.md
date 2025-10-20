---
post_title: 'prompt-builder.prompt.md Use Cases'
author1: 'github-copilot'
post_slug: 'prompt-builder-prompt-use-cases'
microsoft_alias: 'copilot'
featured_image: ''
categories: []
tags: ['use-cases', 'prompt-engineering', 'templates', 'copilot']
ai_note: 'Generated with AI assistance.'
summary: 'Use case scenarios for building, testing, and evolving prompts with structured sections, constraints, and evaluation rubrics.'
post_date: '2025-10-20'
---

<!-- markdownlint-disable MD041 -->

## What

* 通过可复用的“提示词构建器”模板，快速创建高质量、结构化、可评估的提示词与系统指令。

## When

* 需要为新任务/新角色设计稳定的提示词时。
* 需要将隐式需求转化为明确的指令、输入/输出契约、边界条件与评估标准时。
* 需要在团队中共享可维护的提示词资产与最佳实践时。

## Why

* 结构化提示词有助于可重复、可审计、可版本化地改进结果质量。
* 通过约束与评分标准可以降低幻觉与不一致性，提升对齐与可靠性。
* 模板化让不同场景复用成为可能，减少从零开始的成本。

## How

* 按模板组织内容：背景/目标、角色与语气、输入合同、输出格式、限制与安全、推理过程、验证与评测。
* 在每次迭代中记录变更原因与对比结果（A/B/C 实验）。
* 使用小样本单元测试（Happy Path + 边界 1-2 个）快速验证。
* 明确“不能做/不可访问”的范围与错误处理策略，避免越权与不良输出。

## Key points (英文+中文对照)

* Define clear inputs and outputs（定义清晰的输入与输出）
* Constrain behavior and tools（约束行为与工具使用）
* Add evaluation rubric and test cases（加入评估标准与测试用例）
* Version prompts and track changes（提示词版本化并追踪变更）
* Bias/safety considerations included（纳入偏见与安全考虑）

## 使用场景

### 1. 角色化助手设计（Role + Tone + Boundaries）

* 用户故事：作为产品负责人，我要定义一个“API 架构顾问”提示词，明确技能边界、语气与禁止事项。
* 例1："/prompt-builder 请创建‘Kubernetes 平台 SRE 顾问’提示词，语气专业、简洁，禁止臆测版本号。"
* 例2："/prompt-builder 为‘数据治理顾问’加入‘只能读取已提供表结构，禁止生成 DDL’的限制。"
* 例3："/prompt-builder 生成‘安全审计助手’模板，包含‘拒绝恶意请求’与‘最小权限’原则。"
* 例4："/prompt-builder 输出‘云成本优化顾问’提示词，要求列出 3 个节省策略与风险。"
* 例5："/prompt-builder 为‘技术写手’加入‘英中双语输出’与‘表格优先’要求。"

### 2. 输入合同与数据形状（Contracts）

* 用户故事：作为后端工程师，我要为‘API 设计器’定义输入 JSON schema 与错误模式，便于自动校验。
* 例1："/prompt-builder 定义接口生成器的输入 schema（paths/methods/params/examples）。"
* 例2："/prompt-builder 约定错误模式（400/401/403/404/429/5xx）与重试策略描述。"
* 例3："/prompt-builder 指定分页参数与边界限制，并在输出中强制包含。"
* 例4："/prompt-builder 约定鉴权字段在 headers 传递，示例需包含 curl。"
* 例5："/prompt-builder 设计‘空数据/大数据/超时’三类边界输入样例。"

### 3. 输出格式与可执行性（Deterministic Output）

* 用户故事：作为自动化平台工程师，我希望输出严格遵循 JSON/YAML/表格格式，便于 CI 消费。
* 例1："/prompt-builder JSON 输出必须符合 schema，给出校验失败时的回退策略。"
* 例2："/prompt-builder 生成 Markdown 表格，并提供 CSV 备用格式。"
* 例3："/prompt-builder 输出需要携带版本与变更号（semver + git sha）。"
* 例4："/prompt-builder 在代码块中仅包含可运行命令，不要解释性文字。"
* 例5："/prompt-builder 限制每条列表项不超过 120 字符，避免换行破坏解析。"

### 4. 约束与安全（Safety & Governance）

* 用户故事：作为合规负责人，我要把安全与偏见控制整合进提示词，拒绝违规请求并最小化数据暴露。
* 例1："/prompt-builder 加入‘只处理非敏感数据样例’与‘不访问外部网络’。"
* 例2："/prompt-builder 加入‘涉密字段脱敏’与‘日志不落明文凭证’。"
* 例3："/prompt-builder 加入‘拒绝仇恨/暴力/成人内容’，并返回合规错误。"
* 例4："/prompt-builder 明确‘不得输出法律/医疗等专业建议免责声明’。"
* 例5："/prompt-builder 增加‘数据最小化’与‘只读模式’声明。"

### 5. 推理过程与可解释性（Reasoning & Chains）

* 用户故事：作为架构师，我要要求模型在草稿中进行链式思考与对比，再输出精简结论。
* 例1："/prompt-builder 启用‘先思考后回答’并在最终答案隐藏中间推理。"
* 例2："/prompt-builder 要求给出 2-3 个方案对比表与选择理由。"
* 例3："/prompt-builder 对关键参数进行灵敏度分析，说明对结果影响。"
* 例4："/prompt-builder 在限制时间/成本/质量三角下给出权衡。"
* 例5："/prompt-builder 输出‘已知/未知/假设’三栏，明确风险与下一步验证。"

### 6. 评测与回归（Evaluation & Tests）

* 用户故事：作为质量负责人，我要对提示词进行小样本评测，收敛到稳定版本并持续回归。
* 例1："/prompt-builder 生成 Happy Path + 2 个边界用例，并定义评分标准。"
* 例2："/prompt-builder 制作 A/B 测试提示词变体与对比指标。"
* 例3："/prompt-builder 输出一次评测报告模板（样例数据 + 结论）。"
* 例4："/prompt-builder 设计失败回退策略（降级到简单指令/重试/人工）。"
* 例5："/prompt-builder 加入‘鲁棒性检查清单’，如空输入、噪声文本、越权请求。"

### 7. 生命周期与协作（Versioning & Collaboration）

* 用户故事：作为团队协作促进者，我要建立提示词的版本管理、评审流程与贡献指南。
* 例1："/prompt-builder 生成变更日志模板（日期/作者/动机/影响）。"
* 例2："/prompt-builder 制定 PR 模板与评审核对表（安全/格式/测试）。"
* 例3："/prompt-builder 设计目录规范与命名规则（kebab-case）。"
* 例4："/prompt-builder 输出依赖模型/工具矩阵与兼容性说明。"
* 例5："/prompt-builder 生成‘贡献指南’与‘常见问题’骨架文档。"

## 原始文件

* [prompt-builder.prompt.md](../../prompts/prompt-builder.prompt.md)
