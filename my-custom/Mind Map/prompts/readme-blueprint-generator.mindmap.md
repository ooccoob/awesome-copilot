## README Blueprint Generator — Mind Map

### What
- 从 .github/copilot 与 copilot-instructions.md 提炼信息，自动生成结构化 README。

### When
- 新仓库初始化或文档缺失/不一致时；版本大升级后需要统一口径时。

### Why
- 降低上手门槛，统一技术栈、结构、规范与流程说明；减少文档漂移。

### How
- 扫描目录与说明文件→抽取要点→拼装模块化章节→交叉引用与示例代码块→输出 Markdown。

### Key Points (中/英)
- 技术栈/Technology Stack
- 架构/Architecture
- 目录结构/Project Structure
- 开发流程/Workflow
- 编码规范/Coding Standards
- 测试/Testing
- 贡献指南/Contributing
- 许可证/License

### Compact map
- Inputs: .github/copilot/*, copilot-instructions.md
- Sections: Name+Desc → Stack → Architecture → Getting Started → Structure → Features → Workflow → Standards → Testing → Contributing → License
- Output: README.md (Markdown, 交叉链接, 代码块, 列表)
- Constraints: 简洁、可读、面向开发者

### Example Questions (≥10)
- 我们的技术栈与版本如何从文档自动抽取并列出？
- 架构章节应包含哪些关键图示或文字要点？
- Getting Started 需要哪些最小可行步骤与前置条件？
- 目录结构如何从现有仓库推断并结合说明文件？
- Coding Standards 应从哪里汇总并压缩到 10 条以内？
- 测试部分如何说明框架、命令与覆盖率位置？
- Contributing 需要包含哪些提交规范与分支策略？
- 如何在 README 中插入指向其他说明文件的交叉链接？
- 如何保持 README 与源码/脚本变化的同步（减少漂移）？
- 生成的 README 如何控制长度与层级，保证可读性？

---
- Source: d:\mycode\awesome-copilot\prompts\readme-blueprint-generator.prompt.md
- Generated: 2025-10-17
