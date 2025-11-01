---
post_title: "boost-prompt.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "boost-prompt-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "prompt-engineering"]
ai_note: "Generated with AI assistance."
summary: "Use cases for interactive Joyride-powered prompt refinement that captures requirements, clarifies scope, and copies final prompts to the clipboard."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 交互式提示词打磨流程，借助 Joyride 追问、收集需求并生成高质量 Markdown 提示词。

## When

- 用户任务描述模糊，需 iterative 澄清并固化输入。
- 希望把最终提示词复制到剪贴板并便于二次复用时。
- 需要将需求拆分为可执行步骤与交付物。

## Why

- 避免遗漏关键约束或成功标准，确保提示词可执行。
- 提供结构化问答流程，统一输出格式，节省重复沟通成本。
- 通过 Joyride 自动复制结果，提升协作效率。

## How

- 使用 `joyride_request_human_input` 与用户对话，确认任务、约束、交付与资源。
- 组织 prompt 为清晰章节（背景、目标、步骤、交付物等）。
- 最终以 Markdown 形式输出，并调用 Joyride clipboard API 复制。
- 明确声明不生成代码，只做提示词设计。

## Key points (英文+中文对照)

- Iterative clarification workflow（迭代澄清工作流）
- Deliverable-focused prompt design（聚焦交付物的提示设计）
- Tool-assisted clipboard output（工具辅助剪贴板输出）
- No-code guarantee（保证不产出代码）
- Feedback loop support（支持反馈迭代）

## 使用场景

**文件名:取源文件相对路径，然后读取文件名，不包含 .prompt.md，例如 my-custom\\my-prompt\\my-api-create.prompt.md 生成的文件名为 my-api-create**

### 1. 初始需求访谈（Kickoff Discovery）

- 用户故事：作为产品经理，我要梳理模糊的功能想法，获取可执行的提示词，以便 AI 协作编写需求文档。
- 例 1："/boost-prompt [selection=需求草稿] 请引导我完善目标、受众与成功标准后生成提示词。"
- 例 2："/boost-prompt 逐步追问技术约束、交付格式、依赖，最终输出结构化提示。"
- 例 3："/boost-prompt 请提醒我补充示例输入与预期输出，避免 AI 理解偏差。"
- 例 4："/boost-prompt 完成后复制高保真提示词至剪贴板并通知我。"
- 例 5："/boost-prompt 记录未解问题并在结尾提示需要后续确认。"

### 2. 复杂任务拆解（Complex Task Breakdown）

- 用户故事：作为技术负责人，我要把跨团队协作的复杂任务拆解成清晰步骤和角色分工，生成标准化提示词。
- 例 1："/boost-prompt 引导我梳理多阶段任务并按阶段组织提示段落。"
- 例 2："/boost-prompt 询问依赖系统、接口与验收标准后补充到提示中。"
- 例 3："/boost-prompt 对关键风险点发起追问并写入提示的注意事项。"
- 例 4："/boost-prompt 将最终提示分节排版，确保易读。"
- 例 5："/boost-prompt 完成后复述关键步骤，便于我快速复核。"

### 3. 法规或流程合规校验（Compliance Alignment）

- 用户故事：作为合规经理，我要确保提示覆盖必要的法规、审批和审计流程。
- 例 1："/boost-prompt 引导我列出相关法规、审批节点与留痕要求。"
- 例 2："/boost-prompt 追问数据敏感度、保密级别并写入提示。"
- 例 3："/boost-prompt 在提示中添加责任人、汇报节奏与检查清单。"
- 例 4："/boost-prompt 强调不生成代码，仅输出流程指导。"
- 例 5："/boost-prompt 将最终提示复制到剪贴板并提醒我存档。"

### 4. 多轮反馈迭代（Feedback Loop）

- 用户故事：作为交付负责人，我要根据团队反馈快速迭代提示词，保持清晰版本记录。
- 例 1："/boost-prompt 对上一版本的差评逐项追问，修订提示。"
- 例 2："/boost-prompt 记录变更摘要并融入最新版本。"
- 例 3："/boost-prompt 更新成功标准和验收方式后重新输出。"
- 例 4："/boost-prompt 每次迭代完成都复制到剪贴板且提示确认。"
- 例 5："/boost-prompt 若仍有疑问，继续使用 joyride_request_human_input 采集信息。"

### 5. 培训与最佳实践沉淀（Training & Playbook）

- 用户故事：作为知识管理负责人，我要把团队的问答经验沉淀为可复用的提示词模板。
- 例 1："/boost-prompt 引导我梳理培训情境的背景、角色与目标。"
- 例 2："/boost-prompt 追问常见问题与标准回答，整理到提示模板中。"
- 例 3："/boost-prompt 要求我补充必要的材料链接和输出格式。"
- 例 4："/boost-prompt 在提示末尾加入反馈与优化流程说明。"
- 例 5："/boost-prompt 将模板复制到剪贴板以便共享给学员。"

### 6. 无代码自动化协作（No-Code Automation Handoff）

- 用户故事：作为自动化工程师，我要确保提示词能指导 AI 生成流程说明，而非直接写代码。
- 例 1："/boost-prompt 强调不产生代码，仅输出流程描述与参数说明。"
- 例 2："/boost-prompt 追问所需工具、环境与权限设置，补充到提示。"
- 例 3："/boost-prompt 将操作步骤按顺序列出，减少执行偏差。"
- 例 4："/boost-prompt 添加错误处理与回滚建议，增强可靠性。"
- 例 5："/boost-prompt 提醒我在执行前复核提示的约束条件。"

## 原始文件

- [boost-prompt.prompt.md](../../prompts/boost-prompt.prompt.md)
