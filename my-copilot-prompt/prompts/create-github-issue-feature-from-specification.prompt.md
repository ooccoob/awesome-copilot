---
agent: 'agent'
description: 'Create GitHub Issue for feature request from specification file using feature_request.yml template.'
tools: ['search/codebase', 'search', 'github', 'create_issue', 'search_issues', 'update_issue']
---
# 根据规范创建 GitHub 问题

在 `${file}` 处为规范创建 GitHub 问题。

## 工艺流程

1. 分析规格文件以提取需求
2. 使用 `search_issues` 检查现有问题
3. 使用 `create_issue` 创建新问题或使用 `update_issue` 更新现有问题
4. 使用 `feature_request.yml` 模板（回退到默认值）

## 要求

- 完整规范的单一问题
- 明确的标题标识规范
- 仅包括规范所需的更改
- 创建前验证现有问题

## 发行内容

- 标题：规范中的功能名称
- 描述：问题陈述、建议的解决方案和背景
- 标签：功能、增强（视情况而定）
