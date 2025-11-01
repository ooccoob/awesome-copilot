## What / When / Why / How

- What: TDD Refactor（保持全绿下的质量/安全/设计提升）
- When: Green 后清理设计并强化安全
- Why: 降复杂、去重复、提升可维护与合规
- How: 小步重构→频繁跑测→安全清单→记录设计决策与债务

## Key Points

- 质量：命名/SRP/SOLID；降低圈复杂度
- 安全：输入校验/授权/加密/异常信息最小化/依赖扫描/Secret 管理
- 设计：DI、配置外置、结构化日志、性能优化
- Issue：验收复核、状态更新、后续债务登记

## Compact Map

- 复核→重构→安全→性能→记录→关闭/建债

## Example Questions (10+)

- 哪些重复与异味最影响维护？
- 安全基线是否满足（注入/XSS/Secrets 等）？
- 性能热点与改进点？
- 设计模式的引入是否有必要？
- 配置与日志是否达标？
- 依赖是否存在漏洞？
- 全部测试是否保持绿色？
- 验收与文档是否更新？
- 需要创建哪些后续 Issues？
- 是否影响部署与监控？

---
Source: d:\mycode\awesome-copilot\chatmodes\tdd-refactor.chatmode.md
Generated: {{timestamp}}
