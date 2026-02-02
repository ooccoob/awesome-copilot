---
description: 'Step-by-step guide for converting Spring Boot Cassandra applications to use Azure Cosmos DB with Spring Data Cosmos'
applyTo: '**/*.java,**/pom.xml,**/build.gradle,**/application*.properties,**/application*.yml,**/application*.conf'
---

# 综合指南：将 Spring Boot Cassandra 应用程序转换为结合使用 Azure Cosmos DB 和 Spring Data Cosmos (spring-data-cosmos)

## 适用性

本指南适用于：
- ✅ Spring Boot 2.x - 3.x 应用程序（反应式和非反应式）
- ✅ 基于 Maven 和 Gradle 的项目
- ✅ 使用 Spring Data Cassandra、Cassandra DAO 或 DataStax 驱动程序的应用程序
- ✅ 有或没有 Lombok 的项目
- ✅ 基于 UUID 或基于字符串的实体标识符
- ✅ 同步和反应式（Spring WebFlux）应用程序

本指南不涵盖：
- ❌ 非 Spring 框架（Jakarta EE、Micronaut、Quarkus、plain Java）
- ❌ 复杂的 Cassandra 功能（物化视图、UDT、计数器、自定义类型）
- ❌ 批量数据迁移（仅代码转换——数据必须单独迁移）
- ❌ Cassandra 特定的功能，例如轻量级事务 (LWT) 或跨分区的批量操作

## 概述

本指南提供了使用 Spring Data Cosmos 将反应式 Spring Boot 应用程序从 Apache Cassandra 转换为 Azure Cosmos DB 的分步说明。它涵盖了基于实际转换经验的所有主要问题及其解决方案。

## 先决条件

- Java 11 或更高版本（Spring Boot 3.x 需要 Java 17+）
- Azure CLI 已安装并经过身份验证 (`az login`) 以进行本地开发
- 在 Azure 门户中创建的 Azure Cosmos DB 帐户
- Maven 3.6+ 或 Gradle 6+（取决于您的项目）
- 对于使用 Spring Boot 3.x 的 Gradle 项目：确保 JAVA_HOME 环境变量指向 Java 17+
- 对应用程序的数据模型和查询模式有基本的了解

## Azure Cosmos DB 的数据库设置

**关键**：在运行应用程序之前，请确保数据库存在于您的 Cosmos DB 帐户中。

### 选项 1：手动创建数据库（建议首次运行）
1. 转到 Azure 门户 → 您的 Cosmos DB 帐户
2. 导航至“数据浏览器”
3. 点击“新建数据库”
4. 输入与您的应用程序配置匹配的数据库名称（检查 `application.properties` 或 `application.yml` 以获取配置的数据库名称）
5. 选择吞吐量设置（根据您的需要手动或自动缩放）
   - 从手动 400 RU/s 开始进行开发/测试
   - 使用 Autoscale 处理流量可变的生产工作负载
6. 单击“确定”

### 选项 2：自动创建
Spring Data Cosmos 可以在第一次连接时自动创建数据库，但这需要：
- 适当的 RBAC 权限（Cosmos DB 内置数据贡献者角色）
- 如果权限不足可能会失败

### 容器（集合）创建
当应用程序启动时，Spring Data Cosmos 将使用实体中的 `@Container` 注释设置自动创建容器。除非您想要配置特定的吞吐量或索引策略，否则不需要手动创建容器。

## 使用 Azure Cosmos DB 进行身份验证

### 使用 DefaultAzureCredential（推荐）
`DefaultAzureCredential` 身份验证方法是开发和生产的推荐方法：

**它是如何工作的**：
1. 按顺序尝试多个凭据源：
   - 环境变量
   - 工作负载身份（适用于 AKS）
   - 托管身份（适用于 Azure VM/应用服务）
   - Azure CLI (`az login`)
   - Azure PowerShell
   - Azure 开发人员 CLI

**本地开发设置**：
```bash
# Login via Azure CLI
az login

# The application will automatically use your CLI credentials
```

**配置**（无需密钥）：
```java
@Bean
public CosmosClientBuilder getCosmosClientBuilder() {
    return new CosmosClientBuilder()
        .endpoint(uri)
        .credential(new DefaultAzureCredentialBuilder().build());
}
```

**属性文件**（application-cosmos.properties 或 application.properties）：
```properties
azure.cosmos.uri=https://<your-cosmos-account-name>.documents.azure.com:443/
azure.cosmos.database=<your-database-name>
# No key property needed when using DefaultAzureCredential
azure.cosmos.populate-query-metrics=false
```

**注意**：将 `<your-cosmos-account-name>` 和 `<your-database-name>` 替换为您的实际值。

### 所需的 RBAC 权限
使用 DefaultAzureCredential 时，您的 Azure 身份需要适当的 RBAC 权限：

**常见启动错误**：
```
Request blocked by Auth: Request for Read DatabaseAccount is blocked because principal
[xxx] does not have required RBAC permissions to perform action
[Microsoft.DocumentDB/databaseAccounts/sqlDatabases/write] on any scope.
```

**解决方案**：分配“Cosmos DB 内置数据贡献者”角色：
```bash
# Get your user's object ID
PRINCIPAL_ID=$(az ad signed-in-user show --query id -o tsv)

# Assign the role (replace <resource-group> with your actual resource group)
az cosmosdb sql role assignment create \
  --account-name your-cosmos-account \
  --resource-group <resource-group> \
  --scope "/" \
  --principal-id $PRINCIPAL_ID \
  --role-definition-name "Cosmos DB Built-in Data Contributor"
```

