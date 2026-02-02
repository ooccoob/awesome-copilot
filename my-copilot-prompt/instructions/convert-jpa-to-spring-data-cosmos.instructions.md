---
description: 'Step-by-step guide for converting Spring Boot JPA applications to use Azure Cosmos DB with Spring Data Cosmos'
applyTo: '**/*.java,**/pom.xml,**/build.gradle,**/application*.properties'
---

# 将 Spring JPA 项目转换为 Spring Data Cosmos

本通用指南适用于任何 JPA 到 Spring Data Cosmos DB 的转换项目。

## 高层计划

1. 交换构建依赖项（删除 JPA，添加 Cosmos + Identity）。
2. 添加 `cosmos` 配置文件和属性。
3. 使用正确的 Azure 身份验证添加 Cosmos 配置。
4. 转换实体（ids → `String`，添加 `@Container` 和 `@PartitionKey`，删除 JPA 映射，调整关系）。
5. 转换存储库（`JpaRepository` → `CosmosRepository`）。
6. **创建服务层**以实现关系管理和模板兼容性。
7. **关键**：更新所有测试文件以使用字符串 ID 和 Cosmos 存储库。
8. 通过 `CommandLineRunner` 提供种子数据。
9. **关键**：测试运行时功能并修复模板兼容性问题。

## 一步一步

### 第 1 步 - 构建依赖关系

- **Maven** (`pom.xml`)：
  - 删除依赖项 `spring-boot-starter-data-jpa`
  - 删除特定于数据库的依赖项（H2、MySQL、PostgreSQL），除非其他地方需要
  - 添加 `com.azure:azure-spring-data-cosmos:5.17.0` （或最新兼容版本）
  - 添加 `com.azure:azure-identity:1.15.4` （DefaultAzureCredential 必需）
- **Gradle**：对 Gradle 语法应用相同的依赖项更改
- 删除测试容器和特定于 JPA 的测试依赖项

### 第 2 步 — 属性和配置

- 创建`src/main/resources/application-cosmos.properties`：
  ```properties
  azure.cosmos.uri=${COSMOS_URI:https://localhost:8081}
  azure.cosmos.database=${COSMOS_DATABASE:petclinic}
  azure.cosmos.populate-query-metrics=false
  azure.cosmos.enable-multiple-write-locations=false
  ```
- 更新`src/main/resources/application.properties`：
  ```properties
  spring.profiles.active=cosmos
  ```

### 步骤 3 — 使用 Azure Identity 的配置类

- 创建`src/main/java/<rootpkg>/config/CosmosConfiguration.java`：
  ```java
  @Configuration
  @EnableCosmosRepositories(basePackages = "<rootpkg>")
  public class CosmosConfiguration extends AbstractCosmosConfiguration {

    @Value("${azure.cosmos.uri}")
    private String uri;

    @Value("${azure.cosmos.database}")
    private String dbName;

    @Bean
    public CosmosClientBuilder getCosmosClientBuilder() {
      return new CosmosClientBuilder().endpoint(uri).credential(new DefaultAzureCredentialBuilder().build());
    }

    @Override
    protected String getDatabaseName() {
      return dbName;
    }

    @Bean
    public CosmosConfig cosmosConfig() {
      return CosmosConfig.builder().enableQueryMetrics(false).build();
    }
  }

  ```
- **重要**：为了生产安全，使用 `DefaultAzureCredentialBuilder().build()` 而不是基于密钥的身份验证

### 第 4 步 — 实体转换

- 使用 JPA 注释定位所有类（`@Entity`、`@MappedSuperclass`、`@Embeddable`）
- **基础实体更改**：
  - 将 `id` 字段类型从 `Integer` 更改为 `String`
  - 添加 `@Id` 和 `@GeneratedValue` 注释
  - 添加 `@PartitionKey` 字段（通常为 `String partitionKey`）
  - 删除所有 `jakarta.persistence` 导入
- **关键 - Cosmos DB 序列化要求**：
  - **从需要持久化到 Cosmos DB 的字段中删除所有 `@JsonIgnore` 注释**
  - **身份验证实体（用户、权限）必须是完全可序列化的** - 密码、权限或其他持久字段上没有 `@JsonIgnore`
  - **当您需要控制 JSON 字段名称但仍保留数据时，请使用 `@JsonProperty` 而不是 `@JsonIgnore`**
  - **常见的身份验证序列化错误**：`Cannot pass null or empty values to constructor` 通常意味着 `@JsonIgnore` 正在阻止所需的字段序列化
- **特定于实体的更改**：
  - 将 `@Entity` 替换为 `@Container(containerName = "<plural-entity-name>")`
  - 删除 `@Table`、`@Column`、`@JoinColumn` 等。
  - 删除关系注释（`@OneToMany`、`@ManyToOne`、`@ManyToMany`）
  - 对于关系：
    - 嵌入一对多的集合（例如，Owner 中的 `List<Pet> pets`）
    - 使用多对一的参考 ID（例如 Pet 中的 `String ownerId`）
    - **对于复杂关系**：存储 ID 但为模板添加瞬态属性
  - 添加构造函数来设置分区键：`setPartitionKey("entityType")`
