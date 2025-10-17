## 文档综述（What/When/Why/How）

- What：生成 AI/人可执行、确定性的实施计划（多阶段、可并行、可验收）

- When：为功能/重构/升级/数据/架构/流程等创建计划文件时

- Why：让计划可被代理解析并自动执行，最小歧义、可验证、可追踪

- How：采用严格模板（Front matter + 阶段/任务表 + 依赖/风险/测试），标识 REQ/TASK/DEP/AC 等编码并保存到 /plan/

## 示例提问（Examples）

- “为认证模块重构生成实施计划，含分阶段任务表与验收标准”

- “补充依赖/风险与自动校验规则，命名为 feature-auth-module-1.md”

## 结构化要点（CN/EN）

- 原则/Principles：零歧义、可解析 | Deterministic & parseable

- 阶段/Phases：原子化、可并行 | Atomic, parallelizable

- 任务/Tasks：精确到路径/函数/变更 | Concrete details

- 校验/Validation：标注 AC 与验证方式 | Auto-verifiable

- 命名/Naming：purpose-component-version.md

## 中文思维导图

- 模板结构
  - Front matter
  - Requirements
  - Phases & Tasks
- 依赖与风险
  - DEP 列表
  - RISK/ASSUMPTION
- 测试策略
  - 等级/框架
  - 覆盖率
- 验收标准
  - Given-When-Then

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\create-implementation-plan.prompt.md

- 生成时间：2025-10-17
