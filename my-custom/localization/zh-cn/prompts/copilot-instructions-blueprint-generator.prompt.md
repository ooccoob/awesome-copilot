---
description: "与技术无关的蓝图生成器：通过分析既有代码库模式，生成全面的 copilot-instructions.md，用于指导 GitHub Copilot 产出符合项目标准、架构风格与精确技术版本的代码，并避免臆测。"
---

# Copilot 指令蓝图生成器（Copilot Instructions Blueprint Generator）

## 配置变量

${PROJECT_TYPE="Auto-detect|.NET|Java|JavaScript|TypeScript|React|Angular|Python|Multiple|Other"} <!-- 主技术栈 -->
${ARCHITECTURE_STYLE="Layered|Microservices|Monolithic|Domain-Driven|Event-Driven|Serverless|Mixed"} <!-- 架构风格 -->
${CODE_QUALITY_FOCUS="Maintainability|Performance|Security|Accessibility|Testability|All"} <!-- 质量优先级 -->
${DOCUMENTATION_LEVEL="Minimal|Standard|Comprehensive"} <!-- 文档要求程度 -->
${TESTING_REQUIREMENTS="Unit|Integration|E2E|TDD|BDD|All"} <!-- 测试策略 -->
${VERSIONING="Semantic|CalVer|Custom"} <!-- 版本化方式 -->

## 生成的提示

"生成一份全面的 copilot-instructions.md，用于指导 GitHub Copilot 生成与我们项目的标准、架构与技术版本完全一致的代码。指令必须严格基于代码库中实际存在的模式，不得做任何臆测。按以下方法执行：

### 1. 核心指令结构

```markdown
# GitHub Copilot Instructions

## Priority Guidelines

当为本仓库生成代码时：

1. **版本兼容**：始终检测并遵守项目使用的语言、框架与库的精确版本
2. **上下文文件**：优先遵循 .github/copilot 目录中的模式与标准
3. **代码库模式**：若上下文文件无具体指引，扫描代码库以发现既有模式
4. **架构一致**：维持我们的 ${ARCHITECTURE_STYLE} 架构风格与既定边界
5. **代码质量**：在所有生成代码中优先考虑 ${CODE_QUALITY_FOCUS == "All" ? "可维护性、性能、安全性、可访问性与可测试性" : CODE_QUALITY_FOCUS}

## Technology Version Detection

在生成代码前，扫描代码库识别：

1. **语言版本**：检测所用编程语言的精确版本

   - 检查项目文件、配置文件与包管理器
   - 查找语言特定的版本指示（例如 .NET 项目中的 <LangVersion>）
   - 不得使用超出已检测版本范围的语言特性

2. **框架版本**：识别所有框架的精确版本

   - 检查 package.json、.csproj、pom.xml、requirements.txt 等
   - 生成代码需遵守版本约束
   - 不得建议未在已检测框架版本中提供的特性

3. **库版本**：记录关键库与依赖的精确版本
   - 生成与这些特定版本兼容的代码
   - 不得使用未在已检测版本中提供的 API 或特性

## Context Files

优先以下 .github/copilot 目录文件（若存在）：

- **architecture.md**：系统架构指南
- **tech-stack.md**：技术版本与框架细节
- **coding-standards.md**：代码风格与格式标准
- **folder-structure.md**：项目组织指南
- **exemplars.md**：应当遵循的示例性代码模式

## Codebase Scanning Instructions

当上下文文件未提供具体指引时：

1. 找到与当前修改/新增文件相似的文件
2. 分析以下模式：

   - 命名约定
   - 代码组织
   - 错误处理
   - 日志方式
   - 文档风格
   - 测试模式

3. 遵循代码库中最一致的模式
4. 若存在冲突模式，优先参考较新的文件或测试覆盖更高的文件
5. 不要引入代码库中不存在的模式

## Code Quality Standards

${CODE_QUALITY_FOCUS.includes("Maintainability") || CODE_QUALITY_FOCUS == "All" ? `### Maintainability

- 使用自解释的清晰命名
- 遵循代码库中的命名与组织约定
- 遵循既有的实现模式以保持一致
- 函数保持单一职责
- 控制函数复杂度与长度与既有代码相当` : ""}

${CODE_QUALITY_FOCUS.includes("Performance") || CODE_QUALITY_FOCUS == "All" ? `### Performance

