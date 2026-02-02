---
description: 'Guidelines and best practices for building TypeSpec-based declarative agents and API plugins for Microsoft 365 Copilot'
applyTo: '**/*.tsp'
---

# Microsoft 365 Copilot 开发指南的 TypeSpec

## 核心原则

使用 Microsoft 365 Copilot 的 TypeSpec 时：

1. **类型安全第一**：利用 TypeSpec 的强类型来处理所有模型和操作
2. **声明式方法**：使用装饰器来描述意图，而不是实现
3. **限定范围的功能**：尽可能将功能范围限定到特定资源
4. **清晰的说明**：编写明确、详细的代理说明
5. **以用户为中心**：针对 Microsoft 365 Copilot 中的最终用户体验进行设计

## 文件组织

### 标准结构
```
project/
├── appPackage/
│   ├── cards/              # Adaptive Card templates
│   │   └── *.json
│   ├── .generated/         # Generated manifests (auto-generated)
│   └── manifest.json       # Teams app manifest
├── src/
│   ├── main.tsp           # Agent definition
│   └── actions.tsp        # API operations (for plugins)
├── m365agents.yml         # Agents Toolkit configuration
└── package.json
```

### 进口声明
始终在 TypeSpec 文件的顶部包含所需的导入：

```typescript
import "@typespec/http";
import "@typespec/openapi3";
import "@microsoft/typespec-m365-copilot";

using TypeSpec.Http;
using TypeSpec.M365.Copilot.Agents;  // For agents
using TypeSpec.M365.Copilot.Actions; // For API plugins
```

## 代理开发最佳实践

### 代理声明
```typescript
@agent({
  name: "Role-Based Name",  // e.g., "Customer Support Assistant"
  description: "Clear, concise description under 1,000 characters"
})
```

- 使用基于角色的名称来描述代理的用途
- 使描述内容丰富但简洁
- 避免使用“Helper”或“Bot”等通用名称

### 使用说明
```typescript
@instructions("""
  You are a [specific role] specialized in [domain].
  
  Your responsibilities include:
  - [Key responsibility 1]
  - [Key responsibility 2]
  
  When helping users:
  - [Behavioral guideline 1]
  - [Behavioral guideline 2]
  
  You should NOT:
  - [Constraint 1]
  - [Constraint 2]
""")
```

- 用第二人称写作（“你是……”）
- 具体说明代理人的角色和专业知识
- 定义该做什么和不该做什么
- 保持在 8,000 个字符以内
- 使用清晰、结构化的格式

### 对话开始者
```typescript
@conversationStarter(#{
  title: "Action-Oriented Title",  // e.g., "Check Status"
  text: "Specific example query"   // e.g., "What's the status of my ticket?"
})
```

- 提供2-4个不同的开胃菜
- 让每个展示都有不同的功能
- 使用以行动为导向的标题
- 编写实际的示例查询

### 能力-知识来源

**网络搜索** - 尽可能范围到特定网站：
```typescript
op webSearch is AgentCapabilities.WebSearch<Sites = [
  { url: "https://learn.microsoft.com" },
  { url: "https://docs.microsoft.com" }
]>;
```

**OneDrive 和 SharePoint** - 使用 URL 或 ID：
```typescript
op oneDriveAndSharePoint is AgentCapabilities.OneDriveAndSharePoint<
  ItemsByUrl = [
    { url: "https://contoso.sharepoint.com/sites/Engineering" }
  ]
>;
```

**团队消息** - 指定频道/聊天：
```typescript
op teamsMessages is AgentCapabilities.TeamsMessages<Urls = [
  { url: "https://teams.microsoft.com/l/channel/..." }
]>;
```

**电子邮件** - 范围到特定文件夹：
```typescript
op email is AgentCapabilities.Email<
  Folders = [
    { folderId: "Inbox" },
    { folderId: "SentItems" }
  ],
  SharedMailbox = "support@contoso.com"  // Optional
>;
```

**人员** - 无需范围界定：
```typescript
op people is AgentCapabilities.People;
```

