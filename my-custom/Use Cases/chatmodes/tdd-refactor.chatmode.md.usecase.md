---
post_title: "tdd-refactor.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "tdd-refactor-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "tdd-refactor"]
ai_note: "Generated with AI assistance."
summary: "TDD 重构阶段的用例：在所有测试绿灯的保护下，消除重复、改进设计并保持行为不变。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 在测试通过的前提下，改进内部设计（命名、抽象、结构、性能），不改变外部可观察行为。

## When

- 绿灯后出现重复、坏味道或可读性差；需要引入领域语言或解耦时。

## Why

- 通过持续重构保持代码质量与可演进性，避免技术债滚雪球。

## How

- 选择明确的重构手法（提炼函数/内联变量/引入参数对象/策略替换条件等）；每次一个小步并运行测试；不新增功能。

## Key points (英文+中文对照)

- Behaviour unchanged.（行为不变）
- One refactor step.（一次只做一步）
- Tests as safety net.（测试是安全网）
- Name things well.（命名清晰）
- Remove duplication.（去重）

## 使用场景

### 1. 去重与抽象（Deduplicate and abstract）

- 用户故事：作为开发者，我希望消除重复，提炼稳定抽象以降低维护成本。
- 例 1："将重复 Arrange 抽到测试装置或工厂。"
- 例 2："用策略/多态替代复杂条件分支。"
- 例 3："合并重复的验证与映射逻辑。"
- 例 4："提炼领域值对象，替代原始类型。"
- 例 5："引入不可变数据结构减少副作用。"

### 2. 设计与可读性（Design and readability）

- 用户故事：作为评审者，我要提升可读性与一致性，降低心智负担。
- 例 1："采用领域术语重命名类与方法。"
- 例 2："消除过长方法与临时变量。"
- 例 3："按职责拆分模块与文件。"
- 例 4："引入接口与依赖倒置以便测试。"
- 例 5："为关键路径增加日志与注释。"

### 3. 性能与边界（Performance and edges）

- 用户故事：作为维护者，我需要在不改变行为的前提下改进性能与健壮性。
- 例 1："用缓存/惰性计算优化热点。"
- 例 2："增加超时/重试与幂等支持。"
- 例 3："替换不安全 API，补充输入校验。"
- 例 4："分离 I/O 与计算，提升可测试性。"
- 例 5："引入读写分离或批量接口。"

## 原始文件

- [chatmodes/tdd-refactor.chatmode.md](../../../chatmodes/tdd-refactor.chatmode.md)
