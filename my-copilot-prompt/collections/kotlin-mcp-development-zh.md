# Kotlin MCP 服务器开发

使用官方 io.modelcontextprotocol:kotlin-sdk 库在 Kotlin 中构建模型上下文协议 (MCP) 服务器的完整工具包。包括最佳实践说明、生成服务器的提示以及用于指导的专家聊天模式。

**标签：** kotlin、mcp、模型上下文协议、kotlin 多平台、服务器开发、ktor

## 该系列中的项目

|标题 |类型 |描述 | MCP 服务器 |
| ----- | ---- | ----------- | ----------- |
| [Kotlin MCP 服务器开发指南](../instructions/kotlin-mcp-server.instructions-zh.md)<br />[![在 VS 中安装代码](https://img.shields.io/badge/VS_Code-Install-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/instructions?url=vscode%3Achat-instructions%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Finstructions%2Fkotlin-mcp-server.instructions.md)<br />[![在 VS Code 中安装内部人士](https://img.shields.io/badge/VS_Code_Insiders-Install-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/instructions?url=vscode-insiders%3Achat-instructions%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Finstructions%2Fkotlin-mcp-server.instructions.md) |说明 |使用官方 io.modelcontextprotocol:kotlin-sdk 库在 Kotlin 中构建模型上下文协议 (MCP) 服务器的最佳实践和模式。 |  |
| [Kotlin MCP 服务器项目生成器](../prompts/kotlin-mcp-server-generator.prompt-zh.md)<br />[![在 VS 中安装代码](https://img.shields.io/badge/VS_Code-Install-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/prompt?url=vscode%3Achat-prompt%2Finstall%3Furl%3Dhttps%3A%2 F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fprompts%2Fkotlin-mcp-server-generator.prompt.md)<br />[![在 VS Code 中安装内部人员](https://img.shields.io/badge/VS_Code_Insiders-Install-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/prompt?url=vscode-insiders%3Achat-prompt%2Finstall%3Furl%3Dht tps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fprompts%2Fkotlin-mcp-server-generator.prompt.md) |提示|使用官方 io.modelcontextprotocol:kotlin-sdk 库生成具有正确结构、依赖项和实现的完整 Kotlin MCP 服务器项目。 |  |
| [Kotlin MCP 服务器开发专家](../agents/kotlin-mcp-expert.agent-zh.md)<br />[![在 VS 中安装代码](https://img.shields.io/badge/VS_Code-Install-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/agent?url=vscode%3Achat-agent%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fagents%2Fkotlin-mcp-expert.agent.md)<br />[![安装在VS Code Insider](https://img.shields.io/badge/VS_Code_Insiders-Install-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/agent?url=vscode-insiders%3Achat-agent%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fagents%2Fkotlin-mcp-expert.agent.md) |代理|使用官方 SDK 在 Kotlin 中构建模型上下文协议 (MCP) 服务器的专家助手。 [查看用法](#kotlin-mcp-server-development-expert) |  |

## 集合用途

### Kotlin MCP 服务器开发专家

推荐

此聊天模式为在 Kotlin 中构建 MCP 服务器提供专家指导。

此聊天模式非常适合：
- 使用 Kotlin 创建新的 MCP 服务器项目
- 使用协程和 kotlinx.serialization 实现类型安全工具
- 使用 Ktor 设置 stdio 或 SSE 传输
- 调试协程模式和 JSON 架构问题
- 使用官方 SDK 学习 Kotlin MCP 最佳实践
- 构建多平台 MCP 服务器（JVM、Wasm、iOS）

为了获得最佳结果，请考虑：
- 使用指令文件为 Kotlin MCP 开发设置上下文
- 使用 Gradle 提示生成初始项目结构
- 切换到专家聊天模式以获得详细的实施帮助
- 指定是否需要 stdio 还是 SSE/HTTP 传输
- 提供有关您需要哪些工具或功能的详细信息
- 提及您是否需要多平台支持或特定目标

---

*此集合包括 3 个针对 **Kotlin MCP 服务器开发**的精选项目。*