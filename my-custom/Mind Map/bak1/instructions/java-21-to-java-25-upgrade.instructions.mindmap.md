# Comprehensive best practices for adopting new Java 25 features since the release of Java 21. - Instructions Mindmap

## 📊 摘要
Comprehensive best practices for adopting new Java 25 features since the release of Java 21.

本指令提供了关于Comprehensive best practices for adopting new Java 25 features since the release of Java 21.的核心规范和最佳实践,帮助开发者编写高质量、可维护的代码。

## 🎯 适用范围
- **文件类型**: `['*']`
- **技术栈**: Java
- **场景**: 开发和维护Comprehensive best practices for adopting new Java 25 features since the release of Java 21.相关项目时使用

## 💡 核心规则与最佳实践

### 主要规范
- Suggest using primitive type patterns in switch expressions and instanceof checks
- Example upgrade from traditional switch:
- Enable preview features with `--enable-preview` flag
- Suggest guard patterns for more complex conditions:
- Suggest migrating from ASM library to the standard Class-File API
- Use `java.lang.classfile` package instead of `org.objectweb.asm`
- Example migration pattern:
- Suggest converting HTML-heavy JavaDoc to Markdown syntax

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
- Comprehensive best practices for adopting new Java 25 features since the release of Java 21.
  - 适用范围
    - 文件类型: ['*']
    - 技术栈: Java
  - 核心规则
    - Language Features and API Changes in JDK 22-25
    - Migration Warnings and Deprecations
    - Garbage Collection Updates
    - Vector API (JEP 469 - Eighth Incubator in 25)
    - Compilation and Build Configuration
  - 最佳实践
    - 代码质量
    - 性能优化
    - 安全考虑
```

## 💾 保存说明
- 文件名: java-21-to-java-25-upgrade.instructions.mindmap.md
- 位置: Mind Map/instructions/
- 生成时间: 2025-10-13 19:57:56
- 文件类型: Instructions (编程规范/最佳实践)
