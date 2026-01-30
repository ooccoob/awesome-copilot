---
mode: 'agent'
tools: ['githubRepo', 'github', 'get_me', 'get_pull_request', 'get_pull_request_comments', 'get_pull_request_diff', 'get_pull_request_files', 'get_pull_request_reviews', 'get_pull_request_status', 'list_pull_requests', 'request_copilot_review']
description: '列出当前仓库中我的拉取请求'
---

搜索当前仓库（使用#githubRepo获取仓库信息）并列出分配给我的任何拉取请求（使用#list_pull_requests）。

描述每个拉取请求的目的和详细信息。

如果PR正在等待某人审查，在响应中突出显示这一点。

如果PR上有任何检查失败，描述它们并建议可能的修复方案。

如果没有Copilot完成的审查，提议使用#request_copilot_review请求一个。