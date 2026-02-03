---
agent: 'agent'
tools: ['githubRepo', 'github', 'get_issue', 'get_issue_comments', 'get_me', 'list_issues']
description: 'List my issues in the current repository'
---

搜索当前存储库（使用 #githubRepo 获取存储库信息）并列出您发现的分配给我的所有问题（使用 #list_issues）。

根据问题的年龄、评论量和状态（开放/关闭）建议我可能想要关注的问题。
