# Clojure-specific coding patterns, inline def usage, code block templates, and namespace handling for Clojure development. - Instructions Mindmap

## 📊 摘要
Clojure-specific coding patterns, inline def usage, code block templates, and namespace handling for Clojure development.

本指令提供了关于Clojure-specific coding patterns, inline def usage, code block templates, and namespace handling for Clojure development.的核心规范和最佳实践,帮助开发者编写高质量、可维护的代码。

## 🎯 适用范围
- **文件类型**: `**/*.{clj,cljs,cljc,bb,edn.mdx?}`
- **技术栈**: 见文档详情
- **场景**: 开发和维护Clojure-specific coding patterns, inline def usage, code block templates, and namespace handling for Clojure development.相关项目时使用

## 💡 核心规则与最佳实践

### 主要规范
- Always stay inside Calva's REPL instead of launching a second one from the terminal.
- If there is no REPL connection, ask the user to connect the REPL instead of trying to start and connect it yourself.
- Define functions before they are used—prefer ordering over `declare` except when truly necessary.
- Dynamic dependency loading requires Clojure 1.12 or later
- Perfect for library exploration and prototyping
- Interactive Programming requires a working REPL** - You cannot verify behavior without evaluation
- Guessing creates bugs** - Code changes without testing introduce errors
- Develop changes in the REPL before touching files.

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
- Clojure-specific coding patterns, inline def usage, code block templates, and namespace handling for Clojure development.
  - 适用范围
    - 文件类型: **/*.{clj,cljs,cljc,bb,edn.mdx?}
  - 核心规则
    - Code Evaluation Tool usage
    - Docstrings in `defn`
    - Interactive Programming (a.k.a. REPL Driven Development)
    - Structural Editing and REPL-First Habit
    - Code Indentation Before Evaluation
  - 最佳实践
    - 代码质量
    - 性能优化
    - 安全考虑
```

## 💾 保存说明
- 文件名: clojure.instructions.mindmap.md
- 位置: Mind Map/instructions/
- 生成时间: 2025-10-13 19:57:53
- 文件类型: Instructions (编程规范/最佳实践)
