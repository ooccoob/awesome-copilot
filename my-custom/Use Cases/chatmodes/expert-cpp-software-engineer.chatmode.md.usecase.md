---
post_title: "expert-cpp-software-engineer.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "expert-cpp-software-engineer-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases","cpp","performance"]
ai_note: "Generated with AI assistance."
summary: "C++ 专家用例：高性能、内存管理、并发与平台兼容性的实战指南。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 提供 C++ 项目中性能与内存安全的工程用例：资源管理、缓存设计、并发与跨平台打包示例。

## When

- 构建高性能库、移植旧代码或修复内存/并发缺陷时使用。

## Why

- 减少内存泄露、提升运行效率并保证跨平台构建的可重复性。

## How

- 包含 RAII 模式示例、智能指针使用、缓存和内存池设计、Thread Sanitizer/ASAN 检测步骤与基准工具链。

## Key points (英文+中文对照)

- RAII & smart pointers（资源管理）
- UB & safe coding（未定义行为与安全编码）
- Concurrency & atomics（并发与原子操作）
- Profiling & ASAN/TSAN（分析与检测）
- Cross-platform build（跨平台构建）

## 使用场景

### 1. 内存管理与所有权

- 用户故事：作为开发者，我要消除泄露并清晰表述对象所有权。
- 例 1："用 unique_ptr/shared_ptr 的替换示例与内存归属说明。"
- 例 2："示例避免裸指针的迁移策略。"
- 例 3："内存池/对象池设计与适用场景。"
- 例 4："ASAN/Valgrind 的使用模板。"
- 例 5："常见 UB 触发点与检测方法。"

### 2. 并发与同步

- 用户故事：作为系统工程师，我要保证并发代码的正确性与性能。
- 例 1："使用 atomics/lock-free 的示例与陷阱说明。"
- 例 2："线程池设计与任务调度示例。"
- 例 3："TSAN 的检查与修复流程。"
- 例 4："减少锁竞争的重构建议。"
- 例 5："并发数据结构的选择与权衡。"

### 3. 性能优化与基准

- 用户故事：作为性能工程师，我要精确测量并改进热路径。
- 例 1："基准工具（Google Benchmark）示例与基线建立。"
- 例 2："内联/编译优化与其影响的评估示例。"
- 例 3："缓存局部性优化示例。"
- 例 4："剖析 CPU/内存热点的工具与命令。"
- 例 5："减少分配/复制的策略。"

### 4. 平台兼容与构建

- 用户故事：作为 Release 工程师，我要保证可重复构建与发行包质量。
- 例 1："CMake 最佳实践与多平台配置示例。"
- 例 2："静态分析与 lint（clang-tidy）集成。"
- 例 3："打包与符号管理示例（Windows/Linux）。"
- 例 4："自动化测试在不同架构上的运行策略。"
- 例 5："ABI 兼容性检查与版本策略。"

### 5. 安全与漏洞检测

- 用户故事：作为安全团队，我要减少内存安全漏洞并快速识别 CVE 风险。
- 例 1："使用静态分析定位潜在越界/未初始化使用。"
- 例 2："依赖项安全扫描与快速修复流程。"
- 例 3："缓冲区安全策略与示例（safe wrappers）。"
- 例 4："回归测试与 fuzzing 集成示例。"
- 例 5："发布时的安全检查清单。"

## 原始文件

- [chatmodes/expert-cpp-software-engineer.chatmode.md](../../../chatmodes/expert-cpp-software-engineer.chatmode.md)
