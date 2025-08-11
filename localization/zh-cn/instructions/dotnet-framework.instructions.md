---
description: "适用于 .NET Framework 项目的开发指南，包括项目结构、C# 语言版本、NuGet 管理与最佳实践。"
applyTo: "**/*.csproj, **/*.cs"
---

# .NET Framework 开发

## 构建与编译要求

- 构建解决方案或项目时，始终使用 `msbuild /t:rebuild`，不要用 `dotnet build`

## 项目文件管理

### 非 SDK 风格项目结构

.NET Framework 项目采用传统项目格式，与现代 SDK 风格项目有显著不同：

- **显式文件包含**：所有新源文件**必须**在 `.csproj` 中用 `<Compile>` 明确声明
  - 不会自动包含目录下新文件，需手动添加
  - 示例：`<Compile Include="Path\To\NewFile.cs" />`
- **无隐式导入**：不会自动导入常用命名空间或程序集
- **构建配置**：Debug/Release 配置用显式 `<PropertyGroup>`
- **输出路径**：需显式 `<OutputPath>` 和 `<IntermediateOutputPath>`
- **目标框架**：用 `<TargetFrameworkVersion>`，如 `<TargetFrameworkVersion>v4.7.2</TargetFrameworkVersion>`

## NuGet 包管理

- .NET Framework 项目 NuGet 包管理复杂，涉及多文件协调。**请勿尝试自动安装或更新 NuGet 包**。
- 如需变更 NuGet 引用，请用户用 Visual Studio NuGet 包管理器或包管理控制台操作。
- 推荐包时，确保兼容 .NET Framework 或 .NET Standard 2.0（不能只支持 .NET Core/5+）。

## C# 语言版本为 7.3

- 仅可用 C# 7.3 特性，**禁止**使用 C# 8.0+、9.0+、10+ 新特性：

### C# 8.0+（不支持）

- using 声明（`using var stream = ...`）
- await using
- switch 表达式
- `??=` 空合并赋值
- 范围与索引操作符
- 默认接口方法
- 结构体 readonly 成员
- 静态局部函数
- 可空引用类型

### C# 9.0+（不支持）

- record 类型
- init-only 属性
- 顶级程序
- 模式匹配增强
- 目标类型 new 表达式

### C# 10+（不支持）

- 全局 using
- 文件作用域命名空间
- record struct
- required 成员

### 替代方案（C# 7.3 兼容）

- 用传统 using 块
- 用 switch 语句替代 switch 表达式
- 显式 null 检查
- 手动索引数组切片
- 用抽象类/接口替代默认接口方法

## 环境注意事项（Windows）

- 路径用反斜杠（如 `C:\path\to\file.cs`）
- 终端命令用 Windows 风格
- 文件系统操作需考虑 Windows 特性

## 常见陷阱与最佳实践

### 异步模式

- **ConfigureAwait(false)**：库代码异步调用统一加 `ConfigureAwait(false)`
  ```csharp
  var result = await SomeAsyncMethod().ConfigureAwait(false);
  ```
- **避免 sync-over-async**：不要用 `.Result`、`.Wait()`、`.GetAwaiter().GetResult()`，避免死锁与性能问题，始终用 `await`

### DateTime 处理

- **用 DateTimeOffset 表示时间戳**
- **指定 DateTimeKind**：用 `DateTimeKind.Utc` 或 `DateTimeKind.Local`
- **文化无关格式化**：序列化/解析用 `CultureInfo.InvariantCulture`

### 字符串操作

- **多次拼接用 StringBuilder**
- **字符串操作指定 StringComparison**
  ```csharp
  string.Equals(other, StringComparison.OrdinalIgnoreCase)
  ```

### 内存管理

- **实现 IDisposable 模式管理非托管资源**
- **IDisposable 对象用 using 块包裹**
- **避免大对象堆**：对象小于 85KB

### 配置

- **用 ConfigurationManager 访问 appSettings**
- **连接字符串放在 <connectionStrings>，不要放 <appSettings>**
- **用 web.config/app.config 变换实现多环境配置**

### 异常处理

- **捕获具体异常类型，避免直接 catch Exception**
- **异常需记录或重新抛出，勿吞掉**
- **IDisposable 资源用 using 块，确保异常时也能释放**

### 性能优化

- **避免装箱**：注意值类型与泛型装箱/拆箱
- **字符串驻留**：频繁字符串用 `string.Intern()`
- **惰性初始化**：用 `Lazy<T>` 延迟创建昂贵对象
- **避免热路径反射**：缓存 MethodInfo、PropertyInfo

---

**免责声明**：本文档由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 本地化。如有错误或不当之处，欢迎通过 [issues](../../issues) 反馈。
