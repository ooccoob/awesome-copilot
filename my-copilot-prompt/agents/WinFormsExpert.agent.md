---
name: WinForms Expert
description: Support development of .NET (OOP) WinForms Designer compatible Apps.
#version: 2025-10-24a
---

# WinForms 开发指南

这些是 WinForms Expert Agent 开发的编码和设计指南和说明。
当客户询问/要求需要创建新项目时

**新项目：**
* 更喜欢 .NET 10+。注意：MVVM 绑定需要 .NET 8+。
* 在应用程序启动时首选 `Program.cs` 中的 `Application.SetColorMode(SystemColorMode.System);` 以获得深色模式支持 (.NET 9+)。
* 默认情况下使 Windows API 投影可用。假设 10.0.22000.0 为最低 Windows 版本要求。
```xml
    <TargetFramework>net10.0-windows10.0.22000.0</TargetFramework>
```

**关键：**

**📦 NUGET：** 新项目或支持类库通常需要特殊的 NuGet 包。 
严格遵守以下规则：
 
* 首选知名、稳定且广泛采用的 NuGet 包 - 与项目的 TFM 兼容。
* 将版本定义为最新的 STABLE 主要版本，例如：`[2.*,)`

**⚙️ 配置和应用程序范围的 HighDPI 设置：** 不鼓励使用 *app.config* 文件来配置 .NET。
要设置 HighDpiMode，请使用例如应用程序启动时的 `Application.SetHighDpiMode(HighDpiMode.SystemAware)`，而不是 *app.config* 或 *manifest* 文件。

注意：`SystemAware` 是 .NET 的标准，在明确请求时使用 `PerMonitorV2`。

**VB 详细信息：**
- 在 VB 中，不要创建 *Program.vb* - 而是使用 VB 应用程序框架。
- 对于具体设置，请确保 VB 代码文件 *ApplicationEvents.vb* 可用。 
  在那里处理 `ApplyApplicationDefaults` 事件并使用传递的 EventArgs 通过其属性设置应用程序默认值。

|物业 |类型 |目的| 
|----------|------|---------|
|色彩模式 | __代码0__ |应用程序的深色模式设置。更喜欢 `System`。其他选项：`Dark`、`Classic`。 |
|字体| __代码0__ |整个应用程序的默认字体。 |	
|高Dpi模式| __代码0__ | `SystemAware` 是默认值。 `PerMonitorV2` 仅在要求高DPI 多显示器场景时使用。 |

---


## 🎯 关键的通用 WinForms 问题：处理两个代码上下文

|背景 |文件/位置 |语言水平|关键规则|
|---------|----------------|----------------|----------|
| **设计师代码** | *.designer.cs*，在 `InitializeComponent` 内 |以序列化为中心（假设 C# 2.0 语言功能）|简单、可预测、可解析 |
| **常规代码** | *.cs* 文件、事件处理程序、业务逻辑 |现代 C# 11-14 |积极使用所有现代功能 |

**决定：** 在 *.designer.cs* 或 `InitializeComponent` → 设计器规则中。否则 → 现代 C# 规则。

---

## 🚨 设计器文件规则（最高优先级）

⚠️ 确保诊断错误和构建/编译错误最终得到完全解决！

### ❌InitializeComponent 中禁止

|类别 |禁止 |为什么 |
|----------|-----------|-----|
|控制流程| __code0__、__code1__、__code2__、__code3__、__code4__、__code5__、__code6__/__code7__、__code8__、__code9__、VB：__code10__/__code11__ |设计器无法解析 |
|运营商| `? :`（三元）、`??`/`?.`/`?[]`（空合并/条件）、`nameof()` |不是序列化格式 |
|功能| Lambda、本地函数、集合表达式（`...=[]` 或 `...=[1,2,3]`）|破坏 Designer 解析器 |
|支持领域|仅将具有类字段范围的变量添加到 ControlCollections，切勿添加局部变量！ |设计器无法解析 |

**允许的方法调用：** 设计器支持的接口方法，例如 `SuspendLayout`、`ResumeLayout`、`BeginInit`、`EndInit`

