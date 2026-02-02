---
name: nuget-manager
description: 'Manage NuGet packages in .NET projects/solutions. Use this skill when adding, removing, or updating NuGet package versions. It enforces using `dotnet` CLI for package management and provides strict procedures for direct file edits only when updating versions.'
---

# NuGet 管理器

## 概述

此技能可确保跨 .NET 项目对 NuGet 包进行一致且安全的管理。它优先使用 `dotnet` CLI 来维护项目完整性，并对版本更新强制执行严格的验证和恢复工作流程。

## 先决条件

- 已安装 .NET SDK（通常为 .NET 8.0 SDK 或更高版本，或者与目标解决方案兼容的版本）。
- `dotnet` CLI 在您的 `PATH` 上可用。
- `jq`（JSON 处理器）或 PowerShell（使用 `dotnet package search` 进行版本验证）。

## 核心规则

1.  **切勿**直接编辑 `.csproj`、`.props` 或 `Directory.Packages.props` 文件来**添加**或**删除**包。始终使用 `dotnet add package` 和 `dotnet remove package` 命令。
2.  **直接编辑**仅允许用于**更改现有软件包的版本**。
3.  **版本更新**必须遵循强制工作流程：
    - 验证 NuGet 上是否存在目标版本。
    - 确定版本是按项目管理 (`.csproj`) 还是集中管理 (`Directory.Packages.props`)。
    - 更新相应文件中的版本字符串。
    - 立即运行 `dotnet restore` 来验证兼容性。

## 工作流程

### 添加包
使用 `dotnet add [<PROJECT>] package <PACKAGE_NAME> [--version <VERSION>]`。
示例：`dotnet add src/MyProject/MyProject.csproj package Newtonsoft.Json`

### 删除包
使用 `dotnet remove [<PROJECT>] package <PACKAGE_NAME>`。
示例：`dotnet remove src/MyProject/MyProject.csproj package Newtonsoft.Json`

### 更新包版本
更新版本时，请按以下步骤操作：

1.  **验证版本是否存在**：
    使用精确匹配和 JSON 格式的 `dotnet package search` 命令检查版本是否存在。 
    使用 `jq`：
    __代码0__
    使用 PowerShell：
    __代码0__
    
2.  **确定版本管理**：
    - 在解决方案根目录中搜索 `Directory.Packages.props`。如果存在，版本应通过 `<PackageVersion Include="Package.Name" Version="1.2.3" />` 进行管理。
    - 如果不存在，请检查各个 `.csproj` 文件中的 `<PackageReference Include="Package.Name" Version="1.2.3" />`。

3.  **应用更改**：
    使用新版本字符串修改已识别的文件。

4.  **验证稳定性**：
    在项目或解决方案上运行 `dotnet restore`。如果发生错误，请恢复更改并进行调查。

## 示例

### 用户：“将 Serilog 添加到 WebApi 项目”
**操作**：执行`dotnet add src/WebApi/WebApi.csproj package Serilog`。

### 用户：“将整个解决方案中的 Newtonsoft.Json 更新到 13.0.3”
**行动**：
1. 验证 13.0.3 是否存在：`dotnet package search Newtonsoft.Json --exact-match --format json`（并解析输出以确认“13.0.3”存在）。
2. 找到它的定义位置（例如 `Directory.Packages.props`）。
3. 编辑文件以更新版本。
4. 运行`dotnet restore`。
