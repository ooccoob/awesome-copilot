---
description: Microsoft 365 Copilot声明式代理的综合开发指南，包含schema v1.5、TypeSpec集成和Microsoft 365 Agents Toolkit工作流程
applyTo: "**.json, **.ts, **.tsp, **manifest.json, **agent.json, **declarative-agent.json"
---

# Microsoft 365 声明式代理开发指南

## 概述

Microsoft 365 Copilot声明式代理是强大的自定义AI助手，它们通过专门功能、企业数据访问和自定义行为来扩展Microsoft 365 Copilot。这些指南为使用最新的v1.5 JSON架构规范创建生产就绪的代理提供全面的开发实践，完全集成Microsoft 365 Agents Toolkit。

## 架构规范 v1.5

### 核心属性

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/copilot/declarative-agent/v1.5/schema.json",
  "version": "v1.5",
  "name": "字符串（最大100字符）",
  "description": "字符串（最大1000字符）",
  "instructions": "字符串（最大8000字符）",
  "capabilities": ["数组（最大5项）"],
  "conversation_starters": ["数组（最大4项，可选）"]
}
```

### 字符限制和约束
- **名称**: 最大100字符，必需
- **描述**: 最大1000字符，必需
- **指令**: 最大8000字符，必需
- **功能**: 最大5项，最少1项
- **对话开场白**: 最大4项，可选

## 可用功能

### 核心功能
1. **WebSearch**: 互联网搜索和实时信息访问
2. **OneDriveAndSharePoint**: 文件访问、文档搜索、内容管理
3. **GraphConnectors**: 来自第三方系统的企业数据集成
4. **MicrosoftGraph**: 访问Microsoft 365服务和数据

### 通信和协作
5. **TeamsAndOutlook**: Teams聊天、会议、邮件集成
6. **CopilotForMicrosoft365**: 高级Copilot功能和工作流程

### 业务应用程序
7. **PowerPlatform**: Power Apps、Power Automate、Power BI集成
8. **BusinessDataProcessing**: 高级数据处理和分析
9. **WordAndExcel**: 文档创建、编辑、分析
10. **EnterpriseApplications**: 第三方业务系统集成
11. **CustomConnectors**: 自定义API和服务集成

## Microsoft 365 Agents Toolkit集成

### VS Code扩展设置
```bash
# 安装Microsoft 365 Agents Toolkit
# 扩展ID: teamsdevapp.ms-teams-vscode-extension
```

### TypeSpec开发工作流程

#### 1. 现代代理定义
```typespec
import "@typespec/json-schema";

using TypeSpec.JsonSchema;

@jsonSchema("/schemas/declarative-agent/v1.5/schema.json")
namespace DeclarativeAgent;

/** Microsoft 365 声明式代理 */
model Agent {
  /** 架构版本 */
  @minLength(1)
  $schema: "https://developer.microsoft.com/json-schemas/copilot/declarative-agent/v1.5/schema.json";

  /** 代理版本 */
  version: "v1.5";

  /** 代理名称（最大100字符） */
  @maxLength(100)
  @minLength(1)
  name: string;

  /** 代理描述（最大1000字符） */
  @maxLength(1000)
  @minLength(1)
  description: string;

  /** 代理指令（最大8000字符） */
  @maxLength(8000)
  @minLength(1)
  instructions: string;

  /** 代理功能（1-5项） */
  @minItems(1)
  @maxItems(5)
  capabilities: string[];

  /** 对话开场白（最大4项，可选） */
  @maxItems(4)
  conversation_starters?: string[];
}
```

#### 2. 项目结构设置
```
m365-agent/
├── src/
│   ├── agent.tsp           # TypeSpec代理定义
│   ├── agent.json          # 生成的代理清单
│   └── api/                # 自定义连接器API
├── dist/                   # 编译输出
├── package.json
├── teamsapp.local.json     # 本地开发配置
└── teamsapp.yml           # 部署配置
```

### 部署工作流程

#### 1. 本地开发
```bash
# 安装依赖
npm install @microsoft/m365-agent-toolkit

