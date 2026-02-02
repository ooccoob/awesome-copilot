---
agent: 'agent'
tools: ['changes', 'search/codebase', 'edit/editFiles', 'problems', 'search']
description: 'Get best practices for MSTest unit testing, including data-driven tests'
---

# MSTest 最佳实践

您的目标是帮助我使用 MSTest 编写有效的单元测试，涵盖标准和数据驱动的测试方法。

## 项目设置

- 使用命名约定 `[ProjectName].Tests` 的单独测试项目
- 参考MSTest包
- 创建与正在测试的类匹配的测试类（例如，`CalculatorTests` 对应 `Calculator`）
- 使用.NET SDK测试命令：`dotnet test`来运行测试

## 测试结构

- 对测试类使用 `[TestClass]` 属性
- 对测试方法使用 `[TestMethod]` 属性
- 遵循排列-执行-断言 (AAA) 模式
- 使用模式 `MethodName_Scenario_ExpectedBehavior` 命名测试
- 使用 `[TestInitialize]` 和 `[TestCleanup]` 进行每次测试设置和拆卸
- 使用 `[ClassInitialize]` 和 `[ClassCleanup]` 进行每个类的设置和拆卸
- 使用 `[AssemblyInitialize]` 和 `[AssemblyCleanup]` 进行汇编级设置和拆卸

## 标准测试

- 让测试集中于单一行为
- 避免在一种测试方法中测试多种行为
- 使用明确的断言来表达意图
- 仅包含验证测试用例所需的断言
- 使测试独立且幂等（可以按任何顺序运行）
- 避免测试相互依赖

## 数据驱动测试

- 结合数据源属性使用 `[TestMethod]`
- 使用 `[DataRow]` 进行内联测试数据
- 使用 `[DynamicData]` 以编程方式生成测试数据
- 使用 `[TestProperty]` 将元数据添加到测试中
- 在数据驱动测试中使用有意义的参数名称

## 断言

- 使用 `Assert.AreEqual` 实现值相等
- 使用 `Assert.AreSame` 实现引用相等
- 使用 `Assert.IsTrue`/`Assert.IsFalse` 作为布尔条件
- 使用 `CollectionAssert` 进行集合比较
- 使用 `StringAssert` 进行特定于字符串的断言
- 使用 `Assert.Throws<T>` 测试异常
- 确保断言本质上简单，并提供一条消息以明确失败情况

## 模拟和隔离

- 考虑将 Moq 或 NSubstitute 与 MSTest 一起使用
- 模拟依赖关系以隔离被测单元
- 使用接口来促进模拟
- 考虑使用 DI 容器进行复杂的测试设置

## 测试组织

- 按功能或组件对测试进行分组
- 使用带有 `[TestCategory("Category")]` 的测试类别
- 使用 `[Priority(1)]` 的测试优先级进行关键测试
- 使用 `[Owner("DeveloperName")]` 表示所有权
