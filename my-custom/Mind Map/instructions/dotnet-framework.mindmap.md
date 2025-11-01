## .NET Framework 项目开发注意事项

- What: 传统 .NET Framework（非 SDK 风格）项目的构建、项目结构、NuGet 管理与 C# 7.3 限制。
- When: 维护/扩展老项目、添加源文件/依赖、编写异步与配置管理时。
- Why: 规避 SDK 项目的习惯性误用，避免编译/运行时陷阱与死锁问题。
- How: 使用 msbuild 重建；显式在 csproj 中 Include 文件；不在此处自动更新 NuGet；严格遵守 C# 7.3 语法边界。

### 关键要点
- 构建: 使用 `msbuild /t:rebuild`（而非 dotnet build）。
- 项目结构: 需 `<Compile Include="...">` 显式加入源文件；显式 PropertyGroup/OutputPath/TargetFrameworkVersion（如 v4.7.2）。
- NuGet: 不在此流程中安装/升级；需通过 VS 管理器操作；确保包兼容 .NET Framework 或 .NET Standard 2.0。
- C# 版本: 仅 7.3；不支持 using 声明、switch 表达式、??=、^/..、record、init、顶层程序、全局 using、文件作用域 namespace 等。
- 异步: 库代码 `ConfigureAwait(false)`；避免 sync-over-async（.Result/Wait）。
- 时间: 优先 DateTimeOffset；指定 Kind；序列化用 InvariantCulture。
- 字符串: 多次拼接用 StringBuilder；比较指定 StringComparison。
- 内存/释放: 正确实现 IDisposable；using 块；避免 LOH；Lazy<T>。
- 配置: ConfigurationManager；连接串在 <connectionStrings>；使用 config transform。
- 异常: 捕获具体类型；切勿吞异常；释放资源用 using。

### Compact Map
Build→ProjectFile→NuGet→C#7.3→Async→Time→String→Memory→Config→Exceptions

### 示例问题
1) 如何在旧 csproj 中正确添加/移除源码文件？
2) 7.3 下替代 switch 表达式/记录类型的写法？
3) 库代码为何必须 ConfigureAwait(false)？
4) 配置多环境 transform 的推荐结构？
5) 旧项目引入 .NET Standard 包的兼容性检查点？
6) 防止 LOH 与 GC 压力的实践？
7) 同步调用异步 API 的替代方案？
8) app.config 的安全存储与连接串管理？
9) 如何排查 UI 线程死锁（WinForms/WPF）？
10) 生产环境的全局异常与日志策略？

Source: d:\mycode\awesome-copilot\instructions\dotnet-framework.instructions.md | Generated: 2025-10-17T00:00:00Z