**替代**：如果您使用 `az login` 登录，并且您是 Cosmos DB 帐户的所有者/贡献者，则您的帐户应该已经拥有权限。

### 基于密钥的身份验证（仅限本地模拟器）
仅对本地模拟器开发使用基于密钥的身份验证：

```java
@Bean
public CosmosClientBuilder getCosmosClientBuilder() {
    // Only for local emulator
    if (key != null && !key.isEmpty()) {
        return new CosmosClientBuilder()
            .endpoint(uri)
            .key(key);
    }
    // Production: use DefaultAzureCredential
    return new CosmosClientBuilder()
        .endpoint(uri)
        .credential(new DefaultAzureCredentialBuilder().build());
}
```

## 吸取的重要教训

### Java版本要求（Spring Boot 3.x）
**问题**：Spring Boot 3.0+ 需要 Java 17 或更高版本。使用 Java 11 会导致构建失败。
**错误**：
```
No matching variant of org.springframework.boot:spring-boot-gradle-plugin:3.0.5 was found.
Incompatible because this component declares a component compatible with Java 17
and the consumer needed a component compatible with Java 11
```

**解决方案**：
```bash
# Check Java version
java -version

# Set JAVA_HOME to Java 17+
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64  # Linux
# or
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-17.jdk/Contents/Home  # macOS

# Verify
echo $JAVA_HOME
```

**对于 Gradle 项目**，始终使用正确的 JAVA_HOME 运行：
```bash
export JAVA_HOME=/path/to/java-17
./gradlew clean build
./gradlew bootRun
```

### Gradle 特定问题

#### 问题一：旧配置文件冲突
**问题**：重命名或替换Cassandra配置文件时，旧文件可能仍然存在，导致编译错误：
```
error: class CosmosConfiguration is public, should be declared in a file named CosmosConfiguration.java
```

**解决方案**：显式删除旧的 Cassandra 配置文件：
```bash
# Find and remove old Cassandra config files
find src/main/java -name "*CassandraConfig*.java" -o -name "*CassandraConfiguration*.java"
# Review the output, then delete if appropriate
rm src/main/java/<path-to-old-config>/CassandraConfig.java
```

#### 问题 2：存储库 findAllById 返回 Iterable
**问题**：CosmosRepository 的 `findAllById()` 返回 `Iterable<Entity>`，而不是 `List<Entity>`。直接调用 `.stream()` 失败：
```
error: cannot find symbol
  symbol:   method stream()
  location: interface Iterable<YourEntity>
```

**解决方案**：正确处理Iterable：
```java
// WRONG - Iterable doesn't have stream() method
var entities = repository.findAllById(ids).stream()...

// CORRECT - Option 1: Use forEach to populate a collection
Iterable<YourEntity> entitiesIterable = repository.findAllById(ids);
Map<String, YourEntity> entityMap = new HashMap<>();
entitiesIterable.forEach(entity -> entityMap.put(entity.getId(), entity));

// CORRECT - Option 2: Convert to List first
List<YourEntity> entities = new ArrayList<>();
repository.findAllById(ids).forEach(entities::add);

// CORRECT - Option 3: Use StreamSupport (Java 8+)
List<YourEntity> entities = StreamSupport.stream(
    repository.findAllById(ids).spliterator(), false)
    .collect(Collectors.toList());
```

### package-info.java javax.annotation 问题
**问题**： `package-info.java` 使用 `javax.annotation.ParametersAreNonnullByDefault` 会导致 Java 11+ 中的编译错误：
```
error: cannot find symbol
import javax.annotation.ParametersAreNonnullByDefault;
```

**解决方案**：删除或简化package-info.java文件：
```java
// Simple version - just package declaration
package com.your.package;
```

### 实体构造函数问题
**问题**：将 Lombok `@NoArgsConstructor` 与手动构造函数一起使用会导致重复的构造函数编译错误。
**解决方案**：选择一种方法：
- 选项 1：删除 `@NoArgsConstructor` 并保留手动构造函数
- 选项 2：删除手动构造函数并依赖 Lombok 注释
- **最佳实践**：对于具有初始化逻辑（例如设置分区键）的 Cosmos 实体，删除 `@NoArgsConstructor` 并仅使用手动构造函数。

### 业务对象构造函数删除
**问题**：从实体类中删除 `@AllArgsConstructor` 或自定义构造函数会破坏使用这些构造函数的现有代码。
**影响**：映射实用程序、数据播种器和测试文件将无法编译。
**解决方案**：
- 删除或修改构造函数后，搜索所有文件以查找对这些实体的构造函数调用
- 替换为默认构造函数 + setter 模式：
  ```java
  // Before - using all-args constructor
  MyEntity entity = new MyEntity(id, field1, field2, field3);

  // After - using default constructor + setters
  MyEntity entity = new MyEntity();
  entity.setId(id);
  entity.setField1(field1);
  entity.setField2(field2);
  entity.setField3(field3);
  ```
