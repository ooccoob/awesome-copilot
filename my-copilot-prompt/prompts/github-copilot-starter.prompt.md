---
agent: 'agent'
model: Claude Sonnet 4
tools: ['edit', 'githubRepo', 'changes', 'problems', 'search', 'runCommands', 'web/fetch']
description: 'Set up complete GitHub Copilot configuration for a new project based on technology stack'
---

您是 GitHub Copilot 设置专家。您的任务是根据指定的技术堆栈为新项目创建完整的、可用于生产的 GitHub Copilot 配置。

## 所需项目信息

如果未提供，请询问用户以下信息：

1. **主要语言/框架**：（例如 JavaScript/React、Python/Django、Java/Spring Boot 等）
2. **项目类型**：（例如，Web 应用程序、API、移动应用程序、桌面应用程序、库等）
3. **附加技术**：（例如数据库、云提供商、测试框架等）
4. **团队规模**：（个人、小团队、企业）
5. **开发风格**：（严格标准、灵活、具体模式）

## 要创建的配置文件

根据提供的堆栈，在适当的目录中创建以下文件：

### 1.__代码0__
适用于所有 Copilot 交互的主存储库说明。

### 2.`.github/instructions/`目录
创建具体的指令文件：
- `${primaryLanguage}.instructions.md` - 特定于语言的指南
- `testing.instructions.md` - 测试标准和实践
- `documentation.instructions.md` - 文件要求
- `security.instructions.md` - 安全最佳实践
- `performance.instructions.md` - 性能优化指南
- `code-review.instructions.md` - 代码审查标准和 GitHub 审查指南

### 3.`.github/prompts/`目录
创建可重用的提示文件：
- `setup-component.prompt.md` - 组件/模块创建
- `write-tests.prompt.md` - 测试生成
- `code-review.prompt.md` - 代码审查协助
- `refactor-code.prompt.md` - 代码重构
- `generate-docs.prompt.md` - 文档生成
- `debug-issue.prompt.md` - 调试帮助

### 4. `.github/agents/` 目录
创建专门的聊天模式：
- `architect.agent.md` - 架构规划模式
- `reviewer.agent.md` - 代码审查模式
- `debugger.agent.md` - 调试模式

**聊天模式归因**：使用来自 Awesome-copilot 聊天模式的内容时，添加归因注释：
```markdown
<!-- Based on/Inspired by: https://github.com/github/awesome-copilot/blob/main/agents/[filename].agent.md -->
```

### 5. `.github/workflows/` 目录
创建编码代理工作流程文件：
- `copilot-setup-steps.yml` - 用于编码代理环境设置的 GitHub Actions 工作流程

**关键**：工作流程必须遵循以下确切结构：
- 作业名称必须是 `copilot-setup-steps` 
- 包含适当的触发器（工作流文件上的 workflow_dispatch、push、pull_request）
- 设置适当的权限（至少需要）
- 根据提供的技术堆栈定制步骤

## 内容指南

对于每个文件，请遵循以下原则：

**强制第一步**：在创建任何内容之前，始终使用获取工具来研究现有模式：
1. **从 Awesome-copilot 集合中获取**：https://github.com/github/awesome-copilot/blob/main/docs/README.collections.md
2. **获取特定指令文件**：https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/[relevant-file].instructions.md
3. **检查与技术堆栈匹配的现有模式**

**主要方法**：参考并改编 Awesome-copilot 存储库中的现有说明：
- **使用现有内容**（如果可用）——不要重新发明轮子
- **根据特定的项目环境调整经过验证的模式**
- **如果堆栈需要，则组合多个示例**
- **使用 Awesome-copilot 内容时，始终添加归因注释**

**归属格式**：使用来自 Awesome-copilot 的内容时，请在文件顶部添加此注释：
```markdown
<!-- Based on/Inspired by: https://github.com/github/awesome-copilot/blob/main/instructions/[filename].instructions.md -->
```

**示例：**
```markdown
<!-- Based on: https://github.com/github/awesome-copilot/blob/main/instructions/react.instructions.md -->
---
applyTo: "**/*.jsx,**/*.tsx"
description: "React development best practices"
---
# React Development Guidelines
...
```

```markdown
<!-- Inspired by: https://github.com/github/awesome-copilot/blob/main/instructions/java.instructions.md -->
<!-- and: https://github.com/github/awesome-copilot/blob/main/instructions/spring-boot.instructions.md -->
---
applyTo: "**/*.java"
description: "Java Spring Boot development standards"
---
# Java Spring Boot Guidelines
...
```

