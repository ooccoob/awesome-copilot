---
description: 生成针对Copilot Studio集成优化的完整MCP服务器实现，包含正确的模式约束和可流式HTTP支持
mode: agent
---

# Power Platform MCP连接器生成器

生成一个带有Microsoft Copilot Studio模型上下文协议（MCP）集成的完整Power Platform自定义连接器。此提示按照Power Platform连接器标准创建所有必要文件，并支持MCP可流式HTTP。

## 指令

创建一个完整的MCP服务器实现，要求：

1. **使用Copilot Studio MCP模式**：
   - 实现`x-ms-agentic-protocol: mcp-streamable-1.0`
   - 支持JSON-RPC 2.0通信协议
   - 在`/mcp`提供可流式HTTP端点
   - 遵循Power Platform连接器结构

2. **模式合规要求**：
   - **工具输入/输出中无引用类型**（被Copilot Studio过滤）
   - **仅单一类型值**（不是多种类型的数组）
   - **避免枚举输入**（被解释为字符串，不是枚举）
   - 使用原始类型：string、number、integer、boolean、array、object
   - 确保所有端点返回完整URI

3. **要包含的MCP组件**：
   - **工具**：供语言模型调用的函数（✅ 在Copilot Studio中支持）
   - **资源**：来自工具的文件类数据输出（✅ 在Copilot Studio中支持 - 必须作为工具输出才能访问）
   - **提示**：特定任务的预定义模板（❌ 尚未在Copilot Studio中支持）

4. **实现结构**：
   ```
   /apiDefinition.swagger.json  (Power Platform连接器模式)
   /apiProperties.json         (连接器元数据和配置)
   /script.csx                 (自定义代码转换和逻辑)
   /server/                    (MCP服务器实现)
   /tools/                     (各个MCP工具)
   /resources/                 (MCP资源处理器)
   ```

## 上下文变量

- **服务器目的**：[描述MCP服务器应该完成什么]
- **所需工具**：[要实现的特定工具列表]
- **资源**：[要提供的资源类型]
- **身份验证**：[身份验证方法：none、api-key、oauth2]
- **主机环境**：[Azure Function、Express.js、FastAPI等]
- **目标API**：[要集成的外部API]

## 预期输出

生成：

1. **apiDefinition.swagger.json**，包含：
   - 正确的`x-ms-agentic-protocol: mcp-streamable-1.0`
   - 在POST `/mcp`的MCP端点
   - 合规的模式定义（无引用类型）
   - McpResponse和McpErrorResponse定义

2. **apiProperties.json**，包含：
   - 连接器元数据和品牌
   - 身份验证配置
   - 策略模板（如果需要）

3. **script.csx**，包含：
   - 自定义C#代码用于请求/响应转换
   - MCP JSON-RPC消息处理逻辑
   - 数据验证和处理函数
   - 错误处理和日志记录能力

4. **MCP服务器代码**，包含：
   - JSON-RPC 2.0请求处理器
   - 工具注册和执行
   - 资源管理（作为工具输出）
   - 正确的错误处理
   - Copilot Studio兼容性检查

5. **各个工具**，要求：
   - 仅接受原始类型输入
   - 返回结构化输出
   - 在需要时将资源作为输出包含
   - 为Copilot Studio提供清晰的描述

6. **部署配置**，用于：
   - Power Platform环境
   - Copilot Studio代理集成
   - 测试和验证

## 验证检查清单

确保生成的代码：
- [ ] 模式中无引用类型
- [ ] 所有类型字段都是单一类型
- [ ] 通过字符串验证处理枚举
- [ ] 资源通过工具输出可用
- [ ] 完整URI端点
- [ ] JSON-RPC 2.0合规
- [ ] 正确的x-ms-agentic-protocol标头
- [ ] McpResponse/McpErrorResponse模式
- [ ] 为Copilot Studio提供清晰的工具描述
- [ ] 生成编排兼容

## 示例用法

```yaml
Server Purpose: 客户数据管理和分析
Tools Needed:
  - searchCustomers
  - getCustomerDetails
  - analyzeCustomerTrends
Resources:
  - 客户档案
  - 分析报告
Authentication: oauth2
Host Environment: Azure Function
Target APIs: CRM系统REST API
```