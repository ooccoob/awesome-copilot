---
description: Generate a complete MCP server implementation optimized for Copilot Studio integration with proper schema constraints and streamable HTTP support
agent: agent
---

# 电源平台 MCP 连接器生成器

通过 Microsoft Copilot Studio 的模型上下文协议 (MCP) 集成生成完整的 Power Platform 自定义连接器。此提示将按照具有 MCP 流式 HTTP 支持的 Power Platform 连接器标准创建所有必需的文件。

## 使用说明

创建一个完整的 MCP 服务器实现：

1. **使用 Copilot Studio MCP 模式：**
   - 实施 `x-ms-agentic-protocol: mcp-streamable-1.0`
   - 支持JSON-RPC 2.0通信协议
   - 在 `/mcp` 处提供可流传输的 HTTP 端点
   - 遵循 Power Platform 连接器结构

2. **架构合规性要求：**
   - **工具输入/输出中没有参考类型**（由 Copilot Studio 过滤）
   - **仅限单一类型值**（不是多种类型的数组）
   - **避免枚举输入**（解释为字符串，而不是枚举）
   - 使用基本类型：字符串、数字、整数、布尔值、数组、对象
   - 确保所有端点返回完整的 URI

3. **MCP 组件包括：**
   - **工具**：语言模型调用的函数（✅ Copilot Studio 支持）
   - **资源**：来自工具的类似文件的数据输出（✅ Copilot Studio 支持 - 必须是工具输出才能访问）
   - **提示**：特定任务的预定义模板（❌ Copilot Studio 尚不支持）

4. **实现结构：**
   ```
   /apiDefinition.swagger.json  (Power Platform connector schema)
   /apiProperties.json         (Connector metadata and configuration)
   /script.csx                 (Custom code transformations and logic)
   /server/                    (MCP server implementation)
   /tools/                     (Individual MCP tools)
   /resources/                 (MCP resource handlers)
   ```

## 上下文变量

- **服务器用途**：[描述 MCP 服务器应完成的任务]
- **所需工具**：[要实施的具体工具列表]  
- **资源**：[提供的资源类型]
- **身份验证**：[身份验证方法：无、api-key、oauth2]
- **宿主环境**：[Azure Function、Express.js、FastAPI 等]
- **目标 API**：[要集成的外部 API]

## 预期输出

生成：

1. **apiDefinition.swagger.json** 包含：
   - 正确的 `x-ms-agentic-protocol: mcp-streamable-1.0`
   - MCP 端点位于 POST `/mcp`
   - 兼容的架构定义（无引用类型）
   - McpResponse 和 McpErrorResponse 定义

2. **apiProperties.json** 包含：
   - 连接器元数据和品牌
   - 认证配置
   - 政策模板（如果需要）

3. **script.csx** 包含：
   - 用于请求/响应转换的自定义 C# 代码
   - MCP JSON-RPC 消息处理逻辑
   - 数据验证和处理功能
   - 错误处理和日志记录功能

4. **MCP 服务器代码** 包含：
   - JSON-RPC 2.0 请求处理程序
   - 工具注册和执行
   - 资源管理（作为工具输出）
   - 正确的错误处理
   - Copilot Studio 兼容性检查

5. **个人工具**：
   - 仅接受原始类型输入
   - 返回结构化输出
   - 需要时将资源作为产出
   - 为 Copilot Studio 提供清晰的描述

6. **部署配置**用于：
   - 电源平台环境
   - Copilot Studio 代理集成
   - 测试和验证

## 验证清单

确保生成的代码：
- [ ] 模式中没有引用类型
- [ ] 所有类型字段均为单一类型
- [ ] 通过带有验证的字符串进行枚举处理
- [ ] 通过工具输出可用的资源
- [ ] 完整 URI 端点
- [ ] JSON-RPC 2.0 合规性
- [ ] 正确的 x-ms-agentic-protocol 标头
- [ ] McpResponse/McpErrorResponse 模式
- [ ] Copilot Studio 的清晰工具说明
- [ ] 兼容生成编排

## 用法示例

```yaml
Server Purpose: Customer data management and analysis
Tools Needed: 
  - searchCustomers
  - getCustomerDetails
  - analyzeCustomerTrends
Resources:
  - Customer profiles
  - Analysis reports
Authentication: oauth2
Host Environment: Azure Function
Target APIs: CRM System REST API
```