**Copilot 连接器** - 指定连接 ID：
```typescript
op copilotConnectors is AgentCapabilities.GraphConnectors<
  Connections = [
    { connectionId: "your-connector-id" }
  ]
>;
```

**Dataverse** - 特定表的范围：
```typescript
op dataverse is AgentCapabilities.Dataverse<
  KnowledgeSources = [
    {
      hostName: "contoso.crm.dynamics.com";
      tables: [
        { tableName: "account" },
        { tableName: "contact" }
      ];
    }
  ]
>;
```

### 功能 - 生产力工具

```typescript
// Python code execution
op codeInterpreter is AgentCapabilities.CodeInterpreter;

// Image generation
op graphicArt is AgentCapabilities.GraphicArt;

// Meeting content access
op meetings is AgentCapabilities.Meetings;

// Specialized AI models
op scenarioModels is AgentCapabilities.ScenarioModels<
  ModelsById = [
    { id: "model-id" }
  ]
>;
```

## API 插件开发最佳实践

### 服务定义
```typescript
@service
@actions(#{
  nameForHuman: "User-Friendly API Name",
  descriptionForHuman: "What users will understand",
  descriptionForModel: "What the model needs to know",
  contactEmail: "support@company.com",
  privacyPolicyUrl: "https://company.com/privacy",
  legalInfoUrl: "https://company.com/terms"
})
@server("https://api.example.com", "API Name")
@useAuth([AuthType])  // If authentication needed
namespace APINamespace {
  // Operations here
}
```

### 操作定义
```typescript
@route("/resource/{id}")
@get
@action
@card(#{
  dataPath: "$.items",
  title: "$.title",
  file: "cards/card.json"
})
@capabilities(#{
  confirmation: #{
    type: "AdaptiveCard",
    title: "Confirm Action",
    body: "Confirm with {{ function.parameters.param }}"
  }
})
@reasoning("Consider X when Y")
@responding("Present results as Z")
op getResource(
  @path id: string,
  @query filter?: string
): ResourceResponse;
```

### 型号
```typescript
model Resource {
  id: string;
  name: string;
  description?: string;  // Optional fields
  status: "active" | "inactive";  // Union types for enums
  @format("date-time")
  createdAt: utcDateTime;
  @format("uri")
  url?: string;
}

model ResourceList {
  items: Resource[];
  totalCount: int32;
  nextPage?: string;
}
```

### 认证

**API 密钥**
```typescript
@useAuth(ApiKeyAuth<ApiKeyLocation.header, "X-API-Key">)

// Or with reference ID
@useAuth(Auth)
@authReferenceId("${{ENV_VAR_REFERENCE_ID}}")
model Auth is ApiKeyAuth<ApiKeyLocation.header, "X-API-Key">;
```

**OAuth2**
```typescript
@useAuth(OAuth2Auth<[{
  type: OAuth2FlowType.authorizationCode;
  authorizationUrl: "https://auth.example.com/authorize";
  tokenUrl: "https://auth.example.com/token";
  refreshUrl: "https://auth.example.com/refresh";
  scopes: ["read", "write"];
}]>)

// Or with reference ID
@useAuth(Auth)
@authReferenceId("${{OAUTH_REFERENCE_ID}}")
model Auth is OAuth2Auth<[...]>;
```

## 命名约定

### 文件
- `main.tsp` - 代理定义
- `actions.tsp` - API 操作
- `[feature].tsp` - 附加功能文件
- `cards/*.json` - 自适应卡片模板

### 类型规范元素
- **命名空间**：PascalCase（例如，`CustomerSupportAgent`）
- **操作**：驼峰命名法（例如，`listProjects`、`createTicket`）
- **模型**：PascalCase（例如，`Project`、`TicketResponse`）
- **模型属性**：驼峰命名法（例如，`projectId`、`createdDate`）

## 常见模式

### 多功能代理
```typescript
@agent("Knowledge Worker", "Description")
@instructions("...")
namespace KnowledgeWorker {
  op webSearch is AgentCapabilities.WebSearch;
  op files is AgentCapabilities.OneDriveAndSharePoint;
  op people is AgentCapabilities.People;
}
```

