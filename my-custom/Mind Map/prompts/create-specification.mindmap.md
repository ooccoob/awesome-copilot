## 文档综述（What/When/Why/How）

- What：生成面向 AI 的规范文档（requirements/constraints/interfaces/AC/测试/依赖）

- When：需要创建自包含、可解析、无歧义的规格时

- Why：让生成式 AI 与人类按照同一标准理解与实现，提升协作效率

- How：严格模板（Front matter→目的/定义→需求与约束→接口与契约→AC→测试→依赖→示例→校验→相关文档），保存 /spec/

## 示例提问（Examples）

- “为‘架构流程规范’生成 spec-architecture-*.md，补充 AC 与测试策略”

- “区分 REQ/CON/GUD/PAT 并列出接口契约与示例”

## 结构化要点（CN/EN）

- 语言/Language：明确/无歧义 | Precise & explicit

- 契约/Contracts：接口/数据/示例 | APIs & schemas

- 验收/Acceptance：Given-When-Then

- 测试/Testing：层级/框架/覆盖

## 中文思维导图

- 结构分节
  - Purpose & Scope
  - Definitions
  - Requirements
- 合同/接口
  - Schema/示例
- 验收标准
  - AC 列表
- 测试策略
  - 自动化与 CI

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\create-specification.prompt.md

- 生成时间：2025-10-17
