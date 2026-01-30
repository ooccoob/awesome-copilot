---
post_title: "tdd-green.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "tdd-green-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "tdd-green"]
ai_note: "Generated with AI assistance."
summary: "TDD 绿灯阶段的用例：以最小实现让失败测试通过，保持步子小、频繁提交。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 针对当前唯一失败的测试，编写解决它的最小实现（最低可行逻辑）。

## When

- Red 阶段已有失败测试，准备进入实现，使之转为通过时。

## Why

- 限制变化范围，降低回归风险；聚焦在“让测试通过”，避免过度设计与过早抽象。

## How

- 使用最直接的代码让测试通过；保留明显重复/异味到 Refactor 处理；频繁运行测试与提交；必要时添加更多测试以澄清行为。

## Key points (英文+中文对照)

- Make it pass.（先让测试通过）
- Small steps.（小步快跑）
- No premature abstraction.（避免过早抽象）
- Keep focus.（专注当前失败）
- Commit often.（频繁提交）

## 使用场景

### 1. 最小实现（Minimal implementation）

- 用户故事：作为开发者，我需要以最少代码让单个失败测试转绿。
- 例 1："返回硬编码常量以通过最初的简单断言。"
- 例 2："逐步替换硬编码为条件分支，覆盖更多示例。"
- 例 3："仅为当前断言添加所需字段或行为。"
- 例 4："避免引入外部依赖，先用内存实现。"
- 例 5："在提交信息中引用测试名。"

### 2. 逐例推进（Example-driven expansion）

- 用户故事：作为执行者，我希望随着更多示例加入，逐步扩展实现而不超前设计。
- 例 1："当新增示例失败时，再最小增量实现。"
- 例 2："将重复局部提炼函数，先不做全局抽象。"
- 例 3："记录仍存在的技术债以留到重构阶段。"
- 例 4："保证每次变更都由一个失败测试驱动。"
- 例 5："保持代码简单可读，注释阐明权衡。"

### 3. 与重构约定（Prepare for refactor）

- 用户故事：作为团队成员，我要为下一步重构留下线索与保护网。
- 例 1："标记待抽象的重复模式。"
- 例 2："添加覆盖边界的额外断言，强化保护网。"
- 例 3："在 PR 描述中列出后续重构点。"
- 例 4："拆出临时命名，稍后改为领域术语。"
- 例 5："补充针对异常路径的测试，避免回归。"

## 原始文件

- [chatmodes/tdd-green.chatmode.md](../../../chatmodes/tdd-green.chatmode.md)