- 依据既有模式进行内存与资源管理
- 与既有模式一致地处理高计算量操作
- 遵循既有异步模式
- 按照既有模式应用缓存
- 根据代码库中体现的模式进行优化` : ""}

${CODE_QUALITY_FOCUS.includes("Security") || CODE_QUALITY_FOCUS == "All" ? `### Security

- 遵循既有的输入校验模式
- 采用代码库中相同的净化/清洗技术
- 使用与既有模式一致的参数化查询
- 遵循既有认证与授权模式
- 按既有做法处理敏感数据` : ""}

${CODE_QUALITY_FOCUS.includes("Accessibility") || CODE_QUALITY_FOCUS == "All" ? `### Accessibility

- 遵循代码库中的可访问性模式
- ARIA 属性用法与现有组件保持一致
- 保持与现有代码一致的键盘可达性
- 遵循既有的颜色与对比度模式
- 按代码库既有方式提供文本替代` : ""}

${CODE_QUALITY_FOCUS.includes("Testability") || CODE_QUALITY_FOCUS == "All" ? `### Testability

- 遵循既有的可测试性模式
- 匹配代码库中的依赖注入方式
- 使用相同的依赖管理模式
- 遵循既有的 mock 与测试替身策略
- 匹配现有测试的风格` : ""}

## Documentation Requirements

${DOCUMENTATION_LEVEL == "Minimal" ?
`- 匹配现有代码中的注释风格与粒度

- 按代码库中观察到的模式编写文档
- 对非显而易见的行为进行说明，风格与现有一致
- 参数说明格式与既有代码一致` : ""}

${DOCUMENTATION_LEVEL == "Standard" ?
`- 完全遵循代码库既有的文档格式

- 匹配 XML/JSDoc 的风格与完整度
- 以相同风格记录参数、返回与异常
- 跟随既有的用例文档模式
- 类级文档的风格与内容需匹配` : ""}

${DOCUMENTATION_LEVEL == "Comprehensive" ?
`- 参考代码库中最详尽的文档模式

- 匹配最佳文档化文件的风格与完整度
- 与最详尽的文件保持一致的记录方式
- 按既有模式进行文档链接
- 解释设计决策的细节程度需保持一致` : ""}

## Testing Approach

${TESTING_REQUIREMENTS.includes("Unit") || TESTING_REQUIREMENTS == "All" ?
`### Unit Testing

- 匹配现有单元测试的结构与风格
- 使用相同的测试类/方法命名约定
- 采用现有断言模式
- 复用代码库的 mock 方式
- 按既有模式保持测试隔离` : ""}

${TESTING_REQUIREMENTS.includes("Integration") || TESTING_REQUIREMENTS == "All" ?
`### Integration Testing

- 匹配现有集成测试模式
- 测试数据的构造与清理与现有一致
- 采用相同的组件交互测试方法
- 遵循既有的系统行为验证模式` : ""}

${TESTING_REQUIREMENTS.includes("E2E") || TESTING_REQUIREMENTS == "All" ?
`### End-to-End Testing

- 匹配现有 E2E 测试结构与模式
- 遵循既有的 UI 测试做法
- 采用相同的用户旅程验证方法` : ""}

${TESTING_REQUIREMENTS.includes("TDD") || TESTING_REQUIREMENTS == "All" ?
`### Test-Driven Development

- 遵循代码库体现的 TDD 模式
- 匹配既有代码中测试用例的推进节奏
- 测试通过后采用相同的重构步骤` : ""}

${TESTING_REQUIREMENTS.includes("BDD") || TESTING_REQUIREMENTS == "All" ?
`### Behavior-Driven Development

- 匹配现有 Given-When-Then 结构
- 行为描述与现有模式一致
- 测试用例保持与业务一致的关注点` : ""}

## Technology-Specific Guidelines

${PROJECT_TYPE == ".NET" || PROJECT_TYPE == "Auto-detect" || PROJECT_TYPE == "Multiple" ? `### .NET Guidelines

- 检测并严格遵守所用 .NET 版本
- 仅使用与检测版本兼容的 C# 语言特性
- LINQ 用法与代码库保持一致
- 异步 async/await 模式与既有一致
- 依赖注入方式与项目一致
- 集合类型与用法匹配既有代码` : ""}

${PROJECT_TYPE == "Java" || PROJECT_TYPE == "Auto-detect" || PROJECT_TYPE == "Multiple" ? `### Java Guidelines

