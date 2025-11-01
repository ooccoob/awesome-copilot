---
description: '将Spring Boot JPA应用程序转换为使用Azure Cosmos DB和Spring Data Cosmos的分步指南'
applyTo: '**/*.java,**/pom.xml,**/build.gradle,**/application*.properties'
---

# 将Spring JPA项目转换为Spring Data Cosmos

此通用指南适用于任何JPA到Spring Data Cosmos DB转换项目。

## 高级计划

1. 交换构建依赖项（删除JPA，添加Cosmos + Identity）。
2. 添加`cosmos`配置文件和属性。
3. 添加带有适当Azure身份验证的Cosmos配置。
4. 转换实体（ids → `String`，添加`@Container`和`@PartitionKey`，删除JPA映射，调整关系）。
5. 转换仓储（`JpaRepository` → `CosmosRepository`）。
6. **关键**：创建服务层用于关系管理和模板兼容性。
7. **关键**：更新所有测试文件以使用String ID和Cosmos仓储。
8. 通过`CommandLineRunner`种子数据。
9. **关键**：测试运行时功能并修复模板兼容性问题。

## 分步详解

### 步骤1 — 构建依赖项

- **Maven**（`pom.xml`）：
  - 删除依赖`spring-boot-starter-data-jpa`
  - 删除特定于数据库的依赖项（H2、MySQL、PostgreSQL），除非其他地方需要
  - 添加`com.azure:azure-spring-data-cosmos:5.17.0`（或最新兼容版本）
  - 添加`com.azure:azure-identity:1.15.4`（DefaultAzureCredential所需）
- **Gradle**：对Gradle语法应用相同的依赖项更改
- 删除testcontainers和JPA特定测试依赖项

### 步骤2 — 属性和配置

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

### 步骤3 — 带有Azure身份验证的配置类

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
- **重要**：使用`DefaultAzureCredentialBuilder().build()`而不是基于密钥的身份验证以确保生产安全

### 步骤4 — 实体转换

- 定位所有带有JPA注解的类（`@Entity`、`@MappedSuperclass`、`@Embeddable`）
- **基础实体更改**：
  - 将`id`字段类型从`Integer`更改为`String`
  - 添加`@Id`和`@GeneratedValue`注解
  - 添加`@PartitionKey`字段（通常为`String partitionKey`）
  - 删除所有`jakarta.persistence`导入
- **关键 - Cosmos DB序列化要求**：
  - **删除所有`@JsonIgnore`注解**从需要持久化到Cosmos DB的字段
  - **身份验证实体（User、Authority）必须完全可序列化** - 在密码、权限或其他持久化字段上没有`@JsonIgnore`
  - **需要控制JSON字段名称但仍要持久化数据时使用`@JsonProperty`而不是`@JsonIgnore`**
  - **常见身份验证序列化错误**：`Cannot pass null or empty values to constructor`通常意味着`@JsonIgnore`阻止了必需字段的序列化
- **实体特定更改**：
  - 用`@Container(containerName = "<plural-entity-name>")`替换`@Entity`
  - 删除`@Table`、`@Column`、`@JoinColumn`等
  - 删除关系注解（`@OneToMany`、`@ManyToOne`、`@ManyToMany`）
  - 对于关系：
    - 为一对多嵌入集合（例如Owner中的`List<Pet> pets`）
    - 为多对一使用引用ID（例如Pet中的`String ownerId`）
    - **对于复杂关系**：存储ID但为模板添加瞬态属性
  - 添加构造函数设置分区键：`setPartitionKey("entityType")`
- **关键 - 身份验证实体模式**：
  - **对于带有Spring Security的User实体**：将权限存储为`Set<String>`而不是`Set<Authority>`对象
  - **示例User实体转换**：
    ```java
    @Container(containerName = "users")
    public class User {

      @Id
      private String id;

      @PartitionKey
      private String partitionKey = "user";

      private String login;
      private String password; // 没有@JsonIgnore - 必须可序列化

      @JsonProperty("authorities") // 使用@JsonProperty，而不是@JsonIgnore
      private Set<String> authorities = new HashSet<>(); // 存储为字符串

      // 如果需要，为Spring Security兼容性添加瞬态属性
      // @JsonIgnore - 仅用于不持久化到Cosmos的瞬态属性
      private Set<Authority> authorityObjects = new HashSet<>();

      // 在字符串权限和Authority对象之间转换的方法
      public void setAuthorityObjects(Set<Authority> authorities) {
        this.authorityObjects = authorities;
        this.authorities = authorities.stream().map(Authority::getName).collect(Collectors.toSet());
      }
    }

    ```
