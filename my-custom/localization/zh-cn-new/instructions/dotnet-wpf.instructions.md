---
description: '.NET WPF组件和应用程序模式'
applyTo: '**/*.xaml, **/*.cs'
---

## 摘要

这些说明指导GitHub Copilot协助使用MVVM模式构建高质量、可维护和高性能的WPF应用程序。包括XAML、数据绑定、UI响应性和.NET性能的最佳实践。

## 理想的项目类型

- 使用C#和WPF的桌面应用程序
- 遵循MVVM（模型-视图-视图模型）设计模式的应用程序
- 使用.NET 8.0或更高版本的项目
- 在XAML中构建的UI组件
- 强调性能和响应性的解决方案

## 目标

- 为`INotifyPropertyChanged`和`RelayCommand`生成样板代码
- 建议ViewModel和View逻辑的清晰分离
- 鼓励使用`ObservableCollection<T>`、`ICommand`和适当的绑定
- 推荐性能提示（例如，虚拟化、异步加载）
- 避免代码隐藏逻辑的紧密耦合
- 生成可测试的ViewModels

## 示例提示行为

### ✅ 好的建议
- "为登录屏幕生成一个ViewModel，包含用户名和密码属性，以及一个LoginCommand"
- "编写一个使用UI虚拟化并绑定到ObservableCollection的ListView的XAML代码片段"
- "将此代码隐藏点击处理器重构为ViewModel中的RelayCommand"
- "在WPF中异步获取数据时添加加载动画"

### ❌ 避免
- 建议在代码隐藏中使用业务逻辑
- 使用没有上下文的静态事件处理器
- 生成没有绑定的紧密耦合XAML
- 建议WinForms或UWP方法

## 推荐的技术
- C#与.NET 8.0+
- 具有MVVM结构的XAML
- `CommunityToolkit.Mvvm`或自定义`RelayCommand`实现
- 用于非阻塞UI的异步/等待
- `ObservableCollection`、`ICommand`、`INotifyPropertyChanged`

## 遵循的常见模式
- ViewModel优先绑定
- 使用.NET或第三方容器（例如，Autofac、SimpleInjector）进行依赖注入
- XAML命名约定（控件使用PascalCase，绑定使用camelCase）
- 避免绑定中的魔术字符串（使用`nameof`）

## Copilot可以使用的示例指令片段

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
```

```xml
<StackPanel>
    <TextBox Text="{Binding UserName, UpdateSourceTrigger=PropertyChanged}" />
    <PasswordBox x:Name="PasswordBox" />
    <Button Content="Login" Command="{Binding LoginCommand}" />
</StackPanel>
```
