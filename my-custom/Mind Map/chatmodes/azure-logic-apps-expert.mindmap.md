## What / When / Why / How

- What: Azure Logic Apps 专家模式（WDL/集成/企业自动化）
- When: 需要设计/优化/排障 Logic Apps 工作流
- Why: 以最佳实践（性能/成本/弹性/安全/运维）指导方案与实现
- How: 先查官方文档，再给出 JSON/WDL 片段、表达式与模式建议

## Key Points

- 触发器/动作/控制流/表达式/参数/连接/错误处理
- Standard vs Consumption vs ISE 的取舍
- 重试策略、超时、runAfter、异常处理与补偿
- 成本优化：减少动作数、复用连接、并发与阈值
- DevOps：Bicep/ARM、CI/CD、环境参数化、监控

## Compact Map

- 结构
  - triggers/actions/outputs/parameters
  - 控制流：条件/循环/并行/作用域
- 表达式
  - 数据转换、日期/字符串处理
- 连接
  - 身份/机密/网络（VNet/GW）
- 健壮性
  - 重试/超时/异常/死信
- 运维
  - 监控/诊断/告警/成本

## Example Questions (10+)

- 目标是 Standard 还是 Consumption？为什么？
- 该触发器/动作的重试与超时策略如何设置更稳妥？
- 如何减少动作计数以优化成本？
- 复杂表达式（数组映射/合并）的写法示例？
- 失败补偿（回滚/重试）在本场景如何设计？
- 对接私网系统时推荐的网络与身份配置？
- 如何用 Bicep/ARM 参数化并做多环境部署？
- 哪些日志/指标需要接入 Azure Monitor 以便排障？
- 大批量/高并发时的节流与并行策略？
- 常见错误码的诊断路径与应对策略？
- 何时考虑将部分逻辑迁至 Functions？

---
Source: d:\mycode\awesome-copilot\chatmodes\azure-logic-apps-expert.chatmode.md
Generated: {{timestamp}}
