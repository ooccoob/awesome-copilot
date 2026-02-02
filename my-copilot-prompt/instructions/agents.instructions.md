---
description: 'Guidelines for creating custom agent files for GitHub Copilot'
applyTo: '**/*.agent.md'
---

# 自定义代理文件指南

有关创建有效且可维护的自定义代理文件的说明，这些文件为 GitHub Copilot 中的特定开发任务提供专业知识。

## 项目背景

- 目标受众：为 GitHub Copilot 创建自定义代理的开发人员
- 文件格式：带有 YAML frontmatter 的 Markdown
- 文件命名约定：小写字母加连字符（例如 `test-specialist.agent.md`）
- 位置：`.github/agents/` 目录（存储库级别）或 `agents/` 目录（组织/企业级别）
- 目的：定义专门的代理，为特定任务提供定制的专业知识、工具和说明
- 官方文档：https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents

## 必需的前言

每个代理文件必须包含带有以下字段的 YAML frontmatter：

```yaml
---
description: 'Brief description of the agent purpose and capabilities'
name: 'Agent Display Name'
tools: ['read', 'edit', 'search']
model: 'Claude Sonnet 4.5'
target: 'vscode'
infer: true
---
```

### 核心前沿属性

#### **描述**（必填）
- 单引号字符串，清楚地说明代理的目的和领域专业知识
- 应简洁（50-150 个字符）且可操作
- 示例：`'Focuses on test coverage, quality, and testing best practices'`

#### **姓名**（可选）
- UI 中代理的显示名称
- 如果省略，则默认为文件名（不带 `.md` 或 `.agent.md`）
- 使用标题大小写并具有描述性
- 示例：`'Testing Specialist'`

#### **工具**（可选）
- 代理可以使用的工具名称或别名列表
- 支持逗号分隔的字符串或 YAML 数组格式
- 如果省略，代理可以访问所有可用工具
- 有关详细信息，请参阅下面的“工具配置”部分

#### **型号**（强烈推荐）
- 指定代理应使用哪种 AI 模型
- 在 VS Code、JetBrains IDE、Eclipse 和 Xcode 中受支持
- 示例：`'Claude Sonnet 4.5'`、`'gpt-4'`、`'gpt-4o'`
- 根据代理复杂性和所需功能进行选择

#### **目标**（可选）
- 指定目标环境：`'vscode'` 或 `'github-copilot'`
- 如果省略，则代理在两种环境中均可用
- 当代理具有特定于环境的功能时使用

#### **推断**（可选）
- 布尔值控制 Copilot 是否可以根据上下文自动使用该代理
- 默认值：`true`（如果省略）
- 设置为 `false` 以要求手动选择代理

#### **元数据**（可选，仅限 GitHub.com）
- 具有用于代理注释的名称/值对的对象
- 示例：`metadata: { category: 'testing', version: '1.0' }`
- VS Code 不支持

#### **mcp-servers**（可选，仅限组织/企业）
- 配置仅适用于此代理的 MCP 服务器
- 仅支持组织/企业级代理
- 请参阅下面的“MCP 服务器配置”部分

#### **切换**（可选，仅限 VS Code）
- 启用引导式顺序工作流程，通过建议的后续步骤在代理之间进行转换
- 切换配置列表，每个配置指定一个目标代理和可选提示
- 聊天响应完成后，会出现切换按钮，允许用户移至下一个客服人员
- 仅在 VS Code（版本 1.106+）中受支持
- 有关详细信息，请参阅下面的“切换配置”部分

## 切换配置

切换使您能够创建引导式顺序工作流程，在自定义代理之间无缝过渡。这对于编排多步骤开发工作流程非常有用，用户可以在进入下一个步骤之前查看和批准每个步骤。

### 常见的切换模式

- **规划→实施**：在规划代理中生成计划，然后交给实施代理开始编码
- **实施→审查**：完成实施，然后切换到代码审查代理来检查质量和安全问题
- **编写失败的测试→编写通过的测试**：生成失败的测试，然后移交以实现使这些测试通过的代码
- **研究→文档**：研究一个主题，然后过渡到文档代理来编写指南

### 交接前沿结构

使用 `handoffs` 字段在代理文件的 YAML frontmatter 中定义切换：

