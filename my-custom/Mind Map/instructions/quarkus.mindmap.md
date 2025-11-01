## What/When/Why/How
- What: Quarkus 开发规范（Java 17+、Panache、REST、配置、测试、安全）
- When: 新建/重构 Quarkus 服务与 API 时
- Why: 高性能/云原生、可维护与可测试
- How: 约定优于配置 + Dev 模式 + 原生编译 + 测试金字塔

## Key Points
- 版本/构建：Quarkus 3.x；Maven/Gradle；GraalVM 原生
- 结构：按领域分包；JAX-RS + @Path/@GET…；DTO 与实体解耦
- 数据：Panache 实体/仓储；@Transactional；分页/命名查询
- 配置：application.properties/yaml + @ConfigProperty；Profile 管理
- 日志：JBoss/SLF4J；结构化日志；避免 System.out
- 安全：OIDC/JWT；RBAC；Bean Validation
- 测试：@QuarkusTest、RestAssured、Testcontainers、集成/原生测试
- 反模式：字段注入/硬编码配置/吞异常

## Compact Map
- REST: JAX-RS + Response + status codes
- Data: Panache + repo + tx
- Config: profiles + secrets
- Test: QuarkusTest + RestAssured + containers

## Example Questions
1) 控制器是否返回合理状态码与错误体？
2) 数据修改是否标注 @Transactional 并隔离查询？
3) Panache 查询是否分页且避免 N+1？
4) 配置项是否使用 @ConfigProperty 且区分环境？
5) Secrets 是否来源于环境/密管而非硬编码？
6) 安全是否启用 OIDC/JWT 并完成角色校验？
7) 是否具备集成测试与原生镜像验证？
8) 日志是否参数化且包含关键上下文？
9) 包结构是否按领域而非层切？
10) 是否避免字段注入并使用构造注入？
11) 性能关键路径是否经过基准或剖析？

Source: d:\mycode\awesome-copilot\instructions\quarkus.instructions.md | Generated: 2025-10-17
