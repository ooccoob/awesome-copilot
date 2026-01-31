---
代理人：“代理人”
工具：['githubRepo'，'github'，'get_me'，'get_pull_request'，'get_pull_request_comments'，'get_pull_request_diff'，'get_pull_request_files'，'get_pull_request_reviews'，'get_pull_request_status'，'list_pull_requests'， 'request_copilot_review']
描述：“列出当前存储库中我的拉取请求”
---

搜索当前存储库（使用 #githubRepo 获取存储库信息）并列出您找到的分配给我的所有拉取请求（使用 #list_pull_requests）。

描述每个拉取请求的目的和详细信息。

如果 PR 正在等待某人审核，请在回复中突出显示。

如果 PR 存在任何检查失败，请描述它们并提出可能的修复建议。

如果 Copilot 没有进行审核，请使用 #request_copilot_review 提出请求。