- **关键 - 身份验证实体模式**：
  - **对于具有 Spring Security 的用户实体**：将权限存储为 `Set<String>` 而不是 `Set<Authority>` 对象
  - **用户实体转换示例**：
    ```java
    @Container(containerName = "users")
    public class User {

      @Id
      private String id;

      @PartitionKey
      private String partitionKey = "user";

      private String login;
      private String password; // NO @JsonIgnore - must be serializable

      @JsonProperty("authorities") // Use @JsonProperty, not @JsonIgnore
      private Set<String> authorities = new HashSet<>(); // Store as strings

      // Add transient property for Spring Security compatibility if needed
      // @JsonIgnore - ONLY for transient properties not persisted to Cosmos
      private Set<Authority> authorityObjects = new HashSet<>();

      // Conversion methods between string authorities and Authority objects
      public void setAuthorityObjects(Set<Authority> authorities) {
        this.authorityObjects = authorities;
        this.authorities = authorities.stream().map(Authority::getName).collect(Collectors.toSet());
      }
    }

    ```
- **关键 - 关系更改的模板兼容性**：
  - **将关系转换为 ID 引用时，保留模板访问权限**
  - **示例**：如果实体有 `List<Specialty> specialties` → 转换为：
    - 存储：`List<String> specialtyIds`（持久化到 Cosmos）
    - 模板：`@JsonIgnore private List<Specialty> specialties = new ArrayList<>()`（瞬态）
    - 为两个属性添加 getter/setter
  - **更新实体方法逻辑**：`getNrOfSpecialties()`应该使用瞬态列表
- **关键 - Thymeleaf/JSP 应用程序的模板兼容性**：
  - **识别模板属性访问**：在 `.html` 文件中搜索 `${entity.relationshipProperty}`
  - **对于模板中访问的每个关系属性**：
    - **存储**：保留基于 ID 的存储（例如 `List<String> specialtyIds`）
    - **模板访问**：使用 `@JsonIgnore` 添加瞬态属性（例如 `private List<Specialty> specialties = new ArrayList<>()`）
    - **示例**：

      ```java
      // Stored in Cosmos (persisted)
      private List<String> specialtyIds = new ArrayList<>();

      // For template access (transient)
      @JsonIgnore
      private List<Specialty> specialties = new ArrayList<>();

      // Getters/setters for both properties
      public List<String> getSpecialtyIds() {
        return specialtyIds;
      }

      public List<Specialty> getSpecialties() {
        return specialties;
      }

      ```

    - **更新计数方法**：`getNrOfSpecialties()` 应使用瞬态列表，而不是 ID 列表
- **严重 - 方法签名冲突**：
  - **将 ID 类型从 Integer 转换为 String 时，检查方法签名冲突**
  - **常见冲突**：`getPet(String name)` 与 `getPet(String id)` - 两者具有相同的签名
  - **解决方案**：将方法重命名为特定的：
    - `getPet(String id)` 用于基于 ID 的查找
    - `getPetByName(String name)` 用于基于名称的查找
    - `getPetByName(String name, boolean ignoreNew)` 用于基于名称的条件查找
  - **更新控制器和测试中重命名方法的所有调用者**
- **实体的方法更新**：
  - 将 `addVisit(Integer petId, Visit visit)` 更新为 `addVisit(String petId, Visit visit)`
  - 确保所有 ID 比较逻辑使用 `.equals()` 而不是 `==`

### 第 5 步 — 存储库转换

- 更改所有存储库接口：
  - 来自：__代码0__
  - 至：`extends CosmosRepository<Entity, String>`
- **查询方法更新**：
  - 从自定义查询中删除分页参数
  - 将 `Page<Entity> findByX(String param, Pageable pageable)` 更改为 `List<Entity> findByX(String param)`
  - 更新 `@Query` 注释以使用 Cosmos SQL 语法
  - **替换自定义方法名称**：`findPetTypes()` → `findAllOrderByName()`
  - **更新所有引用**以更改控制器和格式化程序中的方法名称

### 步骤 6 — **创建服务层**以实现关系管理和模板兼容性

- **关键**：创建服务类以将 Cosmos 文档存储与现有模板期望联系起来
- **目的**：处理关系群体并保持模板兼容性
- **每个具有关系的实体的服务模式**：
  ```java
  @Service
  public class EntityService {

    private final EntityRepository entityRepository;
    private final RelatedRepository relatedRepository;

    public EntityService(EntityRepository entityRepository, RelatedRepository relatedRepository) {
      this.entityRepository = entityRepository;
      this.relatedRepository = relatedRepository;
    }

    public List<Entity> findAll() {
      List<Entity> entities = entityRepository.findAll();
      entities.forEach(this::populateRelationships);
      return entities;
    }

    public Optional<Entity> findById(String id) {
      Optional<Entity> entityOpt = entityRepository.findById(id);
      if (entityOpt.isPresent()) {
        Entity entity = entityOpt.get();
        populateRelationships(entity);
        return Optional.of(entity);
      }
      return Optional.empty();
    }

    private void populateRelationships(Entity entity) {
      if (entity.getRelatedIds() != null && !entity.getRelatedIds().isEmpty()) {
        List<Related> related = entity
          .getRelatedIds()
          .stream()
          .map(relatedRepository::findById)
          .filter(Optional::isPresent)
          .map(Optional::get)
          .collect(Collectors.toList());
        // Set transient property for template access
        entity.setRelated(related);
      }
    }
  }

  ```

