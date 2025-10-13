# Instructions for using LangChain with Python - Instructions Mindmap

## 📊 摘要
Instructions for using LangChain with Python

本指令提供了关于Instructions for using LangChain with Python的核心规范和最佳实践,帮助开发者编写高质量、可维护的代码。

## 🎯 适用范围
- **文件类型**: `**/*.py`
- **技术栈**: Python
- **场景**: 开发和维护Instructions for using LangChain with Python相关项目时使用

## 💡 核心规则与最佳实践

### 主要规范
- All major LangChain components (chat models, output parsers, retrievers, graphs) implement the Runnable interface.
- Supports synchronous (`invoke`, `batch`, `stream`) and asynchronous (`ainvoke`, `abatch`, `astream`) execution.
- Batching (`batch`, `batch_as_completed`) is optimized for parallel API calls; set `max_concurrency` in `RunnableConfig` to control parallelism.
- Streaming APIs (`stream`, `astream`, `astream_events`) yield outputs as they are produced, critical for responsive LLM apps.
- Input/output types are component-specific (e.g., chat models accept messages, retrievers accept strings, output parsers accept model outputs).
- Inspect schemas with `get_input_schema`, `get_output_schema`, and their JSONSchema variants for validation and OpenAPI generation.
- Use `with_types` to override inferred input/output types for complex LCEL chains.
- Compose Runnables declaratively with LCEL: `chain = prompt | chat_model | output_parser`.

### 代码质量标准
- 遵循行业标准编码规范
- 保持代码简洁可读
- 添加适当的注释和文档
- 进行充分的测试覆盖

## 📝 关键技术要点

### 项目配置
- 正确设置开发环境
- 配置必要的工具和依赖
- 遵循项目结构规范

### 实现标准
- 使用推荐的设计模式
- 遵循命名规范
- 注意性能和安全考虑

## 🗺️ 思维导图

```mindmap
- Instructions for using LangChain with Python
  - 适用范围
    - 文件类型: **/*.py
    - 技术栈: Python
  - 核心规则
    - Runnable Interface (LangChain-specific)
    - Embeddings & vectorstores
    - Vector stores (LangChain-specific)
    - Prompt engineering & governance
    - Chat models
  - 最佳实践
    - 代码质量
    - 性能优化
    - 安全考虑
```

## 💾 保存说明
- 文件名: langchain-python.instructions.mindmap.md
- 位置: Mind Map/instructions/
- 生成时间: 2025-10-13 19:57:56
- 文件类型: Instructions (编程规范/最佳实践)
