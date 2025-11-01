---
mode: 'agent'
description: '基于当前仓库上下文和聊天历史，从awesome-copilot仓库建议相关的GitHub Copilot指令文件，避免与此仓库中现有指令重复。'
tools: ['edit', 'search', 'runCommands', 'runTasks', 'think', 'changes', 'testFailure', 'openSimpleBrowser', 'fetch', 'githubRepo', 'todos', 'search']
---
# 建议优秀的GitHub Copilot指令

分析当前仓库上下文，并建议来自[GitHub awesome-copilot仓库](https://github.com/github/awesome-copilot/blob/main/README.instructions.md)的相关copilot指令文件，这些文件在此仓库中尚不可用。

## 流程

1. **获取可用指令**：从[awesome-copilot README.instructions.md](https://github.com/github/awesome-copilot/blob/main/README.instructions.md)提取指令列表和描述。必须使用`#fetch`工具。
2. **扫描本地指令**：在`.github/instructions/`文件夹中发现现有指令文件
3. **提取描述**：从本地指令文件读取前置内容以获取描述和`applyTo`模式
4. **分析上下文**：审查聊天历史、仓库文件和当前项目需求
5. **比较现有**：与此仓库中已可用的指令对照检查
6. **匹配相关性**：将可用指令与识别的模式和需求进行比较
7. **呈现选项**：显示相关指令，包含描述、理由和可用性状态
8. **验证**：确保建议的指令能够提供现有指令未覆盖的价值
9. **输出**：提供结构化表格，包含建议、描述以及指向awesome-copilot指令和类似本地指令的链接
   **等待**用户请求继续安装特定指令。除非被指示这样做，否则不要安装。
10. **下载资产**：对于请求的指令，自动下载并安装个别指令到`.github/instructions/`文件夹。不要调整文件的内容。使用`#todos`工具跟踪进度。优先使用`#fetch`工具下载资产，但可以使用`#runInTerminal`工具使用`curl`以确保检索所有内容。

## 上下文分析标准

🔍 **仓库模式**：
- 使用的编程语言（.cs、.js、.py、.ts等）
- 框架指示器（ASP.NET、React、Azure、Next.js等）
- 项目类型（Web应用、API、库、工具）
- 开发工作流程需求（测试、CI/CD、部署）

🗨️ **聊天历史上下文**：
- 最近讨论和痛点
- 特定技术问题
- 编码标准讨论
- 开发工作流程需求

## 输出格式

在结构化表格中显示分析结果，比较awesome-copilot指令与现有仓库指令：

| Awesome-Copilot指令 | 描述 | 已安装 | 类似本地指令 | 建议理由 |
|------------------------------|-------------|-------------------|---------------------------|---------------------|
| [blazor.instructions.md](https://github.com/github/awesome-copilot/blob/main/instructions/blazor.instructions.md) | Blazor开发指导 | ❌ 否 | blazor.instructions.md | 已被现有Blazor指令覆盖 |
| [reactjs.instructions.md](https://github.com/github/awesome-copilot/blob/main/instructions/reactjs.instructions.md) | ReactJS开发标准 | ❌ 否 | 无 | 将通过既定模式增强React开发 |
| [java.instructions.md](https://github.com/github/awesome-copilot/blob/main/instructions/java.instructions.md) | Java开发最佳实践 | ❌ 否 | 无 | 可以改进Java代码质量和一致性 |

## 本地指令发现过程

1. 列出`instructions/`目录中的所有`*.instructions.md`文件
2. 对于每个发现的文件，读取前置内容以提取`description`和`applyTo`模式
3. 构建现有指令及其适用文件模式的全面清单
4. 使用此清单避免建议重复项

## 文件结构要求

基于GitHub文档，copilot指令文件应该是：
- **仓库范围指令**：`.github/copilot-instructions.md`（适用于整个仓库）
- **路径特定指令**：`.github/instructions/NAME.instructions.md`（通过`applyTo`前置内容适用于特定文件模式）
- **社区指令**：`instructions/NAME.instructions.md`（用于共享和分发）

## 前置内容结构

awesome-copilot中的指令文件使用此前置内容格式：
```markdown
---
description: '此指令提供内容的简要描述'
applyTo: '**/*.js,**/*.ts' # 可选：用于文件匹配的全局模式
---
```

## 要求

- 使用`githubRepo`工具从awesome-copilot仓库获取内容
- 扫描本地文件系统以查找`instructions/`目录中的现有指令
- 从本地指令文件读取YAML前置内容以提取描述和`applyTo`模式
- 与此仓库中的现有指令比较以避免重复
- 专注于当前指令库覆盖范围的空白
- 验证建议的指令符合仓库的目的和标准
- 为每个建议提供明确的理由
- 包含指向awesome-copilot指令和类似本地指令的链接
- 考虑技术栈兼容性和项目特定需求
- 除了表格和分析外，不提供任何其他信息或上下文

## 图标参考

- ✅ 已在仓库中安装
- ❌ 未在仓库中安装