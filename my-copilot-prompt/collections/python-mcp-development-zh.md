# Python MCP 服务器开发

用于使用带有 FastMCP 的官方 SDK 在 Python 中构建模型上下文协议 (MCP) 服务器的完整工具包。包括最佳实践说明、生成服务器的提示以及用于指导的专家聊天模式。

**标签：** python、mcp、模型上下文协议、fastmcp、服务器开发

## 该系列中的项目

|标题 |类型 |描述 | MCP 服务器 |
| ----- | ---- | ----------- | ----------- |
| [Python MCP服务器开发](../instructions/python-mcp-server.instructions-zh.md)<br />[![在VS中安装代码](https://img.shields.io/badge/VS_Code-Install-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/instructions?url=vscode%3Achat-instructions%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Finstructions%2Fpython-mcp-server.instructions.md)<br />[![在 VS Code 中安装内部人士](https://img.shields.io/badge/VS_Code_Insiders-Install-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/instructions?url=vscode-insiders%3Achat-instructions%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Finstructions%2Fpython-mcp-server.instructions.md) |说明 |使用 Python SDK 构建模型上下文协议 (MCP) 服务器的说明 |  |
| [生成Python MCP服务器](../prompts/python-mcp-server-generator.prompt-zh.md)<br />[![在VS中安装代码](https://img.shields.io/badge/VS_Code-Install-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/prompt?url=vscode%3Achat-prompt%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fprompts%2Fpython-mcp-server-generator.prompt.md)<br />[![在 VS Code 中安装内部人员](https://img.shields.io/badge/VS_Code_Insiders-Install-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/prompt?url=vscode-insiders%3Achat-prompt%2Finstall%3Furl%3Dht tps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fprompts%2Fpython-mcp-server-generator.prompt.md) |提示|使用工具、资源和正确的配置在 Python 中生成完整的 MCP 服务器项目 |  |
| [Python MCP Server Expert](../agents/python-mcp-expert.agent-zh.md)<br />[![在VS中安装代码](https://img.shields.io/badge/VS_Code-Install-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/agent?url=vscode%3Achat-agent%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fagents%2Fpython-mcp-expert.agent.md)<br />[![在 VS Code 中安装内部人员](https://img.shields.io/badge/VS_Code_Insiders-Install-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/agent?url=vscode-insiders%3Achat-agent%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fagents%2Fpython-mcp-expert.agent.md) |代理|用于在 Python 中开发模型上下文协议 (MCP) 服务器的专家助手 [请参阅用法](#python-mcp-server-expert) |  |

## 集合用途

### Python MCP 服务器专家

推荐

此聊天模式为使用 FastMCP 在 Python 中构建 MCP 服务器提供专家指导。

此聊天模式非常适合：
- 使用 Python 创建新的 MCP 服务器项目
- 使用 Pydantic 模型和结构化输出实现类型化工具
- 设置 stdio 或可流传输的 HTTP 传输
- 调试类型提示和架构验证问题
- 使用 FastMCP 学习 Python MCP 最佳实践
- 优化服务器性能和资源管理

为了获得最佳结果，请考虑：
- 使用指令文件为 Python/FastMCP 开发设置上下文
- 使用提示符用 uv 生成初始项目结构
- 切换到专家聊天模式以获得详细的实施帮助
- 指定是否需要 stdio 还是 HTTP 传输
- 提供有关您需要哪些工具或功能的详细信息
- 提及您是否需要结构化输出、采样或启发

---

*此集合包括 3 个针对 **Python MCP 服务器开发**的精选项目。*