### 数据播种器构造函数调用
**问题**：数据播种或初始化代码使用的实体构造函数在实体转换为 Cosmos 注释后可能不存在。
**解决方案**：更新数据播种组件中的所有实体实例以使用 setter：
```java
// Before - constructor-based initialization
MyEntity entity1 = new MyEntity("entity-1", "value1", "value2");

// After - setter-based initialization
MyEntity entity1 = new MyEntity();
entity1.setId("entity-1");
entity1.setField1("value1");
entity1.setField2("value2");
```

**要检查的常用文件**：DataSeeder、DatabaseInitializer、TestDataLoader 或任何实现 `CommandLineRunner` 的 `@Component`
```java
OwnerEntity owner1 = new OwnerEntity();
owner1.setId("owner-1");
```

### 需要更新测试文件
**问题**：测试文件引用旧的 Cassandra DAO 并使用 UUID 构造函数。
**要更新的关键文件**：
1. 删除 `MockReactiveResultSet.java` （Cassandra 特定）
2. 更新 `*ReactiveServicesTest.java` - 用 Cosmos 存储库替换 DAO 引用
3. 更新 `*ReactiveControllerTest.java` - 用 Cosmos 存储库替换 DAO 引用
4. 将所有 `UUID.fromString()` 替换为字符串 ID
5. 用 setter 模式替换构造函数调用： `new Owner(UUID.fromString(...))`

### 应用程序启动和默认AzureCredential行为
**重要**：DefaultAzureCredential 会按顺序尝试多种身份验证方法，这是正常的且符合预期。

**预期的启动日志模式**：
```
INFO c.azure.identity.ChainedTokenCredential : Azure Identity => Attempted credential EnvironmentCredential is unavailable.
INFO c.azure.identity.ChainedTokenCredential : Azure Identity => Attempted credential WorkloadIdentityCredential is unavailable.
INFO c.azure.identity.ChainedTokenCredential : Azure Identity => Attempted credential ManagedIdentityCredential is unavailable.
INFO c.azure.identity.ChainedTokenCredential : Azure Identity => Attempted credential SharedTokenCacheCredential is unavailable.
INFO c.azure.identity.ChainedTokenCredential : Azure Identity => Attempted credential IntelliJCredential is unavailable.
INFO c.azure.identity.ChainedTokenCredential : Azure Identity => Attempted credential AzureCliCredential is unavailable.
INFO c.azure.identity.ChainedTokenCredential : Azure Identity => Attempted credential AzurePowerShellCredential is unavailable.
INFO c.azure.identity.ChainedTokenCredential : Azure Identity => Attempted credential AzureDeveloperCliCredential returns a token
```

**要点**：
- “不可用”消息是 **正常** - 它正在按顺序尝试每个凭据源
- 一旦它找到一个有效的（例如，AzureCliCredential 或 AzureDeveloperCliCredential），它将使用它
- **不要中断启动过程** - 循环凭证源需要 10-15 秒
- 应用程序通常需要 30-60 秒才能完全启动并连接到 Cosmos DB

**成功指标**：
```
INFO c.a.c.i.RxDocumentClientImpl : Initializing DocumentClient [1] with serviceEndpoint [https://your-account.documents.azure.com:443/]
INFO c.a.c.i.GlobalEndpointManager : db account retrieved {...}
INFO c.a.c.implementation.SessionContainer : Registering a new collection resourceId [...]
INFO o.s.b.w.embedded.tomcat.TomcatWebServer : Tomcat started on port(s): 8944 (http)
INFO com.your.app.Application : Started Application in X.XXX seconds
```

**启动失败故障排除**：

1. **如果所有凭证均“不可用”**：
   ```bash
   # Re-authenticate with Azure CLI
   az login

   # Verify login
   az account show
   ```

2. **如果您看到权限错误**：
   ```
   Request blocked by Auth: principal [xxx] does not have required RBAC permissions
   ```
   - 确保 Cosmos DB 帐户中存在数据库（请参阅数据库设置部分）
   - 验证 RBAC 权限（请参阅身份验证部分）
   - 检查您是否登录到正确的 Azure 订阅

3. **端口已在使用**：
   ```bash
   # Find and kill the process
   lsof -ti:8944 | xargs kill -9

   # Or change the port in application.properties
   server.port=8945
   ```

### 应用程序启动耐心
**问题**：应用程序需要 30-60 秒才能完全启动（编译 + Spring Boot + Cosmos DB 连接）。
**解决方案**：
- 对于 Gradle： `./gradlew bootRun` （默认在前台运行）
- 对于 Maven：`mvn spring-boot:run`
- 如果需要，请使用后台执行：`nohup ./gradlew bootRun > app.log 2>&1 &`
- **关键**：不要中断启动过程，特别是在凭证身份验证期间（10-15 秒）
- 监视日志：`tail -f app.log` 或检查“已启动应用程序”消息
- 在测试端点之前等待 Tomcat 启动并显示端口号

### 端口配置
**问题**：应用程序可能无法在默认端口 8080 上运行。
**解决方案**：
- 检查实际端口：`ss -tlnp | grep java`
- 测试连接：`curl http://localhost:<port>/petclinic/api/owners`
- 常用端口：8080、9966、9967

## 系统编译错误解决

在此转换过程中，我们遇到了 100 多个编译错误。以下是解决这些问题的系统方法：

### 第 1 步：识别残留 Cassandra 文件
**问题**：旧的 Cassandra 特定文件在删除依赖项后会导致编译错误。
**解决方案**：系统地删除所有 Cassandra 特定文件：

