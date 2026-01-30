---
post_title: "tdd-red.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "tdd-red-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "tdd-red"]
ai_note: "Generated with AI assistance."
summary: "TDD 红灯阶段的用例：从 GitHub Issue 解析需求，先写失败测试，确保因未实现而失败。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 以问题驱动地先写失败测试，描述期望行为与边界，确保失败原因是“缺实现，而非语法错误”。

## When

- 新需求/缺陷修复之初；需要将 Issue 的验收标准映射为可执行测试时。

## Why

- 通过测试先行锁定行为定义，避免过度设计，建立可回归的行为契约。

## How

- 从分支名提取 Issue 编号，读取 Issue 描述与评论；提取验收标准与边界用例；用 xUnit/FluentAssertions/AutoFixture 撰写测试；一次只写一个测试并验证确实失败。

## Key points (英文+中文对照)

- Write tests first.（先写测试）
- Fail for the right reason.（因未实现而失败）
- One test at a time.（一次一个测试）
- AAA pattern.（遵循 Arrange-Act-Assert）
- Behaviour-focused names.（用行为命名）

## 使用场景

### 1. 从 Issue 到测试（Issue-to-test translation）

- 用户故事：作为开发者，我需要将 Issue 的验收标准转为具体测试用例。
- 例 1："解析分支名中的编号，抓取对应 Issue 内容生成测试骨架。"
- 例 2："根据 DoD 清单生成测试名称与断言。"
- 例 3："标出与边界相关的 Theory 数据集。"
- 例 4："在注释中引用 Issue 链接。"
- 例 5："运行测试，确认失败原因为未实现。"

### 2. 边界与异常优先（Edges and error-first）

- 用户故事：作为质量把关者，我要先覆盖最易错的边界与异常路径。
- 例 1："基于评论中提到的边界，生成最小失败测试。"
- 例 2："补充错误输入/空值/极端规模的案例。"
- 例 3："考虑并发/时序/超时等隐性边界。"
- 例 4："记录测试数据来源与假设。"
- 例 5："确保每个测试只断言一个结果。"

### 3. 语义化命名（Semantic naming）

- 用户故事：作为团队成员，我需要可读性强的测试名与结构。
- 例 1："采用 Should_{Behaviour}_When_{Condition}_Issue123 格式。"
- 例 2："为每个测试添加 AAA 明确分段。"
- 例 3："当行为未明时，先回到 Issue 澄清。"
- 例 4："将重复 Arrange 抽到装置方法。"
- 例 5："在失败信息中包含可诊断上下文。"

### 4. 与绿色/重构衔接（Link to Green/Refactor）

- 用户故事：作为执行者，我希望与后续阶段顺畅衔接。
- 例 1："在测试名或注释中预留实现意图提示。"
- 例 2："给 Green 阶段提供最小实现线索。"
- 例 3："记录需要在 Refactor 处理的技术债。"
- 例 4："确保无生产代码被提前引入。"
- 例 5："在 PR 里附上失败截图作为证据。"

## 原始文件

- [chatmodes/tdd-red.chatmode.md](../../../chatmodes/tdd-red.chatmode.md)
