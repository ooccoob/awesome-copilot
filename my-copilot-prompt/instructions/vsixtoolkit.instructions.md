---
description: 'Guidelines for Visual Studio extension (VSIX) development using Community.VisualStudio.Toolkit'
applyTo: '**/*.cs, **/*.vsct, **/*.xaml, **/source.extension.vsixmanifest'
---

# 使用 Community.VisualStudio.Toolkit 进行 Visual Studio 扩展开发

## 适用范围

**这些说明仅适用于使用 `Community.VisualStudio.Toolkit` 的 Visual Studio 扩展。**

通过检查以下内容来验证项目是否使用该工具包：
- `Community.VisualStudio.Toolkit.*` NuGet 包参考
- `ToolkitPackage` 基类（不是原始 `AsyncPackage`）
- 命令的 `BaseCommand<T>` 模式

**如果项目使用原始 VSSDK（直接 `AsyncPackage`）或新的 `VisualStudio.Extensibility` 模型，请勿应用这些说明。**

## 目标

- 生成异步优先、线程安全的扩展代码
- 使用工具包抽象（`VS.*` 帮助器、`BaseCommand<T>`、`BaseOptionModel<T>`）
- 确保所有 UI 都遵循 Visual Studio 主题
- 遵循 VSSDK 和 VSTHRD 分析器规则
- 生成可测试、可维护的扩展代码
- **当存储库中存在时，遵守 `.editorconfig` 设置**

## 代码风格（.editorconfig）

**如果存储库中存在 `.editorconfig` 文件，则所有生成和修改的代码必须遵循其规则。**

这包括但不限于：
- 缩进样式（制表符与空格）和大小
- 行结尾和最终换行符要求
- 命名约定（字段、属性、方法等）
- 代码风格首选项（`var` 用法、表达式体、大括号等）
- 分析器严重性级别和抑制

在生成代码之前，请检查存储库根目录中的 `.editorconfig` 并应用其设置。如有疑问，请匹配正在编辑的文件中周围代码的样式。

## .NET Framework 和 C# 语言约束

**Visual Studio 扩展面向 .NET Framework 4.8**，但可以在 .NET Framework 运行时施加的约束下使用现代 C# 语法（最高可达 C# 14）。

### ✅ 支持的现代 C# 功能
- 主要构造函数
- 文件范围的命名空间
- 全球使用
- 模式匹配（所有形式）
- 记录（有限制）
- `init` 访问器
- 目标类型 `new`
- 可空引用类型（仅限注释）
- 原始字符串文字
- 集合表达式

### ❌ 不支持（.NET Framework 限制）
- `Span<T>`、`ReadOnlySpan<T>`、`Memory<T>`（无运行时支持）
- `IAsyncEnumerable<T>` （没有 polyfill 包）
- 默认接口实现
- `Index` 和 `Range` 类型（没有对 `^` 和 `..` 运算符的运行时支持）
- `init`-仅结构上的设置器（运行时限制）
- 一些 `System.Text.Json` 功能

### 最佳实践
编写代码时，首选 .NET Framework 4.8 中提供的 API。如果需要现代 API，请检查 polyfill NuGet 包是否存在（例如，`Microsoft.Bcl.AsyncInterfaces` 对应 `IAsyncEnumerable<T>`）。

## 提示行为示例

### ✅ 好的建议
- “创建一个命令，使用 `BaseCommand<T>` 打开当前文件所在的文件夹”
- “使用 `BaseOptionModel<T>` 添加带有布尔设置的选项页面”
- “为 C# 文件编写一个标记器提供程序，突出显示 TODO 注释”
- “处理文件时显示状态栏进度指示器”

### ❌避免
- 建议使用原始 `AsyncPackage` 而不是 `ToolkitPackage`
- 直接使用 `OleMenuCommandService` 代替 `BaseCommand<T>`
- 创建 WPF 元素而不先切换到 UI 线程
- 使用 `.Result`、`.Wait()` 或 `Task.Run` 进行 UI 工作
- 硬编码颜色而不是使用 VS 主题颜色

## 项目结构

