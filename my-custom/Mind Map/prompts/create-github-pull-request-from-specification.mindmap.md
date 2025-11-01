## 文档综述（What/When/Why/How）

- What：基于规格模板创建/更新 GitHub Pull Request 的提示词

- When：需要以仓库的 pull_request_template.md 为规范生成 PR 草稿并完善标题/正文/状态时

- Why：统一 PR 结构与信息密度，保障追踪性与审阅效率，避免重复 PR

- How：读取模板→检查当前分支是否已有 PR→若无则创建草稿→获取 diff→按模板更新标题与正文→切换 Ready→指派作者

## 示例提问（Examples）

- “针对目标分支 main 生成 PR 草稿，并按模板填充变更概览/动机/测试/清单”

- “如果本分支已有 PR，直接更新标题与正文并切换 ready for review”

## 结构化要点（CN/EN）

- 模板/Template：.github/pull_request_template.md

- 去重/Dedup：若已存在则更新 | update if exists

- Diff 分析/Diff：get_pull_request_diff → 变更摘要

- 状态/State：Draft → Ready for review

- 指派/Assign：get_me → update_issue

## 中文思维导图

- 模板解析
  - 结构字段
  - 必填项
- PR 去重
  - 查询现有
  - 创建或更新
- 内容生成
  - 标题/正文
  - 变更摘要
- 审阅准备
  - Ready 状态
  - 指派作者

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\create-github-pull-request-from-specification.prompt.md

- 生成时间：2025-10-17
