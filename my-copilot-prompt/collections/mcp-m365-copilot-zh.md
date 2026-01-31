# 基于 MCP 的 M365 代理

用于通过 Microsoft 365 Copilot 的模型上下文协议集成构建声明性代理的综合集合

**标签：** mcp、m365-copilot、声明性代理、api 插件、模型上下文协议、自适应卡

## 该系列中的项目

|标题 |类型 |描述 | MCP 服务器 |
| ----- | ---- | ----------- | ----------- |
| [Mcp 创建声明式代理](../prompts/mcp-create-declarative-agent.prompt-zh.md)<br />[![在 VS 中安装代码](https://img.shields.io/badge/VS_Code-Install-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/prompt?url=vscode%3Achat-prompt%2Finstall%3Furl%3Dhttps%3A%2F %2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fprompts%2Fmcp-create-declarative-agent.prompt.md)<br />[![在 VS Code 中安装内部人员](https://img.shields.io/badge/VS_Code_Insiders-Install-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/prompt?url=vscode-insiders%3Achat-prompt%2Finstall%3Furl%3Dhtt ps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fprompts%2Fmcp-create-declarative-agent.prompt.md) |提示|没有描述 |  |
| [Mcp 创建自适应卡片](../prompts/mcp-create-adaptive-cards.prompt-zh.md)<br />[![在 VS 中安装代码](https://img.shields.io/badge/VS_Code-Install-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/prompt?url=vscode%3Achat-prompt%2Finstall%3Furl%3Dhttps%3A% 2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fprompts%2Fmcp-create-adaptive-cards.prompt.md)<br />[![在 VS Code 中安装内部人员](https://img.shields.io/badge/VS_Code_Insiders-Install-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/prompt?url=vscode-insiders%3Achat-prompt%2Finstall%3Furl%3Dh ttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fprompts%2Fmcp-create-adaptive-cards.prompt.md) |提示|没有描述 |  |
| [Mcp 部署管理代理](../prompts/mcp-deploy-manage-agents.prompt-zh.md)<br />[![在 VS 中安装代码](https://img.shields.io/badge/VS_Code-Install-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/prompt?url=vscode%3Achat-prompt%2Finstall%3Furl%3Dhttps%3A% 2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fprompts%2Fmcp-deploy-manage-agents.prompt.md)<br />[![在 VS Code 中安装内部人员](https://img.shields.io/badge/VS_Code_Insiders-Install-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/prompt?url=vscode-insiders%3Achat-prompt%2Finstall%3Furl%3Dh ttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fprompts%2Fmcp-deploy-manage-agents.prompt.md) |提示|没有描述 |  |
| [基于MCP的M365 Copilot开发指南](../instructions/mcp-m365-copilot.instructions-zh.md)<br />[![在VS中安装代码](https://img.shields.io/badge/VS_Code-Install-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/instructions?url=vscode%3Achat-instructions%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Finstructions%2Fmcp-m365-copilot.instructions.md)<br />[![在 VS Code 中安装内部人员](https://img.shields.io/badge/VS_Code_Insiders-Install-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/instructions?url=vscode-insiders%3Achat-instructions%2Finstall%3Fur l%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Finstructions%2Fmcp-m365-copilot.instructions.md) |说明 |为具有模型上下文协议集成的 Microsoft 365 Copilot 构建基于 MCP 的声明式代理和 API 插件的最佳实践 |  |
| [MCP M365 Agent Expert](../agents/mcp-m365-agent-expert.agent-zh.md)<br />[![在VS中安装代码](https://img.shields.io/badge/VS_Code-Install-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/agent?url=vscode%3Achat-agent%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fagents%2Fmcp-m365-agent-expert.agent.md)<br />[![在 VS Code 中安装内部人士](https://img.shields.io/badge/VS_Code_Insiders-Install-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/agent?url=vscode-insiders%3Achat-agent%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fagents%2Fmcp-m365-agent-expert.agent.md) |代理|用于为具有模型上下文协议集成的 Microsoft 365 Copilot 构建基于 MCP 的声明式代理的专家助理 [请参阅用法](#mcp-m365-agent-expert) |  |

## 集合用途

### MCP M365 代理专家

推荐

此聊天模式为为 Microsoft 365 Copilot 构建基于 MCP 的声明式代理提供专家指导。

此聊天模式非常适合：
- 通过 MCP 集成创建新的声明式代理
- 设计视觉反应的自适应卡片
- 配置 OAuth 2.0 或 SSO 身份验证
- 设置响应语义和数据提取
- 解决部署和治理问题
- 学习 M365 Copilot 的 MCP 最佳实践

为了获得最佳结果，请考虑：
- 使用说明文件为所有 Copilot 交互设置上下文
- 使用提示生成初始代理结构和配置
- 切换到专家聊天模式以获得详细的实施帮助
- 提供有关您的 MCP 服务器、工具和业务场景的具体详细信息

---

*此集合包括 5 个针对 **基于 MCP 的 M365 Agents** 精选的项目。*