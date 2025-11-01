---
mode: 'agent'
tools: ['changes', 'codebase', 'edit/editFiles', 'problems', 'search']
description: '获取NUnit单元测试最佳实践，包括数据驱动测试'
---

# NUnit最佳实践

您的目标是帮助我使用NUnit编写有效的单元测试，涵盖标准和数据驱动测试方法。

## 项目设置

- 使用命名约定`[ProjectName].Tests`的独立测试项目
- 引用Microsoft.NET.Test.Sdk、NUnit和NUnit3TestAdapter包
- 创建与被测试类匹配的测试类（例如，`Calculator`对应`CalculatorTests`）
- 使用.NET SDK测试命令：`dotnet test`运行测试

## 测试结构

- 对测试类应用`[TestFixture]`属性
- 对测试方法使用`[Test]`属性
- 遵循Arrange-Act-Assert（AAA）模式
- 使用模式`MethodName_Scenario_ExpectedBehavior`命名测试
- 使用`[SetUp]`和`[TearDown]`进行每个测试的设置和清理
- 使用`[OneTimeSetUp]`和`[OneTimeTearDown]`进行每个类的设置和清理
- 使用`[SetUpFixture]`进行程序集级别的设置和清理

## 标准测试

- 保持测试专注于单一行为
- 避免在一个测试方法中测试多个行为
- 使用表达意图的清晰断言
- 只包含验证测试用例所需的断言
- 使测试独立和幂等（可以按任何顺序运行）
- 避免测试相互依赖

## 数据驱动测试

- 使用`[TestCase]`进行内联测试数据
- 使用`[TestCaseSource]`进行程序生成的测试数据
- 使用`[Values]`进行简单参数组合
- 使用`[ValueSource]`进行基于属性或方法的数据源
- 使用`[Random]`进行随机数值测试值
- 使用`[Range]`进行顺序数值测试值
- 使用`[Combinatorial]`或`[Pairwise]`组合多个参数

## 断言

- 使用约束模型的`Assert.That`（首选NUnit风格）
- 使用如`Is.EqualTo`、`Is.SameAs`、`Contains.Item`等约束
- 使用`Assert.AreEqual`进行简单值相等性检查（经典风格）
- 使用`CollectionAssert`进行集合比较
- 使用`StringAssert`进行字符串特定断言
- 使用`Assert.Throws<T>`或`Assert.ThrowsAsync<T>`测试异常
- 在断言中使用描述性消息以便失败时清晰明了

## 模拟和隔离

- 考虑在NUnit旁边使用Moq或NSubstitute
- 模拟依赖项以隔离被测单元
- 使用接口促进模拟
- 考虑为复杂测试设置使用DI容器

## 测试组织

- 按功能或组件分组测试
- 使用`[Category("CategoryName")]`进行分类
- 在必要时使用`[Order]`控制测试执行顺序
- 使用`[Author("DeveloperName")]`指示所有权
- 使用`[Description]`提供额外测试信息
- 考虑对不应自动运行的测试使用`[Explicit]`
- 使用`[Ignore("Reason")]`临时跳过测试