```
src/
├── Commands/           # Command handlers (menu items, toolbar buttons)
├── Options/            # Settings/options pages
├── Services/           # Business logic and services
├── Tagging/            # ITagger implementations (syntax highlighting, outlining)
├── Adornments/         # Editor adornments (IntraTextAdornment, margins)
├── QuickInfo/          # QuickInfo/tooltip providers
├── SuggestedActions/   # Light bulb actions
├── Handlers/           # Event handlers (format document, paste, etc.)
├── Resources/          # Images, icons, license files
├── source.extension.vsixmanifest  # Extension manifest
├── VSCommandTable.vsct            # Command definitions (menus, buttons)
├── VSCommandTable.cs              # Auto-generated command IDs
└── *Package.cs                    # Main package class
```

## Community.VisualStudio.Toolkit 模式

### 全球使用

使用该工具包的扩展应该在包文件中具有以下全局用途：

```csharp
global using System;
global using Community.VisualStudio.Toolkit;
global using Microsoft.VisualStudio.Shell;
global using Task = System.Threading.Tasks.Task;
```

### 封装类别

```csharp
[PackageRegistration(UseManagedResourcesOnly = true, AllowsBackgroundLoading = true)]
[InstalledProductRegistration(Vsix.Name, Vsix.Description, Vsix.Version)]
[ProvideMenuResource("Menus.ctmenu", 1)]
[Guid(PackageGuids.YourExtensionString)]
[ProvideOptionPage(typeof(OptionsProvider.GeneralOptions), Vsix.Name, "General", 0, 0, true, SupportsProfiles = true)]
public sealed class YourPackage : ToolkitPackage
{
    protected override async Task InitializeAsync(CancellationToken cancellationToken, IProgress<ServiceProgressData> progress)
    {
        await this.RegisterCommandsAsync();
    }
}
```

### 命令

命令使用 `[Command]` 属性并继承自 `BaseCommand<T>`：

```csharp
[Command(PackageIds.YourCommandId)]
internal sealed class YourCommand : BaseCommand<YourCommand>
{
    protected override async Task ExecuteAsync(OleMenuCmdEventArgs e)
    {
        // Command implementation
    }

    // Optional: Control command state (enabled, checked, visible)
    protected override void BeforeQueryStatus(EventArgs e)
    {
        Command.Checked = someCondition;
        Command.Enabled = anotherCondition;
    }
}
```

### 选项页

```csharp
internal partial class OptionsProvider
{
    [ComVisible(true)]
    public class GeneralOptions : BaseOptionPage<General> { }
}

public class General : BaseOptionModel<General>
{
    [Category("Category Name")]
    [DisplayName("Setting Name")]
    [Description("Description of the setting.")]
    [DefaultValue(true)]
    public bool MySetting { get; set; } = true;
}
```

## MEF组件

### 标记器提供商

使用 `[Export]` 和适当的 `[ContentType]` 属性：

```csharp
[Export(typeof(IViewTaggerProvider))]
[ContentType("CSharp")]
[ContentType("Basic")]
[TagType(typeof(IntraTextAdornmentTag))]
[TextViewRole(PredefinedTextViewRoles.Document)]
internal sealed class YourTaggerProvider : IViewTaggerProvider
{
    [Import]
    internal IOutliningManagerService OutliningManagerService { get; set; }

    public ITagger<T> CreateTagger<T>(ITextView textView, ITextBuffer buffer) where T : ITag
    {
        if (textView == null || !(textView is IWpfTextView wpfTextView))
            return null;

        if (textView.TextBuffer != buffer)
            return null;

        return wpfTextView.Properties.GetOrCreateSingletonProperty(
            () => new YourTagger(wpfTextView)) as ITagger<T>;
    }
}
```

### 快速信息来源

```csharp
[Export(typeof(IAsyncQuickInfoSourceProvider))]
[Name("YourQuickInfo")]
[ContentType("code")]
[Order(Before = "Default Quick Info Presenter")]
internal sealed class YourQuickInfoSourceProvider : IAsyncQuickInfoSourceProvider
{
    public IAsyncQuickInfoSource TryCreateQuickInfoSource(ITextBuffer textBuffer)
    {
        return textBuffer.Properties.GetOrCreateSingletonProperty(
            () => new YourQuickInfoSource(textBuffer));
    }
}
```