```yaml
---
description: 'Brief description of the agent'
name: 'Agent Name'
tools: ['search', 'read']
handoffs:
  - label: Start Implementation
    agent: implementation
    prompt: 'Now implement the plan outlined above.'
    send: false
  - label: Code Review
    agent: code-review
    prompt: 'Please review the implementation for quality and security issues.'
    send: false
---
```

### 切换属性

列表中的每个切换必须包含以下属性：

|物业 |类型 |必填 |描述 |
|----------|------|----------|-------------|
| __代码0__ |字符串|是的 |聊天界面切换按钮上显示的显示文字 |
| __代码0__ |字符串|是的 |要切换到的目标代理标识符（不带 `.agent.md` 的名称或文件名）|
| __代码0__ |字符串|没有 |预填写目标代理聊天输入的提示文本 |
| __代码0__ |布尔 |没有 |如果为 `true`，则自动将提示提交给目标代理（默认值：`false`） |

### 切换行为

- **按钮显示**：聊天响应完成后，切换按钮将显示为交互式建议
- **上下文保留**：当用户选择切换按钮时，他们会切换到目标座席并保留对话上下文
- **预填充提示**：如果指定了 `prompt`，它将出现在目标代理的聊天输入中预填充
- **手动 vs 自动**：当 `send: false` 时，用户必须查看并手动发送预先填写的提示；当`send: true`时，提示自动提交

### 切换配置指南

#### 何时使用切换

- **多步骤工作流程**：跨专业代理分解复杂的任务
- **质量门**：确保实施阶段之间的审查步骤
- **引导流程**：指导用户完成结构化的开发流程
- **技能转换**：从规划/设计到实施/测试专家

#### 最佳实践

- **清晰标签**：使用以行动为导向的标签，清楚地指示下一步
  - ✅ 好：“开始实施”、“安全审查”、“编写测试”
  - ❌ 避免：“下一步”、“去找代理”、“做某事”

- **相关提示**：提供引用已完成工作的上下文感知提示
  - ✅ 好：`'Now implement the plan outlined above.'`
  - ❌ 避免：没有上下文的通用提示

- **选择性使用**：不要向每个可能的座席进行交接；专注于逻辑工作流程转换
  - 每个代理最多执行 2-3 个最相关的后续步骤
  - 仅为工作流程中自然遵循的座席添加移交

- **代理依赖性**：在创建切换之前确保目标代理存在
  - 向不存在的代理的移交将被默默忽略
  - 测试切换以验证它们按预期工作

- **提示内容**：保持提示简洁且可操作
  - 参考当前代理的工作，不重复内容
  - 提供目标代理可能需要的任何必要上下文

### 示例：完整的工作流程

以下是三个代理通过交接创建完整工作流程的示例：

**规划代理** (`planner.agent.md`)：
```yaml
---
description: 'Generate an implementation plan for new features or refactoring'
name: 'Planner'
tools: ['search', 'read']
handoffs:
  - label: Implement Plan
    agent: implementer
    prompt: 'Implement the plan outlined above.'
    send: false
---
# Planner Agent
You are a planning specialist. Your task is to:
1. Analyze the requirements
2. Break down the work into logical steps
3. Generate a detailed implementation plan
4. Identify testing requirements

Do not write any code - focus only on planning.
```

**实施代理** (`implementer.agent.md`)：
```yaml
---
description: 'Implement code based on a plan or specification'
name: 'Implementer'
tools: ['read', 'edit', 'search', 'execute']
handoffs:
  - label: Review Implementation
    agent: reviewer
    prompt: 'Please review this implementation for code quality, security, and adherence to best practices.'
    send: false
---
# Implementer Agent
You are an implementation specialist. Your task is to:
1. Follow the provided plan or specification
2. Write clean, maintainable code
3. Include appropriate comments and documentation
4. Follow project coding standards

Implement the solution completely and thoroughly.
```

**审核代理** (`reviewer.agent.md`)：
```yaml
---
description: 'Review code for quality, security, and best practices'
name: 'Reviewer'
tools: ['read', 'search']
handoffs:
  - label: Back to Planning
    agent: planner
    prompt: 'Review the feedback above and determine if a new plan is needed.'
    send: false
---
# Code Review Agent
You are a code review specialist. Your task is to:
1. Check code quality and maintainability
2. Identify security issues and vulnerabilities
3. Verify adherence to project standards
4. Suggest improvements

Provide constructive feedback on the implementation.
```

此工作流程允许开发人员：
1. 从 Planner 代理开始创建详细计划
2. 交给实施者代理根据计划编写代码
3. 交给Reviewer代理检查实施情况
4. 如果发现重大问题，可选择将其交回规划

