---
代理人：“代理人”
描述：“根据当前存储库上下文和聊天历史记录，从 Awesome-copilot 存储库建议相关 GitHub Copilot 指令文件，避免与此存储库中的现有指令重复，并识别需要更新的过时指令。”
工具：['编辑'，'搜索'，'runCommands'，'runTasks'，'思考'，'更改'，'testFailure'，'openSimpleBrowser'，'web/fetch'，'githubRepo'，'todos'，'搜索']
---
# 建议很棒的 GitHub Copilot 说明

分析当前存储库上下文并建议来自 [GitHub Awesome-copilot 存储库](https://github.com/github/awesome-copilot/blob/main/docs/README.instructions.md) 的相关副驾驶指令文件，这些文件在此存储库中尚不可用。

## 工艺流程

1. **获取可用指令**：从 [awesome-copilot README.instructions.md](https://github.com/github/awesome-copilot/blob/main/docs/README.instructions.md) 中提取指令列表和描述。必须使用 `#fetch` 工具。
2. **扫描本地指令**：发现`.github/instructions/`文件夹中现有的指令文件
3. **提取描述**：从本地指令文件中读取前面的内容以获取描述和 `applyTo` 模式
4. **获取远程版本**：对于每个本地指令，使用原始 GitHub URL（例如 `https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/<filename>`）从 Awesome-copilot 存储库获取相应版本
5. **比较版本**：将本地指令内容与远程版本进行比较，以确定：
   - 最新的说明（完全匹配）
   - 说明已过时（内容不同）
   - 过时指令的主要区别（描述、applyTo 模式、内容）
6. **分析上下文**：查看聊天历史记录、存储库文件和当前项目需求
7. **比较现有**：对照此存储库中已有的说明进行检查
8. **匹配相关性**：将可用说明与已识别的模式和要求进行比较
9. **当前选项**：显示相关说明，包括说明、理由和可用性状态，包括过时的说明
10. **验证**：确保建议的说明会增加现有说明尚未涵盖的价值
11. **输出**：提供结构化表格，其中包含建议、描述以及 Awesome-copilot 说明和类似本地说明的链接
   **等待**用户请求继续安装或更新特定说明。除非另有指示，否则请勿安装或更新。
12. **下载/更新资产**：对于请求的说明，自动：
    - 将新指令下载到 `.github/instructions/` 文件夹
    - 通过替换为 Awesome-copilot 的最新版本来更新过时的说明
    - 不要调整文件的内容
    - 使用 `#fetch` 工具下载资源，但可以使用 `curl` 和 `#runInTerminal` 工具来确保检索所有内容
    - 使用 `#todos` 工具跟踪进度

## 情境分析标准

🔍 **存储库模式**：
- 使用的编程语言（.cs、.js、.py、.ts 等）
- 框架指标（ASP.NET、React、Azure、Next.js 等）
- 项目类型（Web 应用程序、API、库、工具）
- 开发工作流程要求（测试、CI/CD、部署）

🗨️ **聊天历史上下文**：
- 最近的讨论和痛点
- 技术特定问题
- 编码标准讨论
- 开发工作流程要求

## 输出格式

在结构化表中显示分析结果，将 Awesome-copilot 指令与现有存储库指令进行比较：

|很棒的副驾驶指令 |描述 |已安装 |类似的本地指令|建议理由 |
|------------------------------|-------------|-------------------|---------------------------|---------------------|
| [blazor.instructions.md](https://github.com/github/awesome-copilot/blob/main/instructions/blazor.instructions.md) | Blazor 开发指南 | ✅ 是的 | blazor.instructions.md |现有 Blazor 说明已涵盖 |
| [reactjs.instructions.md](https://github.com/github/awesome-copilot/blob/main/instructions/reactjs.instructions.md) | ReactJS 开发标准 | ❌ 否 |无 |将通过既定模式增强 React 开发 |
| [java.instructions.md](https://github.com/github/awesome-copilot/blob/main/instructions/java.instructions.md) | Java开发最佳实践| ⚠️ 已过时 | java.instructions.md | java.instructions.md | applyTo 模式不同：远程使用 `'**/*.java'` 与本地 `'*.java'` - 建议更新 |

## 本地指令发现过程

1. 列出 `instructions/` 目录中的所有 `*.instructions.md` 文件
2. 对于每个发现的文件，阅读前面的内容以提取 `description` 和 `applyTo` 模式
3. 建立现有指令及其适用文件模式的全面清单
4. 使用此库存以避免建议重复项

## 版本比较流程

1. 对于每个本地指令文件，构造原始 GitHub URL 以获取远程版本：
   - 模式：`https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/<filename>`
2. 使用 `#fetch` 工具获取远程版本
3. 比较整个文件内容（包括前面的内容和正文）
4. 确定具体差异：
   - **前面的内容更改**（描述、applyTo 模式）
   - **内容更新**（指南、示例、最佳实践）
5. 记录过时说明的主要差异
6. 计算相似度以确定是否需要更新

## 文件结构要求

根据 GitHub 文档，copilot-instructions 文件应为：
- **存储库范围的指令**：`.github/copilot-instructions.md`（适用于整个存储库）
- **路径特定指令**：`.github/instructions/NAME.instructions.md`（通过 `applyTo` frontmatter 适用于特定文件模式）
- **社区说明**：`instructions/NAME.instructions.md`（用于共享和分发）

## 前面的内容结构

Awesome-copilot 中的说明文件使用以下前文格式：
```markdown
---
description: 'Brief description of what this instruction provides'
applyTo: '**/*.js,**/*.ts' # Optional: glob patterns for file matching
---
```

## 要求

- 使用 `githubRepo` 工具从 Awesome-copilot 存储库说明文件夹中获取内容
- 扫描本地文件系统以查找 `.github/instructions/` 目录中的现有指令
- 从本地指令文件中读取 YAML 前面的内容以提取描述和 `applyTo` 模式
- 将本地指令与远程版本进行比较以检测过时的指令
- 与此存储库中的现有说明进行比较以避免重复
- 关注当前指令库覆盖范围的差距
- 验证建议的说明是否符合存储库的目的和标准
- 为每项建议提供清晰的理由
- 包含 Awesome-copilot 说明和类似本地说明的链接
- 清楚地识别过时的说明并注明具体差异
- 考虑技术堆栈兼容性和项目特定需求
- 不要提供表格和分析之外的任何其他信息或上下文

## 图标参考

- ✅ 已经安装并且是最新的
- ⚠️已安装但已过时（有更新）
- ❌ 未安装在存储库中

## 更新处理

当发现过时的指令时：
1. 将它们包含在具有 ⚠️ 状态的输出表中
2. 在“建议理由”栏中记录具体差异
3. 提供更新建议并注明关键更改
4. 当用户请求更新时，用远程版本替换整个本地文件
5. 保留 `.github/instructions/` 目录中的文件位置
