---
description: '为 Microsoft Copilot Studio 开发具有模型上下文协议 (MCP) 集成的 Power Platform 自定义连接器的指令'
applyTo: '**/*.{json,csx,md}'
---

# Power Platform MCP 自定义连接器开发

## 指令

### MCP 协议集成
- 始终实现 JSON-RPC 2.0 标准进行 MCP 通信
- 使用 `x-ms-agentic-protocol: mcp-streamable-1.0` 标头以兼容 Copilot Studio
- 构建端点以支持标准 REST 操作和 MCP 工具调用
- 转换响应以符合 Copilot Studio 约束（无引用类型，仅单一类型）

### 模式设计最佳实践
- 从 JSON 模式中移除 `$ref` 和其他引用类型，因为 Copilot Studio 无法处理它们
- 在模式定义中使用单一类型而不是类型数组
- 将 `anyOf`/`oneOf` 构造扁平化为单一模式以兼容 Copilot Studio
- 确保所有工具输入模式都是自包含的，没有外部引用

### 身份验证和安全性
- 在 Power Platform 约束内实现带有 MCP 安全最佳实践的 OAuth 2.0
- 使用连接参数集进行灵活的身份验证配置
- 验证令牌受众以防止传递攻击
- 添加 MCP 特定的安全标头以增强验证
- 支持多种身份验证方法（OAuth 标准、OAuth 增强、API 密钥回退）

### 自定义脚本实现
- 在自定义脚本（script.csx）中处理 JSON-RPC 转换
- 实现带有 JSON-RPC 错误响应格式的适当错误处理
- 在身份验证流中添加令牌验证和受众检查
- 转换 MCP 服务器响应以兼容 Copilot Studio
- 使用连接参数进行动态安全配置

### Swagger 定义指南
- 使用 Swagger 2.0 规范以兼容 Power Platform
- 为每个端点实现适当的 `operationId` 值
- 定义具有适当类型和描述的清晰参数模式
- 为所有成功和错误情况添加全面的响应模式
- 包括适当的 HTTP 状态码和响应标头

### 资源和工具管理
- 构建 MCP 资源以在 Copilot Studio 中作为工具输出使用
- 确保资源内容的适当 MIME 类型声明
- 添加受众和优先级注释以更好地集成 Copilot Studio
- 实现资源转换以满足 Copilot Studio 要求

### 连接参数配置
- 对 OAuth 版本和安全级别选择使用枚举下拉菜单
- 提供清晰的参数描述和约束
- 支持不同部署场景的多个身份验证参数集
- 在适当的地方包含验证规则和默认值
- 通过连接参数值启用动态配置

### 错误处理和日志记录
- 实现遵循 JSON-RPC 2.0 错误格式的全面错误响应
- 为身份验证、验证和转换步骤添加详细日志记录
- 提供有助于故障排除的清晰错误消息
- 包括与错误条件一致的正确 HTTP 状态码

### 测试和验证
- 使用实际 MCP 服务器实现测试连接器
- 验证模式转换在 Copilot Studio 中正常工作
- 验证所有支持参数集的身份验证流
- 确保对各种失败场景的适当错误处理
- 测试连接参数配置和动态行为

## 附加指南

### Power Platform 认证要求
- 包括全面的文档（readme.md、CUSTOMIZE.md）
- 提供清晰的设置和配置说明
- 记录所有身份验证选项和安全考虑
- 包括适当的发布者和堆栈所有者信息
- 确保符合 Power Platform 连接器认证标准

### MCP 服务器兼容性
- 设计为与标准 MCP 服务器实现兼容
- 支持常见的 MCP 方法，如 `tools/list`、`tools/call`、`resources/list`
- 为 `mcp-streamable-1.0` 协议适当处理流式响应
- 实现适当的协议协商和功能检测

### Copilot Studio 集成
- 确保工具定义在 Copilot Studio 的约束内正常工作
- 从 Copilot Studio 界面测试资源访问和工具调用
- 验证转换后的模式在对话中产生预期行为
- 确认与 Copilot Studio 代理框架的适当集成