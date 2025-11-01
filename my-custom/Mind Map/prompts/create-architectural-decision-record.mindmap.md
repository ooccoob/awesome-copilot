## 文档综述（What/When/Why/How）

- What：创建 ADR（架构决策记录）的提示词，面向 AI/Human 可读的标准化文档

- When：需要记录重要技术/架构决策（含备选与取舍、正负后果）并供后续追踪时

- Why：一致的前置条件/模板/命名与顺序编号，利于检索与自动化处理

- How：校验输入（标题/上下文/决策/备选/干系人）→ 采用固定 front matter 与分节，编码化要点（POS/NEG/ALT/IMP/REF）

## 示例提问（Examples）

- “以‘数据库选型’为题创建 ADR，包含两种备选、选用理由与风险”

- “按 /docs/adr/adr-NNNN-*.md 规则生成下一个编号并保存”

- “补充实施要点/迁移策略/成功标准”

## 结构化要点（CN/EN）

- 模板/Template：Front matter + 标准分节 | Standard ADR sections

- 编码/Codes：POS/NEG/ALT/IMP/REF 前缀编号 | Coded bullets

- 命名/Naming：adr-NNNN-title-slug.md | Sequential numbering

- 状态/Status：Proposed/Accepted/Rejected 等 | Lifecycle

- 位置/Location：/docs/adr/ | Repository docs

## 中文思维导图

- 输入校验
  - 标题/上下文
  - 决策/备选/干系人
- 文档结构
  - Front matter
  - 正负后果
- 备选方案
  - 描述/拒绝原因
- 实施说明
  - 迁移/监控
- 关联引用
  - 相关 ADR/外部文档

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\create-architectural-decision-record.prompt.md

- 生成时间：2025-10-17
