---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems", "search"]
description: "获取 JUnit 5 单元测试最佳实践（含参数化测试）"
---

# JUnit 5+ 最佳实践

你的目标是帮助我使用 JUnit 5 编写高质量单元测试，覆盖标准与参数化测试方法。

## 项目设置

- 使用标准 Maven/Gradle 结构
- 测试代码放在 `src/test/java`
- 引入依赖：`junit-jupiter-api`、`junit-jupiter-engine`、`junit-jupiter-params`
- 使用构建工具命令运行测试：`mvn test` 或 `gradle test`

## 测试结构

- 测试类以 `Test` 结尾（如 `Calculator` → `CalculatorTests`）
- 测试方法标注 `@Test`
- 遵循 AAA（Arrange-Act-Assert）模式
- 命名：`methodName_should_expectedBehavior_when_scenario`
- 每个测试的前后置：`@BeforeEach` / `@AfterEach`
- 类级前后置（静态方法）：`@BeforeAll` / `@AfterAll`
- 使用 `@DisplayName` 提供可读名称

## 标准测试

- 聚焦单一行为
- 避免单个测试方法覆盖多种情况
- 测试应独立且幂等（可任意顺序运行）
- 避免测试间依赖

## 参数化测试

- 使用 `@ParameterizedTest` 标注参数化测试
- 简单字面量：`@ValueSource`
- 方法提供参数：`@MethodSource`（返回 `Stream`、`Collection` 等）
- 内联 CSV：`@CsvSource`
- 外部 CSV：`@CsvFileSource`
- 枚举常量：`@EnumSource`

## 断言

- 使用 `org.junit.jupiter.api.Assertions` 的静态方法（`assertEquals`、`assertTrue`、`assertNotNull` 等）
- 可选：使用 AssertJ 提升可读性（`assertThat(...).is...`）
- 异常验证：`assertThrows` / `assertDoesNotThrow`
- 组合断言：`assertAll`（确保相关断言全部执行）
- 断言添加描述信息以便定位失败原因

## Mock 与隔离

- 使用 Mockito 等框架创建 Mock
- 使用 `@Mock` 与 `@InjectMocks` 简化 Mock 创建与注入
- 借助接口抽象以便于 Mock

## 测试组织

- 按功能/组件分包管理
- 分类：`@Tag`（如 `@Tag("fast")`、`@Tag("integration")`）
- 必要时控制顺序：`@TestMethodOrder(OrderAnnotation.class)` + `@Order`
- 临时跳过：`@Disabled`（给出原因）
- 使用 `@Nested` 组织内嵌测试类

```

```
