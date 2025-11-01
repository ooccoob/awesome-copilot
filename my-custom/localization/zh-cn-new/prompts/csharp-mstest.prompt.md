---
mode: 'agent'
tools: ['changes', 'codebase', 'edit/editFiles', 'problems', 'search']
description: '获取MSTest单元测试最佳实践，包括数据驱动测试'
---

# MSTest最佳实践

您的目标是帮助我使用MSTest编写有效的单元测试，涵盖标准和数据驱动测试方法。

## 项目设置

- 使用命名约定`[ProjectName].Tests`的独立测试项目
- 引用MSTest包
- 创建与被测试类匹配的测试类（例如，`Calculator`对应`CalculatorTests`）
- 使用.NET SDK测试命令：`dotnet test`运行测试

## 测试结构

- 对测试类使用`[TestClass]`属性
- 对测试方法使用`[TestMethod]`属性
- 遵循Arrange-Act-Assert（AAA）模式
- 使用模式`MethodName_Scenario_ExpectedBehavior`命名测试
- 使用`[TestInitialize]`和`[TestCleanup]`进行每个测试的设置和清理
- 使用`[ClassInitialize]`和`[ClassCleanup]`进行每个类的设置和清理
- 使用`[AssemblyInitialize]`和`[AssemblyCleanup]`进行程序集级别的设置和清理

## 标准测试

- 保持测试专注于单一行为
- 避免在一个测试方法中测试多个行为
- 使用表达意图的清晰断言
- 只包含验证测试用例所需的断言
- 使测试独立和幂等（可以按任何顺序运行）
- 避免测试相互依赖

## 数据驱动测试

- 使用`[TestMethod]`结合数据源属性
- 使用`[DataRow]`进行内联测试数据
- 使用`[DynamicData]`进行程序生成的测试数据
- 使用`[TestProperty]`为测试添加元数据
- 在数据驱动测试中使用有意义的参数名

## 断言

- 使用`Assert.AreEqual`进行值相等性检查
- 使用`Assert.AreSame`进行引用相等性检查
- 使用`Assert.IsTrue`/`Assert.IsFalse`进行布尔条件检查
- 使用`CollectionAssert`进行集合比较
- 使用`StringAssert`进行字符串特定断言
- 使用`Assert.Throws<T>`测试异常
- 确保断言本质简单并提供失败时的清晰消息

## 模拟和隔离

- 考虑在MSTest旁边使用Moq或NSubstitute
- 模拟依赖项以隔离被测单元
- 使用接口促进模拟
- 考虑为复杂测试设置使用DI容器

## 测试组织

- 按功能或组件分组测试
- 使用`[TestCategory("Category")]`进行测试分类
- 使用`[Priority(1)]`为关键测试设置测试优先级
- 使用`[Owner("DeveloperName")]`指示所有权