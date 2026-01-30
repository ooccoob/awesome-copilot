## What
- Kotlin 与 Spring Boot 的工程化与最佳实践速览（结构、依赖注入、配置、Web/JPA、日志、测试、协程）。

## When to use
- 启动新项目或重构现有 Spring Boot Kotlin 服务，需对齐团队规范与可维护性。

## Why it matters
- Kotlin 语法特性与 Spring 习惯融合可提升简洁性、空安全与生产力；合理测试与配置管理提升稳定性。

## How (关键流程)
- 结构按领域分包；依赖注入用主构造+val；配置用 @ConfigurationProperties + data class
- Web：DTO 用 data class + 校验注解；异常用 @ControllerAdvice 统一处理
- 数据：kotlin-jpa 插件（实体 open）；Spring Data JPA；可选协程/响应式
- 日志：companion logger + 参数化日志
- 测试：JUnit5/Kotest/MockK；Testcontainers 做集成测试；测试切片
- 事务：@Transactional 在服务层；保持无状态服务

## Example questions (≥10)
1. 请生成一个 Kotlin Spring Boot 最小可运行样例，按领域分包并含健康检查接口。
2. 使用 @ConfigurationProperties 编写类型安全配置示例与绑定校验。
3. 给出 data class DTO + Bean Validation 的注册接口示例与控制器异常处理。
4. 实体 open 的三种方式对比（kotlin-jpa 插件/显式 open/All-open），推荐做法是哪种？
5. 提供使用 Testcontainers 的 PostgreSQL 集成测试样例（Repository + Service）。
6. 用 Kotest + MockK 为服务层写一个交互验证测试例子。
7. 示范协程在控制器与服务中使用 suspend，并解释结构化并发的边界处理。
8. 设计全局日志规范（TRACE-ERROR），并展示关键业务上下文的日志占位写法。
9. 列出常见 NPE/空安全陷阱与 Kotlin 化修复建议。
10. 如何用分层配置 application-dev.yml 与 application-prod.yml，并隐藏密钥？

## Key points
- CN: 领域分包、主构造注入、data class、全局异常、测试切片、Testcontainers
- EN: Feature-based packaging, constructor DI, data classes, global exception handling, test slices, Testcontainers

## Mind map (简要)
- Kotlin + Spring Boot
  - 结构/依赖
  - 配置/Profiles
  - Web/校验/异常
  - 数据/JPA/协程
  - 日志
  - 测试/容器
  - 事务

---
Source file: d:\mycode\awesome-copilot\prompts\kotlin-springboot.prompt.md
Generated: 2025-10-17T00:00:00Z
