---
代理人：“代理人”
工具：['更改'、'搜索/代码库'、'编辑/编辑文件'、'问题'、'搜索']
描述：“获取使用 Spring Boot 和 Kotlin 开发应用程序的最佳实践。”
---

# Spring Boot 与 Kotlin 最佳实践

您的目标是帮助我使用 Kotlin 编写高质量、惯用的 Spring Boot 应用程序。

## 项目设置和结构

- **构建工具：** 将 Maven (`pom.xml`) 或 Gradle (`build.gradle`) 与 Kotlin 插件（`kotlin-maven-plugin` 或 `org.jetbrains.kotlin.jvm`）结合使用。
- **Kotlin 插件：** 对于 JPA，启用 `kotlin-jpa` 插件即可自动创建实体类 `open` 而无需样板。
- **启动器：** 像往常一样使用 Spring Boot 启动器（例如 `spring-boot-starter-web`、`spring-boot-starter-data-jpa`）。
- **包结构：** 按功能/域（例如 `com.example.app.order`、`com.example.app.user`）而不是按层组织代码。

## 依赖注入和组件

- **主构造函数：** 始终使用主构造函数来实现所需的依赖注入。这是 Kotlin 中最惯用、最简洁的方法。
- **不变性：** 在主构造函数中将依赖项声明为 `private val` 。在任何地方都优先使用 `val` 而不是 `var` 以提高不变性。
- **组件构造型：** 像在 Java 中一样使用 `@Service`、`@Repository` 和 `@RestController` 注释。

## 配置

- **外部化配置：** 使用 `application.yml` 的可读性和层次结构。
- **类型安全属性：** 使用 `@ConfigurationProperties` 和 `data class` 创建不可变的类型安全配置对象。
- **配置文件：** 使用 Spring 配置文件（`application-dev.yml`、`application-prod.yml`）来管理特定于环境的配置。
- **秘密管理：**切勿对秘密进行硬编码。使用环境变量或专用秘密管理工具，例如 HashiCorp Vault 或 AWS Secrets Manager。

## Web 层（控制器）

- **RESTful API：** 设计清晰且一致的 RESTful 端点。
- **DTO 的数据类：** 对所有 DTO 使用 Kotlin `data class`。这免费提供了 `equals()`、`hashCode()`、`toString()` 和 `copy()` 并提高了不变性。
- **验证：** 在 DTO 数据类上使用带有注释（`@Valid`、`@NotNull`、`@Size`）的 Java Bean 验证 (JSR 380)。
- **错误处理：** 使用 `@ControllerAdvice` 和 `@ExceptionHandler` 实现全局异常处理程序，以获得一致的错误响应。

## 服务层

- **业务逻辑：** 将业务逻辑封装在 `@Service` 类中。
- **无国籍：** 服务应该是无国籍的。
- **事务管理：** 在服务方法上使用 `@Transactional`。在 Kotlin 中，这可以应用于类或函数级别。

## 数据层（存储库）

- **JPA 实体：** 将实体定义为类。请记住它们必须是 `open`。强烈建议使用 `kotlin-jpa` 编译器插件来自动处理此问题。
- **空安全：** 利用 Kotlin 的空安全 (`?`) 来明确定义哪些实体字段在类型级别是可选的或必需的。
- **Spring Data JPA：** 通过扩展 `JpaRepository` 或 `CrudRepository` 使用 Spring Data JPA 存储库。
- **协程：** 对于反应式应用程序，在数据层利用 Spring Boot 对 Kotlin 协程的支持。

## 记录

- **伴随对象记录器：** 声明记录器的惯用方法是在伴随对象中。
  ```kotlin
  companion object {
      private val logger = LoggerFactory.getLogger(MyClass::class.java)
  }
  ```
- **参数化日志记录：** 使用参数化消息 (`logger.info("Processing user {}...", userId)`) 来提高性能和清晰度。

## 测试

- **JUnit 5：** JUnit 5 是默认设置，可与 Kotlin 无缝协作。
- **惯用的测试库：**为了更流畅和惯用的测试，请考虑使用 **Kotest** 进行断言，使用 **MockK** 进行模拟。它们是为 Kotlin 设计的，并提供更具表现力的语法。
- **测试切片：** 使用测试切片注释（如 `@WebMvcTest` 或 `@DataJpaTest`）来测试应用程序的特定部分。
- **测试容器：** 使用测试容器与真实数据库、消息代理等进行可靠的集成测试。

## 协程和异步编程

- **`suspend` 函数：** 对于非阻塞异步代码，请在控制器和服务中使用 `suspend` 函数。 Spring Boot 对协程有很好的支持。
- **结构化并发：** 使用 `coroutineScope` 或 `supervisorScope` 来管理协程的生命周期。