### 建议采取的措施（灯泡）

```csharp
[Export(typeof(ISuggestedActionsSourceProvider))]
[Name("Your Suggested Actions")]
[ContentType("text")]
internal sealed class YourSuggestedActionsSourceProvider : ISuggestedActionsSourceProvider
{
    public ISuggestedActionsSource CreateSuggestedActionsSource(ITextView textView, ITextBuffer textBuffer)
    {
        return new YourSuggestedActionsSource(textView, textBuffer);
    }
}
```

## 线程指南

### 始终切换到 UI 线程进行 WPF 操作

```csharp
await ThreadHelper.JoinableTaskFactory.SwitchToMainThreadAsync(cancellationToken);
// Now safe to create/modify WPF elements
```

### 后台工作

```csharp
ThreadHelper.JoinableTaskFactory.RunAsync(async () =>
{
    await ThreadHelper.JoinableTaskFactory.SwitchToMainThreadAsync();
    await VS.Commands.ExecuteAsync("View.TaskList");
});
```

## VSSDK 和线程分析器规则

扩展应该强制执行这些分析器规则。添加到`.editorconfig`：

```ini
dotnet_diagnostic.VSSDK*.severity = error
dotnet_diagnostic.VSTHRD*.severity = error
```

### 表现规则
|身份证 |规则|修复 |
|----|------|-----|
| **VSSDK001** |派生自 `AsyncPackage` |使用 `ToolkitPackage` （源自 AsyncPackage） |
| **VSSDK002** | __代码0__ |添加到 `[PackageRegistration]` |

### 线程规则 (VSTHRD)
|身份证 |规则|修复 |
|----|------|-----|
| **VSTHRD001** |避免 `.Wait()` |使用 `await` |
| **VSTHRD002** |避免 `JoinableTaskFactory.Run` |使用 `RunAsync` 或 `await` |
| **VSTHRD010** | COM 调用需要 UI 线程 | __代码0__ |
| **VSTHRD100** |没有 `async void` |使用 `async Task` |
| **VSTHRD110** |观察异步结果 | `await task;` 或使用编译指示抑制 |

## Visual Studio 主题

**所有 UI 必须遵循 VS 主题（浅色、深色、蓝色、高对比度）**

### 具有环境颜色的 WPF 主题

```xml
<!-- MyControl.xaml -->
<UserControl x:Class="MyExt.MyControl"
             xmlns:vsui="clr-namespace:Microsoft.VisualStudio.PlatformUI;assembly=Microsoft.VisualStudio.Shell.15.0">
    <Grid Background="{DynamicResource {x:Static vsui:EnvironmentColors.ToolWindowBackgroundBrushKey}}">
        <TextBlock Foreground="{DynamicResource {x:Static vsui:EnvironmentColors.ToolWindowTextBrushKey}}"
                   Text="Hello, themed world!" />
    </Grid>
</UserControl>
```

### 工具包自动主题（推荐）

该工具包为 WPF UserControls 提供自动主题设置：

```xml
<UserControl x:Class="MyExt.MyUserControl"
             xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:toolkit="clr-namespace:Community.VisualStudio.Toolkit;assembly=Community.VisualStudio.Toolkit"
             toolkit:Themes.UseVsTheme="True">
    <!-- Controls automatically get VS styling -->
</UserControl>
```

对于对话框窗口，使用 `DialogWindow`：

```xml
<platform:DialogWindow
    x:Class="MyExt.MyDialog"
    xmlns:platform="clr-namespace:Microsoft.VisualStudio.PlatformUI;assembly=Microsoft.VisualStudio.Shell.15.0"
    xmlns:toolkit="clr-namespace:Community.VisualStudio.Toolkit;assembly=Community.VisualStudio.Toolkit"
    toolkit:Themes.UseVsTheme="True">
</platform:DialogWindow>
```

### 通用主题颜色标记

