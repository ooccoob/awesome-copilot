# Rust MCP 服务器开发

使用带有 async/await、过程宏和类型安全实现的官方 rmcp SDK 在 Rust 中构建高性能模型上下文协议服务器。

**标签：** rust、mcp、模型上下文协议、服务器开发、sdk、tokio、异步、宏、rmcp

## 该系列中的项目

|标题 |类型 |描述 | MCP 服务器 |
| ----- | ---- | ----------- | ----------- |
| [Rust MCP 服务器开发最佳实践](../instructions/rust-mcp-server.instructions-zh.md)<br />[![在 VS 中安装代码](https://img.shields.io/badge/VS_Code-Install-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/instructions?url=vscode%3Achat-instructions%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Finstructions%2Frust-mcp-server.instructions.md)<br />[![在 VS Code 中安装内部人士](https://img.shields.io/badge/VS_Code_Insiders-Install-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/instructions?url=vscode-insiders%3Achat-instructions%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Finstructions%2Frust-mcp-server.instructions.md) |说明 |使用带有异步/等待模式的官方 rmcp SDK 在 Rust 中构建模型上下文协议服务器的最佳实践 |  |
| [Rust Mcp 服务器生成器](../prompts/rust-mcp-server-generator.prompt-zh.md)<br />[![在 VS 中安装代码](https://img.shields.io/badge/VS_Code-Install-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/prompt?url=vscode%3Achat-prompt%2Finstall%3Furl%3Dhttps%3A% 2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fprompts%2Frust-mcp-server-generator.prompt.md)<br />[![在 VS Code 中安装内部人员](https://img.shields.io/badge/VS_Code_Insiders-Install-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/prompt?url=vscode-insiders%3Achat-prompt%2Finstall%3Furl%3Dh ttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fprompts%2Frust-mcp-server-generator.prompt.md) |提示|使用官方 rmcp SDK 生成包含工具、提示、资源和测试的完整 Rust 模型上下文协议服务器项目 |  |
| [Rust MCP Expert](../agents/rust-mcp-expert.agent-zh.md)<br />[![在 VS 中安装代码](https://img.shields.io/badge/VS_Code-Install-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/agent?url=vscode%3Achat-agent%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fagents%2Frust-mcp-expert.agent.md)<br />[![在VS中安装代码内部人士](https://img.shields.io/badge/VS_Code_Insiders-Install-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/agent?url=vscode-insiders%3Achat-agent%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fagents%2Frust-mcp-expert.agent.md) |代理|使用 rmcp SDK 和 tokio 异步运行时进行 Rust MCP 服务器开发的专家助理 [请参阅用法](#rust-mcp-expert) |  |

## 集合用途

### Rust MCP 专家

推荐

这种聊天模式为在 Rust 中构建 MCP 服务器提供了专家指导。

此聊天模式非常适合：
- 使用 Rust 创建新的 MCP 服务器项目
- 使用 tokio 运行时实现异步处理程序
- 使用工具的 rmcp 过程宏
- 设置 stdio、SSE 或 HTTP 传输
- 调试异步 Rust 和所有权问题
- 使用官方 rmcp SDK 学习 Rust MCP 最佳实践
- 使用 Arc 和 RwLock 进行性能优化

为了获得最佳结果，请考虑：
- 使用指令文件为 Rust MCP 开发设置上下文
- 使用提示生成初始项目结构
- 切换到专家聊天模式以获得详细的实施帮助
- 指定您需要哪种传输类型
- 提供有关您需要哪些工具或功能的详细信息
- 提及您是否需要 OAuth 身份验证

---

*此集合包括 3 个针对 **Rust MCP 服务器开发** 的精选项目。*