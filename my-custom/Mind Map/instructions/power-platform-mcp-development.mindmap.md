## What/When/Why/How
- What: 将 MCP 集成至 Power Platform/ Copilot Studio 的连接器设计
- When: 构建支持工具/资源/提示的智能连接器时
- Why: 兼容 Copilot 约束，提供可靠的代理式调用
- How: Swagger 2.0 + 无 $ref 扁平 schema + JSON-RPC 转换与安全

## Key Points
- 协议：JSON-RPC 2.0；x-ms-agentic-protocol: mcp-streamable-1.0
- Schema：移除 $ref；单一类型；扁平 anyOf/oneOf；自包含
- 安全：OAuth2 多参数集；受众校验；MCP 特定安全头
- 脚本：script.csx 负责 JSON-RPC 转换/错误格式化/令牌校验
- Swagger：operationId 清晰；参数/响应 schema 明确；状态码
- 资源：MIME 声明；受众/优先级注解；可作为工具输出
- 连接参数：枚举化安保级别/版本；默认值/校验
- 日志：认证/校验/转换日志；清晰错误消息

## Compact Map
- Transport: REST↔MCP 转换层
- Auth: OAuth/API Key 参数集
- Schema: 无引用/单类型/自包含
- Testing: 真实 MCP 服务端联调

## Example Questions
1) 所有输入/输出 schema 是否无 $ref 且单一类型？
2) 是否为 Copilot Studio 设置 mcp-streamable-1.0 头？
3) 认证参数集是否支持多场景并验证受众？
4) JSON-RPC 错误是否遵循标准并含上下文？
5) 资源输出是否带正确 MIME 与受众注解？
6) 触发/动作是否区分并给出 x-ms-* 扩展？
7) 是否提供端到端脚本与门户验证步骤？
8) 安全日志是否避免泄露敏感信息？
9) 失败路径是否可重试且具幂等保证？
10) 连接参数是否有默认/校验/提示文本？
11) 是否形成发布与认证（Certification）材料？

Source: d:\mycode\awesome-copilot\instructions\power-platform-mcp-development.instructions.md | Generated: 2025-10-17
