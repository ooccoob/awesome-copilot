## 文档综述（What/When/Why/How）

- What：为规格中尚未实现的需求逐条创建 GitHub Issues 的提示词（feature_request.yml）

- When：规格完整而实现不完整，需要逐需求建档并校验未实现状态时

- Why：确保规格→实现→工作项的端到端追踪，减少遗漏

- How：解析规格→校验实现状态→检索去重→按未实现需求创建 Issue（标题含需求 ID/摘要，含实施建议/验收标准）

## 示例提问（Examples）

- “扫描 /spec/xxx.md，列出未实现的需求并逐条创建 Issue，附带验收标准”

- “与代码库/相关规格交叉验证避免重复或已部分实现”

- “统一使用 feature 标签并补充上下文链接”

## 结构化要点（CN/EN）

- 需求/Requirements：从规格提取 | Extract from spec

- 校验/Check：代码/其他规格对比 | Implementation status

- 去重/Dedup：search_issues | Avoid duplicates

- 内容/Content：ID/描述/建议/验收 | ID, desc, guidance, AC

- 约束/Scope：仅未实现项，一项一 Issue | One per unmet

## 中文思维导图

- 规格解析
  - 需求识别
- 实现核验
  - 代码模式检索
  - 关联规格比对
- Issue 生成
  - 标题含 ID
  - 描述/建议/AC
- 去重合并
  - 更新已有

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\create-github-issues-for-unmet-specification-requirements.prompt.md

- 生成时间：2025-10-17
