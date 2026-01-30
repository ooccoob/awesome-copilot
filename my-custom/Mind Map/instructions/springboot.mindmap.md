## What/When/Why/How
- What: Spring Boot 开发指南（依赖注入、配置、组织、日志、安全、构建）
- When: 新建/评审 Spring Boot 应用时
- Why: 提升健壮性、可维护与可测试
- How: 构造注入 + YAML/Profiles + @ConfigurationProperties + 分层

## Key Points
- 依赖注入：构造器 + private final；避免字段注入
- 配置：application.yml；profiles（dev/test/prod）；类型安全绑定
- 组织：按领域分包；Controller 薄、Service 聚焦、Repo 简洁；工具类 final
- 服务：无状态；DTO/ID 边界；事务边界清晰
- 日志：SLF4J 参数化；禁止 System.out
- 安全/输入：JSR-380 校验；参数化查询/JPA/NamedParameterJdbcTemplate
- 构建：Maven/Gradle 构建并跑测；变更后确保可编译

## Compact Map
- DI: constructor + final
- Config: yml + profiles + @ConfigurationProperties
- Layers: ctrl/service/repo
- QA: build+test on change

## Example Questions
1) 是否全部使用构造注入并声明依赖 final？
2) 配置是否类型安全绑定且区分环境？
3) 控制器是否纤薄并进行入参校验？
4) 事务是否覆盖修改路径并避免跨边界？
5) 日志是否参数化且无敏感信息？
6) SQL 是否全参数化或使用 Spring Data？
7) 包结构是否按领域而非技术层？
8) 异常处理是否清晰并返回一致错误体？
9) 是否提供集成测试与单元测试？
10) 构建是否在 CI 中自动验证通过？
11) 工具类是否不可实例化（私有构造）？

Source: d:\mycode\awesome-copilot\instructions\springboot.instructions.md | Generated: 2025-10-17
