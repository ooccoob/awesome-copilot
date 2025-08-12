---
title: 'Prompts Localization Plan'
locale: 'zh-cn'
date_created: '2025-08-12'
last_updated: '2025-08-12'
owner: 'Localization Automation'
status: 'In progress'
---

## Prompts 英文化文档 -> 中文 (zh-cn) 本地化计划

## 目标

对 `prompts` 目录下尚未完成中文本地化的 `.md`（`.prompt.md`）文件进行高质量翻译，确保：

- 结构、段落、代码块与原文一一对应，不遗漏。
- 内部链接指向 zh-cn 已翻译版本（若存在），外部链接保持原样。
- 行数差异控制在 ±5%（中英文长度差异导致的自然换行除外），若超过需复核。
- 每个目标文件末尾追加本地化免责声明（中文）。

## 参考规范

遵循 `instructions/localization.instructions.md` 要求：

- 不遗漏章节与段落
- 图片与外链保留
- 内部文档链接指向 localized 版本
- 添加并本地化免责声明

免责声明模板：

```text
---
**免责声明**：本文件由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 自动本地化，可能存在不准确之处。若发现不当或错误翻译，请提交 [Issue](../../issues) 进行反馈。
```

## 状态枚举

- Pending: 尚未开始
- InProgress: 翻译中
- Review: 机器翻译完成待行数/质量复核
- Done: 已完成（含免责声明 & 行数核对）
- Skipped: 已存在翻译/无需处理

## 工作流

1. 读取源文件 -> 统计行数 S。
2. 翻译正文（保留 front matter 键；翻译 description 文本）。
3. 添加免责声明。(暂时跳过)
4. 生成目标文件（`localization/zh-cn/prompts/<filename>`）。
5. 统计目标行数 T，若 |T - S| / S > 0.05 进入 Review；否则标记 Done。
6. 更新本计划文件对应任务状态与时间戳。

## 优先级规则（初始）

- High: 源文件行数 ≥ 250 行
- Medium: 100 行 ≤ 源文件行数 < 250 行
- Low: 源文件行数 < 100 行

## 任务清单