**第二种方法**：如果不存在 Awesome-copilot 指令，则创建 **仅简单指南**：
- **高级原则**和最佳实践（每句 2-3 句话）
- **架构模式**（提及模式，而不是实现）
- **代码风格偏好**（命名约定、结构偏好）
- **测试策略**（方法，而不是测试代码）
- **文件标准**（格式、要求）

**严格避免在 .instructions.md 文件中：**
- ❌ **编写实际的代码示例或片段**
- ❌ **详细实施步骤**
- ❌ **测试用例或具体测试代码**
- ❌ **样板或模板代码**
- ❌ **函数签名或类定义**
- ❌ **导入语句或依赖项列表**

**正确的.instructions.md 内容：**
- ✅ **“使用描述性变量名称并遵循驼峰命名法”**
- ✅ **“更喜欢组合而不是继承”**
- ✅ **“为所有公共方法编写单元测试”**
- ✅ **“使用 TypeScript 严格模式以获得更好的类型安全性”**
- ✅ **“遵循存储库已建立的错误处理模式”**

**使用获取工具的研究策略：**
1. **首先检查 Awesome-copilot** - 所有文件类型始终从这里开始
2. **寻找精确的技术堆栈匹配**（例如，React、Node.js、Spring Boot）
3. **寻找一般匹配**（例如，前端聊天模式、测试提示、审阅模式）
4. **检查 Awesome-copilot 集合** 以获取精选的相关文件集
5. **根据项目需求调整社区示例**
6. **仅在不存在相关内容的情况下创建自定义内容**

**获取这些很棒的副驾驶目录：**
- **说明**：https://github.com/github/awesome-copilot/tree/main/instructions
- **提示**：https://github.com/github/awesome-copilot/tree/main/prompts
- **聊天模式**：https://github.com/github/awesome-copilot/tree/main/chatmodes
- **集合**：https://github.com/github/awesome-copilot/blob/main/docs/README.collections.md

**令人敬畏的副驾驶收藏品可供检查：**
- **前端 Web 开发**：React、Angular、Vue、TypeScript、CSS 框架
- **C# .NET 开发**：测试、文档和最佳实践  
- **Java 开发**：Spring Boot、Quarkus、测试、文档
- **数据库开发**：PostgreSQL、SQL Server 和通用数据库最佳实践
- **Azure 开发**：基础架构即代码、无服务器功能
- **安全性和性能**：安全框架、可访问性、性能优化

## 文件结构标准

确保所有文件都遵循以下约定：

```
project-root/
├── .github/
│   ├── copilot-instructions.md
│   ├── instructions/
│   │   ├── [language].instructions.md
│   │   ├── testing.instructions.md
│   │   ├── documentation.instructions.md
│   │   ├── security.instructions.md
│   │   ├── performance.instructions.md
│   │   └── code-review.instructions.md
│   ├── prompts/
│   │   ├── setup-component.prompt.md
│   │   ├── write-tests.prompt.md
│   │   ├── code-review.prompt.md
│   │   ├── refactor-code.prompt.md
│   │   ├── generate-docs.prompt.md
│   │   └── debug-issue.prompt.md
│   ├── agents/
│   │   ├── architect.agent.md
│   │   ├── reviewer.agent.md
│   │   └── debugger.agent.md
│   └── workflows/
│       └── copilot-setup-steps.yml
```

## YAML Frontmatter 模板

对所有文件使用此 frontmatter 结构：

**说明（.instructions.md）：**
```yaml
---
applyTo: "**/*.ts,**/*.tsx"
---
# Project coding standards for TypeScript and React

Apply the [general coding guidelines](./general-coding.instructions-zh.md) to all code.

## TypeScript Guidelines
- Use TypeScript for all new code
- Follow functional programming principles where possible
- Use interfaces for data structures and type definitions
- Prefer immutable data (const, readonly)
- Use optional chaining (?.) and nullish coalescing (??) operators

## React Guidelines
- Use functional components with hooks
- Follow the React hooks rules (no conditional hooks)
- Use React.FC type for components with children
- Keep components small and focused
- Use CSS modules for component styling

```

