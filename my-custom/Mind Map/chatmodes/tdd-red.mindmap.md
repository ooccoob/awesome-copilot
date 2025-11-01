## What / When / Why / How

- What: TDD Red（先写失败测试，来自 Issue 行为约束）
- When: 开始实现前，用测试描述期望行为
- Why: 驱动设计，锁定范围，避免偏航
- How: 获取 Issue→分析需求→写单一失败测试→验证失败原因正确

## Key Points

- 规范：描述性命名+AAA；单断言聚焦
- 工具：xUnit/FluentAssertions/AutoFixture/Theory
- 连接 Issue：分支号/测试名关联

## Compact Map

- 取 Issue→分解行为→首个失败测试→确认失败

## Example Questions (10+)

- 从 Issue 提炼的首个可测行为？
- 失败是否因缺实现而非语法错误？
- 边界案例与多输入 Theory？
- 测试命名是否表达业务语义？
- 何时添加更多测试迫使泛化？
- 数据构造与隔离策略？
- 与已有测试的冲突？
- 需要哪些桩或替身？
- 如何链接回 Issue 追踪？
- 通过后进入 Green 的条件？

---
Source: d:\mycode\awesome-copilot\chatmodes\tdd-red.chatmode.md
Generated: {{timestamp}}
