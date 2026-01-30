---
description: '构建 Spring Boot 基础应用程序的指南'
applyTo: '**/*.java, **/*.kt'
---

# Spring Boot 开发

## 一般指令

- 在审查代码更改时仅提出高置信度的建议。
- 编写具有良好可维护性实践的代码，包括对为什么做出某些设计决策的注释。
- 处理边缘情况并编写清晰的异常处理。
- 对于库或外部依赖项，在注释中提及它们的用途和目的。

## Spring Boot 指令

### 依赖注入

- 对所有必需的依赖项使用构造函数注入。
- 将依赖项字段声明为 `private final`。

### 配置

- 使用 YAML 文件（`application.yml`）进行外部化配置。
- 环境配置文件：使用 Spring 配置文件用于不同环境（dev、test、prod）
- 配置属性：使用 @ConfigurationProperties 进行类型安全的配置绑定
- 密钥管理：使用环境变量或密钥管理系统外部化密钥

### 代码组织

- 包结构：按功能/领域而不是按层组织
- 关注点分离：保持控制器薄、服务专注、仓储简单
- 工具类：使工具类为 final 并带有私有构造函数

### 服务层

- 将业务逻辑放在带有 `@Service` 注解的类中。
- 服务应该是无状态且可测试的。
- 通过构造函数注入仓储。
- 服务方法签名应使用域 ID 或 DTO，除非必要否则不直接暴露仓储实体。

### 日志记录

- 对所有日志记录使用 SLF4J（`private static final Logger logger = LoggerFactory.getLogger(MyClass.class);`）。
- 不要直接使用具体实现（Logback、Log4j2）或 `System.out.println()`。
- 使用参数化日志记录：`logger.info("User {} logged in", userId);`。

### 安全性和输入处理

- 使用参数化查询 | 始终使用 Spring Data JPA 或 `NamedParameterJdbcTemplate` 防止 SQL 注入。
- 使用 JSR-380（`@NotNull`、`@Size` 等）注解和 `BindingResult` 验证请求体和参数

## 构建和验证

- 在添加或修改代码后，验证项目继续成功构建。
- 如果项目使用 Maven，运行 `mvn clean package`。
- 如果项目使用 Gradle，运行 `./gradlew build`（在 Windows 上为 `gradlew.bat build`）。
- 确保所有测试都作为构建的一部分通过。

## 有用的命令

| Gradle 命令               | Maven 命令                        | 描述                                        |
|:--------------------------|:----------------------------------|:--------------------------------------------|
| `./gradlew bootRun`       |`./mvnw spring-boot:run`           | 运行应用程序。                              |
| `./gradlew build`         |`./mvnw package`                   | 构建应用程序。                              |
| `./gradlew test`          |`./mvnw test`                      | 运行测试。                                  |
| `./gradlew bootJar`       |`./mvnw spring-boot:repackage`     | 将应用程序打包为 JAR。                       |
| `./gradlew bootBuildImage`|`./mvnw spring-boot:build-image`   | 将应用程序打包为容器镜像。                   |