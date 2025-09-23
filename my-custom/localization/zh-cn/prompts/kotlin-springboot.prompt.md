---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems", "search"]
description: "获取使用 Kotlin 开发 Spring Boot 应用的最佳实践"
---

# Spring Boot with Kotlin 最佳实践

你的目标是帮助我用 Kotlin 编写高质量、符合惯用法的 Spring Boot 应用。

## 项目设置与结构

- **构建工具：** 使用 Maven（`pom.xml`）或 Gradle（`build.gradle`）并启用 Kotlin 插件（`kotlin-maven-plugin` 或 `org.jetbrains.kotlin.jvm`）
- **Kotlin 插件：** 如使用 JPA，启用 `kotlin-jpa` 以避免手动将实体设为 `open`
- **Starters：** 正常使用 Boot Starters（如 `spring-boot-starter-web`、`spring-boot-starter-data-jpa`）
- **按域组织包：** 按功能/领域而非严格分层

## 依赖注入与组件

- **主构造器：** 对必需依赖使用主构造器注入（Kotlin 最惯用、简洁）
- **不可变性：** 依赖声明为 `private val`，尽量使用 `val`
- **组件注解：** 与 Java 相同使用 `@Service`、`@Repository`、`@RestController`

## 配置

- **外置配置：** 使用 `application.yml`
- **类型安全属性：** `@ConfigurationProperties` + `data class` 生成不可变配置对象
- **Profiles：** 通过 `application-dev.yml`、`application-prod.yml` 管理环境差异
- **机密管理：** 不要硬编码机密；使用环境变量或专用机密管理工具

## Web 层（控制器）

- **RESTful：** 端点清晰一致
- **DTO：** 使用 Kotlin `data class` 作为 DTO，天然提供 `equals/hashCode/toString/copy`
- **校验：** 在 DTO 上使用 JSR 380 注解（`@Valid`、`@NotNull`、`@Size`）
- **错误处理：** `@ControllerAdvice` + `@ExceptionHandler`

## 服务层

- **业务逻辑：** 封装在 `@Service`
- **无状态：** 服务保持无状态
- **事务：** `@Transactional`（类/方法级）

## 数据层（仓储）

- **JPA 实体：** 类需为 `open`；推荐使用 `kotlin-jpa` 插件
- **空安全：** 使用 Kotlin 的空安全标注 `?` 定义可选字段
- **Spring Data JPA：** 继承 `JpaRepository`/`CrudRepository`
- **协程：** 在响应式应用中使用 Kotlin 协程

## 日志

- **伴生对象：**
  ```kotlin
  companion object {
      private val logger = LoggerFactory.getLogger(MyClass::class.java)
  }
  ```
- **参数化日志：** `logger.info("Processing user {}...", userId)`

## 测试

- **JUnit 5：** 与 Kotlin 无缝配合
- **Kotlin 生态：** 使用 Kotest（断言）与 MockK（Mock）
- **切片测试：** `@WebMvcTest`、`@DataJpaTest`
- **Testcontainers：** 真实依赖的可靠集成测试

## 协程与异步

- **`suspend`：** 控制器与服务中使用 `suspend` 提升非阻塞能力
- **结构化并发：** 使用 `coroutineScope` 或 `supervisorScope` 管理协程生命周期

```

```