```bash
# Identify and delete old DAOs
find . -name "*Dao.java" -o -name "*DAO.java"
# Delete: OwnerReactiveDao, PetReactiveDao, VetReactiveDao, VisitReactiveDao

# Identify and delete Cassandra mappers
find . -name "*Mapper.java" -o -name "*EntityToOwnerMapper.java"
# Delete: EntityToOwnerMapper, EntityToPetMapper, EntityToVetMapper, EntityToVisitMapper

# Identify and delete old configuration
find . -name "*CassandraConfig.java" -o -name "CassandraConfiguration.java"
# Delete: CassandraConfiguration.java

# Identify test utilities for Cassandra
find . -name "MockReactiveResultSet.java"
# Delete: MockReactiveResultSet.java (Cassandra-specific test utility)
```

### 第 2 步：运行增量编译检查
**方法**：每次重大更改后，进行编译以确定剩余问题：

```bash
# After deleting old files
mvn compile 2>&1 | grep -E "(ERROR|error)" | wc -l
# Expected: Number decreases with each fix

# After updating entity constructors
mvn compile 2>&1 | grep "constructor"
# Identify constructor-related compilation errors

# After fixing business object constructors
mvn compile 2>&1 | grep -E "(new Owner|new Pet|new Vet|new Visit)"
# Identify remaining constructor calls that need fixing
```

### 第 3 步：系统地修复与构造函数相关的错误
**模式**：搜索特定文件类型中的所有构造函数调用：

```bash
# Find all constructor calls in MappingUtils
grep -n "new Owner\|new Pet\|new Vet\|new Visit" src/main/java/**/MappingUtils.java

# Find all constructor calls in DataSeeder
grep -n "new OwnerEntity\|new PetEntity\|new VetEntity\|new VisitEntity" src/main/java/**/DataSeeder.java

# Find all constructor calls in test files
grep -rn "new Owner\|new Pet\|new Vet\|new Visit" src/test/java/
```

### 第 4 步：最后更新测试
**基本原理**：在测试代码之前修复应用程序代码，以便清楚地看到所有问题：

1. 第一：更新测试存储库模拟（DAO → Cosmos 存储库）
2. 第二：修复测试数据中的 UUID → String 转换
3. 第三：更新测试设置中的构造函数调用
4. 最后：运行测试来验证：`mvn test`

### 第 5 步：验证零编译错误
**最终检查**：
```bash
# Clean and full compile
mvn clean compile

# Should see: BUILD SUCCESS
# Should NOT see any ERROR messages

# Verify test compilation
mvn test-compile

# Run tests
mvn test
```

**成功指标**：
- `mvn compile`：取得成功
- `mvn test`：所有测试都通过（即使某些测试被跳过）
- 输出中没有错误消息
- 没有“找不到符号”错误
- 没有“构造函数无法应用”错误

## 转换步骤

### 1.更新Maven依赖关系

#### 删除 Cassandra 依赖项
```xml
<!-- REMOVE these Cassandra dependencies -->
<dependency>
    <groupId>com.datastax.oss</groupId>
    <artifactId>java-driver-core</artifactId>
</dependency>
<dependency>
    <groupId>com.datastax.oss</groupId>
    <artifactId>java-driver-query-builder</artifactId>
</dependency>
```

#### 添加 Azure Cosmos 依赖项
```xml
<!-- Azure Spring Data Cosmos (Java 11 compatible) -->
<dependency>
    <groupId>com.azure</groupId>
    <artifactId>azure-spring-data-cosmos</artifactId>
    <version>3.46.0</version>
</dependency>

<!-- Azure Identity for DefaultAzureCredential authentication -->
<dependency>
    <groupId>com.azure</groupId>
    <artifactId>azure-identity</artifactId>
    <version>1.11.4</version>
</dependency>
```

#### 关键：添加版本管理以实现兼容性
Spring Boot 2.3.x 与 Azure 库存在版本冲突。将其添加到您的 `<dependencyManagement>` 部分：

```xml
<dependencyManagement>
    <dependencies>
        <!-- Override reactor-netty version to fix compatibility with azure-spring-data-cosmos -->
        <dependency>
            <groupId>io.projectreactor.netty</groupId>
            <artifactId>reactor-netty</artifactId>
            <version>1.0.40</version>
        </dependency>
        <dependency>
            <groupId>io.projectreactor.netty</groupId>
            <artifactId>reactor-netty-http</artifactId>
            <version>1.0.40</version>
        </dependency>
        <dependency>
            <groupId>io.projectreactor.netty</groupId>
            <artifactId>reactor-netty-core</artifactId>
            <version>1.0.40</version>
        </dependency>

        <!-- Override reactor-core version to support Sinks API required by azure-identity -->
        <dependency>
            <groupId>io.projectreactor</groupId>
            <artifactId>reactor-core</artifactId>
            <version>3.4.32</version>
        </dependency>

        <!-- Override Netty versions to fix compatibility with Azure Cosmos Client -->
        <dependency>
            <groupId>io.netty</groupId>
            <artifactId>netty-bom</artifactId>
            <version>4.1.101.Final</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>

        <!-- Override netty-tcnative to match Netty version -->
        <dependency>
            <groupId>io.netty</groupId>
            <artifactId>netty-tcnative-boringssl-static</artifactId>
            <version>2.0.62.Final</version>
        </dependency>
    </dependencies>
</dependencyManagement>
```

