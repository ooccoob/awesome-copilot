## 文档综述（What/When/Why/How）

- What：根据 https://llmstxt.org/ 规范，为仓库根创建 llms.txt 导航文件

- When：需要为 LLM 提供高价值入口，指向关键文档/规范/示例/配置时

- Why：帮助 LLM 快速理解仓库目的与结构，提升回答相关性与效率

- How：分析仓库→规划分节（Documentation/Specifications/Examples/Configuration/Optional）→生成 H1/引用/分节链接清单

## 示例提问（Examples）

- “扫描仓库并生成符合规范的 llms.txt，链接需相对路径且有效”

- “按优先级组织文件，文案简洁明确，适配人/LLM 双读者”

## 结构化要点（CN/EN）

- 结构/Format：H1→blockquote→H2 分节 | Spec-compliant

- 链接/Links：描述性标题 + 相对路径 | Descriptive links

- 分类/Sections：Docs/Specs/Examples/Config/Optional

- 选择/Selection：排除实现细节与无关内容 | Exclude noise

## 中文思维导图

- 规范研读
  - 结构要求
  - 链接格式
- 仓库分析
  - 目的/范围
  - 重点目录
- 内容规划
  - 分节与优先级
  - 描述撰写
- 校验
  - 规范/链接有效

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\create-llms.prompt.md

- 生成时间：2025-10-17
