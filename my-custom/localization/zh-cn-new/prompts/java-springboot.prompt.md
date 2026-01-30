---
mode: 'agent'
tools: ['changes', 'codebase', 'edit/editFiles', 'problems', 'search']
description: '获取使用Spring Boot开发应用程序的最佳实践。'
---

# Spring Boot最佳实践

您的目标是通过遵循既定最佳实践来帮助我编写高质量的Spring Boot应用程序。

## 项目设置和结构

- **构建工具：** 使用Maven（`pom.xml`）或Gradle（`build.gradle`）进行依赖管理。
- **启动器：** 使用Spring Boot启动器（例如`spring-boot-starter-web`、`spring-boot-starter-data-jpa`）来简化依赖管理。
- **包结构：** 按功能/域组织代码（例如`com.example.app.order`、`com.example.app.user`），而不是按层组织（例如`com.example.app.controller`、`com.example.app.service`）。

## 依赖注入和组件

- **构造函数注入：** 始终对必需依赖项使用基于构造函数的注入。这使得组件更易于测试，依赖项更加明确。
- **不可变性：** 将依赖项字段声明为`private final`。
- **组件构造型：** 适当使用`@Component`、`@Service`、`@Repository`和`@Controller`/`@RestController`注解来定义bean。

## 配置

- **外部化配置：** 使用`application.yml`（或`application.properties`）进行配置。YAML因其可读性和层次结构而通常更受青睐。
- **类型安全属性：** 使用`@ConfigurationProperties`将配置绑定到强类型Java对象。
- **配置文件：** 使用Spring配置文件（`application-dev.yml`、`application-prod.yml`）来管理特定环境的配置。
- **秘密管理：** 不要硬编码秘密。使用环境变量或专用秘密管理工具，如HashiCorp Vault或AWS Secrets Manager。

## Web层（控制器）

- **RESTful API：** 设计清晰一致的RESTful端点。
- **DTO（数据传输对象）：** 在API层使用DTO来暴露和消费数据。不要直接向客户端暴露JPA实体。
- **验证：** 在DTO上使用Java Bean验证（JSR 380）注解（`@Valid`、`@NotNull`、`@Size`）来验证请求负载。
- **错误处理：** 使用`@ControllerAdvice`和`@ExceptionHandler`实现全局异常处理器，以提供一致的错误响应。

## 服务层

- **业务逻辑：** 将所有业务逻辑封装在`@Service`类中。
- **无状态性：** 服务应该是无状态的。
- **事务管理：** 在服务方法上使用`@Transactional`以声明方式管理数据库事务。在必要的最细粒度级别应用它。

## 数据层（仓储）

- **Spring Data JPA：** 通过扩展`JpaRepository`或`CrudRepository`使用Spring Data JPA仓储进行标准数据库操作。
- **自定义查询：** 对于复杂查询，使用`@Query`或JPA Criteria API。
- **投影：** 使用DTO投影从数据库中仅获取必要的数据。

## 日志记录

- **SLF4J：** 使用SLF4J API进行日志记录。
- **日志记录器声明：** `private static final Logger logger = LoggerFactory.getLogger(MyClass.class);`
- **参数化日志记录：** 使用参数化消息（`logger.info("Processing user {}...", userId);`）而不是字符串连接来提高性能。

## 测试

- **单元测试：** 使用JUnit 5和像Mockito这样的模拟框架为服务和组件编写单元测试。
- **集成测试：** 使用`@SpringBootTest`进行加载Spring应用程序上下文的集成测试。
- **测试切片：** 使用测试切片注解如`@WebMvcTest`（用于控制器）或`@DataJpaTest`（用于仓储）来隔离测试应用程序的特定部分。
- **Testcontainers：** 考虑使用Testcontainers进行与真实数据库、消息代理等的可靠集成测试。

## 安全

- **Spring Security：** 使用Spring Security进行身份验证和授权。
- **密码编码：** 始终使用强哈希算法（如BCrypt）编码密码。
- **输入清理：** 通过使用Spring Data JPA或参数化查询防止SQL注入。通过正确编码输出防止跨站脚本（XSS）。