# 编译TypeSpec
tsp compile src/agent.tsp

# 本地预览
npm run preview
```

#### 2. 部署到Microsoft 365
```bash
# 身份验证
m365 login

# 部署代理
m365 teams app deploy --manifest-path dist/agent.json

# 测试部署
m365 teams app install --manifest-path dist/agent.json
```

## 开发最佳实践

### 指令编写指南

#### 1. 清晰的角色定义
```json
{
  "instructions": "您是专门处理[具体领域]的Microsoft 365 Copilot代理。您的核心职责包括[主要职责列表]。始终使用[语气和风格]与用户互动。"
}
```

#### 2. 功能对齐
确保指令与声明的功能保持一致：
- 如果声明了`OneDriveAndSharePoint`，包含文件处理指令
- 如果声明了`WebSearch`，包含搜索和验证指令
- 如果声明了`TeamsAndOutlook`，包含通信工作流程

#### 3. 错误处理
```json
{
  "instructions": "如果遇到错误或无法完成请求：1. 明确说明问题 2. 提供替代解决方案 3. 在必要时建议联系支持团队。"
}
```

### 对话开场白设计

#### 有效开场白示例
```json
{
  "conversation_starters": [
    "帮我分析上一季度的销售数据",
    "创建一个项目进度跟踪文档",
    "搜索最新的行业趋势报告",
    "安排团队会议并准备议程"
  ]
}
```

## 高级功能

### 自定义连接器集成

#### 1. 连接器定义
```json
{
  "connectionReferences": [
    {
      "id": "custom-api-connector",
      "connectorId": "/providers/microsoft.powerapps/apis/shared_custom-api",
      "connectionName": "custom-api-connection",
      "displayName": "自定义API连接器"
    }
  ]
}
```

#### 2. TypeSpec API定义
```typespec
namespace CustomAPI;

/** 自定义数据模型 */
model CustomerData {
  customerID: string;
  name: string;
  email: string;
  lastPurchaseDate: string;
}

/** API响应模型 */
model APIResponse {
  success: boolean;
  data?: CustomerData[];
  error?: string;
}
```

### 企业数据集成

#### Graph连接器配置
```json
{
  "graphConnectors": [
    {
      "connectorId": "custom-erp-connector",
      "name": "ERP系统连接器",
      "description": "访问企业ERP系统数据"
    }
  ]
}
```

## 安全和合规

### 数据保护原则
1. **最小权限原则**: 只请求必要的功能
2. **数据分类**: 明确标记敏感数据处理
3. **审计日志**: 启用所有操作的审计跟踪

### 合规检查清单
- [ ] 数据处理符合GDPR要求
- [ ] 实施适当的数据加密
- [ ] 配置访问控制策略
- [ ] 建立数据保留政策

## 测试和验证

### 功能测试
```bash
# 测试代理功能
m365 teams app test --manifest-path dist/agent.json

# 验证架构合规性
tsp validate src/agent.tsp
```

### 性能监控
- 监控响应时间
- 跟踪用户满意度
- 分析使用模式
- 识别瓶颈问题

## 故障排除

### 常见问题
1. **架构验证失败**: 检查JSON语法和必需字段
2. **功能不可用**: 验证用户权限和许可证
3. **连接器错误**: 确认API端点和身份验证
4. **部署失败**: 检查清单文件和网络连接

### 调试工具
```bash
# 启用详细日志
DEBUG=* npm run preview

# 验证代理清单
tsp compile --validate src/agent.tsp
```

## 维护和更新

### 版本控制
- 使用语义版本控制
- 维护变更日志
- 测试向后兼容性

### 监控指标
- 用户采用率
- 功能使用统计
- 性能基准
- 错误率

## 参考资料

- [Microsoft 365 Agents Toolkit文档](https://learn.microsoft.com/microsoft-365/copilot/agents-toolkit/)
- [TypeSpec规范](https://typespec.io/)
- [Microsoft 365 Copilot API参考](https://learn.microsoft.com/graph/api/copilot-overview)
- [安全最佳实践](https://learn.microsoft.com/microsoft-365/compliance/)