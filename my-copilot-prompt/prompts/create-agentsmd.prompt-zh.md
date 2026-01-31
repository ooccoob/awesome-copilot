---
描述：“提示为存储库生成 AGENTS.md 文件”
代理人：“代理人”
---

# 创建高质量的 AGENTS.md 文件

您是代码代理。您的任务是在此存储库的根目录下创建一个完整、准确的 AGENTS.md，遵循 https://agents.md/ 上的公共指导。

AGENTS.md 是一种开放格式，旨在为编码代理提供他们在项目中有效工作所需的上下文和说明。

## 什么是 AGENTS.md？

AGENTS.md 是一个 Markdown 文件，充当“代理自述文件”——一个专用的、可预测的位置，用于提供上下文和说明，以帮助 AI 编码代理在您的项目上工作。它通过包含编码代理所需的详细技术上下文来补充 README.md，但可能会使以人为本的 README 变得混乱。

## 关键原则

- **以代理为中心**：包含自动化工具的详细技术说明
- **补充 README.md**：不取代人工文档，但添加特定于代理的上下文
- **标准化位置**：放置在存储库根目录（或 monorepos 的子项目根目录）
- **开放格式**：使用标准 Markdown，结构灵活
- **生态系统兼容性**：适用于 20 多种不同的 AI 编码工具和代理

## 文件结构和内容指南

### 1. 所需设置

- 在存储库根目录中创建文件作为 `AGENTS.md`
- 使用标准 Markdown 格式
- 无必填字段 - 根据项目需求灵活的结构

### 2. 包含的基本部分

#### 项目概况

- 简要描述该项目的用途
- 架构概述（如果复杂）
- 使用的关键技术和框架

#### 设置命令

- 安装说明
- 环境设置步骤
- 依赖管理命令
- 数据库设置（如果适用）

#### 开发流程

- 如何启动开发服务器
- 构建命令
- 手表/热重载设置
- 包管理器细节（npm、pnpm、yarn 等）

#### 测试说明

- 如何运行测试（单元、集成、e2e）
- 测试文件位置和命名约定
- 覆盖范围要求
- 使用的特定测试模式或框架
- 如何运行测试子集或专注于特定领域

#### 代码风格指南

- 特定于语言的约定
- 语法检查和格式化规则
- 文件组织模式
- 命名约定
- 导入/导出模式

#### 构建和部署

- 构建命令和输出
- 环境配置
- 部署步骤和要求
- CI/CD 管道信息

### 3. 可选但推荐的部分

#### 安全考虑

- 安全测试要求
- 保密管理
- 身份验证模式
- 权限模型

#### Monorepo 说明（如果适用）

- 如何使用多个包
- 跨包依赖
- 选择性构建/测试
- 特定于包的命令

#### 拉取请求指南

- 标题格式要求
- 提交前需要进行的检查
- 审核流程
- 提交消息约定

#### 调试和故障排除

- 常见问题及解决方案
- 记录模式
- 调试配置
- 性能考虑

## 示例模板

使用此作为起始模板并根据特定项目进行自定义：

```markdown
# AGENTS.md

## Project Overview

[Brief description of the project, its purpose, and key technologies]

## Setup Commands

- Install dependencies: `[package manager] install`
- Start development server: `[command]`
- Build for production: `[command]`

## Development Workflow

- [Development server startup instructions]
- [Hot reload/watch mode information]
- [Environment variable setup]

## Testing Instructions

- Run all tests: `[command]`
- Run unit tests: `[command]`
- Run integration tests: `[command]`
- Test coverage: `[command]`
- [Specific testing patterns or requirements]

## Code Style

- [Language and framework conventions]
- [Linting rules and commands]
- [Formatting requirements]
- [File organization patterns]

## Build and Deployment

- [Build process details]
- [Output directories]
- [Environment-specific builds]
- [Deployment commands]

## Pull Request Guidelines

- Title format: [component] Brief description
- Required checks: `[lint command]`, `[test command]`
- [Review requirements]

## Additional Notes

- [Any project-specific context]
- [Common gotchas or troubleshooting tips]
- [Performance considerations]
```

## 来自 Agents.md 的工作示例

这是来自 Agents.md 网站的真实示例：

```markdown
# Sample AGENTS.md file

## Dev environment tips

- Use `pnpm dlx turbo run where <project_name>` to jump to a package instead of scanning with `ls`.
- Run `pnpm install --filter <project_name>` to add the package to your workspace so Vite, ESLint, and TypeScript can see it.
- Use `pnpm create vite@latest <project_name> -- --template react-ts` to spin up a new React + Vite package with TypeScript checks ready.
- Check the name field inside each package's package.json to confirm the right name—skip the top-level one.

## Testing instructions

- Find the CI plan in the .github/workflows folder.
- Run `pnpm turbo run test --filter <project_name>` to run every check defined for that package.
- From the package root you can just call `pnpm test`. The commit should pass all tests before you merge.
- To focus on one step, add the Vitest pattern: `pnpm vitest run -t "<test name>"`.
- Fix any test or type errors until the whole suite is green.
- After moving files or changing imports, run `pnpm lint --filter <project_name>` to be sure ESLint and TypeScript rules still pass.
- Add or update tests for the code you change, even if nobody asked.

## PR instructions

- Title format: [<project_name>] <Title>
- Always run `pnpm lint` and `pnpm test` before committing.
```

## 实施步骤

1. **分析项目结构**了解：

   - 使用的编程语言和框架
   - 包管理器和构建工具
   - 测试框架
   - 项目架构（monorepo、单包等）

2. **通过检查确定关键工作流程**：

   - package.json 脚本
   - Makefile 或其他构建文件
   - CI/CD 配置文件
   - 文档文件

3. **创建全面的部分**涵盖：

   - 所有必要的设置和开发命令
   - 测试策略和命令
   - 代码风格和约定
   - 构建和部署流程

4. **包括代理可以直接执行的具体的、可操作的命令**

5. **通过确保所有命令按文档说明工作来测试说明**

6. **重点关注**代理商需要了解的内容，而不是一般项目信息

## 最佳实践

- **具体**：包括准确的命令，而不是模糊的描述
- **使用代码块**：为了清晰起见，将命令用反引号括起来
- **包括上下文**：解释为什么需要某些步骤
- **保持最新**：随着项目的发展而更新
- **测试命令**：确保所有列出的命令确实有效
- **考虑嵌套文件**：对于 monorepos，根据需要在子项目中创建 AGENTS.md 文件

## Monorepo注意事项

对于大型单一仓库：

- 将主 AGENTS.md 放置在存储库根目录中
- 在子项目目录中创建附加 AGENTS.md 文件
- 对于任何给定位置，最近的 AGENTS.md 文件优先
- 包括包/项目之间的导航提示

## 最后的注释

- AGENTS.md 可与 20 多种 AI 编码工具配合使用，包括 Cursor、Aider、Gemini CLI 等
- 格式有意灵活 - 根据您的项目需求进行调整
- 专注于可操作的说明，帮助代理理解并使用您的代码库
- 这是动态文档 - 随着项目的发展进行更新

创建 AGENTS.md 文件时，请优先考虑清晰度、完整性和可操作性。目标是为任何编码代理提供足够的背景信息，以便有效地为项目做出贡献，而无需额外的人工指导。