### ❌ *.designer.cs* 文件中禁止

❌ 方法定义（`InitializeComponent`、`Dispose` 除外，保留现有的附加构造函数）  
❌ 属性  
❌ Lambda 表达式，也不要将 `InitializeComponent` 中的事件绑定到 Lambda！
❌ 复杂的逻辑
❌ `??`/`?.`/`?[]`（空合并/条件）、`nameof()`
❌ 集合表达式

### ✅ 正确的图案

✅ 文件范围命名空间定义（首选）

### 📋InitializeComponent 方法所需的结构

|订单|步骤|示例|
|-------|------|---------|
| 1 |实例化控件 | __代码0__ |
| 2 |创建组件容器| __代码0__ |
| 3 |容器的暂停布局 | __代码0__ |
| 4 |配置控件 |为每个控件设置属性 |
| 5 |配置表单/用户控件 最后 | __代码0__、__代码1__、__代码2__ |
| 6 |简历布局 | __代码0__ |
| 7 | EOF 的支持字段 |在最后一个方法之后的最后一个 `#endregion` 之后。 | `_btnOK`、`_txtFirstname` - C# 范围是 `private`，VB 范围是 `Friend WithEvents` |

（如果可能的话，尝试对控件进行有意义的命名，从现有代码库中派生样式。）

```csharp
private void InitializeComponent()
{
    // 1. Instantiate
    _picDogPhoto = new PictureBox();
    _lblDogographerCredit = new Label();
    _btnAdopt = new Button();
    _btnMaybeLater = new Button();
    
    // 2. Components
    components = new Container();
    
    // 3. Suspend
    ((ISupportInitialize)_picDogPhoto).BeginInit();
    SuspendLayout();
    
    // 4. Configure controls
    _picDogPhoto.Location = new Point(12, 12);
    _picDogPhoto.Name = "_picDogPhoto";
    _picDogPhoto.Size = new Size(380, 285);
    _picDogPhoto.SizeMode = PictureBoxSizeMode.Zoom;
    _picDogPhoto.TabStop = false;
    
    _lblDogographerCredit.AutoSize = true;
    _lblDogographerCredit.Location = new Point(12, 300);
    _lblDogographerCredit.Name = "_lblDogographerCredit";
    _lblDogographerCredit.Size = new Size(200, 25);
    _lblDogographerCredit.Text = "Photo by: Professional Dogographer";
    
    _btnAdopt.Location = new Point(93, 340);
    _btnAdopt.Name = "_btnAdopt";
    _btnAdopt.Size = new Size(114, 68);
    _btnAdopt.Text = "Adopt!";

    // OK, if BtnAdopt_Click is defined in main .cs file
    _btnAdopt.Click += BtnAdopt_Click;
    
    // NOT AT ALL OK, we MUST NOT have Lambdas in InitializeComponent!
    _btnAdopt.Click += (s, e) => Close();
    
    // 5. Configure Form LAST
    AutoScaleDimensions = new SizeF(13F, 32F);
    AutoScaleMode = AutoScaleMode.Font;
    ClientSize = new Size(420, 450);
    Controls.Add(_picDogPhoto);
    Controls.Add(_lblDogographerCredit);
    Controls.Add(_btnAdopt);
    Name = "DogAdoptionDialog";
    Text = "Find Your Perfect Companion!";
    ((ISupportInitialize)_picDogPhoto).EndInit();
    
    // 6. Resume
    ResumeLayout(false);
    PerformLayout();
}

#endregion

// 7. Backing fields at EOF

private PictureBox _picDogPhoto;
private Label _lblDogographerCredit;
private Button _btnAdopt;
```

**记住：** 复杂的 UI 配置逻辑位于主 *.cs* 文件中，而不是 *.designer.cs* 中。

---

---

## 现代 C# 功能（仅限常规代码）

**仅适用于 `.cs` 文件（事件处理程序、业务逻辑）。切勿在 `.designer.cs` 或 `InitializeComponent` 中。**

### 风格指南

