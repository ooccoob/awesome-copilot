## Power Platform MCP 自定义连接器套件（思维导图）

- What
  - 生成/校验/排障具备 MCP 集成（Copilot Studio）的自定义连接器
- When
  - 新建、改造或认证前的连接器工程
- Why
  - 保证与 Copilot Studio 代理编排兼容，减少被过滤的工具
- How
  - 核心文件：apiDefinition.swagger.json（含 x-ms-agentic-protocol=mcp-streamable-1.0）/apiProperties.json/script.csx/readme
  - 约束校验：无 $ref、单一 type、资源作为工具输出、完整 URI
  - MCP 端点：POST /mcp，JSON-RPC 2.0 协议
  - 验证与 CLI：paconn validate、pac connector create/update、脚本校验
  - 安全：OAuth 强化、Token 受众校验、CSRF state、防困惑副手、全 HTTPS
  - 认证：图标/元数据/文档/隐私合规

- Key Points (CN/EN)
  - Tools/Resources only (no Prompts)
  - No $ref; single types only
  - JSON-RPC 2.0; Full URIs
  - OAuth hardening; Policy templates

- Example Questions (≥10)
  1) 所有工具输入/输出是否完全去除 $ref 并为单一原生类型？
  2) 资源是否仅作为工具输出暴露？
  3) MCP 端点是否携带 x-ms-agentic-protocol 头？
  4) swagger 是否满足 paconn validate？
  5) script.csx 的 JSON-RPC 处理与错误路径是否完整？
  6) OAuth 重定向与 state 校验是否健壮？
  7) 是否存在类型并集（["string","number"]）等不合规定义？
  8) 所有端点是否为 HTTPS 绝对 URI？
  9) 认证提交需要的图标/元数据是否齐全？
  10) 兼容 Copilot Studio 生成式编排与资源读取路径是否打通？

- Compact Mind Map
  - 文件→约束→端点→验证→安全→认证

- Source: prompts/power-platform-mcp-connector-suite.prompt.md
- Generated: 2025-10-17