### 2. 配置设置

#### 创建 Cosmos 配置类
将您的 Cassandra 配置替换为：

```java
@Configuration
@EnableCosmosRepositories  // Required for non-reactive repositories
@EnableReactiveCosmosRepositories  // CRITICAL: Required for reactive repositories
public class CosmosConfiguration extends AbstractCosmosConfiguration {

    @Value("${azure.cosmos.uri}")
    private String uri;

    @Value("${azure.cosmos.database}")
    private String database;

    @Bean
    public CosmosClientBuilder getCosmosClientBuilder() {
        return new CosmosClientBuilder()
            .endpoint(uri)
            .credential(new DefaultAzureCredential());
    }

    @Bean
    public CosmosAsyncClient cosmosAsyncClient(CosmosClientBuilder cosmosClientBuilder) {
        return cosmosClientBuilder.buildAsyncClient();
    }

    @Bean
    public CosmosClientBuilderFactory cosmosFactory(CosmosAsyncClient cosmosAsyncClient) {
        return new CosmosClientBuilderFactory(cosmosAsyncClient);
    }

    @Bean
    public ReactiveCosmosTemplate reactiveCosmosTemplate(CosmosClientBuilderFactory cosmosClientBuilderFactory) {
        return new ReactiveCosmosTemplate(cosmosClientBuilderFactory, database);
    }

    @Override
    protected String getDatabaseName() {
        return database;
    }
}
```

**重要说明：**
- **需要两个注释**：@EnableCosmosRepositories 和 @EnableReactiveCosmosRepositories
- 缺少 @EnableReactiveCosmosRepositories 将导致反应式存储库出现“无合格 bean”错误

#### 应用程序属性
添加cosmos配置文件配置：

```properties
# application-cosmos.properties
azure.cosmos.uri=https://your-cosmos-account.documents.azure.com:443/
azure.cosmos.database=your-database-name
```

### 3. 实体转换

#### 从 Cassandra 转换为 Cosmos 注解

**之前（卡桑德拉）：**
```java
@Table(value = "entity_table")
public class EntityName {
    @PartitionKey
    private UUID id;

    @ClusteringColumn
    private String fieldName;

    @Column("column_name")
    private String anotherField;
}
```

**之后（宇宙）：**
```java
@Container(containerName = "entities")
public class EntityName {
    @Id
    private String id;  // Changed from UUID to String

    @PartitionKey
    private String fieldName;  // Choose appropriate partition key

    private String anotherField;

    // Generate String IDs
    public EntityName() {
        this.id = UUID.randomUUID().toString();
    }
}
```

#### 主要变化：
- 将 `@Table` 替换为 `@Container(containerName = "...")`
- 将 `@PartitionKey` 更改为 Cosmos 分区键策略
- 将所有 ID 从 `UUID` 转换为 `String`
- 删除 `@Column` 注释（Cosmos 使用字段名称）
- 删除 `@ClusteringColumn` （在 Cosmos 中不适用）

### 4. 存储库转换

#### 使用 Cosmos 存储库替换 Cassandra 数据访问层

**如果您的应用程序使用 DAO 或自定义数据访问类：**

**之前（Cassandra DAO 模式）：**
```java
@Repository
public class EntityReactiveDao {
    // Custom Cassandra query methods
}
```

**之后（Cosmos 存储库）：**
```java
@Repository
public interface EntityCosmosRepository extends ReactiveCosmosRepository<EntityName, String> {

    @Query("SELECT * FROM entities e WHERE e.fieldName = @fieldName")
    Flux<EntityName> findByFieldName(@Param("fieldName") String fieldName);

    @Query("SELECT * FROM entities e WHERE e.id = @id")
    Mono<EntityName> findEntityById(@Param("id") String id);
}
```

**如果您的应用程序使用 Spring Data Cassandra 存储库：**

**之前：**
```java
@Repository
public interface EntityCassandraRepository extends ReactiveCassandraRepository<EntityName, UUID> {
    // Cassandra-specific methods
}
```

**之后：**
```java
@Repository
public interface EntityCosmosRepository extends ReactiveCosmosRepository<EntityName, String> {
    // Convert existing methods to Cosmos queries
}
```

**如果您的应用程序使用直接 CqlSession 或 Cassandra 驱动程序：**
- 用存储库模式替换直接驱动程序调用
- 将 CQL 查询转换为 Cosmos SQL 语法
- 实现存储库接口，如上所示

#### 要点：
- **关键**：使用 `ReactiveCosmosRepository<Entity, String>` 进行反应式编程（不是 CosmosRepository）
- 对于非反应式应用程序使用 `CosmosRepository<Entity, String>`
- **存储库接口更改**：如果从现有 Cassandra 存储库/DAO 进行转换，请确保所有存储库接口都扩展 ReactiveCosmosRepository
- **常见错误**：“没有 ReactiveCosmosRepository 类型的合格 bean”= 缺少@EnableReactiveCosmosRepositories
- **如果使用自定义数据访问类**：转换为存储库模式以实现更好的集成
- **如果已经使用 Spring Data**：将接口扩展从 ReactiveCassandraRepository 更改为 ReactiveCosmosRepository
- 使用类似 SQL 的语法（不是 CQL）通过 `@Query` 注释实现自定义查询
- 所有查询参数必须使用 `@Param` 注释

### 5. 服务层更新

