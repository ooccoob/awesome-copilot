---
描述：“.NET MAUI 组件和应用程序模式”
applyTo: '**/*.xaml, **/*.cs'
---

# .NET毛伊岛

## .NET MAUI 代码风格和结构

- 编写惯用且高效的 .NET MAUI 和 C# 代码。
- 遵循 .NET 和 .NET MAUI 约定。
- 让 UI（视图）专注于布局和绑定；将逻辑保留在 ViewModel 和服务中。
- 对 I/O 和长时间运行的工作使用 async/await 来保持 UI 响应能力。

## 命名约定

- 组件名称、方法名称和公共成员遵循 PascalCase。
- 对私有字段和局部变量使用驼峰命名法。
- 在接口名称前加上“I”前缀（例如 IUserService）。

## .NET MAUI 和 .NET 特定指南

- 利用 .NET MAUI 的内置功能来实现组件生命周期（例如 OnAppearing、OnDisappearing）。
- 通过 `{Binding}` 和 MVVM 模式有效地使用数据绑定。
- 按照关注点分离构建 .NET MAUI 组件和服务。
- 使用存储库的目标 .NET SDK 和设置支持的语言版本；避免需要预览语言功能，除非项目已为其配置。

## 关键规则（一致性）

- 切勿使用 ListView（已弃用）。使用集合视图。
- 切勿使用 TableView（已弃用）。更喜欢 CollectionView 或 Grid/VerticalStackLayout 等布局。
- 切勿使用 Frame（已弃用）。请改用边框。
- 切勿使用 `*AndExpand` 布局选项（已弃用）。请改用网格和显式调整大小。
- 切勿将 ScrollView 或 CollectionView 放置在 StackLayout/VerticalStackLayout/Horizo​​ntalStackLayout 内（可能会破坏滚动和虚拟化）。使用 Grid 作为父布局。
- 切勿在运行时将图像引用为 `.svg`。使用 PNG/JPG 资源。
- 切勿将 Shell 导航与 NavigationPage/TabbedPage/FlyoutPage 混合使用。
- 切勿使用渲染器。使用处理程序。
- 切勿设置 `BackgroundColor`；使用 `Background` （支持渐变/画笔，是首选的现代 API）。

## 布局和控制选择

- 优先选择 `VerticalStackLayout`/`HorizontalStackLayout` 而不是 `StackLayout Orientation="..."` （性能更高）。
- 对于小型、不可滚动的列表（≤20 项），请使用 `BindableLayout`。对于较大或可滚动的列表，请使用 `CollectionView`。
- 对于复杂布局以及需要细分空间时，首选 `Grid`。
- 对于带有边框/背景的容器，优先选择 `Border` 而不是 `Frame`。

## 外壳导航

- 使用 Shell 作为主要导航主机。
- 使用 `Routing.RegisterRoute(...)` 注册路线并使用 `Shell.Current.GoToAsync(...)` 进行导航。
- 启动时设置一次 `MainPage` ；避免频繁更改。
- 不要在 Shell 内嵌套选项卡。

## 错误处理和验证

- 为 .NET MAUI 页面和 API 调用实施正确的错误处理。
- 使用日志记录应用程序级别的错误；记录并显示可恢复故障的用户友好消息。
- 在表单中使用 FluentValidation 或 DataAnnotations 实现验证。

## MAUI API 和性能优化

- 为了性能和正确性，首选编译绑定。
	- 在 XAML 中，在页面/视图/模板上设置 `x:DataType`。
	- 尽可能首选 C# 中基于表达式的绑定。
	- 考虑在项目设置中启用更严格的 XAML 编译（例如 `MauiStrictXamlCompilation=true`），尤其是在 CI 中。
- 避免深度布局嵌套（尤其是嵌套的 StackLayout）。对于复杂的布局更喜欢网格。
- 保持绑定有意：
	- 当值不变时使用 `OneTime`。
	- 仅将 `TwoWay` 用于可编辑值。
	- 避免绑定静态常量；直接设置它们。
- 使用 `Dispatcher.Dispatch()` 或 `Dispatcher.DispatchAsync()` 从后台工作更新 UI：
	- 当您引用页面、视图或其他 BindableObject 时，首选 `BindableObject.Dispatcher`。
	- 在没有直接 BindableObject 访问的服务或 ViewModel 中工作时，通过 DI 注入 `IDispatcher` 。
	- 仅当没有可用的调度程序时才使用 `MainThread.BeginInvokeOnMainThread(...)` 作为后备。
	- **避免**过时的 `Device.BeginInvokeOnMainThread` 模式。

## 资源和资产

- 将图像放置在 `Resources/Images/` 中，将字体放置在 `Resources/Fonts/` 中，将原始资源放置在 `Resources/Raw/` 中。
- 参考图像为 PNG/JPG（例如 `<Image Source="logo.png" />`），而不是 `.svg`。
- 使用适当大小的图像以避免内存膨胀。

## 状态管理

- 更喜欢 DI 管理的服务来实现共享状态和横切关注点；将 ViewModel 的范围限制为导航/页面生命周期。

## API设计与集成

- 使用 HttpClient 或其他适当的服务与外部 API 或您自己的后端进行通信。
- 使用 try-catch 实现 API 调用的错误处理，并在 UI 中提供正确的用户反馈。

## 存储和秘密

- 使用 `SecureStorage` 作为机密（令牌、刷新令牌），并通过清除/重置和重新身份验证来处理异常（不支持的设备、密钥更改、损坏）。
- 避免在首选项中存储秘密。

## 测试与调试

- 使用 xUnit、NUnit 或 MSTest 测试组件和服务。
- 在测试期间使用 Moq 或 NSubstitute 模拟依赖关系。

## 安全与认证

- 必要时使用 OAuth 或 JWT 令牌进行 API 身份验证，在 MAUI 应用程序中实施身份验证和授权。
- 对所有 Web 通信使用 HTTPS，并确保实施正确的 CORS 策略。

## 常见陷阱

- 频繁更改 `MainPage` 可能会导致导航问题。
- 父母和孩子观点上的手势识别器可能会发生冲突；在需要的地方使用 `InputTransparent = true` 。
- 取消订阅事件导致内存泄漏；始终取消订阅并处置资源。
- 深度嵌套的布局会损害性能；扁平化视觉层次。
- 仅在模拟器上进行测试会错过真实设备的边缘情况；在物理设备上进行测试。