### 步骤 6.5 — **Spring Security 集成**（对于身份验证至关重要）

- **用户详细信息服务集成模式**：
  ```java
  @Service
  @Transactional
  public class DomainUserDetailsService implements UserDetailsService {

    private final UserRepository userRepository;
    private final AuthorityRepository authorityRepository;

    @Override
    public UserDetails loadUserByUsername(String login) {
      log.debug("Authenticating user: {}", login);

      return userRepository
        .findOneByLogin(login)
        .map(user -> createSpringSecurityUser(login, user))
        .orElseThrow(() -> new UsernameNotFoundException("User " + login + " was not found"));
    }

    private org.springframework.security.core.userdetails.User createSpringSecurityUser(String lowercaseLogin, User user) {
      if (!user.isActivated()) {
        throw new UserNotActivatedException("User " + lowercaseLogin + " was not activated");
      }

      // Convert string authorities back to GrantedAuthority objects
      List<GrantedAuthority> grantedAuthorities = user
        .getAuthorities()
        .stream()
        .map(SimpleGrantedAuthority::new)
        .collect(Collectors.toList());

      return new org.springframework.security.core.userdetails.User(user.getLogin(), user.getPassword(), grantedAuthorities);
    }
  }

  ```
- **关键身份验证要求**：
  - 用户实体必须是完全可序列化的（密码/权限上没有 `@JsonIgnore`）
  - 将权限存储为 `Set<String>` 以实现 Cosmos DB 兼容性
  - 在 UserDetailsService 中的字符串权限和 `GrantedAuthority` 对象之间进行转换
  - 添加全面的调试日志以跟踪身份验证流程
  - 适当处理激活/停用的用户状态

#### **模板关系人口模式**

返回模板渲染实体的每个服务方法都必须填充瞬态属性：

```java
private void populateRelationships(Entity entity) {
  // For each relationship used in templates
  if (entity.getRelatedIds() != null && !entity.getRelatedIds().isEmpty()) {
    List<Related> relatedObjects = entity
      .getRelatedIds()
      .stream()
      .map(relatedRepository::findById)
      .filter(Optional::isPresent)
      .map(Optional::get)
      .collect(Collectors.toList());
    entity.setRelated(relatedObjects); // Set transient property
  }
}

```

#### **控制器中的关键服务使用**

- **用控制器中的服务调用替换所有直接存储库调用**
- **永远不要将实体从存储库直接返回到没有关系群体的模板
- **更新控制器**以使用服务层而不是直接使用存储库
- **控制器模式更改**：

  ```java
  // OLD: Direct repository usage
  @Autowired
  private EntityRepository entityRepository;

  // NEW: Service layer usage
  @Autowired
  private EntityService entityService;
  // Update method calls
  // OLD: entityRepository.findAll()
  // NEW: entityService.findAll()

  ```

### 第 7 步 — 数据播种

- 创建 `@Component` 实现 `CommandLineRunner`：
  ```java
  @Component
  public class DataSeeder implements CommandLineRunner {

    @Override
    public void run(String... args) throws Exception {
      if (ownerRepository.count() > 0) {
        return; // Data already exists
      }
      // Seed comprehensive test data with String IDs
      // Use meaningful ID patterns: "owner-1", "pet-1", "pettype-1", etc.
    }
  }

  ```
- **严重 - JDK 17+ 的 BigDecimal 反射问题**：
  - **如果使用 BigDecimal 字段**，您可能会在播种过程中遇到反射错误
  - **错误模式**：`Unable to make field private final java.math.BigInteger java.math.BigDecimal.intVal accessible`
  - **解决方案**：
    1. 对于货币值，使用 `Double` 或 `String` 而不是 `BigDecimal`
    2. 添加 JVM 参数：`--add-opens java.base/java.math=ALL-UNNAMED`
    3. 将 BigDecimal 操作包装在 try-catch 中并优雅地处理
  - **即使播种失败，应用程序也会成功启动** - 检查日志中是否有播种错误

### 步骤 8 — 测试文件转换（关键部分）

**此步骤经常被忽视，但对于成功转换至关重要**

#### A. **编译检查策略**

- **每次重大更改后，运行 `mvn test-compile` 以尽早发现问题**
- **继续之前系统地修复编译错误**
- **不要依赖 IDE - Maven 编译揭示所有问题**

#### B. **系统地搜索和更新所有测试文件**

**使用搜索工具查找并更新每个事件：**

