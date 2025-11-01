## 文档综述（What/When/Why/How）

- What：基于实现计划（按阶段/Phase）批量创建 GitHub Issues 的提示词（feature/chore 模板）

- When：实施计划已拆分阶段，需要一阶段一 Issue 并消除重复时

- Why：将计划落地到可执行工作项，保持粒度清晰与模板一致

- How：解析 plan→识别阶段→检索去重→按阶段创建/更新 Issue（标题/描述/标签），仅限计划要求

## 示例提问（Examples）

- “为 implementation-plan.md 的各阶段创建对应 Issue，并补充验收标准”

- “使用 feature 或 chore 模板按类型打标签，保持命名规范”

- “避免重复创建，发现同名则更新内容”

## 结构化要点（CN/EN）

- 输入/Input：实现计划文件 | Implementation plan

- 拆分/Split：Phase→Issue | One per phase

- 模板/Templates：feature_request.yml / chore_request.yml | Typed

- 去重/Dedup：search_issues 先查 | Avoid duplicates

- 内容/Content：标题/描述/标签/验收标准 | Structured

## 中文思维导图

- 计划解析
  - 阶段识别
  - 依赖关系
- Issue 生成
  - 模板选择
  - 命名规范
- 去重与更新
  - 搜索合并
- 合规校验
  - 仅限计划范围

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\create-github-issues-feature-from-implementation-plan.prompt.md

- 生成时间：2025-10-17
