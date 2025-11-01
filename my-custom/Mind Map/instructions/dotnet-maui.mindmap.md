## What/When/Why/How
- What: .NET MAUI 开发规范与结构化建议（XAML/C#、生命周期、绑定、状态、缓存、API、测试与安全）
- When: 新建/重构页面与组件，排查卡顿/阻塞/渲染过多时
- Why: 统一风格、避免 UI 线程阻塞、提高可测试性与性能
- How: MVVM+DI、OnAppearing/OnDisappearing、async/await、IMemoryCache、命名与验证约定

## Key Points
- 命名: PascalCase(类型/公开成员), camelCase(私有/局部), 接口 I 前缀
- 架构: 视图仅展示；复杂逻辑进 ViewModel/服务；关注分层与 SoC
- 生命周期: 在 OnAppearing 触发异步加载与取消；释放在 OnDisappearing
- 绑定: {Binding}+INPC；高频属性用 OnPropertyChanged 精准触发
- 异步: 全链路 async/await；避免同步 I/O 卡住主线程
- 性能: 控制重绘；BatchBegin/BatchCommit 批量更新；减少布局深度
- 缓存: IMemoryCache 轻量缓存；分布式缓存按需
- API: HttpClient/Refit；错误处理与 UI 反馈解耦
- 验证: DataAnnotations/FluentValidation；统一错误展示
- 测试: xUnit/NUnit/MSTest + Mock 框架；VM/服务层优先
- 安全: OAuth/JWT；HTTPS；CORS 与配置安全

## Compact Map
命名→MVVM/DI→生命周期→绑定/INPC→异步/性能→缓存→API/错误→验证→测试→安全

## Example Questions (10+)
1) 生成登录页 MVVM（含 DataAnnotations 验证与命令）
2) OnAppearing 异步加载并支持取消的样例
3) 使用 BatchBegin/BatchCommit 降低重绘的示例
4) 设计可测试的 HttpClient 服务封装与单测
5) CollectionView 如何减少不必要重绘与卡顿？
6) 集成 FluentValidation 并绑定表单错误
7) IMemoryCache 缓存分页数据的策略与失效
8) Refit 接口定义与错误弹窗的解耦
9) 长任务后台执行+进度回传到 UI 的模式
10) 统一 API 异常到 UI 的错误提示中台
11) Shell 导航与返回拦截的最佳实践

Source: d:\mycode\awesome-copilot\instructions\dotnet-maui.instructions.md | Generated: 2025-10-17T00:00:00Z
