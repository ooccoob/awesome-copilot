---
post_title: "ai-prompt-engineering-safety-review.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "ai-prompt-engineering-safety-review-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "prompt-engineering", "safety"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the AI Prompt Engineering Safety Review prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于审查和增强 AI 提示词安全性的工作流程。

## When

- 在将提示词部署到生产环境之前。
- 当提示词可能处理敏感信息或生成有风险的内容时。
- 需要确保提示词符合安全和合规要求时。

## Why

- 识别和减轻与提示词相关的潜在安全风险，如注入攻击、数据泄露或不当内容生成。
- 提高 AI 生成内容的可靠性和安全性。
- 确保 AI 应用符合组织的安全策略和行业最佳实践。

## How

- 使用 `/ai-prompt-engineering-safety-review` 命令并提供要审查的提示词。
- AI 将分析提示词的潜在漏洞，并提供改进建议。
- 根据建议修改提示词，并可选择再次提交以进行重新审查。

## Key points (英文+中文对照)

- Prompt Safety Review (提示词安全审查)
- Risk Mitigation (风险缓解)
- Compliance Assurance (合规保证)
- Iterative Refinement (迭代优化)

## 使用场景

### 1. 生产部署前的最终审查 (Final Review Before Production)

- **用户故事**: 作为一名 AI 工程师，在将一个新的聊天机器人功能上线之前，我需要确保其提示词是安全的，不会被恶意用户利用。
- **例 1**: `/ai-prompt-engineering-safety-review [selection=new_chatbot.prompt.md] 请审查此提示词是否存在注入漏洞。`
- **例 2**: `/ai-prompt-engineering-safety-review [selection=new_chatbot.prompt.md] 分析此提示词是否可能生成不当或有害内容。`

### 2. 处理敏感数据的提示词 (Prompts Handling Sensitive Data)

- **用户故事**: 作为一名开发人员，我正在编写一个处理用户个人信息的提示词，我需要确保它不会意外泄露敏感数据。
- **例 1**: `/ai-prompt-engineering-safety-review [selection=pii_processing.prompt.md] 检查此提示词的数据处理部分是否存在隐私泄露风险。`
- **例 2**: `/ai-prompt-engineering-safety-review [selection=pii_processing.prompt.md] 评估此提示词在处理财务数据时的安全性。`

### 3. 合规性检查 (Compliance Check)

- **用户故事**: 作为一名合规官，我需要验证公司的 AI 提示词是否符合 GDPR 和其他数据保护法规。
- **例 1**: `/ai-prompt-engineering-safety-review [selection=customer_service.prompt.md] 审查此提示词是否满足 GDPR 的数据最小化原则。`
- **例 2**: `/ai-prompt-engineering-safety-review [selection=customer_service.prompt.md] 确认此提示词的输出不包含任何受保护的健康信息 (PHI)。`

### 4. 第三方或开源提示词的安全性评估 (Security Assessment of Third-Party Prompts)

- **用户故事**: 作为一名安全分析师，我需要评估从开源社区获取的提示词模板的安全性，然后再将其集成到我们的系统中。
- **例 1**: `/ai-prompt-engineering-safety-review [selection=open_source_template.prompt.md] 分析这个从 GitHub 下载的提示词模板是否存在已知的安全漏洞。`

## 原始文件

- [ai-prompt-engineering-safety-review.prompt.md](../../prompts/ai-prompt-engineering-safety-review.prompt.md)
