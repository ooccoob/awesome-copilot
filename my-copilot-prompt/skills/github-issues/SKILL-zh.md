---
名称：github问题
描述：'使用 MCP 工具创建、更新和管理 GitHub 问题。当用户想要创建错误报告、功能请求或任务问题、更新现有问题、添加标签/受让人/里程碑或管理问题工作流程时，请使用此技能。触发“创建问题”、“提交错误”、“请求功能”、“更新问题 X”或任何 GitHub 问题管理任务等请求。
---

# GitHub 问题

使用 `@modelcontextprotocol/server-github` MCP 服务器管理 GitHub 问题。

## 可用的 MCP 工具

|工具|目的|
|------|---------|
| __代码0__ |创建新问题 |
| __代码0__ |更新现有问题 |
| __代码0__ |获取问题详细信息 |
| __代码0__ |搜索问题 |
| __代码0__ |添加评论 |
| __代码0__ |列出存储库问题 |

## 工作流程

1. **确定操作**：创建、更新或查询？
2. **收集上下文**：获取存储库信息、现有标签、里程碑（如果需要）
3. **结构内容**：使用[references/templates.md](references/templates-zh.md)中的适当模板
4. **执行**：调用适当的MCP工具
5. **确认**：向用户报告问题 URL

## 制造问题

### 所需参数

```
owner: repository owner (org or user)
repo: repository name  
title: clear, actionable title
body: structured markdown content
```

### 可选参数

```
labels: ["bug", "enhancement", "documentation", ...]
assignees: ["username1", "username2"]
milestone: milestone number (integer)
```

### 标题指南

- 有用时以类型前缀开头：`[Bug]`、`[Feature]`、`[Docs]`
- 具体且可操作
- 保持在 72 个字符以下
- 示例：
  - __代码0__
  - __代码0__
  - __代码0__

### 车身结构

始终使用 [references/templates.md](references/templates-zh.md) 中的模板。根据问题类型选择：

|用户请求 |模板|
|--------------|----------|
| Bug、错误、损坏、无法工作 |错误报告 |
|功能、增强、添加、新增 |功能请求 |
|任务、琐事、重构、更新 |任务|

## 更新问题

使用 `mcp__github__update_issue` ：

```
owner, repo, issue_number (required)
title, body, state, labels, assignees, milestone (optional - only changed fields)
```

状态值：`open`、`closed`

## 示例

### 示例 1：错误报告

**用户**：“创建错误问题 - 使用 SSO 时登录页面崩溃”

**操作**：通过以下方式调用 `mcp__github__create_issue`：
```json
{
  "owner": "github",
  "repo": "awesome-copilot",
  "title": "[Bug] Login page crashes when using SSO",
  "body": "## Description\nThe login page crashes when users attempt to authenticate using SSO.\n\n## Steps to Reproduce\n1. Navigate to login page\n2. Click 'Sign in with SSO'\n3. Page crashes\n\n## Expected Behavior\nSSO authentication should complete and redirect to dashboard.\n\n## Actual Behavior\nPage becomes unresponsive and displays error.\n\n## Environment\n- Browser: [To be filled]\n- OS: [To be filled]\n\n## Additional Context\nReported by user.",
  "labels": ["bug"]
}
```

### 示例 2：功能请求

**用户**：“创建高优先级的深色模式功能请求”

**操作**：通过以下方式调用 `mcp__github__create_issue`：
```json
{
  "owner": "github",
  "repo": "awesome-copilot",
  "title": "[Feature] Add dark mode support",
  "body": "## Summary\nAdd dark mode theme option for improved user experience and accessibility.\n\n## Motivation\n- Reduces eye strain in low-light environments\n- Increasingly expected by users\n- Improves accessibility\n\n## Proposed Solution\nImplement theme toggle with system preference detection.\n\n## Acceptance Criteria\n- [ ] Toggle switch in settings\n- [ ] Persists user preference\n- [ ] Respects system preference by default\n- [ ] All UI components support both themes\n\n## Alternatives Considered\nNone specified.\n\n## Additional Context\nHigh priority request.",
  "labels": ["enhancement", "high-priority"]
}
```

## 常用标签

适用时使用这些标准标签：

|标签|用于 |
|-------|---------|
| __代码0__ |有什么东西不工作 |
| __代码0__ |新功能或改进 |
| __代码0__ |文档更新 |
| __代码0__ |适合新人|
| __代码0__ |需要额外注意|
| __代码0__ |需要更多信息 |
| __代码0__ |不会被解决 |
| __代码0__ |已经存在 |
| __代码0__ |紧急问题|

## 温馨提示

- 在创建问题之前始终确认存储库上下文
- 询问遗漏的关键信息而不是猜测
- 已知时链接相关问题：`Related to #123`
- 对于更新，首先获取当前问题以保留未更改的字段