| ID  | File                                                                | Priority | Source Path                                                                 | Target Path                                                                                    | SrcLines | TgtLines | Status | LastUpdate | Notes                                           |
| --- | ------------------------------------------------------------------- | -------- | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | -------- | -------- | ------ | ---------- | ----------------------------------------------- |
| 1   | ai-prompt-engineering-safety-review.prompt.md                       | Medium   | prompts/ai-prompt-engineering-safety-review.prompt.md                       | localization/zh-cn/prompts/ai-prompt-engineering-safety-review.prompt.md                       | 180      | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 2   | architecture-blueprint-generator.prompt.md                          | High     | prompts/architecture-blueprint-generator.prompt.md                          | localization/zh-cn/prompts/architecture-blueprint-generator.prompt.md                          | 266      | 94       | Review | 2025-08-12 | 初译完成，待复核                                |
| 3   | aspnet-minimal-api-openapi.prompt.md                                | Low      | prompts/aspnet-minimal-api-openapi.prompt.md                                | localization/zh-cn/prompts/aspnet-minimal-api-openapi.prompt.md                                | 32       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 4   | az-cost-optimize.prompt.md                                          | High     | prompts/az-cost-optimize.prompt.md                                          | localization/zh-cn/prompts/az-cost-optimize.prompt.md                                          | 281      | 263      | Review | 2025-08-12 | 结构已对齐，行数已统计，待差异复核              |
| 5   | azure-resource-health-diagnose.prompt.md                            | High     | prompts/azure-resource-health-diagnose.prompt.md                            | localization/zh-cn/prompts/azure-resource-health-diagnose.prompt.md                            | 264      | 232      | Review | 2025-08-12 | 结构已对齐，行数已统计，待差异复核              |
| 6   | breakdown-epic-arch.prompt.md                                       | Low      | prompts/breakdown-epic-arch.prompt.md                                       | localization/zh-cn/prompts/breakdown-epic-arch.prompt.md                                       | 41       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 7   | breakdown-epic-pm.prompt.md                                         | Low      | prompts/breakdown-epic-pm.prompt.md                                         | localization/zh-cn/prompts/breakdown-epic-pm.prompt.md                                         | 33       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 8   | breakdown-feature-implementation.prompt.md                          | Low      | prompts/breakdown-feature-implementation.prompt.md                          | localization/zh-cn/prompts/breakdown-feature-implementation.prompt.md                          | 92       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 9   | breakdown-feature-prd.prompt.md                                     | Low      | prompts/breakdown-feature-prd.prompt.md                                     | localization/zh-cn/prompts/breakdown-feature-prd.prompt.md                                     | 36       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 10  | breakdown-plan.prompt.md                                            | High     | prompts/breakdown-plan.prompt.md                                            | localization/zh-cn/prompts/breakdown-plan.prompt.md                                            | 349      | 96       | Review | 2025-08-12 | 初译完成；待补全细节                            |
| 11  | breakdown-test.prompt.md                                            | High     | prompts/breakdown-test.prompt.md                                            | localization/zh-cn/prompts/breakdown-test.prompt.md                                            | 265      | 293      | Review | 2025-08-12 | 重译并结构对齐，行数已统计，待差异复核          |
| 12  | code-exemplars-blueprint-generator.prompt.md                        | Medium   | prompts/code-exemplars-blueprint-generator.prompt.md                        | localization/zh-cn/prompts/code-exemplars-blueprint-generator.prompt.md                        | 103      | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 13  | comment-code-generate-a-tutorial.prompt.md                          | Low      | prompts/comment-code-generate-a-tutorial.prompt.md                          | localization/zh-cn/prompts/comment-code-generate-a-tutorial.prompt.md                          | 21       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 14  | containerize-aspnetcore.prompt.md                                   | High     | prompts/containerize-aspnetcore.prompt.md                                   | localization/zh-cn/prompts/containerize-aspnetcore.prompt.md                                   | 302      | 230      | Review | 2025-08-12 | 初译完成，待行数/结构复核                       |
| 15  | containerize-aspnet-framework.prompt.md                             | High     | prompts/containerize-aspnet-framework.prompt.md                             | localization/zh-cn/prompts/containerize-aspnet-framework.prompt.md                             | 368      | 297      | Review | 2025-08-12 | 初译完成；待补全细节                            |
| 16  | copilot-instructions-blueprint-generator.prompt.md                  | Medium   | prompts/copilot-instructions-blueprint-generator.prompt.md                  | localization/zh-cn/prompts/copilot-instructions-blueprint-generator.prompt.md                  | 231      | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 17  | create-architectural-decision-record.prompt.md                      | Low      | prompts/create-architectural-decision-record.prompt.md                      | localization/zh-cn/prompts/create-architectural-decision-record.prompt.md                      | 66       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 18  | create-github-action-workflow-specification.prompt.md               | Medium   | prompts/create-github-action-workflow-specification.prompt.md               | localization/zh-cn/prompts/create-github-action-workflow-specification.prompt.md               | 200      | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 19  | create-github-issue-feature-from-specification.prompt.md            | Low      | prompts/create-github-issue-feature-from-specification.prompt.md            | localization/zh-cn/prompts/create-github-issue-feature-from-specification.prompt.md            | 21       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 20  | create-github-issues-feature-from-implementation-plan.prompt.md     | Low      | prompts/create-github-issues-feature-from-implementation-plan.prompt.md     | localization/zh-cn/prompts/create-github-issues-feature-from-implementation-plan.prompt.md     | 21       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 21  | create-github-issues-for-unmet-specification-requirements.prompt.md | Low      | prompts/create-github-issues-for-unmet-specification-requirements.prompt.md | localization/zh-cn/prompts/create-github-issues-for-unmet-specification-requirements.prompt.md | 26       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 22  | create-implementation-plan.prompt.md                                | Medium   | prompts/create-implementation-plan.prompt.md                                | localization/zh-cn/prompts/create-implementation-plan.prompt.md                                | 106      | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 23  | create-llms.prompt.md                                               | Medium   | prompts/create-llms.prompt.md                                               | localization/zh-cn/prompts/create-llms.prompt.md                                               | 147      | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 24  | create-oo-component-documentation.prompt.md                         | Medium   | prompts/create-oo-component-documentation.prompt.md                         | localization/zh-cn/prompts/create-oo-component-documentation.prompt.md                         | 147      | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 25  | create-readme.prompt.md                                             | Low      | prompts/create-readme.prompt.md                                             | localization/zh-cn/prompts/create-readme.prompt.md                                             | 17       | 19       | Done   | 2025-08-12 | 行数差异在±5% 内                                |
| 26  | create-specification.prompt.md                                      | Low      | prompts/create-specification.prompt.md                                      | localization/zh-cn/prompts/create-specification.prompt.md                                      | 84       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 27  | create-spring-boot-java-project.prompt.md                           | Medium   | prompts/create-spring-boot-java-project.prompt.md                           | localization/zh-cn/prompts/create-spring-boot-java-project.prompt.md                           | 116      | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 28  | create-spring-boot-kotlin-project.prompt.md                         | Medium   | prompts/create-spring-boot-kotlin-project.prompt.md                         | localization/zh-cn/prompts/create-spring-boot-kotlin-project.prompt.md                         | 104      | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 29  | csharp-async.prompt.md                                              | Low      | prompts/csharp-async.prompt.md                                              | localization/zh-cn/prompts/csharp-async.prompt.md                                              | 35       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 30  | csharp-docs.prompt.md                                               | Low      | prompts/csharp-docs.prompt.md                                               | localization/zh-cn/prompts/csharp-docs.prompt.md                                               | 22       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 31  | csharp-mstest.prompt.md                                             | Low      | prompts/csharp-mstest.prompt.md                                             | localization/zh-cn/prompts/csharp-mstest.prompt.md                                             | 51       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 32  | csharp-nunit.prompt.md                                              | Low      | prompts/csharp-nunit.prompt.md                                              | localization/zh-cn/prompts/csharp-nunit.prompt.md                                              | 56       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 33  | csharp-tunit.prompt.md                                              | Low      | prompts/csharp-tunit.prompt.md                                              | localization/zh-cn/prompts/csharp-tunit.prompt.md                                              | 79       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 34  | csharp-xunit.prompt.md                                              | Low      | prompts/csharp-xunit.prompt.md                                              | localization/zh-cn/prompts/csharp-xunit.prompt.md                                              | 53       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 35  | dotnet-best-practices.prompt.md                                     | Low      | prompts/dotnet-best-practices.prompt.md                                     | localization/zh-cn/prompts/dotnet-best-practices.prompt.md                                     | 61       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 36  | dotnet-design-pattern-review.prompt.md                              | Low      | prompts/dotnet-design-pattern-review.prompt.md                              | localization/zh-cn/prompts/dotnet-design-pattern-review.prompt.md                              | 33       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 37  | ef-core.prompt.md                                                   | Low      | prompts/ef-core.prompt.md                                                   | localization/zh-cn/prompts/ef-core.prompt.md                                                   | 57       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 38  | folder-structure-blueprint-generator.prompt.md                      | High     | prompts/folder-structure-blueprint-generator.prompt.md                      | localization/zh-cn/prompts/folder-structure-blueprint-generator.prompt.md                      | 331      | 212      | Review | 2025-08-12 | 初译完成；待行数复核                            |
| 39  | generate-custom-instructions-from-codebase.prompt.md                | Medium   | prompts/generate-custom-instructions-from-codebase.prompt.md                | localization/zh-cn/prompts/generate-custom-instructions-from-codebase.prompt.md                | 184      | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 40  | gen-specs-as-issues.prompt.md                                       | Medium   | prompts/gen-specs-as-issues.prompt.md                                       | localization/zh-cn/prompts/gen-specs-as-issues.prompt.md                                       | 123      | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 41  | git-flow-branch-creator.prompt.md                                   | High     | prompts/git-flow-branch-creator.prompt.md                                   | localization/zh-cn/prompts/git-flow-branch-creator.prompt.md                                   | 253      | 253      | Review | 2025-08-12 | 初译完成，待复核                                |
| 42  | java-docs.prompt.md                                                 | Low      | prompts/java-docs.prompt.md                                                 | localization/zh-cn/prompts/java-docs.prompt.md                                                 | 22       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 43  | java-junit.prompt.md                                                | Low      | prompts/java-junit.prompt.md                                                | localization/zh-cn/prompts/java-junit.prompt.md                                                | 48       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 44  | javascript-typescript-jest.prompt.md                                | Low      | prompts/javascript-typescript-jest.prompt.md                                | localization/zh-cn/prompts/javascript-typescript-jest.prompt.md                                | 37       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 45  | java-springboot.prompt.md                                           | Low      | prompts/java-springboot.prompt.md                                           | localization/zh-cn/prompts/java-springboot.prompt.md                                           | 46       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 46  | kotlin-springboot.prompt.md                                         | Low      | prompts/kotlin-springboot.prompt.md                                         | localization/zh-cn/prompts/kotlin-springboot.prompt.md                                         | 51       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 47  | mkdocs-translations.prompt.md                                       | Low      | prompts/mkdocs-translations.prompt.md                                       | localization/zh-cn/prompts/mkdocs-translations.prompt.md                                       | 83       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 48  | multi-stage-dockerfile.prompt.md                                    | Low      | prompts/multi-stage-dockerfile.prompt.md                                    | localization/zh-cn/prompts/multi-stage-dockerfile.prompt.md                                    | 36       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 49  | my-issues.prompt.md                                                 | Low      | prompts/my-issues.prompt.md                                                 | localization/zh-cn/prompts/my-issues.prompt.md                                                 | 7        | 9        | Done   | 2025-08-12 | 行数差异在±5% 内                                |
| 50  | my-pull-requests.prompt.md                                          | Low      | prompts/my-pull-requests.prompt.md                                          | localization/zh-cn/prompts/my-pull-requests.prompt.md                                          | 10       | 12       | Done   | 2025-08-12 | 行数差异在±5% 内                                |
| 51  | next-intl-add-language.prompt.md                                    | Low      | prompts/next-intl-add-language.prompt.md                                    | localization/zh-cn/prompts/next-intl-add-language.prompt.md                                    | 16       | 18       | Done   | 2025-08-12 | 行数差异在±5% 内                                |
| 52  | playwright-automation-fill-in-form.prompt.md                        | Low      | prompts/playwright-automation-fill-in-form.prompt.md                        | localization/zh-cn/prompts/playwright-automation-fill-in-form.prompt.md                        | 18       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 53  | playwright-explore-website.prompt.md                                | Low      | prompts/playwright-explore-website.prompt.md                                | localization/zh-cn/prompts/playwright-explore-website.prompt.md                                | 15       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 54  | playwright-generate-test.prompt.md                                  | Low      | prompts/playwright-generate-test.prompt.md                                  | localization/zh-cn/prompts/playwright-generate-test.prompt.md                                  | 15       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 55  | postgresql-code-review.prompt.md                                    | Medium   | prompts/postgresql-code-review.prompt.md                                    | localization/zh-cn/prompts/postgresql-code-review.prompt.md                                    | 173      | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 56  | postgresql-optimization.prompt.md                                   | High     | prompts/postgresql-optimization.prompt.md                                   | localization/zh-cn/prompts/postgresql-optimization.prompt.md                                   | 334      | 302      | Review | 2025-08-12 | 初译完成；待行数复核                            |
| 57  | project-workflow-analysis-blueprint-generator.prompt.md             | High     | prompts/project-workflow-analysis-blueprint-generator.prompt.md             | localization/zh-cn/prompts/project-workflow-analysis-blueprint-generator.prompt.md             | 244      | 203      | Review | 2025-08-12 | 初译完成，待复核                                |
| 58  | prompt-builder.prompt.md                                            | Medium   | prompts/prompt-builder.prompt.md                                            | localization/zh-cn/prompts/prompt-builder.prompt.md                                            | 110      | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 59  | readme-blueprint-generator.prompt.md                                | Low      | prompts/readme-blueprint-generator.prompt.md                                | localization/zh-cn/prompts/readme-blueprint-generator.prompt.md                                | 59       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 60  | repo-story-time.prompt.md                                           | Medium   | prompts/repo-story-time.prompt.md                                           | localization/zh-cn/prompts/repo-story-time.prompt.md                                           | 110      | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 61  | review-and-refactor.prompt.md                                       | Low      | prompts/review-and-refactor.prompt.md                                       | localization/zh-cn/prompts/review-and-refactor.prompt.md                                       | 11       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 62  | sql-code-review.prompt.md                                           | High     | prompts/sql-code-review.prompt.md                                           | localization/zh-cn/prompts/sql-code-review.prompt.md                                           | 248      | 200      | Review | 2025-08-12 | 初译完成，待复核                                |
| 63  | sql-optimization.prompt.md                                          | High     | prompts/sql-optimization.prompt.md                                          | localization/zh-cn/prompts/sql-optimization.prompt.md                                          | 249      | 220      | Review | 2025-08-12 | 初译完成，待复核                                |
| 64  | suggest-awesome-github-copilot-chatmodes.prompt.md                  | Low      | prompts/suggest-awesome-github-copilot-chatmodes.prompt.md                  | localization/zh-cn/prompts/suggest-awesome-github-copilot-chatmodes.prompt.md                  | 54       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 65  | suggest-awesome-github-copilot-prompts.prompt.md                    | Low      | prompts/suggest-awesome-github-copilot-prompts.prompt.md                    | localization/zh-cn/prompts/suggest-awesome-github-copilot-prompts.prompt.md                    | 54       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 66  | technology-stack-blueprint-generator.prompt.md                      | Medium   | prompts/technology-stack-blueprint-generator.prompt.md                      | localization/zh-cn/prompts/technology-stack-blueprint-generator.prompt.md                      | 207      | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 67  | update-avm-modules-in-bicep.prompt.md                               | Low      | prompts/update-avm-modules-in-bicep.prompt.md                               | localization/zh-cn/prompts/update-avm-modules-in-bicep.prompt.md                               | 35       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 68  | update-implementation-plan.prompt.md                                | Medium   | prompts/update-implementation-plan.prompt.md                                | localization/zh-cn/prompts/update-implementation-plan.prompt.md                                | 106      | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 69  | update-llms.prompt.md                                               | Medium   | prompts/update-llms.prompt.md                                               | localization/zh-cn/prompts/update-llms.prompt.md                                               | 167      | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 70  | update-markdown-file-index.prompt.md                                | Low      | prompts/update-markdown-file-index.prompt.md                                | localization/zh-cn/prompts/update-markdown-file-index.prompt.md                                | 54       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 71  | update-oo-component-documentation.prompt.md                         | Medium   | prompts/update-oo-component-documentation.prompt.md                         | localization/zh-cn/prompts/update-oo-component-documentation.prompt.md                         | 120      | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |
| 72  | update-specification.prompt.md                                      | Low      | prompts/update-specification.prompt.md                                      | localization/zh-cn/prompts/update-specification.prompt.md                                      | 84       | 0        | Review | 2025-08-12 | 已翻译；暂跳过(3)(5)，未添加免责声明/未统计行数 |

## 批次策略

启动批次（Baseline 评估）：针对 High 优先级中篇幅最大的 3–5 篇（如 containerize-aspnet-framework、breakdown-plan、postgresql-optimization、folder-structure-blueprint-generator、containerize-aspnetcore）。

随后按优先级滚动执行，每批 4–8 篇：

- 先 High，再 Medium，穿插 1–2 篇 Low 作为“快胜利（quick win）”。
- 每批结束做行数差异与结构对齐复核，更新本计划表。

## 更新日志

| Date       | Action | Detail                                |
| ---------- | ------ | ------------------------------------- |
| 2025-08-12 | Init   | 建立 prompts 翻译计划，登记 72 个文件 |