- 搜索：`int.*TEST.*ID` → 替换为：`String.*TEST.*ID = "test-xyz-1"`
- 搜索：`setId\(\d+\)` → 替换为：`setId("test-id-X")`
- 搜索：`findById\(\d+\)` → 替换为：`findById("test-id-X")`
- 搜索：`\.findPetTypes\(\)` → 替换为：`.findAllOrderByName()`
- 搜索：`\.findByLastNameStartingWith\(.*,.*Pageable` → 删除分页参数

#### C. 更新测试注释和导入

- 将 `@DataJpaTest` 替换为 `@SpringBootTest` 或适当的切片测试
- 删除 `@AutoConfigureTestDatabase` 注释
- 从测试中删除 `@Transactional` （除非单分区操作）
- 从 `org.springframework.orm` 包中删除导入

#### D. 修复所有测试文件中实体 ID 的使用

**必须更新的关键文件（搜索整个测试目录）：**

- `*ControllerTests.java` - 路径变量、实体创建、模拟设置
- `*ServiceTests.java` - 存储库交互、实体 ID
- `EntityUtils.java` - ID 处理的实用方法
- `*FormatterTests.java` - 存储库方法调用
- `*ValidatorTests.java` - 使用字符串 ID 创建实体
- 集成测试类 - 测试数据设置

#### E. **修复受存储库更改影响的控制器和服务类**

- **更新使用更改的签名调用存储库方法的控制器**
- **更新使用存储库方法的格式化程序/转换器**
- **要检查的常用文件**：
  - `PetTypeFormatter.java` - 经常调用 `findPetTypes()` 方法
  - `*Controller.java` - 可能需要删除分页逻辑
  - 使用存储库方法的服务类

#### F. 更新测试中的存储库模拟

- 从存储库模拟中删除分页：
  - __代码0__
  - → __代码0__
- 更新模拟中的方法名称：
  - __代码0__
  - → __代码0__

#### G. 修复测试使用的实用程序类

- 更新 `EntityUtils.java` 或类似内容：
  - 删除 JPA 特定的异常导入 (`ObjectRetrievalFailureException`)
  - 将方法签名从 `int id` 更改为 `String id`
  - 更新ID比较逻辑：`entity.getId() == entityId` → `entity.getId().equals(entityId)`
  - 将 JPA 异常替换为标准异常 (`IllegalArgumentException`)

#### H. 更新字符串 ID 的断言

- 更改 ID 断言：
  - __代码0__ → __代码1__
  - __代码0__ → __代码1__
  - JSON 路径断言：`jsonPath("$.id").value(1)` → `jsonPath("$.id").value("test-id-1")`

### 步骤 8 — 测试文件转换（关键部分）

**此步骤经常被忽视，但对于成功转换至关重要**

#### A. **编译检查策略**

- **每次重大更改后，运行 `mvn test-compile` 以尽早发现问题**
- **继续之前系统地修复编译错误**
- **不要依赖 IDE - Maven 编译揭示所有问题**

#### B. **系统地搜索和更新所有测试文件**

**使用搜索工具查找并更新每个事件：**

- 搜索：`setId\(\d+\)` → 替换为：`setId("test-id-X")`
- 搜索：`findById\(\d+\)` → 替换为：`findById("test-id-X")`
- 搜索：`\.findPetTypes\(\)` → 替换为：`.findAllOrderByName()`
- 搜索：`\.findByLastNameStartingWith\(.*,.*Pageable` → 删除分页参数

#### C. 更新测试注释和导入

- 将 `@DataJpaTest` 替换为 `@SpringBootTest` 或适当的切片测试
- 删除 `@AutoConfigureTestDatabase` 注释
- 从测试中删除 `@Transactional` （除非单分区操作）
- 从 `org.springframework.orm` 包中删除导入

#### D. 修复所有测试文件中实体 ID 的使用

**必须更新的关键文件（搜索整个测试目录）：**

- `*ControllerTests.java` - 路径变量、实体创建、模拟设置
- `*ServiceTests.java` - 存储库交互、实体 ID
- `EntityUtils.java` - ID 处理的实用方法
- `*FormatterTests.java` - 存储库方法调用
- `*ValidatorTests.java` - 使用字符串 ID 创建实体
- 集成测试类 - 测试数据设置

#### E. **修复受存储库更改影响的控制器和服务类**

- **更新使用更改的签名调用存储库方法的控制器**
- **更新使用存储库方法的格式化程序/转换器**
- **要检查的常用文件**：
  - `PetTypeFormatter.java` - 经常调用 `findPetTypes()` 方法
  - `*Controller.java` - 可能需要删除分页逻辑
  - 使用存储库方法的服务类

#### F. 更新测试中的存储库模拟

- 从存储库模拟中删除分页：
  - __代码0__
  - → __代码0__
- 更新模拟中的方法名称：
  - __代码0__
  - → __代码0__

#### G. 修复测试使用的实用程序类

- 更新 `EntityUtils.java` 或类似内容：
  - 删除 JPA 特定的异常导入 (`ObjectRetrievalFailureException`)
  - 将方法签名从 `int id` 更改为 `String id`
  - 更新ID比较逻辑：`entity.getId() == entityId` → `entity.getId().equals(entityId)`
  - 将 JPA 异常替换为标准异常 (`IllegalArgumentException`)

