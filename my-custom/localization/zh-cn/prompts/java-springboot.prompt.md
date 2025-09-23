---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems", "search"]
description: "获取 Spring Boot 应用开发最佳实践"
---

# Spring Boot 最佳实践

你的目标是帮助我遵循既定最佳实践开发高质量的 Spring Boot 应用。

## 项目设置与结构

- **构建工具：** 使用 Maven（`pom.xml`）或 Gradle（`build.gradle`）进行依赖管理
- **Starters：** 使用 Spring Boot Starters（如 `spring-boot-starter-web`、`spring-boot-starter-data-jpa`）简化依赖
- **按域组织包：** 按功能/领域组织代码（如 `com.example.app.order`、`com.example.app.user`），而非严格按分层

## 依赖注入与组件

- **构造器注入：** 对必需依赖使用构造器注入，便于测试且依赖显式
- **不可变性：** 依赖字段声明为 `private final`
- **组件注解：** 合理使用 `@Component`、`@Service`、`@Repository`、`@Controller`/`@RestController`

## 配置

- **外置配置：** 使用 `application.yml`（或 `application.properties`），YAML 可读性与层次更好
- **类型安全属性：** 使用 `@ConfigurationProperties` 绑定到强类型对象
- **Profiles：** 使用 `application-dev.yml`、`application-prod.yml` 等环境配置
- **机密管理：** 不要硬编码机密；使用环境变量或 Vault/AWS Secrets Manager 等

## Web 层（控制器）

- **RESTful：** 端点清晰一致
- **DTO：** API 层使用 DTO，不要直接暴露 JPA 实体
- **校验：** 在 DTO 上使用 JSR 380 注解（`@Valid`、`@NotNull`、`@Size` 等）
- **错误处理：** 使用 `@ControllerAdvice` + `@ExceptionHandler` 统一错误响应

## 服务层

- **业务逻辑：** 封装于 `@Service`
- **无状态：** 服务保持无状态
- **事务：** `@Transactional` 标注在最细粒度的方法上

## 数据层（仓储）

- **Spring Data JPA：** 继承 `JpaRepository`/`CrudRepository`
- **自定义查询：** 复杂查询使用 `@Query` 或 Criteria API
- **投影：** 使用 DTO 投影只取必要字段

## 日志

- **SLF4J：** 使用 SLF4J API
- **声明：** `private static final Logger logger = LoggerFactory.getLogger(MyClass.class);`
- **参数化：** 使用参数化日志避免字符串拼接

## 测试

- **单元测试：** JUnit5 + Mockito
- **集成测试：** `@SpringBootTest`
- **切片测试：** `@WebMvcTest`、`@DataJpaTest` 等隔离特定层
- **Testcontainers：** 使用真实依赖的可靠集成测试

## 安全

- **Spring Security：** 处理认证与授权
- **密码加密：** 使用 BCrypt 等强哈希
- **输入与输出：** 使用参数化查询防 SQL 注入，正确输出编码防 XSS

```

```
