---
mode: 'agent'
tools: ['changes', 'codebase', 'edit/editFiles', 'problems', 'search']
description: '获取XUnit单元测试最佳实践，包括数据驱动测试'
---

# XUnit最佳实践

您的目标是帮助我使用XUnit编写有效的单元测试，涵盖标准和数据驱动测试方法。

## 项目设置

- 使用命名约定`[ProjectName].Tests`的独立测试项目
- 引用Microsoft.NET.Test.Sdk、xunit和xunit.runner.visualstudio包
- 创建与被测试类匹配的测试类（例如，`Calculator`对应`CalculatorTests`）
- 使用.NET SDK测试命令：`dotnet test`运行测试

## 测试结构

- 不需要测试类属性（不像MSTest/NUnit）
- 对简单测试使用基于事实的测试和`[Fact]`属性
- 遵循Arrange-Act-Assert（AAA）模式
- 使用模式`MethodName_Scenario_ExpectedBehavior`命名测试
- 使用构造函数进行设置，使用`IDisposable.Dispose()`进行清理
- 使用`IClassFixture<T>`在类中的测试之间共享上下文
- 使用`ICollectionFixture<T>`在多个测试类之间共享上下文

## 标准测试

- 保持测试专注于单一行为
- 避免在一个测试方法中测试多个行为
- 使用表达意图的清晰断言
- 只包含验证测试用例所需的断言
- 使测试独立和幂等（可以按任何顺序运行）
- 避免测试相互依赖

## 数据驱动测试

- 使用`[Theory]`结合数据源属性
- 使用`[InlineData]`进行内联测试数据
- 使用`[MemberData]`进行基于方法的测试数据
- 使用`[ClassData]`进行基于类的测试数据
- 通过实现`DataAttribute`创建自定义数据属性
- 在数据驱动测试中使用有意义的参数名

## 断言

- 使用`Assert.Equal`进行值相等性检查
- 使用`Assert.Same`进行引用相等性检查
- 使用`Assert.True`/`Assert.False`进行布尔条件检查
- 使用`Assert.Contains`/`Assert.DoesNotContain`进行集合检查
- 使用`Assert.Matches`/`Assert.DoesNotMatch`进行正则表达式模式匹配
- 使用`Assert.Throws<T>`或`await Assert.ThrowsAsync<T>`测试异常
- 使用流式断言库获得更可读的断言

## 模拟和隔离

- 考虑在XUnit旁边使用Moq或NSubstitute
- 模拟依赖项以隔离被测单元
- 使用接口促进模拟
- 考虑为复杂测试设置使用DI容器

## 测试组织

- 按功能或组件分组测试
- 使用`[Trait("Category", "CategoryName")]`进行分类
- 使用集合夹具对具有共享依赖的测试进行分组
- 考虑使用输出助手（`ITestOutputHelper`）进行测试诊断
- 在fact/theory属性中使用`Skip = "reason"`有条件地跳过测试