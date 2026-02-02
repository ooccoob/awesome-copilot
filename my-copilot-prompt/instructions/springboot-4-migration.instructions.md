---
description: "Comprehensive guide for migrating Spring Boot applications from 3.x to 4.0, focusing on Gradle Kotlin DSL and version catalogs"
applyTo: "**/*.java, **/*.kt, **/build.gradle.kts, **/build.gradle, **/settings.gradle.kts, **/gradle/libs.versions.toml, **/*.properties, **/*.yml, **/*.yaml"
---

# Spring Boot 3.x 到 4.0 迁移指南

## 项目背景

本指南提供了有关将 Spring Boot 项目从版本 3.x 升级到 4.0 的全面 GitHub Copilot 说明，重点是 Gradle Kotlin DSL、版本目录 (`libs.versions.toml`) 和特定于 Kotlin 的注意事项。

**Spring Boot 4.0 中的关键架构变化：**
- 模块化依赖结构，具有集中的、较小的模块
- 需要 Spring 框架 7.x
- Jakarta EE 11（Servlet 6.1 基线）
- Jackson 3.x 迁移（包命名空间更改）
- Kotlin 2.2+ 要求
- 全面产权重组

## 系统要求

### 最低版本

- **Java**：17+（首选最新的 LTS：Java 21 或 25）
- **Kotlin**：2.2.0 或更高版本
- **Spring 框架**：7.x（由 Spring Boot 4.0 管理）
- **Jakarta EE**：11（Servlet 6.1 基线）
- **GraalVM**（对于本机映像）：25+
- **Gradle**：8.5+（用于 Kotlin DSL 和版本目录支持）
- **Gradle CycloneDX 插件**：3.0.0+

### 验证兼容性

```bash
# Check current versions
./gradlew --version
./gradlew dependencies --configuration runtimeClasspath
```

## 迁移前步骤

### 1.升级到最新的Spring Boot 3.5.x

在迁移到 4.0 之前，请升级到最新的 3.5.x 版本：

```kotlin
// libs.versions.toml
[versions]
springBoot = "3.5.6" # Latest 3.x before migrating to 4.0
```

### 2. 清理弃用内容

从 Spring Boot 3.x 中删除所有已弃用的 API 使用。这些将是 4.0 中的编译错误：

```bash
# Build and review warnings
./gradlew clean build --warning-mode all
```

### 3. 检查依赖项更改

