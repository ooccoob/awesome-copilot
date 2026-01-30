## 文档综述（What/When/Why/How）

- What：生成 code exemplars 蓝图提示词，用于扫描代码库并产出 exemplars.md 的高质量示例清单

- When：需要归纳项目内最佳实践样例、沉淀编码规范与模式，并指导后续一致性开发时

- Why：以真实文件为准，按技术栈/层次/类别组织代表性样例，避免臆造，提升团队一致性与可复用性

- How：参数化设置项目类型/扫描深度/分类方式/是否包含片段，输出结构化 exemplars.md（不引用不存在的文件）

## 示例提问（Examples）

- “自动检测技术栈并生成分层（展示/业务/数据/横切）示例，每类不超过 3 个，附简要说明”

- “按架构层与文件类型分类，列出最具代表性的模式与实现，并补充反模式需避免项”

- “以前端(React/TS)为主，输出组件/状态/路由/表单/测试的最佳样例索引”

## 结构化要点（CN/EN）

- 识别/Detect：技术栈与框架 | Auto-detect primary languages & frameworks

- 标准/Criteria：可读性、文档、错误处理、设计原则、单一职责 | Readability, docs, error handling, design principles

- 分类/Categories：模式类型/架构层/文件类型 | Pattern/Layer/File Type

- 产出/Output：路径、说明、要点、可选片段 | Path, description, key details, optional snippet

- 约束/Constraint：仅引用真实存在文件，禁止臆造 | Only real files, no hypothetical

## 中文思维导图

- 扫描与识别
  - 自动识别语言/框架
  - 查找高质量实现
- 评估标准
  - 命名/结构/文档
  - 错误处理/设计原则
- 分类组织
  - 架构层/模式/文件类型
  - 每类上限数量
- 文档输出
  - exemplars.md 结构
  - 真实路径与要点
- 附加说明
  - 一致性观察
  - 反模式提示

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\code-exemplars-blueprint-generator.prompt.md

- 生成时间：2025-10-17