|类别 |代币|用途 |
|----------|-------|-------|
| **背景** | __代码0__ |窗口/面板背景|
| **前景** | __代码0__ |文字|
| **命令栏** | __代码0__ |菜单项|
| **链接** | __代码0__ |超链接 |

### 主题感知图标

使用 VS 图像目录中的 `KnownMonikers` 来获取主题感知图标：

```csharp
public ImageMoniker IconMoniker => KnownMonikers.Settings;
```

在 VSCT 中：
```xml
<Icon guid="ImageCatalogGuid" id="Settings"/>
<CommandFlag>IconIsMoniker</CommandFlag>
```

## VS SDK常用API

### VS 帮助程序方法 (Community.VisualStudio.Toolkit)

```csharp
// Status bar
await VS.StatusBar.ShowMessageAsync("Message");
await VS.StatusBar.ShowProgressAsync("Working...", currentStep, totalSteps);

// Solution/Projects
Solution solution = await VS.Solutions.GetCurrentSolutionAsync();
IEnumerable<SolutionItem> items = await VS.Solutions.GetActiveItemsAsync();
bool isOpen = await VS.Solutions.IsOpenAsync();

// Documents
DocumentView docView = await VS.Documents.GetActiveDocumentViewAsync();
string text = docView?.TextBuffer?.CurrentSnapshot.GetText();
await VS.Documents.OpenAsync(fileName);
await VS.Documents.OpenInPreviewTabAsync(fileName);

// Commands
await VS.Commands.ExecuteAsync("View.TaskList");

// Settings
await VS.Settings.OpenAsync<OptionsProvider.GeneralOptions>();

// Messages
await VS.MessageBox.ShowAsync("Title", "Message");
await VS.MessageBox.ShowErrorAsync("Extension Name", ex.ToString());

// Events
VS.Events.SolutionEvents.OnAfterOpenProject += OnAfterOpenProject;
VS.Events.DocumentEvents.Saved += OnDocumentSaved;
```

### 使用设置

```csharp
// Read settings synchronously
var value = General.Instance.MyOption;

// Read settings asynchronously
var general = await General.GetLiveInstanceAsync();
var value = general.MyOption;

// Write settings
General.Instance.MyOption = newValue;
General.Instance.Save();

// Or async
general.MyOption = newValue;
await general.SaveAsync();

// Listen for settings changes
General.Saved += OnSettingsSaved;
```

### 文本缓冲区操作

```csharp
// Get snapshot
ITextSnapshot snapshot = textBuffer.CurrentSnapshot;

// Get line
ITextSnapshotLine line = snapshot.GetLineFromLineNumber(lineNumber);
string lineText = line.GetText();

// Create tracking span
ITrackingSpan trackingSpan = snapshot.CreateTrackingSpan(span, SpanTrackingMode.EdgeInclusive);

// Edit buffer
using (ITextEdit edit = textBuffer.CreateEdit())
{
    edit.Replace(span, newText);
    edit.Apply();
}

// Insert at caret position
DocumentView docView = await VS.Documents.GetActiveDocumentViewAsync();
if (docView?.TextView != null)
{
    SnapshotPoint position = docView.TextView.Caret.Position.BufferPosition;
    docView.TextBuffer?.Insert(position, "text to insert");
}
```

## VSCT 命令表

### 菜单/命令结构

```xml
<Commands package="YourPackage">
  <Menus>
    <Menu guid="YourPackage" id="SubMenu" type="Menu">
      <Parent guid="YourPackage" id="MenuGroup"/>
      <Strings>
        <ButtonText>Menu Name</ButtonText>
        <CommandName>Menu Name</CommandName>
        <CanonicalName>.YourExtension.MenuName</CanonicalName>
      </Strings>
    </Menu>
  </Menus>

  <Groups>
    <Group guid="YourPackage" id="MenuGroup" priority="0x0600">
      <Parent guid="guidSHLMainMenu" id="IDM_VS_CTXT_CODEWIN"/>
    </Group>
  </Groups>

  <Buttons>
    <Button guid="YourPackage" id="CommandId" type="Button">
      <Parent guid="YourPackage" id="MenuGroup"/>
      <Icon guid="ImageCatalogGuid" id="Settings"/>
      <CommandFlag>IconIsMoniker</CommandFlag>
      <CommandFlag>DynamicVisibility</CommandFlag>
      <Strings>
        <ButtonText>Command Name</ButtonText>
        <CanonicalName>.YourExtension.CommandName</CanonicalName>
      </Strings>
    </Button>
  </Buttons>
</Commands>

<Symbols>
  <GuidSymbol name="YourPackage" value="{guid-here}">
    <IDSymbol name="MenuGroup" value="0x0001"/>
    <IDSymbol name="CommandId" value="0x0100"/>
  </GuidSymbol>
</Symbols>
```

