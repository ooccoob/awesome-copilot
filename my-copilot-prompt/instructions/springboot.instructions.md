---
description: 'Guidelines for building Spring Boot base applications'
applyTo: '**/*.java, **/*.kt'
---

# Spring Boot开发

## 一般说明

- 在检查代码更改时仅提出高可信度建议。
- 编写具有良好可维护性实践的代码，包括对为什么做出某些设计决策的评论。
- 处理边缘情况并编写清晰的异常处理。
- 对于库或外部依赖项，请在注释中提及它们的用法和目的。

## Spring 启动说明

### 依赖注入

- 对所有必需的依赖项使用构造函数注入。
- 将依赖字段声明为 `private final`。

### 配置

- 使用 YAML 文件 (`application.yml`) 进行外部化配置。
- 环境配置文件：针对不同环境（开发、测试、生产）使用 Spring 配置文件
- 配置属性：使用@ConfigurationProperties进行类型安全的配置绑定
- 秘密管理：使用环境变量或秘密管理系统将秘密外部化

### 代码组织

- 包结构：按功能/域而不是按层组织
- 关注点分离：保持控制器精简、服务集中、存储库简单
- 实用程序类：使用私有构造函数使实用程序类成为最终的

### 服务层

- 将业务逻辑放置在带 `@Service` 注释的类中。
- 服务应该是无状态且可测试的。
- 通过构造函数注入存储库。
- 服务方法签名应使用域 ID 或 DTO，除非必要，否则不要直接公开存储库实体。

### 记录

- 使用 SLF4J 进行所有日志记录 (`private static final Logger logger = LoggerFactory.getLogger(MyClass.class);`)。
- 不要直接使用具体实现（Logback、Log4j2）或 `System.out.println()`。
- 使用参数化日志记录：`logger.info("User {} logged in", userId);`。

### 安全和输入处理

- 使用参数化查询 |始终使用 Spring Data JPA 或 `NamedParameterJdbcTemplate` 来防止 SQL 注入。
- 使用 JSR-380（`@NotNull`、`@Size` 等）注释和 `BindingResult` 验证请求正文和参数

## 构建和验证

- 添加或修改代码后，验证项目是否继续成功构建。
- 如果项目使用Maven，则运行`mvn clean package`。
- 如果项目使用 Gradle，请运行 `./gradlew build`（或 Windows 上的 `gradlew.bat build`）。
- 确保所有测试作为构建的一部分通过。

## 有用的命令

| Gradle 命令 | Maven 命令 |描述 |
|:--------------------------|:----------------------------------|:----------------------------------------------|
| __代码0__ |__代码1__ |运行应用程序。                          |
| __代码0__ |__代码1__ |构建应用程序。                        |
| __代码0__ |__代码1__ |运行测试。                                    |
| __代码0__ |__代码1__ |将应用程序打包为 JAR。             |
| __代码0__|__代码1__ |将应用程序打包为容器镜像。 |
