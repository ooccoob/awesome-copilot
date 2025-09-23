---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems", "runCommands"]
description: "获取 Entity Framework Core 的最佳实践"
---

# Entity Framework Core 最佳实践

你的目标是帮助我在使用 Entity Framework Core 时遵循最佳实践。

## 数据上下文设计

- 保持 DbContext 聚焦且内聚
- 使用构造函数注入配置选项
- 通过重写 OnModelCreating 使用 Fluent API 做映射配置
- 用 IEntityTypeConfiguration 拆分实体配置
- 控制台应用或测试中考虑使用 DbContextFactory 模式

## 实体设计

- 使用有意义的主键（权衡自然键与代理键）
- 正确建模关系（一对一/一对多/多对多）
- 通过数据注解或 Fluent API 添加约束与验证
- 合理设计导航属性
- 值对象可用 Owned Entity Types

## 性能

- 只读查询使用 AsNoTracking()
- 大结果集实现分页：Skip() + Take()
- 需要时用 Include() 进行贪婪加载
- 使用投影（Select）仅取必要字段
- 高频查询使用已编译查询（Compiled Queries）
- 避免 N+1 问题：正确包含相关数据

## 迁移（Migrations）

- 创建小而专注的迁移
- 使用有意义的迁移名称
- 生产前审查迁移生成的 SQL
- 部署时考虑使用 migration bundles
- 适当时通过迁移添加种子数据

## 查询

- 谨慎使用 IQueryable，并理解查询何时执行
- 优先使用强类型 LINQ 而非原始 SQL
- 使用恰当的操作符（Where、OrderBy、GroupBy）
- 复杂操作可考虑数据库函数
- 可用 Specification 模式实现可复用查询

## 跟踪与保存

- 选择合适的更改跟踪策略
- 合批调用 SaveChanges()
- 多用户场景实现并发控制
- 多操作使用事务
- 为 Web 应用选择合适的 DbContext 生命周期（Scoped）

## 安全

- 通过参数化查询防止 SQL 注入
- 实施合适的数据访问权限
- 谨慎使用原始 SQL
- 敏感数据考虑加密
- 使用迁移管理数据库用户权限

## 测试

- 单元测试使用内存数据库 provider
- 集成测试可使用独立 SQLite 上下文
- 纯单元测试中 Mock DbContext/DbSet
- 在隔离环境中测试迁移
- 模型变更可考虑快照测试

在评审我的 EF Core 代码时，请识别上述问题并提出改进建议。