## 最佳实践

### 1. 性能

- 处理大文档之前检查文件/缓冲区大小
- 使用 `NormalizedSnapshotSpanCollection` 进行高效的跨度操作
- 尽可能缓存解析结果
- 在库代码中使用 `ConfigureAwait(false)`

```csharp
// Skip large files
if (buffer.CurrentSnapshot.Length > 150000)
    return null;
```

### 2. 错误处理

- 将外部操作包装在 try-catch 中
- 适当记录错误
- 永远不要让异常让VS崩溃

```csharp
try
{
    // Operation
}
catch (Exception ex)
{
    await ex.LogAsync();
}
```

### 3. 一次性资源

- 在标记器和其他长期对象上实现 `IDisposable`
- 取消订阅 Dispose 中的事件

```csharp
public void Dispose()
{
    if (!_isDisposed)
    {
        _buffer.Changed -= OnBufferChanged;
        _isDisposed = true;
    }
}
```

### 4. 内容类型

`[ContentType]` 属性的常见内容类型：
- `"text"` - 所有文本文件
- `"code"` - 所有代码文件
- `"CSharp"` - C# 文件
- `"Basic"` - VB.NET 文件
- `"CSS"`、`"LESS"`、`"SCSS"` - 样式文件
- `"TypeScript"`、`"JavaScript"` - 脚本文件
- `"HTML"`、`"HTMLX"` - HTML 文件
- `"XML"` - XML 文件
- `"JSON"` - JSON 文件

### 5. 图像和图标

使用 VS 图像目录中的 `KnownMonikers`：

```csharp
public ImageMoniker IconMoniker => KnownMonikers.Settings;
```

在 VSCT 中：
```xml
<Icon guid="ImageCatalogGuid" id="Settings"/>
<CommandFlag>IconIsMoniker</CommandFlag>
```

## 测试

- 使用 `[VsTestMethod]` 进行需要 VS 上下文的测试
- 尽可能模拟 VS 服务
- 与 VS 集成分开测试业务逻辑

## 常见陷阱

|陷阱|解决方案 |
|---------|----------|
|阻塞 UI 线程 |始终使用 `async`/`await` |
|在后台线程上创建 WPF |首先调用 `SwitchToMainThreadAsync()` |
|忽略取消标记 |通过异步链传递它们 |
| VSCommandTable.cs 不匹配 | VSCT 更改后重新生成 |
|硬编码 GUID |使用 `PackageGuids` 和 `PackageIds` 常量 |
|吞咽异常|使用 `await ex.LogAsync()` 登录 |
|缺少动态可见性 |需要 `BeforeQueryStatus` 才能工作 |
|使用 `.Result`、`.Wait()` |造成死锁；总是 `await` |
|硬编码颜色 |使用 VS 主题颜色 (`EnvironmentColors`) |
| `async void` 方法 |使用 `async Task` 代替 |

## 验证

构建并验证扩展：

```bash
msbuild /t:rebuild
```

确保在 `.editorconfig` 中启用分析器：

```ini
dotnet_diagnostic.VSSDK*.severity = error
dotnet_diagnostic.VSTHRD*.severity = error
```

发布前在VS实验实例中进行测试。

## NuGet 包

|套餐 |目的|
|---------|---------|
| __代码0__ |简化 VS 扩展开发 |
| __代码0__ |核心VS SDK |
| __代码0__ | VSIX 构建工具 |
| __代码0__ |线程分析仪|
| __代码0__ | VSSDK 分析器 |

