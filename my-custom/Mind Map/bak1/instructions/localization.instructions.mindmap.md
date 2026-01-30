# Guidelines for localizing markdown documents - Instructions Mindmap

## 📊 摘要
Guidelines for localizing markdown documents

本指令提供了关于Guidelines for localizing markdown documents的核心规范和最佳实践,帮助开发者编写高质量、可维护的代码。

## 🎯 适用范围
- **文件类型**: `**/*.md`
- **技术栈**: 见文档详情
- **场景**: 开发和维护Guidelines for localizing markdown documents相关项目时使用

## 💡 核心规则与最佳实践

### 主要规范
- Find all markdown documents and localize them into given locale.
- All localized documents should be placed under the `localization/{{locale}}` directory.
- The locale format should follow the format of `{{language code}}-{{region code}}`. The language code is defined in ISO 639-1, and the region code is d
- Localize all the sections and paragraphs in the original documents.
- DO NOT miss any sections nor any paragraphs while localizing.
- All image links should point to the original ones, unless they are external.
- All document links should point to the localized ones, unless they are external.
- ALWAYS add the disclaimer to the end of each localized document.

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
- Guidelines for localizing markdown documents
  - 适用范围
    - 文件类型: **/*.md
  - 核心规则
    - Instruction
    - Disclaimer
  - 最佳实践
    - 代码质量
    - 性能优化
    - 安全考虑
```

## 💾 保存说明
- 文件名: localization.instructions.mindmap.md
- 位置: Mind Map/instructions/
- 生成时间: 2025-10-13 19:57:56
- 文件类型: Instructions (编程规范/最佳实践)