#### 更新反应式编程的服务类（如果适用）

**如果您的应用程序有服务层：**

**关键**：服务方法必须返回 Flux/Mono，而不是 Iterable/Optional

```java
@Service
public class EntityReactiveServices {
    private final EntityCosmosRepository repository;

    public EntityReactiveServices(EntityCosmosRepository repository) {
        this.repository = repository;
    }

    // CORRECT: Returns Flux<EntityName>
    public Flux<EntityName> findAll() {
        return repository.findAll();
    }

    // CORRECT: Returns Mono<EntityName>
    public Mono<EntityName> findById(String id) {
        return repository.findById(id);
    }

    // CORRECT: Returns Mono<EntityName>
    public Mono<EntityName> save(EntityName entity) {
        return repository.save(entity);
    }

    // Custom queries - MUST return Flux/Mono
    public Flux<EntityName> findByFieldName(String fieldName) {
        return repository.findByFieldName(fieldName);
    }

    // WRONG PATTERNS TO AVOID:
    // public Iterable<EntityName> findAll() - Will cause compilation errors
    // public Optional<EntityName> findById() - Will cause compilation errors
    // repository.findAll().collectList() - Unnecessary blocking
}
```

**如果您的应用程序在控制器中使用直接存储库注入：**
- 考虑添加服务层以更好地分离关注点
- 更新控制器依赖项以使用新的 Cosmos 存储库
- 确保整个调用链中正确的反应类型处理

**常见问题：**
- **编译错误**：使用 Iterable 返回类型时“无法解析方法”
- **运行时错误**：尝试不必要地调用 .collectList() 或 .block()
- **性能**：阻止反应式流违背了反应式编程的目的

### 6. 控制器更新（如果适用）

#### 更新字符串 ID 的 REST 控制器

**如果您的应用程序有 REST 控制器：**

**之前：**
```java
@GetMapping("/entities/{entityId}")
public Mono<EntityDto> getEntity(@PathVariable UUID entityId) {
    return entityService.findById(entityId);
}
```

**之后：**
```java
@GetMapping("/entities/{entityId}")
public Mono<EntityDto> getEntity(@PathVariable String entityId) {
    return entityService.findById(entityId);
}
```

**如果您的应用程序不使用控制器：**
- 将相同的 UUID → 字符串转换原则应用于您的数据访问层
- 更新接受/返回实体 ID 的任何外部 API 或接口

### 7. 数据映射实用程序（如果适用）

#### 更新域对象和实体之间的映射

**如果您的应用程序使用映射实用程序或转换器：**

```java
public class MappingUtils {

    // Convert domain object to entity
    public static EntityName toEntity(DomainObject domain) {
        EntityName entity = new EntityName();
        entity.setId(domain.getId()); // Now String instead of UUID
        entity.setFieldName(domain.getFieldName());
        entity.setAnotherField(domain.getAnotherField());
        // ... other fields
        return entity;
    }

    // Convert entity to domain object
    public static DomainObject toDomain(EntityName entity) {
        DomainObject domain = new DomainObject();
        domain.setId(entity.getId());
        domain.setFieldName(entity.getFieldName());
        domain.setAnotherField(entity.getAnotherField());
        // ... other fields
        return domain;
    }
}
```

**如果您的应用程序不使用显式映射：**
- 确保整个代码库中 ID 类型的使用保持一致
- 更新任何对象构造或复制逻辑以处理字符串 ID

### 8. 测试更新

#### 更新测试类

**关键**：所有测试文件都必须更新才能使用字符串 ID 和 Cosmos 存储库：

```java
**If your application has unit tests:**

```java
@ExtendWith(MockitoExtension.class)
类 EntityReactiveServicesTest {

    @模拟
    私有 EntityCosmosRepository 实体存储库； // 更新到 Cosmos 存储库

    @InjectMocks
    私有 EntityReactiveServices 实体服务；

    @测试
    无效 testFindById() {
        StringentityId = "测试实体id"; // 从 UUID 更改为 String
        实体名称模拟实体 = new 实体名称();
        mockEntity.setId(entityId);

        when(entityRepository.findById(entityId)).thenReturn(Mono.just(mockEntity));

        StepVerifier.create(entityService.findById(entityId))
            .expectNext(mockEntity)
            .verifyComplete();
    }
}
```

**If your application has integration tests:**
- Update test data setup to use String IDs
- Replace Cassandra test containers with Cosmos DB emulator (if available)
- Update test queries to use Cosmos SQL syntax instead of CQL

**If your application doesn't have tests:**
- Consider adding basic tests to verify the conversion works correctly
- Focus on testing ID conversion and basic CRUD operations
```

### 9. 常见问题及解决方案

#### 问题 1：reactor.core.publisher.Sinks 出现 NoClassDefFoundError
**问题**：Azure Identity 库需要更新的 Reactor Core 版本
**错误**：`java.lang.NoClassDefFoundError: reactor/core/publisher/Sinks`
**根本原因**：Spring Boot 2.3.x 使用没有 Sinks API 的旧版 Reactor-Core
**解决方案**：在 dependencyManagement 中添加reactor-core版本覆盖（参见步骤1）

