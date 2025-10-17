## 文档综述（What/When/Why/How）

- What：生成 copilot-instructions.md 的蓝图提示词，指导 Copilot 严格遵循项目真实版本与既有模式

- When：需要集中化约束 Copilot 产出与项目架构/质量/测试/文档/版本策略一致时

- Why：避免“想当然”与越权新特性，确保与代码库现状兼容并维持一致性

- How：先扫描版本/架构/模式/质量标准，再输出固定结构说明（优先级、版本检测、上下文文件、扫描指引、质量/测试/技术栈规则等）

## 示例提问（Examples）

- “基于当前仓库生成 copilot-instructions.md，列出已用语言/框架/库的精确版本与限制”

- “按架构风格与代码库模式给出命名/日志/错误处理/测试等一致性约束”

- “补充技术栈专项规则（.NET/Java/JS/React/Angular/Python）与版本化策略”

## 结构化要点（CN/EN）

- 版本/Versions：语言/框架/库精确版本 | Exact versions only

- 上下文/Context：.github/copilot/* 优先 | Prioritize context files

- 扫描/Scan：相似文件→命名/日志/错误/文档/测试模式 | Derive patterns

- 质量/Quality：可维护/性能/安全/可及/可测 | Focus per config

- 测试/Testing：Unit/Integration/E2E/TDD/BDD 一致

## 中文思维导图

- 版本检测
  - 语言/框架/库
  - 约束与禁用项
- 架构一致
  - 边界与依赖倒置
  - 模式与组织
- 代码质量
  - 命名/日志/异常
  - 性能/安全/可及
- 测试策略
  - 层级与风格
  - mock/断言
- 版本化
  - 语义/日历/自定义

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\copilot-instructions-blueprint-generator.prompt.md

- 生成时间：2025-10-17