#### H. 更新字符串 ID 的断言

- 更改 ID 断言：
  - __代码0__ → __代码1__
  - __代码0__ → __代码1__
  - JSON 路径断言：`jsonPath("$.id").value(1)` → `jsonPath("$.id").value("test-id-1")`

### 第 9 步 — **运行时测试和模板兼容性**

#### **关键**：编译成功后测试正在运行的应用程序

- **启动应用程序**：`mvn spring-boot:run`
- **浏览 Web 界面中的所有页面**以识别运行时错误
- **转换后常见的运行时问题**：
  - 模板尝试访问不再存在的属性（例如，`vet.specialties`）
  - 服务层不填充瞬态关系属性
  - 控制器不使用服务层进行关系加载

#### **模板兼容性修复**：

- **如果模板访问关系属性**（例如，`entity.relatedObjects`）：
  - 确保具有适当 getter/setter 的实体上存在瞬态属性
  - 验证服务层填充这些瞬态属性
  - 更新 `getNrOfXXX()` 方法以使用瞬态列表而不是 ID 列表
- **检查日志中的 SpEL（Spring 表达式语言）错误**：
  - `Property or field 'xxx' cannot be found` → 添加缺失的瞬态属性
  - `EL1008E` 错误 → 服务层未填充关系

#### **服务层验证**：

- **确保所有控制器使用服务层**而不是直接存储库访问
- **在返回实体之前验证服务方法填充关系**
- **通过Web界面测试所有CRUD操作**

### 步骤 9.5 — **模板运行时验证**（关键）

#### **系统模板测试流程**

编译成功并启动应用程序后：

1. **系统地导航到应用程序中的每个页面**
2. **测试每个显示实体数据的模板**：
   - 列表页面（例如 `/vets`、`/owners`）
   - 详细信息页面（例如 `/owners/{id}`、`/vets/{id}`）
   - 表单和编辑页面
3. **查找特定模板错误**：
   - __代码0__
   - `EL1008E` Spring 表达式语言错误
   - 应出现关系的数据为空或缺失

#### **模板错误解决清单**

遇到模板错误时：

- [ ] **从错误消息中识别丢失的属性**
- [ ] **检查实体中属性是否作为瞬态字段存在**
- [ ] **在返回实体之前验证服务层填充属性**
- [ ] **确保控制器使用服务层**，而不是直接存储库访问
- [ ] **修复后再次测试特定页面**

#### **常见模板错误模式**

- `Property or field 'specialties' cannot be found` → 将 `@JsonIgnore private List<Specialty> specialties` 添加到 Vet 实体
- `Property or field 'pets' cannot be found` → 将 `@JsonIgnore private List<Pet> pets` 添加到所有者实体
- 显示空关系数据 → 服务未填充瞬态属性

### 步骤 10 — **系统错误解决过程**

#### 当编译失败时：

1. **首先运行 `mvn compile`** - 在测试之前修复主要源问题
2. **运行`mvn test-compile`** - 系统地修复每个测试编译错误
3. **关注最常见的错误模式**：
   - `int cannot be converted to String` → 更改测试常量和实体设置器
   - `method X cannot be applied to given types` → 删除分页参数
   - `cannot find symbol: method Y()` → 更新为新的存储库方法名称
   - 方法签名冲突→重命名冲突的方法

### 步骤 10 — **系统错误解决过程**

#### 当编译失败时：

1. **首先运行 `mvn compile`** - 在测试之前修复主要源问题
2. **运行`mvn test-compile`** - 系统地修复每个测试编译错误
3. **关注最常见的错误模式**：
   - `int cannot be converted to String` → 更改测试常量和实体设置器
   - `method X cannot be applied to given types` → 删除分页参数
   - `cannot find symbol: method Y()` → 更新为新的存储库方法名称
   - 方法签名冲突→重命名冲突的方法
#### 当运行时失败时：

1. **检查应用程序日志**以获取特定错误消息
2. **查找模板/SpEL 错误**：
   - `Property or field 'xxx' cannot be found` → 向实体添加瞬态属性
   - 缺少关系数据 → 服务层未填充关系
3. **验证控制器中服务层的使用**
4. **测试所有应用程序页面的导航**

#### 常见错误模式及解决方案：

- **`method findByLastNameStartingWith cannot be applied`** → 删除 `Pageable` 参数
- **`cannot find symbol: method findPetTypes()`** → 更改为 `findAllOrderByName()`
- **`incompatible types: int cannot be converted to String`** → 更新测试 ID 常量
- **`method getPet(String) is already defined`** → 重命名一个方法（例如，`getPetByName`）
- **`cannot find symbol: method isNotZero()`** → 将字符串 ID 更改为 `isNotEmpty()`
- **`Property or field 'specialties' cannot be found`** → 添加瞬态属性并填充到服务中
- **`ClassCastException: reactor.core.publisher.BlockingIterable cannot be cast to java.util.List`** → 修复存储库 `findAllWithEagerRelationships()` 方法以使用 StreamSupport
- **`Unable to make field...BigDecimal.intVal accessible`** → 在整个应用程序中将 BigDecimal 替换为 Double
- **健康检查数据库故障** → 从健康检查准备配置中删除“db”

