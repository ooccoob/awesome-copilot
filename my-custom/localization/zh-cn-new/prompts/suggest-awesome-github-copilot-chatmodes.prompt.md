---
mode: 'agent'
description: '基于当前仓库上下文和聊天历史，从awesome-copilot仓库建议相关的GitHub Copilot自定义聊天模式文件，避免与此仓库中现有自定义聊天模式重复。'
tools: ['edit', 'search', 'runCommands', 'runTasks', 'think', 'changes', 'testFailure', 'openSimpleBrowser', 'fetch', 'githubRepo', 'todos', 'search']
---

# 建议优秀的GitHub Copilot自定义聊天模式

分析当前仓库上下文，并建议来自[GitHub awesome-copilot仓库](https://github.com/github/awesome-copilot/blob/main/README.chatmodes.md)的相关自定义聊天模式文件，这些文件在此仓库中尚不可用。自定义聊天模式文件位于awesome-copilot仓库的[chatmodes](https://github.com/github/awesome-copilot/tree/main/chatmodes)文件夹中。

## 流程

1. **获取可用的自定义聊天模式**：从[awesome-copilot README.chatmodes.md](https://github.com/github/awesome-copilot/blob/main/README.chatmodes.md)提取自定义聊天模式列表和描述。必须使用`#fetch`工具。
2. **扫描本地自定义聊天模式**：在`.github/chatmodes/`文件夹中发现现有的自定义聊天模式文件
3. **提取描述**：从本地自定义聊天模式文件读取前置内容以获取描述
4. **分析上下文**：审查聊天历史、仓库文件和当前项目需求
5. **比较现有**：与此仓库中已可用的自定义聊天模式对照检查
6. **匹配相关性**：将可用的自定义聊天模式与识别的模式和需求进行比较
7. **呈现选项**：显示相关自定义聊天模式，包含描述、理由和可用性状态
8. **验证**：确保建议的聊天模式能够提供现有聊天模式未覆盖的价值
9. **输出**：提供结构化表格，包含建议、描述以及指向awesome-copilot自定义聊天模式和类似本地自定义聊天模式的链接
   **等待**用户请求继续安装特定的自定义聊天模式。除非被指示这样做，否则不要安装。
10. **下载资产**：对于请求的聊天模式，自动下载并安装个别聊天模式到`.github/chatmodes/`文件夹。不要调整文件的内容。使用`#todos`工具跟踪进度。优先使用`#fetch`工具下载资产，但可以使用`#runInTerminal`工具使用`curl`以确保检索所有内容。

## 上下文分析标准

🔍 **仓库模式**：
- 使用的编程语言（.cs、.js、.py等）
- 框架指示器（ASP.NET、React、Azure等）
- 项目类型（Web应用、API、库、工具）
- 文档需求（README、规范、ADR）

🗨️ **聊天历史上下文**：
- 最近讨论和痛点
- 功能请求或实现需求
- 代码审查模式
- 开发工作流程需求

## 输出格式

在结构化表格中显示分析结果，比较awesome-copilot自定义聊天模式与现有仓库自定义聊天模式：

| Awesome-Copilot自定义聊天模式 | 描述 | 已安装 | 类似本地自定义聊天模式 | 建议理由 |
|---------------------------|-------------|-------------------|-------------------------|---------------------|
| [code-reviewer.chatmode.md](https://github.com/github/awesome-copilot/blob/main/chatmodes/code-reviewer.chatmode.md) | 专门的代码审查自定义聊天模式 | ❌ 否 | 无 | 通过专用代码审查辅助增强开发工作流程 |
| [architect.chatmode.md](https://github.com/github/awesome-copilot/blob/main/chatmodes/architect.chatmode.md) | 软件架构指导 | ✅ 是 | azure_principal_architect.chatmode.md | 已被现有架构自定义聊天模式覆盖 |
| [debugging-expert.chatmode.md](https://github.com/github/awesome-copilot/blob/main/chatmodes/debugging-expert.chatmode.md) | 调试辅助自定义聊天模式 | ❌ 否 | 无 | 可以提高开发团队的故障排除效率 |

## 本地聊天模式发现过程

1. 列出`.github/chatmodes/`目录中的所有`*.chatmode.md`文件
2. 对于每个发现的文件，读取前置内容以提取`description`
3. 构建现有聊天模式的全面清单
4. 使用此清单避免建议重复项

## 要求

- 使用`githubRepo`工具从awesome-copilot仓库聊天模式文件夹获取内容
- 扫描本地文件系统以查找`.github/chatmodes/`目录中的现有聊天模式
- 从本地聊天模式文件读取YAML前置内容以提取描述
- 与此仓库中的现有聊天模式比较以避免重复
- 专注于当前聊天模式库覆盖范围的空白
- 验证建议的聊天模式符合仓库的目的和标准
- 为每个建议提供明确的理由
- 包含指向awesome-copilot聊天模式和类似本地聊天模式的链接
- 除了表格和分析外，不提供任何其他信息或上下文

## 图标参考

- ✅ 已在仓库中安装
- ❌ 未在仓库中安装