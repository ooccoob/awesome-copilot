## What
- 使用 Jest 编写 JS/TS 测试的结构与常用模式：组织、Mock、异步、快照、React 组件与常用断言。

## When
- 为函数/组件/模块编写单测与集成测试，需统一结构与最佳实践时。

## Why
- 提升可读性与稳定性，隔离外部依赖，聚焦行为。

## How
- 结构：*.test.(ts|js)；邻近或 __tests__；describe/it 分层
- Mock：jest.mock / jest.spyOn / mockImplementation；afterEach resetAllMocks
- 异步：async/await；resolves/rejects；必要时 setTimeout
- 快照：小而稳；审慎更新
- React：RTL；以用户行为与可访问性为先；userEvent
- 断言：基本/数组/对象/异常/Mock 调用

## Key points (CN)
- 独立可重复；单一行为；清晰命名
- 以 AAA 模式组织
- 对外部依赖统一 Mock 策略

## Key points (EN)
- Co-located tests; descriptive names
- Effective mocking; async patterns; RTL-first
- Rich matchers and mock verifications

## Example questions
- “为该 hooks 编写包含异步请求的单测？”
- “如何对模块内函数使用 spyOn 定向 Mock？”

## 思维导图（要点）
- 结构/命名
- Mock/异步/快照
- RTL 与断言

—
- Source: d:\mycode\awesome-copilot\prompts\javascript-typescript-jest.prompt.md
- Generated: 2025-10-17
