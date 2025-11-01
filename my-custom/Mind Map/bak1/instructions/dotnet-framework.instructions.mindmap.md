# Guidance for working with .NET Framework projects. Includes project structure, C# language version, NuGet management, and best practices. - Instructions Mindmap

## 📊 摘要
Guidance for working with .NET Framework projects. Includes project structure, C# language version, NuGet management, and best practices.

本指令提供了关于Guidance for working with .NET Framework projects. Includes project structure, C# language version, NuGet management, and best practices.的核心规范和最佳实践,帮助开发者编写高质量、可维护的代码。

## 🎯 适用范围
- **文件类型**: `**/*.csproj, **/*.cs`
- **技术栈**: C#, .NET
- **场景**: 开发和维护Guidance for working with .NET Framework projects. Includes project structure, C# language version, NuGet management, and best practices.相关项目时使用

## 💡 核心规则与最佳实践

### 主要规范
- Always use `msbuild /t:rebuild` to build the solution or projects instead of `dotnet build`
- Explicit File Inclusion**: All new source files **MUST** be explicitly added to the project file (`.csproj`) using a `<Compile>` element
- No Implicit Imports**: Unlike SDK-style projects, .NET Framework projects do not automatically import common namespaces or assemblies
- Build Configuration**: Contains explicit `<PropertyGroup>` sections for Debug/Release configurations
- Output Paths**: Explicit `<OutputPath>` and `<IntermediateOutputPath>` definitions
- Target Framework**: Uses `<TargetFrameworkVersion>` instead of `<TargetFramework>`
- Instead, if changes to NuGet references are required, ask the user to install or update NuGet packages using the Visual Studio NuGet Package Manager o
- When recommending NuGet packages, ensure they are compatible with .NET Framework or .NET Standard 2.0 (not only .NET Core or .NET 5+).

### 代码质量标准
- 遵循行业标准编码规范
- 保持代码简洁可读
- 添加适当的注释和文档
- 进行充分的测试覆盖

## 📝 关键技术要点

### 项目配置
- 正确设置开发环境
- 配置必要的工具和依赖
- 遵循项目结构规范

### 实现标准
- 使用推荐的设计模式
- 遵循命名规范
- 注意性能和安全考虑

## 🗺️ 思维导图

```mindmap
- Guidance for working with .NET Framework projects. Includes project structure, C# language version, NuGet management, and best practices.
  - 适用范围
    - 文件类型: **/*.csproj, **/*.cs
    - 技术栈: C#, .NET
  - 核心规则
    - Build and Compilation Requirements
    - Project File Management
    - NuGet Package Management
    - C# Language Version is 7.3
    - Environment Considerations (Windows environment)
  - 最佳实践
    - 代码质量
    - 性能优化
    - 安全考虑
```

## 💾 保存说明
- 文件名: dotnet-framework.instructions.mindmap.md
- 位置: Mind Map/instructions/
- 生成时间: 2025-10-13 19:57:55
- 文件类型: Instructions (编程规范/最佳实践)