#### 问题 2：Netty Epoll 方法出现 NoSuchMethodError
**问题**：Spring Boot Netty 和 Azure Cosmos 要求之间的版本不匹配
**错误**：`java.lang.NoSuchMethodError: 'boolean io.netty.channel.epoll.Epoll.isTcpFastOpenClientSideAvailable()'`
**根本原因**：Spring Boot 2.3.x 使用 Netty 4.1.51.Final，Azure 需要更新的方法
**解决方案**：添加 netty-bom 版本覆盖（参见步骤 1）

#### 问题 3：SSL 上下文的 NoSuchMethodError
**问题**：Netty TLS 本机库版本不匹配
**错误**：`java.lang.NoSuchMethodError: 'boolean io.netty.internal.tcnative.SSLContext.setCurvesList(long, java.lang.String[])'`
**根本原因**：netty-tcnative 版本与升级后的 Netty 不兼容
**解决方案**：添加 netty-tcnative-boringssl-static 版本覆盖（参见步骤 1）

#### 问题 4：未创建 ReactiveCosmosRepository bean
**问题**：缺少 @EnableReactiveCosmosRepositories 注释
**错误**：`No qualifying bean of type 'ReactiveCosmosRepository' available`
**根本原因**：只有 @EnableCosmosRepositories 不会创建反应式存储库 bean
**解决方案**：将 @EnableCosmosRepositories 和 @EnableReactiveCosmosRepositories 添加到配置中

#### 问题5：存储库接口编译错误
**问题**：使用 CosmosRepository 而不是 ReactiveCosmosRepository
**错误**：`Cannot resolve method 'findAll()' in 'CosmosRepository'`
**根本原因**：CosmosRepository 返回 Iterable，而不是 Flux
**解决方案**：更改所有存储库接口以扩展 ReactiveCosmosRepository<Entity, String>

#### 问题 6：服务层响应式类型不匹配
**问题**：服务方法返回 Iterable/Optional 而不是 Flux/Mono
**错误**：`Required type: Flux<Entity> Provided: Iterable<Entity>`
**根本原因**：存储库方法返回反应类型，服务必须匹配
**解决方案**：更新所有服务方法签名以返回 Flux/Mono

#### 问题 7：DefaultAzureCredential 身份验证失败
**问题**：DefaultAzureCredential 找不到凭据
**错误**：`All credentials in the chain are unavailable` 或特定凭证不可用消息
**根本原因**：没有可用的有效 Azure 凭据源

**解决方案**：
1. **对于本地开发**：确保 Azure CLI 登录
   ```bash
   az login
   # Verify login
   az account show
   ```

2. **对于 Azure 托管的应用程序**：确保启用托管标识并具有适当的 RBAC 权限

3. **检查凭据链顺序**：DefaultAzureCredential 按以下顺序尝试：
   - 环境变量 → 工作负载身份 → 托管身份 → Azure CLI → PowerShell → 开发人员 CLI

#### 问题 8：未找到数据库错误
**问题**：应用程序无法启动，并出现数据库未找到错误
**错误**：`Database 'your-database-name' not found` 或 `Resource Not Found`
**根本原因**：Cosmos DB 帐户中不存在数据库

**解决方案**：在首次运行之前创建数据库（请参阅数据库设置部分）：
```bash
# Via Azure CLI
az cosmosdb sql database create \
  --account-name your-cosmos-account \
  --name your-database-name \
  --resource-group your-resource-group

# Or via Azure Portal (recommended for first-time setup)
# Portal → Cosmos DB → Data Explorer → New Database
```

**注意**：容器（集合）将从实体 `@Container` 注释自动创建，但数据库本身可能需要首先存在，具体取决于您的 RBAC 权限。

#### 问题 9：RBAC 权限错误
**问题**：应用程序因权限被拒绝错误而失败
**错误**：
```
Request blocked by Auth: principal [xxx] does not have required RBAC permissions
to perform action [Microsoft.DocumentDB/databaseAccounts/sqlDatabases/write]
```

**根本原因**：您的 Azure 身份缺乏所需的 Cosmos DB 权限

**解决方案**：分配“Cosmos DB 内置数据贡献者”角色：
```bash
# Get resource group
RESOURCE_GROUP=$(az cosmosdb show --name your-cosmos-account --query resourceGroup -o tsv 2>/dev/null)

# If the above fails, list all Cosmos accounts to find it
az cosmosdb list --query "[?name=='your-cosmos-account'].{name:name, resourceGroup:resourceGroup}" -o table

# Assign role
az cosmosdb sql role assignment create \
  --account-name your-cosmos-account \
  --resource-group $RESOURCE_GROUP \
  --scope "/" \
  --principal-id $(az ad signed-in-user show --query id -o tsv) \
  --role-definition-name "Cosmos DB Built-in Data Contributor"
```

**替代**：门户 → Cosmos DB → 访问控制 (IAM) → 添加角色分配 →“Cosmos DB 内置数据贡献者”

#### 问题10：分区关键策略差异
**问题**：Cassandra 集群键不直接映射到 Cosmos 分区键
**错误**：跨分区查询或性能不佳
**根本原因**：不同的数据分布策略
**解决方案**：根据查询模式选择合适的分区键，通常是最常查询的字段

#### 问题 10：UUID 到 String 转换问题
**问题**：测试文件和控制器仍然使用 UUID 类型
**错误**：`Cannot convert UUID to String` 或类型不匹配错误
**根本原因**：并非所有出现的 UUID 都被转换为字符串
**解决方案**：系统地搜索所有 UUID 引用并将其替换为 String

