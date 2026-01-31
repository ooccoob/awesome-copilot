---
代理人：“代理人”
描述：“使用 pull_request_template.md 模板从规范文件创建 GitHub Pull 请求以获取功能请求。”
工具：['搜索/代码库'、'搜索'、'github'、'create_pull_request'、'update_pull_request'、'get_pull_request_diff']
---
# 根据规范创建 GitHub Pull 请求

在 `${workspaceFolder}/.github/pull_request_template.md` 处为规范创建 GitHub Pull 请求。

## 工艺流程

1. 分析“${workspaceFolder}/.github/pull_request_template.md”中的规范文件模板，通过“搜索”工具提取需求。
2. 使用“create_pull_request”工具在 `${input:targetBranch}` 上创建拉取请求草稿模板。并确保当前分支不存在任何拉取请求 `get_pull_request`。如果已继续执行步骤 4，并跳过步骤 3。
3. 通过使用“get_pull_request_diff”工具分析拉取请求中更改的信息来获取拉取请求中的更改。
4. 使用“update_pull_request”工具更新上一步中创建的拉取请求正文和标题。合并第一步中获得的模板中的信息，根据需要更新正文和标题。
5. 使用“update_pull_request”工具从草稿切换到准备审核状态。更新拉取请求的状态。
6. 使用“get_me”获取人员的用户名已创建拉取请求并分配给 `update_issue` 工具。分配拉取请求
7. 已向用户创建响应 URL 拉取请求。

## 要求
- 完整规范的单个拉取请求
- 清晰的 title/pull_request_template.md 标识规范
- 在 pull_request_template.md 中填写足够的信息
- 在创建之前验证现有拉取请求