### 版本兼容性

- **VS Code**：VS Code 1.106 及更高版本支持切换
- **GitHub.com**：目前不支持；代理转换工作流程使用不同的机制
- **其他 IDE**：有限支持或不支持；专注于 VS Code 实现以实现最大兼容性

## 工具配置

### 工具规范策略

**启用所有工具**（默认）：
```yaml
# Omit tools property entirely, or use:
tools: ['*']
```

**启用特定工具**：
```yaml
tools: ['read', 'edit', 'search', 'execute']
```

**启用 MCP 服务器工具**：
```yaml
tools: ['read', 'edit', 'github/*', 'playwright/navigate']
```

**禁用所有工具**：
```yaml
tools: []
```

### 标准工具别名

所有别名都不区分大小写：

|别名 |别名 |类别 |描述 |
|-------|------------------|----------|-------------|
| __代码0__ | shell、Bash、powershell |外壳执行 |在适当的 shell 中执行命令 |
| __代码0__ |阅读，笔记本阅读，查看 |文件读取 |读取文件内容 |
| __代码0__ |编辑、多重编辑、写入、NotebookEdit |文件编辑|编辑和修改文件|
| __代码0__ | Grep、Glob、搜索 |代码搜索 |搜索文件或文件中的文本 |
| __代码0__ |自定义代理，任务 |代理调用|调用其他定制代理 |
| __代码0__ |网络搜索、网络获取 |网络访问|获取网页内容并搜索 |
| __代码0__ | TodoWrite |任务管理|创建和管理任务列表（仅限 VS Code）|

### 内置 MCP 服务器工具

**GitHub MCP 服务器**：
```yaml
tools: ['github/*']  # All GitHub tools
tools: ['github/get_file_contents', 'github/search_repositories']  # Specific tools
```
- 默认情况下所有只读工具均可用
- 令牌范围仅限于源存储库

**剧作家 MCP 服务器**：
```yaml
tools: ['playwright/*']  # All Playwright tools
tools: ['playwright/navigate', 'playwright/screenshot']  # Specific tools
```
- 配置为仅访问本地主机
- 对于浏览器自动化和测试很有用

### 工具选择最佳实践

- **最小权限原则**：仅启用代理目的所需的工具
- **安全**：除非明确要求，否则限制 `execute` 访问
- **重点**：更少的工具 = 更清晰的代理目的和更好的性能
- **文档**：评论为什么复杂配置需要特定工具

## 子代理调用（代理编排）

代理可以使用**代理调用工具**（`agent` 工具）调用其他代理来编排多步骤工作流。

推荐的方法是**基于提示的编排**：
- 编排器用自然语言定义了逐步的工作流程。
- 每个步骤都委托给专门的代理。
- 编排器仅传递基本上下文（例如，基本路径、标识符），并要求每个子代理读取其自己的工具/约束的 `.agent.md` 规范。

### 它是如何运作的

1) 通过在协调器的工具列表中包含 `agent` 来启用代理调用：

```yaml
tools: ['read', 'edit', 'search', 'agent']
```

2) 对于每个步骤，通过提供以下内容来调用子代理：
- **代理名称**（用户选择/调用的标识符）
- **代理规范路径**（要读取和遵循的 `.agent.md` 文件）
- **最小共享上下文**（例如，`basePath`、`projectName`、`logFile`）

### 提示模式（推荐）

对每个步骤使用一致的“包装提示”，以便子代理的行为可预测：

```text
This phase must be performed as the agent "<AGENT_NAME>" defined in "<AGENT_SPEC_PATH>".

IMPORTANT:
- Read and apply the entire .agent.md spec (tools, constraints, quality standards).
- Work on "<WORK_UNIT_NAME>" with base path: "<BASE_PATH>".
- Perform the necessary reads/writes under this base path.
- Return a clear summary (actions taken + files produced/modified + issues).
```

可选：如果您需要一个轻量级、结构化的包装器来实现可追溯性，请在提示中嵌入一个小的 JSON 块（仍然是人类可读且与工具无关）：

```text
{
  "step": "<STEP_ID>",
  "agent": "<AGENT_NAME>",
  "spec": "<AGENT_SPEC_PATH>",
  "basePath": "<BASE_PATH>"
}
```

### Orchestrator 结构（保持通用）

对于可维护的协调器，记录这些结构元素：

