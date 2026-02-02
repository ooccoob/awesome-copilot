---
description: 'Guidelines for creating high-quality Agent Skills for GitHub Copilot'
applyTo: '**/.github/skills/**/SKILL.md, **/.claude/skills/**/SKILL.md'
---

# 代理技能文件指南

有关创建有效且可移植的代理技能的说明，这些技能可通过专业功能、工作流程和捆绑资源增强 GitHub Copilot。

## 什么是代理技能？

代理技能是独立的文件夹，其中包含说明和捆绑资源，可教授 AI 代理专业功能。与自定义指令（定义编码标准）不同，技能支持特定于任务的工作流程，其中可以包括脚本、示例、模板和参考数据。

主要特点：
- **便携式**：跨 VS Code、Copilot CLI 和 Copilot 编码代理工作
- **渐进式加载**：仅在与用户请求相关时加载
- **资源捆绑**：可以包含脚本、模板、示例以及说明
- **按需**：根据提示相关性自动激活

## 目录结构

技能存储在特定位置：

|地点 |范围 |推荐|
|----------|-------|----------------|
| __代码0__ |项目/存储库 |推荐项目技能|
| __代码0__ |项目/存储库 |旧版，向后兼容 |
| __代码0__ |个人（用户范围）|个人技能推荐|
| __代码0__ |个人（用户范围）|旧版，向后兼容 |

每个技能**必须**有自己的子目录，其中至少包含一个 `SKILL.md` 文件。

## 所需的 SKILL.md 格式

### 前言（必填）

```yaml
---
name: webapp-testing
description: Toolkit for testing local web applications using Playwright. Use when asked to verify frontend functionality, debug UI behavior, capture browser screenshots, check for visual regressions, or view browser console logs. Supports Chrome, Firefox, and WebKit browsers.
license: Complete terms in LICENSE.txt
---
```

|领域 |必填 |限制条件|
|-------|----------|-------------|
| __代码0__ |是的 |小写字母、空格连字符，最多 64 个字符（例如 `webapp-testing`）|
| __代码0__ |是的 |功能和用例的清晰描述，最多 1024 个字符 |
| __代码0__ |没有 |引用 LICENSE.txt（例如 `Complete terms in LICENSE.txt`）或 SPDX 标识符 |

### 描述 最佳实践

**关键**：`description` 字段是自动技能发现的主要机制。 Copilot 仅读取 `name` 和 `description` 来决定是否加载技能。如果你的描述含糊不清，该技能将永远不会被激活。

**描述中应包含的内容：**
1. **什么**该技能的作用（能力）
2. **何时** 使用它（特定触发器、场景、文件类型或用户请求）
3. **用户可能在提示中提到的关键字**

**好的描述：**
```yaml
description: Toolkit for testing local web applications using Playwright. Use when asked to verify frontend functionality, debug UI behavior, capture browser screenshots, check for visual regressions, or view browser console logs. Supports Chrome, Firefox, and WebKit browsers.
```

**描述不准确：**
```yaml
description: Web testing helpers
```

糟糕的描述失败是因为：
- 没有特定的触发器（Copilot 应何时加载此触发器？）
- 没有关键字（什么用户提示会匹配？）
- 没有能力（它实际上能做什么？）

### 正文内容

正文包含 Copilot 在激活技能后加载的详细说明。推荐栏目：

|部分|目的|
|---------|---------|
| __代码0__ |简要概述此技能的用途 |
| __代码0__ |场景列表（强化描述触发）|
| __代码0__ |所需工具、依赖项、环境设置 |
| __代码0__ |常见任务的编号步骤 |
| __代码0__ |常见问题及解决方案表|
| __代码0__ |捆绑文档或外部资源的链接 |

## 捆绑资源

技能可以包括 Copilot 按需访问的其他文件：

### 支持的资源类型

|文件夹|目的|加载到上下文中？ |示例文件 |
|--------|---------|---------------------|---------------|
| __代码0__ |执行特定操作的可执行自动化 |执行时 | __代码1__、__代码2__、__代码3__ |
| __代码0__ | AI 代理阅读文档以指导决策 |是的，当引用时 | __代码1__、__代码2__、__代码3__ |
| __代码0__ | **静态文件在输出中按原样使用**（未由 AI 代理修改）|没有 | __代码1__、__代码2__、__代码3__ |
| __代码0__ | **AI 代理修改**并构建的起始代码/支架 |是的，当引用时 | `viewer.html`（插入算法），`hello-world/`（扩展）|

### 目录结构示例

```
.github/skills/my-skill/
├── SKILL.md              # Required: Main instructions
├── LICENSE.txt           # Recommended: License terms (Apache 2.0 typical)
├── scripts/              # Optional: Executable automation
│   ├── helper.py         # Python script
│   └── helper.ps1        # PowerShell script
├── references/           # Optional: Documentation loaded into context
│   ├── api_reference.md
│   ├── workflow-setup.md     # Detailed workflow (>5 steps)
│   └── workflow-deployment.md
├── assets/               # Optional: Static files used AS-IS in output
│   ├── baseline.png      # Reference image for comparison
│   └── report-template.html
└── templates/            # Optional: Starter code the AI agent modifies
    ├── scaffold.py       # Code scaffold the AI agent customizes
    └── config.template   # Config template the AI agent fills in
```

