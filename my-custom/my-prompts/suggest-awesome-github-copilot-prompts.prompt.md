---
agent: 'agent'
description: 'Suggest relevant GitHub Copilot prompt files from the awesome-copilot repository based on current repository context and chat history, avoiding duplicates with existing prompts in this repository, and identifying outdated prompts that need updates.'
tools: ['edit', 'search', 'runCommands', 'runTasks', 'think', 'changes', 'testFailure', 'openSimpleBrowser', 'web/fetch', 'githubRepo', 'todos', 'search']
---
# 建议很棒的 GitHub Copilot 提示

分析当前存储库上下文并建议来自 [GitHub Awesome-copilot 存储库](https://github.com/github/awesome-copilot/blob/main/docs/README.prompts.md) 的相关提示文件，这些文件在此存储库中尚不可用。

## 工艺流程

1. **获取可用提示**：从 [awesome-copilot README.prompts.md](https://github.com/github/awesome-copilot/blob/main/docs/README.prompts.md) 中提取提示列表和描述。必须使用 `#fetch` 工具。
2. **扫描本地提示**：发现 `.github/prompts/` 文件夹中现有的提示文件
3. **提取描述**：从本地提示文件中读取前文以获取描述
4. **获取远程版本**：对于每个本地提示，使用原始 GitHub URL（例如 `https://raw.githubusercontent.com/github/awesome-copilot/main/prompts/<filename>`）从 Awesome-copilot 存储库获取相应版本
5. **比较版本**：将本地提示内容与远程版本进行比较，以确定：
   - 最新的提示（完全匹配）
   - 提示已过时（内容不同）
   - 过时提示的主要区别（工具、描述、内容）
6. **分析上下文**：查看聊天历史记录、存储库文件和当前项目需求
7. **比较现有**：对照此存储库中已有的提示进行检查
8. **匹配相关性**：将可用提示与已识别的模式和要求进行比较
9. **当前选项**：显示相关提示，包括说明、理由和可用性状态，包括过时的提示
10. **验证**：确保建议的提示会增加现有提示尚未涵盖的价值
11. **输出**：提供结构化表格，其中包含建议、描述以及 Awesome-copilot 提示和类似本地提示的链接
    **等待**用户请求继续安装或更新特定提示。除非另有指示，否则请勿安装或更新。
12. **下载/更新资产**：对于请求的提示，自动：
    - 将新提示下载到 `.github/prompts/` 文件夹
    - 通过替换为 Awesome-copilot 的最新版本来更新过时的提示
    - 不要调整文件的内容
    - 使用 `#fetch` 工具下载资源，但可以使用 `curl` 和 `#runInTerminal` 工具来确保检索所有内容
    - 使用 `#todos` 工具跟踪进度

## 情境分析标准

🔍 **存储库模式**：
- 使用的编程语言（.cs、.js、.py 等）
- 框架指标（ASP.NET、React、Azure 等）
- 项目类型（Web 应用程序、API、库、工具）
- 文档需求（自述文件、规格、ADR）

🗨️ **聊天历史上下文**：
- 最近的讨论和痛点
- 功能请求或实施需求
- 代码审查模式
- 开发工作流程要求

## 输出格式

在结构化表中显示分析结果，将 Awesome-copilot 提示与现有存储库提示进行比较：

|很棒的副驾驶提示|描述 |已安装 |类似的本地提示|建议理由 |
|-------------------------|-------------|-------------------|---------------------|---------------------|
| [代码审查.提示.md](https://github.com/github/awesome-copilot/blob/main/prompts/code-review.prompt.md) |自动代码审查提示 | ❌ 否 |无 |将通过标准化代码审查流程来增强开发工作流程 |
| [文档.提示.md](https://github.com/github/awesome-copilot/blob/main/prompts/documentation.prompt.md) |生成项目文档 | ✅ 是的 |创建_oo_component_documentation.prompt.md |现有文档提示已涵盖 |
| [调试.提示.md](https://github.com/github/awesome-copilot/blob/main/prompts/debugging.prompt.md) |调试帮助提示| ⚠️ 已过时 |调试.提示.md |工具配置不同：远程使用 `'codebase'` 与本地缺失 - 建议更新 |

## 本地提示发现过程

1. 列出 `.github/prompts/` 目录中所有 `*.prompt.md` 文件
2. 对于每个发现的文件，阅读前面的内容以提取 `description`
3. 建立现有提示的全面清单
4. 使用此库存以避免建议重复项

## 版本比较流程

1. 对于每个本地提示文件，构造原始 GitHub URL 以获取远程版本：
   - 模式：`https://raw.githubusercontent.com/github/awesome-copilot/main/prompts/<filename>`
2. 使用 `#fetch` 工具获取远程版本
3. 比较整个文件内容（包括前面的内容和正文）
4. 确定具体差异：
   - **前面的内容更改**（描述、工具、模式）
   - **工具数组修改**（添加、删除或重命名工具）
   - **内容更新**（说明、示例、指南）
5. 记录过时提示的关键差异
6. 计算相似度以确定是否需要更新

## 要求

- 使用 `githubRepo` 工具从 Awesome-copilot 存储库提示文件夹中获取内容
- 扫描本地文件系统以查找 `.github/prompts/` 目录中的现有提示
- 从本地提示文件中读取 YAML 前面的内容以提取描述
- 将本地提示与远程版本进行比较以检测过时的提示
- 与此存储库中的现有提示进行比较以避免重复
- 关注当前即时图书馆覆盖率的差距
- 验证建议的提示是否符合存储库的目的和标准
- 为每项建议提供清晰的理由
- 包含 Awesome-copilot 提示和类似本地提示的链接
- 清楚地识别过时的提示并注明具体差异
- 不要提供表格和分析之外的任何其他信息或上下文


## 图标参考

- ✅ 已经安装并且是最新的
- ⚠️已安装但已过时（有更新）
- ❌ 未安装在存储库中

## 更新处理

当发现过时的提示时：
1. 将它们包含在具有 ⚠️ 状态的输出表中
2. 在“建议理由”栏中记录具体差异
3. 提供更新建议并注明关键更改
4. 当用户请求更新时，用远程版本替换整个本地文件
5. 保留 `.github/prompts/` 目录中的文件位置