- **动态参数**：从用户处提取哪些值（例如，`projectName`、`fileName`、`basePath`）。
- **子代理注册表**：将每个步骤映射到 `agentName` + `agentSpecPath` 的列表/表格。
- **步骤排序**：显式顺序（步骤 1 → 步骤 N）。
- **触发条件**（可选但推荐）：定义何时运行或跳过步骤。
- **日志记录策略**（可选但推荐）：每个步骤后更新一个日志/报告文件。

避免在 Orchestrator 提示符中嵌入编排“代码”（JavaScript、Python 等）；更喜欢确定性的、工具驱动的协调。

### 基本模式

构造每个步骤调用：

1. **步骤描述**：明确的一行目的（用于日志和可追溯性）
2. **代理身份**：`agentName` + `agentSpecPath`
3. **上下文**：一组小的、明确的变量（路径、ID、环境名称）
4. **预期输出**：要创建/更新的文件以及应写入的位置
5. **返回摘要**：要求子代理返回简短的结构化摘要

### 示例：多步骤处理

```text
Step 1: Transform raw input data
Agent: data-processor
Spec: .github/agents/data-processor.agent.md
Context: projectName=${projectName}, basePath=${basePath}
Input: ${basePath}/raw/
Output: ${basePath}/processed/
Expected: write ${basePath}/processed/summary.md

Step 2: Analyze processed data (depends on Step 1 output)
Agent: data-analyst
Spec: .github/agents/data-analyst.agent.md
Context: projectName=${projectName}, basePath=${basePath}
Input: ${basePath}/processed/
Output: ${basePath}/analysis/
Expected: write ${basePath}/analysis/report.md
```

### 要点

- **在提示中传递变量**：对所有动态值使用 `${variableName}`
- **保持提示集中**：每个子代理的清晰、具体的任务
- **返回摘要**：每个子代理应报告其完成的工作
- **顺序执行**：当输出/输入之间存在依赖关系时按顺序运行步骤
- **错误处理**：在继续执行相关步骤之前检查结果

### ⚠️ 工具可用性要求

**关键**：如果子代理需要特定工具（例如，`edit`、`execute`、`search`），则编排器必须将这些工具包含在其自己的 `tools` 列表中。子代理无法访问其父协调器无法使用的工具。

**示例**：
```yaml
# If your sub-agents need to edit files, execute commands, or search code
tools: ['read', 'edit', 'search', 'execute', 'agent']
```

协调器的工具权限充当所有调用的子代理的上限。仔细规划您的工具列表，以确保所有子代理都拥有他们需要的工具。

### ⚠️重要限制

**子代理编排不适合大规模数据处理。** 在以下情况下避免使用多步骤子代理管道：
- 处理数百或数千个文件
- 处理大型数据集
- 在大型代码库上执行批量转换
- 编排超过 5-10 个连续步骤

每个子代理调用都会增加延迟和上下文开销。对于大容量处理，请直接在单个代理中实现逻辑。仅使用编排来协调集中、可管理的数据集上的专门任务。

## 代理提示结构

标题下方的降价内容定义了代理的行为、专业知识和说明。结构良好的提示通常包括：

1. **代理身份和角色**：代理是谁及其主要角色
2. **核心职责**：代理执行哪些具体任务
3. **方法和方法论**：代理如何完成任务
4. **指南和限制**：该做什么/避免什么以及质量标准
5. **输出期望**：期望的输出格式和质量

### 即时写作最佳实践

- **具体而直接**：使用祈使语气（“分析”、“生成”）；避免模糊的术语
- **定义边界**：明确说明范围限制和约束
- **包括上下文**：解释领域专业知识并参考相关框架
- **关注行为**：描述代理应该如何思考和工作
- **使用结构化格式**：标题、项目符号和列表使提示易于扫描

## 变量定义和提取

代理可以定义动态参数以从用户输入中提取值，并在代理的行为和子代理通信中使用它们。这使得灵活的、上下文感知的代理能够适应用户提供的数据。

### 何时使用变量

**在以下情况下使用变量**：
- 代理行为取决于用户输入
- 需要将动态值传递给子代理
- 希望使代理可以在不同的上下文中重用
- 需要参数化工作流程
- 需要跟踪或引用用户提供的上下文

**示例**：
- 从用户提示中提取项目名称
- 捕获管道处理的认证名称
- 识别文件路径或目录
- 提取配置选项
- 解析功能名称或模块标识符

