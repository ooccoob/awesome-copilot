---
agent: 'agent'
tools: ['changes', 'search/codebase', 'edit/editFiles', 'problems', 'runCommands']
description: 'Get best practices for Entity Framework Core'
---

# 实体框架核心最佳实践

您的目标是帮助我在使用 Entity Framework Core 时遵循最佳实践。

## 数据上下文设计

- 保持 DbContext 类的重点和凝聚力
- 使用构造函数注入配置选项
- 重写 OnModelCreating 以实现流畅的 API 配置
- 使用 IEntityTypeConfiguration 单独的实体配置
- 考虑对控制台应用程序或测试使用 DbContextFactory 模式

## 实体设计

- 使用有意义的主键（考虑自然键与代理键）
- 实施适当的关系（一对一、一对多、多对多）
- 使用数据注释或 Fluent API 进行约束和验证
- 实施适当的导航属性
- 考虑将拥有的实体类型用于值对象

## 性能

- 使用 AsNoTracking() 进行只读查询
- 使用 Skip() 和 Take() 实现大型结果集的分页
- 在需要时使用 Include() 预先加载相关实体
- 考虑投影（选择）以仅检索必填字段
- 对频繁执行的查询使用编译查询
- 通过正确包含相关数据来避免 N+1 查询问题

## 迁移

- 创建小型、集中的迁移
- 描述性地命名迁移
- 在应用于生产之前验证迁移 SQL 脚本
- 考虑使用迁移包进行部署
- 适当时通过迁移添加数据播种

## 查询

- 明智地使用 IQueryable 并了解查询何时执行
- 与原始 SQL 相比，更喜欢强类型 LINQ 查询
- 使用适当的查询运算符（Where、OrderBy、GroupBy）
- 考虑复杂操作的数据库函数
- 实施可重用查询的规范模式

## 变更跟踪和保存

- 使用适当的变更跟踪策略
- 批量调用 SaveChanges()
- 实现多用户场景的并发控制
- 考虑使用事务进行多个操作
- 使用适当的 DbContext 生命周期（适用于 Web 应用程序）

## 安全性

- 使用参数化查询避免 SQL 注入
- 实施适当的数据访问权限
- 小心原始 SQL 查询
- 考虑对敏感信息进行数据加密
- 使用迁移来管理数据库用户权限

## 测试

- 使用内存数据库提供程序进行单元测试
- 使用 SQLite 创建单独的测试上下文以进行集成测试
- 用于纯单元测试的 Mock DbContext 和 DbSet
- 在隔离环境中测试迁移
- 考虑对模型更改进行快照测试

在检查我的 EF Core 代码时，找出问题并提出遵循这些最佳实践的改进建议。
