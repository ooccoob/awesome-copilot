---
description: 'Best practices for building MCP-based declarative agents and API plugins for Microsoft 365 Copilot with Model Context Protocol integration'
applyTo: '**/{*mcp*,*agent*,*plugin*,declarativeAgent.json,ai-plugin.json,mcp.json,manifest.json}'
---

# 基于 MCP 的 M365 Copilot 开发指南

## 核心原则

### 模型上下文协议优先
- 利用 MCP 服务器进行外部系统集成
- 从服务器端点导入工具，而不是手动定义
- 让 MCP 处理模式发现和函数生成
- 在 Agents Toolkit 中使用点击式工具选择

### 声明式优于命令式
- 通过配置而不是代码定义代理行为
- 使用 declarativeAgent.json 获取说明和功能
- 在 ai-plugin.json 中指定工具和操作
- 在 mcp.json 中配置 MCP 服务器

### 安全与治理
- 始终使用 OAuth 2.0 或 SSO 进行身份验证
- 工具选择遵循最小权限原则
- 验证 MCP 服务器端点是否安全
- 部署前检查合规性要求

### 以用户为中心的设计
- 创建自适应卡片以获得丰富的视觉反应
- 提供清晰的对话开场白
- 跨中心的响应式体验设计
- 在组织部署之前进行彻底测试

## MCP服务器设计

### 服务器选择
选择符合以下条件的 MCP 服务器：
- 公开用户任务的相关工具
- 支持安全身份验证（OAuth 2.0、SSO）
- 提供可靠的正常运行时间和性能
- 遵循MCP规范标准
- 返回结构良好的响应数据

### 工具导入策略
- 仅导入必要的工具（避免范围过度）
- 来自同一服务器的相关工具分组
- 在组合之前单独测试每个工具
- 选择多个工具时考虑令牌限制

### 认证配置
**OAuth 2.0 静态注册：**
```json
{
  "type": "OAuthPluginVault",
  "reference_id": "YOUR_AUTH_ID",
  "client_id": "github_client_id",
  "client_secret": "github_client_secret",
  "authorization_url": "https://github.com/login/oauth/authorize",
  "token_url": "https://github.com/login/oauth/access_token",
  "scope": "repo read:user"
}
```

**SSO（微软 Entra ID）：**
```json
{
  "type": "OAuthPluginVault",
  "reference_id": "sso_auth",
  "authorization_url": "https://login.microsoftonline.com/common/oauth2/v2.0/authorize",
  "token_url": "https://login.microsoftonline.com/common/oauth2/v2.0/token",
  "scope": "User.Read"
}
```

## 文件组织

### 项目结构
```
project-root/
├── appPackage/
│   ├── manifest.json           # Teams app manifest
│   ├── declarativeAgent.json   # Agent config (instructions, capabilities)
│   ├── ai-plugin.json          # API plugin definition
│   ├── color.png               # App icon color
│   └── outline.png             # App icon outline
├── .vscode/
│   └── mcp.json               # MCP server configuration
├── .env.local                  # Credentials (NEVER commit)
└── teamsapp.yml               # Teams Toolkit config
```

### 关键文件

**声明性Agent.json：**
- 代理名称和描述
- 行为指导
- 对话开始者
- 功能（插件的操作）

**ai-plugin.json：**
- MCP服务器工具导入
- 响应语义（data_path、属性）
- 静态自适应卡片模板
- 函数定义（自动生成）

**mcp.json：**
- MCP 服务器 URL
- 服务器元数据端点
- 认证参考

**.env.local:**
- OAuth 客户端凭据
- API 密钥和秘密
- 特定于环境的配置
- **关键**：添加到 .gitignore

## 响应语义最佳实践

### 数据路径配置
使用 JSONPath 提取相关数据：
```json
{
  "data_path": "$.items[*]",
  "properties": {
    "title": "$.name",
    "subtitle": "$.description", 
    "url": "$.html_url"
  }
}
```

### 模板选择
对于动态模板：
```json
{
  "data_path": "$",
  "template_selector": "$.templateType",
  "properties": {
    "title": "$.title",
    "url": "$.url"
  }
}
```

### 静态模板
在 ai-plugin.json 中定义以保持格式一致：
- 当所有响应都遵循相同结构时使用
- 比动态模板更好的性能
- 更容易维护和版本控制

## 自适应卡指南

### 设计原则
- **单列布局**：垂直堆叠元素
- **灵活的宽度**：使用“拉伸”或“自动”，而不是固定像素
- **响应式设计**：在 Chat、Teams、Outlook 中测试
- **最小的复杂性**：保持卡片简单且易于扫描

### 模板语言模式
**条件：**
```json
{
  "type": "TextBlock",
  "text": "${if(status == 'active', '✅ Active', '❌ Inactive')}"
}
```

**数据绑定：**
```json
{
  "type": "TextBlock",
  "text": "${title}",
  "weight": "bolder"
}
```

**数字格式：**
```json
{
  "type": "TextBlock",
  "text": "Score: ${formatNumber(score, 0)}"
}
```

