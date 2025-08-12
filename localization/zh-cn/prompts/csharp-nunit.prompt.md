---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems", "search"]
description: "获取 NUnit 单元测试最佳实践（含数据驱动测试）"
---

# NUnit 最佳实践

你的目标是帮助我使用 NUnit 编写高质量单元测试，涵盖标准测试与数据驱动测试。

## 项目设置

- 使用独立测试项目，命名约定为 `[ProjectName].Tests`
- 引用 Microsoft.NET.Test.Sdk、NUnit、NUnit3TestAdapter
- 按被测类进行测试类命名（如 `Calculator` → `CalculatorTests`）
- 使用 .NET SDK 测试命令：`dotnet test`

## 测试结构

- 测试类使用 `[TestFixture]`
- 测试方法使用 `[Test]`
- 遵循 AAA（Arrange-Act-Assert）模式
- 测试命名：`方法名_场景_期望行为`
- 每个测试前后置：`[SetUp]` / `[TearDown]`
- 类级前后置：`[OneTimeSetUp]` / `[OneTimeTearDown]`
- 程序集级前后置：`[SetUpFixture]`

## 标准测试

- 聚焦单一行为
- 避免在一个测试方法中覆盖多个行为
- 使用清晰的断言表达意图
- 只保留验证该用例所需的断言
- 测试应独立且幂等，可任意顺序执行
- 避免测试间相互依赖

## 数据驱动测试

- 内联数据：`[TestCase]`
- 生成型数据：`[TestCaseSource]`
- 简单取值组合：`[Values]`
- 基于属性/方法的数据源：`[ValueSource]`
- 随机值：`[Random]`
- 数值区间：`[Range]`
- 多参数组合：`[Combinatorial]` / `[Pairwise]`

## 断言

- 首选约束模型：`Assert.That(..., Is.EqualTo(...))` 等
- 经典风格：`Assert.AreEqual` 等
- 集合：`CollectionAssert`
- 字符串：`StringAssert`
- 异常：`Assert.Throws<T>` / `Assert.ThrowsAsync<T>`
- 为断言添加描述性消息提升可读性

## Mock 与隔离

- 可搭配 Moq 或 NSubstitute
- 对依赖进行 Mock 以隔离被测单元
- 借助接口以便于 Mock
- 复杂场景可考虑 DI 容器

## 测试组织

- 按功能/组件分组
- 类别：`[Category("CategoryName")]`
- 执行顺序：`[Order]`（必要时）
- 作者：`[Author("DeveloperName")]`
- 描述：`[Description]`
- 显式：`[Explicit]`（不自动执行）
- 暂停：`[Ignore("Reason")]`

```

```