> **LICENSE.txt**：创建技能时，从 https://www.apache.org/licenses/LICENSE-2.0.txt 下载 Apache 2.0 许可证文本并保存为 `LICENSE.txt`。更新附录部分中的版权年份和所有者。

### 资产与模板：主要区别

**资产**是静态资源**在输出中保持不变**：
- 嵌入到生成文档中的 `logo.png`
- A `report-template.html` 复制为输出格式
- 应用于文本渲染的 `custom-font.ttf`

**模板**是**AI代理主动修改的起始代码/支架**：
- AI 代理插入逻辑的 `scaffold.py`
- `config.template`，AI 代理根据用户要求填写值
- AI 代理通过新功能扩展的 `hello-world/` 项目目录

**经验法则**：如果 AI 代理读取并构建文件内容 → `templates/`。如果文件在输出中按原样使用 → `assets/`。

### 引用 SKILL.md 中的资源

使用相对路径来引用技能目录中的文件：

```markdown
## Available Scripts

Run the [helper script](./scripts/helper.py) to automate common tasks.

See [API reference](./references/api_reference-zh.md) for detailed documentation.

Use the [scaffold](./templates/scaffold.py) as a starting point.
```

## 渐进式加载架构

技能使用三级加载来提高效率：

|水平|负载是什么？当 |
|-------|------------|------|
| 1. 发现 |仅 `name` 和 `description` |始终（轻量级元数据）|
| 2. 使用说明|完整的 `SKILL.md` 正文 |当请求与描述匹配时 |
| 3. 资源 |脚本、示例、文档 |仅当副驾驶引用它们时 |

这意味着：
- 在不消耗上下文的情况下安装许多技能
- 每个任务仅加载相关内容
- 除非明确需要，否则不会加载资源

## 内容指南

### 写作风格

- 使用祈使语气：“运行”、“创建”、“配置”（而不是“你应该运行”）
- 具体且可操作
- 包含带参数的精确命令
- 显示有帮助的预期输出
- 保持章节集中且易于浏览

### 脚本要求

包含脚本时，首选跨平台语言：

|语言 |使用案例|
|----------|----------|
|蟒蛇 |复杂的自动化、数据处理 |
|普沃什 | PowerShell 核心脚本 |
| Node.js |基于 JavaScript 的工具 |
| bash/shell |简单的自动化任务 |

最佳实践：
- 包括帮助/使用文档（`--help` 标志）
- 使用清晰的消息优雅地处理错误
- 避免存储凭据或秘密
- 尽可能使用相对路径

### 何时捆绑脚本

在以下情况下将脚本纳入您的技能中：
- 相同的代码会被代理重复重写
- 确定性可靠性至关重要（例如文件操作、API 调用）
- 复杂的逻辑受益于预先测试而不是每次生成
- 该操作具有独立的目的，可以独立发展
- 可测试性很重要——脚本可以进行单元测试和验证
- 可预测的行为优于动态生成

脚本支持演进：当复杂性可能增加、需要跨调用的一致行为或需要未来的可扩展性时，即使是简单的操作也会受益于作为脚本实现。

### 安全考虑

- 脚本依赖于现有的凭证助手（无凭证存储）
- 仅包含 `--force` 标志用于破坏性操作
- 在不可逆转的操作之前警告用户
- 记录任何网络操作或外部调用

## 常见模式

### 参数表模式

清楚记录参数：

```markdown
| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `--input` | Yes | - | Input file or URL to process |
| `--action` | Yes | - | Action to perform |
| `--verbose` | No | `false` | Enable verbose output |
```

## 验证清单

发布技能之前：

- [ ] `SKILL.md` 与 `name` 和 `description` 具有有效的 frontmatter
- [ ] `name` 为小写字母，带连字符，≤64 个字符
- [ ] `description` 清楚地说明了它的作用、使用时间以及相关的关键字
- [ ] 正文包括何时使用、先决条件和分步工作流程
- [ ] SKILL.md 正文保持在 500 行以下（将大内容拆分到 `references/` 文件夹中）
- [ ] 大型工作流程（>5 个步骤）分为 `references/` 文件夹，其中包含来自 SKILL.md 的清晰链接
- [ ] 脚本包括帮助文档和错误处理
- [ ] 用于所有资源引用的相对路径
- [ ] 没有硬编码的凭据或秘密

## 工作流执行模式

执行多步骤工作流程时，创建一个 TODO 列表，其中每个步骤引用相关文档：

```markdown
## TODO
- [ ] Step 1: Configure environment - see [workflow-setup.md](./references/workflow-setup-zh.md#environment)
- [ ] Step 2: Build project - see [workflow-setup.md](./references/workflow-setup-zh.md#build)
- [ ] Step 3: Deploy to staging - see [workflow-deployment.md](./references/workflow-deployment-zh.md#staging)
- [ ] Step 4: Run validation - see [workflow-deployment.md](./references/workflow-deployment-zh.md#validation)
- [ ] Step 5: Deploy to production - see [workflow-deployment.md](./references/workflow-deployment-zh.md#production)
```

这确保了可追溯性，并允许在中断时恢复工作流程。

## 相关资源

- [代理技能规范](https://agentskills.io/)
- [VS Code Agent 技能文档](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [参考技能库](https://github.com/anthropics/skills)
- [超棒的副驾驶技能](https://github.com/github/awesome-copilot/blob/main/docs/README.skills.md)
