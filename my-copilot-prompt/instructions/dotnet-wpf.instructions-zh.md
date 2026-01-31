---
描述：“.NET WPF 组件和应用程序模式”
applyTo: '**/*.xaml, **/*.cs'
---

## 总结

这些说明指导 GitHub Copilot 协助使用 MVVM 模式构建高质量、可维护且高性能的 WPF 应用程序。它包括 XAML、数据绑定、UI 响应能力和 .NET 性能的最佳实践。

## 理想的项目类型

- 使用 C# 和 WPF 的桌面应用程序
- 遵循 MVVM（模型-视图-视图模型）设计模式的应用程序
- 使用 .NET 8.0 或更高版本的项目
- 使用 XAML 构建的 UI 组件
- 强调性能和响应能力的解决方案

## 目标

- 为 `INotifyPropertyChanged` 和 `RelayCommand` 生成样板
- 建议将 ViewModel 和 View 逻辑完全分离
- 鼓励使用 `ObservableCollection<T>`、`ICommand` 和正确的绑定
- 推荐性能技巧（例如虚拟化、异步加载）
- 避免紧密耦合代码隐藏逻辑
- 生成可测试的 ViewModel

## 提示行为示例

### ✅ 好的建议
- “为登录屏幕生成一个 ViewModel，其中包含用户名和密码属性以及 LoginCommand”
- “为使用 UI 虚拟化并绑定到 ObservableCollection 的 ListView 编写 XAML 代码段”
- “将此代码隐藏的点击处理程序重构为 ViewModel 中的 RelayCommand”
- “在 WPF 中异步获取数据时添加加载微调器”

### ❌避免
- 在代码隐藏中建议业务逻辑
- 在没有上下文的情况下使用静态事件处理程序
- 生成紧密耦合的 XAML，无需绑定
- 建议 WinForms 或 UWP 方法

## 首选技术
- C# 与 .NET 8.0+
- 具有 MVVM 结构的 XAML
- `CommunityToolkit.Mvvm` 或自定义 `RelayCommand` 实现
- 异步/等待非阻塞 UI
- __代码0__、__代码1__、__代码2__

## 要遵循的常见模式
- ViewModel 优先绑定
- 使用 .NET 或第三方容器（例如 Autofac、SimpleInjector）进行依赖注入
- XAML 命名约定（控件采用 PascalCase，绑定采用 CamelCase）
- 避免绑定中的魔术字符串（使用 `nameof`）

## 副驾驶可以使用的示例说明片段

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
        // Add login logic here
    }
}
```

```xml
<StackPanel>
    <TextBox Text="{Binding UserName, UpdateSourceTrigger=PropertyChanged}" />
    <PasswordBox x:Name="PasswordBox" />
    <Button Content="Login" Command="{Binding LoginCommand}" />
</StackPanel>
```