- 检测并遵守所用 Java 版本
- 设计模式与代码库保持一致
- 异常处理模式匹配现有代码
- 集合类型与用法与既有一致
- 依赖注入模式按现有实现` : ""}

${PROJECT_TYPE == "JavaScript" || PROJECT_TYPE == "TypeScript" || PROJECT_TYPE == "Auto-detect" || PROJECT_TYPE == "Multiple" ? `### JavaScript/TypeScript Guidelines

- 检测并遵守所用 ECMAScript/TypeScript 版本
- 模块 import/export 模式需匹配现有
- TypeScript 类型定义风格保持一致
- 异步模式（Promise、async/await）与现有一致
- 错误处理方式参考相似文件` : ""}

${PROJECT_TYPE == "React" || PROJECT_TYPE == "Auto-detect" || PROJECT_TYPE == "Multiple" ? `### React Guidelines

- 检测并遵守所用 React 版本
- 组件结构模式匹配现有组件
- Hooks 与生命周期用法与既有一致
- 状态管理方式与现有一致
- Props 类型/校验模式与现有一致` : ""}

${PROJECT_TYPE == "Angular" || PROJECT_TYPE == "Auto-detect" || PROJECT_TYPE == "Multiple" ? `### Angular Guidelines

- 检测并遵守所用 Angular 版本
- 组件与模块模式匹配代码库
- 装饰器用法与现有一致
- RxJS 模式与代码库一致
- 组件通信模式参考既有做法` : ""}

${PROJECT_TYPE == "Python" || PROJECT_TYPE == "Auto-detect" || PROJECT_TYPE == "Multiple" ? `### Python Guidelines

- 检测并遵守所用 Python 版本
- 导入组织方式与现有模块一致
- 若使用类型注解，匹配现有风格
- 错误处理与现有代码一致
- 模块组织结构匹配既有` : ""}

## Version Control Guidelines

${VERSIONING == "Semantic" ?
`- 遵循代码库中的语义化版本（SemVer）实践

- 保持破坏性变更的记录方式一致
- 退役/弃用说明方式匹配现有` : ""}

${VERSIONING == "CalVer" ?
`- 遵循代码库中的日历化版本（CalVer）实践

- 变更记录方式保持一致
- 重要变更的高亮方式一致` : ""}

${VERSIONING == "Custom" ?
`- 匹配代码库所用的自定义版本模式

- 变更日志格式保持一致
- 标签约定按项目既有执行` : ""}

## General Best Practices

- 命名约定与现有代码完全一致
- 代码组织模式参考相似文件
- 错误处理保持与现有一致
- 测试方法遵循既有做法
- 日志记录与现有模式一致
- 配置管理方式与代码库一致

## Project-Specific Guidance

- 在生成任何代码前彻底扫描代码库
- 毫无例外地尊重既有的架构边界
- 保持与周边代码的风格与模式一致
- 如有不确定，优先与既有代码一致，而非外部“最佳实践”或更新语言特性
```

### 2. 代码库分析指引

为了创建 copilot-instructions.md，先分析代码库以：

1. **识别精确技术版本**：

   - ${PROJECT_TYPE == "Auto-detect" ? "通过扫描文件扩展名与配置文件检测所有语言、框架与库" : `聚焦 ${PROJECT_TYPE} 相关技术`}
   - 从项目文件、package.json、.csproj 等提取精确版本
   - 记录版本约束与兼容性要求

2. **理解架构**：

   - 分析目录结构与模块组织
   - 识别清晰的分层边界与组件关系
   - 记录组件间通信模式

3. **记录代码模式**：

   - 整理不同代码要素的命名约定
   - 记录文档风格与完整度
   - 记录错误处理模式
   - 映射测试方法与覆盖

4. **质量标准**：
   - 识别实际使用的性能优化技术
   - 记录已实现的安全实践
   - 如适用，记录可访问性特性
   - 记录代码库中体现的质量模式

### 3. 实施说明

最终的 copilot-instructions.md 应：

- 放置在 .github/copilot 目录
- 仅引用代码库中存在的模式与标准
- 明确包含版本兼容性要求
- 避免规定代码库中不存在的做法
- 提供来自代码库的具体示例
- 在保证全面性的同时保持简明

重要：仅基于在代码库中实际观察到的模式给出指引。明确要求 Copilot 将与现有代码的一致性置于外部最佳实践或更新语言特性之上。
"

## 预期输出

一份全面的 copilot-instructions.md，将指导 GitHub Copilot 生成与既有技术版本完全兼容、并遵循既定模式与架构的代码。
