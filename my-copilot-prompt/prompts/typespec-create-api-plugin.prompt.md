---
mode: 'agent'
tools: ['changes', 'search/codebase', 'edit/editFiles', 'problems']
description: 'Generate a TypeSpec API plugin with REST operations, authentication, and Adaptive Cards for Microsoft 365 Copilot'
model: 'gpt-4.1'
tags: [typespec, m365-copilot, api-plugin, rest-api]
---

# 创建 TypeSpec API 插件

为与外部 REST API 集成的 Microsoft 365 Copilot 创建完整的 TypeSpec API 插件。

## 要求

使用以下命令生成 TypeSpec 文件：

### main.tsp - 代理定义
```typescript
import "@typespec/http";
import "@typespec/openapi3";
import "@microsoft/typespec-m365-copilot";
import "./actions.tsp";

using TypeSpec.Http;
using TypeSpec.M365.Copilot.Agents;
using TypeSpec.M365.Copilot.Actions;

@agent({
  name: "[Agent Name]",
  description: "[Description]"
})
@instructions("""
  [Instructions for using the API operations]
""")
namespace [AgentName] {
  // Reference operations from actions.tsp
  op operation1 is [APINamespace].operationName;
}
```

### actions.tsp - API 操作
```typescript
import "@typespec/http";
import "@microsoft/typespec-m365-copilot";

using TypeSpec.Http;
using TypeSpec.M365.Copilot.Actions;

@service
@actions(#{
    nameForHuman: "[API Display Name]",
    descriptionForModel: "[Model description]",
    descriptionForHuman: "[User description]"
})
@server("[API_BASE_URL]", "[API Name]")
@useAuth([AuthType]) // Optional
namespace [APINamespace] {
  
  @route("[/path]")
  @get
  @action
  op operationName(
    @path param1: string,
    @query param2?: string
  ): ResponseModel;

  model ResponseModel {
    // Response structure
  }
}
```

## 身份验证选项

根据API要求选择：

1. **无身份验证**（公共 API）
   ```typescript
   // No @useAuth decorator needed
   ```

2. **API 密钥**
   ```typescript
   @useAuth(ApiKeyAuth<ApiKeyLocation.header, "X-API-Key">)
   ```

3. **OAuth2**
   ```typescript
   @useAuth(OAuth2Auth<[{
     type: OAuth2FlowType.authorizationCode;
     authorizationUrl: "https://oauth.example.com/authorize";
     tokenUrl: "https://oauth.example.com/token";
     refreshUrl: "https://oauth.example.com/token";
     scopes: ["read", "write"];
   }]>)
   ```

4. **注册授权参考**
   ```typescript
   @useAuth(Auth)
   
   @authReferenceId("registration-id-here")
   model Auth is ApiKeyAuth<ApiKeyLocation.header, "X-API-Key">
   ```

## 功能能力

### 确认对话框
```typescript
@capabilities(#{
  confirmation: #{
    type: "AdaptiveCard",
    title: "Confirm Action",
    body: """
    Are you sure you want to perform this action?
      * **Parameter**: {{ function.parameters.paramName }}
    """
  }
})
```

### 自适应卡响应
```typescript
@card(#{
  dataPath: "$.items",
  title: "$.title",
  url: "$.link",
  file: "cards/card.json"
})
```

### 推理和回应说明
```typescript
@reasoning("""
  Consider user's context when calling this operation.
  Prioritize recent items over older ones.
""")
@responding("""
  Present results in a clear table format with columns: ID, Title, Status.
  Include a summary count at the end.
""")
```

## 最佳实践

1. **操作名称**：使用清晰、面向操作的名称（listProjects、createTicket）
2. **模型**：为请求和响应定义类似 TypeScript 的模型
3. **HTTP 方法**：使用适当的动词（@get、@post、@patch、@delete）
4. **路径**：将 RESTful 路径约定与 @route 一起使用
5. **参数**：适当使用@path、@query、@header、@body
6. **描述**：为模型理解提供清晰的描述
7. **确认**：添加破坏性操作（删除、更新关键数据）
8. **卡片**：用于具有多个数据项的丰富视觉响应

## 工作流程

询问用户：
1. API 基本 URL 和用途是什么？
2. 需要哪些操作（CRUD操作）？
3. API 使用什么身份验证方法？
4. 任何操作都需要确认吗？
5. 回复是否需要自适应卡？

然后生成：
- 使用代理定义完成 `main.tsp`
- 使用 API 操作和模型完成 `actions.tsp`
- 如果需要自适应卡，则可选 `cards/card.json`
