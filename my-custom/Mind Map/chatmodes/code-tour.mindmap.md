## What / When / Why / How

- What: VSCode CodeTour 专家（.tour JSON 编写/维护）
- When: 需要为大型代码库创建引导式上手与深度导览
- Why: 降低认知负荷与上手时间，形成可维护的故事化导览
- How: 依据官方 schema 组织 steps（内容/目录/选择/命令），验证与版本策略

## Key Points

- 位置：.tours/.vscode/tours/.github/tours
- 步骤类型：content/directory/selection/command/view/uri
- 组织：循序渐进、分组清晰、交互性强、主导览与链接
- 版本：无/分支/提交/标签；防漂移
- CI：校验与 PR 漂移检查

## Compact Map

- 目标与学习路径
- 结构与文件对齐
- 步骤设计与交互元素
- 版本/漂移/维护
- 团队采纳（README/CONTRIBUTING 链接）

## Example Questions (10+)

- 本仓库的主导览目标和学习成果是什么？
- 哪些文件/目录/行需要被强调，顺序为何？
- 哪类交互（命令/代码片段/终端）能提升学习效果？
- 版本策略采用何种（分支/提交/标签）？
- 如何在 CI 中检测 tour 漂移？
- 步骤标题与描述如何做到简洁且上下文足够？
- 复杂项目是否拆分为多条互链的 tours？
- 新人 30 分钟能学到什么？
- 需要哪些图片/图表辅助理解？
- 如何组织目录与命名以便维护？
- 如何编写可复用的教程型 steps？

---
Source: d:\mycode\awesome-copilot\chatmodes\code-tour.chatmode.md
Generated: {{timestamp}}
