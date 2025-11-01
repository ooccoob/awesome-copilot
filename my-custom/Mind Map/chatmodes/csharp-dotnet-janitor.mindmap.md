## What / When / Why / How

- What: C#/.NET 清洁工（现代化/质量/性能/测试/文档）
- When: 需要系统化清理技术债并提升代码质量
- Why: 降低维护成本、提升稳定与性能
- How: 增量小步、保持行为、每次修改伴随测试

## Key Points

- 现代化：语言新特性、可空、替换过时 API
- 质量：移除未用、命名一致、简化 LINQ、修复告警
- 性能：集合/内存/async/Span/Memory
- 测试：缺口分析、AAA、FluentAssertions
- 文档：XML 注释、README、使用示例
- 资料：microsoft.docs.mcp 查询官方最佳实践

## Compact Map

- 扫描警告与过时项
- 覆盖率缺口与关键路径
- 局部性能瓶颈与改造
- 文档同步与示例
- 每次变更→测试验证

## Example Questions (10+)

- 哪些 obsolete API 需要迁移？官方替代是什么？
- 可空参考类型引入范围与策略？
- 哪些 LINQ 可简化以提升可读性与性能？
- 分配/装箱热点在哪里？是否可用 Span/Memory？
- 异步调用链是否正确使用 async/await？
- 覆盖率缺口影响哪些公共 API？
- 静态分析告警的优先修复序？
- 命名与格式化策略如何一致化？
- 文档与示例是否反映最新 API？
- CI 如何强制这些规范并防回退？
- 变更是否影响向后兼容？

---
Source: d:\mycode\awesome-copilot\chatmodes\csharp-dotnet-janitor.chatmode.md
Generated: {{timestamp}}