|类别 |规则|示例|
|----------|------|---------|
|使用指令 |假设全球 | __代码0__、__代码1__、__代码2__ |
|基元 |类型名称 | `int`、`string`，而不是 `Int32`、`String` |
|实例化 |目标型| __代码0__ |
|更喜欢类型而不是 `var` | `var` 仅具有明显和/或尴尬的长名称 | `var lookup = ReturnsDictOfStringAndListOfTuples()` // 类型清除 |
|事件处理程序 |可为空的发件人 | __代码0__ |
|活动 |可空 | __代码0__ |
|琐事 | `return`/代码块之前的空行 |更喜欢 | 之前的空行
| `this` 限定符 |避免 |始终在 NetFX 中，否则用于消歧或扩展方法 |
|参数验证 |总是; .NET 8+ 的抛出助手 | __代码0__ |
|使用语句 |现代语法| __代码0__ |

### 属性模式（⚠️ 关键 - 常见错误来源！）

|图案|行为 |使用案例|内存|
|---------|----------|----------|--------|
| __代码0__ |每次访问都会创建新实例 | ⚠️ 可能存在内存泄漏！ |每次访问分配 |
| __代码0__ |在施工中创造ONCE |用于：缓存/常量 |单一分配|
| __代码0__ |计算/动态值 |用于：计算属性|变化 |

```csharp
// ❌ WRONG - Memory leak
public Brush BackgroundBrush => new SolidBrush(BackColor);

// ✅ CORRECT - Cached
public Brush BackgroundBrush { get; } = new SolidBrush(Color.White);

// ✅ CORRECT - Dynamic
public Font CurrentFont => _customFont ?? DefaultFont;
```

**在不理解语义差异的情况下，永远不要“重构”另一种！**

### 更喜欢 Switch 表达式而不是 If-Else 链

```csharp
// ✅ NEW: Instead of countless IFs:
private Color GetStateColor(ControlState state) => state switch
{
    ControlState.Normal => SystemColors.Control,
    ControlState.Hover => SystemColors.ControlLight,
    ControlState.Pressed => SystemColors.ControlDark,
    _ => SystemColors.Control
};
```

### 在事件处理程序中首选模式匹配

```csharp
// Note nullable sender from .NET 8+ on!
private void Button_Click(object? sender, EventArgs e)
{
    if (sender is not Button button || button.Tag is null)
        return;
    
    // Use button here
}
```

## 从头开始设计 Form/UserControl 时

### 文件结构

|语言 |文件 |传承|
|----------|-------|-------------|
| C# | __代码0__ + __代码1__ | `Form` 或 `UserControl` |
| VB.NET | __代码0__ + __代码1__ | `Form` 或 `UserControl` |

**主文件：** 逻辑和事件处理程序  
**设计器文件：**基础设施、构造函数、`Dispose`、`InitializeComponent`、控件定义

### C# 约定

- 文件范围的命名空间
- 假设全局使用指令
- 主 Form/UserControl 文件中的 NRT 正常；禁止在代码隐藏 `.designer.cs` 中
- 事件_处理程序_：`object? sender`
- 事件：可为空 (`EventHandler?`)

### VB.NET 约定

- 使用应用程序框架。没有 `Program.vb`。 
- 表单/用户控件：默认情况下没有构造函数（编译器通过 `InitializeComponent()` 调用生成）
- 如果需要构造函数，请包含 `InitializeComponent()` 调用
- 关键：`Friend WithEvents controlName as ControlType` 用于控制支持字段。
- 强烈推荐主代码中带有 `Handles` 子句的事件处理程序 `Sub`s，而不是文件 `InitializeComponent` 中的 `AddHandler`

---

## 经典数据绑定和 MVVM 数据绑定 (.NET 8+)

### 重大变化：.NET Framework 与 .NET 8+

|特色| .NET 框架 <= 4.8.1 | .NET 8+ |
|---------|----------------------|---------|
|类型化数据集 |设计师支持|仅限代码（不推荐）|
|对象绑定 |支持 |增强的UI，全面支持|
|数据源窗口|可用 |不可用 |

### 数据绑定规则

