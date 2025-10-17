## What
- 获取当前仓库中分配给我的 Issues 列表，并基于时长、评论数、状态给出优先建议。

## When to use
- 需要快速聚焦我名下的工作项与下一步行动。

## Why it matters
- 减少切换成本，避免遗忘长时间未更新的问题，提升响应效率。

## How (关键流程)
- 获取仓库信息 → 列出 assigned 给我的 issues → 统计年龄/评论数/状态
- 优先级建议：长期未更新 + 评论多 + 仍 open → 优先
- 输出结构化清单与建议下一步

## Example questions (≥10)
1. 列出我在当前仓库的所有 open issues，并按最后更新时间排序。
2. 标记评论超过 10 条且超过 14 天未更新的问题，建议处理顺序。
3. 将无复现步骤的 bug 打上 needs-repro 标签并创建模板评论。
4. 展示已关闭但近 7 天内关闭的 issue，检查是否需要回归测试。
5. 给每个 issue 生成“本周可执行”的下一步任务建议。
6. 统计按标签（bug/feature/docs）的分布与平均存续天数。
7. 找出由我创建但分配给他人的 issues，并建议是否需要跟进评论。
8. 识别“阻塞中”的 issues 并生成提请协助的评论草稿。
9. 生成适合周会的 issue 摘要（top 5）。
10. 输出一个 Markdown 表格，便于贴到项目周报。

## Key points
- CN: 指派过滤、优先排序、结构化输出、可执行建议
- EN: Assignment filter, priority ranking, structured output, actionable suggestions

## Mind map (简要)
- 拉取 → 过滤 → 统计 → 排序 → 建议 → 输出

---
Source file: d:\mycode\awesome-copilot\prompts\my-issues.prompt.md
Generated: 2025-10-17T00:00:00Z
