---
代理人：“代理人”
工具：['更改'、'搜索/代码库'、'编辑/编辑文件'、'问题'、'搜索']
描述：“获取 XUnit 单元测试的最佳实践，包括数据驱动测试”
---

# XUnit 最佳实践

您的目标是帮助我使用 XUnit 编写有效的单元测试，涵盖标准和数据驱动的测试方法。

## 项目设置

- 使用命名约定 `[ProjectName].Tests` 的单独测试项目
- 参考 Microsoft.NET.Test.Sdk、xunit 和 xunit.runner.visualstudio 包
- 创建与正在测试的类匹配的测试类（例如，`CalculatorTests` 对应 `Calculator`）
- 使用.NET SDK测试命令：`dotnet test`来运行测试

## 测试结构

- 不需要测试类属性（与 MSTest/NUnit 不同）
- 使用带有 `[Fact]` 属性的基于事实的测试进行简单测试
- 遵循排列-执行-断言 (AAA) 模式
- 使用模式 `MethodName_Scenario_ExpectedBehavior` 命名测试
- 使用构造函数进行设置，使用 `IDisposable.Dispose()` 进行拆卸
- 使用 `IClassFixture<T>` 在类中的测试之间共享上下文
- 使用 `ICollectionFixture<T>` 在多个测试类之间共享上下文

## 标准测试

- 让测试集中于单一行为
- 避免在一种测试方法中测试多种行为
- 使用明确的断言来表达意图
- 仅包含验证测试用例所需的断言
- 使测试独立且幂等（可以按任何顺序运行）
- 避免测试相互依赖

## 数据驱动测试

- 结合数据源属性使用 `[Theory]`
- 使用 `[InlineData]` 进行内联测试数据
- 对基于方法的测试数据使用 `[MemberData]`
- 对基于类的测试数据使用 `[ClassData]`
- 通过实现 `DataAttribute` 创建自定义数据属性
- 在数据驱动测试中使用有意义的参数名称

## 断言

- 使用 `Assert.Equal` 实现值相等
- 使用 `Assert.Same` 实现引用相等
- 使用 `Assert.True`/`Assert.False` 作为布尔条件
- 使用 `Assert.Contains`/`Assert.DoesNotContain` 进行集合
- 使用 `Assert.Matches`/`Assert.DoesNotMatch` 进行正则表达式模式匹配
- 使用 `Assert.Throws<T>` 或 `await Assert.ThrowsAsync<T>` 来测试异常
- 使用流畅的断言库以获得更具可读性的断言

## 模拟和隔离

- 考虑将 Moq 或 NSubstitute 与 XUnit 一起使用
- 模拟依赖关系以隔离被测单元
- 使用接口来促进模拟
- 考虑使用 DI 容器进行复杂的测试设置

## 测试组织

- 按功能或组件对测试进行分组
- 使用 `[Trait("Category", "CategoryName")]` 进行分类
- 使用集合装置对具有共享依赖项的测试进行分组
- 考虑输出助手 (`ITestOutputHelper`) 进行测试诊断
- 使用 `Skip = "reason"` 事实上/理论属性有条件地跳过测试
