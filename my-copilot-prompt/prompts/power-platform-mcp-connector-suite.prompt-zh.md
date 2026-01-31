---
描述：通过 Copilot Studio 的 MCP 集成生成完整的 Power Platform 自定义连接器 - 包括架构生成、故障排除和验证
代理人：代理人
---

# 电源平台 MCP 连接器套件

通过 Microsoft Copilot Studio 的模型上下文协议集成生成全面的 Power Platform 自定义连接器实现。

## Copilot Studio 中的 MCP 功能

**当前支持：**
- ✅ **工具**：LLM 可以调用的函数（经用户批准）
- ✅ **资源**：代理可以读取的类似文件的数据（必须是工具输出）

**尚不支持：**
- ❌ **提示**：预先编写的模板（为将来的支持做好准备）

## 连接器一代

使用以下命令创建完整的 Power Platform 连接器：

**核心文件：**
- `apiDefinition.swagger.json` 与 `x-ms-agentic-protocol: mcp-streamable-1.0`
- `apiProperties.json` 具有连接器元数据和身份验证
- `script.csx` 具有用于 MCP JSON-RPC 处理的自定义 C# 转换
- `readme.md` 以及连接器文档

**MCP 集成：**
- JSON-RPC 2.0 通信的 POST `/mcp` 端点
- McpResponse 和 McpErrorResponse 架构定义
- Copilot Studio 约束合规性（无参考类型，单一类型）
- 资源集成作为工具输出（支持资源和工具；尚不支持提示）

## 架构验证和故障排除

**验证 Copilot Studio 合规性架构：**
- ✅ 工具输入/输出中没有引用类型 (`$ref`)
- ✅ 仅单一类型值（不是 `["string", "number"]`）
- ✅ 原始类型：字符串、数字、整数、布尔值、数组、对象
- ✅ 资源作为工具输出，而不是单独的实体
- ✅ 所有端点的完整 URI

**常见问题和修复：**
- 过滤工具→删除引用类型，使用基元
- 类型错误 → 具有验证逻辑的单一类型
- 资源不可用 → 包含在工具输出中
- 连接失败 → 验证 `x-ms-agentic-protocol` 标头

## 上下文变量

- **连接器名称**：[连接器的显示名称]
- **服务器用途**：[MCP 服务器应完成的任务]
- **所需工具**：[要实施的 MCP 工具列表]
- **资源**：[提供的资源类型]
- **身份验证**：[无、api-key、oauth2、基本]
- **宿主环境**：[Azure Function、Express.js 等]
- **目标 API**：[要集成的外部 API]

## 生成模式

### 模式 1：全新连接器
从头开始生成新 Power Platform MCP 连接器的所有文件，包括 CLI 验证设置。

### 模式 2：模式验证
使用 paconn 和验证工具分析并修复现有架构以确保 Copilot Studio 合规性。

### 模式3：集成故障排除
使用 CLI 调试工具诊断并解决 Copilot Studio 与 MCP 的集成问题。

### 模式 4：混合连接器
通过适当的验证工作流程将 MCP 功能添加到现有 Power Platform 连接器。

### 模式5：认证准备
准备用于 Microsoft 认证提交的连接器，并具有完整的元数据和验证合规性。

### 模式六：OAuth安全加固
实施通过 MCP 安全最佳实践和高级令牌验证增强的 OAuth 2.0 身份验证。

## 预期输出

**1. apiDefinition.swagger.json**
- 带有 Microsoft 扩展的 Swagger 2.0 格式
- MCP 端点：具有正确协议头的 `POST /mcp`
- 兼容的架构定义（仅限原始类型）
- McpResponse/McpErrorResponse 定义

**2. apiProperties.json**
- 连接器元数据和品牌（需要 `iconBrandColor`）
- 认证配置
- MCP 转换的策略模板

**3.脚本.csx**
- JSON-RPC 2.0 消息处理
- 请求/响应转换
- MCP协议合规逻辑
- 错误处理和验证

**4.实施指南**
- 工具注册和执行模式
- 资源管理策略
- Copilot Studio 集成步骤
- 测试和验证程序

## 验证清单

### 技术合规性
- [ ] MCP 端点中的 `x-ms-agentic-protocol: mcp-streamable-1.0`
- [ ] 任何模式定义中都没有引用类型
- [ ] 所有类型字段都是单一类型（不是数组）
- [ ] 作为工具输出包含的资源
- [ ] script.csx 中的 JSON-RPC 2.0 合规性
- [ ] 贯穿全文的完整 URI 端点
- [ ] Copilot Studio 代理的清晰描述
- [ ] 身份验证已正确配置
- [ ] MCP 转型的政策模板
- [ ] 生成编排兼容性

### CLI 验证
- [ ] **paconn validate**：`paconn validate --api-def apiDefinition.swagger.json` 通过，没有错误
- [ ] **pac CLI 就绪**：可以使用 `pac connector create/update` 创建/更新连接器
- [ ] **脚本验证**：script.csx 在 pac CLI 上传期间通过自动验证
- [ ] **包验证**：`ConnectorPackageValidator.ps1` 运行成功

### OAuth 和安全要求
- [ ] **OAuth 2.0 增强版**：标准 OAuth 2.0 与 MCP 安全最佳实践实施
- [ ] **令牌验证**：实施令牌受众验证以防止直通攻击
- [ ] **自定义安全逻辑**：增强 script.csx 中的 MCP 合规性验证
- [ ] **状态参数保护**：用于防止 CSRF 的安全状态参数
- [ ] **HTTPS 强制**：所有生产端点仅使用 HTTPS
- [ ] **MCP 安全实践**：在 OAuth 2.0 中实施混淆代理攻击预防

### 认证要求
- [ ] **完整元数据**：包含产品和服务信息的settings.json
- [ ] **图标合规性**：PNG 格式，230x230 或 500x500 尺寸
- [ ] **文档**：带有全面示例的认证就绪自述文件
- [ ] **安全合规性**：通过 MCP 安全实践、隐私政策增强 OAuth 2.0
- [ ] **身份验证流程**：具有正确配置的自定义安全验证的 OAuth 2.0

## 用法示例

```yaml
Mode: Complete New Connector
Connector Name: Customer Analytics MCP
Server Purpose: Customer data analysis and insights
Tools Needed:
  - searchCustomers: Find customers by criteria
  - getCustomerProfile: Retrieve detailed customer data
  - analyzeCustomerTrends: Generate trend analysis
Resources:
  - Customer profiles (JSON data)
  - Analysis reports (structured data)
Authentication: oauth2
Host Environment: Azure Function
Target APIs: CRM REST API
```