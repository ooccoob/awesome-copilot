## What
- Spring Boot 开发最佳实践：结构、配置、Web/Service/数据层、测试、安全与日志。

## When
- 新建或重构 Spring Boot 应用，期望高可维护性与一致标准时。

## Why
- 降低隐性复杂度，提升测试性、扩展性与安全性。

## How
- 结构：按领域分包；使用 starters
- 配置：application.yml + @ConfigurationProperties + Profiles
- 控制层：DTO + 校验(@Valid) + 全局异常(@ControllerAdvice)
- 服务层：无状态 + @Transactional 粒度恰当
- 数据层：Spring Data JPA/投影/定制查询
- 测试：JUnit5/切片测试/集成测试/Testcontainers
- 安全与日志：Spring Security/BCrypt/SLF4J 参数化

## Key points (CN)
- 构造器注入+final；避免实体直出
- 只查所需字段；分页+缓存
- 统一错误响应与日志上下文

## Key points (EN)
- Feature-oriented packaging; typed config
- DTOs, validation, global error handling
- Transactions, projections, test slices

## Example questions
- “给用户模块加 @ConfigurationProperties 与切片测试示例？”
- “统一异常响应体与日志规范模板？”

## 思维导图（要点）
- 结构/配置
- Web/Service/Repo
- 测试/安全/日志
- 性能/分页/缓存

—
- Source: d:\mycode\awesome-copilot\prompts\java-springboot.prompt.md
- Generated: 2025-10-17
