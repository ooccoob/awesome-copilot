---
mode: 'agent'
tools: ['changes', 'codebase', 'edit/editFiles', 'problems', 'search']
description: '获取JUnit 5单元测试的最佳实践，包括数据驱动测试'
---

# JUnit 5+最佳实践

您的目标是帮助我使用JUnit 5编写有效的单元测试，涵盖标准和数据驱动测试方法。

## 项目设置

- 使用标准Maven或Gradle项目结构。
- 将测试源代码放在`src/test/java`中。
- 包含`junit-jupiter-api`、`junit-jupiter-engine`和`junit-jupiter-params`（用于参数化测试）的依赖项。
- 使用构建工具命令运行测试：`mvn test`或`gradle test`。

## 测试结构

- 测试类应具有`Test`后缀，例如`Calculator`类的`CalculatorTest`。
- 对测试方法使用`@Test`。
- 遵循Arrange-Act-Assert（AAA）模式。
- 使用描述性约定命名测试，如`methodName_should_expectedBehavior_when_scenario`。
- 对每个测试的设置和清理使用`@BeforeEach`和`@AfterEach`。
- 对每个类的设置和清理使用`@BeforeAll`和`@AfterAll`（必须是静态方法）。
- 使用`@DisplayName`为测试类和方法提供人类可读的名称。

## 标准测试

- 保持测试专注于单一行为。
- 避免在一个测试方法中测试多个条件。
- 使测试独立和幂等（可以按任何顺序运行）。
- 避免测试相互依赖。

## 数据驱动（参数化）测试

- 使用`@ParameterizedTest`将方法标记为参数化测试。
- 对简单字面值（字符串、整数等）使用`@ValueSource`。
- 使用`@MethodSource`引用提供测试参数作为`Stream`、`Collection`等的工厂方法。
- 对内联逗号分隔值使用`@CsvSource`。
- 使用`@CsvFileSource`从类路径使用CSV文件。
- 使用`@EnumSource`使用枚举常量。

## 断言

- 使用`org.junit.jupiter.api.Assertions`的静态方法（例如`assertEquals`、`assertTrue`、`assertNotNull`）。
- 为了更流畅和可读的断言，考虑使用像AssertJ这样的库（`assertThat(...).is...`）。
- 使用`assertThrows`或`assertDoesNotThrow`测试异常。
- 使用`assertAll`分组相关断言，以确保在测试失败之前检查所有断言。
- 在断言中使用描述性消息以提供失败的清晰度。

## 模拟和隔离

- 使用像Mockito这样的模拟框架为依赖项创建模拟对象。
- 使用Mockito的`@Mock`和`@InjectMocks`注解简化模拟创建和注入。
- 使用接口促进模拟。

## 测试组织

- 使用包按功能或组件分组测试。
- 使用`@Tag`对测试进行分类（例如`@Tag("fast")`、`@Tag("integration")`）。
- 在严格必要时使用`@TestMethodOrder(MethodOrderer.OrderAnnotation.class)`和`@Order`控制测试执行顺序。
- 使用`@Disabled`暂时跳过测试方法或类，提供原因。
- 使用`@Nested`在嵌套内部类中分组测试以获得更好的组织和结构。