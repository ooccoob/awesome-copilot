## What / When / Why / How

- What: 规划模式（仅生成实现计划，不直接改代码）
- When: 新功能/重构前需要清晰的实施路线
- Why: 降低风险、明确范围、保证可测试与可交付
- How: 按模板输出 Markdown 计划：概述/需求/步骤/测试

## Key Points

- 只产出计划文档，不执行改动
- 结构固定：Overview/Requirements/Implementation Steps/Testing
- 用条目化、可执行的步骤，保持可验证
- 可结合工具检索代码与现状，但结果体现在计划中

## Compact Map

- 目标→范围→拆解步骤→测试设计
- 清单式计划→可追踪 →便于评审

## Example Questions (10+)

- 功能/重构的业务目标与边界是什么？
- 涉及哪些模块与公共依赖？
- 需要的数据和接口变更点在哪里？
- 里程碑如何划分，怎样并行推进？
- 回滚策略与兼容性要求是什么？
- 风险与前置条件清单？
- 每一步的可验证产出是什么？
- 测试范围包含哪些单测/集成/端到端？
- 需要哪些观测点与日志变更？
- 成功标准与退出条件如何度量？

---
Source: d:\mycode\awesome-copilot\chatmodes\planner.chatmode.md
Generated: {{timestamp}}
