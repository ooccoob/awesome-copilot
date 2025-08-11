````instructions
---
description: '.NET WPF 组件与应用模式'
applyTo: '**/*.xaml, **/*.cs'
---

## 摘要

本指令指导 GitHub Copilot 协助构建高质量、可维护且高性能的 WPF 应用，采用 MVVM 模式。内容涵盖 XAML、数据绑定、UI 响应性和 .NET 性能最佳实践。

## 理想项目类型

- 使用 C# 和 WPF 的桌面应用
- 遵循 MVVM（模型-视图-视图模型）设计模式的应用
- 使用 .NET 8.0 或更高版本的项目
- 用 XAML 构建的 UI 组件
- 注重性能和响应性的解决方案

## 目标

- 生成 `INotifyPropertyChanged` 和 `RelayCommand` 的样板代码
- 建议清晰分离 ViewModel 与 View 逻辑
- 鼓励使用 `ObservableCollection<T>`、`ICommand` 及正确的数据绑定
- 推荐性能优化建议（如虚拟化、异步加载）
- 避免代码与界面逻辑紧耦合
- 生成可测试的 ViewModel

## 示例提示行为

### ✅ 推荐建议
- “为登录界面生成 ViewModel，包含用户名、密码属性和 LoginCommand”
- “编写 ListView 的 XAML 片段，使用 UI 虚拟化并绑定 ObservableCollection”
- “将 code-behind 的点击处理器重构为 ViewModel 中的 RelayCommand”
- “在 WPF 异步获取数据时添加加载动画”

### ❌ 避免
- 在 code-behind 中编写业务逻辑
- 使用无上下文的静态事件处理器
- 生成无绑定的紧耦合 XAML
- 推荐 WinForms 或 UWP 方案

## 推荐技术
- C#（.NET 8.0+）
- XAML + MVVM 结构
- `CommunityToolkit.Mvvm` 或自定义 `RelayCommand`
- UI 非阻塞建议用 async/await
- `ObservableCollection`、`ICommand`、`INotifyPropertyChanged`

## 常用模式
- ViewModel 优先绑定
- 使用 .NET 或第三方容器（如 Autofac、SimpleInjector）实现依赖注入
- XAML 控件命名用 PascalCase，绑定用 camelCase
- 绑定时避免魔法字符串（用 `nameof`）

## Copilot 可用示例代码片段

```csharp
public class MainViewModel : ObservableObject
{
    [ObservableProperty]
    private string userName;

    [ObservableProperty]
    private string password;

    [RelayCommand]
    private void Login()
    {
        // 在此添加登录逻辑
    }
}
````

```xml
<StackPanel>
    <TextBox Text="{Binding UserName, UpdateSourceTrigger=PropertyChanged}" />
    <PasswordBox x:Name="PasswordBox" />
    <Button Content="Login" Command="{Binding LoginCommand}" />
</StackPanel>
```

---

> 本文件为自动翻译，仅供参考。如有歧义请以英文原文为准。

```

```
