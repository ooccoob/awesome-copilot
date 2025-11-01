---
mode: 'agent'
tools: ['changes', 'codebase', 'edit/editFiles', 'problems', 'search']
description: '获取TUnit单元测试最佳实践，包括数据驱动测试'
---

# TUnit最佳实践

您的目标是帮助我使用TUnit编写有效的单元测试，涵盖标准和数据驱动测试方法。

## 项目设置

- 使用命名约定`[ProjectName].Tests`的独立测试项目
- 引用TUnit包和TUnit.Assertions用于流式断言
- 创建与被测试类匹配的测试类（例如，`Calculator`对应`CalculatorTests`）
- 使用.NET SDK测试命令：`dotnet test`运行测试
- TUnit需要.NET 8.0或更高版本

## 测试结构

- 不需要测试类属性（像xUnit/NUnit那样）
- 对测试方法使用`[Test]`属性（不是像xUnit那样的`[Fact]`）
- 遵循Arrange-Act-Assert（AAA）模式
- 使用模式`MethodName_Scenario_ExpectedBehavior`命名测试
- 使用生命周期钩子：`[Before(Test)]`用于设置，`[After(Test)]`用于清理
- 使用`[Before(Class)]`和`[After(Class)]`在类中的测试之间共享上下文
- 使用`[Before(Assembly)]`和`[After(Assembly)]`在测试类之间共享上下文
- TUnit支持高级生命周期钩子，如`[Before(TestSession)]`和`[After(TestSession)]`

## 标准测试

- 保持测试专注于单一行为
- 避免在一个测试方法中测试多个行为
- 使用TUnit的流式断言语法配合`await Assert.That()`
- 只包含验证测试用例所需的断言
- 使测试独立和幂等（可以按任何顺序运行）
- 避免测试相互依赖（如果需要使用`[DependsOn]`属性）

## 数据驱动测试

- 使用`[Arguments]`属性进行内联测试数据（等同于xUnit的`[InlineData]`）
- 使用`[MethodData]`进行基于方法的测试数据（等同于xUnit的`[MemberData]`）
- 使用`[ClassData]`进行基于类的测试数据
- 通过实现`ITestDataSource`创建自定义数据源
- 在数据驱动测试中使用有意义的参数名
- 可以对同一测试方法应用多个`[Arguments]`属性

## 断言

- 使用`await Assert.That(value).IsEqualTo(expected)`进行值相等性检查
- 使用`await Assert.That(value).IsSameReferenceAs(expected)`进行引用相等性检查
- 使用`await Assert.That(value).IsTrue()`或`await Assert.That(value).IsFalse()`进行布尔条件检查
- 使用`await Assert.That(collection).Contains(item)`或`await Assert.That(collection).DoesNotContain(item)`进行集合检查
- 使用`await Assert.That(value).Matches(pattern)`进行正则表达式模式匹配
- 使用`await Assert.That(action).Throws<TException>()`或`await Assert.That(asyncAction).ThrowsAsync<TException>()`测试异常
- 使用`.And`运算符链式断言：`await Assert.That(value).IsNotNull().And.IsEqualTo(expected)`
- 使用`.Or`运算符进行替代条件：`await Assert.That(value).IsEqualTo(1).Or.IsEqualTo(2)`
- 使用`.Within(tolerance)`进行DateTime和数值的容差比较
- 所有断言都是异步的，必须被await

## 高级功能

- 使用`[Repeat(n)]`多次重复测试
- 使用`[Retry(n)]`在失败时自动重试
- 使用`[ParallelLimit<T>]`控制并行执行限制
- 使用`[Skip("reason")]`有条件地跳过测试
- 使用`[DependsOn(nameof(OtherTest))]`创建测试依赖
- 使用`[Timeout(milliseconds)]`设置测试超时
- 通过扩展TUnit的基础属性创建自定义属性

## 测试组织

- 按功能或组件分组测试
- 使用`[Category("CategoryName")]`进行测试分类
- 使用`[DisplayName("Custom Test Name")]`自定义测试名称
- 考虑使用`TestContext`进行测试诊断和信息
- 对平台特定测试使用条件属性，如自定义`[WindowsOnly]`

## 性能和并行执行

- TUnit默认并行运行测试（不像xUnit需要显式配置）
- 使用`[NotInParallel]`禁用特定测试的并行执行
- 使用带有自定义限制类的`[ParallelLimit<T>]`控制并发
- 同一类中的测试默认顺序运行
- 使用`[Repeat(n)]`配合`[ParallelLimit<T>]`进行负载测试场景

## 从xUnit迁移

- 将`[Fact]`替换为`[Test]`
- 将`[Theory]`替换为`[Test]`，对数据使用`[Arguments]`
- 将`[InlineData]`替换为`[Arguments]`
- 将`[MemberData]`替换为`[MethodData]`
- 将`Assert.Equal`替换为`await Assert.That(actual).IsEqualTo(expected)`
- 将`Assert.True`替换为`await Assert.That(condition).IsTrue()`
- 将`Assert.Throws<T>`替换为`await Assert.That(action).Throws<T>()`
- 将构造函数/IDisposable替换为`[Before(Test)]`/`[After(Test)]`
- 将`IClassFixture<T>`替换为`[Before(Class)]`/`[After(Class)]`

**为什么选择TUnit而不是xUnit？**

TUnit提供现代、快速和灵活的测试体验，具有xUnit中不存在的高级功能，如异步断言、更精细的生命周期钩子和改进的数据驱动测试能力。TUnit的流式断言提供更清晰和更具表现力的测试验证，使其特别适合复杂的.NET项目。