## What/When/Why/How
- What: Java 基线开发规范与最佳实践（命名、异常、日志、测试、接口、性能、安全等）。
- When: 新建/重构 Java 模块或进行代码评审时。
- Why: 提升可维护性、可靠性与一致性，降低技术债与安全风险。
- How: 依据规范实现/评审，配套自动化构建与静态检查。

## Key Points
- 命名：包小写、类 PascalCase、方法/变量 camelCase、常量 UPPER_SNAKE_CASE。
- 语法/特性：Record、模式匹配、var 合理使用；不可变优先；Streams/Lambdas。
- 代码异味：参数过多、重复代码、方法过长、认知复杂度、魔法数、空catch等。
- Bug模式：资源关闭、== 比较对象、冗余转换、恒真条件、不可达代码。
- 异常：Javadoc 注释，统一业务异常，边界记录一次，禁止吞异常。
- 日志：SLF4J 参数化、上下文但不含敏感信息；debug 开关防损耗。
- 安全：JSR-303 校验，参数化SQL，XSS/CSRF/SSRF防护，凭证不硬编码。
- 测试：AIR 原则，最小 happy + 边界用例，尽量 mock 外部依赖。
- 性能：批量/分页、只查所需字段、缓存与过期策略、避免循环外部访问。

## Compact Map
Baseline
- Naming/Style
- Immutability/Streams/Pattern matching
- Exceptions/Logging
- Security/Validation/SQL
- Testing/CI
- Performance/DB

## Review Checklist
- [ ] 资源关闭与异常仅记录一次
- [ ] 命名与分层合理、职责单一
- [ ] 入参校验与SQL参数化
- [ ] 日志脱敏与级别恰当
- [ ] 单测覆盖关键路径与边界
- [ ] 复杂逻辑拆分降低复杂度

## Example Questions (≥10)
- 怎样将数据类改为 Record 并保持兼容？
- 何时使用 Optional 替代 null？
- 如何降低方法的认知复杂度（S3776）？
- try-with-resources 的最佳实践是什么？
- 参数过多时如何用 Builder/值对象重构？
- 如何统一异常处理并避免重复日志？
- 在 MyBatis 中如何避免 N+1 查询？
- 如何设计统一返回体与分页结构？
- 日志中如何做到上下文充分但不泄露敏感信息？
- 性能优化的首要三步是什么？

Source: d:\mycode\awesome-copilot\instructions\java.instructions.md | Generated: 2025-10-17
