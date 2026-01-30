## What/When/Why/How
- What: Joyride 用户脚本项目助手（ClojureScript + VS Code API 的 REPL 驱动自动化）。
- When: 在用户目录或工程中使用 Joyride 开发交互式脚本、一次性自动化、可视化 Flare 等。
- Why: 通过 REPL 实时验证与演进，获得更可靠、更快速的 VS Code 自动化体验。
- How: 阅读 README 与 scripts/src；用 Joyride evaluation 在正确命名空间下小步评估并验证。

## Key Points
- 信息源：agent-joyride-eval.md、user-assistance.md（通过 fetch 获取最新）。
- 哲学：交互式编程；小步构建；数据优先；尽量无副作用；必要副作用可控。
- 命名空间：使用 (in-ns 'ns) 明确评估目标；避免落到 user 命名空间。
- VS Code API：vscode/window/commands；输入选择需 awaitResult: true。
- Joyride API：joyride.core/*file*、load-file、slurp、extension-context、output-channel。
- Promise：使用 promesa/p 处理异步；prefer 直接 awaitResult 收敛结果。
- Flare：用 joyride.flare/flare!+ 生成可视 WebView/侧边栏，支持消息通信与资源文件。
- 扩展互操作：检测扩展已安装与激活后安全调用其 API。
- 脚本守卫：仅在被直接运行时执行 main（invoked-script == *file*）。
- Disposables：注册到 extension-context 的 subscriptions。

## Compact Map
Joyride
- REPL 驱动
- (in-ns) 定位
- VS Code API 互操作
- joyride.core/flare
- awaitResult/Promise
- 脚本守卫/Disposables

## Checklist
- [ ] 读取并验证 docs 最新内容
- [ ] 在 REPL 先试后改文件
- [ ] 关键对话框使用 awaitResult: true
- [ ] 管理并清理 Disposables
- [ ] Flare 组件保留引用可关闭

## Example Questions (≥10)
- 如何在 REPL 中安全调用 showQuickPick 并拿到返回值？
- 如何用 flare!+ 创建带 Hiccup 的侧边栏并实现消息通信？
- 怎么用 joyride.core/load-file 热加载脚本？
- 如何在 VS Code 中获取已安装的 Python 扩展信息？
- awaitResult 何时必须开启？
- promesa 的 p/let 在 Joyride 场景的常见用法？
- 如何编写脚本只在被直接运行时执行？
- 如何把事件监听器注册到 subscriptions 并在需要时释放？
- 如何在 REPL 中逐步构建函数而非一次写完？
- 如何组织命名空间与关键字以保持数据平坦且可组合？

Source: d:\mycode\awesome-copilot\instructions\joyride-user-project.instructions.md | Generated: 2025-10-17
