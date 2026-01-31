````prompt
---
mode: 'agent'
tools: ['changes', 'search/codebase', 'edit/editFiles', 'problems']
description: 'Create a declarative agent for Microsoft 365 Copilot by integrating an MCP server with authentication, tool selection, and configuration'
model: 'gpt-4.1'
tags: [mcp, m365-copilot, declarative-agent, model-context-protocol, api-plugin]
---

# Create MCP-based Declarative Agent for Microsoft 365 Copilot

Create a complete declarative agent for Microsoft 365 Copilot that integrates with a Model Context Protocol (MCP) server to access external systems and data.

## Requirements

Generate the following project structure using Microsoft 365 Agents Toolkit:

### Project Setup
1. **Scaffold declarative agent** via Agents Toolkit
2. **Add MCP action** pointing to MCP server
3. **Select tools** to import from MCP server
4. **Configure authentication** (OAuth 2.0 or SSO)
5. **Review generated files** (manifest.json, ai-plugin.json, declarativeAgent.json)

### Key Files Generated

**appPackage/manifest.json** - Teams app manifest with plugin reference:
```json
{
"$schema": "https://developer.microsoft.com/json-schemas/teams/vDevPreview/MicrosoftTeams.schema.json",
  "manifestVersion": "devPreview",
  “版本”：“1.0.0”，
  "id": "...",
  “开发人员”：{
    “名称”：“...”，
    "网站网址": "...",
    "privacyUrl": "...",
    "termsOfUseUrl": "..."
  },
  “姓名”：{
    "short": "代理名称",
    "full": "代理全名"
  },
  “描述”：{
    "short": "简短描述",
    "full": "完整描述"
  },
  “副驾驶代理”：{
    “声明性代理”：[
      {
        "id": "声明性代理",
        “文件”：“声明性Agent.json”
      }
    ]
  }
}
```

**appPackage/declarativeAgent.json** - Agent definition:
```json
{
  "$schema": "https://aka.ms/json-schemas/copilot/declarative-agent/v1.0/schema.json",
  “版本”：“v1.0”，
  "name": "代理人姓名",
  "description": "代理描述",
  "instructions": "您是一名帮助[特定领域]的助手。使用可用的工具来[功能]。",
  “能力”：[
    {
      "name": "网络搜索",
      “网站”：[
        {
          “url”：“https://learn.microsoft.com”
        }
      ]
    },
    {
      “名称”：“MCP”，
      “文件”：“ai-plugin.json”
    }
  ]
}
```

**appPackage/ai-plugin.json** - MCP plugin manifest:
```json
{
  “schema_version”：“v2.1”，
  "name_for_ human": "服务名称",
  "description_for_ human": "用户描述",
  "description_for_model": "AI 模型的描述",
  "contact_email": "support@company.com",
  "命名空间": "服务名称",
  “能力”：{
    “conversation_starters”：[
      {
        "text": "示例查询 1"
      }
    ]
  },
  “功能”：[
    {
      "name": "函数名称",
      "description": "功能描述",
      “能力”：{
        “响应语义”：{
          “数据路径”：“$”，
          “属性”：{
            "标题": "$.标题",
            "副标题": "$.描述"
          }
        }
      }
    }
  ],
  “运行时”：[
    {
      “类型”：“MCP”，
      “规格”：{
        “url”：“https://api.service.com/mcp/”
      },
      "run_for_functions": ["函数名称"],
      “授权”：{
        “类型”：“OAuthPluginVault”，
        “reference_id”：“${{OAUTH_REFERENCE_ID}}”
      }
    }
  ]
}
```

**/.vscode/mcp.json** - MCP server configuration:
```json
{
  "serverUrl": "https://api.service.com/mcp/",
  "pluginFilePath": "appPackage/ai-plugin.json"
}
```

## MCP Server Integration

### Supported MCP Endpoints
The MCP server must provide:
- **Server metadata** endpoint
- **Tools listing** endpoint (exposes available functions)
- **Tool execution** endpoint (handles function calls)

### Tool Selection
When importing from MCP:
1. Fetch available tools from server
2. Select specific tools to include (for security/simplicity)
3. Tool definitions are auto-generated in ai-plugin.json