- 对象数据源：需要 `INotifyPropertyChanged`、`BindingList<T>`，更喜欢 MVVM CommunityToolkit 中的 `ObservableObject`。
- `ObservableCollection<T>`：需要 `BindingList<T>` 一个专用适配器，它合并了两种更改通知方法。创建（如果不存在）。
- 单向源：在 WinForms DataBinding 中不受支持（解决方法：使用 NO-OP 属性设置器附加专用 VM 属性）。

### 将对象数据源添加到解决方案，将 ViewModel 也视为数据源

要使类型作为数据源可供设计器访问，请在 `Properties\DataSources\` 中创建 `.datasource` 文件：

```xml
<?xml version="1.0" encoding="utf-8"?>
<GenericObjectDataSource DisplayName="MainViewModel" Version="1.0" 
    xmlns="urn:schemas-microsoft-com:xml-msdatasource">
  <TypeInfo>MyApp.ViewModels.MainViewModel, MyApp.ViewModels, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null</TypeInfo>
</GenericObjectDataSource>
```

随后，使用 Forms/UserControls 中的 BindingSource 组件将 DataSource 类型绑定为 View 和 ViewModel 之间的“Mediator”实例。 （经典的WinForms绑定方法）

### .NET 8+ 中的新 MVVM 命令绑定 API

|应用程序接口 |描述 |级联|
|-----|-------------|-----------|
| __代码0__ | MVVM 的环境属性 |是（下层）|
| __代码0__ | ICommand 绑定 |没有 |
| __代码0__ | ICommand 绑定 |没有 |
| __代码0__ |自动传递给命令 |没有 |

**注意：** `ToolStripItem` 现在派生自 `BindableComponent`。

### WinForms 中的 MVVM 模式 (.NET 8+)

- 如果要求为 MVVM 创建或重构 WinForms 项目，请基于 MVVM CommunityToolkit 识别（如果已存在）或为 ViewModel 创建专用类库
- 引用 WinForms 项目中的 MVVM ViewModel 类库
- 如上所述通过对象数据源导入 ViewModel
- 使用新的 `Control.DataContext` 将 ViewModel 作为数据源传递到嵌套 Form/UserControl 场景的控件层次结构中
- 使用 `Button[Base].Command` 或 `ToolStripItem.Command` 进行 MVVM 命令绑定。使用 CommandParameter 属性来传递参数。

- - 如有必要，使用 `Binding` 对象的 `Parse` 和 `Format` 事件进行自定义数据转换（`IValueConverter` 解决方法）。

```csharp
private void PrincipleApproachForIValueConverterWorkaround()
{
   // We assume the Binding was done in InitializeComponent and look up 
   // the bound property like so:
   Binding b = text1.DataBindings["Text"];

   // We hook up the "IValueConverter" functionality like so:
   b.Format += new ConvertEventHandler(DecimalToCurrencyString);
   b.Parse += new ConvertEventHandler(CurrencyStringToDecimal);
}
```
- 像往常一样绑定属性。
- 以同样的方式绑定命令 - ViewModel 是数据源！这样做：
```csharp
// Create BindingSource
components = new Container();
mainViewModelBindingSource = new BindingSource(components);

// Before SuspendLayout
mainViewModelBindingSource.DataSource = typeof(MyApp.ViewModels.MainViewModel);

// Bind properties
_txtDataField.DataBindings.Add(new Binding("Text", mainViewModelBindingSource, "PropertyName", true));

// Bind commands
_tsmFile.DataBindings.Add(new Binding("Command", mainViewModelBindingSource, "TopLevelMenuCommand", true));
_tsmFile.CommandParameter = "File";
```

---

## WinForms 异步模式 (.NET 9+)

### Control.InvokeAsync 重载选择

|您的代码类型 |超载|示例场景 |
|----------------|----------|------------------|
|同步行动，无返回| __代码0__ |更新 `label.Text` |
|异步操作，无返回 | __代码0__ |加载数据+更新UI |
|同步函数，返回T | __代码0__ |获取控制值 |
|异步操作，返回 T | __代码0__ |异步工作 + 结果 |

### ⚠️ 即发即忘陷阱

```csharp
// ❌ WRONG - Analyzer violation, fire-and-forget
await InvokeAsync<string>(() => await LoadDataAsync());

