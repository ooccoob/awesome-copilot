## What/When/Why/How
- What: Joyride 工作区自动化助手（.joyride/ 下的团队共享 VS Code 自动化）。
- When: 需要项目内共享激活脚本、任务面板、工作流定制与上下文感知的自动配置时。
- Why: 让团队获取一致、可版本化的自动化与开发体验；降低上手成本。
- How: 在 .joyride/ 中放置 workspace_activate.cljs 等；REPL 小步验证后再落盘。

## Key Points
- 背景：工作区范围、版本控制、上下文感知。
- 哲学：数据导向、逐步演进、以 REPL 为先；仅在请求时修改文件。
- 命名空间：使用 (in-ns ...) 正确加载；joyride.core/load-file。
- 上下文键：:project/type, :build/config, :team/conventions 等“合成命名空间”。
- 交互：vscode API + Joyride evaluation；输入/选择需 awaitResult: true。
- 激活：workspace_activate.cljs 自动初始化工作区。
- 资源：以 Flare 呈现可视化辅助界面；关闭/列表/广播。
- 可维护性：扁平化数据建模；函数参数使用 map 便于扩展。

## Compact Map
Workspace
- .joyride/ 结构
- activate 脚本
- VS Code API
- awaitResult/Promise
- Data/Keywords
- Flare 视图

## Checklist
- [ ] 只在 REPL 验证后再修改文件
- [ ] 关键操作 awaitResult: true
- [ ] 统一的工作区元数据结构
- [ ] 激活脚本幂等可重入
- [ ] Disposables 注册与清理

## Example Questions (≥10)
- 如何设计 workspace_activate.cljs 实现自动任务注册与面板启动？
- 在多根工作区如何遍历各根目录并构建索引？
- 如何把团队脚本放入版本库并区分用户私有设置？
- 如何通过 Flare 提供交互式仪表盘？
- 如何检查某扩展是否已激活并调用其 API？
- awaitResult 应用于哪些 VS Code API 场景？
- 如何组织 :workspace/* 与 :project/* 关键字以便扩展？
- 发生错误时如何在不污染状态下回滚 Disposables？
- 如何在 REPL 中逐步拼装功能后再写入 .joyride/ 文件？
- 如何调试与排查命名空间加载问题？

Source: d:\mycode\awesome-copilot\instructions\joyride-workspace-automation.instructions.md | Generated: 2025-10-17