### 变量声明模式

在代理提示符的早期定义变量部分以记录预期参数：

```markdown
# Agent Name

## Dynamic Parameters

- **Parameter Name**: Description and usage
- **Another Parameter**: How it's extracted and used

## Your Mission

Process [PARAMETER_NAME] to accomplish [task].
```

### 变量提取方法

#### 1. **显式用户输入**
如果提示中未检测到，请用户提供变量：

```markdown
## Your Mission

Process the project by analyzing your codebase.

### Step 1: Identify Project
If no project name is provided, **ASK THE USER** for:
- Project name or identifier
- Base path or directory location
- Configuration type (if applicable)

Use this information to contextualize all subsequent tasks.
```

#### 2. **从提示中隐式提取**
自动从用户的自然语言输入中提取变量：

```javascript
// Example: Extract certification name from user input
const userInput = "Process My Certification";

// Extract key information
const certificationName = extractCertificationName(userInput);
// Result: "My Certification"

const basePath = `certifications/${certificationName}`;
// Result: "certifications/My Certification"
```

#### 3. **上下文变量解析**
使用文件上下文或工作区信息来派生变量：

```markdown
## Variable Resolution Strategy

1. **From User Prompt**: First, look for explicit mentions in user input
2. **From File Context**: Check current file name or path
3. **From Workspace**: Use workspace folder or active project
4. **From Settings**: Reference configuration files
5. **Ask User**: If all else fails, request missing information
```

### 在代理提示中使用变量

#### 指令中的变量替换

在代理提示中使用模板变量使其动态化：

```markdown
# Agent Name

## Dynamic Parameters
- **Project Name**: ${projectName}
- **Base Path**: ${basePath}
- **Output Directory**: ${outputDir}

## Your Mission

Process the **${projectName}** project located at `${basePath}`.

## Process Steps

1. Read input from: `${basePath}/input/`
2. Process files according to project configuration
3. Write results to: `${outputDir}/`
4. Generate summary report

## Quality Standards

- Maintain project-specific coding standards for **${projectName}**
- Follow directory structure: `${basePath}/[structure]`
```

#### 将变量传递给子代理

调用子代理时，通过提示中的替换变量传递所有上下文。更喜欢传递**路径和标识符**，而不是整个文件内容。

示例（提示模板）：

```text
This phase must be performed as the agent "documentation-writer" defined in ".github/agents/documentation-writer.agent.md".

IMPORTANT:
- Read and apply the entire .agent.md spec.
- Project: "${projectName}"
- Base path: "projects/${projectName}"
- Input: "projects/${projectName}/src/"
- Output: "projects/${projectName}/docs/"

Task:
1. Read source files under the input path.
2. Generate documentation.
3. Write outputs under the output path.
4. Return a concise summary (files created/updated, key decisions, issues).
```

子代理接收提示中嵌入的所有必要上下文。变量在发送提示之前解析，因此子代理使用具体路径和值，而不是变量占位符。

### 真实示例：Code Review Orchestrator

通过多个专用代理验证代码的简单编排器示例：

1) 确定共享上下文：
- __代码0__，__代码1__
- `basePath`（例如，`projects/${repositoryName}/pr-${prNumber}`）

2) 按顺序调用专用代理（每个代理读取自己的 `.agent.md` 规范）：

```text
Step 1: Security Review
Agent: security-reviewer
Spec: .github/agents/security-reviewer.agent.md
Context: repositoryName=${repositoryName}, prNumber=${prNumber}, basePath=projects/${repositoryName}/pr-${prNumber}
Output: projects/${repositoryName}/pr-${prNumber}/security-review.md

Step 2: Test Coverage
Agent: test-coverage
Spec: .github/agents/test-coverage.agent.md
Context: repositoryName=${repositoryName}, prNumber=${prNumber}, basePath=projects/${repositoryName}/pr-${prNumber}
Output: projects/${repositoryName}/pr-${prNumber}/coverage-report.md

Step 3: Aggregate
Agent: review-aggregator
Spec: .github/agents/review-aggregator.agent.md
Context: repositoryName=${repositoryName}, prNumber=${prNumber}, basePath=projects/${repositoryName}/pr-${prNumber}
Output: projects/${repositoryName}/pr-${prNumber}/final-review.md
```

#### 示例：条件步骤编排（代码审查）

此示例显示了更完整的编排，其中包括**飞行前检查**、**条件步骤**以及**必需与可选**行为。

