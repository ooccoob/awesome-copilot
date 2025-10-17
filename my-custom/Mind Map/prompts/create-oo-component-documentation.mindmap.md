## 文档综述（What/When/Why/How）

- What：为面向对象组件生成标准化技术文档（C4/arc42/IEEE1016 对齐）

- When：需要面向开发/维护者沉淀组件职责、架构、接口、实现与质量属性时

- Why：统一模板与命名，支持自动化解析、可视化与检索

- How：分析组件路径→输出含 Front matter/概览/架构/接口表/实现/示例/质量/参考的 Markdown，保存 /docs/components/

## 示例提问（Examples）

- “为 src/core/auth 组件生成文档，补充 Mermaid 结构与依赖图”

- “提取公共 API 表，含参数/返回/用法说明”

## 结构化要点（CN/EN）

- 标准/Standards：C4/arc42/IEEE1016

- 分节/Sections：Overview/Architecture/Interfaces/Implementation/Usage/Quality/Refs

- 图示/Diagrams：Mermaid（class/graph）

- 细节/Details：异常/配置/性能/可扩展性

## 中文思维导图

- 组件分析
  - 结构/继承
  - 模式/依赖
- 文档结构
  - Front matter
  - API 表格
- 可视化
  - Mermaid 图
- 质量属性
  - 安全/性能/可靠/可维护

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\create-oo-component-documentation.prompt.md

- 生成时间：2025-10-17
