---
agent: 'agent'
tools: ['changes', 'search/codebase', 'edit/editFiles', 'problems']
description: 'Get best practices for C# async programming'
---

# C# 异步编程最佳实践

您的目标是帮助我遵循 C# 异步编程的最佳实践。

## 命名约定

- 对所有异步方法使用“Async”后缀
- 如果适用，将方法名称与其同步对应项相匹配（例如，`GetDataAsync()` 对应 `GetData()`）

## 返回类型

- 当方法返回值时返回 `Task<T>`
- 当方法没有返回值时返回 `Task`
- 对于高性能场景，请考虑 `ValueTask<T>` 以减少分配
- 避免为除事件处理程序之外的异步方法返回 `void`

## 异常处理

- 在await 表达式周围使用try/catch 块
- 避免在异步方法中吞咽异常
- 在适当的时候使用 `ConfigureAwait(false)` 来防止库代码中的死锁
- 使用 `Task.FromException()` 传播异常，而不是抛出异步任务返回方法

## 性能

- 使用 `Task.WhenAll()` 并行执行多个任务
- 使用 `Task.WhenAny()` 实现超时或执行第一个完成的任务
- 仅传递任务结果时避免不必要的异步/等待
- 考虑对长时间运行的操作使用取消令牌

## 常见陷阱

- 切勿在异步代码中使用 `.Wait()`、`.Result` 或 `.GetAwaiter().GetResult()`
- 避免混合阻塞和异步代码
- 不要创建 async void 方法（事件处理程序除外）
- 始终等待任务返回方法

## 实施模式

- 为长时间运行的操作实现异步命令模式
- 使用异步流 (IAsyncEnumerable<T>) 异步处理序列
- 考虑公共 API 的基于任务的异步模式 (TAP)

在检查我的 C# 代码时，确定这些问题并提出遵循这些最佳实践的改进建议。