#### **特定于模板的运行时错误**

- **__代码0__**：

  - 根本原因：模板访问关系属性已转换为 ID 存储
  - 解决方案：向实体添加瞬态属性+在服务层填充
  - 预防措施：在转换关系之前始终检查模板使用情况

- **`EL1008E` Spring 表达式语言错误**：

  - 根本原因：服务层未填充瞬态属性
  - 解决方案：验证 `populateRelationships()` 方法被调用并且正常工作
  - 预防：在服务层实现后测试所有模板导航

- **模板中的空/空关系数据**：
  - 根本原因：控制器绕过服务层或服务未填充关系
  - 解决方案：确保所有控制器方法都使用服务层进行实体检索
  - 预防措施：切勿将存储库结果直接返回到模板

### 第 11 步 — 验证清单

转换后验证：

- [ ] **主应用程序编译**：`mvn compile` 成功
- [ ] **所有测试文件编译**：`mvn test-compile`成功
- [ ] **没有编译错误**：解决每个编译错误
- [ ] **应用程序成功启动**：`mvn spring-boot:run` 没有错误
- [ ] **加载所有网页**：浏览所有应用程序页面而不会出现运行时错误
- [ ] **服务层填充关系**：正确设置瞬态属性
- [ ] **所有模板页面均呈现无错误**：浏览整个应用程序
- [ ] **关系数据正确显示**：列表、计数和相关对象正确显示
- [ ] **日志中没有 SpEL 模板错误**：在导航期间检查应用程序日志
- [ ] **瞬态属性带有 @JsonIgnore 注释**：防止 JSON 序列化问题
- [ ] **一致使用服务层**：控制器中没有直接存储库访问以进行模板渲染
- [ ] 没有剩余的 `jakarta.persistence` 导入
- [ ] 所有实体 ID 均一致为 `String` 类型
- [ ] 所有存储库接口都扩展 `CosmosRepository<Entity, String>`
- [ ] 配置使用 `DefaultAzureCredential` 进行身份验证
- [ ] 数据播种组件存在并且可以工作
- [ ] 测试文件一致地使用字符串 ID
- [ ] 更新了 Cosmos 方法的存储库模拟
- [ ] **实体类中没有方法签名冲突**
- [ ] **调用者（控制器、测试、格式化程序）中的所有重命名方法均已更新**

### 要避免的常见陷阱

1. **不经常检查编译** - 每次重大更改后运行 `mvn test-compile`
2. **方法签名冲突** - 转换ID类型时的方法重载问题
3. **忘记更新方法调用者** - 重命名方法时，更新所有调用者
4. **缺少存储库方法重命名** - 必须在调用的所有地方更新自定义存储库方法
5. **使用基于密钥的身份验证** - 使用 `DefaultAzureCredential` 代替
6. **混合整数和字符串 ID** - 与各处的字符串 ID 保持一致，尤其是在测试中
7. **不更新控制器分页逻辑** - 当存储库更改时从控制器中删除分页
8. **保留 JPA 特定的测试注释** - 替换为与 Cosmos 兼容的替代方案
9. **不完整的测试文件更新** - 搜索整个测试目录，而不仅仅是明显的文件
10. **跳过运行时测试** - 始终测试正在运行的应用程序，而不仅仅是编译
11. **缺少服务层** - 不要直接从控制器访问存储库
12. **忘记瞬态属性** - 模板可能需要访问关系数据
13. **不测试模板导航** - 编译成功并不意味着模板可以工作
14. **缺少模板的瞬态属性** - 模板需要对象访问，而不仅仅是 ID
15. **服务层绕过** - 控制器必须使用服务，而不是直接访问存储库
16. **不完整的关系填充** - 服务方法必须填充模板使用的所有瞬态属性
17. **忘记瞬态属性上的 @JsonIgnore** - 防止序列化问题
18. **@JsonIgnore 对持久化字段** - **关键**：切勿在需要存储在 Cosmos DB 中的字段上使用 `@JsonIgnore`
19. **身份验证序列化错误** - 用户/权限实体必须完全可序列化，且 `@JsonIgnore` 不会阻止必填字段
20. **BigDecimal 反射问题** - 使用替代数据类型或 JVM 参数来实现 JDK 17+ 兼容性
21. **存储库反应类型转换** - 不要将 `findAll()` 直接转换为 `List`，而是使用 `StreamSupport.stream().collect(Collectors.toList())`
22. **运行状况检查数据库引用** - 删除 JPA 后从 Spring Boot 运行状况检查中删除数据库依赖项
23. **集合类型不匹配** - 更新服务方法以一致地处理字符串与对象集合

### 系统地调试编译问题

如果转换后编译失败：

