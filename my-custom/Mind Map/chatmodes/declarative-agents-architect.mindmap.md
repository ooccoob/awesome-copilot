## What / When / Why / How

- What: Microsoft 365 Declarative Agent 架构师（v1.5、TypeSpec、Toolkit）
- When: 需要设计/实现企业级 M365 Declarative Agent
- Why: 在能力/限制内交付合规、可测、可部署的 Agent
- How: 明确业务→选能力（≤5）→TypeSpec/JSON→Playground 验证→部署与监控

## Key Points

- 能力清单（11 项）与配额/限制（名称/描述/指令字数/数组上限）
- 选型：TypeSpec 开发或直接 JSON
- VS Code Toolkit 与本地 Playground 调试
- 生产：环境/变量/部署/监控/性能
- 质量：验证 v1.5 约束、字符/数组限制、国际化

## Compact Map

- 需求澄清（角色/场景/合规）
- 能力组合与权衡
- 类型/清单实现（TypeSpec/JSON）
- 本地验证与测试
- 部署与运维

## Example Questions (10+)

- 业务目标与主要用户画像是什么？
- 需要哪些能力组合（≤5）才能达成最小可行？
- 名称/描述/指令的字符限制如何满足？
- 选择 TypeSpec 还是手写 JSON？为什么？
- 对话起始与行为覆盖如何设计？
- 本地调试/验证流程如何组织？
- 部署环境隔离（dev/stage/prod）如何管理？
- 监控/日志/指标如何集成？
- 性能与延迟的瓶颈在哪里，如何优化？
- 多语言/本地化如何实现？
- 安全与权限边界如何限制？

---
Source: d:\mycode\awesome-copilot\chatmodes\declarative-agents-architect.chatmode.md
Generated: {{timestamp}}
