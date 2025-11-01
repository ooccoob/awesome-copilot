---
post_title: "demonstrate-understanding.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "demonstrate-understanding-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases","explain","pedagogy"]
ai_note: "Generated with AI assistance."
summary: "Demonstrate-understanding 模式：把复杂概念分解为对等解释、比喻与可验证示例的使用场景集合。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 提供把复杂技术点以可验证示例、分级解释与比喻呈现的方法，便于教育、评审与知识传递。

## When

- 在做设计评审、培训新成员或编写文档时需要把概念变得可检验、可复现。

## Why

- 明确的理解校验（teach-back）能降低误解并加速知识传播。

## How

- 给出分层解释模板（TL;DR / medium / deep dive）、示例代码/REPL 片段以及一组可自动校验的检查点。

## Key points (英文+中文对照)

- Layered explanations（分层解释）
- Concrete examples（具体示例）
- Teach-back checks（教会式校验）
- Analogies（类比）
- Validation steps（验证步骤）

## 使用场景

### 1. 设计评审沟通

- 用户故事：作为架构师，我要确保审查者理解设计假设与权衡。
- 例 1："生成可复现的最小示例并列出假设。"
- 例 2："提供图示与类比帮助理解并发模型。"
- 例 3："列出评审问题清单（验证点）。"
- 例 4："给出示例输入与期望输出进行端到端验证。"
- 例 5："对复杂术语给出简短定义与应用示例。"

### 2. 新人入职培训

- 用户故事：作为导师，我需要一套能被新人自测的学习任务。
- 例 1："创建练习题与自动评分提示。"
- 例 2："分步引导的 REPL 示例与边界测试。"
- 例 3："知识检查点与通过标准。"
- 例 4："推荐学习路径与资源链接。"
- 例 5："给出常见误区与纠正方法。"

### 3. 文档与示例库

- 用户故事：作为文档作者，我要为每个概念提供最小可运行示例。
- 例 1："生成可拷贝粘贴的代码示例与依赖说明。"
- 例 2："给出输入/输出样例与边界条件。"
- 例 3："创建可执行的 sandbox 链接或代码片段。"
- 例 4："示例的版本兼容注记。"
- 例 5："示例的性能/资源限制注释。"

### 4. 评审与知识共享

- 用户故事：作为团队成员，我需要把复杂问题解释给非专业同事。
- 例 1："用一个 3 行 TL;DR 开头并后续给出技术层次说明。"
- 例 2："用类比将系统行为映射到日常现象。"
- 例 3："提供可验证故事板用于非技术的验收。"
- 例 4："汇总 FAQ 与常见问题解决步骤。"
- 例 5："提供参考实现与变体对照表。"

### 5. 面向客户的白皮书与演示

- 用户故事：作为产品经理，我需要把复杂能力向客户清晰展示。
- 例 1："用用户旅程图示展示能力与限制。"
- 例 2："给出成功案例的可验证度量。"
- 例 3："准备 demo 脚本与失败处理说明。"
- 例 4："生成 FAQ 与合规/安全说明要点。"
- 例 5："为 PoC 准备最小实现清单。"

## 原始文件

- [chatmodes/demonstrate-understanding.chatmode.md](../../../chatmodes/demonstrate-understanding.chatmode.md)