1. **从主编译开始**：`mvn compile` - 首先修复实体和控制器问题
2. **然后测试编译**：`mvn test-compile` - 系统地修复每个错误
3. **检查整个代码库中剩余的 `jakarta.persistence` 导入**
4. **验证所有测试常量都使用字符串 ID** - 搜索 `int.*TEST.*ID`
5. **确保存储库方法签名匹配**新的 Cosmos 接口
6. **检查实体关系和测试中的混合整数/字符串 ID 使用**
7. **验证所有模拟都使用正确的方法名称**（`findAllOrderByName()` 不是 `findPetTypes()`）
8. **查找方法签名冲突** - 通过重命名冲突方法来解决
9. **验证断言方法是否适用于字符串 ID**（`isNotEmpty()` 不是 `isNotZero()`）

### 系统地调试运行时问题

如果编译成功后运行时失败：

1. **检查应用程序启动日志**是否有初始化错误
2. **浏览所有页面**以识别模板/控制器问题
3. **在日志中查找 SpEL 模板错误**：
   - `Property or field 'xxx' cannot be found` → 缺少瞬态属性
   - `EL1008E` → 服务层未填充关系
4. **验证正在使用服务层**而不是直接存储库访问
5. **检查服务方法中是否填充了瞬态属性**
6. **通过Web界面测试所有CRUD操作**
7. **验证数据播种是否正确**并维护关系
8. **特定于身份验证的调试**：
   - `Cannot pass null or empty values to constructor` → 检查必填字段中是否有 `@JsonIgnore`
   - `BadCredentialsException` → 验证用户实体序列化和密码字段可访问性
   - 检查“DomainUserDetailsService”调试输出的日志以跟踪身份验证流程

### **成功的专业秘诀**

- **尽早且经常编译** - 不要让错误累积
- **使用全局搜索和替换** - 查找所有出现的模式进行更新
- **系统化** - 在移动到下一个之前修复所有文件中的一种类型的错误
- **测试方法仔细重命名** - 确保所有调用者均已更新
- **使用有意义的字符串 ID** - “owner-1”、“pet-1”而不是随机字符串
- **检查控制器类** - 他们经常调用更改签名的存储库方法
- **始终测试运行时** - 编译成功并不能保证模板功能正常
- **服务层至关重要** - 文档存储和模板期望之间的桥梁

### **身份验证故障排除指南**（重要）

#### **常见身份验证序列化错误**：

1. **__代码0__**：

   - **根本原因**：`@JsonIgnore` 阻止将所需字段序列化到 Cosmos DB
   - **解决方案**：从所有持久字段（密码、权限等）中删除 `@JsonIgnore`
   - **验证**：检查用户实体在存储字段上没有 `@JsonIgnore`

2. 登录期间**`BadCredentialsException`**：

   - **根本原因**：身份验证期间无法访问密码字段
   - **解决方案**：确保密码字段在 UserDetailsService 中可序列化且可访问
   - **验证**：在 `loadUserByUsername` 方法中添加调试日志

3. **当局未正确加载**：

   - **根本原因**：权威对象存储为复杂实体而不是字符串
   - **解决方案**：将权限存储为 `Set<String>` 并在 UserDetailsService 中转换为 `GrantedAuthority`
   - **图案**：

     ```java
     // In User entity - stored in Cosmos
     @JsonProperty("authorities")
     private Set<String> authorities = new HashSet<>();

     // In UserDetailsService - convert for Spring Security
     List<GrantedAuthority> grantedAuthorities = user
       .getAuthorities()
       .stream()
       .map(SimpleGrantedAuthority::new)
       .collect(Collectors.toList());

     ```

4. **身份验证期间未找到用户实体**：
   - **根本原因**：存储库查询方法不适用于字符串 ID
   - **解决方案**：更新存储库 `findOneByLogin` 方法以与 Cosmos DB 配合使用
   - **验证**：独立测试存储库方法

#### **身份验证调试清单**：

- [ ] 用户实体完全可序列化（持久字段上没有 `@JsonIgnore` ）
- [ ] 密码字段可访问且不为空
- [ ] 权限存储为 `Set<String>`
- [ ] UserDetailsService 将字符串权限转换为 `GrantedAuthority`
- [ ] 存储库方法使用字符串 ID
- [ ] 在身份验证服务中启用调试日志记录
- [ ] 适当检查用户激活状态
- [ ] 使用已知凭据测试登录（admin/admin）

### **常见运行时问题和解决方案**

#### **问题 1：存储库反应类型转换错误**

**错误**：`ClassCastException: reactor.core.publisher.BlockingIterable cannot be cast to java.util.List`

**根本原因**：Cosmos 存储库返回反应类型 (`Iterable`)，但旧版 JPA 代码需要 `List`

**解决方案**：在存储库方法中正确转换反应类型：

```java
// WRONG - Direct casting fails
default List<Entity> customFindMethod() {
    return (List<Entity>) this.findAll(); // ClassCastException!
}

// CORRECT - Convert Iterable to List
default List<Entity> customFindMethod() {
    return StreamSupport.stream(this.findAll().spliterator(), false)
            .collect(Collectors.toList());
}
```

**要检查的文件**：

- 具有自定义默认方法的所有存储库接口
- 从 Cosmos 存储库调用返回 `List<Entity>` 的任何方法
- 导入 `java.util.stream.StreamSupport` 和 `java.util.stream.Collectors`