比较您的依赖关系：
- [Spring Boot 3.5.x 依赖版本](https://docs.spring.io/spring-boot/3.5/appendix/dependency-versions/coordinates.html)
- [Spring Boot 4.0.x 依赖版本](https://docs.spring.io/spring-boot/4.0/appendix/dependency-versions/coordinates.html)

## 模块重组和启动器更改

### 关键：模块化架构

Spring Boot 4.0 引入了**更小的、更集中的模块**来取代大型的整体 jar。这需要大多数项目中的依赖项更新。

**对于库作者很重要：**由于模块化工作和包重组，**强烈建议不要在同一工件中支持 Spring Boot 3 和 Spring Boot 4**。库作者应该为每个主要版本发布单独的工件，以避免运行时冲突并确保干净的依赖关系管理。

### 迁移策略：选择一种方法

#### 选项 1：特定技术的启动器（推荐用于生产）

Spring Boot 涵盖的大多数技术现在都有**专用的测试入门伴侣**。这提供了细粒度的控制。

**完整的入门参考：** 有关所有可用入门（核心、Web、数据库、Spring Data、消息传递、安全、模板、生产就绪等）及其测试伙伴的综合表，请参阅[官方 Spring Boot 4.0 迁移指南](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide#starters)。

**libs.versions.toml：**
```toml
[versions]
springBoot = "4.0.0"

[libraries]
# Core starters with dedicated test modules
spring-boot-starter-web = { module = "org.springframework.boot:spring-boot-starter-webmvc", version.ref = "springBoot" }
spring-boot-starter-webmvc-test = { module = "org.springframework.boot:spring-boot-starter-webmvc-test", version.ref = "springBoot" }

spring-boot-starter-data-jpa = { module = "org.springframework.boot:spring-boot-starter-data-jpa", version.ref = "springBoot" }
spring-boot-starter-data-jpa-test = { module = "org.springframework.boot:spring-boot-starter-data-jpa-test", version.ref = "springBoot" }

spring-boot-starter-security = { module = "org.springframework.boot:spring-boot-starter-security", version.ref = "springBoot" }
spring-boot-starter-security-test = { module = "org.springframework.boot:spring-boot-starter-security-test", version.ref = "springBoot" }
```

**构建.gradle.kts：**
```kotlin
dependencies {
    implementation(libs.spring.boot.starter.webmvc)
    implementation(libs.spring.boot.starter.data.jpa)
    implementation(libs.spring.boot.starter.security)

    testImplementation(libs.spring.boot.starter.webmvc.test)
    testImplementation(libs.spring.boot.starter.data.jpa.test)
    testImplementation(libs.spring.boot.starter.security.test)
}
```

#### 选项 2：经典入门（快速迁移，已弃用）

为了快速迁移，请使用捆绑所有自动配置的**经典启动器**（如 Spring Boot 3.x）：

**libs.versions.toml：**
```toml
[libraries]
spring-boot-starter-classic = { module = "org.springframework.boot:spring-boot-starter-classic", version.ref = "springBoot" }
spring-boot-starter-test-classic = { module = "org.springframework.boot:spring-boot-starter-test-classic", version.ref = "springBoot" }
```

**构建.gradle.kts：**
```kotlin
dependencies {
    implementation(libs.spring.boot.starter.classic)
    testImplementation(libs.spring.boot.starter.test.classic)
}
```

**警告**：经典启动器已**弃用**，并将在未来版本中删除。计划迁移到特定技术的启动器。

#### 选项 3：直接模块依赖项（高级）

对于传递依赖的显式控制：

**libs.versions.toml：**
```toml
[libraries]
spring-boot-webmvc = { module = "org.springframework.boot:spring-boot-webmvc", version.ref = "springBoot" }
spring-boot-webmvc-test = { module = "org.springframework.boot:spring-boot-webmvc-test", version.ref = "springBoot" }
```

### 重命名 Starters（重大更改）

更新 `libs.versions.toml` 中的这些起始名称：

| Spring Boot 3.x |春季启动4.0 |笔记|
|----------------|-----------------|-------|
| __代码0__ | __代码1__ |显式命名|
| __代码0__ | __代码1__ |连字符已删除 |
| __代码0__ | __代码1__ |仅当使用 `org.aspectj.lang.annotation` | 时才需要
| __代码0__ | __代码1__ |安全命名空间|
| __代码0__ | __代码1__ |安全命名空间|
| __代码0__ | __代码1__ |安全命名空间|

**迁移示例（libs.versions.toml）：**
```toml
[libraries]
# Old (Spring Boot 3.x)
# spring-boot-starter-web = { module = "org.springframework.boot:spring-boot-starter-web", version.ref = "springBoot" }
# spring-boot-starter-oauth2-client = { module = "org.springframework.boot:spring-boot-starter-oauth2-client", version.ref = "springBoot" }

# New (Spring Boot 4.0)
spring-boot-starter-webmvc = { module = "org.springframework.boot:spring-boot-starter-webmvc", version.ref = "springBoot" }
spring-boot-starter-security-oauth2-client = { module = "org.springframework.boot:spring-boot-starter-security-oauth2-client", version.ref = "springBoot" }
```

### AspectJ 入门说明

仅当您**实际使用 AspectJ 注释**时才包含 `spring-boot-starter-aspectj`：

```kotlin
// Only needed if code uses org.aspectj.lang.annotation package
import org.aspectj.lang.annotation.Aspect
import org.aspectj.lang.annotation.Before

@Aspect
class MyAspect {
    @Before("execution(* com.example..*(..))")
    fun beforeAdvice() { }
}
```

如果不使用 AspectJ，请删除依赖项。

## 删除的功能和替代方案

### 嵌入式服务器

#### 移除了暗流

**Undertow 已完全删除** - 与 Servlet 6.1 基线不兼容。

**迁移：**
- 使用 **Tomcat**（默认）或 **Jetty**
- **不要**将 Spring Boot 4.0 应用程序部署到非 Servlet 6.1 容器

**libs.versions.toml：**
```toml
[libraries]
# Remove Undertow
# spring-boot-starter-undertow = { module = "org.springframework.boot:spring-boot-starter-undertow", version.ref = "springBoot" }

# Use Tomcat (default) or Jetty
spring-boot-starter-jetty = { module = "org.springframework.boot:spring-boot-starter-jetty", version.ref = "springBoot" }
```

**构建.gradle.kts：**
```kotlin
dependencies {
    implementation(libs.spring.boot.starter.webmvc) {
        exclude(group = "org.springframework.boot", module = "spring-boot-starter-tomcat")
    }
    implementation(libs.spring.boot.starter.jetty) // Alternative to Tomcat
}
```

### 会话管理

#### 春季会议 Hazelcast 和 MongoDB 已删除

**由各自团队维护**，不再在 Spring Boot 依赖管理中。

**迁移（libs.versions.toml）：**
```toml
[versions]
hazelcast-spring-session = "3.x.x" # Check Hazelcast documentation
mongodb-spring-session = "4.x.x"   # Check MongoDB documentation

[libraries]
# Explicit versions required
spring-session-hazelcast = { module = "com.hazelcast:spring-session-hazelcast", version.ref = "hazelcast-spring-session" }
spring-session-mongodb = { module = "org.springframework.session:spring-session-data-mongodb", version.ref = "mongodb-spring-session" }
```

### 反应式消息传递

#### Pulsar Reactive 已删除

Spring Pulsar 放弃了 Reactor 支持 - 删除了反应式 Pulsar 客户端。

**迁移：**
- 使用命令式 Pulsar 客户端
- 或者迁移到替代反应式消息传递（Kafka、RabbitMQ）

### 测试

#### Spock 框架已删除

**Spock 尚不支持 Groovy 5**（Spring Boot 4.0 所需）。

**迁移：**
- 将 JUnit 5 与 Kotlin 结合使用
- 或者等待 Spock Groovy 5 兼容性

### 构建特点

#### 删除了可执行 Jar 启动脚本

删除了“完全可执行”jar 的嵌入式启动脚本（特定于 Unix，使用有限）。

**build.gradle.kts（删除）：**
```kotlin
// Remove this configuration
tasks.bootJar {
    launchScript() // No longer supported
}
```

**替代方案：**
- 直接使用`java -jar app.jar`
- 将 Gradle 应用程序插件用于本机启动器
- 使用systemd服务文件

#### 经典的 Uber-Jar 装载机被移除

经典的 uber-jar 加载器已被删除。从构建中删除任何加载器实现配置。

**Maven (pom.xml) - 删除：**
```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
            <configuration>
                <loaderImplementation>CLASSIC</loaderImplementation> <!-- REMOVE THIS -->
            </configuration>
        </plugin>
    </plugins>
</build>
```

**Gradle (build.gradle.kts) - 删除：**
```kotlin
tasks.bootJar {
    loaderImplementation = org.springframework.boot.loader.tools.LoaderImplementation.CLASSIC // REMOVE THIS
}
```

## 杰克逊3号迁移

### 主要突破性变化：包命名空间

Jackson 3 更改了**组 ID 和包名称**：

|组件|老（杰克逊2）|新（杰克逊 3）|
|-----------|----------------|-----------------|
|群组 ID | __代码0__ | __代码1__ |
|套餐 | __代码0__ | __代码1__ |
|例外 | __代码0__ |仍然使用 `com.fasterxml.jackson.core` 组 |

**libs.versions.toml：**
```toml
[versions]
jackson = "3.0.1" # Managed by Spring Boot 4.0

[libraries]
# Jackson 3 uses new group ID
jackson-databind = { module = "tools.jackson.core:jackson-databind", version.ref = "jackson" }
jackson-module-kotlin = { module = "tools.jackson.module:jackson-module-kotlin", version.ref = "jackson" }

# Exception: annotations still use old group
jackson-annotations = { module = "com.fasterxml.jackson.core:jackson-annotations", version.ref = "jackson" }
```

### 类和注释重命名

更新导入和注释：

| Spring Boot 3.x |春季启动4.0 |
|----------------|-----------------|
| __代码0__ | __代码1__ |
| __代码0__ | __代码1__ |
| __代码0__ | __代码1__ |
| __代码0__ | __代码1__ |
| __代码0__ | __代码1__ |

**迁移示例：**
```kotlin
// Old (Spring Boot 3.x)
import com.fasterxml.jackson.databind.ObjectMapper
import org.springframework.boot.autoconfigure.jackson.Jackson2ObjectMapperBuilderCustomizer
import org.springframework.boot.jackson.JsonComponent

@JsonComponent
class CustomSerializer : JsonSerializer<MyType>() { }

@Configuration
class JacksonConfig {
    @Bean
    fun customizer(): Jackson2ObjectMapperBuilderCustomizer {
        return Jackson2ObjectMapperBuilderCustomizer { builder ->
            builder.simpleDateFormat("yyyy-MM-dd")
        }
    }
}

// New (Spring Boot 4.0)
import tools.jackson.databind.ObjectMapper
import org.springframework.boot.autoconfigure.jackson.JsonMapperBuilderCustomizer
import org.springframework.boot.jackson.JacksonComponent

@JacksonComponent
class CustomSerializer : JsonSerializer<MyType>() { }

@Configuration
class JacksonConfig {
    @Bean
    fun customizer(): JsonMapperBuilderCustomizer {
        return JsonMapperBuilderCustomizer { builder ->
            builder.simpleDateFormat("yyyy-MM-dd")
        }
    }
}
```

### 配置属性更改

**application.yml 迁移：**
```yaml
# Old (Spring Boot 3.x)
spring:
  jackson:
    read:
      enums-using-to-string: true
    write:
      dates-as-timestamps: false

# New (Spring Boot 4.0)
spring:
  jackson:
    json:
      read:
        enums-using-to-string: true
      write:
        dates-as-timestamps: false
```

### Jackson 2 兼容性模块（临时）

对于逐步迁移，请使用**临时兼容性模块**（已弃用，将被删除）：

**libs.versions.toml：**
```toml
[libraries]
spring-boot-jackson2 = { module = "org.springframework.boot:spring-boot-jackson2", version.ref = "springBoot" }
```

**构建.gradle.kts：**
```kotlin
dependencies {
    implementation(libs.spring.boot.jackson2)
}
```

**应用程序.yml：**
```yaml
spring:
  jackson:
    use-jackson2-defaults: true # Use Jackson 2 behavior
```

**使用兼容性模块时 `spring.jackson2.*` 命名空间下的属性**。

**计划从此模块迁移** - 它将在未来版本中删除。

## 核心框架变更

### 可空性注释：JSpecify

Spring Boot 4.0 在整个代码库中添加了 **JSpecify 可空性注释**。

**影响：**
- Kotlin 空安全可能会标记新的警告/错误
- 空检查器（SpotBugs、NullAway）可能会报告新问题
- **像 `body()` 这样的 RestClient 方法现在显式标记为可为 null** - 始终检查 null 或使用 `Objects.requireNonNull()`

**迁移到 Kotlin：**
```kotlin
// Explicit nullable types may be required
fun processUser(id: String?): User? {
    return userRepository.findById(id) // May now be explicitly nullable
}

// RestClient body() can return null
val body: String? = restClient.get()
    .uri("https://api.example.com/data")
    .retrieve()
    .body(String::class.java) // Nullable - handle appropriately

if (body != null) {
    println(body.length)
}
```

**执行器端点参数：**
- 不能使用 `javax.annotations.NonNull` 或 `org.springframework.lang.Nullable`
- 使用 `org.jspecify.annotations.Nullable` 代替

**libs.versions.toml：**
```toml
[libraries]
jspecify = { module = "org.jspecify:jspecify", version = "1.0.0" }
```

### 包裹搬迁

#### Bootstrap注册中心

**旧进口：**
```kotlin
import org.springframework.boot.BootstrapRegistry
```

**新进口：**
```kotlin
import org.springframework.boot.bootstrap.BootstrapRegistry
```

#### 环境后处理器

**旧进口：**
```kotlin
import org.springframework.boot.env.EnvironmentPostProcessor
```

**新进口：**
```kotlin
import org.springframework.boot.EnvironmentPostProcessor
```

**更新`META-INF/spring.factories`：**
```properties
# Old
org.springframework.boot.env.EnvironmentPostProcessor=com.example.MyPostProcessor

# New
org.springframework.boot.EnvironmentPostProcessor=com.example.MyPostProcessor
```

**注意：** 已弃用的表单暂时仍可用，但将被删除。

#### 实体扫描

**旧进口：**
```kotlin
import org.springframework.boot.autoconfigure.domain.EntityScan
```

**新进口：**
```kotlin
import org.springframework.boot.persistence.autoconfigure.EntityScan
```

### 记录更改

#### 登录默认字符集

日志文件现在默认为 **UTF-8** （与 Log4j2 协调）：

**logback-spring.xml（显式配置）：**
```xml
<configuration>
    <appender name="FILE" class="ch.qos.logback.core.FileAppender">
        <file>app.log</file>
        <encoder>
            <charset>UTF-8</charset> <!-- Now default -->
            <pattern>%d{yyyy-MM-dd HH:mm:ss} - %msg%n</pattern>
        </encoder>
    </appender>
</configuration>
```

**控制台日志记录：** 如果可用，则使用 `Console#charset()` (Java 17+)，否则回退到 UTF-8。这提供了更好的平台兼容性，同时保持一致的编码。

### 开发工具变更

#### 默认情况下禁用实时重新加载

**应用程序.yml：**
```yaml
spring:
  devtools:
    livereload:
      enabled: true # Must explicitly enable in 4.0
```

**libs.versions.toml：**
```toml
[libraries]
spring-boot-devtools = { module = "org.springframework.boot:spring-boot-devtools", version.ref = "springBoot" }
```

**构建.gradle.kts：**
```kotlin
dependencies {
    developmentOnly(libs.spring.boot.devtools)
}
```

### PropertyMapper API 行为变化

**重大更改：** 当源为 `null` 时，默认情况下不再调用适配器/谓词方法。

**迁移模式：**
```kotlin
// Old behavior (Spring Boot 3.x)
map.from(source::method).to(destination::method)
// Calls destination.method(null) if source returns null

// New behavior (Spring Boot 4.0)
map.from(source::method).to(destination::method)
// Skips call if source returns null

// Explicit null handling (new)
map.from(source::method).always().to(destination::method)
// Always calls destination.method(value), even if null
```

**删除的方法：** `alwaysApplyingNotNull()` - 使用 `always()` 代替。

**迁移示例：**查看 [Spring Boot commit 239f384ac0](https://github.com/spring-projects/spring-boot/commit/239f384ac0893d151b89f204886874c6adb00001) 以了解 Spring Boot 本身如何适应新的 API。

## 依赖关系和构建更改

### Gradle 插件更新

**构建.gradle.kts：**
```kotlin
plugins {
    kotlin("jvm") version "2.2.0" // Minimum 2.2.0
    kotlin("plugin.spring") version "2.2.0"
    id("org.springframework.boot") version "4.0.0"
    id("io.spring.dependency-management") version "1.1.7"
    id("org.cyclonedx.bom") version "3.0.0" // Minimum 3.0.0
}
```

### Gradle 中的可选依赖项

默认情况下，可选依赖项**不再包含在 uber jar 中**。

**build.gradle.kts（明确包含选项）：**
```kotlin
tasks.bootJar {
    includeOptional = true // If needed
}
```

### Spring Retry → Spring 框架核心重试

Spring Boot 4.0 删除了 **Spring Retry** 的依赖管理（迁移到 Spring Framework 7.0 核心重试的组合）。

**迁移选项 1：使用 Spring Framework 核心重试（推荐）**

```kotlin
// Use built-in Spring Framework retry
import org.springframework.core.retry.RetryTemplate
import org.springframework.core.retry.support.RetryTemplateBuilder

@Configuration
class RetryConfig {
    @Bean
    fun retryTemplate(): RetryTemplate {
        return RetryTemplateBuilder()
            .maxAttempts(3)
            .fixedBackoff(1000)
            .build()
    }
}
```

**迁移选项 2：显式 Spring 重试版本（临时）**

**libs.versions.toml：**
```toml
[versions]
spring-retry = "2.0.5" # Explicit version required

[libraries]
spring-retry = { module = "org.springframework.retry:spring-retry", version.ref = "spring-retry" }
```

**计划迁移到 Spring Framework 核心重试。**

### Spring授权服务器

现在 Spring Security 的一部分 - 删除了显式版本管理。

**libs.versions.toml（之前 - Spring Boot 3.x）：**
```toml
[versions]
spring-authorization-server = "1.3.0" # No longer works

[libraries]
spring-security-oauth2-authorization-server = { module = "org.springframework.security:spring-security-oauth2-authorization-server", version.ref = "spring-authorization-server" }
```

**迁移（Spring Boot 4.0）：**
```toml
[versions]
spring-security = "7.0.0" # Use Spring Security version instead

[libraries]
# Managed by spring-security.version property, not separate
spring-security-oauth2-authorization-server = { module = "org.springframework.security:spring-security-oauth2-authorization-server", version.ref = "spring-security" }
```

或者依赖Spring Boot依赖管理（推荐）：
```kotlin
dependencies {
    implementation("org.springframework.security:spring-security-oauth2-authorization-server")
    // Version managed by Spring Boot 4.0
}
```

### Elasticsearch 客户端变更

#### 低级客户端替换

**已弃用的低级 `RestClient` → 新的 `Rest5Client`:**

**注意：**高级客户端（`ElasticsearchClient` 和 Spring Data 的 `ReactiveElasticsearchClient`）**保持不变**，并已在内部更新以使用新的低级客户端。

**进口：**
```kotlin
// Old (Spring Boot 3.x)
import org.elasticsearch.client.RestClient
import org.elasticsearch.client.RestClientBuilder
import org.springframework.boot.autoconfigure.elasticsearch.RestClientBuilderCustomizer

// New (Spring Boot 4.0)
import co.elastic.clients.transport.rest_client.Rest5Client
import co.elastic.clients.transport.rest_client.Rest5ClientBuilder
import org.springframework.boot.autoconfigure.elasticsearch.Rest5ClientBuilderCustomizer
```

**配置：**
```kotlin
@Configuration
class ElasticsearchConfig {

    // Old
    // @Bean
    // fun restClientCustomizer(): RestClientBuilderCustomizer {
    //     return RestClientBuilderCustomizer { builder ->
    //         builder.setRequestConfigCallback { config ->
    //             config.setConnectTimeout(5000)
    //         }
    //     }
    // }

    // New
    @Bean
    fun rest5ClientCustomizer(): Rest5ClientBuilderCustomizer {
        return Rest5ClientBuilderCustomizer { builder ->
            builder.setRequestConfigCallback { config ->
                config.setConnectTimeout(5000)
            }
        }
    }
}
```

**依赖整合：**

嗅探器现在包含在 `co.elastic.clients:elasticsearch-java` 模块中。

**libs.versions.toml：**
```toml
[libraries]
# Remove these - no longer managed
# elasticsearch-rest-client = { module = "org.elasticsearch.client:elasticsearch-rest-client", version = "..." }
# elasticsearch-rest-client-sniffer = { module = "org.elasticsearch.client:elasticsearch-rest-client-sniffer", version = "..." }

# Use single dependency (includes sniffer)
elasticsearch-java = { module = "co.elastic.clients:elasticsearch-java", version = "8.x.x" }
```

### Hibernate 依赖项更改

**libs.versions.toml：**
```toml
[libraries]
# Renamed module (hibernate-jpamodelgen replaced by hibernate-processor)
hibernate-processor = { module = "org.hibernate.orm:hibernate-processor", version.ref = "hibernate" }

# These artifacts are NO LONGER PUBLISHED by Hibernate:
# hibernate-proxool - discontinued by Hibernate project
# hibernate-vibur - discontinued by Hibernate project
# Remove any dependencies on these modules
```

**注意：** `hibernate-jpamodelgen` 工件仍然存在，但已被弃用。继续使用 `hibernate-processor` 。

## 配置属性更改

### MongoDB 财产重组

**重大重组：** 非 Spring Data 属性移至 `spring.mongodb.*`：

**application.yml 迁移：**
```yaml
# Old (Spring Boot 3.x)
spring:
  data:
    mongodb:
      uri: mongodb://localhost:27017/mydb
      database: mydb
      host: localhost
      port: 27017
      username: user
      password: pass
      authentication-database: admin
      replica-set-name: rs0
      additional-hosts:
        - host1:27017
        - host2:27017
      ssl:
        enabled: true
        bundle: my-bundle
      representation:
        uuid: STANDARD

management:
  health:
    mongo:
      enabled: true
  metrics:
    mongo:
      command:
        enabled: true
      connectionpool:
        enabled: true

# New (Spring Boot 4.0)
spring:
  mongodb:
    uri: mongodb://localhost:27017/mydb
    database: mydb
    host: localhost
    port: 27017
    username: user
    password: pass
    authentication-database: admin
    replica-set-name: rs0
    additional-hosts:
      - host1:27017
      - host2:27017
    ssl:
      enabled: true
      bundle: my-bundle
    representation:
      uuid: STANDARD # Explicit configuration now required

  data:
    mongodb:
      # Spring Data-specific properties remain here
      auto-index-creation: true
      field-naming-strategy: org.springframework.data.mapping.model.SnakeCaseFieldNamingStrategy
      gridfs:
        bucket: fs
        database: gridfs-db
      repositories:
        type: auto
      representation:
        big-decimal: DECIMAL128 # Explicit configuration now required

management:
  health:
    mongodb: # Renamed from "mongo"
      enabled: true
  metrics:
    mongodb: # Renamed from "mongo"
      command:
        enabled: true
      connectionpool:
        enabled: true
```

**主要变化：**
- **UUID 表示**：**强制** - 未提供默认值，必须显式配置 `spring.mongodb.representation.uuid`（例如，`STANDARD`、`JAVA_LEGACY`、`PYTHON_LEGACY`、`C_SHARP_LEGACY`）
- **BigDecimal 表示**：**强制** - 未提供默认值，必须显式配置 `spring.data.mongodb.representation.big-decimal`（例如 `DECIMAL128`、`STRING`）
- **管理属性**：`mongo` → `mongodb`
- **如果保存 UUID 或 BigDecimal 值时未能配置这些将导致运行时错误**

### Spring 会话属性重命名

**application.yml 迁移：**
```yaml
# Old (Spring Boot 3.x)
spring:
  session:
    redis:
      namespace: myapp:session
      flush-mode: on-save
    mongodb:
      collection-name: sessions

# New (Spring Boot 4.0)
spring:
  session:
    data:
      redis:
        namespace: myapp:session
        flush-mode: on-save
      mongodb:
        collection-name: sessions
```

### 持久性模块属性更改

**application.yml 迁移：**
```yaml
# Old (Spring Boot 3.x)
spring:
  dao:
    exceptiontranslation:
      enabled: true

# New (Spring Boot 4.0)
spring:
  persistence:
    exceptiontranslation:
      enabled: true
```

## Web 框架的变化

### 静态资源位置

`PathRequest#toStaticResources()` 现在默认包含 `/fonts/**`。

**安全配置（如果需要，排除字体）：**
```kotlin
import org.springframework.boot.autoconfigure.security.servlet.PathRequest
import org.springframework.boot.autoconfigure.security.StaticResourceLocation

@Configuration
@EnableWebSecurity
class SecurityConfig {

    @Bean
    fun securityFilterChain(http: HttpSecurity): SecurityFilterChain {
        http {
            authorizeHttpRequests {
                // Exclude fonts if needed
                authorize(PathRequest.toStaticResources()
                    .atCommonLocations()
                    .excluding(StaticResourceLocation.FONTS), permitAll)
                authorize(anyRequest, authenticated)
            }
        }
        return http.build()
    }
}
```

### HttpMessageConverters 弃用

由于框架改进（合并的客户端/服务器转换器），`HttpMessageConverters` 已弃用。

**迁移：**
```kotlin
// Old (Spring Boot 3.x)
import org.springframework.boot.autoconfigure.http.HttpMessageConverters
import org.springframework.context.annotation.Bean

@Configuration
class WebConfig {
    @Bean
    fun customConverters(): HttpMessageConverters {
        return HttpMessageConverters(MyCustomConverter())
    }
}

// New (Spring Boot 4.0)
import org.springframework.boot.autoconfigure.http.client.ClientHttpMessageConvertersCustomizer
import org.springframework.boot.autoconfigure.http.server.ServerHttpMessageConvertersCustomizer

@Configuration
class WebConfig {

    // Separate client and server converters
    @Bean
    fun clientConvertersCustomizer(): ClientHttpMessageConvertersCustomizer {
        return ClientHttpMessageConvertersCustomizer { converters ->
            converters.add(MyCustomClientConverter())
        }
    }

    @Bean
    fun serverConvertersCustomizer(): ServerHttpMessageConvertersCustomizer {
        return ServerHttpMessageConvertersCustomizer { converters ->
            converters.add(MyCustomServerConverter())
        }
    }
}
```

### 球衣和 Jackson 3 不兼容

**Jersey 4.0 限制：** Spring Boot 4.0 支持 Jersey 4.0，**尚不支持 Jackson 3**。

**解决方案：** 使用 `spring-boot-jackson2` 兼容性模块 **代替或与 ** `spring-boot-jackson` 一起使用：

**libs.versions.toml：**
```toml
[libraries]
spring-boot-starter-jersey = { module = "org.springframework.boot:spring-boot-starter-jersey", version.ref = "springBoot" }
spring-boot-jackson2 = { module = "org.springframework.boot:spring-boot-jackson2", version.ref = "springBoot" }
# Optional: Keep Jackson 3 for non-Jersey parts of application
spring-boot-jackson = { module = "org.springframework.boot:spring-boot-jackson", version.ref = "springBoot" }
```

**构建.gradle.kts：**
```kotlin
dependencies {
    implementation(libs.spring.boot.starter.jersey)
    implementation(libs.spring.boot.jackson2) // Required for Jersey JSON processing
    // Optional: Use Jackson 3 elsewhere in application
    // implementation(libs.spring.boot.jackson)
}
```

**注意：** 如果您的应用程序中仅使用 Jersey，您可以使用 Jackson 2 兼容模块完全替换 Jackson 3。

## 消息传递框架的变化

### Kafka Streams 定制器更换

**已弃用 `StreamBuilderFactoryBeanCustomizer` → `StreamsBuilderFactoryBeanConfigurer`:**

```kotlin
// Old (Spring Boot 3.x)
import org.springframework.boot.autoconfigure.kafka.StreamsBuilderFactoryBeanCustomizer

@Configuration
class KafkaStreamsConfig {
    @Bean
    fun streamsCustomizer(): StreamBuilderFactoryBeanCustomizer {
        return StreamBuilderFactoryBeanCustomizer { factoryBean ->
            factoryBean.setKafkaStreamsCustomizer { streams ->
                // Custom config
            }
        }
    }
}

// New (Spring Boot 4.0)
import org.springframework.kafka.config.StreamsBuilderFactoryBeanConfigurer

@Configuration
class KafkaStreamsConfig {
    @Bean
    fun streamsConfigurer(): StreamsBuilderFactoryBeanConfigurer {
        return StreamsBuilderFactoryBeanConfigurer { factoryBean ->
            factoryBean.setKafkaStreamsCustomizer { streams ->
                // Custom config
            }
        }
    }
}
```

**注意：** 新配置器使用默认值 `0` 实现 `Ordered`。

### Kafka 重试属性更改

**application.yml 迁移：**
```yaml
# Old (Spring Boot 3.x)
spring:
  kafka:
    retry:
      topic:
        backoff:
          random: true

# New (Spring Boot 4.0)
spring:
  kafka:
    retry:
      topic:
        backoff:
          jitter: 0.5 # More flexible than boolean
```

### RabbitMQ 重试定制器拆分

**Spring AMQP 从 Spring Retry → Spring Framework 核心重试**，与定制器拆分：

```kotlin
// Old (Spring Boot 3.x)
import org.springframework.boot.autoconfigure.amqp.RabbitRetryTemplateCustomizer

@Configuration
class RabbitConfig {
    @Bean
    fun retryCustomizer(): RabbitRetryTemplateCustomizer {
        return RabbitRetryTemplateCustomizer { template ->
            // Applies to both RabbitTemplate and listeners
        }
    }
}

// New (Spring Boot 4.0)
import org.springframework.boot.autoconfigure.amqp.RabbitTemplateRetrySettingsCustomizer
import org.springframework.boot.autoconfigure.amqp.RabbitListenerRetrySettingsCustomizer

@Configuration
class RabbitConfig {

    // For RabbitTemplate operations
    @Bean
    fun templateRetryCustomizer(): RabbitTemplateRetrySettingsCustomizer {
        return RabbitTemplateRetrySettingsCustomizer { settings ->
            settings.maxAttempts = 5
        }
    }

    // For message listeners
    @Bean
    fun listenerRetryCustomizer(): RabbitListenerRetrySettingsCustomizer {
        return RabbitListenerRetrySettingsCustomizer { settings ->
            settings.maxAttempts = 3
        }
    }
}
```

## 测试框架的变化

### Mockito 集成已删除

`MockitoTestExecutionListener` 已删除（在 3.4 中已弃用）。

**迁移到 MockitoExtension：**
```kotlin
// Old (Spring Boot 3.x)
import org.springframework.boot.test.context.SpringBootTest
import org.mockito.Mock
import org.mockito.Captor

@SpringBootTest
class MyServiceTest {
    @Mock
    private lateinit var repository: MyRepository

    @Captor
    private lateinit var captor: ArgumentCaptor<String>
}

// New (Spring Boot 4.0)
import org.springframework.boot.test.context.SpringBootTest
import org.mockito.Mock
import org.mockito.Captor
import org.mockito.junit.jupiter.MockitoExtension
import org.junit.jupiter.api.extension.ExtendWith

@SpringBootTest
@ExtendWith(MockitoExtension::class) // Explicit extension required
class MyServiceTest {
    @Mock
    private lateinit var repository: MyRepository

    @Captor
    private lateinit var captor: ArgumentCaptor<String>
}
```

### @SpringBootTest 更改

`@SpringBootTest` 不再自动提供 **MockMVC**、**WebTestClient** 或 **TestRestTemplate**。

#### 模拟MVC配置

```kotlin
// Old (Spring Boot 3.x)
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class ControllerTest {
    @Autowired
    private lateinit var mockMvc: MockMvc // Available automatically
}

// New (Spring Boot 4.0)
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc
import org.springframework.boot.test.autoconfigure.web.servlet.HtmlUnit

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@AutoConfigureMockMvc // Explicit annotation required
class ControllerTest {
    @Autowired
    private lateinit var mockMvc: MockMvc
}

// HtmlUnit configuration moved to annotation attribute
@AutoConfigureMockMvc(
    htmlUnit = HtmlUnit(webClient = false, webDriver = false)
)
```

#### Web测试客户端配置

```kotlin
// Old (Spring Boot 3.x)
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class WebFluxTest {
    @Autowired
    private lateinit var webTestClient: WebTestClient // Available automatically
}

// New (Spring Boot 4.0)
import org.springframework.boot.test.autoconfigure.web.reactive.AutoConfigureWebTestClient

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@AutoConfigureWebTestClient // Explicit annotation required
class WebFluxTest {
    @Autowired
    private lateinit var webTestClient: WebTestClient
}
```

#### TestRestTemplate → RestTestClient（推荐）

**Spring Boot 4.0 引入了 `RestTestClient`** 作为 `TestRestTemplate` 的现代替代品。

```kotlin
// Old approach (still works with annotation)
import org.springframework.boot.test.autoconfigure.web.client.AutoConfigureTestRestTemplate
import org.springframework.boot.test.web.client.TestRestTemplate

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@AutoConfigureTestRestTemplate // Required in 4.0
class RestApiTest {
    @Autowired
    private lateinit var testRestTemplate: TestRestTemplate
}

// New recommended approach
import org.springframework.boot.test.autoconfigure.web.client.AutoConfigureRestTestClient
import org.springframework.boot.resttestclient.RestTestClient

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@AutoConfigureRestTestClient // New annotation
class RestApiTest {
    @Autowired
    private lateinit var restTestClient: RestTestClient

    @Test
    fun testEndpoint() {
        val response = restTestClient.get()
            .uri("/api/users")
            .retrieve()
            .toEntity<List<User>>()

        assertThat(response.statusCode).isEqualTo(HttpStatus.OK)
    }
}
```

**TestRestTemplate 包更改（如果仍在使用）：**

**重要提示：** 如果继续使用 `TestRestTemplate`，您必须：
1. 添加 `spring-boot-resttestclient` 测试依赖项
2. **更新包导入**（类移至新包）

**libs.versions.toml：**
```toml
[libraries]
spring-boot-resttestclient = { module = "org.springframework.boot:spring-boot-resttestclient", version.ref = "springBoot" }
```

**构建.gradle.kts：**
```kotlin
dependencies {
    testImplementation(libs.spring.boot.resttestclient)
}
```

**更新包导入（必需）：**
```kotlin
// Old package import - will cause compilation failure
// import org.springframework.boot.test.web.client.TestRestTemplate

// New package import - required in Spring Boot 4.0
import org.springframework.boot.resttestclient.TestRestTemplate
```

### @PropertyMapping注解重定位

```kotlin
// Old (Spring Boot 3.x)
import org.springframework.boot.test.autoconfigure.properties.PropertyMapping
import org.springframework.boot.test.autoconfigure.properties.Skip

// New (Spring Boot 4.0)
import org.springframework.boot.test.context.PropertyMapping
import org.springframework.boot.test.context.PropertyMapping.Skip
```

## 生产就绪的功能和模块

### 运行状况、指标和可观察性模块

Spring Boot 4.0 将生产就绪功能模块化为重点模块：

**libs.versions.toml：**
```toml
[libraries]
# Health monitoring
spring-boot-health = { module = "org.springframework.boot:spring-boot-health", version.ref = "springBoot" }

# Micrometer metrics
spring-boot-micrometer-metrics = { module = "org.springframework.boot:spring-boot-micrometer-metrics", version.ref = "springBoot" }
spring-boot-micrometer-metrics-test = { module = "org.springframework.boot:spring-boot-micrometer-metrics-test", version.ref = "springBoot" }

# Micrometer observation
spring-boot-micrometer-observation = { module = "org.springframework.boot:spring-boot-micrometer-observation", version.ref = "springBoot" }

# Distributed tracing
spring-boot-micrometer-tracing = { module = "org.springframework.boot:spring-boot-micrometer-tracing", version.ref = "springBoot" }
spring-boot-micrometer-tracing-test = { module = "org.springframework.boot:spring-boot-micrometer-tracing-test", version.ref = "springBoot" }
spring-boot-micrometer-tracing-brave = { module = "org.springframework.boot:spring-boot-micrometer-tracing-brave", version.ref = "springBoot" }
spring-boot-micrometer-tracing-opentelemetry = { module = "org.springframework.boot:spring-boot-micrometer-tracing-opentelemetry", version.ref = "springBoot" }

# OpenTelemetry integration
spring-boot-opentelemetry = { module = "org.springframework.boot:spring-boot-opentelemetry", version.ref = "springBoot" }

# Zipkin reporter
spring-boot-zipkin = { module = "org.springframework.boot:spring-boot-zipkin", version.ref = "springBoot" }
```

**build.gradle.kts（示例可观测性堆栈）：**
```kotlin
dependencies {
    // Actuator with metrics and tracing
    implementation(libs.spring.boot.starter.actuator)
    implementation(libs.spring.boot.micrometer.observation)
    implementation(libs.spring.boot.micrometer.tracing.opentelemetry)
    implementation(libs.spring.boot.opentelemetry)

    // Test support
    testImplementation(libs.spring.boot.micrometer.metrics.test)
    testImplementation(libs.spring.boot.micrometer.tracing.test)
}
```

**注意：** 大多数使用启动器（例如 `spring-boot-starter-actuator`）的应用程序不需要直接声明这些模块。使用直接模块依赖关系进行细粒度控制。

## 执行器的变化

### 默认情况下启用运行状况探测

活跃度和就绪度探测现在**默认启用**。

**application.yml（如果需要则禁用）：**
```yaml
management:
  endpoint:
    health:
      probes:
        enabled: false # Disable if not using Kubernetes probes
```

**自动暴露：**
- __代码0__
- __代码0__

## 构建配置

### Kotlin 编译器配置

**构建.gradle.kts：**
```kotlin
import org.jetbrains.kotlin.gradle.tasks.KotlinCompile

plugins {
    kotlin("jvm") version "2.2.0" // Minimum 2.2.0
    kotlin("plugin.spring") version "2.2.0"
    kotlin("plugin.jpa") version "2.2.0"
    id("org.springframework.boot") version "4.0.0"
    id("io.spring.dependency-management") version "1.1.7"
}

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(21) // Or 17, 25
    }
}

kotlin {
    compilerOptions {
        freeCompilerArgs.addAll(
            "-Xjsr305=strict", // Strict null-safety
            "-Xemit-jvm-type-annotations" // Emit type annotations
        )
    }
}

tasks.withType<KotlinCompile> {
    kotlinOptions {
        jvmTarget = "21" // Match Java toolchain
    }
}

tasks.withType<Test> {
    useJUnitPlatform()
}
```

### Java 预览功能（如果使用 Java 25）

**构建.gradle.kts：**
```kotlin
tasks.withType<JavaCompile> {
    options.compilerArgs.add("--enable-preview")
}

tasks.withType<Test> {
    jvmArgs("--enable-preview")
}

tasks.withType<JavaExec> {
    jvmArgs("--enable-preview")
}
```

## 迁移清单

### 预迁移

- [ ] 升级到最新的 Spring Boot 3.5.x
- [ ] 检查并修复所有弃用警告
- [ ] 记录当前依赖版本
- [ ] 运行完整的测试套件并验证绿色构建
- [ ] 回顾 [Spring Boot 3.5.x → 4.0 依赖项更改](https://docs.spring.io/spring-boot/4.0/appendix/dependency-versions/coordinates.html)

### 核心迁移

- [ ] 使用 Spring Boot 4.0.0 更新 `libs.versions.toml`
- [ ] 将 Kotlin 版本更新至 2.2.0+
- [ ] 重命名起始符：`spring-boot-starter-web` → `spring-boot-starter-webmvc` 等。
- [ ] 添加特定于技术的测试启动器（或暂时使用经典启动器）
- [ ] 删除 Undertow 依赖项（如果存在）（切换到 Tomcat/Jetty）
- [ ] 删除 `spring-session-hazelcast` / `spring-session-mongodb` 或添加显式版本

### 杰克逊3号迁移

- [ ] 更新导入：`com.fasterxml.jackson` → `tools.jackson`
- [ ] 更新异常：`jackson-annotations` 仍然使用 `com.fasterxml.jackson.core`
- [ ] 重命名：`@JsonComponent` → `@JacksonComponent`
- [ ] 重命名：`Jackson2ObjectMapperBuilderCustomizer` → `JsonMapperBuilderCustomizer`
- [ ] 更新属性：`spring.jackson.read.*` → `spring.jackson.json.read.*`
- [ ] 如果需要，请考虑临时 `spring-boot-jackson2` 模块

### 物业更新

- [ ] MongoDB: `spring.data.mongodb.*` → `spring.mongodb.*` （对于非 Spring Data 属性）
- [ ] 会话：`spring.session.redis.*` → `spring.session.data.redis.*`
- [ ] 持久性：`spring.dao.exceptiontranslation` → `spring.persistence.exceptiontranslation`
- [ ] 卡夫卡重试：`backoff.random` → `backoff.jitter`

### 代码更新

- [ ] 更新包：`BootstrapRegistry` → `org.springframework.boot.bootstrap.BootstrapRegistry`
- [ ] 更新包：`EnvironmentPostProcessor` → `org.springframework.boot.EnvironmentPostProcessor`
- [ ] 更新包：`EntityScan` → `org.springframework.boot.persistence.autoconfigure.EntityScan`
- [ ] 更新：`RestClient` → `Rest5Client` (Elasticsearch)
- [ ] 更新：`StreamBuilderFactoryBeanCustomizer` → `StreamsBuilderFactoryBeanConfigurer` (Kafka)
- [ ] 分割：`RabbitRetryTemplateCustomizer` → `RabbitTemplateRetrySettingsCustomizer` / `RabbitListenerRetrySettingsCustomizer`
- [ ] 替换：`HttpMessageConverters` → `ClientHttpMessageConvertersCustomizer` / `ServerHttpMessageConvertersCustomizer`
- [ ] 更新：如果需要 null 处理，则 `PropertyMapper` 与 `.always()` 一起使用

### 测试更新

- [ ] 使用 `@Mock` / `@Captor` 将 `@ExtendWith(MockitoExtension::class)` 添加到测试中
- [ ] 使用 `MockMvc` 将 `@AutoConfigureMockMvc` 添加到测试中
- [ ] 使用 `WebTestClient` 将 `@AutoConfigureWebTestClient` 添加到测试中
- [ ] 迁移 `TestRestTemplate` → `RestTestClient` （或添加 `@AutoConfigureTestRestTemplate`）
- [ ] 更新：`@PropertyMapping` 导入 → `org.springframework.boot.test.context`

### 构建配置

- [ ] 将 Gradle 更新到 8.5+
- [ ] 将 Gradle CycloneDX 插件更新至 3.0.0+
- [ ] 查看 uber jar 中包含的可选依赖项
- [ ] 删除 `loaderImplementation = CLASSIC`（如果存在）
- [ ] 删除 `launchScript()` 配置（如果存在）

### 验证

- [ ] 运行 `./gradlew clean build`
- [ ] 运行完整的测试套件
- [ ] 使用 TestContainers 验证集成测试
- [ ] 检查新的 Kotlin 空安全警告
- [ ] 测试 Spring Boot Actuator 端点
- [ ] 验证运行状况探测（`/actuator/health/liveness`、`/actuator/health/readiness`）
- [ ] 使用新默认值进行性能测试

### 迁移后

- [ ] 查看 Spring Boot 4.0 发行说明以了解其他功能
- [ ] 考虑采用新的 Spring Framework 7.0 功能
- [ ] 计划从经典启动器迁移（如果使用）
- [ ] 计划从 `spring-boot-jackson2` 模块迁移（如果使用）
- [ ] 更新 CI/CD 管道以满足 Java 17+ 要求
- [ ] 更新部署清单（Servlet 6.1 容器）

## 常见陷阱

1. **经典启动器**：记住这些已被弃用 - 计划迁移到特定于技术的启动器
2. **Undertow**：完全删除，没有解决方法 - 必须使用 Tomcat 或 Jetty
3. **Jackson 3 软件包**：很容易错过 `jackson-annotations` 仍然使用旧的组 ID
4. **MongoDB 属性**：许多已移至 `spring.mongodb.*`，但有些仍保留在 `spring.data.mongodb.*` 中
5. **测试配置**：`@SpringBootTest` 不再自动配置 MockMVC/WebTestClient/TestRestTemplate
6. **Kotlin 2.2**：所需的最低版本 - 旧版本将无法工作
7. **空安全**：JSpecify 注释可能会在 Kotlin 中出现新警告
8. **PropertyMapper**：空处理的行为变化 - 审查用法
9. **Jersey + Jackson 3**：不兼容 - 使用 `spring-boot-jackson2` 模块
10. **运行状况探测**：现在默认启用 - 可能会影响非 Kubernetes 部署

## 性能考虑因素

- **模块化启动器**：使用特定于技术的启动器，JAR 更小，启动速度更快
- **Spring Framework 7**：核心框架的性能改进
- **Jackson 3**：改进了 JSON 处理性能
- **虚拟线程**：考虑使用 Java 21+ (`spring.threads.virtual.enabled=true`) 启用

## 资源

- [Spring Boot 4.0 迁移指南](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide)
- [Spring Boot 4.0 发行说明](https://github.com/spring-projects/spring-boot/releases)
- [Spring 框架 7.0 文档](https://docs.spring.io/spring-framework/reference/)
- [Jackson 3 迁移指南](https://github.com/FasterXML/jackson/wiki/Jackson-3.0-Migration-Guide)
- [Kotlin 2.2 发行说明](https://kotlinlang.org/docs/whatsnew22.html)

---
