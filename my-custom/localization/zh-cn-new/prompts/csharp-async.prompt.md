---
mode: 'agent'
tools: ['changes', 'codebase', 'edit/editFiles', 'problems']
description: '获取C#异步编程最佳实践'
---

# C#异步编程最佳实践

您的目标是帮助我在C#中遵循异步编程的最佳实践。

## 命名约定

- 对所有异步方法使用'Async'后缀
- 当适用时，与同步对应方法匹配方法名称（例如，`GetData()`对应`GetDataAsync()`）

## 返回类型

- 当方法返回值时返回`Task<T>`
- 当方法不返回值时返回`Task`
- 在高性能场景中考虑`ValueTask<T>`以减少分配
- 避免异步方法返回`void`，事件处理器除外

## 异常处理

- 在await表达式周围使用try/catch块
- 避免在异步方法中吞并异常
- 在适当时使用`ConfigureAwait(false)`以防止库代码中的死锁
- 使用`Task.FromException()`传播异常，而不是在返回异步Task的方法中抛出异常

## 性能

- 使用`Task.WhenAll()`进行多个任务的并行执行
- 使用`Task.WhenAny()`实现超时或获取第一个完成的任务
- 在简单传递任务结果时避免不必要的async/await
- 考虑为长时间运行的操作使用取消令牌

## 常见陷阱

- 永远不要在异步代码中使用`.Wait()`、`.Result`或`.GetAwaiter().GetResult()`
- 避免混合阻塞和异步代码
- 不要创建async void方法（事件处理器除外）
- 始终await返回Task的方法

## 实现模式

- 为长时间运行的操作实现异步命令模式
- 使用异步流（IAsyncEnumerable<T>）异步处理序列
- 为公共API考虑基于任务的异步模式（TAP）

在审查我的C#代码时，识别这些问题并建议遵循这些最佳实践的改进。