**条件渲染：**
```json
{
  "type": "Container",
  "$when": "${count(items) > 0}",
  "items": [ ... ]
}
```

### 卡元素使用
- **文本块**：标题、描述、元数据
- **FactSet**：键值对（状态、日期、ID）
- **图像**：图标、缩略图（使用尺寸：“小”）
- **容器**：对相关内容进行分组
- **ActionSet**：后续操作的按钮

## 测试和部署

### 本地测试工作流程
1. **规定**：Teams 工具包 → 规定
2. **部署**：Teams 工具包 → 部署
3. **旁载**：应用程序上传到 Teams
4. **测试**：访问 [m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat)
5. **迭代**：修复问题并重新部署

### 部署前检查表
- [ ] 所有 MCP 服务器工具均经过单独测试
- [ ] 身份验证流程端到端工作
- [ ] 自适应卡在集线器上正确渲染
- [ ] 响应语义提取期望数据
- [ ] 错误处理提供清晰的消息
- [ ] 对话开头相关且清晰
- [ ] 代理指令指导正确的行为
- [ ] 合规性和安全性审查

### 部署选项
**组织部署：**
- IT 管理员部署到所有或选定的用户
- 需要 Microsoft 365 管理中心批准
- 最适合内部业务代理

**代理店：**
- 提交至合作伙伴中心进行验证
- 所有 Copilot 用户均可公开使用
- 需要严格的安全审查

## 常见模式

### 多工具代理
从多个 MCP 服务器导入工具：
```json
{
  "mcpServers": {
    "github": {
      "url": "https://github-mcp.example.com"
    },
    "jira": {
      "url": "https://jira-mcp.example.com"
    }
  }
}
```

### 搜索和显示
1. 工具从 MCP 服务器检索数据
2. 响应语义提取相关字段
3. 自适应卡显示格式化结果
4. 用户可以通过卡片按钮执行操作

### 已验证的操作
1. 用户触发需要身份验证的工具
2. OAuth 流重定向以获取同意
3. 访问令牌存储在插件库中
4. 后续请求使用存储的令牌

## 错误处理

### MCP 服务器错误
- 在代理响应中提供清晰的错误消息
- 如果可用的话，退回到替代工具
- 记录错误以进行调试
- 引导用户重试或替代方法

### 认证失败
- 检查 .env.local 中的 OAuth 凭据
- 验证范围与所需权限匹配
- 首先在 Copilot 之外测试身份验证流程
- 确保令牌刷新逻辑有效

### 响应解析失败
- 验证响应语义中的 JSONPath 表达式
- 优雅地处理丢失或空数据
- 在适当的情况下提供默认值
- 使用不同的 API 响应进行测试

## 性能优化

### 工具选择
- 仅导入必要的工具（减少令牌使用）
- 避免来自多个服务器的冗余工具
- 测试每个工具对响应时间的影响

### 响应大小
- 使用data_path过滤掉不需要的数据
- 尽可能限制结果集
- 考虑对大型数据集进行分页
- 保持自适应卡轻量化

### 缓存策略
- MCP 服务器应在适当的地方进行缓存
- 代理响应可能会被 M365 缓存
- 考虑对时间敏感数据进行缓存失效

## 安全最佳实践

### 凭证管理
- **永远不要** 将 .env.local 提交到源代码管理
- 对所有秘密使用环境变量
- 定期轮换 OAuth 凭据
- 为开发/生产使用单独的凭据

### 数据隐私
- 仅请求最小必要范围
- 避免记录敏感的用户数据
- 查看数据驻留要求
- 遵循合规政策（GDPR 等）

### 服务器验证
- 验证 MCP 服务器可信且安全
- 仅检查 HTTPS 端点
- 查看服务器的隐私政策
- 测试注入漏洞

## 治理与合规

### 管理控制
代理人可以是：
- **阻止**：阻止使用
- **部署**：分配给特定用户/组
- **已发布**：在整个组织范围内提供

### 监控
曲目：
- 代理的使用和采用
- 错误率和性能
- 用户反馈及满意度
- 安全事件

### 审核要求
维护：
- 代理配置的更改历史记录
- 敏感操作的访问日志
- 部署审批记录
- 合规证明

## 资源和参考资料

### 官方文档
- [使用 MCP 构建声明式代理 (DevBlogs)](https://devblogs.microsoft.com/microsoft365dev/build-declarative-agents-for-microsoft-365-copilot-with-mcp/)
- [构建 MCP 插件（学习）](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/build-mcp-plugins)
- [API插件自适应卡（学习）](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/api-plugin-adaptive-cards)
- [管理 Copilot 座席（学习）](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps)

### 工具和 SDK
- Microsoft 365 代理工具包（VS Code 扩展 v6.3.x+）
- 用于代理打包的 Teams 工具包
- 自适应卡片设计器
- MCP 规范文档

### 合作伙伴示例
- Monday.com：任务管理集成
- Canva：设计自动化
- Sitecore：内容管理
