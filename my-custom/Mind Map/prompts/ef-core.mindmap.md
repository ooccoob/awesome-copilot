## 文档综述（What/When/Why/How）

- What：Entity Framework Core 最佳实践（上下文/实体/性能/迁移/查询/变更跟踪/安全/测试）

- When：设计/优化 EF Core 数据访问层时

- Why：避免 N+1/过度跟踪/低效查询，提升性能与可维护性

- How：DbContext 设计分离；实体关系与约束；AsNoTracking/分页/投影/Include；规范迁移；并发/事务

## 示例提问（Examples）

- “为读操作使用 AsNoTracking 并改为投影以减少字段”

- “创建描述性迁移并评审 SQL，使用迁移 bundle 部署”

## 结构化要点（CN/EN）

- 上下文/Context：IEntityTypeConfiguration/Factory

- 实体/Entities：关系/约束/值对象

- 性能/Perf：分页/Include/Compiled Query/避免 N+1

- 迁移/Migrations：小步命名/脚本审查

- 查询/Query：LINQ 强类型/函数

- 跟踪/Tracking：批量 SaveChanges/并发/事务

- 安全/Security：参数化/权限/加密

- 测试/Testing：InMemory/SQLite/Mock

## 中文思维导图

- 设计
- 性能
- 迁移
- 查询
- 变更与事务
- 安全与测试

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\ef-core.prompt.md

- 生成时间：2025-10-17