- **关键 - 关系更改的模板兼容性**：
  - **将关系转换为ID引用时，保留模板访问**
  - **示例**：如果实体有`List<Specialty> specialties` → 转换为：
    - 存储：`List<String> specialtyIds`（持久化到Cosmos）
    - 模板：`@JsonIgnore private List<Specialty> specialties = new ArrayList<>()`（瞬态）
    - 为两个属性添加getter/setter
  - **更新实体方法逻辑**：`getNrOfSpecialties()`应该使用瞬态列表
- **关键 - Thymeleaf/JSP应用程序的模板兼容性**：
  - **识别模板属性访问**：在`.html`文件中搜索`${entity.relationshipProperty}`
  - **对于在模板中访问的每个关系属性**：
    - **存储**：保持基于ID的存储（例如`List<String> specialtyIds`）
    - **模板访问**：添加带有`@JsonIgnore`的瞬态属性（例如`private List<Specialty> specialties = new ArrayList<>()`）
    - **示例**：

      ```java
      // 存储在Cosmos中（持久化）
      private List<String> specialtyIds = new ArrayList<>();

      // 用于模板访问（瞬态）
      @JsonIgnore
      private List<Specialty> specialties = new ArrayList<>();

      // 两个属性的getter/setter
      public List<String> getSpecialtyIds() {
        return specialtyIds;
      }

      public List<Specialty> getSpecialties() {
        return specialties;
      }

      ```

    - **更新计数方法**：`getNrOfSpecialties()`应该使用瞬态列表，而不是ID列表
- **关键 - 方法签名冲突**：
  - **当将ID类型从Integer转换为String时，检查方法签名冲突**
  - **常见冲突**：`getPet(String name)` vs `getPet(String id)` - 两者具有相同的签名
  - **解决方案**：重命名方法使其具体化：
    - `getPet(String id)`用于基于ID的查找
    - `getPetByName(String name)`用于基于名称的查找
    - `getPetByName(String name, boolean ignoreNew)`用于条件性基于名称的查找
  - **在控制器和测试中更新所有重命名方法的调用者**
- **实体的方法更新**：
  - 将`addVisit(Integer petId, Visit visit)`更新为`addVisit(String petId, Visit visit)`
  - 确保所有ID比较逻辑使用`.equals()`而不是`==`

### 步骤5 — 仓储转换

- 更改所有仓储接口：
  - 从：`extends JpaRepository<Entity, Integer>`
  - 到：`extends CosmosRepository<Entity, String>`
- **查询方法更新**：
  - 从自定义查询中删除分页参数
  - 将`Page<Entity> findByX(String param, Pageable pageable)`更改为`List<Entity> findByX(String param)`
  - 更新`@Query`注解以使用Cosmos SQL语法
  - **替换自定义方法名称**：`findPetTypes()` → `findAllOrderByName()`
  - **在控制器和格式化程序中更新所有对更改方法名的引用**

### 步骤6 — **创建服务层**用于关系管理和模板兼容性

