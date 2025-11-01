---
mode: 'agent'
description: '使用pull_request_template.md模板从规范文件为功能请求创建GitHub Pull Request。'
tools: ['codebase', 'search', 'github', 'create_pull_request', 'update_pull_request', 'get_pull_request_diff']
---

# 从规范创建GitHub Pull Request

为`${workspaceFolder}/.github/pull_request_template.md`处的规范创建GitHub Pull Request。

## 流程

1. 使用'search'工具分析从`${workspaceFolder}/.github/pull_request_template.md`的规范文件模板以提取需求。
2. 使用'create_pull_request'工具在`${input:targetBranch}`上创建pull request草稿模板。确保当前分支没有任何现有的pull request。如果有，继续步骤4并跳过步骤3。
3. 使用'get_pull_request_diff'工具获取pull request中的更改以分析pull request中更改的信息。
4. 使用'update_pull_request'工具更新上一步中创建的pull request主体和标题。整合第一步获得的模板信息，根据需要更新主体和标题。
5. 使用'update_pull_request'工具从草稿转换为准备审查。要更新pull request状态。
6. 使用'get_me'获取创建pull request的人员用户名并分配给'update_issue'工具。要分配pull request
7. 向用户响应创建的pull request URL。

## 要求
- 为完整规范创建单个pull request
- 识别规范的清晰标题/pull_request_template.md
- 在pull_request_template.md中填写足够的信息
- 创建前验证现有pull request