### Authentication Types

**OAuth 2.0 (Static Registration)**
```json
“授权”：{
  “类型”：“OAuthPluginVault”，
  "reference_id": "${{OAUTH_REFERENCE_ID}}",
  "authorization_url": "https://auth.service.com/authorize",
  "client_id": "${{CLIENT_ID}}",
  "client_secret": "${{CLIENT_SECRET}}",
  “范围”：“读写”
}
```

**Single Sign-On (SSO)**
```json
“授权”：{
  “类型”：“单点登录”
}
```

## Response Semantics

### Define Data Mapping
Use `response_semantics` to extract relevant fields from API responses:

```json
“能力”：{
  “响应语义”：{
    "data_path": "$.结果",
    “属性”：{
      "标题": "$.name",
      "副标题": "$.描述",
      "url": "$.link"
    }
  }
}
```

### Add Adaptive Cards (Optional)
See the `mcp-create-adaptive-cards` prompt for adding visual card templates.

## Environment Configuration

Create `.env.local` or `.env.dev` for credentials:

```env
OAUTH_REFERENCE_ID=您的 oauth-reference-id
CLIENT_ID=您的客户 ID
CLIENT_SECRET=您的客户秘密
```

## Testing & Deployment

### Local Testing
1. **Provision** agent in Agents Toolkit
2. **Start debugging** to sideload in Teams
3. Test in Microsoft 365 Copilot at https://m365.cloud.microsoft/chat
4. Authenticate when prompted
5. Query the agent using natural language

### Validation
- Verify tool imports in ai-plugin.json
- Check authentication configuration
- Test each exposed function
- Validate response data mapping

## Best Practices

### Tool Design
- **Focused functions**: Each tool should do one thing well
- **Clear descriptions**: Help the model understand when to use each tool
- **Minimal scoping**: Only import tools the agent needs
- **Descriptive names**: Use action-oriented function names

### Security
- **Use OAuth 2.0** for production scenarios
- **Store secrets** in environment variables
- **Validate inputs** on the MCP server side
- **Limit scopes** to minimum required permissions
- **Use reference IDs** for OAuth registration

### Instructions
- **Be specific** about the agent's purpose and capabilities
- **Define behavior** for both successful and error scenarios
- **Reference tools** explicitly in instructions when applicable
- **Set expectations** for users about what the agent can/cannot do

### Performance
- **Cache responses** when appropriate on MCP server
- **Batch operations** where possible
- **Set timeouts** for long-running operations
- **Paginate results** for large datasets

## Common MCP Server Examples

### GitHub MCP Server
```
网址：https://api.githubcopilot.com/mcp/
工具：search_repositories、search_users、get_repository
验证：OAuth 2.0
```

### Jira MCP Server
```
网址：https://your-domain.atlassian.net/mcp/
工具：search_issues、create_issue、update_issue
验证：OAuth 2.0
```

### Custom Service
```
网址：https://api.your-service.com/mcp/
工具：您的服务公开的自定义工具
身份验证：OAuth 2.0 或 SSO
```

## Workflow

Ask the user:
1. What MCP server are you integrating with (URL)?
2. What tools should be exposed to Copilot?
3. What authentication method does the server support?
4. What should the agent's primary purpose be?
5. Do you need response semantics or Adaptive Cards?

Then generate:
- Complete appPackage/ structure (manifest.json, declarativeAgent.json, ai-plugin.json)
- mcp.json configuration
- .env.local template
- Provisioning and testing instructions

## Troubleshooting

### MCP Server Not Responding
- Verify server URL is correct
- Check network connectivity
- Validate MCP server implements required endpoints

### Authentication Fails
- Verify OAuth credentials are correct
- Check reference ID matches registration
- Confirm scopes are requested properly
- Test OAuth flow independently

### Tools Not Appearing
- Ensure mcp.json points to correct server
- Verify tools were selected during import
- Check ai-plugin.json has correct function definitions
- Re-fetch actions from MCP if server changed

### Agent Not Understanding Queries
- Review instructions in declarativeAgent.json
- Check function descriptions are clear
- Verify response_semantics extract correct data
- Test with more specific queries

````