## 文档综述（What/When/Why/How）

- What：.editorconfig 生成专家（项目分析→规则生成→逐条说明），含用户偏好与最佳实践

- When：需要统一多语言/多 IDE 的代码风格时

- Why：减少风格差异与无谓 diff，提升协作一致性

- How：分析项目文件类型→生成覆盖性规则→两部分输出（配置 + 逐条解释），遵循用户偏好（空格/2 空格）

## 示例提问（Examples）

- “基于项目结构生成 .editorconfig，并解释每条规则的作用”

- “为 Markdown 关闭修剪尾空格，其他文件开启”

## 结构化要点（CN/EN）

- 通用/Universal：root/charset/lf/trim/insert_final_newline

- 语言/Language：按扩展分节覆盖

- 偏好/Prefs：indent_style=space, indent_size=2

- 解释/Explain：规则逐条说明

## 中文思维导图

- 上下文分析
- 通用规则
- 语言分节
- 偏好覆盖
- 说明输出

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\editorconfig.prompt.md

- 生成时间：2025-10-17
