---
description: 为Copilot Studio生成完整的Power Platform自定义连接器，包含MCP集成 - 包括模式生成、故障排除和验证
mode: agent
---

# Power Platform MCP连接器套件

生成完整的Power Platform自定义连接器实现，为Microsoft Copilot Studio集成模型上下文协议（MCP）。

## Copilot Studio中的MCP功能

**当前支持：**
- ✅ **工具**：LLM可以调用的函数（需要用户批准）
- ✅ **资源**：代理可以读取的类文件数据（必须是工具输出）

**尚不支持：**
- ❌ **提示**：预写模板（为将来支持做准备）

## 连接器生成

创建完整的Power Platform连接器，包含：

**核心文件：**
- `apiDefinition.swagger.json`，包含`x-ms-agentic-protocol: mcp-streamable-1.0`
- `apiProperties.json`，包含连接器元数据和身份验证
- `script.csx`，用于MCP JSON-RPC处理的自定义C#转换
- `readme.md`，包含连接器文档

**MCP集成：**
- 用于JSON-RPC 2.0通信的POST `/mcp`端点
- McpResponse和McpErrorResponse模式定义
- Copilot Studio约束合规性（无引用类型，单一类型）
- 资源作为工具输出集成（支持资源和工具；提示尚不支持）

## 模式验证和故障排除

**验证Copilot Studio合规性的模式：**
- ✅ 工具输入/输出中无引用类型（`$ref`）
- ✅ 仅单一类型值（不是`["string", "number"]`）
- ✅ 原语类型：string、number、integer、boolean、array、object
- ✅ 资源作为工具输出，而非独立实体
- ✅ 所有端点的完整URI

**常见问题和修复：**
- 工具被过滤 → 删除引用类型，使用原语
- 类型错误 → 使用验证逻辑的单一类型
- 资源不可用 → 包含在工具输出中
- 连接失败 → 验证`x-ms-agentic-protocol`头

## 上下文变量

- **连接器名称**：[连接器的显示名称]
- **服务器目的**：[MCP服务器应该完成什么]
- **所需工具**：[要实现的MCP工具列表]
- **资源**：[要提供的资源类型]
- **身份验证**：[none、api-key、oauth2、basic]
- **主机环境**：[Azure Function、Express.js等]
- **目标API**：[要集成的外部API]

## 生成模式

### 模式1：全新连接器
从零开始为新的Power Platform MCP连接器生成所有文件，包括CLI验证设置。

### 模式2：模式验证
使用paconn和验证工具分析和修复现有模式的Copilot Studio合规性。

### 模式3：集成故障排除
使用CLI调试工具诊断和解决与Copilot Studio的MCP集成问题。

### 模式4：混合连接器
使用适当的验证工作流程为现有Power Platform连接器添加MCP功能。

### 模式5：认证准备
准备连接器以提交Microsoft认证，包含完整元数据和验证合规性。

### 模式6：OAuth安全加固
实施OAuth 2.0身份验证，增强MCP安全最佳实践和高级令牌验证。

## 预期输出

**1. apiDefinition.swagger.json**
- 具有Microsoft扩展的Swagger 2.0格式
- MCP端点：`POST /mcp`，具有适当的协议头
- 合规的模式定义（仅原语类型）
- McpResponse/McpErrorResponse定义

**2. apiProperties.json**
- 连接器元数据和品牌（`iconBrandColor`必需）
- 身份验证配置
- MCP转换的策略模板

**3. script.csx**
- JSON-RPC 2.0消息处理
- 请求/响应转换
- MCP协议合规逻辑
- 错误处理和验证

**4. 实施指导**
- 工具注册和执行模式
- 资源管理策略
- Copilot Studio集成步骤
- 测试和验证程序

## 验证清单

### 技术合规性
- [ ] MCP端点中的`x-ms-agentic-protocol: mcp-streamable-1.0`
- [ ] 任何模式定义中无引用类型
- [ ] 所有类型字段都是单一类型（不是数组）
- [ ] 资源作为工具输出包含
- [ ] script.csx中的JSON-RPC 2.0合规性
- [ ] 全程完整URI端点
- [ ] 为Copilot Studio代理提供清晰描述
- [ ] 正确配置身份验证
- [ ] MCP转换的策略模板
- [ ] 生成编排兼容性

### CLI验证
- [ ] **paconn validate**：`paconn validate --api-def apiDefinition.swagger.json`通过无错误
- [ ] **pac CLI就绪**：可以使用`pac connector create/update`创建/更新连接器
- [ ] **脚本验证**：script.csx在pac CLI上传期间通过自动验证
- [ ] **包验证**：`ConnectorPackageValidator.ps1`成功运行

### OAuth和安全要求
- [ ] **OAuth 2.0增强**：标准OAuth 2.0与MCP安全最佳实践实施
- [ ] **令牌验证**：实施令牌受众验证以防止传递攻击
- [ ] **自定义安全逻辑**：script.csx中用于MCP合规性的增强验证
- [ ] **状态参数保护**：用于CSRF预防的安全状态参数
- [ ] **HTTPS强制**：所有生产端点仅使用HTTPS
- [ ] **MCP安全实践**：在OAuth 2.0内实施困惑代理攻击预防

### 认证要求
- [ ] **完整元数据**：settings.json，包含产品和服务信息
- [ ] **图标合规性**：PNG格式，230x230或500x500尺寸
- [ ] **文档**：认证就绪的readme，包含全面示例
- [ ] **安全合规性**：OAuth 2.0增强MCP安全实践，隐私政策
- [ ] **身份验证流程**：OAuth 2.0与自定义安全验证正确配置

## 示例用法

```yaml
模式：全新连接器
连接器名称：客户分析MCP
服务器目的：客户数据分析和洞察
所需工具：
  - searchCustomers：按条件查找客户
  - getCustomerProfile：检索详细客户数据
  - analyzeCustomerTrends：生成趋势分析
资源：
  - 客户档案（JSON数据）
  - 分析报告（结构化数据）
身份验证：oauth2
主机环境：Azure Function
目标API：CRM REST API
```