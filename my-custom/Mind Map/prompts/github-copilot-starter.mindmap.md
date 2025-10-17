## What
- 为新项目基于技术栈创建完整的 GitHub Copilot 配置：instructions/prompts/chatmodes/workflows 目录与内容。

## When
- 新仓库初始化、需要团队化使用 Copilot 且遵循最佳实践时。

## Why
- 复用 awesome-copilot 既有模式，保证一致、可扩展、易上手。

## How
- 采集项目信息（语言/类型/规模/风格/技术）
- 研究：先 fetch awesome-copilot 指南与示例并归因备注
- 生成：.github 下 instructions/prompts/chatmodes/workflows
- 约束：instructions 不含代码；文件均带 frontmatter；workflow 简单
- 提供使用与自定义说明

## Key points (CN)
- “研究优先，改编其次，自创最后”
- 严格 frontmatter 与目录规范
- 工作流仅保留必要步骤

## Key points (EN)
- Research-first from awesome-copilot
- Clear structure and attribution
- Minimal workflows per tech stack

## Example questions
- “为 Java/Spring Boot 库生成完整 Copilot 配置骨架？”
- “按团队‘严格标准’风格定制 testing 与 review 指南？”

## 思维导图（要点）
- 采集→研究→生成→校验
- 结构/归因/约束

—
- Source: d:\mycode\awesome-copilot\prompts\github-copilot-starter.prompt.md
- Generated: 2025-10-17
