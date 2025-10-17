## What
- TaskSync V4 协议：强制通过终端 Read-Host 循环获取任务，严禁自动结束会话与“结语”

## When
- 需要长时间连续执行任务、通过终端输入循环派发任务时

## Why
- 避免会话中断，保障自动化连续性与可控的人机交互节奏

## How
- 禁止事项
  - 任何自动结束/告别语/等待用户提示；仅允许显式 stop/end/terminate/quit 终止
- 强制循环
  - 完成任一任务后立刻执行 `$task = Read-Host "Enter your task"`
  - 若检测将结束会话，立即再次执行 Read-Host（紧急覆写）
- 状态机
  - State1 执行任务 → State2 请求任务（必须执行 Read-Host）→ 循环；State3 仅在显式终止
- 终端协议
  - 标准提问：Enter your task；问题模式：How can I help you?
  - 解析 none/stop/quit 等特殊命令
- 通信
  - 完成后简要总结 + 立刻宣告“Requesting next task from terminal.” 并运行 Read-Host
- 错误处理
  - 终端失败时重试；任务冲突优先完成当前或处理紧急覆写

## Key Points
- 永不结束、无结语、始终通过终端请求下一任务
- 任务计数与状态跟踪

## Compact Map
- 禁止: 结束/结语/等待
- 循环: 执行→请求→执行
- 命令: Read-Host/none/stop
- 优先: 紧急覆写>当前任务

## Example Questions
1) 完成任务后具体需要输出哪两步？
2) 何时进入 State2 且必须做什么？
3) 收到 none 时应如何处理？
4) 如何识别并处理紧急覆盖任务？
5) 会话即将结束时如何自救？
6) 哪些结语是被禁止的？
7) 如何做任务计数与状态跟踪？
8) 错误场景下 Read-Host 重试策略？
9) 终止的合法命令有哪些？
10) 与普通聊天式提问有何差异？
11) 何时需要问题模式的 Read-Host？

Source: d:\mycode\awesome-copilot\instructions\tasksync.instructions.md | Generated: 2025-10-17