### 10. 数据播种（如果适用）

#### 实施数据填充

**如果您的应用程序需要初始数据：**

```java
@Component
public class DataSeeder implements CommandLineRunner {

    private final EntityCosmosRepository entityRepository;

    @Override
    public void run(String... args) throws Exception {
        if (entityRepository.count().block() == 0) {
            // Seed initial data
            EntityName entity = new EntityName();
            entity.setFieldName("Sample Value");
            entity.setAnotherField("Sample Data");

            entityRepository.save(entity).block();
        }
    }
}
```

**如果您的应用程序有现有的数据迁移需求：**
- 创建迁移脚本以从 Cassandra 导出并导入到 Cosmos DB
- 考虑数据转换需求（UUID 到字符串转换）
- 规划 Cassandra 和 Cosmos 数据模型之间的任何架构差异

**如果您的应用程序不需要数据播种：**
- 跳过此步骤，继续验证

### 11. 应用简介

#### 更新 Cosmos 配置文件的 application.yml
```yaml
spring:
  profiles:
    active: cosmos

---
spring:
  profiles: cosmos

azure:
  cosmos:
    uri: ${COSMOS_URI:https://your-account.documents.azure.com:443/}
    database: ${COSMOS_DATABASE:your-database}
```

## 验证步骤

1. **编译检查**：`mvn compile` 应该成功且没有错误
2. **测试检查**：`mvn test` 应该通过更新的测试用例
3. **运行时检查**：应用程序应在没有版本冲突的情况下启动
4. **连接检查**：应用程序应成功连接到 Cosmos DB
5. **数据检查**：CRUD 操作应通过 API 进行
6. **UI 检查**：前端应显示来自 Cosmos DB 的数据

## 最佳实践

1. **ID 策略**：对于 Cosmos DB 始终使用字符串 ID 而不是 UUID
2. **分区键**：根据查询模式和数据分布选择分区键
3. **查询设计**：使用@Query注解进行自定义查询，而不是方法命名约定
4. **反应式编程**：在整个服务层坚持 Flux/Mono 模式
5. **版本管理**：始终包含 Spring Boot 2.x 项目的依赖版本覆盖
6. **测试**：更新所有测试文件以使用字符串 ID 和模拟 Cosmos 存储库
7. **身份验证**：使用 DefaultAzureCredential 进行生产就绪身份验证

## 故障排除命令

```bash
# Check dependencies and version conflicts
mvn dependency:tree | grep -E "(reactor|netty|cosmos)"

# Verify specific problematic dependencies
mvn dependency:tree | grep "reactor-core"
mvn dependency:tree | grep "reactor-netty"
mvn dependency:tree | grep "netty-tcnative"

# Test connection
curl http://localhost:8080/api/entities

# Check Azure login status
az account show

# Clean and rebuild (often fixes dependency issues)
mvn clean compile

# Run with debug logging for dependency resolution
mvn dependency:resolve -X

# Check for compilation errors specifically
mvn compile 2>&1 | grep -E "(ERROR|error)"

# Run with debug for runtime issues
mvn spring-boot:run -Dspring-boot.run.jvmArguments="-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=5005"

# Check application logs for version conflicts
grep -E "(NoSuchMethodError|NoClassDefFoundError|reactor|netty)" application.log
```

## 典型错误序列和解决方法

根据真实的转换经验，您可能会按以下顺序遇到这些错误：

### **阶段 1：编译错误**
1. **缺少依赖项** → 添加 azure-spring-data-cosmos 和 azure-identity
2. **配置类错误** → 创建 CosmosConfiguration（如果尚不存在）
3. **实体注解错误** → 将@Table转换为@Container等。
4. **存储库接口错误** → 更改为 ReactiveCosmosRepository（如果使用存储库模式）

### **阶段 2：Bean 创建错误**
5. **“没有 ReactiveCosmosRepository 类型的合格 bean”** → 添加 @EnableReactiveCosmosRepositories
6. **服务层类型不匹配** → 将Iterable更改为Flux，将Optional更改为Mono（如果使用服务层）

### **阶段 3：运行时版本冲突**（最复杂）
7. **NoClassDefFoundError：reactor.core.publisher.Sinks** → 添加reactor-core 3.4.32覆盖
8. **NoSuchMethodError：Epoll.isTcpFastOpenClientSideAvailable** → 添加 netty-bom 4.1.101.Final 覆盖
9. **NoSuchMethodError：SSLContext.setCurvesList** → 添加 netty-tcnative-boringssl-static 2.0.62.Final 覆盖

### **阶段 4：身份验证和连接**
10. **ManagedIdentityCredential 身份验证不可用** → 运行 `az login --use-device-code`
11. **应用程序成功启动** → 已连接到 Cosmos DB！

**关键**：按顺序解决这些问题。不要向前跳过——每个阶段都必须在下一个阶段出现之前得到解决。

## 性能考虑因素

1. **分区策略**：设计分区键以均匀分配负载
2. **查询优化**：使用索引并尽可能避免跨分区查询
3. **连接池**：Cosmos 客户端自动管理连接
4. **请求单位**：监控 RU 消耗并根据需要调整吞吐量
5. **批量操作**：使用批量操作进行多个文档更新

本指南涵盖了从 Cassandra 转换为 Cosmos DB 的所有主要方面，包括现实场景中遇到的所有版本冲突和身份验证问题。
