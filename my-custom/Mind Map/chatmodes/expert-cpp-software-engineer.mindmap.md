## What / When / Why / How

- What: C++ 软件工程专家（现代 C++、构建、性能、工具链）
- When: 需要高性能/低延迟/系统级开发与优化
- Why: 利用现代 C++ 特性与生态构建可靠可维护系统
- How: 需求→接口→实现→测试→分析→调优→文档

## Key Points

- 现代 C++：RAII、智能指针、constexpr、ranges、协程
- 构建：CMake/包管理（vcpkg/conan）
- 工具： sanitizers、valgrind、perf、clang-tidy、ASan/TSan/UBSan
- ABI/并发：内存模型、锁/无锁、原子/栅栏
- 跨平台：条件编译/CI matrix

## Compact Map

- 设计：接口/异常/错误
- 实现：值语义/移动语义
- 测试：gtest/benchmark
- 调优：profile→fix→verify
- 交付：包/文档/示例

## Example Questions (10+)

- 该模块的异常与错误处理策略是什么？
- 值/移动语义如何设计以避免拷贝？
- 哪些热点函数需要基准与内联/向量化？
- 内存分配模式如何优化与复用？
- 线程安全与锁竞争如何评估与消除？
- ABI 稳定性与版本语义如何保证？
- 哪些 UB 风险需要 sanitizer 覆盖？
- CMake/包管理如何组织以便复用？
- 平台差异（Windows/Linux/macOS）需特别处理什么？
- 日志与监控如何内置且零成本切换？
- 第三方依赖的许可证合规如何核对？

---
Source: d:\mycode\awesome-copilot\chatmodes\expert-cpp-software-engineer.chatmode.md
Generated: {{timestamp}}
