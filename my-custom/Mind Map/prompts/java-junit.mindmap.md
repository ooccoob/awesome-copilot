## What
- JUnit 5 单元测试最佳实践：结构、参数化、断言、Mock、组织与标签。

## When
- 为类/服务编写可靠、可维护的单测与小型集成测试时。

## Why
- 增强可读性与稳定性，改进反馈速度与覆盖面。

## How
- 结构：Test 后缀；@Test；AAA 模式；@DisplayName
- 生命周期：@BeforeEach/@AfterEach；@BeforeAll/@AfterAll
- 参数化：@ParameterizedTest + Value/Method/Csv/CsvFile/EnumSource
- 断言：Assertions + assertAll/throws；可选 AssertJ
- Mock：Mockito @Mock/@InjectMocks；接口友好
- 组织：包按功能；@Tag/@Nested；必要时排序/禁用

## Key points (CN)
- 测试独立、幂等；避免相互依赖
- 描述性命名：method_should_expected_when_scenario
- 失败信息清晰

## Key points (EN)
- Parameterized tests; grouped assertions
- Mockito-based isolation; tagging and nesting
- Clear naming and independence

## Example questions
- “为 Calculator.add 编写参数化测试（CSV）并断言异常？”
- “如何使用 @Nested 组织复杂用例组？”

## 思维导图（要点）
- 结构/生命周期
- 参数化/断言
- Mock/组织/标签

—
- Source: d:\mycode\awesome-copilot\prompts\java-junit.prompt.md
- Generated: 2025-10-17
