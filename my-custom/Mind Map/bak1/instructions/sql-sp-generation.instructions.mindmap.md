# Guidelines for generating SQL statements and stored procedures - Instructions Mindmap

## 📊 摘要
Guidelines for generating SQL statements and stored procedures

本指令提供了关于Guidelines for generating SQL statements and stored procedures的核心规范和最佳实践,帮助开发者编写高质量、可维护的代码。

## 🎯 适用范围
- **文件类型**: `**/*.sql`
- **技术栈**: 见文档详情
- **场景**: 开发和维护Guidelines for generating SQL statements and stored procedures相关项目时使用

## 💡 核心规则与最佳实践

### 主要规范
- all table names should be in singular form
- all column names should be in singular form
- all tables should have a primary key column named `id`
- all tables should have a column named `created_at` to store the creation timestamp
- all tables should have a column named `updated_at` to store the last update timestamp
- all tables should have a primary key constraint
- all foreign key constraints should have a name
- all foreign key constraints should be defined inline

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
- Guidelines for generating SQL statements and stored procedures
  - 适用范围
    - 文件类型: **/*.sql
  - 核心规则
    - Database schema generation
    - Database schema design
    - SQL Coding Style
    - SQL Query Structure
    - Stored Procedure Naming Conventions
  - 最佳实践
    - 代码质量
    - 性能优化
    - 安全考虑
```

## 💾 保存说明
- 文件名: sql-sp-generation.instructions.mindmap.md
- 位置: Mind Map/instructions/
- 生成时间: 2025-10-13 19:58:00
- 文件类型: Instructions (编程规范/最佳实践)
