## What / When / Why / How

- What: Power Platform MCP 集成专家（自定义连接器 + Copilot Studio）
- When: 需要将连接器与 MCP 协议无缝对接时
- Why: 兼顾平台约束、MCP 规范与企业级安全合规
- How: 设计→Swagger+扩展→认证→MCP 工具/资源→验证→发布/认证

## Key Points

- 连接器：Swagger/x-ms-*；apiDefinition/apiProperties/script.csx
- CLI：paconn/pac；自动化校验与 CI
- 认证：OAuth2（Audience/PKCE/State/Scope 验证）；防 token 透传
- MCP：x-ms-agentic-protocol=mcp-streamable-1.0；JSON-RPC；工具/资源
- 约束：无引用类型；单类型值；资源作为工具输出

## Compact Map

- 架构与文件结构
- 认证与安全
- 协议与模式
- 校验与部署
- 监控与运维

## Example Questions (10+)

- Swagger 需要哪些 x-ms 扩展与约束？
- OAuth2 的 Audience/Scope/State 如何校验？
- 如何消除“困惑副手”与 token 透传风险？
- 工具与资源的 JSON-RPC 流程如何设计？
- Copilot Studio 的约束如何影响 schema？
- CLI 验证失败的常见原因与修复？
- 性能与扩展性考虑有哪些？
- 生产部署与监控如何实施？
- 认证提交所需的材料与检查表？
- 出错处理与用户体验如何优化？

---
Source: d:\mycode\awesome-copilot\chatmodes\power-platform-mcp-integration-expert.chatmode.md
Generated: {{timestamp}}
