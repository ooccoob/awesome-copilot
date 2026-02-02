---
applyTo: '*'
description: 'Quarkus development standards and instructions'
---

- 使用 Java 17 或更高版本的高质量 Quarkus 应用程序的说明。

## 项目背景

- 最新 Quarkus 版本：3.x
- Java版本：17或更高版本
- 使用 Maven 或 Gradle 进行构建管理。
- 专注于简洁的架构、可维护性和性能。

## 开发标准

  - 为每个类、方法和复杂的逻辑写出清晰简洁的注释。
  - 对公共 API 和方法使用 Javadoc，以确保消费者的清晰度。
  - 在整个项目中保持一致的编码风格，遵守 Java 约定。
  - 遵守 Quarkus 编码标准和最佳实践，以实现最佳性能和可维护性。
  - 遵循 Jarkarta EE 和 MicroProfile 约定，确保包组织清晰。
  - 在适当的情况下使用 Java 17 或更高版本的功能，例如记录和密封类。


## 命名约定
  - 使用 PascalCase 命名类名（例如 `ProductService`、`ProductResource`）。
  - 使用驼峰命名法作为方法和变量名称（例如 `findProductById`、`isProductAvailable`）。
  - 对常量使用 ALL_CAPS（例如 `DEFAULT_PAGE_SIZE`）。

##  夸库斯
  - 利用 Quarkus 开发模式加快开发周期。
  - 使用 Quarkus 扩展和最佳实践实施构建时优化。
  - 使用 GraalVM 配置本机构建以获得最佳性能（例如，使用 quarkus-maven-plugin）。
  - 使用 quarkus 日志记录功能（JBoss、SL4J 或 JUL）实现一致的日志记录实践。

### Quarkus 特定模式
- 对单例 bean 使用 `@ApplicationScoped` 而不是 `@Singleton`
- 使用 `@Inject` 进行依赖注入
- 与传统的 JPA 存储库相比，更喜欢 Panache 存储库
- 在修改数据的服务方法上使用 `@Transactional`
- 将 `@Path` 与描述性 REST 端点路径一起应用
- 对 REST 资源使用 `@Consumes(MediaType.APPLICATION_JSON)` 和 `@Produces(MediaType.APPLICATION_JSON)`

### 休息资源
- 始终使用 JAX-RS 注释（`@Path`、`@GET`、`@POST` 等）
- 返回正确的 HTTP 状态代码（200、201、400、404、500）
- 使用 `Response` 类进行复杂响应
- 使用 try-catch 块包含正确的错误处理
- 使用 Bean Validation 注解验证输入参数
- 对公共端点实施速率限制

### 数据存取
- 与传统 JPA 相比，更喜欢 Panache 实体（扩展 `PanacheEntity`）
- 使用 Panache 存储库 (`PanacheRepository<T>`) 进行复杂查询
- 始终使用 `@Transactional` 进行数据修改
- 使用命名查询进行复杂的数据库操作
- 为列表端点实现正确的分页


### 配置
- 使用 `application.properties` 或 `application.yaml` 进行简单配置
- 使用 `@ConfigProperty` 作为类型安全的配置类
- 敏感数据首选环境变量
- 使用不同环境的配置文件（开发、测试、生产）


### 测试
- 使用 `@QuarkusTest` 进行集成测试
- 使用 JUnit 5 进行单元测试
- 使用 `@QuarkusIntegrationTest` 进行本机构建测试
- 使用 `@QuarkusTestResource` 模拟外部依赖项
- 使用 RestAssured 进行 REST 端点测试 (`@QuarkusTestResource`)
- 使用 `@Transactional` 进行修改数据库的测试
- 使用测试容器进行数据库集成测试

### 不要使用这些模式：
- 不要在测试中使用字段注入（使用构造函数注入）
- 不要硬编码配置值
- 不要忽视异常


## 开发流程

### 创建新功能时：
1. 创建具有适当验证的实体
2. 使用自定义查询创建存储库
3. 使用业务逻辑创建服务
4. 使用适当的端点创建 REST 资源
5. 编写综合测试
6. 添加适当的错误处理
7. 更新文档

## 安全考虑

### 实施安全时：
- 使用 Quarkus 安全扩展（例如 `quarkus-smallrye-jwt`、`quarkus-oidc`）。
- 使用 MicroProfile JWT 或 OIDC 实施基于角色的访问控制 (RBAC)。
- 验证所有输入参数
