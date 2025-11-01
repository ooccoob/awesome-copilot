## DDD + .NET 架构最佳实践

- What: 围绕 DDD/SOLID/.NET 的系统构建准则与强制思考流程（分析→校验→计划→实现→复核）。
- When: 设计领域模型/聚合、实现应用/基础设施、制定测试与质量门禁时。
- Why: 提高内聚与一致性，保护领域规则，确保可测试与合规可审计。
- How: 先分析领域/边界/语言→审视 SOLID 与聚合边界→列出改动与测试→再实现并验证质量清单。

### 强制流程
1) 显式领域分析（模式、层、语言、安全）。
2) 设计校验（聚合边界、SRP、规则封装、测试命名、术语一致）。
3) 实施计划（新建/修改文件、事件、接口/类结构、测试清单）。
4) 执行实现（先域后应用，异步与 DI，领域事件解耦，充分测试与文档）。
5) 复核与验证（覆盖率≥85% 领域/应用，性能/安全/合规核对）。

### 分层标准
- Domain: Aggregate/ValueObject/DomainService/DomainEvent/Specification。
- Application: AppService/DTO/输入校验/构造器注入。
- Infrastructure: Repository/EventBus/ORM/外部适配器。
- Testing: 方法_条件_结果 命名；单元/集成/验收分类。

### 质量清单（节选）
- 术语一致、SRP/DIP、规则封装、事件发布/处理、decimal 金额精度、事务边界、审计可追溯、合规（PCI/SOX/LGPD）。

### 示例问题
1) 如何划定聚合边界以保证事务一致性？
2) 何时选 Domain Service 而非 Application Service？
3) 事件风暴输出如何映射为领域事件？
4) Repository 接口如何与 ORM 解耦并保持测试友好？
5) 金额精度/四舍五入策略如何封装到值对象？
6) Saga 与补偿适用场景与实现要点？
7) 覆盖率 85% 的优先级与取舍？
8) 事件溯源与审计的落地方式？
9) Method_Condition_Expected 命名与可读性示例？
10) 跨上下文集成如何保持向后兼容？

Source: d:\mycode\awesome-copilot\instructions\dotnet-architecture-good-practices.instructions.md | Generated: 2025-10-17T00:00:00Z
