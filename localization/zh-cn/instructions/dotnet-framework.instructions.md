---
description: "适用于 .NET Framework 项目的指导。涵盖项目结构、C# 语言版本、NuGet 管理和最佳实践。"
applyTo: "**/*.csproj, **/*.cs"
---

# .NET Framework 开发规范

## 构建与编译要求

- 始终使用 `msbuild /t:rebuild` 构建解决方案或项目，不要使用 `dotnet build`

## 项目文件管理

### 非 SDK 风格项目结构

.NET Framework 项目采用传统项目格式，与现代 SDK 风格项目有显著区别：

- **显式文件包含**：所有新源文件**必须**通过 `<Compile>` 元素显式添加到 `.csproj` 项目文件中

  - .NET Framework 项目不会像 SDK 风格项目那样自动包含目录下的文件
  - 示例：`<Compile Include="Path\To\NewFile.cs" />`

- **无隐式导入**：与 SDK 风格项目不同，.NET Framework 项目不会自动导入常用命名空间或程序集

- **构建配置**：需显式包含 Debug/Release 的 `<PropertyGroup>` 配置段

- **输出路径**：需显式定义 `<OutputPath>` 和 `<IntermediateOutputPath>`

- **目标框架**：使用 `<TargetFrameworkVersion>` 而非 `<TargetFramework>`
  - 示例：`<TargetFrameworkVersion>v4.7.2</TargetFrameworkVersion>`

## NuGet 包管理

- .NET Framework 项目中的 NuGet 包安装和更新较为复杂，涉及多个文件的协调修改。因此，**请勿直接在本项目中尝试安装或更新 NuGet 包**。
- 如需变更 NuGet 引用，请用户通过 Visual Studio 的 NuGet 包管理器或包管理器控制台操作。
- 推荐 NuGet 包时，需确保其兼容 .NET Framework 或 .NET Standard 2.0（不能仅支持 .NET Core 或 .NET 5+）。

## C# 语言版本为 7.3

- 本项目仅支持 C# 7.3 及以下特性。请避免使用：

### 不支持的 C# 8.0+ 特性：

- Using 声明（`using var stream = ...`）
- Await using 语句（`await using var resource = ...`）
- Switch 表达式（`variable switch { ... }`）
- Null 合并赋值（`??=`）
- 范围与索引操作符（`array[1..^1]`, `array[^1]`）
- 接口默认实现
- 结构体只读成员
- 静态本地函数
- 可空引用类型（`string?`, `#nullable enable`）

### 不支持的 C# 9.0+ 特性：

- 记录类型（`public record Person(string Name)`）
- Init-only 属性（`{ get; init; }`）
- 顶级程序（无 Main 方法的程序）
- 模式匹配增强
- 目标类型 new 表达式（`List<string> list = new()`）

### 不支持的 C# 10+ 特性：

- 全局 using
- 文件作用域命名空间
- 记录结构体
- Required 成员

### 推荐用法（C# 7.3 兼容）：

- 传统 using 语句（带大括号）
- 使用 switch 语句替代 switch 表达式
- 显式 null 检查替代 null 合并赋值
- 手动索引实现数组切片
- 用抽象类或接口替代接口默认实现

## 环境注意事项（Windows 环境）

- 路径使用 Windows 风格反斜杠（如 `C:\path\to\file.cs`）
- 建议命令行操作时使用 Windows 适用命令
- 文件系统操作需考虑 Windows 特性

## 常见 .NET Framework 问题与最佳实践

### 异步/等待模式

- **ConfigureAwait(false)**：在库代码中始终使用 `ConfigureAwait(false)` 以避免死锁：
  ```csharp
  var result = await SomeAsyncMethod().ConfigureAwait(false);
  ```
- **避免同步等待异步**：不要使用 `.Result`、`.Wait()` 或 `.GetAwaiter().GetResult()`，这些同步等待异步的写法易导致死锁和性能问题。始终使用 `await`。

### DateTime 处理

- **时间戳优先用 DateTimeOffset**：绝对时间点建议用 `DateTimeOffset` 替代 `DateTime`
- **指定 DateTimeKind**：如用 `DateTime`，务必指定 `DateTimeKind.Utc` 或 `DateTimeKind.Local`
- **文化无关格式化**：序列化/解析时用 `CultureInfo.InvariantCulture`

### 字符串操作

- **多次拼接用 StringBuilder**
- **字符串比较需指定 StringComparison**：
  ```csharp
  string.Equals(other, StringComparison.OrdinalIgnoreCase)
  ```

### 内存管理

- **实现 IDisposable 模式**：管理非托管资源时需正确实现 `IDisposable`
- **用 using 包裹 IDisposable 对象**
- **避免大对象堆分配**：对象尽量小于 85KB，避免进入 LOH

### 配置管理

- **用 ConfigurationManager 访问配置**：通过 `ConfigurationManager.AppSettings` 获取应用设置
- **连接字符串**：存于 `<connectionStrings>` 节点，不要放在 `<appSettings>`
- **环境配置变更**：用 web.config/app.config 转换实现多环境配置

### 异常处理

- **捕获具体异常类型**，避免直接 catch `Exception`
- **异常需记录或适当重新抛出**，不可无声吞掉
- **用 using 保证资源释放**，即使发生异常也能清理

### 性能建议

- **避免装箱**：注意值类型与泛型的装箱/拆箱
- **字符串驻留**：频繁字符串可用 `string.Intern()`
- **惰性初始化**：用 `Lazy<T>` 延迟创建开销大的对象
- **避免热路径反射**：如需反射，缓存 `MethodInfo`、`PropertyInfo`

---

> 本文档为自动翻译，仅供参考。如有歧义请以英文原文为准。
