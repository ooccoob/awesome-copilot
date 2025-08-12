---
mode: 'agent'
description: '基于当前仓库上下文与对话历史，从 awesome-copilot 仓库中推荐相关的 GitHub Copilot chatmode 文件，并避免与本仓库已有 chatmode 重复。'
tools: ['changes', 'codebase', 'editFiles', 'fetch', 'findTestFiles', 'githubRepo', 'new', 'openSimpleBrowser', 'problems', 'runCommands', 'runTasks', 'runTests', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI']
---

# 推荐 Awesome GitHub Copilot Chatmodes

分析当前仓库上下文，推荐来自 [GitHub awesome-copilot 仓库](https://github.com/github/awesome-copilot/tree/main/chatmodes) 的相关 chatmode 文件，且不与本仓库已存在的 chatmode 重复。

## 流程

1. 获取可用 Chatmodes：从 [awesome-copilot chatmodes 目录](https://github.com/github/awesome-copilot/tree/main/chatmodes) 提取清单与描述。
2. 扫描本地 Chatmodes：发现 `.github/chatmodes/` 目录下已存在的 chatmode 文件。
3. 提取描述：读取本地 chatmode 文件 front matter 获取 description。
4. 分析上下文：审阅聊天历史、仓库文件与当前项目需求。
5. 去重对比：与本仓库现有 chatmodes 比对避免重复。
6. 匹配相关性：将可用 chatmodes 与识别出的模式和需求对照匹配。
7. 呈现选项：输出包含描述、理由与可用性状态的建议列表。
8. 校验：确保建议的 chatmodes 能补足目前缺口、确有价值。
9. 输出：以结构化表格展示建议、描述，以及到 awesome-copilot 与本地相似 chatmode 的链接。
10. 后续：若提出建议，提供可由 GitHub Copilot 自动执行的添加步骤，并在用户确认时支持自动执行。

## 上下文分析维度

🔎 仓库模式：
- 使用的编程语言（.cs、.js、.py 等）
- 框架指示（ASP.NET、React、Azure 等）
- 项目类型（Web 应用、API、库、工具）
- 文档需求（README、规格、ADR）

🛑 对话历史：
- 近期讨论与痛点
- 特性需求或实现需求
- 代码评审模式
- 开发流程要求

## 输出格式

以结构化表格对比 awesome-copilot 与本地 chatmodes：

| Awesome-Copilot Chatmode | 描述 | 是否已安装 | 本地相似 Chatmode | 建议理由 |
|---------------------------|------|------------|-------------------|----------|
| [code-reviewer.chatmode.md](https://github.com/github/awesome-copilot/blob/main/chatmodes/code-reviewer.chatmode.md) | 专用代码评审 chatmode | ❌ No | None | 为开发流程引入专职代码评审能力 |
| [architect.chatmode.md](https://github.com/github/awesome-copilot/blob/main/chatmodes/architect.chatmode.md) | 软件架构指导 | ✅ Yes | azure_principal_architect.chatmode.md | 已由现有架构类 chatmode 覆盖 |
| [debugging-expert.chatmode.md](https://github.com/github/awesome-copilot/blob/main/chatmodes/debugging-expert.chatmode.md) | 调试专家 chatmode | ❌ No | None | 提升排障效率与研发速度 |

## 本地 Chatmodes 发现流程

1. 枚举 `.github/chatmodes/` 目录下所有 `*.chatmode.md` 文件。
2. 读取各文件 front matter 的 `description`。
3. 构建本地 chatmodes 清单。
4. 用该清单避免重复推荐。

## 要求

- 使用 `githubRepo` 获取 awesome-copilot 的 chatmodes 列表。
- 扫描 `.github/chatmodes/` 目录，读取本地已有 chatmodes。
- 解析本地文件 front matter，提取 description。
- 针对本仓库缺口提出建议，避免重复。
- 给出清晰的建议理由与双向链接（上游与本地）。
- 输出仅包含表格与必要分析，不添加无关内容。

## 图标说明

- ✅ 已安装
- ❌ 未安装
