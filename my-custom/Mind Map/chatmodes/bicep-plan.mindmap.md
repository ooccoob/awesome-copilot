## What / When / Why / How

- What: Azure Bicep 基础设施实现规划（仅产出规划文档，不做部署流程）
- When: 在编码前需要一个可执行、可追踪的 Bicep 资源实现蓝图
- Why: 明确资源、参数、依赖与输出，降本增效并降低返工
- How: 基于 MS Docs 与 AVM 校验→输出 INFRA.{goal}.md（机器可读、确定性）

## Key Points

- 写作边界：仅写 .bicep-planning-files/ 下文件，其他不改
- 结构：Resources 清单（AVM/Raw、参数、输出、依赖、引用）+ 分阶段实施计划
- 资料：始终查阅 MS Docs；优先 AVM，若无则 Raw + 明确 API 版本
- 网络/架构：可生成总览与网络图以辅助沟通
- 工具：todos 跟踪子任务，fetch 获取变更日志与模块版本

## Compact Map

- 目标
  - goal 与约束明确
- 资源
  - AVM or Raw + apiVersion
  - 参数/输出/依赖/引用
- 阶段
  - Phase 1..n 任务表（TASK-001..）
- 校验
  - 文档链接、版本锚定

## Example Questions (10+)

- 哪些资源使用 AVM，哪些必须 Raw？API 版本如何确定？
- 资源间依赖关系与部署顺序是什么？
- 需要暴露哪些 outputs 给上游/下游模块？
- 参数最小集合与默认值如何设计以支持多环境？
- 日志诊断/策略合规项需要怎样在计划中体现？
- 私网/专线/VNet/PE 的网络设计如何在计划中表达？
- 成本敏感资源（数据库、网络设备）有哪些配额与地区限制？
- 有哪些必须 pin 版本的模块/提供者？
- 哪些风险与回滚策略应提前写入？
- 目标 INFRA.{goal}.md 的成功校验标准是什么？
- 参考文档与变更日志链接有哪些？

---
Source: d:\mycode\awesome-copilot\chatmodes\bicep-plan.chatmode.md
Generated: {{timestamp}}
