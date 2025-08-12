---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems", "search"]
description: "获取 MSTest 单元测试最佳实践（含数据驱动测试）"
---

# MSTest 最佳实践

你的目标是帮助我使用 MSTest 编写高质量单元测试，涵盖标准测试与数据驱动测试。

## 项目设置

- 使用独立测试项目，命名约定为 `[ProjectName].Tests`
- 引用 MSTest 相关包
- 按被测类进行测试类命名（如 `Calculator` → `CalculatorTests`）
- 使用 .NET SDK 测试命令：`dotnet test`

## 测试结构

- 测试类使用 `[TestClass]`
- 测试方法使用 `[TestMethod]`
- 遵循 AAA（Arrange-Act-Assert）模式
- 测试命名：`方法名_场景_期望行为`
- 每个测试前后置：`[TestInitialize]` / `[TestCleanup]`
- 类级前后置：`[ClassInitialize]` / `[ClassCleanup]`
- 程序集级前后置：`[AssemblyInitialize]` / `[AssemblyCleanup]`

## 标准测试

- 聚焦单一行为
- 避免在一个测试方法中覆盖多个行为
- 使用清晰的断言表达意图
- 只保留验证该用例所需的断言
- 测试应独立且幂等，可任意顺序执行
- 避免测试间相互依赖

## 数据驱动测试

- 使用 `[TestMethod]` 搭配数据源特性
- 内联数据：`[DataRow]`
- 生成型数据：`[DynamicData]`
- 元数据：`[TestProperty]`
- 使用有意义的参数名

## 断言

- 值相等：`Assert.AreEqual`
- 引用相等：`Assert.AreSame`
- 布尔：`Assert.IsTrue` / `Assert.IsFalse`
- 集合：`CollectionAssert`
- 字符串：`StringAssert`
- 异常：`Assert.ThrowsException<T>`（或合适的 MSTest API）
- 为断言添加失败消息以便定位问题

## Mock 与隔离

- 可搭配 Moq 或 NSubstitute
- 对依赖进行 Mock 以隔离被测单元
- 借助接口以便于 Mock
- 复杂场景可考虑 DI 容器

## 测试组织

- 按功能/组件分组
- 类别：`[TestCategory("Category")]`
- 优先级：`[Priority(1)]`
- 责任人：`[Owner("DeveloperName")]`

```

```
