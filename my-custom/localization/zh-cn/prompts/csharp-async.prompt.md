---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems"]
description: "获取 C# 异步编程最佳实践"
---

# C# 异步编程最佳实践

你的目标是帮助我遵循 C# 异步编程的最佳实践。

## 命名约定

- 所有异步方法使用 `Async` 后缀
- 与同步方法成对时，名称应保持对应（例如 `GetData()` 对应 `GetDataAsync()`）

## 返回类型

- 返回值使用 `Task<T>`
- 无返回值使用 `Task`
- 高性能、减少分配场景可考虑 `ValueTask<T>`
- 除事件处理器外，避免 `async void`

## 异常处理

- 在 await 表达式周围使用 try/catch
- 避免吞掉异常
- 在库代码中适当使用 `ConfigureAwait(false)` 防止死锁
- 对于返回 Task 的异步方法，用 `Task.FromException()` 传播异常而非直接抛出

## 性能

- 使用 `Task.WhenAll()` 并行执行多个任务
- 使用 `Task.WhenAny()` 实现超时或取首个完成的任务
- 仅传递任务结果时避免不必要的 async/await 包装
- 对长时间运行的操作考虑使用取消令牌（CancellationToken）

## 常见陷阱

- 异步代码中不要使用 `.Wait()`、`.Result` 或 `.GetAwaiter().GetResult()`
- 避免混用阻塞与异步代码
- 不要创建 `async void` 方法（事件处理器除外）
- 始终等待（await）返回 Task 的方法

## 实施模式

- 对长时间运行的操作实现异步命令模式
- 使用异步流（`IAsyncEnumerable<T>`）按序异步处理
- 对公共 API 采用基于 Task 的异步模式（TAP）

在审查我的 C# 代码时，请识别上述问题并给出改进建议。

```

```