**动态参数（输入）：**
- __代码0__，__代码1__
- `basePath`（例如，`projects/${repositoryName}/pr-${prNumber}`）
- `logFile`（例如，`${basePath}/.review-log.md`）

**飞行前检查（推荐）：**
- 验证预期的文件夹/文件是否存在（例如 `${basePath}/changes/`、`${basePath}/reports/`）。
- 检测影响步骤触发器的高级特征（例如，存储库语言、是否存在 `package.json`、`pom.xml`、`requirements.txt`、测试文件夹）。
- 在开始时记录一次结果。

**步进触发条件：**

|步骤|状态 |触发条件|关于失败|
|------|--------|-------------------|-----------|
| 1：安全审查| **必填** |永远奔跑|停止管道 |
| 2：依赖性审计|可选|如果存在依赖项清单（`package.json`、`pom.xml` 等）|继续 |
| 3：测试覆盖率检查|可选|是否存在测试项目/文件 |继续 |
| 4：性能检查|可选|如果性能敏感代码发生更改或存在性能配置 |继续 |
| 5：汇总与判决| **必填** |如果步骤 1 完成，则始终运行 |停止管道|

**执行流程（自然语言）：**
1. 初始化 `basePath` 并创建/更新 `logFile`。
2. 进行飞行前检查并记录下来。
3. 依次执行步骤 1 → N。
4. 对于每个步骤：
  - 如果触发条件为 false：标记为 **SKIPPED** 并继续。
  - 否则：使用包装器提示调用子代理并捕获其摘要。
  - 标记为 **成功** 或 **失败**。
  - 如果该步骤是**必需**并且失败：停止管道并写入失败摘要。
5. 以最终摘要部分结束（总体状态、工件、下一步操作）。

**子代理调用提示（示例）：**

```text
This phase must be performed as the agent "security-reviewer" defined in ".github/agents/security-reviewer.agent.md".

IMPORTANT:
- Read and apply the entire .agent.md spec.
- Work on repository "${repositoryName}" PR "${prNumber}".
- Base path: "${basePath}".

Task:
1. Review the changes under "${basePath}/changes/".
2. Write findings to "${basePath}/reports/security-review.md".
3. Return a short summary with: critical findings, recommended fixes, files created/modified.
```

**记录格式（示例）：**

```markdown
## Step 2: Dependency Audit
**Status:** ✅ SUCCESS / ⚠️ SKIPPED / ❌ FAILED
**Trigger:** package.json present
**Started:** 2026-01-16T10:30:15Z
**Completed:** 2026-01-16T10:31:05Z
**Duration:** 00:00:50
**Artifacts:** reports/dependency-audit.md
**Summary:** [brief agent summary]
```

此模式适用于任何编排场景：提取变量、调用具有清晰上下文的子代理、等待结果。


### 可变最佳实践

#### 1. **清晰的文档**
始终记录预期的变量：

```markdown
## Required Variables
- **projectName**: The name of the project (string, required)
- **basePath**: Root directory for project files (path, required)

## Optional Variables
- **mode**: Processing mode - quick/standard/detailed (enum, default: standard)
- **outputFormat**: Output format - markdown/json/html (enum, default: markdown)

## Derived Variables
- **outputDir**: Automatically set to ${basePath}/output
- **logFile**: Automatically set to ${basePath}/.log.md
```

#### 2. **一致的命名**
使用一致的变量命名约定：

```javascript
// Good: Clear, descriptive naming
const variables = {
  projectName,          // What project to work on
  basePath,            // Where project files are located
  outputDirectory,     // Where to save results
  processingMode,      // How to process (detail level)
  configurationPath    // Where config files are
};

// Avoid: Ambiguous or inconsistent
const bad_variables = {
  name,     // Too generic
  path,     // Unclear which path
  mode,     // Too short
  config    // Too vague
};
```

#### 3. **验证和约束**
记录有效值和约束：

```markdown
## Variable Constraints

**projectName**:
- Type: string (alphanumeric, hyphens, underscores allowed)
- Length: 1-100 characters
- Required: yes
- Pattern: `/^[a-zA-Z0-9_-]+$/`

**processingMode**:
- Type: enum
- Valid values: "quick" (< 5min), "standard" (5-15min), "detailed" (15+ min)
- Default: "standard"
- Required: no
```

## MCP 服务器配置（仅限组织/企业）

