## What
- 生成符合 Power Platform 自定义连接器与 Copilot Studio 集成的 MCP 服务与清单（swagger、apiProperties、脚本与工具）。

## When to use
- 需要在 Copilot Studio 中以 mcp-streamable-1.0 模式集成自定义工具与资源输出。

## Why it matters
- 严格的架构/协议限制（无引用类型、单一类型字段、全 URI）避免发布/校验失败并提升可用性。

## How (关键流程)
- 协议：x-ms-agentic-protocol: mcp-streamable-1.0，JSON-RPC 2.0，经 /mcp 端点
- 清单：apiDefinition.swagger.json + apiProperties.json（认证/品牌/策略）
- 代码：script.csx 处理转换/校验/日志；server + tools + resources 目录
- 约束：工具输入输出仅用基础类型；资源通过工具返回；避免 enum/引用类型
- 校验：McpResponse/McpErrorResponse；返回完整 URI；兼容生成式编排

## Example questions (≥10)
1. 生成完整 swagger 与 apiProperties 示例，包含 OAuth2 配置与 /mcp POST 定义。
2. 在 script.csx 中实现 JSON-RPC 解析、错误包装与日志记录的最小示例。
3. 设计一个 searchCustomers 工具的输入/输出 schema（仅基本类型）与资源返回策略。
4. 如何在工具输出中附带下载报告的资源 URI？请给示例。
5. 列出“被 Copilot Studio 过滤/不支持”的 schema 模式与规避方式。
6. 提供本地调试方案：使用 ngrok/Functions 本地运行并在 Copilot Studio 验证。
7. 给出生成式编排兼容性检查清单（header、响应结构、错误码）。
8. 提供自动化校验脚本，检测是否出现引用类型/多类型字段/enum 输入。
9. 如何分层目录与命名，便于多工具扩展与 CI 校验？
10. 生成 CI Workflow：lint swagger、跑 csx 单元测试、打包部署连接器。

## Key points
- CN: 协议严格、基础类型限定、资源经工具返回、全 URI、自动校验
- EN: Protocol strictness, primitive-only schemas, resources via tools, full URIs, automated validation

## Mind map (简要)
- 目标: Copilot Studio MCP
  - 协议/端点
  - 清单/属性
  - 脚本/服务器/工具
  - 约束与校验
  - 调试与部署

---
Source file: d:\mycode\awesome-copilot\prompts\mcp-copilot-studio-server-generator.prompt.md
Generated: 2025-10-17T00:00:00Z
