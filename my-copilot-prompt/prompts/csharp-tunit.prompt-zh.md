---
代理人：“代理人”
工具：['更改'、'搜索/代码库'、'编辑/编辑文件'、'问题'、'搜索']
描述：“获取 TUnit 单元测试的最佳实践，包括数据驱动测试”
---

# TUnit 最佳实践

您的目标是帮助我使用 TUnit 编写有效的单元测试，涵盖标准和数据驱动的测试方法。

## 项目设置

- 使用命名约定 `[ProjectName].Tests` 的单独测试项目
- 参考 TUnit 包和 TUnit.Assertions 以实现流畅的断言
- 创建与正在测试的类匹配的测试类（例如，`CalculatorTests` 对应 `Calculator`）
- 使用.NET SDK测试命令：`dotnet test`来运行测试
- TUnit 需要 .NET 8.0 或更高版本

## 测试结构

- 不需要测试类属性（如 xUnit/NUnit）
- 对测试方法使用 `[Test]` 属性（不像 xUnit 那样使用 `[Fact]`）
- 遵循排列-执行-断言 (AAA) 模式
- 使用模式 `MethodName_Scenario_ExpectedBehavior` 命名测试
- 使用生命周期挂钩：`[Before(Test)]` 用于设置，`[After(Test)]` 用于拆卸
- 使用 `[Before(Class)]` 和 `[After(Class)]` 在类中的测试之间共享上下文
- 使用 `[Before(Assembly)]` 和 `[After(Assembly)]` 跨测试类共享上下文
- TUnit 支持高级生命周期挂钩，例如 `[Before(TestSession)]` 和 `[After(TestSession)]`

## 标准测试

- 让测试集中于单一行为
- 避免在一种测试方法中测试多种行为
- 将 TUnit 的流畅断言语法与 `await Assert.That()` 结合使用
- 仅包含验证测试用例所需的断言
- 使测试独立且幂等（可以按任何顺序运行）
- 避免测试相互依赖（如果需要，使用 `[DependsOn]` 属性）

## 数据驱动测试

- 对内联测试数据使用 `[Arguments]` 属性（相当于 xUnit 的 `[InlineData]`）
- 将 `[MethodData]` 用于基于方法的测试数据（相当于 xUnit 的 `[MemberData]`）
- 对基于类的测试数据使用 `[ClassData]`
- 通过实施 `ITestDataSource` 创建自定义数据源
- 在数据驱动测试中使用有意义的参数名称
- 多个 `[Arguments]` 属性可以应用于同一个测试方法

## 断言

- 使用 `await Assert.That(value).IsEqualTo(expected)` 实现值相等
- 使用 `await Assert.That(value).IsSameReferenceAs(expected)` 实现引用相等
- 使用 `await Assert.That(value).IsTrue()` 或 `await Assert.That(value).IsFalse()` 作为布尔条件
- 使用 `await Assert.That(collection).Contains(item)` 或 `await Assert.That(collection).DoesNotContain(item)` 进行集合
- 使用 `await Assert.That(value).Matches(pattern)` 进行正则表达式模式匹配
- 使用 `await Assert.That(action).Throws<TException>()` 或 `await Assert.That(asyncAction).ThrowsAsync<TException>()` 来测试异常
- 使用 `.And` 运算符进行链式断言：`await Assert.That(value).IsNotNull().And.IsEqualTo(expected)`
- 使用 `.Or` 运算符作为替代条件：`await Assert.That(value).IsEqualTo(1).Or.IsEqualTo(2)`
- 使用 `.Within(tolerance)` 进行日期时间和数字与公差的比较
- 所有断言都是异步的并且必须等待

## 高级功能

- 使用 `[Repeat(n)]` 多次重复测试
- 使用 `[Retry(n)]` 在失败时自动重试
- 使用 `[ParallelLimit<T>]` 控制并行执行限制
- 使用 `[Skip("reason")]` 有条件地跳过测试
- 使用 `[DependsOn(nameof(OtherTest))]` 创建测试依赖项
- 使用 `[Timeout(milliseconds)]` 设置测试超时
- 通过扩展 TUnit 的基本属性来创建自定义属性

## 测试组织

- 按功能或组件对测试进行分组
- 使用 `[Category("CategoryName")]` 进行测试分类
- 使用 `[DisplayName("Custom Test Name")]` 作为自定义测试名称
- 考虑使用 `TestContext` 进行测试诊断和信息
- 使用条件属性（如自定义 `[WindowsOnly]`）进行特定于平台的测试

## 性能和并行执行

- TUnit 默认情况下并行运行测试（与需要显式配置的 xUnit 不同）
- 使用 `[NotInParallel]` 禁用特定测试的并行执行
- 使用 `[ParallelLimit<T>]` 和自定义限制类来控制并发
- 默认情况下，同一类中的测试按顺序运行
- 将 `[Repeat(n)]` 与 `[ParallelLimit<T>]` 结合使用用于负载测试场景

## 从 xUnit 迁移

- 将 `[Fact]` 替换为 `[Test]`
- 将 `[Theory]` 替换为 `[Test]` 并使用 `[Arguments]` 作为数据
- 将 `[InlineData]` 替换为 `[Arguments]`
- 将 `[MemberData]` 替换为 `[MethodData]`
- 将 `Assert.Equal` 替换为 `await Assert.That(actual).IsEqualTo(expected)`
- 将 `Assert.True` 替换为 `await Assert.That(condition).IsTrue()`
- 将 `Assert.Throws<T>` 替换为 `await Assert.That(action).Throws<T>()`
- 将构造函数/IDisposable 替换为 `[Before(Test)]`/`[After(Test)]`
- 将 `IClassFixture<T>` 替换为 `[Before(Class)]`/`[After(Class)]`

**为什么选择 TUnit 而不是 xUnit？**

TUnit 提供了现代、快速且灵活的测试体验，以及 xUnit 中不存在的高级功能，例如异步断言、更精细的生命周期挂钩以及改进的数据驱动测试功能。 TUnit 流畅的断言提供了更清晰、更具表现力的测试验证，使其特别适合复杂的 .NET 项目。
