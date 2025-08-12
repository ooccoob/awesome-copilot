---
applyTo: "quarkus.instructions.md"
---

<!-- 本文件为自动翻译，供参考。请结合实际需求进行校对和完善。-->

# Quarkus 开发规范与最佳实践

## 项目背景

- 最新 Quarkus 版本：3.x
- Java 17 及以上
- 用 Maven 或 Gradle 构建
- 强调架构清晰、可维护性和性能

## 开发标准

- 每个类、方法、复杂逻辑需有清晰注释
- 公共 API 和方法用 Javadoc
- 统一 Java 代码风格
- 遵循 Quarkus 官方最佳实践
- 遵循 Jakarta EE 和 MicroProfile 规范，包结构清晰
- 合理用 Java 17+ 新特性（如 record、sealed class）

## 命名规范

- 类名 PascalCase
- 方法/变量 camelCase
- 常量 ALL_CAPS

## Quarkus 相关

- 用 `@ApplicationScoped` 代替 `@Singleton`
- 用 `@Inject` 注入依赖
- 优先用 Panache repository
- 数据修改方法加 `@Transactional`
- REST 资源用 `@Path` 明确路径
- REST 资源用 `@Consumes`/`@Produces` 明确类型

### REST 资源

- 用 JAX-RS 注解
- 返回合适 HTTP 状态码
- 复杂响应用 Response 类
- 错误处理用 try-catch
- 输入参数用 Bean Validation
- 公共接口建议限流

### 数据访问

- 优先用 PanacheEntity
- 复杂查询用 PanacheRepository
- 数据修改加 `@Transactional`
- 复杂操作用命名查询
- 列表接口实现分页

### 配置

- 用 application.properties/yaml
- 用 `@ConfigProperty` 类型安全配置
- 敏感数据用环境变量
- 用 profile 区分环境

### 测试

- 用 `@QuarkusTest` 做集成测试
- 用 JUnit 5 做单元测试
- 用 `@QuarkusIntegrationTest` 做原生测试
- 外部依赖用 `@QuarkusTestResource` mock
- REST 测试用 RestAssured
- 数据修改测试加 `@Transactional`
- 数据库集成测试用 test-containers

### 禁止用法

- 测试中禁用字段注入（用构造注入）
- 禁止硬编码配置
- 禁止忽略异常

## 开发流程

1. 建实体，校验
2. 建 repository
3. 建 service
4. 建 REST 资源
5. 写测试
6. 加错误处理
7. 补文档

## 安全建议

- 用 Quarkus Security 扩展
- 实现基于角色的访问控制
- 校验所有输入参数

---

免责声明：本翻译仅供参考，具体实践请结合实际项目需求和最新官方文档。
