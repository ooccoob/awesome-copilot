---
mode: 'agent'
tools: ['githubRepo', 'github', 'get_issue', 'get_issue_comments', 'get_me', 'list_issues']
description: '列出当前仓库中我的问题'
---

搜索当前仓库（使用#githubRepo获取仓库信息）并列出分配给我的任何问题（使用#list_issues）。

根据它们的年龄、评论数量和状态（开放/已关闭）建议我可能想要关注的问题。