- **关键**：创建服务类以桥接Cosmos文档存储与现有模板期望
- **目的**：处理关系填充并保持模板兼容性
- **每个带有关系的实体的服务模式**：
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
        // 为模板访问设置瞬态属性
        entity.setRelated(related);
      }
    }
  }

  ```

### 步骤6.5 — **Spring Security集成**（身份验证关键）

- **UserDetailsService集成模式**：
  ```java
  @Service
  @Transactional
  public class DomainUserDetailsService implements UserDetailsService {

    private final UserRepository userRepository;
    private final AuthorityRepository authorityRepository;

    @Override
    public UserDetails loadUserByUsername(String login) {
      log.debug("正在验证用户: {}", login);

      return userRepository
        .findOneByLogin(login)
        .map(user -> createSpringSecurityUser(login, user))
        .orElseThrow(() -> new UsernameNotFoundException("用户 " + login + " 未找到"));
    }

    private org.springframework.security.core.userdetails.User createSpringSecurityUser(String lowercaseLogin, User user) {
      if (!user.isActivated()) {
        throw new UserNotActivatedException("用户 " + lowercaseLogin + " 未激活");
      }

      // 将字符串权限转换回GrantedAuthority对象
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
  - User实体必须完全可序列化（密码/权限上没有`@JsonIgnore`）
  - 为了Cosmos DB兼容性，将权限存储为`Set<String>`
  - 在UserDetailsService中在字符串权限和`GrantedAuthority`对象之间转换
  - 为身份验证流添加全面的调试日志
  - 适当处理已激活/未激活用户状态

#### **模板关系填充模式**

每个返回实体用于模板渲染的服务方法必须填充瞬态属性：

```java
private void populateRelationships(Entity entity) {
  // 对于模板中使用的每个关系
  if (entity.getRelatedIds() != null && !entity.getRelatedIds().isEmpty()) {
    List<Related> relatedObjects = entity
      .getRelatedIds()
      .stream()
      .map(relatedRepository::findById)
      .filter(Optional::isPresent)
      .map(Optional::get)
      .collect(Collectors.toList());
    entity.setRelated(relatedObjects); // 设置瞬态属性
  }
}
```

#### **控制器中的关键服务使用**

- **用服务调用替换所有直接仓储调用**在控制器中
- **绝不直接从仓储返回实体**到模板而不进行关系填充
- **更新控制器**以使用服务层而不是直接使用仓储
- **控制器模式更改**：

  ```java
  // 旧：直接仓储使用
  @Autowired
  private EntityRepository entityRepository;

  // 新：服务层使用
  @Autowired
  private EntityService entityService;
  // 更新方法调用
  // 旧：entityRepository.findAll()
  // 新：entityService.findAll()

  ```

### 步骤7 — 数据种子

- 创建实现`CommandLineRunner`的`@Component`：
  ```java
  @Component
  public class DataSeeder implements CommandLineRunner {

    @Override
    public void run(String... args) throws Exception {
      if (ownerRepository.count() > 0) {
        return; // 数据已存在
      }
      // 使用String ID种子化全面的测试数据
      // 使用有意义的ID模式："owner-1"、"pet-1"、"pettype-1"等
    }
  }

  ```
- **关键 - JDK 17+的BigDecimal反射问题**：
  - **如果使用BigDecimal字段**，您可能在种子化期间遇到反射错误
  - **错误模式**：`Unable to make field private final java.math.BigInteger java.math.BigDecimal.intVal accessible`
  - **解决方案**：
    1. 对货币值使用`Double`或`String`而不是`BigDecimal`
    2. 添加JVM参数：`--add-opens java.base/java.math=ALL-UNNAMED`
    3. 将BigDecimal操作包装在try-catch中并优雅处理
  - **即使种子化失败应用程序也会成功启动** - 检查日志中的种子化错误

### 步骤8 — 测试文件转换（关键部分）

**此步骤经常被忽略但对成功转换至关重要**

#### A. **编译检查策略**

- **每次重大更改后运行`mvn test-compile`以尽早发现问题**
- **在继续之前系统地修复编译错误**
- **不要依赖IDE - Maven编译揭示所有问题**

#### B. **系统地搜索和更新所有测试文件**

**使用搜索工具查找和更新每个出现：**

- 搜索：`int.*TEST.*ID` → 替换为：`String.*TEST.*ID = "test-xyz-1"`
- 搜索：`setId\(\d+\)` → 替换为：`setId("test-id-X")`
- 搜索：`findById\(\d+\)` → 替换为：`findById("test-id-X")`
- 搜索：`\.findPetTypes\(\)` → 替换为：`.findAllOrderByName()`
- 搜索：`\.findByLastNameStartingWith\(.*,.*Pageable` → 删除分页参数

#### C. 更新测试注解和导入

- 用`@SpringBootTest`或适当的切片测试替换`@DataJpaTest`
- 删除`@AutoConfigureTestDatabase`注解
- 从测试中删除`@Transactional`（除非单分区操作）
- 删除来自`org.springframework.orm`包的导入

#### D. 在所有测试文件中修复实体ID使用

**必须更新的关键文件（搜索整个测试目录）：**

- `*ControllerTests.java` - 路径变量、实体创建、模拟设置
- `*ServiceTests.java` - 仓储交互、实体ID
- `EntityUtils.java` - ID处理的实用方法
- `*FormatterTests.java` - 仓储方法调用
- `*ValidatorTests.java` - 带有String ID的实体创建
- 集成测试类 - 测试数据设置

#### E. **修复受仓储更改影响的控制器和服务类**

- **更新调用具有已更改签名的仓储方法的控制器**
- **更新使用仓储方法的格式化程序/转换器**
- **要检查的常见文件**：
  - `PetTypeFormatter.java` - 通常调用`findPetTypes()`方法
  - `*Controller.java` - 可能需要删除分页逻辑
  - 使用仓储方法的服务类

#### F. 更新测试中的仓储模拟

- 从仓储模拟中删除分页：
  - `given(repository.findByX(param, pageable)).willReturn(pageResult)`
  - → `given(repository.findByX(param)).willReturn(listResult)`
- 更新模拟中的方法名称：
  - `given(petTypeRepository.findPetTypes()).willReturn(types)`
  - → `given(petTypeRepository.findAllOrderByName()).willReturn(types)`

#### G. 修复测试使用的实用类

- 更新`EntityUtils.java`或类似：
  - 删除JPA特定异常导入（`ObjectRetrievalFailureException`）
  - 将方法签名从`int id`更改为`String id`
  - 更新ID比较逻辑：`entity.getId() == entityId` → `entity.getId().equals(entityId)`
  - 用标准异常（`IllegalArgumentException`）替换JPA异常

#### H. 更新String ID的断言

- 更改ID断言：
  - `assertThat(entity.getId()).isNotZero()` → `assertThat(entity.getId()).isNotEmpty()`
  - `assertThat(entity.getId()).isEqualTo(1)` → `assertThat(entity.getId()).isEqualTo("test-id-1")`
  - JSON路径断言：`jsonPath("$.id").value(1)` → `jsonPath("$.id").value("test-id-1")`

### 步骤9 — **运行时测试和模板兼容性**

#### **关键**：编译成功后测试运行的应用程序

- **启动应用程序**：`mvn spring-boot:run`
- **浏览Web界面中的所有页面**以识别运行时错误
- **转换后的常见运行时问题**：
  - 模板试图访问不再存在的属性（例如`vet.specialties`）
  - 服务层未填充瞬态关系属性
  - 控制器未使用服务层进行关系加载

#### **模板兼容性修复**：

- **如果模板访问关系属性**（例如`entity.relatedObjects`）：
  - 确保瞬态属性存在于实体上并带有适当的getter/setter
  - 验证服务层填充这些瞬态属性
  - 更新`getNrOfXXX()`方法以使用瞬态列表而不是ID列表
- **检查日志中的SpEL（Spring表达式语言）错误**：
  - `Property or field 'xxx' cannot be found` → 添加缺失的瞬态属性
  - `EL1008E`错误 → 服务层未填充关系

#### **服务层验证**：

- **确保所有控制器使用服务层**而不是直接仓储访问
- **验证服务方法在返回实体之前填充关系**
- **通过Web界面测试所有CRUD操作**

### 步骤9.5 — **模板运行时验证**（关键）

#### **系统性模板测试过程**

成功编译和应用程序启动后：

1. **系统地浏览应用程序中的每个页面**
2. **测试每个显示实体数据的模板**：
   - 列表页面（例如`/vets`、`/owners`）
   - 详情页面（例如`/owners/{id}`、`/vets/{id}`）
   - 表单和编辑页面
3. **查找特定的模板错误**：
   - `Property or field 'relationshipName' cannot be found on object of type 'EntityName'`
   - `EL1008E` Spring表达式语言错误
   - 关系应该出现的地方出现空或缺失的数据

#### **模板错误解决清单**

遇到模板错误时：

- [ ] **从错误消息中识别缺失的属性**
- [ ] **检查属性是否作为瞬态字段存在于实体中**
- [ ] **验证服务层在返回实体之前填充属性**
- [ ] **确保控制器使用服务层**，而不是直接仓储访问
- [ ] **修复后再次测试特定页面**

#### **常见模板错误模式**

- `Property or field 'specialties' cannot be found` → 将`@JsonIgnore private List<Specialty> specialties`添加到Vet实体
- `Property or field 'pets' cannot be found` → 将`@JsonIgnore private List<Pet> pets`添加到Owner实体
- 显示空关系数据 → 服务未填充瞬态属性

### 步骤10 — **系统性错误解决过程**

#### 编译失败时：

1. **首先运行`mvn compile`** - 在测试之前修复主源代码问题
2. **然后运行`mvn test-compile`** - 系统地修复每个测试编译错误
3. **专注于最常见的错误模式**：
   - `int cannot be converted to String` → 更改测试常量和实体setter
   - `method X cannot be applied to given types` → 删除分页参数
   - `cannot find symbol: method Y()` → 更新为新的仓储方法名称
   - 方法签名冲突 → 重命名冲突方法

### 步骤11 — 验证清单

转换后，验证：

- [ ] **主应用程序编译**：`mvn compile`成功
- [ ] **所有测试文件编译**：`mvn test-compile`成功
- [ ] **无编译错误**：解决每个编译错误
- [ ] **应用程序成功启动**：`mvn spring-boot:run`无错误
- [ ] **所有网页加载**：浏览所有应用程序页面无运行时错误
- [ ] **服务层填充关系**：瞬态属性正确设置
- [ ] **所有模板页面无错误渲染**：浏览整个应用程序
- [ ] **关系数据正确显示**：列表、计数和相关对象正确显示
- [ ] **日志中无SpEL模板错误**：浏览期间检查应用程序日志
- [ ] **瞬态属性带有@JsonIgnore注解**：防止JSON序列化问题
- [ ] **一致使用服务层**：控制器中无直接仓储访问用于模板渲染
- [ ] 无剩余的`jakarta.persistence`导入
- [ ] 所有实体ID一致为`String`类型
- [ ] 所有仓储接口扩展`CosmosRepository<Entity, String>`
- [ ] 配置使用`DefaultAzureCredential`进行身份验证
- [ ] 数据种子组件存在并工作
- [ ] 测试文件一致使用String ID
- [ ] 仓储模拟更新为Cosmos方法
- [ ] **实体类中无方法签名冲突**
- [ ] **所有重命名的方法在调用者中更新**（控制器、测试、格式化程序）

### 要避免的常见陷阱

1. **不经常检查编译** - 每次重大更改后运行`mvn test-compile`
2. **方法签名冲突** - 转换ID类型时的方法重载问题
3. **忘记更新方法调用者** - 重命名方法时，更新所有调用者
4. **缺少仓储方法重命名** - 自定义仓储方法必须在所有调用的地方更新
5. **使用基于密钥的身份验证** - 改为使用`DefaultAzureCredential`
6. **混合Integer和String ID** - 各处保持使用String ID，特别是在测试中
7. **不更新控制器分页逻辑** - 当仓储更改时从控制器中删除分页
8. **保留JPA特定测试注解** - 替换为Cosmos兼容的替代方案
9. **测试文件更新不完整** - 搜索整个测试目录，不仅仅是明显的文件
10. **跳过运行时测试** - 始终测试运行的应用程序，而不仅仅是编译
11. **缺少服务层** - 不要直接从控制器访问仓储
12. **忘记瞬态属性** - 模板可能需要访问关系数据
13. **不测试模板导航** - 编译成功并不意味着模板工作
14. **模板缺少瞬态属性** - 模板需要对象访问，而不仅仅是ID
15. **服务层绕过** - 控制器必须使用服务，从不直接仓储访问
16. **关系填充不完整** - 服务方法必须填充模板使用的所有瞬态属性
17. **瞬态属性上忘记@JsonIgnore** - 防止序列化问题
18. **持久化字段上有@JsonIgnore** - **关键**：绝不要在需要存储在Cosmos DB的字段上使用`@JsonIgnore`
19. **身份验证序列化错误** - User/Authority实体必须完全可序列化，没有`@JsonIgnore`阻止必需字段
20. **BigDecimal反射问题** - 对JDK 17+兼容性使用替代数据类型或JVM参数
21. **仓储反应式类型转换** - 不要直接将`findAll()`转换为`List`，使用`StreamSupport.stream().collect(Collectors.toList())`
22. **健康检查数据库引用** - JPA删除后从Spring Boot健康检查中删除数据库依赖
23. **集合类型不匹配** - 更新服务方法以一致处理String vs 对象集合