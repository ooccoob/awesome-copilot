## 文档综述（What/When/Why/How）

- What：为既有 GitHub Actions 工作流生成“行为规范”文档的提示词（与实现解耦）

- When：需抽象工作流的目标、触发、作业依赖、约束、质量门禁与监控以便维护与评审时

- Why：语义清晰、结构化、AI 友好，便于变更/审计/对齐团队认知

- How：解析 yml→提取目的/触发/作业图/输入输出/资源限制/权限/错误处理/门禁/监控→保存到 /spec/

## 示例提问（Examples）

- “为 ci.yml 生成规范，包含 Mermaid 作业依赖图与需求矩阵/错误恢复策略”

- “梳理输入/输出契约与 Secrets/Variables 表格，并列出并发/超时/权限”

- “补充变更管理流程与版本历史模板”

## 结构化要点（CN/EN）

- 目标/Purpose：业务目标与触发 | Triggers & goals

- 流程/Flow：作业与依赖图 | Jobs & dependencies

- 契约/Contracts：Inputs/Outputs/Secrets/Vars | I/O tables

- 约束/Constraints：超时/并发/权限/Runner | Runtime limits

- 质量/Quality：Gates/监控/告警 | Quality gates & metrics

## 中文思维导图

- 工作流概览
  - 目的与触发
  - 目标环境
- 执行流程
  - Mermaid 图
  - 作业矩阵
- 契约清单
  - 输入/输出
  - Secrets/Vars
- 执行约束
  - 超时/并发/权限
- 错误与门禁
  - 恢复策略
  - 质量门禁

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\create-github-action-workflow-specification.prompt.md

- 生成时间：2025-10-17
