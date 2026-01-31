---
代理人：“代理人”
描述：“根据当前存储库上下文和聊天历史记录从 Awesome-copilot 存储库建议相关 GitHub Copilot 自定义代理文件，避免与此存储库中的现有自定义代理重复，并识别需要更新的过时代理。”
工具：[“编辑”，“搜索”，“runCommands”，“runTasks”，“更改”，“testFailure”，“openSimpleBrowser”，“fetch”，“githubRepo”，“todos”]
---

# 建议很棒的 GitHub Copilot 自定义代理

分析当前存储库上下文并建议来自 [GitHub Awesome-copilot 存储库](https://github.com/github/awesome-copilot/blob/main/docs/README.agents.md) 的相关自定义代理文件，这些文件在此存储库中尚不可用。自定义代理文件位于 Awesome-copilot 存储库的 [agents](https://github.com/github/awesome-copilot/tree/main/agents) 文件夹中。

## 工艺流程

1. **获取可用的自定义代理**：从 [awesome-copilot README.agents.md](https://github.com/github/awesome-copilot/blob/main/docs/README.agents.md) 中提取自定义代理列表和描述。必须使用 `fetch` 工具。
2. **扫描本地自定义代理**：发现 `.github/agents/` 文件夹中现有的自定义代理文件
3. **提取描述**：从本地自定义代理文件中读取前文以获取描述
4. **获取远程版本**：对于每个本地代理，使用原始 GitHub URL（例如 `https://raw.githubusercontent.com/github/awesome-copilot/main/agents/<filename>`）从 Awesome-copilot 存储库获取相应版本
5. **比较版本**：将本地代理内容与远程版本进行比较，以确定：
   - 最新的代理（完全匹配）
   - 过时的代理（内容不同）
   - 过时代理的主要区别（工具、描述、内容）
6. **分析上下文**：查看聊天历史记录、存储库文件和当前项目需求
7. **匹配相关性**：将可用的自定义代理与已识别的模式和要求进行比较
8. **当前选项**：显示相关的自定义代理，包括说明、理由和可用性状态，包括过时的代理
9. **验证**：确保建议的代理能够增加现有代理尚未涵盖的价值
10. **输出**：提供结构化表格，其中包含建议、描述以及指向 Awesome-copilot 自定义代理和类似本地自定义代理的链接
    **等待**用户请求继续安装或更新特定自定义代理。除非另有指示，否则请勿安装或更新。
11. **下载/更新资产**：对于请求的代理，自动：
    - 将新代理下载到 `.github/agents/` 文件夹
    - 通过替换为 Awesome-copilot 的最新版本来更新过时的代理
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

在结构化表中显示分析结果，将 Awesome-copilot 自定义代理与现有存储库自定义代理进行比较：

| Awesome-Copilot 定制代理 |描述 |已安装 |类似本地定制代理|建议理由 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------------------------- | ------------------------------------------------------------- |
| [振幅实验实现.agent.md](https://github.com/github/awesome-copilot/blob/main/agents/amplitude-experiment-implementation.agent.md) |此自定义代理使用 Amplitude 的 MCP 工具在 Amplitude 内部部署新实验，从而实现无缝变体测试功能并推出产品功能 | ❌ 否 |无 |将增强产品内的实验能力|
| [launchdarkly-flag-cleanup.agent.md](https://github.com/github/awesome-copilot/blob/main/agents/launchdarkly-flag-cleanup.agent.md) | LaunchDarkly 的功能标志清理代理 | ✅ 是的 |启动darkly-flag-cleanup.agent.md |现有 LaunchDarkly 自定义代理已涵盖 |
| [principal-software-engineer.agent.md](https://github.com/github/awesome-copilot/blob/main/agents/principal-software-engineer.agent.md) |提供主要级别的软件工程指导，重点关注卓越工程、技术领导力和务实实施。                            | ⚠️ 已过时 |主体软件工程师.agent.md |工具配置不同：远程使用 `'web/fetch'` 与本地 `'fetch'` - 建议更新 |

## 本地代理发现过程

1. 列出 `.github/agents/` 目录中所有 `*.agent.md` 文件
2. 对于每个发现的文件，阅读前面的内容以提取 `description`
3. 建立现有代理商的全面库存
4. 使用此库存以避免建议重复项

## 版本比较流程

1. 对于每个本地代理文件，构建原始 GitHub URL 以获取远程版本：
   - 模式：`https://raw.githubusercontent.com/github/awesome-copilot/main/agents/<filename>`
2. 使用 `fetch` 工具获取远程版本
3. 比较整个文件内容（包括标题、工具数组和正文）
4. 确定具体差异：
   - **前面的内容更改**（描述、工具）
   - **工具数组修改**（添加、删除或重命名工具）
   - **内容更新**（说明、示例、指南）
5. 记录过时代理的主要差异
6. 计算相似度以确定是否需要更新

## 要求

- 使用 `githubRepo` 工具从 Awesome-copilot 存储库代理文件夹中获取内容
- 扫描本地文件系统以查找 `.github/agents/` 目录中的现有代理
- 从本地代理文件中读取 YAML Front Matter 以提取描述
- 将本地代理与远程版本进行比较以检测过时的代理
- 与此存储库中的现有代理进行比较以避免重复
- 关注当前代理库覆盖范围的差距
- 验证建议的代理是否符合存储库的目的和标准
- 为每项建议提供清晰的理由
- 包含 Awesome-copilot 代理和类似本地代理的链接
- 清楚地识别过时的代理并注明具体差异
- 不要提供表格和分析之外的任何其他信息或上下文

## 图标参考

- ✅ 已经安装并且是最新的
- ⚠️已安装但已过时（有更新）
- ❌ 未安装在存储库中

## 更新处理

当发现过时的代理时：
1. 将它们包含在具有 ⚠️ 状态的输出表中
2. 在“建议理由”栏中记录具体差异
3. 提供更新建议并注明关键更改
4. 当用户请求更新时，用远程版本替换整个本地文件
5. 保留 `.github/agents/` 目录中的文件位置
