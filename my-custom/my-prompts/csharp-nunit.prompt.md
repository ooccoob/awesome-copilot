---
agent: 'agent'
tools: ['changes', 'search/codebase', 'edit/editFiles', 'problems', 'search']
description: 'Get best practices for NUnit unit testing, including data-driven tests'
---

# NUnit 最佳实践

您的目标是帮助我使用 NUnit 编写有效的单元测试，涵盖标准和数据驱动的测试方法。

## 项目设置

- 使用命名约定 `[ProjectName].Tests` 的单独测试项目
- 参考 Microsoft.NET.Test.Sdk、NUnit 和 NUnit3TestAdapter 包
- 创建与正在测试的类匹配的测试类（例如，`CalculatorTests` 对应 `Calculator`）
- 使用.NET SDK测试命令：`dotnet test`来运行测试

## 测试结构

- 将 `[TestFixture]` 属性应用于测试类
- 对测试方法使用 `[Test]` 属性
- 遵循排列-执行-断言 (AAA) 模式
- 使用模式 `MethodName_Scenario_ExpectedBehavior` 命名测试
- 使用 `[SetUp]` 和 `[TearDown]` 进行每次测试设置和拆卸
- 使用 `[OneTimeSetUp]` 和 `[OneTimeTearDown]` 进行每个类的设置和拆卸
- 使用 `[SetUpFixture]` 进行汇编级设置和拆卸

## 标准测试

- 让测试集中于单一行为
- 避免在一种测试方法中测试多种行为
- 使用明确的断言来表达意图
- 仅包含验证测试用例所需的断言
- 使测试独立且幂等（可以按任何顺序运行）
- 避免测试相互依赖

## 数据驱动测试

- 使用 `[TestCase]` 进行内联测试数据
- 使用 `[TestCaseSource]` 以编程方式生成测试数据
- 使用 `[Values]` 进行简单的参数组合
- 对基于属性或方法的数据源使用 `[ValueSource]`
- 使用 `[Random]` 获取随机数字测试值
- 使用 `[Range]` 表示连续的数字测试值
- 使用 `[Combinatorial]` 或 `[Pairwise]` 组合多个参数

## 断言

- 将 `Assert.That` 与约束模型一起使用（首选 NUnit 样式）
- 使用 `Is.EqualTo`、`Is.SameAs`、`Contains.Item` 等约束
- 使用 `Assert.AreEqual` 实现简单的值相等（经典风格）
- 使用 `CollectionAssert` 进行集合比较
- 使用 `StringAssert` 进行特定于字符串的断言
- 使用 `Assert.Throws<T>` 或 `Assert.ThrowsAsync<T>` 来测试异常
- 在断言中使用描述性消息以清楚地了解失败

## 模拟和隔离

- 考虑将 Moq 或 NSubstitute 与 NUnit 一起使用
- 模拟依赖关系以隔离被测单元
- 使用接口来促进模拟
- 考虑使用 DI 容器进行复杂的测试设置

## 测试组织

- 按功能或组件对测试进行分组
- 使用带有 `[Category("CategoryName")]` 的类别
- 必要时使用 `[Order]` 控制测试执行顺序
- 使用 `[Author("DeveloperName")]` 表示所有权
- 使用 `[Description]` 提供额外的测试信息
- 对于不应自动运行的测试，请考虑使用 `[Explicit]`
- 使用 `[Ignore("Reason")]` 暂时跳过测试
