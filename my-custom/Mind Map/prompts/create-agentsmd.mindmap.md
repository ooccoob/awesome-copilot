## 文档综述（What/When/Why/How）

- What：依据 agents.md 公共指南为仓库生成高质量 AGENTS.md 的提示词

- When：希望为 AI 代码代理提供“面向代理的 README”，集中给出可执行上下文与流程时

- Why：统一位置/结构/命令，提升代理在项目中的自洽性与效率

- How：分析项目结构/脚本/CI/文档→编写 AGENTS.md（概览、安装、开发/测试/构建/部署、代码风格、PR 指南、疑难排查）

## 示例提问（Examples）

- “解析 package.json/Makefile/CI，生成可直接执行的开发/测试/构建命令清单”

- “为 monorepo 给出子项目导航与过滤执行指引”

- “补充常见问题、日志与调试方式”

## 结构化要点（CN/EN）

- 位置/Location：仓库根或子项目根 | Repo root or subproject

- 章节/Sections：概览/安装/开发/测试/风格/构建/部署/PR/排障 | Standard sections

- 可执行/Actionable：具体命令与上下文 | Concrete commands

- Monorepo：就近覆盖与导航技巧 | Proximity precedence

- 维护/Maintain：随项目演进更新 | Keep current

## 中文思维导图

- 项目分析
  - 语言/包管理/脚本
  - CI/CD 与文档
- 指令整理
  - 安装/启动
  - 构建/打包
- 测试规范
  - 位置/命名/覆盖
- 风格约定
  - Lint/Format
- PR 指南
  - 检查/流程

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\create-agentsmd.prompt.md

- 生成时间：2025-10-17
