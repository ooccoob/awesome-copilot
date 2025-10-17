## 文档综述（What/When/Why/How）

- What：C# 异步编程最佳实践提示词（命名/返回/异常/性能/陷阱/模式）

- When：评审/重构异步代码或设计公开 API 时

- Why：减少死锁/阻塞/泄漏等问题，提升可维护性与性能

- How：按条目化规范进行审核与修正，覆盖 Await/Task/ValueTask/并发/取消/异常处理等

## 示例提问（Examples）

- “检查该库是否存在 .Result/.Wait 阻塞与混用同步/异步问题”

- “为批量 IO 使用 WhenAll，补充取消令牌与异常聚合处理”

## 结构化要点（CN/EN）

- 命名/Naming：Async 后缀

- 返回/Return：Task/Task<T>/ValueTask

- 异常/Exceptions：try/catch、ConfigureAwait(false)

- 性能/Perf：并行/避免多余 async/await

- 陷阱/Pitfalls：禁用 .Result/.Wait；避免 async void

## 中文思维导图

- 命名与返回
- 异常与上下文
- 并发与取消
- 常见陷阱
- 实现模式

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\csharp-async.prompt.md

- 生成时间：2025-10-17
