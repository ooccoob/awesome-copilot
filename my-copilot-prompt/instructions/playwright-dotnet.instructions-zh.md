---
描述：“Playwright .NET 测试生成说明”
适用于：'**'
---

# Playwright .NET 测试生成说明

## 测试写作指南

### 代码质量标准

- **定位器**：优先考虑面向用户、基于角色的定位器（`GetByRole`、`GetByLabel`、`GetByText` 等），以实现弹性和可访问性。使用 `await Test.StepAsync()` 对交互进行分组并提高测试可读性和报告。
- **断言**：使用自动重试网络优先断言。这些断言使用来自剧作家断言的 `Expect()` （例如 `await Expect(locator).ToHaveTextAsync()`）。除非专门测试可见性更改，否则避免检查可见性。
- **超时**：依靠 Playwright 的内置自动等待机制。避免硬编码等待或增加默认超时。
- **清晰度**：使用清楚说明意图的描述性测试和步骤标题。仅添加注释来解释复杂的逻辑或不明显的交互。

### 测试结构

- **使用**：对于 MSTest，以 `using Microsoft.Playwright;` 和 `using Microsoft.Playwright.Xunit;` 或 `using Microsoft.Playwright.NUnit;` 或 `using Microsoft.Playwright.MSTest;` 开头。
- **组织**：创建从 `PageTest` 继承的测试类（在 NUnit、xUnit 和 MSTest 包中可用）或将 `IClassFixture<PlaywrightFixture>` 用于带有自定义装置的 xUnit。将某个功能的相关测试分组到同一测试类中。
- **设置**：使用 `[SetUp]` (NUnit)、`[TestInitialize]` (MSTest) 或构造函数初始化 (xUnit) 进行所有测试通用的设置操作（例如，导航到页面）。
- **标题**：使用适当的测试属性（对于 NUnit 为 `[Test]`、对于 xUnit 为 `[Fact]`、对于 MSTest 为 `[TestMethod]`）以及遵循 C# 命名约定的描述性方法名称（例如 `SearchForMovieByTitle`）。

### 文件组织

- **位置**：将所有测试文件存储在 `Tests/` 目录中或按功能组织。
- **命名**：使用约定 `<FeatureOrPage>Tests.cs`（例如，`LoginTests.cs`、`SearchTests.cs`）。
- **范围**：针对每个主要应用程序功能或页面一个测试类。

### 断言最佳实践

- **UI 结构**：使用 `ToMatchAriaSnapshotAsync` 验证组件的可访问性树结构。这提供了全面且可访问的快照。
- **元素计数**：使用 `ToHaveCountAsync` 断言定位器找到的元素数量。
- **文本内容**：使用 `ToHaveTextAsync` 进行精确文本匹配，使用 `ToContainTextAsync` 进行部分匹配。
- **导航**：在操作后使用 `ToHaveURLAsync` 验证页面 URL。

## 测试结构示例

```csharp
using Microsoft.Playwright;
using Microsoft.Playwright.Xunit;
using static Microsoft.Playwright.Assertions;

namespace PlaywrightTests;

public class MovieSearchTests : PageTest
{
    public override async Task InitializeAsync()
    {
        await base.InitializeAsync();
        // Navigate to the application before each test
        await Page.GotoAsync("https://debs-obrien.github.io/playwright-movies-app");
    }

    [Fact]
    public async Task SearchForMovieByTitle()
    {
        await Test.StepAsync("Activate and perform search", async () =>
        {
            await Page.GetByRole(AriaRole.Search).ClickAsync();
            var searchInput = Page.GetByRole(AriaRole.Textbox, new() { Name = "Search Input" });
            await searchInput.FillAsync("Garfield");
            await searchInput.PressAsync("Enter");
        });

        await Test.StepAsync("Verify search results", async () =>
        {
            // Verify the accessibility tree of the search results
            await Expect(Page.GetByRole(AriaRole.Main)).ToMatchAriaSnapshotAsync(@"
                - main:
                  - heading ""Garfield"" [level=1]
                  - heading ""search results"" [level=2]
                  - list ""movies"":
                    - listitem ""movie"":
                      - link ""poster of The Garfield Movie The Garfield Movie rating"":
                        - /url: /playwright-movies-app/movie?id=tt5779228&page=1
                        - img ""poster of The Garfield Movie""
                        - heading ""The Garfield Movie"" [level=2]
            ");
        });
    }
}
```

## 测试执行策略

1. **初始运行**：使用 `dotnet test` 或使用 IDE 中的测试运行器执行测试
2. **调试失败**：分析测试失败并确定根本原因
3. **迭代**：根据需要细化定位器、断言或测试逻辑
4. **验证**：确保测试一致通过并覆盖预期功能
5. **报告**：提供有关测试结果和发现的任何问题的反馈

## 质量检查表

在完成测试之前，请确保：

- [ ] 所有定位器都是可访问的且特定的，并且避免严格模式违规
- [ ] 测试按逻辑分组并遵循清晰的结构
- [ ] 断言有意义并反映用户期望
- [ ] 测试遵循一致的命名约定
- [ ] 代码格式正确并有注释