## 资源

- [社区.VisualStudio.工具包](https://github.com/VsixCommunity/Community.VisualStudio.Toolkit)
- [VS 扩展性文档](https://learn.microsoft.com/en-us/visualstudio/extensibility/)
- [VSIX 社区示例](https://github.com/VsixCommunity/Samples)

## 自述文件和市场演示

好的自述文件适用于 GitHub 和 VS Marketplace。 Marketplace 使用 README.md 作为扩展的描述页面。

### 自述文件结构

```markdown
[marketplace]: https://marketplace.visualstudio.com/items?itemName=Publisher.ExtensionName
[repo]: https://github.com/user/repo

# Extension Name

[![Build](https://github.com/user/repo/actions/workflows/build.yaml/badge.svg)](...)
[![Visual Studio Marketplace Version](https://img.shields.io/visual-studio-marketplace/v/Publisher.ExtensionName)][marketplace]
[![Visual Studio Marketplace Downloads](https://img.shields.io/visual-studio-marketplace/d/Publisher.ExtensionName)][marketplace]

Download this extension from the [Visual Studio Marketplace][marketplace]
or get the [CI build](http://vsixgallery.com/extension/ExtensionId/).

--------------------------------------

**Hook line that sells the extension in one sentence.**

![Screenshot](art/screenshot.png)

## Features

### Feature 1
Description with screenshot...

## How to Use
...

## License
[Apache 2.0](LICENSE)
```

### 自述文件最佳实践

|元素|指南|
|---------|-----------|
| **标题** |使用与 vsixmanifest | 中的 `DisplayName` 相同的名称
| **勾线** |徽章后立即出现大胆的一句话价值主张 |
| **截图** |放置在 `/art` 文件夹中，使用相对路径 (`art/image.png`) |
| **图像尺寸** |为了清晰起见，保持在 1MB 以下、800-1200 像素宽 |
| **徽章** |版本、下载、评级、构建状态 |
| **功能部分** |使用 H3 (`###`) 并附有每个主要功能的屏幕截图 |
| **键盘快捷键** |格式为 **Ctrl+M、Ctrl+C**（粗体）|
| **表格** |非常适合比较选项或列出功能 |
| **链接** |使用顶部的参考样式链接以获得更清晰的降价 |

### VSIX 清单（source.extension.vsixmanifest）

```xml
<Metadata>
  <Identity Id="ExtensionName.guid-here" Version="1.0.0" Language="en-US" Publisher="Your Name" />
  <DisplayName>Extension Name</DisplayName>
  <Description xml:space="preserve">Short, compelling description under 200 chars. This appears in search results and the extension tile.</Description>
  <MoreInfo>https://github.com/user/repo</MoreInfo>
  <License>Resources\LICENSE.txt</License>
  <Icon>Resources\Icon.png</Icon>
  <PreviewImage>Resources\Preview.png</PreviewImage>
  <Tags>keyword1, keyword2, keyword3</Tags>
</Metadata>
```

### 清单最佳实践

|元素|指南|
|---------|-----------|
| **显示名称** | 3-5 个单词，没有“for Visual Studio”（隐含）|
| **描述** |少于 200 个字符，重点关注价值而不是功能。出现在搜索图块 |
| **标签** | 5-10 个相关关键词，以逗号分隔，有助于被发现 |
| **图标** | 128x128 或 256x256 PNG，小尺寸下可见的简单设计 |
| **预览图片** | 200x200 PNG，可以与图标或功能截图相同|
| **更多信息** |链接到 GitHub 存储库以获取文档和问题 |

### 写作技巧

1. **以优势而非功能为主导** - “停止与 XML 注释搏斗”胜过“XML 注释格式化程序”
2. **展示，而非讲述** - 屏幕截图比描述更有说服力
3. **使用一致的术语** - 匹配自述文件、清单和 UI 之间的术语
4. **保持描述易于浏览** - 短段落、要点、表格
5. **包括键盘快捷键** - 用户喜欢生产力提示
6. **添加“为什么”部分** - 在解决方案之前解释问题
