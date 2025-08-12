---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems", "search"]
description: "获取 xUnit 单元测试最佳实践（含数据驱动测试）"
---

# xUnit 最佳实践

你的目标是帮助我使用 xUnit 编写高质量单元测试，涵盖标准测试与数据驱动测试。

## 项目设置

- 使用独立测试项目，命名约定为 `[ProjectName].Tests`
- 引用 Microsoft.NET.Test.Sdk、xunit、xunit.runner.visualstudio
- 按被测类进行测试类命名（如 `Calculator` → `CalculatorTests`）
- 使用 .NET SDK 测试命令：`dotnet test`

## 测试结构

- 无需类级特性（不同于 MSTest/NUnit）
- 简单测试使用 `[Fact]`
- 遵循 AAA（Arrange-Act-Assert）模式
- 测试命名：`方法名_场景_期望行为`
- 使用构造函数进行初始化，`IDisposable.Dispose()` 做清理
- 共享上下文（类级）：`IClassFixture<T>`
- 共享上下文（跨类）：`ICollectionFixture<T>`

## 标准测试

- 聚焦单一行为
- 避免在一个测试方法中覆盖多个行为
- 使用清晰的断言表达意图
- 只保留验证该用例所需的断言
- 测试应独立且幂等，可任意顺序执行
- 避免测试间相互依赖

## 数据驱动测试

- 使用 `[Theory]` 搭配数据源特性
- 内联数据：`[InlineData]`
- 方法数据：`[MemberData]`
- 类数据：`[ClassData]`
- 可实现 `DataAttribute` 自定义数据源
- 使用有意义的参数名

## 断言

- 值相等：`Assert.Equal`
- 引用相等：`Assert.Same`
- 布尔：`Assert.True` / `Assert.False`
- 集合：`Assert.Contains` / `Assert.DoesNotContain`
- 正则：`Assert.Matches` / `Assert.DoesNotMatch`
- 异常：`Assert.Throws<T>` / `await Assert.ThrowsAsync<T>`
- 可选使用 FluentAssertions 提升可读性

## Mock 与隔离

- 可搭配 Moq 或 NSubstitute
- 对依赖进行 Mock 以隔离被测单元
- 借助接口以便于 Mock
- 复杂场景可考虑 DI 容器

## 测试组织

- 按功能/组件分组
- 分类：`[Trait("Category", "CategoryName")]`
- 使用集合夹具组织共享依赖
- 输出辅助：`ITestOutputHelper`
- 条件跳过：在 `[Fact]`/`[Theory]` 上设置 `Skip = "reason"`

```

```
