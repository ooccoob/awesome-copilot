## 文档综述（What/When/Why/How）

- What：基于给定规格文件，创建单个功能类 GitHub Issue 的提示词（使用 feature_request.yml 模板）

- When：存在独立的功能规格，需要以一条 Issue 覆盖全部变更并避免重复时

- Why：将需求从规格同步到工作项，确保追踪性与模板合规

- How：解析规格→搜索重复→使用模板创建/更新 Issue（标题/描述/标签），仅包含规格要求的变更

## 示例提问（Examples）

- “为 /spec/feature-x.md 创建功能 Issue，若存在同名则更新并补充上下文/受影响范围”

- “根据模板生成问题描述：问题背景/拟议方案/上下文链接”

- “自动打上 feature/enhancement 标签”

## 结构化要点（CN/EN）

- 输入/Input：规格文件路径 | Spec file path

- 去重/Dedupe：search_issues 检查现有 | Avoid duplicates

- 模板/Template：feature_request.yml | Template-first

- 内容/Content：标题/描述/标签 | Title/Body/Labels

- 约束/Constraint：单 Issue 覆盖完整规格 | Single issue per spec

## 中文思维导图

- 规格解析
  - 需求提取
  - 影响范围
- 去重策略
  - 搜索现有
  - 更新合并
- Issue 生成
  - 模板套用
  - 标题/描述/标签
- 验证
  - 仅规格范围

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\create-github-issue-feature-from-specification.prompt.md

- 生成时间：2025-10-17