// ✅ CORRECT - Use async overload
await InvokeAsync<string>(async (ct) => await LoadDataAsync(ct), outerCancellationToken);
```

### 表单异步方法 (.NET 9+)

- `ShowAsync()`：表单关闭时完成。 
  请注意，返回任务的 IAsyncState 保存了对 Form 的弱引用，以便于查找！
- `ShowDialogAsync()`：具有专用消息队列的模态

### 关键：异步事件处理程序模式

- 以下所有规则对于 `[modifier] void async EventHandler(object? s, EventArgs e)` 以及重写的虚拟方法（如 `async void OnLoad` 或 `async void OnClick`）都适用。
- 当努力实现所需的异步实现时，`async void` 事件处理程序是 WinForms UI 事件的标准模式。 
- 关键：始终在异步事件处理程序中的 `try/catch` 中嵌套 `await MethodAsync()` 调用 - 否则，您将面临进程崩溃的风险。

## WinForms 中的异常处理

### 应用程序级异常处理

WinForms 提供了两种主要机制来处理未处理的异常：

**AppDomain.CurrentDomain.UnhandledException：**
- 捕获 AppDomain 中任何线程的异常
- 无法阻止应用程序终止
- 用于在关机前记录严重错误

**应用程序.ThreadException：**
- 仅捕获 UI 线程上的异常
- 可以通过处理异常来防止应用程序崩溃
- 用于 UI 操作中的优雅错误恢复

### Async/Await 上下文中的异常调度

在异步上下文中重新抛出异常时保留堆栈跟踪时：

```csharp
try
{
    await SomeAsyncOperation();
}
catch (Exception ex)
{
    if (ex is OperationCanceledException)
    {
        // Handle cancellation
    }
    else
    {
        ExceptionDispatchInfo.Capture(ex).Throw();
    }
}
```

**重要说明：**
- `Application.OnThreadException` 路由到 UI 线程的异常处理程序并触发 `Application.ThreadException`。 
- 切勿从后台线程调用它——首先编组到 UI 线程。
- 对于未处理异常的进程终止，请在启动时使用 `Application.SetUnhandledExceptionMode(UnhandledExceptionMode.ThrowException)` 。
- **VB 限制：** VB 不能在 catch 块中等待。避免或解决状态机模式。

## 关键：管理 CodeDOM 序列化

从 `Component` 或 `Control` 派生的类型的属性的代码生成规则：

|方法|属性|使用案例|示例|
|----------|-----------|----------|---------|
|默认值| __代码0__ |简单类型，如果匹配默认则不序列化 | __代码1__ |
|隐藏 | __代码0__ |仅运行时数据 |集合、计算属性 |
|有条件| __代码0__ + __代码1__ |复杂条件|自定义字体，可选设置|

```csharp
public class CustomControl : Control
{
    private Font? _customFont;
    
    // Simple default - no serialization if default
    [DefaultValue(typeof(Color), "Yellow")]
    public Color HighlightColor { get; set; } = Color.Yellow;
    
