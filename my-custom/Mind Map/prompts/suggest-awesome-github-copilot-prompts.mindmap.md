## What
- 目标：基于当前仓库与会话上下文，筛选 awesome-copilot 中相关 prompts，避免与本地重复，输出建议表。
- 输入：远端 README.prompts.md 清单；本地 .github/prompts/*.prompt.md front matter；仓库技术/流程信号。
- 输出：候选表（上游链接、本地相似项、是否已装、引入理由），待确认后再安装。

## When
- 项目需要补齐分析/设计/编码/调试/测试/上线等阶段的提示库时。
- 新增技术/框架后需相应提示模板时。
- 希望沉淀团队标准化提示以提升质量与速度时。

## Why
- 降低提示工程门槛，统一产出质量。
- 复用社区高质量提示模版，快速覆盖场景。
- 避免重复与冲突，维持提示生态可维护。

## How
- fetch 上游目录 → 扫描本地 prompts → 解析 front matter → 匹配仓库特征与缺口 → 去重 → 输出建议表。
- 去重：主题/文件名近似 + 描述/用途对齐 → 标注重复/互补。
- 安装：经用户许可，落至 .github/prompts/；保留原文；记录 todos。

## Key Points
- 仅输出建议与链接，不直接安装；表格结构固定便于比对。
- 关注开发全链路及与现有工作流（CI/CD/Code Review）对接。
- 控制单文件体积与命名规范，便于后续治理。

## Compact Map
- Discovery: 上游清单 + 本地现况
- Analysis: 技术栈/流程缺口
- Suggest: 表格化候选（✅/❌ 已装）
- Next: 选择→下载→校验

## Example Questions (10+)
- 针对我们使用的 Vue2 + Spring Boot，哪些 prompts 最实用？
- 是否已有“代码审查”提示，新的会否重复？
- 需要“性能分析/SQL 优化/日志排错”类提示，有推荐吗？
- 为 Bicep/基础设施变更生成 MR 描述的提示有哪些？
- 能否提供“编写单测”的提示并适配我们断言风格？
- 如何为多语言仓库拆分提示生效范围？
- 是否有“发布说明/变更日志/版本升级”提示？
- 适配我们 README/规范模板的文档生成提示有哪些？
- 可否列出前 10 个最能提升效率的 prompts 与理由？
- 安装前如何对比本地相似提示以避免冲突？
- 如何计划后续提示的版本化与回滚？

---
Source: d:\mycode\awesome-copilot\prompts\suggest-awesome-github-copilot-prompts.prompt.md
Generated: 2025-10-17T00:00:00Z
