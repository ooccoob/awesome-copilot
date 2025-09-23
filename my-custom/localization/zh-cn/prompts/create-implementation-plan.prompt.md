---
mode: "agent"
description: "为新增功能、重构现有代码或升级依赖、设计、架构或基础设施创建一份新的实施计划文件。"
tools: ["changes", "codebase", "editFiles", "extensions", "fetch", "githubRepo", "openSimpleBrowser", "problems", "runTasks", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI"]
---

# 创建实施计划（Implementation Plan）

## 首要指令

你的目标是为 `${input:PlanPurpose}` 创建一份新的实施计划文件。输出必须可被机器读取、确定性且结构化，便于其他 AI 系统或人类执行。

## 执行上下文

该提示面向 AI-到-AI 的通信与自动处理。所有指令都应被字面理解并系统化执行，无需人工解读或澄清。

## 核心要求

- 生成可由 AI 代理或人类完全执行的实施计划
- 采用零歧义、确定性的语言
- 以可自动解析与执行的结构组织内容
- 确保内容自包含，无需外部上下文即可理解

## 计划结构要求

计划需由离散、原子化的阶段构成，每个阶段包含可执行任务。除非显式声明依赖，否则任务默认可并行执行。

## 阶段架构

- 每个阶段必须具有可度量的完成标准
- 阶段内任务可并行执行，除非声明依赖
- 所有任务描述必须包含具体文件路径、函数名与精确实现细节
- 不应存在需要人工判断的开放性任务

## 面向 AI 的实现标准

- 使用明确、无歧义的语言
- 以可机器解析的格式组织（表格、列表、结构化数据）
- 在适用处提供具体文件路径、行号与精确代码引用
- 明确定义所有变量、常量与配置值
- 在每个任务描述中包含完整上下文
- 标识符统一使用前缀（REQ-、TASK- 等）
- 提供可自动验证的校验标准

## 输出文件规范

- 将实施计划文件保存到 `/plan/` 目录
- 命名规范：`[purpose]-[component]-[version].md`
- purpose 前缀：`upgrade|refactor|feature|data|infrastructure|process|architecture|design`
- 示例：`upgrade-system-command-4.md`、`feature-auth-module-1.md`
- 文件必须为有效 Markdown，包含正确的 front matter

## 强制模板结构

所有实施计划必须严格遵循以下模板，各节均为必填，且需提供可执行内容。AI 代理在执行前必须校验模板合规性。

## 模板校验规则

- front matter 字段齐全且格式正确
- 所有标题与示例完全匹配（区分大小写）
- 所有标识符前缀符合规范
- 表格包含所需列
- 不得保留占位文本

## 状态

实施计划的状态必须在 front matter 中明确定义，且反映当前状态，可选值（括号内为徽章颜色）：`Completed`（亮绿色）、`In progress`（黄色）、`Planned`（蓝色）、`Deprecated`（红色）、`On Hold`（橙色）。并在引言以徽章展示。

```md
---
goal: [Concise Title Describing the Package Implementation Plan's Goal]
version: [Optional: e.g., 1.0, Date]
date_created: [YYYY-MM-DD]
last_updated: [Optional: YYYY-MM-DD]
owner: [Optional: Team/Individual responsible for this spec]
status: 'Completed'|'In progress'|'Planned'|'Deprecated'|'On Hold'
tags: [Optional: List of relevant tags or categories, e.g., `feature`, `upgrade`, `chore`, `architecture`, `migration`, `bug` etc]
---

# Introduction

![Status: <status>](https://img.shields.io/badge/status-<status>-<status_color>)

[A short concise introduction to the plan and the goal it is intended to achieve.]

## 1. Requirements & Constraints

[Explicitly list all requirements & constraints that affect the plan and constrain how it is implemented. Use bullet points or tables for clarity.]

- **REQ-001**: Requirement 1
- **SEC-001**: Security Requirement 1
- **[3 LETTERS]-001**: Other Requirement 1
- **CON-001**: Constraint 1
- **GUD-001**: Guideline 1
- **PAT-001**: Pattern to follow 1

## 2. Implementation Steps

### Implementation Phase 1

- GOAL-001: [Describe the goal of this phase, e.g., "Implement feature X", "Refactor module Y", etc.]

| Task     | Description           | Completed | Date       |
| -------- | --------------------- | --------- | ---------- |
| TASK-001 | Description of task 1 | ✅        | 2025-04-25 |
| TASK-002 | Description of task 2 |           |            |
| TASK-003 | Description of task 3 |           |            |

### Implementation Phase 2

- GOAL-002: [Describe the goal of this phase, e.g., "Implement feature X", "Refactor module Y", etc.]

| Task     | Description           | Completed | Date |
| -------- | --------------------- | --------- | ---- |
| TASK-004 | Description of task 4 |           |      |
| TASK-005 | Description of task 5 |           |      |
| TASK-006 | Description of task 6 |           |      |

## 3. Alternatives

[A bullet point list of any alternative approaches that were considered and why they were not chosen. This helps to provide context and rationale for the chosen approach.]

- **ALT-001**: Alternative approach 1
- **ALT-002**: Alternative approach 2

## 4. Dependencies

[List any dependencies that need to be addressed, such as libraries, frameworks, or other components that the plan relies on.]

- **DEP-001**: Dependency 1
- **DEP-002**: Dependency 2

## 5. Files

[List the files that will be affected by the feature or refactoring task.]

- **FILE-001**: Description of file 1
- **FILE-002**: Description of file 2

## 6. Testing

[List the tests that need to be implemented to verify the feature or refactoring task.]

- **TEST-001**: Description of test 1
- **TEST-002**: Description of test 2

## 7. Risks & Assumptions

[List any risks or assumptions related to the implementation of the plan.]

- **RISK-001**: Risk 1
- **ASSUMPTION-001**: Assumption 1

## 8. Related Specifications / Further Reading

[Link to related spec 1]
[Link to relevant external documentation]
```
