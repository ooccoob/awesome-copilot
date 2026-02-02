---
description: 'Instructions for upgrading .NET MAUI applications from version 9 to version 10, including breaking changes, deprecated APIs, and migration strategies for ListView to CollectionView.'
applyTo: '**/*.csproj, **/*.cs, **/*.xaml'
---

# 从 .NET MAUI 9 升级到 .NET MAUI 10

本指南重点关注需要代码更新的关键重大更改和过时的 API，帮助您将 .NET MAUI 应用程序从 .NET 9 升级到 .NET 10。

---

## 目录

1. [快速入门](#quick-start)
2. [更新目标框架](#update-target-framework)
3. [重大更改（P0 - 必须修复）](#breaking-changes-p0---must-fix)
   - [内部消息中心](#messagingcenter-made-internal)
   - [ListView 和 TableView 已弃用](#listview-and-tableview-deprecated)
4. [已弃用的 API（P1 - 很快修复）](#deprecated-apis-p1---fix-soon)
   - [动画方法](#1-animation-methods)
   - [DisplayAlert 和 DisplayActionSheet](#2-displayalert-and-displayactionsheet)
   - [Page.IsBusy](#3-pageisbusy)
   - [MediaPicker API](#4-mediapicker-apis)
5. [建议更改 (P2)](#recommended-changes-p2)
6. [批量迁移工具](#bulk-migration-tools)
7. [测试您的升级](#testing-your-upgrade)
8. [疑难解答](#troubleshooting)

---

## 快速入门

**五步升级过程：**

1. **将 TargetFramework** 更新为 `net10.0`
2. **将 CommunityToolkit.Maui** 更新到 12.3.0+（如果您使用它）- 必需
3. **修复重大更改** - MessagingCenter (P0)
4. **将 ListView/TableView 迁移到 CollectionView**（P0 - 关键）
5. **修复已弃用的 API** - 动画方法、DisplayAlert、IsBusy、MediaPicker (P1)

> ⚠️ **重大突破性变更**： 
> - CommunityToolkit.Maui **必须** 版本为 12.3.0 或更高版本
> - ListView 和 TableView 现已过时（最重要的迁移工作）

---

## 更新目标框架

### 单一平台

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
  </PropertyGroup>
</Project>
```

### 多平台

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFrameworks>net10.0-android;net10.0-ios;net10.0-maccatalyst;net10.0-windows10.0.19041.0</TargetFrameworks>
  </PropertyGroup>
</Project>
```

### 可选：Linux 兼容性（GitHub Copilot、WSL 等）

> 💡 **对于 Linux 开发**：如果您在 Linux 上构建（例如，GitHub Codespaces、WSL 或使用 GitHub Copilot），您可以通过有条件地排除 iOS/Mac Catalyst 目标来使您的项目在 Linux 上编译：

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <!-- Start with Android (always supported) -->
    <TargetFrameworks>net10.0-android</TargetFrameworks>
    
    <!-- Add iOS/Mac Catalyst only when NOT on Linux -->
    <TargetFrameworks Condition="!$([MSBuild]::IsOSPlatform('linux'))">$(TargetFrameworks);net10.0-ios;net10.0-maccatalyst</TargetFrameworks>
    
    <!-- Add Windows only when on Windows -->
    <TargetFrameworks Condition="$([MSBuild]::IsOSPlatform('windows'))">$(TargetFrameworks);net10.0-windows10.0.19041.0</TargetFrameworks>
  </PropertyGroup>
</Project>
```

**好处：**
- ✅ 在 Linux 上成功编译（无需 iOS/Mac 工具）
- ✅ 可与 GitHub Codespaces 和 Copilot 配合使用
- ✅ 根据构建操作系统自动包含正确的目标
- ✅ 在操作系统环境之间切换时无需更改

**参考：** [dotnet/maui#32186](https://github.com/dotnet/maui/pull/32186)

### 更新所需的 NuGet 包

> ⚠️ **重要**：如果您使用 CommunityToolkit.Maui，则 **必须** 更新到版本 12.3.0 或更高版本。早期版本与.NET 10不兼容，会导致编译错误。

```bash
# Update CommunityToolkit.Maui (if you use it)
dotnet add package CommunityToolkit.Maui --version 12.3.0

# Update other common packages to .NET 10 compatible versions
dotnet add package Microsoft.Maui.Controls --version 10.0.0
```

**检查所有 NuGet 包：**
```bash
# List all packages and check for updates
dotnet list package --outdated

# Update all packages to latest compatible versions
dotnet list package --outdated | grep ">" | cut -d '>' -f 1 | xargs -I {} dotnet add package {}
```

---

## 重大变更（P0 - 必须修复）

### 内部的消息中心

**状态：** 🚨 **中断** - `MessagingCenter` 现在是 `internal` 并且无法访问。

**您将看到的错误：**
```
error CS0122: 'MessagingCenter' is inaccessible due to its protection level
```

**需要迁移：**

#### 步骤1：安装CommunityToolkit.Mvvm

```bash
dotnet add package CommunityToolkit.Mvvm --version 8.3.0
```

#### 第 2 步：定义消息类别

```csharp
// OLD: No message class needed
MessagingCenter.Send(this, "UserLoggedIn", userData);

// NEW: Create a message class
public class UserLoggedInMessage
{
    public UserData Data { get; set; }
    
    public UserLoggedInMessage(UserData data)
    {
        Data = data;
    }
}
```

#### 第 3 步：更新发送呼叫

```csharp
// ❌ OLD (Broken in .NET 10)
using Microsoft.Maui.Controls;

MessagingCenter.Send(this, "UserLoggedIn", userData);
MessagingCenter.Send<App, string>(this, "StatusChanged", "Active");

// ✅ NEW (Required)
using CommunityToolkit.Mvvm.Messaging;

WeakReferenceMessenger.Default.Send(new UserLoggedInMessage(userData));
WeakReferenceMessenger.Default.Send(new StatusChangedMessage("Active"));
```

#### 第 4 步：更新订阅通话

```csharp
// ❌ OLD (Broken in .NET 10)
MessagingCenter.Subscribe<App, UserData>(this, "UserLoggedIn", (sender, data) =>
{
    // Handle message
    CurrentUser = data;
});

// ✅ NEW (Required)
WeakReferenceMessenger.Default.Register<UserLoggedInMessage>(this, (recipient, message) =>
{
    // Handle message
    CurrentUser = message.Data;
});
```

#### ⚠️ 重要的行为差异：重复订阅

如果您尝试向同一收件人多次注册相同的消息类型，**WeakReferenceMessenger** 会抛出 `InvalidOperationException`（MessagingCenter 允许这样做）：

```csharp
// ❌ This THROWS InvalidOperationException in WeakReferenceMessenger
WeakReferenceMessenger.Default.Register<UserLoggedInMessage>(this, (r, m) => Handler1(m));
WeakReferenceMessenger.Default.Register<UserLoggedInMessage>(this, (r, m) => Handler2(m)); // ❌ THROWS!

// ✅ Solution 1: Unregister before re-registering
WeakReferenceMessenger.Default.Unregister<UserLoggedInMessage>(this);
WeakReferenceMessenger.Default.Register<UserLoggedInMessage>(this, (r, m) => Handler1(m));

// ✅ Solution 2: Handle multiple actions in one registration
WeakReferenceMessenger.Default.Register<UserLoggedInMessage>(this, (r, m) => 
{
    Handler1(m);
    Handler2(m);
});
```

**为什么这很重要：** 如果您的代码在多个位置（例如，在页面构造函数中和 `OnAppearing` 中）订阅同一消息，您将遇到运行时崩溃。

#### 第 5 步：完成后取消注册

```csharp
// ❌ OLD
MessagingCenter.Unsubscribe<App, UserData>(this, "UserLoggedIn");

// ✅ NEW (CRITICAL - prevents memory leaks)
WeakReferenceMessenger.Default.Unregister<UserLoggedInMessage>(this);

// Or unregister all messages for this recipient
WeakReferenceMessenger.Default.UnregisterAll(this);
```

#### 完成之前/之后示例

**之前 (.NET 9)：**
```csharp
// Sender
public class LoginViewModel
{
    public async Task LoginAsync()
    {
        var user = await AuthService.LoginAsync(username, password);
        MessagingCenter.Send(this, "UserLoggedIn", user);
    }
}

// Receiver
public partial class MainPage : ContentPage
{
    public MainPage()
    {
        InitializeComponent();
        
        MessagingCenter.Subscribe<LoginViewModel, User>(this, "UserLoggedIn", (sender, user) =>
        {
            WelcomeLabel.Text = $"Welcome, {user.Name}!";
        });
    }
    
    protected override void OnDisappearing()
    {
        base.OnDisappearing();
        MessagingCenter.Unsubscribe<LoginViewModel, User>(this, "UserLoggedIn");
    }
}
```

**（.NET 10）之后：**
```csharp
// 1. Define message
public class UserLoggedInMessage
{
    public User User { get; }
    
    public UserLoggedInMessage(User user)
    {
        User = user;
    }
}

// 2. Sender
public class LoginViewModel
{
    public async Task LoginAsync()
    {
        var user = await AuthService.LoginAsync(username, password);
        WeakReferenceMessenger.Default.Send(new UserLoggedInMessage(user));
    }
}

// 3. Receiver
public partial class MainPage : ContentPage
{
    public MainPage()
    {
        InitializeComponent();
        
        WeakReferenceMessenger.Default.Register<UserLoggedInMessage>(this, (recipient, message) =>
        {
            WelcomeLabel.Text = $"Welcome, {message.User.Name}!";
        });
    }
    
    protected override void OnDisappearing()
    {
        base.OnDisappearing();
        WeakReferenceMessenger.Default.UnregisterAll(this);
    }
}
```

**主要区别：**
- ✅ 类型安全的消息类
- ✅ 没有魔法弦
- ✅ 更好的智能感知支持
- ✅ 更容易重构
- ⚠️ **一定要记得注销！**

---

### ListView 和 TableView 已弃用

**状态：** 🚨 **已弃用 (P0)** - `ListView`、`TableView` 和所有单元格类型现已过时。迁移到 `CollectionView`。

**警告您会看到：**
```
warning CS0618: 'ListView' is obsolete: 'ListView is deprecated. Please use CollectionView instead.'
warning CS0618: 'TableView' is obsolete: 'Please use CollectionView instead.'
warning CS0618: 'TextCell' is obsolete: 'The controls which use TextCell (ListView and TableView) are obsolete. Please use CollectionView instead.'
```

**过时的类型：**
- __代码0__ → __代码1__
- `TableView` → `CollectionView` （对于设置页面，请考虑垂直 StackLayout 和 BindableLayout）
- `TextCell` → 带标签的自定义数据模板
- `ImageCell` → 带有图像+标签的自定义数据模板
- `EntryCell` → 带条目的自定义数据模板
- `SwitchCell` → 带开关的自定义数据模板
- `ViewCell` → 数据模板

**影响：** 这是一个 **重大** 重大变更。 ListView 和 TableView 是 MAUI 应用程序中最常用的控件。

#### 为什么这需要时间

将ListView/TableView转换为CollectionView并不是简单的查找-替换：

1. **不同的事件模型** - `ItemSelected` → `SelectionChanged` 具有不同的参数
2. **不同的分组** - GroupDisplayBinding 不再存在
3. **上下文操作** - 必须转换为 SwipeView
4. **项目尺寸** - `HasUnevenRows` 处理方式不同
5. **特定于平台的代码** - iOS/Android ListView 平台配置需要删除
6. **需要测试** - CollectionView 虚拟化方式不同，可能会影响性能

#### 迁移策略

**第 1 步：清点您的 ListViews**

```bash
# Find all ListView/TableView usages
grep -r "ListView\|TableView" --include="*.xaml" --include="*.cs" .
```

**第2步：基本ListView→CollectionView**

**之前（列表视图）：**
```xaml
<ListView ItemsSource="{Binding Items}"
          ItemSelected="OnItemSelected"
          HasUnevenRows="True">
    <ListView.ItemTemplate>
        <DataTemplate>
            <TextCell Text="{Binding Title}"
                     Detail="{Binding Description}" />
        </DataTemplate>
    </ListView.ItemTemplate>
</ListView>
```

**之后（CollectionView）：**
```xaml
<CollectionView ItemsSource="{Binding Items}"
                SelectionMode="Single"
                SelectionChanged="OnSelectionChanged">
    <CollectionView.ItemTemplate>
        <DataTemplate>
            <VerticalStackLayout Padding="10">
                <Label Text="{Binding Title}" 
                       FontAttributes="Bold" />
                <Label Text="{Binding Description}"
                       FontSize="12"
                       TextColor="{StaticResource Gray600}" />
            </VerticalStackLayout>
        </DataTemplate>
    </CollectionView.ItemTemplate>
</CollectionView>
```

> ⚠️ **注意：** CollectionView 默认情况下具有 `SelectionMode="None"` （禁用选择）。您必须显式设置 `SelectionMode="Single"` 或 `SelectionMode="Multiple"` 才能启用选择。

**代码隐藏更改：**
```csharp
// ❌ OLD (ListView)
void OnItemSelected(object sender, SelectedItemChangedEventArgs e)
{
    if (e.SelectedItem == null)
        return;
        
    var item = (MyItem)e.SelectedItem;
    // Handle selection
    
    // Deselect
    ((ListView)sender).SelectedItem = null;
}

// ✅ NEW (CollectionView)
void OnSelectionChanged(object sender, SelectionChangedEventArgs e)
{
    if (e.CurrentSelection.Count == 0)
        return;
        
    var item = (MyItem)e.CurrentSelection.FirstOrDefault();
    // Handle selection
    
    // Deselect (optional)
    ((CollectionView)sender).SelectedItem = null;
}
```

**步骤 3：分组 ListView → 分组 CollectionView**

**之前（分组列表视图）：**
```xaml
<ListView ItemsSource="{Binding GroupedItems}"
          IsGroupingEnabled="True"
          GroupDisplayBinding="{Binding Key}">
    <ListView.ItemTemplate>
        <DataTemplate>
            <TextCell Text="{Binding Name}" />
        </DataTemplate>
    </ListView.ItemTemplate>
</ListView>
```

**之后（分组 CollectionView）：**
```xaml
<CollectionView ItemsSource="{Binding GroupedItems}"
                IsGrouped="true">
    <CollectionView.GroupHeaderTemplate>
        <DataTemplate>
            <Label Text="{Binding Key}"
                   FontAttributes="Bold"
                   BackgroundColor="{StaticResource Gray100}"
                   Padding="10,5" />
        </DataTemplate>
    </CollectionView.GroupHeaderTemplate>
    
    <CollectionView.ItemTemplate>
        <DataTemplate>
            <VerticalStackLayout Padding="20,10">
                <Label Text="{Binding Name}" />
            </VerticalStackLayout>
        </DataTemplate>
    </CollectionView.ItemTemplate>
</CollectionView>
```

**第 4 步：上下文操作 → SwipeView**

> ⚠️ **平台注意：** SwipeView 需要触摸输入。在 Windows 桌面上，它仅适用于触摸屏，不适用于鼠标/触控板。考虑为桌面场景提供替代 UI（例如按钮、右键菜单）。

**之前（带有 ContextActions 的 ListView）：**
```xaml
<ListView.ItemTemplate>
    <DataTemplate>
        <ViewCell>
            <ViewCell.ContextActions>
                <MenuItem Text="Delete" 
                         IsDestructive="True"
                         Command="{Binding Source={RelativeSource AncestorType={x:Type local:MyPage}}, Path=DeleteCommand}"
                         CommandParameter="{Binding .}" />
            </ViewCell.ContextActions>
            
            <Label Text="{Binding Title}" Padding="10" />
        </ViewCell>
    </DataTemplate>
</ListView.ItemTemplate>
```

**之后（CollectionView 与 SwipeView）：**
```xaml
<CollectionView.ItemTemplate>
    <DataTemplate>
        <SwipeView>
            <SwipeView.RightItems>
                <SwipeItems>
                    <SwipeItem Text="Delete"
                              BackgroundColor="Red"
                              Command="{Binding Source={RelativeSource AncestorType={x:Type local:MyPage}}, Path=DeleteCommand}"
                              CommandParameter="{Binding .}" />
                </SwipeItems>
            </SwipeView.RightItems>
            
            <VerticalStackLayout Padding="10">
                <Label Text="{Binding Title}" />
            </VerticalStackLayout>
        </SwipeView>
    </DataTemplate>
</CollectionView.ItemTemplate>
```

**第 5 步：设置的 TableView → 替代方法**

TableView 通常用于设置页面。以下是现代替代方案：

**选项 1：带有分组数据的 CollectionView**
```xaml
<CollectionView ItemsSource="{Binding SettingGroups}"
                IsGrouped="true"
                SelectionMode="None">
    <CollectionView.GroupHeaderTemplate>
        <DataTemplate>
            <Label Text="{Binding Title}" 
                   FontAttributes="Bold"
                   Margin="10,15,10,5" />
        </DataTemplate>
    </CollectionView.GroupHeaderTemplate>
    
    <CollectionView.ItemTemplate>
        <DataTemplate>
            <Grid Padding="15,10" ColumnDefinitions="*,Auto">
                <Label Text="{Binding Title}" 
                       VerticalOptions="Center" />
                <Switch Grid.Column="1" 
                        IsToggled="{Binding IsEnabled}"
                        IsVisible="{Binding ShowSwitch}" />
            </Grid>
        </DataTemplate>
    </CollectionView.ItemTemplate>
</CollectionView>
```

**选项 2：垂直 StackLayout（适用于小型设置列表）**
```xaml
<ScrollView>
    <VerticalStackLayout BindableLayout.ItemsSource="{Binding Settings}"
                        Spacing="10"
                        Padding="15">
        <BindableLayout.ItemTemplate>
            <DataTemplate>
                <Border StrokeThickness="0"
                       BackgroundColor="{StaticResource Gray100}"
                       Padding="15,10">
                    <Grid ColumnDefinitions="*,Auto">
                        <Label Text="{Binding Title}" 
                              VerticalOptions="Center" />
                        <Switch Grid.Column="1" 
                               IsToggled="{Binding IsEnabled}" />
                    </Grid>
                </Border>
            </DataTemplate>
        </BindableLayout.ItemTemplate>
    </VerticalStackLayout>
</ScrollView>
```

**步骤 6：删除特定于平台的 ListView 代码**

如果您使用了特定于平台的 ListView 功能，请删除它们：

```csharp
// ❌ OLD - Remove these using statements (NOW OBSOLETE IN .NET 10)
using Microsoft.Maui.Controls.PlatformConfiguration;
using Microsoft.Maui.Controls.PlatformConfiguration.iOSSpecific;
using Microsoft.Maui.Controls.PlatformConfiguration.AndroidSpecific;

// ❌ OLD - Remove ListView platform configurations (NOW OBSOLETE IN .NET 10)
myListView.On<iOS>().SetSeparatorStyle(SeparatorStyle.FullWidth);
myListView.On<Android>().IsFastScrollEnabled();

// ❌ OLD - Remove Cell platform configurations (NOW OBSOLETE IN .NET 10)
viewCell.On<iOS>().SetDefaultBackgroundColor(Colors.White);
viewCell.On<Android>().SetIsContextActionsLegacyModeEnabled(false);
```

**迁移：** CollectionView 没有以同样的方式进行特定于平台的配置。如果您需要特定于平台的样式：

```csharp
// ✅ NEW - Use conditional compilation
#if IOS
var backgroundColor = Colors.White;
#elif ANDROID
var backgroundColor = Colors.Transparent;
#endif

var grid = new Grid
{
    BackgroundColor = backgroundColor,
    // ... rest of cell content
};
```

或者在 XAML 中：
```xaml
<CollectionView.ItemTemplate>
    <DataTemplate>
        <Grid>
            <Grid.BackgroundColor>
                <OnPlatform x:TypeArguments="Color">
                    <On Platform="iOS" Value="White" />
                    <On Platform="Android" Value="Transparent" />
                </OnPlatform>
            </Grid.BackgroundColor>
            <!-- Cell content -->
        </Grid>
    </DataTemplate>
</CollectionView.ItemTemplate>
```

#### 常见模式和陷阱

**1.空视图**
```xaml
<!-- CollectionView has built-in EmptyView support -->
<CollectionView ItemsSource="{Binding Items}">
    <CollectionView.EmptyView>
        <ContentView>
            <VerticalStackLayout Padding="50" VerticalOptions="Center">
                <Label Text="No items found" 
                       HorizontalTextAlignment="Center" />
            </VerticalStackLayout>
        </ContentView>
    </CollectionView.EmptyView>
    <!-- ... -->
</CollectionView>
```

**2.拉动刷新**
```xaml
<RefreshView IsRefreshing="{Binding IsRefreshing}"
             Command="{Binding RefreshCommand}">
    <CollectionView ItemsSource="{Binding Items}">
        <!-- ... -->
    </CollectionView>
</RefreshView>
```

**3.项目间距**
```xaml
<!-- Use ItemsLayout for spacing -->
<CollectionView ItemsSource="{Binding Items}">
    <CollectionView.ItemsLayout>
        <LinearItemsLayout Orientation="Vertical" 
                          ItemSpacing="10" />
    </CollectionView.ItemsLayout>
    <!-- ... -->
</CollectionView>
```

**4.页眉和页脚**
```xaml
<CollectionView ItemsSource="{Binding Items}">
    <CollectionView.Header>
        <Label Text="My List" 
               FontSize="24" 
               Padding="10" />
    </CollectionView.Header>
    
    <CollectionView.Footer>
        <Label Text="End of list" 
               Padding="10" 
               HorizontalTextAlignment="Center" />
    </CollectionView.Footer>
    
    <!-- ItemTemplate -->
</CollectionView>
```

**5.加载更多/无限滚动**
```xaml
<CollectionView ItemsSource="{Binding Items}"
                RemainingItemsThreshold="5"
                RemainingItemsThresholdReachedCommand="{Binding LoadMoreCommand}">
    <!-- ItemTemplate -->
</CollectionView>
```

**6。商品尺寸优化**

CollectionView 使用 `ItemSizingStrategy` 来控制项目测量：

```xaml
<!-- Default: Each item measured individually (like HasUnevenRows="True") -->
<CollectionView ItemSizingStrategy="MeasureAllItems">
    <!-- ... -->
</CollectionView>

<!-- Performance: Only first item measured, rest use same height -->
<CollectionView ItemSizingStrategy="MeasureFirstItem">
    <!-- Use this when all items have similar heights -->
</CollectionView>
```

> 💡 **性能提示：** 如果您的列表项具有一致的高度，请使用 `ItemSizingStrategy="MeasureFirstItem"` 以获得大型列表的更好性能。

#### .NET 10 处理程序更改（iOS/Mac Catalyst）

> ℹ️ **.NET 10 默认在 iOS 和 Mac Catalyst 上使用新的优化的 CollectionView 和 CarouselView 处理程序**，从而提供改进的性能和稳定性。

**如果您之前选择使用 .NET 9 中的新处理程序**，您现在应该**删除**以下代码：

```csharp
// ❌ REMOVE THIS in .NET 10 (these handlers are now default)
#if IOS || MACCATALYST
builder.ConfigureMauiHandlers(handlers =>
{
    handlers.AddHandler<CollectionView, CollectionViewHandler2>();
    handlers.AddHandler<CarouselView, CarouselViewHandler2>();
});
#endif
```

优化的处理程序在 .NET 10 中自动使用 - 无需配置！

**仅当您遇到问题**时，您可以恢复到旧处理程序：

```csharp
// In MauiProgram.cs - only if needed
#if IOS || MACCATALYST
builder.ConfigureMauiHandlers(handlers =>
{
    handlers.AddHandler<Microsoft.Maui.Controls.CollectionView, 
                        Microsoft.Maui.Controls.Handlers.Items.CollectionViewHandler>();
});
#endif
```

但是，Microsoft 建议使用新的默认处理程序以获得最佳结果。

#### 测试清单

迁移后，测试这些场景：

- [ ] **项目选择**工作正常
- [ ] **分组列表**显示正确的标题
- [ ] **滑动操作**（如果使用）适用于 iOS 和 Android
- [ ] **空视图** 当列表为空时出现
- [ ] **拉动刷新**有效（如果使用）
- [ ] **滚动性能**是可以接受的（特别是对于大型列表）
- [ ] **项目大小**正确（CollectionView 默认情况下自动调整大小）
- [ ] **选择视觉状态**正确显示/隐藏
- [ ] **数据绑定**正确更新列表
- [ ] **从列表项导航**有效

#### 迁移复杂性因素

ListView 到 CollectionView 的迁移很复杂，因为：
- 每个 ListView 可能有独特的行为
- 特定于平台的代码需要更新
- 需要大量测试
- 上下文操作需要 SwipeView 转换
- 分组列表需要模板更新
- 可能需要更改 ViewModel

#### 快速参考：ListView 与 CollectionView

|特色|列表视图 |收藏查看 |
|---------|----------|----------------|
| **评选活动** | __代码0__ | __代码1__ |
| **选择参数** | __代码0__ | __代码1__ |
| **被选中** | __代码0__ | __代码1__ |
| **上下文菜单** | __代码0__ | __代码1__ |
| **分组** | __代码0__ | __代码1__ |
| **组标题** | __代码0__ | __代码1__ |
| **偶数行** | __代码0__ |自动调整大小（默认）|
| **空状态** |手册| `EmptyView` 属性 |
| **细胞** | TextCell、ImageCell 等 |自定义数据模板 |

---

## 已弃用的 API（P1 - 很快修复）

这些 API 仍然可以在 .NET 10 中工作，但会显示编译器警告。它们将在未来的版本中被删除。

### 1. 动画方法

**状态：** ⚠️ **已弃用** - 所有同步动画方法均替换为异步版本。

**警告您会看到：**
```
warning CS0618: 'ViewExtensions.FadeTo(VisualElement, double, uint, Easing)' is obsolete: 'Please use FadeToAsync instead.'
```

**迁移表：**

|老方法|新方法|示例|
|-----------|-----------|---------|
| __代码0__ | __代码1__ | __代码2__ |
| __代码0__ | __代码1__ | __代码2__ |
| __代码0__ | __代码1__ | __代码2__ |
| __代码0__ | __代码1__ | __代码2__ |
| __代码0__ | __代码1__ | __代码2__ |
| __代码0__ | __代码1__ | __代码2__ |
| __代码0__ | __代码1__ | __代码2__ |
| __代码0__ | __代码1__ | __代码2__ |
| __代码0__ | __代码1__ | __代码2__ |
| __代码0__ | __代码1__ | __代码2__ |
| __代码0__ | __代码1__ |请参阅下面的特别说明 |

#### 迁移示例

**简单动画：**
```csharp
// ❌ OLD (Deprecated)
await myButton.FadeTo(0, 500);
await myButton.ScaleTo(1.5, 300);
await myButton.TranslateTo(100, 100, 250);

// ✅ NEW (Required)
await myButton.FadeToAsync(0, 500);
await myButton.ScaleToAsync(1.5, 300);
await myButton.TranslateToAsync(100, 100, 250);
```

**连续动画：**
```csharp
// ❌ OLD
await image.FadeTo(0, 300);
await image.ScaleTo(0.5, 300);
await image.FadeTo(1, 300);

// ✅ NEW
await image.FadeToAsync(0, 300);
await image.ScaleToAsync(0.5, 300);
await image.FadeToAsync(1, 300);
```

**并行动画：**
```csharp
// ❌ OLD
await Task.WhenAll(
    image.FadeTo(0, 300),
    image.ScaleTo(0.5, 300),
    image.RotateTo(360, 300)
);

// ✅ NEW
await Task.WhenAll(
    image.FadeToAsync(0, 300),
    image.ScaleToAsync(0.5, 300),
    image.RotateToAsync(360, 300)
);
```

**取消：**
```csharp
// NEW: Async methods support cancellation
CancellationTokenSource cts = new();

try
{
    await view.FadeToAsync(0, 2000);
}
catch (TaskCanceledException)
{
    // Animation was cancelled
}

// Cancel from elsewhere
cts.Cancel();
```

#### 特殊情况：LayoutTo

`LayoutToAsync()` 已弃用，并显示一条特殊消息：“使用翻译来动画布局更改。”

```csharp
// ❌ OLD (Deprecated)
await view.LayoutToAsync(new Rect(100, 100, 200, 200), 250);

// ✅ NEW (Use TranslateToAsync instead)
await view.TranslateToAsync(100, 100, 250);

// Or animate Translation properties directly
var animation = new Animation(v => view.TranslationX = v, 0, 100);
animation.Commit(view, "MoveX", length: 250);
```

---

### 2. DisplayAlert和DisplayActionSheet

**状态：** ⚠️ **已弃用** - 同步方法替换为异步版本。

**警告您会看到：**
```
warning CS0618: 'Page.DisplayAlert(string, string, string)' is obsolete: 'Use DisplayAlertAsync instead'
```

#### 迁移示例

**显示警报：**
```csharp
// ❌ OLD (Deprecated)
await DisplayAlert("Success", "Data saved successfully", "OK");
await DisplayAlert("Error", "Failed to save", "Cancel");
bool result = await DisplayAlert("Confirm", "Delete this item?", "Yes", "No");

// ✅ NEW (Required)
await DisplayAlertAsync("Success", "Data saved successfully", "OK");
await DisplayAlertAsync("Error", "Failed to save", "Cancel");
bool result = await DisplayAlertAsync("Confirm", "Delete this item?", "Yes", "No");
```

**显示操作表：**
```csharp
// ❌ OLD (Deprecated)
string action = await DisplayActionSheet(
    "Choose an action",
    "Cancel",
    "Delete",
    "Edit", "Share", "Duplicate"
);

// ✅ NEW (Required)
string action = await DisplayActionSheetAsync(
    "Choose an action",
    "Cancel",
    "Delete",
    "Edit", "Share", "Duplicate"
);
```

**在 ViewModel 中（使用 IDispatcher）：**
```csharp
// If you're calling from a ViewModel, you'll need access to a Page
public class MyViewModel
{
    private readonly IDispatcher _dispatcher;
    private readonly Page _page;
    
    public MyViewModel(IDispatcher dispatcher, Page page)
    {
        _dispatcher = dispatcher;
        _page = page;
    }
    
    public async Task ShowAlertAsync()
    {
        await _dispatcher.DispatchAsync(async () =>
        {
            await _page.DisplayAlertAsync("Info", "Message from ViewModel", "OK");
        });
    }
}
```

---

### 3. Page.IsBusy

**状态：** ⚠️ **已弃用** - 属性将在 .NET 11 中删除。

**警告您会看到：**
```
warning CS0618: 'Page.IsBusy' is obsolete: 'Page.IsBusy has been deprecated and will be removed in .NET 11'
```

**为什么它被弃用：**
- 跨平台行为不一致
- 有限的定制选项
- 不适用于现代 MVVM 模式

#### 迁移示例

**简单页面：**
```xaml
<!-- ❌ OLD (Deprecated) -->
<ContentPage IsBusy="{Binding IsLoading}">
    <StackLayout>
        <Label Text="Content here" />
    </StackLayout>
</ContentPage>

<!-- ✅ NEW (Recommended) -->
<ContentPage>
    <Grid>
        <!-- Main content -->
        <StackLayout>
            <Label Text="Content here" />
        </StackLayout>
        
        <!-- Loading indicator overlay -->
        <ActivityIndicator IsRunning="{Binding IsLoading}"
                          IsVisible="{Binding IsLoading}"
                          Color="{StaticResource Primary}"
                          VerticalOptions="Center"
                          HorizontalOptions="Center" />
    </Grid>
</ContentPage>
```

**带有加载叠加：**
```xaml
<!-- ✅ Better: Custom loading overlay -->
<ContentPage>
    <Grid>
        <!-- Main content -->
        <ScrollView>
            <VerticalStackLayout Padding="20">
                <Label Text="Your content here" />
            </VerticalStackLayout>
        </ScrollView>
        
        <!-- Loading overlay -->
        <Grid IsVisible="{Binding IsLoading}"
              BackgroundColor="#80000000">
            <VerticalStackLayout VerticalOptions="Center"
                               HorizontalOptions="Center"
                               Spacing="10">
                <ActivityIndicator IsRunning="True"
                                 Color="White" />
                <Label Text="Loading..."
                       TextColor="White" />
            </VerticalStackLayout>
        </Grid>
    </Grid>
</ContentPage>
```

**在代码隐藏中：**
```csharp
// ❌ OLD (Deprecated)
public partial class MyPage : ContentPage
{
    async Task LoadDataAsync()
    {
        IsBusy = true;
        try
        {
            await LoadDataFromServerAsync();
        }
        finally
        {
            IsBusy = false;
        }
    }
}

// ✅ NEW (Recommended)
public partial class MyPage : ContentPage
{
    async Task LoadDataAsync()
    {
        LoadingIndicator.IsVisible = true;
        LoadingIndicator.IsRunning = true;
        try
        {
            await LoadDataFromServerAsync();
        }
        finally
        {
            LoadingIndicator.IsVisible = false;
            LoadingIndicator.IsRunning = false;
        }
    }
}
```

**在视图模型中：**
```csharp
public class MyViewModel : INotifyPropertyChanged
{
    private bool _isLoading;
    public bool IsLoading
    {
        get => _isLoading;
        set
        {
            _isLoading = value;
            OnPropertyChanged();
        }
    }
    
    public async Task LoadDataAsync()
    {
        IsLoading = true;
        try
        {
            await LoadDataFromServerAsync();
        }
        finally
        {
            IsLoading = false;
        }
    }
}
```

---

### 4.MediaPicker API

**状态：** ⚠️ **已弃用** - 单选方法替换为多选变体。

**警告您会看到：**
```
warning CS0618: 'MediaPicker.PickPhotoAsync(MediaPickerOptions)' is obsolete: 'Switch to PickPhotosAsync which also allows multiple selections.'
warning CS0618: 'MediaPicker.PickVideoAsync(MediaPickerOptions)' is obsolete: 'Switch to PickVideosAsync which also allows multiple selections.'
```

**改变了什么：**
- `PickPhotoAsync()` → `PickPhotosAsync()` （返回 `List<FileResult>`）
- `PickVideoAsync()` → `PickVideosAsync()` （返回 `List<FileResult>`）
- `MediaPickerOptions` 上的新 `SelectionLimit` 属性（默认值：1）
- 旧方法仍然有效，但已被标记为过时

**关键行为：**
- **保留默认行为：** `SelectionLimit = 1`（单选）
- 设置 `SelectionLimit = 0` 进行无限多选
- 设置 `SelectionLimit > 1` 以获得特定限制

**平台说明：**
- ✅ **iOS：** 由本机选择器 UI 强制执行选择限制
- ⚠️ **Android：** 并非所有自定义选择器都遵循 `SelectionLimit` - 请注意！
- ⚠️ **Windows：** 不支持 `SelectionLimit` - 实现您自己的验证

#### 迁移示例

**简单的照片选择器（保持单选行为）：**
```csharp
// ❌ OLD (Deprecated)
var photo = await MediaPicker.PickPhotoAsync(new MediaPickerOptions
{
    Title = "Pick a photo"
});

if (photo != null)
{
    var stream = await photo.OpenReadAsync();
    MyImage.Source = ImageSource.FromStream(() => stream);
}

// ✅ NEW (maintains same behavior - picks only 1 photo)
var photos = await MediaPicker.PickPhotosAsync(new MediaPickerOptions
{
    Title = "Pick a photo",
    SelectionLimit = 1  // Explicit: only 1 photo
});

var photo = photos.FirstOrDefault();
if (photo != null)
{
    var stream = await photo.OpenReadAsync();
    MyImage.Source = ImageSource.FromStream(() => stream);
}
```

**简单视频选择器（保持单选行为）：**
```csharp
// ❌ OLD (Deprecated)
var video = await MediaPicker.PickVideoAsync(new MediaPickerOptions
{
    Title = "Pick a video"
});

if (video != null)
{
    VideoPlayer.Source = video.FullPath;
}

// ✅ NEW (maintains same behavior - picks only 1 video)
var videos = await MediaPicker.PickVideosAsync(new MediaPickerOptions
{
    Title = "Pick a video",
    SelectionLimit = 1  // Explicit: only 1 video
});

var video = videos.FirstOrDefault();
if (video != null)
{
    VideoPlayer.Source = video.FullPath;
}
```

**不带选项的照片选择器（使用默认值）：**
```csharp
// ❌ OLD (Deprecated)
var photo = await MediaPicker.PickPhotoAsync();

// ✅ NEW (default SelectionLimit = 1, so same behavior)
var photos = await MediaPicker.PickPhotosAsync();
var photo = photos.FirstOrDefault();
```

**多照片选择（新功能）：**
```csharp
// ✅ NEW: Pick up to 5 photos
var photos = await MediaPicker.PickPhotosAsync(new MediaPickerOptions
{
    Title = "Pick up to 5 photos",
    SelectionLimit = 5
});

foreach (var photo in photos)
{
    var stream = await photo.OpenReadAsync();
    // Process each photo
}

// ✅ NEW: Unlimited selection
var allPhotos = await MediaPicker.PickPhotosAsync(new MediaPickerOptions
{
    Title = "Pick photos",
    SelectionLimit = 0  // No limit
});
```

**多视频选择（新功能）：**
```csharp
// ✅ NEW: Pick up to 3 videos
var videos = await MediaPicker.PickVideosAsync(new MediaPickerOptions
{
    Title = "Pick up to 3 videos",
    SelectionLimit = 3
});

foreach (var video in videos)
{
    // Process each video
    Console.WriteLine($"Selected: {video.FileName}");
}
```

**处理空结果：**
```csharp
// NEW: Returns empty list if user cancels (not null)
var photos = await MediaPicker.PickPhotosAsync(new MediaPickerOptions
{
    SelectionLimit = 1
});

// ✅ Check for empty list
if (photos.Count == 0)
{
    await DisplayAlertAsync("Cancelled", "No photo selected", "OK");
    return;
}

var photo = photos.First();
// Process photo...
```

**使用 Try-Catch（与之前相同）：**
```csharp
try
{
    var photos = await MediaPicker.PickPhotosAsync(new MediaPickerOptions
    {
        Title = "Pick a photo",
        SelectionLimit = 1
    });
    
    if (photos.Count > 0)
    {
        await ProcessPhotoAsync(photos.First());
    }
}
catch (PermissionException)
{
    await DisplayAlertAsync("Permission Denied", "Camera access required", "OK");
}
catch (Exception ex)
{
    await DisplayAlertAsync("Error", $"Failed to pick photo: {ex.Message}", "OK");
}
```

#### 迁移清单

迁移到新的 MediaPicker API 时：

- [ ] 将 `PickPhotoAsync()` 替换为 `PickPhotosAsync()`
- [ ] 将 `PickVideoAsync()` 替换为 `PickVideosAsync()`
- [ ] 设置 `SelectionLimit = 1` 以保持单选行为
- [ ] 将 `FileResult?` 更改为 `List<FileResult>` （或使用 `.FirstOrDefault()`）
- [ ] 将空检查更新为空列表检查 (`photos.Count == 0`)
- [ ] 在 Android 上测试 - 确保自定义选择器遵守限制（或添加验证）
- [ ] 在 Windows 上测试 - 如果需要，添加您自己的限制验证
- [ ] 考虑多重选择是否会改善您的用户体验（可选）

#### 特定于平台的验证（Windows 和 Android）

```csharp
// ✅ Recommended: Validate selection limit on platforms that don't enforce it
var photos = await MediaPicker.PickPhotosAsync(new MediaPickerOptions
{
    Title = "Pick up to 5 photos",
    SelectionLimit = 5
});

// On Windows and some Android pickers, the limit might not be enforced
if (photos.Count > 5)
{
    await DisplayAlertAsync(
        "Too Many Photos", 
        $"Please select up to 5 photos. You selected {photos.Count}.", 
        "OK"
    );
    return;
}

// Continue processing...
```

#### 捕获方法（不变）

**注意：** 捕获方法（`CapturePhotoAsync`、`CaptureVideoAsync`）**未**弃用并保持不变：

```csharp
// ✅ These still work as-is (no changes needed)
var photo = await MediaPicker.CapturePhotoAsync();
var video = await MediaPicker.CaptureVideoAsync();
```

#### 快速迁移模式

**对于所有现有的单选代码，请使用此模式：**

```csharp
// ❌ OLD
var photo = await MediaPicker.PickPhotoAsync(options);
if (photo != null)
{
    // Process photo
}

// ✅ NEW (drop-in replacement)
var photos = await MediaPicker.PickPhotosAsync(options ?? new MediaPickerOptions { SelectionLimit = 1 });
var photo = photos.FirstOrDefault();
if (photo != null)
{
    // Process photo (same code as before)
}
```

---

## 建议更改 (P2)

建议进行这些更改，但并不立即要求。考虑在下一个重构周期中进行迁移。

### 应用程序.主页

**状态：** ⚠️ **已弃用** - 属性将在未来版本中删除。

**警告您会看到：**
```
warning CS0618: 'Application.MainPage' is obsolete: 'This property is deprecated. Initialize your application by overriding Application.CreateWindow...'
```

#### 迁移示例

```csharp
// ❌ OLD (Deprecated)
public partial class App : Application
{
    public App()
    {
        InitializeComponent();
        MainPage = new AppShell();
    }
    
    // Changing page later
    public void SwitchToLoginPage()
    {
        MainPage = new LoginPage();
    }
}

// ✅ NEW (Recommended)
public partial class App : Application
{
    public App()
    {
        InitializeComponent();
    }
    
    protected override Window CreateWindow(IActivationState? activationState)
    {
        return new Window(new AppShell());
    }
    
    // Changing page later
    public void SwitchToLoginPage()
    {
        if (Windows.Count > 0)
        {
            Windows[0].Page = new LoginPage();
        }
    }
}
```

**CreateWindow的好处：**
- 更好的多窗口支持
- 更明确的初始化
- 更清晰的关注点分离
- 与壳牌配合使用效果更好

---

## 批量迁移工具

使用这些查找/替换模式快速更新您的代码库。

### Visual Studio / VS 代码

**正则表达式模式 - 查找/替换**

#### 动画方法

```regex
Find:    \.FadeTo\(
Replace: .FadeToAsync(

Find:    \.ScaleTo\(
Replace: .ScaleToAsync(

Find:    \.TranslateTo\(
Replace: .TranslateToAsync(

Find:    \.RotateTo\(
Replace: .RotateToAsync(

Find:    \.RotateXTo\(
Replace: .RotateXToAsync(

Find:    \.RotateYTo\(
Replace: .RotateYToAsync(

Find:    \.ScaleXTo\(
Replace: .ScaleXToAsync(

Find:    \.ScaleYTo\(
Replace: .ScaleYToAsync(

Find:    \.RelRotateTo\(
Replace: .RelRotateToAsync(

Find:    \.RelScaleTo\(
Replace: .RelScaleToAsync(
```

#### 显示方式

```regex
Find:    DisplayAlert\(
Replace: DisplayAlertAsync(

Find:    DisplayActionSheet\(
Replace: DisplayActionSheetAsync(
```

#### 媒体选择器方法

**⚠️注意：** MediaPicker 迁移需要由于返回类型更改（`FileResult?` → `List<FileResult>`）而手动更改代码。使用这些搜索来查找实例：

```bash
# Find PickPhotoAsync usages
grep -rn "PickPhotoAsync" --include="*.cs" .

# Find PickVideoAsync usages
grep -rn "PickVideoAsync" --include="*.cs" .
```

**手动迁移模式：**
```csharp
// Find: await MediaPicker.PickPhotoAsync(
// Replace with:
var photos = await MediaPicker.PickPhotosAsync(new MediaPickerOptions { SelectionLimit = 1 });
var photo = photos.FirstOrDefault();

// Find: await MediaPicker.PickVideoAsync(
// Replace with:
var videos = await MediaPicker.PickVideosAsync(new MediaPickerOptions { SelectionLimit = 1 });
var video = videos.FirstOrDefault();
```

#### ListView/TableView检测（需要手动迁移）

**⚠️ 注意：** ListView/TableView 迁移无法自动化。使用这些搜索来查找实例：

```bash
# Find all ListView usages in XAML
grep -r "<ListView" --include="*.xaml" .

# Find all TableView usages in XAML
grep -r "<TableView" --include="*.xaml" .

# Find ListView in C# code
grep -r "new ListView\|ListView " --include="*.cs" .

# Find Cell types in XAML
grep -r "TextCell\|ImageCell\|EntryCell\|SwitchCell\|ViewCell" --include="*.xaml" .

# Find ItemSelected handlers (need to change to SelectionChanged)
grep -r "ItemSelected=" --include="*.xaml" .
grep -r "ItemSelected\s*\+=" --include="*.cs" .

# Find ContextActions (need to change to SwipeView)
grep -r "ContextActions" --include="*.xaml" .

# Find platform-specific ListView code (needs removal)
grep -r "PlatformConfiguration.*ListView" --include="*.cs" .
```

**创建迁移清单：**
```bash
# Generate a report of all ListView/TableView instances
echo "=== ListView/TableView Migration Inventory ===" > migration-report.txt
echo "" >> migration-report.txt
echo "XAML ListView instances:" >> migration-report.txt
grep -rn "<ListView" --include="*.xaml" . >> migration-report.txt
echo "" >> migration-report.txt
echo "XAML TableView instances:" >> migration-report.txt
grep -rn "<TableView" --include="*.xaml" . >> migration-report.txt
echo "" >> migration-report.txt
echo "ItemSelected handlers:" >> migration-report.txt
grep -rn "ItemSelected" --include="*.xaml" --include="*.cs" . >> migration-report.txt
echo "" >> migration-report.txt
cat migration-report.txt
```

### PowerShell脚本

```powershell
# Replace animation methods in all .cs files
Get-ChildItem -Path . -Recurse -Filter *.cs | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    
    # Animation methods
    $content = $content -replace '\.FadeTo\(', '.FadeToAsync('
    $content = $content -replace '\.ScaleTo\(', '.ScaleToAsync('
    $content = $content -replace '\.TranslateTo\(', '.TranslateToAsync('
    $content = $content -replace '\.RotateTo\(', '.RotateToAsync('
    $content = $content -replace '\.RotateXTo\(', '.RotateXToAsync('
    $content = $content -replace '\.RotateYTo\(', '.RotateYToAsync('
    $content = $content -replace '\.ScaleXTo\(', '.ScaleXToAsync('
    $content = $content -replace '\.ScaleYTo\(', '.ScaleYToAsync('
    $content = $content -replace '\.RelRotateTo\(', '.RelRotateToAsync('
    $content = $content -replace '\.RelScaleTo\(', '.RelScaleToAsync('
    
    # Display methods
    $content = $content -replace 'DisplayAlert\(', 'DisplayAlertAsync('
    $content = $content -replace 'DisplayActionSheet\(', 'DisplayActionSheetAsync('
    
    Set-Content $_.FullName $content
}

Write-Host "✅ Migration complete!"
```

---

## 测试您的升级

### 构建验证

```bash
# Clean solution
dotnet clean

# Restore packages
dotnet restore

# Build for each platform
dotnet build -f net10.0-android -c Release
dotnet build -f net10.0-ios -c Release
dotnet build -f net10.0-maccatalyst -c Release
dotnet build -f net10.0-windows -c Release

# Check for warnings
dotnet build --no-incremental 2>&1 | grep -i "warning CS0618"
```

### 启用警告作为错误（临时）

```xml
<!-- Add to your .csproj to catch all obsolete API usage -->
<PropertyGroup>
  <WarningsAsErrors>CS0618</WarningsAsErrors>
</PropertyGroup>
```

### 测试清单

- [ ] 应用程序在所有平台上成功启动
- [ ] 所有动画均正常工作
- [ ] 对话框（警报/操作表）正确显示
- [ ] 加载指示器工作（如果您使用 IsBusy）
- [ ] 组件间通信工作（MessagingCenter 替代）
- [ ] 构建输出中没有 CS0618 警告
- [ ] 没有与过时 API 相关的运行时异常

---

## 故障排除

### 错误：“MessagingCenter”由于其保护级别而无法访问

**原因：** MessagingCenter 现在位于 .NET 10 内部。

**解决方案：**
1. 安装 `CommunityToolkit.Mvvm` 包
2. 替换为 `WeakReferenceMessenger` （请参阅 [MessagingCenter 部分](#messagingcenter-made-internal)）
3. 为每种消息类型创建消息类
4. 不要忘记注销！

---

### 警告：动画方法已过时

**原因：** 使用同步动画方法（`FadeTo`、`ScaleTo` 等）

**快速修复：**
```bash
# Use PowerShell script from Bulk Migration Tools section
# Or use Find/Replace patterns
```

**手动修复：**
将 `Async` 添加到每个动画方法调用的末尾：
- __代码0__ → __代码1__
- __代码0__ → __代码1__
- 等等

---

### Page.IsBusy 不再工作

**原因：** IsBusy 仍然有效，但已被弃用。

**解决方案：** 替换为显式 ActivityIndicator（请参阅 [IsBusy 部分](#3-pageisbusy)）

---

### 构建失败并显示“未找到目标框架 'net10.0'”

**原因：** .NET 10 SDK 未安装或不是最新版本。

**解决方案：**
```bash
# Check SDK version
dotnet --version  # Should be 10.0.100 or later

# Install .NET 10 SDK from:
# https://dotnet.microsoft.com/download/dotnet/10.0

# Update workloads
dotnet workload update
```

---

### MessagingCenter 迁移破坏了现有代码

**常见问题：**

1. **忘记注销：**
   ```csharp
   // ⚠️ Memory leak if you don't unregister
   protected override void OnDisappearing()
   {
       base.OnDisappearing();
       WeakReferenceMessenger.Default.UnregisterAll(this);
   }
   ```

2. **错误的消息类型：**
   ```csharp
   // ❌ Wrong
   WeakReferenceMessenger.Default.Register<UserLoggedIn>(this, handler);
   WeakReferenceMessenger.Default.Send(new UserData());  // Wrong type!
   
   // ✅ Correct
   WeakReferenceMessenger.Default.Register<UserLoggedInMessage>(this, handler);
   WeakReferenceMessenger.Default.Send(new UserLoggedInMessage(userData));
   ```

3. **接收者参数混淆：**
   ```csharp
   // The recipient parameter is the object that registered (this)
   WeakReferenceMessenger.Default.Register<MyMessage>(this, (recipient, message) =>
   {
       // recipient == this
       // message == the message that was sent
   });
   ```

---

### 警告：MediaPicker 方法已过时

**原因：** 使用已弃用的 `PickPhotoAsync` 或 `PickVideoAsync` 方法。

**解决方案：** 迁移到 `PickPhotosAsync` 或 `PickVideosAsync`：

```csharp
// ❌ OLD
var photo = await MediaPicker.PickPhotoAsync(options);

// ✅ NEW (maintain single-selection)
var photos = await MediaPicker.PickPhotosAsync(new MediaPickerOptions 
{ 
    Title = options?.Title,
    SelectionLimit = 1 
});
var photo = photos.FirstOrDefault();
```

**主要变化：**
- 返回类型从 `FileResult?` 更改为 `List<FileResult>`
- 使用 `.FirstOrDefault()` 获取单个结果
- 设置 `SelectionLimit = 1` 以保持旧行为
- 检查 `photos.Count == 0` 而不是 `photo == null`

---

### MediaPicker 返回的项目数多于 SelectionLimit

**原因：** Windows 和某些 Android 自定义选择器不强制执行 `SelectionLimit`。

**解决方案：** 添加手动验证：

```csharp
var photos = await MediaPicker.PickPhotosAsync(new MediaPickerOptions
{
    SelectionLimit = 5
});

if (photos.Count > 5)
{
    await DisplayAlertAsync("Error", "Too many photos selected", "OK");
    return;
}
```

---

### 迁移后动画未完成

**原因：** 忘记 `await` 关键字。

```csharp
// ❌ Wrong - animation runs but code continues immediately
view.FadeToAsync(0, 500);
DoSomethingElse();

// ✅ Correct - wait for animation to complete
await view.FadeToAsync(0, 500);
DoSomethingElse();
```

---

### 警告：ListView/TableView/TextCell 已过时

**原因：** 使用已弃用的 ListView、TableView 或 Cell 类型。

**解决方案：** 迁移到CollectionView（参见[ListView和TableView部分](#listview-and-tableview-deprecated)）

**快速决策指南：**
- **简单列表** → 带有自定义 DataTemplate 的 CollectionView
- **包含 <20 项的设置页面** → VerticalStackLayout 和 BindableLayout
- **设置页面包含 20 多个项目** → 分组 CollectionView
- **分组数据列表** → CollectionView 带有 `IsGrouped="True"`

---

### CollectionView 没有 SelectedItem 事件

**原因：** CollectionView 使用 `SelectionChanged` 而不是 `ItemSelected`。

**解决方案：**
```csharp
// ❌ OLD (ListView)
void OnItemSelected(object sender, SelectedItemChangedEventArgs e)
{
    var item = e.SelectedItem as MyItem;
}

// ✅ NEW (CollectionView)
void OnSelectionChanged(object sender, SelectionChangedEventArgs e)
{
    var item = e.CurrentSelection.FirstOrDefault() as MyItem;
}
```

---

### 特定于平台的 ListView 配置已过时

**原因：** 使用 `Microsoft.Maui.Controls.PlatformConfiguration.*Specific.ListView` 扩展。

**Error:**
```
warning CS0618: 'ListView' is obsolete: 'With the deprecation of ListView, this class is obsolete. Please use CollectionView instead.'
```

**解决方案：**
1. 使用语句删除特定于平台的 ListView：
   ```csharp
   // ❌ Remove these
   using Microsoft.Maui.Controls.PlatformConfiguration;
   using Microsoft.Maui.Controls.PlatformConfiguration.iOSSpecific;
   using Microsoft.Maui.Controls.PlatformConfiguration.AndroidSpecific;
   ```

2. 删除特定于平台的 ListView 调用：
   ```csharp
   // ❌ Remove these
   myListView.On<iOS>().SetSeparatorStyle(SeparatorStyle.FullWidth);
   myListView.On<Android>().IsFastScrollEnabled();
   viewCell.On<iOS>().SetDefaultBackgroundColor(Colors.White);
   ```

3. CollectionView 有不同的平台自定义选项 - 请参阅 CollectionView 文档以获取替代方案。

---

### ListView 迁移后 CollectionView 性能问题

**Common Causes:**

1. **不使用 DataTemplate 缓存：**
   ```xaml
   <!-- ❌ Bad performance -->
   <CollectionView.ItemTemplate>
       <DataTemplate>
           <ComplexView />
       </DataTemplate>
   </CollectionView.ItemTemplate>
   
   <!-- ✅ Better - use simpler templates -->
   <CollectionView.ItemTemplate>
       <DataTemplate>
           <VerticalStackLayout Padding="10">
               <Label Text="{Binding Title}" />
           </VerticalStackLayout>
       </DataTemplate>
   </CollectionView.ItemTemplate>
   ```

2. **复杂的嵌套布局：**
   - 避免在 ItemTemplate 中深度嵌套布局
   - 尽可能使用 Grid 而不是 StackLayout
   - 考虑使用 FlexLayout 进行复杂布局

3. **图像未缓存：**
   ```xaml
   <Image Source="{Binding ImageUrl}"
          Aspect="AspectFill"
          HeightRequest="80"
          WidthRequest="80">
       <Image.Behaviors>
           <!-- Add caching behavior if needed -->
       </Image.Behaviors>
   </Image>
   ```

---

## Quick Reference Card

### Priority Checklist

**必须修复（P0 - 破坏/严重）：**
- [ ] 将 `MessagingCenter` 替换为 `WeakReferenceMessenger`
- [ ] 将 `ListView` 迁移到 `CollectionView`
- [ ] 将 `TableView` 迁移到 `CollectionView` 或 `BindableLayout`
- [ ] 将 `TextCell`、`ImageCell` 等替换为自定义 DataTemplates
- [ ] 将 `ContextActions` 转换为 `SwipeView`
- [ ] 删除特定于平台的 ListView 配置

**应该修复（P1 - 已弃用）：**
- [ ] 更新动画方法：添加 `Async` 后缀
- [ ] 更新 `DisplayAlert` → `DisplayAlertAsync`
- [ ] 更新 `DisplayActionSheet` → `DisplayActionSheetAsync`  
- [ ] 将 `Page.IsBusy` 替换为 `ActivityIndicator`
- [ ] 替换 `PickPhotoAsync` → `PickPhotosAsync` （用 `SelectionLimit = 1`）
- [ ] 替换 `PickVideoAsync` → `PickVideosAsync` （用 `SelectionLimit = 1`）

**Nice to Have (P2):**
- [ ] 将 `Application.MainPage` 迁移到 `CreateWindow`

### 常见模式

```csharp
// Animation
await view.FadeToAsync(0, 500);

// Alert
await DisplayAlertAsync("Title", "Message", "OK");

// Messaging
WeakReferenceMessenger.Default.Send(new MyMessage());
WeakReferenceMessenger.Default.Register<MyMessage>(this, (r, m) => { });
WeakReferenceMessenger.Default.UnregisterAll(this);

// Loading
IsLoading = true;
try { await LoadAsync(); }
finally { IsLoading = false; }
```

---

## 其他资源

- **官方文档：** https://learn.microsoft.com/dotnet/maui/
- **迁移指南：** https://learn.microsoft.com/dotnet/maui/migration/
- **GitHub 问题：** https://github.com/dotnet/maui/issues
- **CommunityToolkit.Mvvm：** https://learn.microsoft.com/dotnet/communitytoolkit/mvvm/

---

**文档版本：** 2.0  
**最后更新时间：** 2025 年 11 月  
**适用于：** .NET MAUI 10.0.100 及更高版本
