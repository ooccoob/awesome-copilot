---
description: 'Guidance for working with .NET Framework projects. Includes project structure, C# language version, NuGet management, and best practices.'
applyTo: '**/*.csproj, **/*.cs'
---

# .NET框架开发

## 构建和编译要求
- 始终使用 `msbuild /t:rebuild` 来构建解决方案或项目，而不是 `dotnet build`

## 项目文件管理

### 非 SDK 风格的项目结构
.NET Framework 项目使用旧项目格式，这与现代 SDK 样式项目有很大不同：

- **显式文件包含**：所有新源文件**必须**使用 `<Compile>` 元素显式添加到项目文件 (`.csproj`)
  - .NET Framework 项目不会像 SDK 样式项目那样自动在目录中包含文件
  - 示例：`<Compile Include="Path\To\NewFile.cs" />`

- **无隐式导入**：与 SDK 样式项目不同，.NET Framework 项目不会自动导入公共命名空间或程序集
 
- **构建配置**：包含用于调试/发布配置的显式 `<PropertyGroup>` 部分

- **输出路径**：显式 `<OutputPath>` 和 `<IntermediateOutputPath>` 定义

- **目标框架**：使用 `<TargetFrameworkVersion>` 而不是 `<TargetFramework>`
  - 示例：`<TargetFrameworkVersion>v4.7.2</TargetFrameworkVersion>`

## NuGet 包管理
- 在 .NET Framework 项目中安装和更新 NuGet 包是一项复杂的任务，需要对多个文件进行协调更改。因此，**不要尝试在此项目中安装或更新 NuGet 包**。
- 相反，如果需要更改 NuGet 引用，请要求用户使用 Visual Studio NuGet 包管理器或 Visual Studio 包管理器控制台安装或更新 NuGet 包。
- 推荐 NuGet 包时，请确保它们与 .NET Framework 或 .NET Standard 2.0 兼容（不仅是 .NET Core 或 .NET 5+）。

## C# 语言版本为 7.3
- 该项目仅限于 C# 7.3 功能。请避免使用：

### C# 8.0+ 功能（不支持）：
  - 使用声明 (`using var stream = ...`)
  - 等待使用语句 (`await using var resource = ...`)
  - 开关表达式 (`variable switch { ... }`)
  - 空合并赋值 (`??=`)
  - 范围和索引运算符（`array[1..^1]`、`array[^1]`）
  - 默认接口方法
  - 结构体中的只读成员
  - 静态局部函数
  - 可空引用类型（`string?`、`#nullable enable`）

### C# 9.0+ 功能（不支持）：
  - 记录 (`public record Person(string Name)`)
  - 仅初始化属性 (`{ get; init; }`)
  - 顶级程序（没有Main方法的程序）
  - 模式匹配增强功能
  - 目标类型的新表达式 (`List<string> list = new()`)

### C# 10+ 功能（不支持）：
  - 全局使用语句
  - 文件范围的命名空间
  - 记录结构
  - 所需成员

### 使用替代（C# 7.3 兼容）：
  - 带大括号的传统 using 语句
  - switch 语句而不是 switch 表达式
  - 显式空值检查而不是空值合并赋值
  - 使用手动索引进行数组切片
  - 抽象类或接口代替默认接口方法

## 环境注意事项（Windows环境）
- 使用带有反斜杠的 Windows 样式路径（例如 `C:\path\to\file.cs`）
- 建议终端操作时使用适合 Windows 的命令
- 处理文件系统操作时考虑特定于 Windows 的行为

## 常见的 .NET Framework 陷阱和最佳实践

### 异步/等待模式
- **ConfigureAwait(false)**：始终在库代码中使用 `ConfigureAwait(false)` 以避免死锁：
  ```csharp
  var result = await SomeAsyncMethod().ConfigureAwait(false);
  ```
- **避免异步同步**：不要使用 `.Result` 或 `.Wait()` 或 `.GetAwaiter().GetResult()`。这些异步同步模式可能会导致死锁和性能不佳。始终使用 `await` 进行异步调用。

### 日期时间处理
- **使用 DateTimeOffset 作为时间戳**：对于绝对时间点，优先使用 `DateTimeOffset` 而不是 `DateTime`
- **指定 DateTimeKind**：使用 `DateTime` 时，始终指定 `DateTimeKind.Utc` 或 `DateTimeKind.Local`
- **文化感知格式**：使用 `CultureInfo.InvariantCulture` 进行序列化/解析

### 字符串操作
- **用于串联的 StringBuilder**：使用 `StringBuilder` 进行多个字符串串联
- **StringComparison**：始终为字符串操作指定 `StringComparison`：
  ```csharp
  string.Equals(other, StringComparison.OrdinalIgnoreCase)
  ```

### 内存管理
- **处置模式**：为非托管资源正确实现 `IDisposable`
- **Using 语句**：始终将 `IDisposable` 对象包装在 using 语句中
- **避免大型对象堆**：将对象保持在 85KB 以下以避免 LOH 分配

### 配置
- **使用 ConfigurationManager**：通过 `ConfigurationManager.AppSettings` 访问应用程序设置
- **连接字符串**：存储在 `<connectionStrings>` 部分，而不是 `<appSettings>`
- **转换**：使用 web.config/app.config 转换进行特定于环境的设置

### 异常处理
- **特定异常**：捕获特定异常类型，而不是通用的`Exception`
- **不要吞下异常**：始终适当地记录或重新抛出异常
- **用于一次性资源**：即使发生异常也确保正确的清理

### 性能考虑因素
- **避免装箱**：注意值类型和泛型的装箱/拆箱
- **字符串驻留**：对常用字符串明智地使用 `string.Intern()`
- **延迟初始化**：使用 `Lazy<T>` 进行昂贵的对象创建
- **避免热路径中的反射**：尽可能缓存 `MethodInfo`、`PropertyInfo` 对象