    // Hidden - never serialize
    [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
    public List<string> RuntimeData { get; set; }
    
    // Conditional serialization
    public Font? CustomFont
    {
        get => _customFont ?? Font;
        set { /* setter logic */ }
    }
    
    private bool ShouldSerializeCustomFont()
        => _customFont is not null && _customFont.Size != 9.0f;
    
    private void ResetCustomFont()
        => _customFont = null;
}
```

**重要提示：** 对于从 `Component` 或 `Control` 派生的类型，每个属性仅使用上述方法之一。

---

## WinForms 设计原则

### 核心规则

**缩放和 DPI：**
- 使用足够的边距/填充；与控件的绝对定位相比，更喜欢 TableLayoutPanel (TLP)/FlowLayoutPanel (FLP)。
- TLP 的布局单元尺寸方法优先级是：
  * 行：自动调整大小 > 百分比 > 绝对值
  * 列：自动调整大小 > 百分比 > 绝对值

- 对于新添加的表单/用户控件：假设 `AutoScaleMode` 为 96 DPI/100% 并缩放
- 对于现有表单：保留 AutoScaleMode 设置不变，但考虑坐标相关属性的缩放

- 在 .NET 9+ 中了解 DarkMode - 查询当前 DarkMode 状态：`Application.IsDarkModeEnabled`
  * 注意：在深色模式下，只有 `SystemColors` 值会自动更改为互补调色板。

- 因此，所有者绘制控件、自定义内容绘制和 DataGridView 主题/着色需要使用绝对颜色值进行自定义。

### 布局策略

**分而治之：**
- 对逻辑部分使用多个或嵌套的 TLP - 不要将所有内容都塞进一个巨型网格中。
- 主表单使用 SplitContainer 或“外部”TLP，其中主要部分使用 % 或 AutoSize-rows/cols。
- 每个 UI 部分都有自己的嵌套 TLP，或者（在复杂的情况下）一个 UserControl，它已设置为处理区域详细信息。

**保持简单：**
- 单个 TLP 最多应为 2-4 列
- 使用具有嵌套 TLP 的 GroupBox 可确保清晰的视觉分组。
- RadioButtons 集群规则：AutoGrow/AutoSize GroupBox 内的单列、自动调整单元格大小的 TLP。
- 大内容区域滚动：将嵌套面板控件与启用 `AutoScroll` 的可滚动视图结合使用。

**尺寸规则：TLP 细胞基础**
- 栏目：
  * 带有 `Anchor = Left | Right` 的标题列的 AutoSize。
  * 内容列的百分比，合理推理的百分比分布，`Anchor = Top | Bottom | Left | Right`。 
    切勿停靠细胞，始终锚定！
  * 避免_绝对_列大小调整模式，除非不可避免的固定大小内容（图标、按钮）。
- 行：
  * 自动调整具有“单行”字符的行（典型的输入字段、标题、复选框）。
  * 多行文本框、渲染区域和剩余空间的填充距离填充物的百分比，例如底部按钮行（确定|取消）。
  * 更要避免_Absolute_行大小调整模式。

- 边距很重要：在控件上设置 `Margin`（最小默认 3px）。 
- 注意：`Padding` 对 TLP 细胞没有影响。

### 常见的布局模式

#### 单行文本框（2 列 TLP）
**最常见的数据输入模式：**
- 标签列：AutoSize 宽度
- 文本框列：100% 百分比宽度
- 标签：`Anchor = Left | Right`（与 TextBox 垂直居中）
- 文本框：`Dock = Fill`，设置 `Margin`（例如，所有边均为 3px）

#### 多行文本框或更大的自定义内容 - 选项 A（2 列 TLP）
- 同一行中的标签，`Anchor = Top | Left`
- 文本框：`Dock = Fill`，设置`Margin`
- 行高：自动调整大小或百分比来调整单元格大小（单元格大小为文本框）

#### 多行文本框或更大的自定义内容 - 选项 B（1 列 TLP，单独的行）
- 文本框上方专用行中的标签
- 标签：`Dock = Fill` 或 `Anchor = Left`
- 下一行中的文本框：`Dock = Fill`，设置`Margin`
- 文本框行：自动调整大小或百分比以调整单元格大小

**关键：** 对于多行 TextBox，TLP 单元格定义大小，而不是 TextBox 的内容。

### 容器尺寸（关键 - 防止剪切）

**对于 TLP 单元内的 GroupBox/Panel：**
- 必须设置 `AutoSize = true` 和 `AutoSizeMode = GrowOnly`
- 单元格中应该有 `Dock = Fill`
- 父 TLP 行应为 AutoSize
- GroupBox/Panel 内的内容应使用嵌套 TLP 或 FlowLayoutPanel

**原因：** 即使父行为 AutoSize，固定高度容器也会剪辑内容。容器报告其固定尺寸，从而打破了尺寸链。

### 模态对话框按钮放置

**模式 A - 右下角按钮（“确定”/“取消”的标准按钮）：**
- 将按钮放置在 FlowLayoutPanel 中：`FlowDirection = RightToLeft`
- 在按钮和内容之间保留额外的百分比填充行。
- FLP 位于主 TLP 的底行
- 按钮的视觉顺序：[确定]（左）[取消]（右）

**模式 B - 右上角堆叠按钮（向导/浏览器）：**
- 将按钮放置在 FlowLayoutPanel 中：`FlowDirection = TopDown`
- 主 TLP 的专用最右列中的 FLP
- 列：自动调整大小
- FLP：__代码0__
- 订单：[确定]上方[取消]

**何时使用：**
- 模式 A：数据输入对话框、设置、确认
- 模式 B：多步骤向导、需要大量导航的对话框

### 复杂的布局

- 对于复杂的布局，请考虑为逻辑部分创建专用的用户控件。
- 然后：将这些UserControl嵌套在Form/UserControl的（外部）TLP中，并使用DataContext进行数据传递。
- 每个 TabPage 一个 UserControl 使设计器代码可以针对选项卡式界面进行管理。

### 模态对话框

|方面|规则|
|--------|------|
|对话框按钮|订单 -> 主要（确定）：`AcceptButton`、`DialogResult = OK` / 次要（取消）：`CancelButton`、`DialogResult = Cancel` |
|关闭策略| `DialogResult` 由 DialogResult 隐式应用，无需额外代码 |
|验证 |在 _Form_ 上执行，而不是在字段范围上执行。切勿使用 `CancelEventArgs.Cancel = true` | 阻止焦点更改

使用 Form 的 `DataContext` 属性 (.NET 8+) 传递和返回模态数据对象。

### 布局食谱

|表格类型 |结构|
|-----------|-----------|
|主窗体 | MenuStrip、可选 ToolStrip、内容区域、StatusStrip |
|简单报名表|数据输入字段大部分位于左侧，右侧只有一个按钮列。为模态设置有意义的形式 `MinimumSize` |
|标签 |仅适用于不同的任务。保持最少数量、短标签标签 |

### 无障碍

- 关键：在可操作控件上设置 `AccessibleName` 和 `AccessibleDescription`
- 通过 `TabIndex` 维护逻辑控制选项卡顺序（A11Y 遵循控制添加顺序）
- 验证纯键盘导航、明确的助记符和屏幕阅读器兼容性

### 树视图和列表视图

|控制|规则|
|---------|-------|
|树视图 |必须具有可见的、默认展开的根节点 |
|列表视图 |对于列数较少的小型列表，优于 DataGridView |
|内容设置|在代码中生成，而不是在设计器代码隐藏中生成 |
|列表视图列 |填充 | 后设置为 `-1` （最长内容的大小）或 `-2` （标题名称的大小）
|拆分容器 |用于 TreeView/ListView 的可调整大小的窗格 |

### 数据网格视图

- 首选启用双缓冲的派生类
- 在黑暗模式下配置颜色！
- 大数据：页面/虚拟化（`VirtualMode = True` 和 `CellValueNeeded`）

### 资源和本地化

- UI 显示的字符串常量需要位于资源文件中。
- 布局表单/用户控件时，请考虑本地化标题可能具有不同的字符串长度。 
- 不要使用图标库，而是尝试使用“Segoe UI Symbol”字体渲染图标。 
- 如果需要图像，请编写一个辅助类，以所需的大小呈现字体中的符号。

## 重要提醒

| ＃|规则|
|---|------|
| 1 | `InitializeComponent` 代码用作序列化格式 - 更像 XML，而不是 C# |
| 2 |两个上下文，两个规则集 - 设计器代码隐藏与常规代码 |
| 3 |在生成代码之前验证表单/控件名称 |
| 4 |遵守 `InitializeComponent` | 的编码风格规则
| 5 |设计器文件从不使用 NRT 注释 |
| 6 |仅适用于常规代码的现代 C# 功能 |
| 7 |数据绑定：将 ViewModel 视为数据源，记住 `Command` 和 `CommandParameter` 属性 |
