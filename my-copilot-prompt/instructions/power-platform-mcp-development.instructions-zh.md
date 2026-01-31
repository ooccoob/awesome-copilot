---
描述：“针对 Microsoft Copilot Studio 开发具有模型上下文协议 (MCP) 集成的 Power Platform 自定义连接器的说明”
applyTo: '**/*.{json,csx,md}'
---

# 电源平台 MCP 定制连接器开发

## 使用说明

### MCP协议集成
- 始终为 MCP 通信实施 JSON-RPC 2.0 标准
- 使用 `x-ms-agentic-protocol: mcp-streamable-1.0` 标头实现 Copilot Studio 兼容性
- 构建端点以支持标准 REST 操作和 MCP 工具调用
- 转换响应以符合 Copilot Studio 约束（无参考类型，仅限单一类型）

### 架构设计最佳实践
- 从 JSON 架构中删除 `$ref` 和其他引用类型，因为 Copilot Studio 无法处理它们
- 在模式定义中使用单一类型而不是类型数组
- 将 `anyOf`/`oneOf` 构造展平为单一架构，以实现 Copilot Studio 兼容性
- 确保所有工具输入模式都是独立的，无需外部引用

### 身份验证和安全
- 在 Power Platform 限制范围内使用 MCP 安全最佳实践实施 OAuth 2.0
- 使用连接参数集进行灵活的身份验证配置
- 验证令牌受众以防止直通攻击
- 添加 MCP 特定的安全标头以增强验证
- 支持多种身份验证方法（OAuth 标准、OAuth 增强、API 密钥回退）

### 自定义脚本实现
- 在自定义脚本 (script.csx) 中处理 JSON-RPC 转换
- 使用 JSON-RPC 错误响应格式实施正确的错误处理
- 在身份验证流程中添加令牌验证和受众检查
- 转换 MCP 服务器响应以实现 Copilot Studio 兼容性
- 使用连接参数进行动态安全配置

### Swagger 定义指南
- 使用 Swagger 2.0 规范实现 Power Platform 兼容性
- 为每个端点实现正确的 `operationId` 值
- 使用适当的类型和描述定义清晰的参数模式
- 为所有成功和错误案例添加全面的响应模式
- 包含正确的 HTTP 状态代码和响应标头

### 资源和工具管理
- 将 MCP 资源构建为可在 Copilot Studio 中作为工具输出使用
- 确保资源内容的 MIME 类型声明正确
- 添加受众和优先级注释以实现更好的 Copilot Studio 集成
- 实施资源转型以满足 Copilot Studio 要求

### 连接参数配置
- 使用枚举下拉菜单进行 OAuth 版本和安全级别选择
- 提供清晰的参数描述和约束
- 支持多种认证参数集，适合不同的部署场景
- 在适当的情况下包括验证规则和默认值
- 通过连接参数值启用动态配置

### 错误处理和日志记录
- 按照 JSON-RPC 2.0 错误格式实现全面的错误响应
- 添加身份验证、验证和转换步骤的详细日志记录
- 提供清晰的错误消息以帮助排除故障
- 包含与错误条件一致的正确 HTTP 状态代码

### 测试和验证
- 使用实际 MCP 服务器实现测试连接器
- 使用 Copilot Studio 验证架构转换是否正常工作
- 验证所有支持的参数集的身份验证流程
- 确保对各种故障场景进行正确的错误处理
- 测试连接参数配置和动态行为

## 附加指南

### 电源平台认证要求
- 包括综合文档（readme.md、CUSTOMIZE.md）
- 提供清晰的设置和配置说明
- 记录所有身份验证选项和安全注意事项
- 包括正确的发布者和堆栈所有者信息
- 确保符合 Power Platform 连接器认证标准

### MCP 服务器兼容性
- 设计与标准 MCP 服务器实现兼容
- 支持常见的MCP方法，如`tools/list`、`tools/call`、`resources/list`
- 适当处理 `mcp-streamable-1.0` 协议的流响应
- 实施适当的协议协商和能力检测

### 副驾驶工作室集成
- 确保工具定义在 Copilot Studio 的限制范围内正常工作
- 从 Copilot Studio 界面测试资源访问和工具调用
- 验证转换后的模式是否在对话中产生预期的行为
- 确认与 Copilot Studio 代理框架的正确集成