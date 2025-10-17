## What/When/Why/How
- What: WPF + MVVM 的实践准则（XAML、绑定、命令、虚拟化、性能与测试）
- When: 构建桌面应用、重构 code-behind 逻辑、优化可测试性与响应性
- Why: 解耦视图/逻辑、提升可维护性、提升列表/大数据量渲染性能
- How: CommunityToolkit.Mvvm 或自定义 RelayCommand、INotifyPropertyChanged、虚拟化与异步

## Key Points
- 模式: MVVM 优先，避免业务写入 code-behind
- 绑定: ObservableCollection<T>/ICommand；使用 nameof 防止魔法字符串
- 命令: RelayCommand 封装交互；异步命令处理长任务
- 性能: ItemsControl/ListView 启用虚拟化；延迟加载；减少 UI 线程阻塞
- XAML: 清晰命名；最小化复杂视觉树；DataTemplate/Style 复用
- 测试: ViewModel 单测为主；依赖注入分离 IO/服务

## Compact Map
MVVM→绑定/命令→虚拟化→异步→样式与模板→测试/DI

## Example Questions (10+)
1) 生成登录页 ViewModel（INPC+RelayCommand）
2) ListView 启用虚拟化与增量加载示例
3) 将 Button Click 事件迁移为 RelayCommand
4) 使用 nameof 重构绑定路径，移除魔法字符串
5) 异步加载数据并在 UI 显示 Loading 状态
6) 设计 DataTemplate 与 Style 复用规范
7) 写一个 ViewModel 的 xUnit 单元测试样例
8) 大列表卡顿如何排查与优化？
9) 绑定错误诊断与输出窗口分析
10) 对话框交互的 MVVM 实现方式

Source: d:\mycode\awesome-copilot\instructions\dotnet-wpf.instructions.md | Generated: 2025-10-17T00:00:00Z
