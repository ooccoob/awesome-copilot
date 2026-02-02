---
description: 'Guidelines for creating high-quality custom instruction files for GitHub Copilot'
applyTo: '**/*.instructions.md'
---

# 自定义说明文件指南

有关创建有效且可维护的自定义说明文件的说明，这些文件指导 GitHub Copilot 生成特定于域的代码并遵循项目约定。

## 项目背景

- 目标受众：使用特定于域的代码的开发人员和 GitHub Copilot
- 文件格式：带有 YAML frontmatter 的 Markdown
- 文件命名约定：小写字母加连字符（例如 `react-best-practices.instructions.md`）
- 位置：`.github/instructions/`目录
- 目的：为代码生成、审查和文档提供上下文感知指导

## 必需的前言

每个指令文件必须包含带有以下字段的 YAML frontmatter：

```yaml
---
description: 'Brief description of the instruction purpose and scope'
applyTo: 'glob pattern for target files (e.g., **/*.ts, **/*.py)'
---
```

### 前沿事项指南

- **描述**：单引号字符串，1-500个字符，明确说明用途
- **applyTo**：指定这些指令适用于哪些文件的全局模式
  - 单一模式：`'**/*.ts'`
  - 多种模式：`'**/*.ts, **/*.tsx, **/*.js'`
  - 具体文件：`'src/**/*.py'`
  - 所有文件：`'**'`

## 文件结构

结构良好的说明文件应包括以下部分：

### 1. 标题和概述

- 使用 `#` 标题的清晰描述性标题
- 简要介绍解释目的和范围
- 可选：包含关键技术和版本的项目上下文部分

### 2. 核心部分

根据领域将内容组织成逻辑部分：

- **一般说明**：高级指南和原则
- **最佳实践**：推荐的模式和方法
- **代码标准**：命名约定、格式、样式规则
- **架构/结构**：项目组织和设计模式
- **常见模式**：常用的实现
- **安全**：安全考虑（如果适用）
- **性能**：优化指南（如果适用）
- **测试**：测试标准和方法（如果适用）

### 3. 示例和代码片段

提供带有清晰标签的具体示例：

```markdown
### Good Example
\`\`\`language
// Recommended approach
code example here
\`\`\`

### Bad Example
\`\`\`language
// Avoid this pattern
code example here
\`\`\`
```

### 4. 验证和验证（可选但推荐）

- 构建命令来验证代码
- 语法检查和格式化工具
- 测试要求
- 验证步骤

## 内容指南

### 写作风格

- 使用清晰、简洁的语言
- 以祈使语气写作（“使用”、“实施”、“避免”）
- 具体且可操作
- 避免使用含糊不清的术语，如“应该”、“可能”、“可能”
- 使用项目符号和列表以提高可读性
- 保持章节集中且易于浏览

### 最佳实践

- **具体**：提供具体的例子而不是抽象的概念
- **展示原因**：解释推荐背后的理由（当它增加价值时）
- **使用表格**：用于比较选项、列出规则或显示模式
- **包括示例**：真实的代码片段比描述更有效
- **保持最新**：参考当前版本和最佳实践
- **链接资源**：包括官方文档和权威来源

### 要包含的常见模式

1. **命名约定**：如何命名变量、函数、类、文件
2. **代码组织**：文件结构、模块组织、导入顺序
3. **错误处理**：首选错误处理模式
4. **依赖关系**：如何管理和记录依赖关系
5. **注释和文档**：何时以及如何记录代码
6. **版本信息**：目标语言/框架版本

## 遵循的模式

### 要点和列表

```markdown
## Security Best Practices

- Always validate user input before processing
- Use parameterized queries to prevent SQL injection
- Store secrets in environment variables, never in code
- Implement proper authentication and authorization
- Enable HTTPS for all production endpoints
```

### 结构化信息表

```markdown
## Common Issues

| Issue            | Solution            | Example                       |
| ---------------- | ------------------- | ----------------------------- |
| Magic numbers    | Use named constants | `const MAX_RETRIES = 3`       |
| Deep nesting     | Extract functions   | Refactor nested if statements |
| Hardcoded values | Use configuration   | Store API URLs in config      |
```

### 代码比较

```markdown
### Good Example - Using TypeScript interfaces
\`\`\`typescript
interface User {
  id: string;
  name: string;
  email: string;
}

function getUser(id: string): User {
  // Implementation
}
\`\`\`

### Bad Example - Using any type
\`\`\`typescript
function getUser(id: any): any {
  // Loses type safety
}
\`\`\`
```

### 有条件指导

```markdown
## Framework Selection

- **For small projects**: Use Minimal API approach
- **For large projects**: Use controller-based architecture with clear separation
- **For microservices**: Consider domain-driven design patterns
```

## 要避免的模式

- **过于冗长的解释**：保持简洁且易于浏览
- **过时的信息**：始终参考当前版本和实践
- **不明确的指导方针**：具体说明要做什么或要避免什么
- **缺少示例**：没有具体代码示例的抽象规则
- **矛盾的建议**：确保整个文件的一致性
- **从文档复制粘贴**：通过提炼和情境化来增加价值

## 测试您的指令

在最终确定说明文件之前：

1. **使用 Copilot 进行测试**：在 VS Code 中尝试使用实际提示的说明
2. **验证示例**：确保代码示例正确且运行无错误
3. **检查 Glob 模式**：确认 `applyTo` 模式与预期文件匹配

## 结构示例

这是新指令文件的最小示例结构：

```markdown
---
description: 'Brief description of purpose'
applyTo: '**/*.ext'
---

# Technology Name Development

Brief introduction and context.

## General Instructions

- High-level guideline 1
- High-level guideline 2

## Best Practices

- Specific practice 1
- Specific practice 2

## Code Standards

### Naming Conventions
- Rule 1
- Rule 2

### File Organization
- Structure 1
- Structure 2

## Common Patterns

### Pattern 1
Description and example

\`\`\`language
code example
\`\`\`

### Pattern 2
Description and example

## Validation

- Build command: `command to verify`
- Linting: `command to lint`
- Testing: `command to test`
```

## 维护保养

- 更新依赖项或框架时查看说明
- 更新示例以反映当前的最佳实践
- 删除过时的模式或已弃用的功能
- 添加社区中出现的新模式
- 随着项目结构的发展保持全局模式的准确性

## 其他资源

- [自定义指令文档](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [很棒的副驾驶指令](https://github.com/github/awesome-copilot/tree/main/instructions)