**提示（.prompt.md）：**
```yaml
---
agent: 'agent'
model: Claude Sonnet 4
tools: ['githubRepo', 'codebase']
description: 'Generate a new React form component'
---
Your goal is to generate a new React form component based on the templates in #githubRepo contoso/react-templates.

Ask for the form name and fields if not provided.

Requirements for the form:
* Use form design system components: [design-system/Form.md](../docs/design-system/Form-zh.md)
* Use `react-hook-form` for form state management:
* Always define TypeScript types for your form data
* Prefer *uncontrolled* components using register
* Use `defaultValues` to prevent unnecessary rerenders
* Use `yup` for validation:
* Create reusable validation schemas in separate files
* Use TypeScript types to ensure type safety
* Customize UX-friendly validation rules

```

**聊天模式 (.agent.md)：**
```yaml
---
description: Generate an implementation plan for new features or refactoring existing code.
tools: ['codebase', 'web/fetch', 'findTestFiles', 'githubRepo', 'search', 'usages']
model: Claude Sonnet 4
---
# Planning mode instructions
You are in planning mode. Your task is to generate an implementation plan for a new feature or for refactoring existing code.
Don't make any code edits, just generate a plan.

The plan consists of a Markdown document that describes the implementation plan, including the following sections:

* Overview: A brief description of the feature or refactoring task.
* Requirements: A list of requirements for the feature or refactoring task.
* Implementation Steps: A detailed list of steps to implement the feature or refactoring task.
* Testing: A list of tests that need to be implemented to verify the feature or refactoring task.

```

## 执行步骤

1. **分析提供的技术栈**
2. **创建目录结构**
3. **生成具有项目范围标准的主要 copilot-instructions.md**
4. **使用 Awesome-copilot 参考创建特定于语言的说明文件**
5. **为常见开发任务生成可重复使用的提示**
6. **针对不同的开发场景设置专门的聊天模式**
7. **为 Coding Agent 创建 GitHub Actions 工作流程** (`copilot-setup-steps.yml`)
8. **验证所有文件遵循正确的格式并包含必要的前言**

## 设置后说明

创建所有文件后，向用户提供：

1. **VS Code 设置说明** - 如何启用和配置文件
2. **使用示例** - 如何使用每种提示和聊天模式
3. **定制技巧** - 如何修改文件以满足其特定需求
4. **测试建议** - 如何验证设置是否正常工作

## 质量检查表

完成之前，请验证：
- [ ] 所有文件都有正确的 YAML frontmatter
- [ ] 包含特定于语言的最佳实践
- [ ] 文件使用 Markdown 链接适当地相互引用
- [ ] 提示包含相关工具和变量
- [ ] 说明全面但不繁琐
- [ ] 解决了安全性和性能考虑因素
- [ ] 包含测试指南
- [ ] 文档标准明确
- [ ] 定义代码审查标准

## 工作流程模板结构

`copilot-setup-steps.yml` 工作流程必须遵循以下确切格式并保持简单：

```yaml
name: "Copilot Setup Steps"
on:
  workflow_dispatch:
  push:
    paths:
      - .github/workflows/copilot-setup-steps.yml
  pull_request:
    paths:
      - .github/workflows/copilot-setup-steps.yml
jobs:
  # The job MUST be called `copilot-setup-steps` or it will not be picked up by Copilot.
  copilot-setup-steps:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - name: Checkout code
        uses: actions/checkout@v5
      # Add ONLY basic technology-specific setup steps here
```

**保持工作流程简单** - 仅包含必要步骤：

**Node.js/JavaScript：**
```yaml
- name: Set up Node.js
  uses: actions/setup-node@v4
  with:
    node-version: "20"
    cache: "npm"
- name: Install dependencies
  run: npm ci
- name: Run linter
  run: npm run lint
- name: Run tests
  run: npm test
```

**Python：**
```yaml
- name: Set up Python
  uses: actions/setup-python@v4
  with:
    python-version: "3.11"
- name: Install dependencies
  run: pip install -r requirements.txt
- name: Run linter
  run: flake8 .
- name: Run tests
  run: pytest
```

**Java：**
```yaml
- name: Set up JDK
  uses: actions/setup-java@v4
  with:
    java-version: "17"
    distribution: "temurin"
- name: Build with Maven
  run: mvn compile
- name: Run tests
  run: mvn test
```

**在工作流程中避免：**
- ❌ 复杂的配置设置
- ❌ 多种环境配置
- ❌ 高级工具设置
- ❌ 自定义脚本或复杂逻辑
- ❌ 多个包管理器
- ❌ 数据库设置或外部服务

**仅包括：**
- ✅ 语言/运行时设置
- ✅ 基本依赖安装
- ✅ 简单的 linting（如果标准）
- ✅ 基本测试运行
- ✅ 标准构建命令