MCP 服务器通过附加工具扩展代理功能。仅支持组织和企业级代理。

### 配置格式

```yaml
---
name: my-custom-agent
description: 'Agent with MCP integration'
tools: ['read', 'edit', 'custom-mcp/tool-1']
mcp-servers:
  custom-mcp:
    type: 'local'
    command: 'some-command'
    args: ['--arg1', '--arg2']
    tools: ["*"]
    env:
      ENV_VAR_NAME: ${{ secrets.API_KEY }}
---
```

### MCP 服务器属性

- **类型**：服务器类型（`'local'` 或 `'stdio'`）
- **命令**：启动MCP服务器的命令
- **args**：命令参数数组
- **工具**：从此服务器启用的工具（全部为 `["*"]`）
- **env**：环境变量（支持secret）

### 环境变量和秘密

必须在“copilot”环境下的存储库设置中配置机密。

**支持的语法**：
```yaml
env:
  # Environment variable only
  VAR_NAME: COPILOT_MCP_ENV_VAR_VALUE

  # Variable with header
  VAR_NAME: $COPILOT_MCP_ENV_VAR_VALUE
  VAR_NAME: ${COPILOT_MCP_ENV_VAR_VALUE}

  # GitHub Actions-style (YAML only)
  VAR_NAME: ${{ secrets.COPILOT_MCP_ENV_VAR_VALUE }}
  VAR_NAME: ${{ var.COPILOT_MCP_ENV_VAR_VALUE }}
```

## 文件组织和命名

### 存储库级代理
- 位置：`.github/agents/`
- 范围：仅在特定存储库中可用
- 访问：使用存储库配置的 MCP 服务器

### 组织/企业级代理
- 位置： `.github-private/agents/` （然后移动到 `agents/` 根目录）
- 范围：适用于组织/企业中的所有存储库
- 访问：可以配置专用MCP服务器

### 命名约定
- 使用带连字符的小写字母：`test-specialist.agent.md`
- 名称应反映代理目的
- 文件名成为默认代理名称（如果未指定 `name`）
- 允许的字符：`.`、`-`、`_`、`a-z`、`A-Z`、`0-9`

## 代理处理和行为

### 版本控制
- 基于代理文件的 Git 提交 SHA
- 为不同的代理版本创建分支/标签
- 使用存储库/分支的最新版本进行实例化
- PR 交互使用相同的代理版本以保持一致性

### 名称冲突
优先级（从最高到最低）：
1. 存储库级代理
2. 组织级代理
3. 企业级代理

较低级别的配置会覆盖具有相同名称的较高级别的配置。

### 刀具加工
- `tools` 列出过滤器可用工具（内置和 MCP）
- 未指定工具 = 启用所有工具
- 空列表 (`[]`) = 禁用所有工具
- 具体列表 = 仅启用那些工具
- 无法识别的工具名称将被忽略（允许特定于环境的工具）

### MCP服务器处理订单
1. 开箱即用的 MCP 服务器（例如 GitHub MCP）
2. 自定义代理 MCP 配置（仅限组织/企业）
3. 存储库级 MCP 配置

每个级别都可以覆盖之前级别的设置。

## 代理创建清单

### 前题
- [ ] `description` 字段存在且具有描述性（50-150 个字符）
- [ ] `description` 用单引号括起来
- [ ] `name` 指定（可选但推荐）
- [ ] `tools` 适当配置（或故意省略）
- [ ] `model` 指定以获得最佳性能
- [ ] `target` 如果环境特定则设置
- [ ] 如果需要手动选择，则 `infer` 设置为 `false`

### 提示内容
- [ ] 明确的代理身份和角色定义
- [ ] 明确列出核心职责
- [ ] 方法和方法论解释
- [ ] 规定的准则和限制
- [ ] 记录输出预期
- [ ] 提供有帮助的示例
- [ ] 说明具体且可操作
- [ ] 范围和边界明确界定
- [ ] 总内容不超过30,000字符

### 文件结构
- [ ] 文件名遵循小写加连字符约定
- [ ] 文件放置在正确的目录中（`.github/agents/` 或 `agents/`）
- [ ] 文件名仅使用允许的字符
- [ ] 文件扩展名是 `.agent.md`

### 品质保证
- [ ] 代理目的唯一且不重复
- [ ] 工具是最少且必要的
- [ ] 说明清晰明确
- [ ] 代理已通过代表性任务进行测试
- [ ] 文档参考是最新的
- [ ] 解决安全考虑（如果适用）

