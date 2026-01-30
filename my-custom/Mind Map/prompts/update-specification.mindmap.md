## What
- 目标：基于新需求或代码变更，更新 /spec/*.md 规范文档，优化为“生成式 AI 友好”的自包含规格。
- 模板：Front Matter + 10 个固定章节（目的/定义/需求/接口/验收/测试/背景/依赖/示例/校验/关联）。

## When
- 新增能力/接口/数据契约；架构/流程/安全策略调整；跨团队协作需要统一标准时。

## Why
- 使 AI/人均能准确解析与执行；减少歧义，提升自动化程度与复用性。

## How
- 读取 `${file}` → 依模板补齐与改写：
  - 清晰区分 REQ/SEC/CON/GUD/PAT；提供示例与边界；统一术语定义。
  - 接口/数据契约用表格/代码块描述；Given-When-Then 定义 AC。
  - 自动化测试策略：级别/框架/数据/CI/覆盖率/性能。
  - 依赖以“是什么/为何”描述，避免绑定具体库实现（除非为架构约束）。
  - 追加验证标准与相关文档链接；Front Matter last_updated 更新。

## Key Points
- 命名与路径：/spec/[schema|tool|data|infrastructure|process|architecture|design]-*.md。
- 语言：精确、无比喻；结构化列表/表格优先；自包含。
- 示例：覆盖边界与异常；必要时提供伪码/JSON Schema。

## Compact Map
- Analyze changes → Apply template → Update sections → Validate → Save

## Example Questions (10+)
- 本次变更涉及的数据契约有哪些字段新增/删除/变更？
- 如何以 Given-When-Then 写出可测试的 AC？
- 安全/合规要求（认证/授权/加密/日志）如何落在规范？
- 与现有模块的接口边界与幂等/重试策略是什么？
- 测试覆盖率阈值与性能指标如何设定？
- 依赖应如何抽象表述，避免绑定到具体实现？
- 示例应覆盖哪些极端/异常输入？
- 如何组织术语表并消除多义？
- 规范如何服务于代码生成与 PR 审核？
- 多服务/多仓下如何拆分与链接规范？
- 规范更新的版本化与变更记录如何维护？

---
Source: d:\mycode\awesome-copilot\prompts\update-specification.prompt.md
Generated: 2025-10-17T00:00:00Z
