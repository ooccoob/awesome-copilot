---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems", "search"]
description: "获取 TUnit 单元测试最佳实践（含数据驱动测试）"
---

# TUnit 最佳实践

你的目标是帮助我使用 TUnit 编写高质量单元测试，涵盖标准测试与数据驱动测试。

## 项目设置

- 使用独立测试项目，命名约定为 `[ProjectName].Tests`
- 引用 TUnit 与 TUnit.Assertions（用于流式断言）
- 按被测类进行测试类命名（如 `Calculator` → `CalculatorTests`）
- 使用 .NET SDK 测试命令：`dotnet test`
- 需要 .NET 8.0 或更高版本

## 测试结构

- 无需类级特性（不同于 xUnit/NUnit）
- 测试方法使用 `[Test]`（不是 xUnit 的 `[Fact]`）
- 遵循 AAA（Arrange-Act-Assert）模式
- 测试命名：`方法名_场景_期望行为`
- 生命周期钩子：`[Before(Test)]` / `[After(Test)]`
- 类级共享上下文：`[Before(Class)]` / `[After(Class)]`
- 程序集级共享上下文：`[Before(Assembly)]` / `[After(Assembly)]`
- 还支持 `[Before(TestSession)]` / `[After(TestSession)]`

## 标准测试

- 聚焦单一行为
  n- 使用 TUnit 的异步流式断言：`await Assert.That()`
- 只保留验证该用例所需的断言
- 测试应独立且幂等，可任意顺序执行
- 避免测试间相互依赖（必要时可使用 `[DependsOn]`）

## 数据驱动测试

- 内联数据：`[Arguments]`（对应 xUnit 的 `[InlineData]`）
- 方法数据：`[MethodData]`（对应 xUnit 的 `[MemberData]`）
- 类数据：`[ClassData]`
- 可实现 `ITestDataSource` 定制数据源
- 参数命名应清晰有意义
- 可对同一测试方法应用多个 `[Arguments]`

## 断言

- 值相等：`await Assert.That(value).IsEqualTo(expected)`
- 引用相等：`await Assert.That(value).IsSameReferenceAs(expected)`
- 布尔：`await Assert.That(value).IsTrue()` / `IsFalse()`
- 集合包含：`await Assert.That(collection).Contains(item)` / `DoesNotContain(item)`
- 正则匹配：`await Assert.That(value).Matches(pattern)`
- 异常：`await Assert.That(action).Throws<TException>()` / `ThrowsAsync<TException>()`
- 链式：`.And` 与 `.Or`
- 容差：`.Within(tolerance)`（日期/数值）
- 所有断言均为异步，必须 `await`

## 高级特性

- 重复执行：`[Repeat(n)]`
- 失败重试：`[Retry(n)]`
- 并行限制：`[ParallelLimit<T>]`
- 跳过：`[Skip("reason")]`
- 依赖：`[DependsOn(nameof(OtherTest))]`
- 超时：`[Timeout(milliseconds)]`
- 可扩展自定义属性

## 测试组织

- 按功能/组件分组
- 类别：`[Category("CategoryName")]`
- 自定义显示名：`[DisplayName("Custom Test Name")]`
- 诊断：`TestContext`
- 条件/平台：如自定义 `[WindowsOnly]`

## 性能与并行

- 默认并行执行（与 xUnit 不同）
- 使用 `[NotInParallel]` 禁用指定测试并行
- 用 `[ParallelLimit<T>]` 控制并发
- 同一类内测试默认顺序执行
- 搭配 `[Repeat(n)]` 与 `[ParallelLimit<T>]` 可做简单压测

## 从 xUnit 迁移

- `[Fact]` → `[Test]`
- `[Theory]` → `[Test]` + `[Arguments]`
- `[InlineData]` → `[Arguments]`
- `[MemberData]` → `[MethodData]`
- `Assert.Equal` → `await Assert.That(actual).IsEqualTo(expected)`
- `Assert.True` → `await Assert.That(condition).IsTrue()`
- `Assert.Throws<T>` → `await Assert.That(action).Throws<T>()`
- 构造器/IDisposable → `[Before(Test)]`/`[After(Test)]`
- `IClassFixture<T>` → `[Before(Class)]`/`[After(Class)]`

**为何选择 TUnit 而非 xUnit？**

TUnit 提供更现代、快速、灵活的测试体验，具备 xUnit 所不具备的高级特性，如异步断言、更精细的生命周期钩子与更强的数据驱动能力。其流式断言可读性强，尤其适合复杂 .NET 项目。

```

```