## 常见代理模式

### 测试专家
**目的**：专注于测试覆盖率和质量
**工具**：所有工具（用于全面的测试创建）
**方法**：分析、识别差距、编写测试、避免生产代码更改

### 实施计划员
**目的**：制定详细的技术计划和规格
**工具**：仅限于 `['read', 'search', 'edit']`
**方法**：分析需求、创建文档、避免实施

### 代码审查员
**目的**：审查代码质量并提供反馈
**工具**：仅限 `['read', 'search']`
**方法**：分析，提出改进建议，不直接修改

### 重构专家
**目的**：改善代码结构和可维护性
**工具**：`['read', 'search', 'edit']`
**方法**：分析模式、提出重构建议、安全实施

### 安全审核员
**目的**：识别安全问题和漏洞
**工具**：`['read', 'search', 'web']`
**方法**：扫描代码，对照 OWASP 检查，报告结果

## 要避免的常见错误

### 标题错误
- ❌ 缺少 `description` 字段
- ❌ 描述未用引号引起来
- ❌ 未检查文档的无效工具名称
- ❌ 不正确的 YAML 语法（缩进、引号）

### 工具配置问题
- ❌ 授予过多不必要的工具访问权限
- ❌ 缺少代理所需的工具
- ❌ 没有一致地使用工具别名
- ❌ 忘记 MCP 服务器命名空间 (`server-name/tool`)

### 提示内容问题
- ❌ 模糊、不明确的指示
- ❌ 冲突或矛盾的指导方针
- ❌ 缺乏明确的范围定义
- ❌ 产出低于预期
- ❌ 过于冗长的说明（超出字符限制）
- ❌ 没有复杂任务的示例或上下文

### 组织问题
- ❌ 文件名不反映代理目的
- ❌ 错误的目录（混淆存储库与组织级别）
- ❌ 在文件名中使用空格或特殊字符
- ❌ 重复的代理名称导致冲突

## 测试和验证

### 手动测试
1. 使用正确的 frontmatter 创建代理文件
2. 重新加载 VS Code 或刷新 GitHub.com
3. 从 Copilot Chat 的下拉列表中选择客服人员
4. 使用代表性用户查询进行测试
5. 验证工具访问是否按预期工作
6. 确认输出符合预期

### 集成测试
- 在范围内使用不同文件类型测试代理
- 验证 MCP 服务器连接（如果已配置）
- 检查缺少上下文的代理行为
- 测试错误处理和边缘情况
- 验证代理切换和移交

### 质量检查
- 运行代理创建清单
- 针对常见错误列表进行回顾
- 与存储库中的示例代理进行比较
- 获得复杂代理的同行评审
- 记录任何特殊配置需求

## 其他资源

### 官方文档
- [创建自定义代理](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents)
- [自定义代理配置](https://docs.github.com/en/copilot/reference/custom-agents-configuration)
- [VS Code 中的自定义代理](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
- [MCP 集成](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/extend-coding-agent-with-mcp)

### 社区资源
- [超棒副驾驶特工合集](https://github.com/github/awesome-copilot/tree/main/agents)
- [自定义库示例](https://docs.github.com/en/copilot/tutorials/customization-library/custom-agents)
- [您的第一个自定义代理教程](https://docs.github.com/en/copilot/tutorials/customization-library/custom-agents/your-first-custom-agent)

### 相关文件
- [提示文件指南](./prompt.instructions-zh.md) - 用于创建提示文件
- [指令指南](./instructions.instructions-zh.md) - 用于创建指令文件

## 版本兼容性说明

### GitHub.com（编码代理）
- ✅ 完全支持所有标准 frontmatter 属性
- ✅ 存储库和组织/企业级代理
- ✅ MCP 服务器配置（组织/企业）
- ❌ 不支持 `model`、`argument-hint`、`handoffs` 属性

### VS Code / JetBrains / Eclipse / Xcode
- ✅ 支持 `model` 属性用于 AI 模型选择
- ✅ 支持 `argument-hint` 和 `handoffs` 属性
- ✅ 用户个人资料和工作区级代理
- ❌ 无法在存储库级别配置 MCP 服务器
- ⚠️ 某些属性的行为可能有所不同

为多个环境创建代理时，请重点关注公共属性并在所有目标环境中进行测试。必要时使用 `target` 属性创建特定于环境的代理。