#### **问题 2：Java 17+ 中的 BigDecimal 反射问题**

**错误**：`Unable to make field private final java.math.BigInteger java.math.BigDecimal.intVal accessible`

**根本原因**：Java 17+ 模块系统在序列化期间限制对 BigDecimal 内部字段的反射访问

**解决方案**：

1. **对于简单情况，替换为 Double**：

   ```java
   // Before: BigDecimal fields
   private BigDecimal amount;

   // After: Double fields (if precision requirements allow)
   private Double amount;

   ```

2. **使用 String 来满足高精度要求**：

   ```java
   // Store as String, convert as needed
   private String amount; // Store "1500.00"

   public BigDecimal getAmountAsBigDecimal() {
     return new BigDecimal(amount);
   }

   ```

3. **添加 JVM 参数**（如果必须保留 BigDecimal）：
   ```
   --add-opens java.base/java.math=ALL-UNNAMED
   ```

#### **问题3：健康检查数据库依赖关系**

**错误**：应用程序无法进行运行状况检查以查找已删除的数据库组件

**根本原因**：删除后 Spring Boot 运行状况检查仍然引用 JPA/数据库依赖项

**解决方案**：更新健康检查配置：

```yaml
# In application.yml - Remove database from health checks
management:
  health:
    readiness:
      include: 'ping,diskSpace' # Remove 'db' if present
```

**要检查的文件**：

- 所有 `application*.yml` 配置文件
- 删除任何特定于数据库的运行状况指标
- 检查执行器端点配置

#### **问题 4：服务中集合类型不匹配**

**错误**：将实体关系转换为基于字符串的存储时出现类型不匹配错误

**根本原因**：实体转换后期望不同集合类型的服务方法

**解决方案**：更新服务方法以处理新的实体结构：

```java
// Before: Entity relationships
public Set<RelatedEntity> getRelatedEntities() {
    return entity.getRelatedEntities(); // Direct entity references
}

// After: String-based relationships with conversion
public Set<RelatedEntity> getRelatedEntities() {
    return entity.getRelatedEntityIds()
        .stream()
        .map(relatedRepository::findById)
        .filter(Optional::isPresent)
        .map(Optional::get)
        .collect(Collectors.toSet());
}

### **Enhanced Error Resolution Process**

#### **Common Error Patterns and Solutions**:

1. **Reactive Type Casting Errors**:
   - **Pattern**: `cannot be cast to java.util.List`
   - **Fix**: Use `StreamSupport.stream().collect(Collectors.toList())`
   - **Files**: Repository interfaces with custom default methods

2. **BigDecimal Serialization Errors**:
   - **Pattern**: `Unable to make field...BigDecimal.intVal accessible`
   - **Fix**: Replace with Double, String, or add JVM module opens
   - **Files**: Entity classes, DTOs, data initialization classes

3. **Health Check Database Errors**:
   - **Pattern**: Health check fails looking for database
   - **Fix**: Remove database references from health check configuration
   - **Files**: application.yml configuration files

4. **Collection Type Conversion Errors**:
   - **Pattern**: Type mismatch in entity relationship handling
   - **Fix**: Update service methods to handle String-based entity references
   - **Files**: Service classes, DTOs, entity relationship methods

#### **Enhanced Validation Checklist**:
- [ ] **Repository reactive casting handled**: No ClassCastException on collection returns
- [ ] **BigDecimal compatibility resolved**: Java 17+ serialization works
- [ ] **Health checks updated**: No database dependencies in health configuration
- [ ] **Service layer collection handling**: String-based entity references work correctly
- [ ] **Data seeding completes**: "Data seeding completed" message appears in logs
- [ ] **Application starts fully**: Both frontend and backend accessible
- [ ] **Authentication works**: Can sign in without serialization errors
- [ ] **CRUD operations functional**: All entity operations work through UI

## **Quick Reference: Common Post-Migration Fixes**

### **Top Runtime Issues to Check**

1. **Repository Collection Casting**:
   ```java
   // 修复任何返回集合的存储库方法：
   默认列表 <Entity> customFindMethod() {
       返回 StreamSupport.stream(this.findAll().spliterator(), false)
               .collect(Collectors.toList());
   }

2. **BigDecimal 兼容性（Java 17+）**：

   ```java
   // Replace BigDecimal fields with alternatives:
   private Double amount; // Or String for high precision

   ```

3. **健康检查配置**：
   ```yaml
   # Remove database dependencies from health checks:
   management:
     health:
       readiness:
         include: 'ping,diskSpace'
   ```

### **身份验证转换模式**

- **从需要 Cosmos DB 持久性的字段中删除 `@JsonIgnore`**
- **将复杂对象存储为简单类型**（例如，权限为 `Set<String>`）
- **在服务/存储库层中简单类型和复杂类型之间的转换**

### **模板/UI 兼容性模式**

- **使用 `@JsonIgnore` 添加瞬态属性**，以便 UI 访问相关数据
- **使用服务层**在渲染之前填充瞬态关系
- **永远不要将存储库结果直接返回**到没有关系群体的模板
