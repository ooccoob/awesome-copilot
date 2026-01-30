## What/When/Why/How
- What: Rust 代码规范与 API 设计（风格/错误/所有权/测试）
- When: 开发或评审 Rust 库与二进制
- Why: 保持安全/高效/可维护与可演进
- How: Idiomatic Rust + 所有权/借用 + 错误与 API 指南

## Key Points
- 风格：rustfmt；行宽≈100；clippy 零警告
- 所有权：借用优先；&str 参数；零拷贝；Rc/Arc/RefCell/Mutex 场景
- 错误：Result/Option；? 传播；thiserror/anyhow；有意义消息
- API：新类型/特定类型代替 bool；实现 Debug/Clone/Default/From
- 异步：tokio/async-std；async/await；共享状态 Arc<RwLock>
- 模块：lib/main 分离；封装字段；sealed traits 防外部实现
- 性能：迭代器优先；避免不必要分配；并行 rayon
- 测试：单元/集成；示例用 ?；文档注释 ///

## Compact Map
- Ownership: borrow→mut borrow→move
- Errors: Result + thiserror/anyhow
- API: traits/From/AsRef/newtype
- Tooling: fmt/clippy/test/doc

## Example Questions
1) 公有 API 是否完整文档与示例？
2) 是否避免 unwrap/expect 并使用 ? 传播？
3) 借用是否优于 clone，零拷贝是否可行？
4) 错误类型是否清晰且实现标准 traits？
5) 是否实现 Debug/Display/FromIterator 等常用 traits？
6) 结构体字段是否私有并提供构建器？
7) 并发共享是否用 Arc<RwLock>/Mutex 并避免死锁？
8) 迭代器/组合子是否替代索引循环？
9) clippy 是否通过且无 unsafe（或有注释）？
10) 模块结构是否支持复用与测试？
11) 依赖与特性 flags 是否最小化？

Source: d:\mycode\awesome-copilot\instructions\rust.instructions.md | Generated: 2025-10-17
