# PowerShell Pester testing best practices based on Pester v5 conventions - Instructions Mindmap

## 📊 摘要
PowerShell Pester testing best practices based on Pester v5 conventions

本指令提供了关于PowerShell Pester testing best practices based on Pester v5 conventions的核心规范和最佳实践,帮助开发者编写高质量、可维护的代码。

## 🎯 适用范围
- **文件类型**: `**/*.Tests.ps1`
- **技术栈**: 见文档详情
- **场景**: 开发和维护PowerShell Pester testing best practices based on Pester v5 conventions相关项目时使用

## 💡 核心规则与最佳实践

### 主要规范
- File Convention:** Use `*.Tests.ps1` naming pattern
- Placement:** Place test files next to tested code or in dedicated test directories
- Import Pattern:** Use `BeforeAll { . $PSScriptRoot/FunctionName.ps1 }` to import tested functions
- No Direct Code:** Put ALL code inside Pester blocks (`BeforeAll`, `Describe`, `Context`, `It`, etc.)
- `Describe`**: Top-level grouping, typically named after function being tested
- `Context`**: Sub-grouping within Describe for specific scenarios
- `It`**: Individual test cases, use descriptive names
- `Should`**: Assertion keyword for test validation

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
- PowerShell Pester testing best practices based on Pester v5 conventions
  - 适用范围
    - 文件类型: **/*.Tests.ps1
  - 核心规则
    - File Naming and Structure
    - Test Structure Hierarchy
    - Core Keywords
    - Setup and Teardown
    - Assertions (Should)
  - 最佳实践
    - 代码质量
    - 性能优化
    - 安全考虑
```

## 💾 保存说明
- 文件名: powershell-pester-5.instructions.mindmap.md
- 位置: Mind Map/instructions/
- 生成时间: 2025-10-13 19:57:58
- 文件类型: Instructions (编程规范/最佳实践)
