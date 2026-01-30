---
description: '使用.NET Framework项目的指导。包括项目结构、C#语言版本、NuGet管理和最佳实践。'
applyTo: '**/*.csproj, **/*.cs'
---

# .NET Framework 开发

## 构建和编译要求
- 始终使用`msbuild /t:rebuild`来构建解决方案或项目，而不是`dotnet build`

## 项目文件管理

### 非SDK样式项目结构
.NET Framework项目使用传统项目格式，与现代SDK样式项目有很大不同：

- **显式文件包含**：所有新的源文件**必须**使用`<Compile>`元素显式添加到项目文件（`.csproj`）中
  - .NET Framework项目不会像SDK样式项目那样自动包含目录中的文件
  - 示例：`<Compile Include="Path\To\NewFile.cs" />`

- **无隐式导入**：与SDK样式项目不同，.NET Framework项目不会自动导入通用命名空间或程序集
 
- **构建配置**：包含Debug/Release配置的显式`<PropertyGroup>`部分

- **输出路径**：显式`<OutputPath>`和`<IntermediateOutputPath>`定义

- **目标框架**：使用`<TargetFrameworkVersion>`而不是`<TargetFramework>`
  - 示例：`<TargetFrameworkVersion>v4.7.2</TargetFrameworkVersion>`

## NuGet包管理
- 在.NET Framework项目中安装和更新NuGet包是一项复杂的任务，需要协调更改多个文件。因此，**不要尝试在此项目中安装或更新NuGet包**
- 相反，如果需要更改NuGet引用，要求用户使用Visual Studio NuGet包管理器或Visual Studio包管理器控制台安装或更新NuGet包
- 推荐NuGet包时，确保它们与.NET Framework或.NET Standard 2.0兼容（而不仅仅是.NET Core或.NET 5+）

## C#语言版本为7.3
- 此项目仅限于C# 7.3功能。请避免使用：

### C# 8.0+功能（不支持）：
  - using声明（`using var stream = ...`）
  - await using语句（`await using var resource = ...`）
  - Switch表达式（`variable switch { ... }`）
  - 空值合并赋值（`??=`）
  - 范围和索引运算符（`array[1..^1]`、`array[^1]`）
  - 默认接口方法
  - 结构中的只读成员
  - 静态本地函数
  - 可空引用类型（`string?`、`#nullable enable`）

### C# 9.0+功能（不支持）：
  - 记录（`public record Person(string Name)`）
  - 仅初始化属性（`{ get; init; }`）
  - 顶级程序（没有Main方法的程序）
  - 模式匹配增强
  - 目标类型new表达式（`List<string> list = new()`）

### C# 10+功能（不支持）：
  - 全局using语句
  - 文件范围命名空间
  - 记录结构
  - 必需成员

### 替代使用（C# 7.3兼容）：
  - 使用大括号的传统using语句
  - 使用switch语句而不是switch表达式
  - 使用显式空值检查而不是空值合并赋值
  - 使用手动索引的数组切片
  - 使用抽象类或接口而不是默认接口方法

## 环境考虑（Windows环境）
- 使用带有反斜杠的Windows样式路径（例如，`C:\path\to\file.cs`）
- 建议终端操作时使用Windows适当的命令
- 处理文件系统操作时考虑Windows特定行为

## 常见.NET Framework陷阱和最佳实践

### 异步/等待模式
- **ConfigureAwait(false)**：在库代码中始终使用`ConfigureAwait(false)`以避免死锁：
  ```csharp
  var result = await SomeAsyncMethod().ConfigureAwait(false);
  ```
- **避免同步覆盖异步**：不要使用`.Result`、`.Wait()`或`.GetAwaiter().GetResult()`。这些同步覆盖异步模式可能导致死锁和性能不佳。始终对异步调用使用`await`。

### DateTime处理
- **对时间戳使用DateTimeOffset**：对于绝对时间点，优先使用`DateTimeOffset`而不是`DateTime`
- **指定DateTimeKind**：使用`DateTime`时，始终指定`DateTimeKind.Utc`或`DateTimeKind.Local`
- **文化感知格式**：对序列化/解析使用`CultureInfo.InvariantCulture`

### 字符串操作
- **StringBuilder用于连接**：对多个字符串连接使用`StringBuilder`
- **StringComparison**：为字符串操作始终指定`StringComparison`：
  ```csharp
  string.Equals(other, StringComparison.OrdinalIgnoreCase)
  ```

### 内存管理
- **Dispose模式**：为非托管资源正确实现`IDisposable`
- **Using语句**：始终将`IDisposable`对象包装在using语句中
- **避免大对象堆**：保持对象在85KB以下以避免LOH分配

### 配置
- **使用ConfigurationManager**：通过`ConfigurationManager.AppSettings`访问应用程序设置
- **连接字符串**：存储在`<connectionStrings>`部分，而不是`<appSettings>`
- **转换**：对特定于环境的设置使用web.config/app.config转换

### 异常处理
- **特定异常**：捕获特定异常类型，而不是通用`Exception`
- **不要吞并异常**：始终适当地记录或重新抛出异常
- **对可释放资源使用using**：确保即使在发生异常时也能正确清理

### 性能考虑
- **避免装箱**：注意值类型和泛型的装箱/拆箱
- **字符串驻留**：对频繁使用的字符串明智地使用`string.Intern()`
- **延迟初始化**：对昂贵的对象创建使用`Lazy<T>`
- **避免在热路径中使用反射**：尽可能缓存`MethodInfo`、`PropertyInfo`对象
