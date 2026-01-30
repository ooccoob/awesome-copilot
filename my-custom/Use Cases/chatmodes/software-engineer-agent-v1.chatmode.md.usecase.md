---
post_title: "software-engineer-agent-v1 — 用例"
post_slug: "software-engineer-agent-v1-use-cases"
tags: ['chatmode','agent','software-engineer','usecase']
ai_note: '根据 chatmodes/software-engineer-agent-v1.chatmode.md 生成的中文用例'
summary: '模拟软件工程师代理的任务分配、代码审查与自动化修复用例。'
post_date: '2025-10-20'
---

<!-- markdownlint-disable MD041 -->

什么

- 一个能够执行常规软件工程任务的代理：包括创建 PR、运行测试、生成修复建议与代码审查要点。

何时

- 在需要自动化常见重复性工程任务或作为开发助理来加速团队交付时。

为什么

- 提高开发效率、减少人工重复劳动，并为初学者提供可操作的指导。

如何

- 提供仓库上下文、失败的测试日志或待处理 issue；要求输出补丁建议、测试命令与审查要点。

关键要点

- 保持变更小且可验证
- 在提交或合并前执行最小安全检查
- 提供详细的审查注释以便人工复核

示例场景

1) 自动化修复 lint 错误
- 示例提示："为这个 lint 报告自动生成修复补丁并运行测试。"
- 预期產出：补丁文件、测试结果与变更摘要。

2) PR 初稿生成
- 示例提示："基于 issue 生成 PR 描述、变更范围和测试步骤。"
- 预期產出：PR 模板、变更点列表与回滚指引。

3) 代码审查要点
- 示例提示："审查此 PR 并指出潜在性能与安全问题。"
- 预期產出：审查清单与建议修改。

4) 回归测试自动化
- 示例提示："失败的集成测试生成最小复现并建议修复步骤。"
- 预期產出：复现脚本、关键断言与修复思路。

5) 文档同步
- 示例提示："根据代码变更更新相关文档与 chagelog。"
- 预期產出：文档片段与发行说明草案。

原始 chatmode: ../../../../chatmodes/software-engineer-agent-v1.chatmode.md
