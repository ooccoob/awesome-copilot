---
agent: 'agent'
description: 'Create GitHub Issues from implementation plan phases using feature_request.yml or chore_request.yml templates.'
tools: ['search/codebase', 'search', 'github', 'create_issue', 'search_issues', 'update_issue']
---
# 根据实施计划创建 GitHub 问题

在 `${file}` 处为实施计划创建 GitHub 问题。

## 工艺流程

1. 分析计划文件以确定阶段
2. 使用 `search_issues` 检查现有问题
3. 使用 `create_issue` 在每个阶段创建新问题或使用 `update_issue` 更新现有问题
4. 使用 `feature_request.yml` 或 `chore_request.yml` 模板（回退到默认值）

## 要求

- 每个实施阶段一个问题
- 清晰、结构化的标题和描述
- 仅包括计划所需的更改
- 创建前验证现有问题

## 发行内容

- 标题：实施计划中的阶段名称
- 描述：阶段详细信息、要求和背景
- 标签：适合问题类型（功能/琐事）
