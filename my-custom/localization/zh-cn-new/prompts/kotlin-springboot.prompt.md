---
mode: 'agent'
tools: ['changes', 'codebase', 'edit/editFiles', 'problems', 'search']
description: '获取使用Spring Boot和Kotlin开发应用程序的最佳实践。'
---

# Spring Boot与Kotlin最佳实践

您的目标是通过遵循既定最佳实践来帮助我使用Kotlin编写高质量、惯用的Spring Boot应用程序。

## 项目设置和结构

- **构建工具：** 使用带有Kotlin插件（`kotlin-maven-plugin`或`org.jetbrains.kotlin.jvm`）的Maven（`pom.xml`）或Gradle（`build.gradle`）。
- **Kotlin插件：** 对于JPA，启用`kotlin-jpa`插件，自动使实体类变为`open`而无需样板代码。
- **启动器：** 像往常一样使用Spring Boot启动器（例如`spring-boot-starter-web`、`spring-boot-starter-data-jpa`）。
- **包结构：** 按功能/域组织代码（例如`com.example.app.order`、`com.example.app.user`），而不是按层组织。

## 依赖注入和组件

- **主构造函数：** 始终使用主构造函数进行必需的依赖注入。这是Kotlin中最惯用和简洁的方法。
- **不可变性：** 在主构造函数中将依赖项声明为`private val`。在任何地方都优先使用`val`而不是`var`以促进不可变性。
- **组件构造型：** 像在Java中一样使用`@Service`、`@Repository`和`@RestController`注解。

## 配置

- **外部化配置：** 使用`application.yml`因其可读性和层次结构。
- **类型安全属性：** 使用`@ConfigurationProperties`与`data class`创建不可变的、类型安全的配置对象。
- **配置文件：** 使用Spring配置文件（`application-dev.yml`、`application-prod.yml`）来管理特定环境的配置。
- **秘密管理：** 绝不硬编码秘密。使用环境变量或专用秘密管理工具，如HashiCorp Vault或AWS Secrets Manager。

## Web层（控制器）

- **RESTful API：** 设计清晰一致的RESTful端点。
- **DTO的数据类：** 对所有DTO使用Kotlin `data class`。这免费提供`equals()`、`hashCode()`、`toString()`和`copy()`，并促进不可变性。
- **验证：** 在DTO数据类上使用Java Bean验证（JSR 380）注解（`@Valid`、`@NotNull`、`@Size`）。
- **错误处理：** 使用`@ControllerAdvice`和`@ExceptionHandler`实现全局异常处理器，以提供一致的错误响应。

## 服务层

- **业务逻辑：** 将业务逻辑封装在`@Service`类中。
- **无状态性：** 服务应该是无状态的。
- **事务管理：** 在服务方法上使用`@Transactional`。在Kotlin中，这可以应用于类或函数级别。

## 数据层（仓储）

- **JPA实体：** 将实体定义为类。记住它们必须是`open`的。强烈建议使用`kotlin-jpa`编译器插件自动处理这个问题。
- **空安全：** 利用Kotlin的空安全（`?`）在类型级别明确定义哪些实体字段是可选的或必需的。
- **Spring Data JPA：** 通过扩展`JpaRepository`或`CrudRepository`使用Spring Data JPA仓储。
- **协程：** 对于反应式应用程序，在数据层利用Spring Boot对Kotlin协程的支持。

## 日志记录

- **伴随对象日志记录器：** 声明日志记录器的惯用方式是在伴随对象中。
  ```kotlin
  companion object {
      private val logger = LoggerFactory.getLogger(MyClass::class.java)
  }
  ```
- **参数化日志记录：** 使用参数化消息（`logger.info("Processing user {}...", userId)`）以获得性能和清晰度。

## 测试

- **JUnit 5：** JUnit 5是默认选择，与Kotlin无缝配合。
- **惯用测试库：** 为了更流畅和惯用的测试，考虑使用**Kotest**进行断言，**MockK**进行模拟。它们专为Kotlin设计，提供更具表现力的语法。
- **测试切片：** 使用测试切片注解如`@WebMvcTest`或`@DataJpaTest`来测试应用程序的特定部分。
- **Testcontainers：** 使用Testcontainers进行与真实数据库、消息代理等的可靠集成测试。

## 协程和异步编程

- **`suspend`函数：** 对于非阻塞异步代码，在控制器和服务中使用`suspend`函数。Spring Boot对协程有出色的支持。
- **结构化并发：** 使用`coroutineScope`或`supervisorScope`来管理协程的生命周期。