### 增删改查 API 插件
```typescript
namespace ProjectAPI {
  @route("/projects") @get @action
  op list(): Project[];
  
  @route("/projects/{id}") @get @action
  op get(@path id: string): Project;
  
  @route("/projects") @post @action
  @capabilities(#{confirmation: ...})
  op create(@body project: CreateProject): Project;
  
  @route("/projects/{id}") @patch @action
  @capabilities(#{confirmation: ...})
  op update(@path id: string, @body project: UpdateProject): Project;
  
  @route("/projects/{id}") @delete @action
  @capabilities(#{confirmation: ...})
  op delete(@path id: string): void;
}
```

### 自适应卡数据绑定
```json
{
  "type": "AdaptiveCard",
  "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
  "version": "1.5",
  "body": [
    {
      "type": "Container",
      "$data": "${$root}",
      "items": [
        {
          "type": "TextBlock",
          "text": "Title: ${if(title, title, 'N/A')}",
          "wrap": true
        }
      ]
    }
  ]
}
```

## 验证和测试

### 配置之前
1. 运行 TypeSpec 验证：`npm run build` 或使用 Agents Toolkit
2. 检查 `@card` 装饰器中的所有文件路径是否存在
3. 验证身份验证引用是否匹配配置
4. 确保能力范围适当
5. 查看说明的清晰度和长度

### 测试策略
1. **提供**：部署到开发环境
2. **测试**：使用 Microsoft 365 Copilot，网址为 https://m365.cloud.microsoft/chat
3. **调试**：启用 Copilot 开发人员模式以获取编排器见解
4. **迭代**：根据实际行为进行细化
5. **验证**：测试所有对话启动器和功能

## 性能优化

1. **范围功能**：如果只需要子集，则不要授予对所有数据的访问权限
2. **限制操作**：仅公开代理实际使用的 API 操作
3. **高效模型**：使响应模型专注于必要的数据
4. **卡片优化**：在自适应卡片中使用条件渲染 (`$when`)
5. **缓存**：使用适当的缓存标头设计 API

## 安全最佳实践

1. **身份验证**：始终对非公共 API 使用身份验证
2. **范围**：将功能访问限制为所需的最低资源
3. **验证**：验证API操作中的所有输入
4. **秘密**：对敏感数据使用环境变量
5. **参考**：使用 `@authReferenceId` 作为生产凭证
6. **权限**：请求最小必要的 OAuth 范围

## 错误处理

```typescript
model ErrorResponse {
  error: {
    code: string;
    message: string;
    details?: ErrorDetail[];
  };
}

model ErrorDetail {
  field?: string;
  message: string;
}
```

## 文档

在 TypeSpec 中包含复杂操作的注释：

```typescript
/**
 * Retrieves project details with associated tasks and team members.
 * 
 * @param id - Unique project identifier
 * @param includeArchived - Whether to include archived tasks
 * @returns Complete project information
 */
@route("/projects/{id}")
@get
@action
op getProjectDetails(
  @path id: string,
  @query includeArchived?: boolean
): ProjectDetails;
```

## 要避免的常见陷阱

1. ❌ 通用代理名称（“Helper Bot”）
2. ❌ 模糊的说明（“帮助用户做事”）
3. ❌ 无能力范围（访问所有数据）
4. ❌ 缺少破坏性操作的确认
5. ❌ 过于复杂的自适应卡
6. ❌ TypeSpec 文件中的硬编码凭证
7. ❌ 缺少错误响应模型
8. ❌ 命名约定不一致
9. ❌ 功能太多（仅使用需要的功能）
10. ❌ 超过 8,000 个字符的说明

## 资源

- [TypeSpec 官方文档](https://typespec.io/)
- [Microsoft 365 Copilot 扩展性](https://learn.microsoft.com/microsoft-365-copilot/extensibility/)
- [代理工具包](https://aka.ms/M365AgentsToolkit)
- [自适应卡片设计器](https://adaptivecards.io/designer/)
