---
post_title: "ruby-mcp-expert — 用例"
post_slug: "ruby-mcp-expert-use-cases"
tags: ['chatmode','ruby','mcp','usecase']
ai_note: '根据 chatmodes/ruby-mcp-expert.chatmode.md 生成的中文用例'
summary: '针对 Ruby/Rails 应用的工程化用例，包括性能调优、依赖管理与部署流水线。'
post_date: '2025-10-20'
---

<!-- markdownlint-disable MD041 -->

什么

- 针对 Ruby 生态（尤其 Rails）常见工程问题提供诊断、修复与 CI/CD 建议。

何时

- 在维护遗留 Rails 应用、迁移 Ruby 版本或构建新的服务时。

为什么

- Ruby/Rails 在依赖、启动时间与 ActiveRecord 性能上有独特挑战，需要专门的实战用例。

如何

- 提供日志、慢查询样本或 Gemfile；请求输出优化清单、迁移步骤与 CI 配置示例。

关键要点

- 优化数据库查询与 N+1 问题
- 管理 Gem 版本与安全补丁
- 降低启动时间与内存占用

示例场景

1) N+1 查询修复
- 示例提示："定位并修复 N+1 查询，同时保持分页性能。"
- 预期產出：查询重写建议与索引调整。

2) Gem 依赖冲突
- 示例提示："为升级 Rails 版本准备 Gem 兼容性清单。"
- 预期產出：替代库建议与分阶段升级计划。

3) 性能回归分析
- 示例提示："对某次部署后的性能回归进行定位与修复建议。"
- 预期產出：回归引入点、负载测试建议与补救措施。

4) 配置 CI/CD
- 示例提示："构建一个针对 Rails 的快速 CI 流水线，并在合并前运行关键检查。"
- 预期產出：CI 配置样板、测试与部署阶段说明。

5) 内存优化
- 示例提示："分析内存泄漏并建议短期与长期缓解方案。"
- 预期產出：内存分析步骤、代码修复与监控建议。

原始 chatmode: ../../../../chatmodes/ruby-mcp-expert.chatmode.md
