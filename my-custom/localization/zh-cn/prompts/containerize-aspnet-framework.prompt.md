---
mode: "agent"
tools: ["codebase", "editFiles", "runCommands"]
description: "为 ASP.NET .NET Framework 项目创建适配工程的 Dockerfile 与 .dockerignore，完成容器化。"
---

# ASP.NET .NET Framework 容器化提示词

将下方“容器化设置”中指定的 ASP.NET（.NET Framework）项目进行容器化，且只聚焦于让应用在 Windows Docker 容器内成功运行所必须的改动。容器化应全面考虑此处列出的各项设置。

注意：这是 .NET Framework 应用，而非 .NET Core。其容器化流程与 .NET Core 存在差异。

## 容器化设置（Containerization Settings）

本节包含将 ASP.NET（.NET Framework）应用容器化所需的具体设置与配置。运行本提示词前，请确保这些设置已按需填写。通常仅需最前面的少量设置，后续设置如不适用可沿用默认值。

未指定的设置将采用默认值，默认值以方括号 [ ] 给出。

### 基本项目信息（Basic Project Information）

1. 待容器化的项目：

   - [ProjectName（提供 .csproj 文件路径）]

2. 使用的 Windows Server SKU：

   - [Windows Server Core（默认）或 Windows Server Full]

3. 使用的 Windows Server 版本：

   - [2022、2019 或 2016（默认 2022）]

4. Docker 镜像构建阶段（build stage）的自定义基础镜像（若填 None 则使用微软标准基础镜像）：

   - [为构建阶段指定的基础镜像（默认 None）]

5. Docker 镜像运行阶段（run stage）的自定义基础镜像（若填 None 则使用微软标准基础镜像）：
   - [为运行阶段指定的基础镜像（默认 None）]

### 容器配置（Container Configuration）

1. 需要在镜像中暴露的端口：

   - 主 HTTP 端口：[例如 80]
   - 额外端口：[列出其他端口，或 “None”]

2. 容器运行的账户：

   - [账户名，或默认使用 "ContainerUser"]

3. 需要在镜像中配置的 IIS 设置：
   - [列出具体 IIS 设置，或 “None”]

### 构建配置（Build configuration）

1. 构建镜像前需要执行的自定义构建步骤：

   - [列出具体步骤，或 “None”]

2. 构建镜像后需要执行的自定义步骤：
   - [列出具体步骤，或 “None”]

### 依赖（Dependencies）

1. 需要在镜像内注册到 GAC 的 .NET 程序集：

   - [程序集名称与版本，或 “None”]

2. 需要复制进镜像并安装的 MSI：

   - [MSI 名称与版本，或 “None”]

3. 需要在镜像内注册的 COM 组件：
   - [COM 组件名称，或 “None”]

### 系统配置（System Configuration）

1. 需要写入镜像的注册表键与值：

   - [注册表路径与值，或 “None”]

2. 需要在镜像中设置的环境变量：

   - [变量名与值，或 “Use defaults”]

3. 需要在镜像中安装的 Windows Server 角色与功能：
   - [角色/功能名称，或 “None”]

### 文件系统（File System）

1. 需要复制到镜像中的文件/目录：

   - [相对项目根路径，或 “None”]
   - 镜像内目标路径：[容器内路径，或 “Not applicable”]

2. 从容器化中排除的文件/目录：
   - [需排除的路径，或 “None”]

### .dockerignore 配置（.dockerignore Configuration）

1. `.dockerignore` 中需要额外包含的匹配规则（默认会包含常用忽略项，这里仅列增量部分）：
   - 附加规则：[列出需要额外忽略的模式，或 “None”]

### 健康探针（Health Check）配置（Health Check Configuration）

1. 健康检查端点：

   - [健康检查 URL 路径，或 “None”]

2. 健康检查间隔与超时：
   - [时间间隔与超时设置，或 “Use defaults”]

### 其他指令（Additional Instructions）

1. 容器化必须遵循的其他要求：

   - [具体要求，或 “None”]

2. 已知问题与须处理事项：
   - [描述任何已知问题，或 “None”]

## 范围（Scope）

- ✅ 修改应用配置，确保使用 Configuration Builders 从环境变量读取 app settings 与连接串
- ✅ 为 ASP.NET 应用创建并配置 Dockerfile
- ✅ 在 Dockerfile 中使用多阶段构建（build/publish → 复制到最终镜像）
- ✅ 配置 Windows 容器平台兼容性（Windows Server Core 或 Full）
- ✅ 正确处理依赖（GAC 程序集、MSI、COM 组件）
- ❌ 不包含基础设施搭建（另行处理）
- ❌ 不做容器化必要之外的代码改动

## 执行流程（Execution Process）

1. 复核上方“容器化设置”，明确容器化需求
2. 创建 `progress.md`，用复选标记跟踪进度
3. 打开项目 `.csproj`，读取 `TargetFrameworkVersion` 判断 .NET Framework 版本
4. 选择合适的 Windows Server 容器镜像，依据：
   - 项目检测到的 .NET Framework 版本
   - 设置中指定的 Windows Server SKU（Core 或 Full）
   - 设置中指定的 Windows Server 版本（2016/2019/2022）
   - Windows Server Core 标签参考：
     https://github.com/microsoft/dotnet-framework-docker/blob/main/README.aspnet.md#full-tag-listing
5. 确认所需 NuGet 包已安装。不要在缺失时自动安装；若缺失，应暂停并提示用户通过 Visual Studio 的 NuGet 管理器或控制台安装。必需包包括：
   - `Microsoft.Configuration.ConfigurationBuilders.Environment`
6. 修改 `web.config`，为 appSettings 与 connectionStrings 启用从环境变量读取的 Configuration Builders：
   - 在 `configSections` 中添加 ConfigBuilders 节
   - 在根节点添加 `configBuilders` 节
   - 为 `appSettings` 与 `connectionStrings` 配置 `EnvironmentConfigBuilder`
   - 示例：
     ```xml
     <configSections>
       <section name="configBuilders" type="System.Configuration.ConfigurationBuildersSection, System.Configuration, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" restartOnExternalChanges="false" requirePermission="false" />
     </configSections>
     <configBuilders>
       <builders>
         <add name="Environment" type="Microsoft.Configuration.ConfigurationBuilders.EnvironmentConfigBuilder, Microsoft.Configuration.ConfigurationBuilders.Environment" />
       </builders>
     </configBuilders>
     <appSettings configBuilders="Environment">
       <!-- existing app settings -->
     </appSettings>
     <connectionStrings configBuilders="Environment">
       <!-- existing connection strings -->
     </connectionStrings>
     ```
7. 在将要放置 Dockerfile 的目录创建 `LogMonitorConfig.json`，其内容需与文末“参考内容”一致，不得改动（除非“容器化设置”明确要求）。
   - 特别注意事件日志的级别不要升到 Information，以免产生日志噪音。
8. 在项目根目录创建 Dockerfile：
   - 使用多阶段：
     - 构建阶段：使用 Windows Server Core 的 `mcr.microsoft.com/dotnet/framework/sdk`（除非设置中指定自定义镜像）
       - 先复制 sln、csproj、packages.config
       - 如有 `NuGet.config`，复制并配置私有源
       - 还原 NuGet 包
       - 再复制其余源码，使用 MSBuild 构建并发布到 `C:\publish`
     - 最终阶段：使用 `mcr.microsoft.com/dotnet/framework/aspnet`（除非设置中指定自定义镜像）
       - 复制 `LogMonitorConfig.json` 到容器目录（如 `C:\LogMonitor`）
       - 从微软仓库下载 LogMonitor.exe：
         https://github.com/microsoft/windows-container-tools/releases/download/v2.1.1/LogMonitor.exe
       - 设置工作目录为 `C:\inetpub\wwwroot`
       - 从构建阶段复制已发布内容（`C:\publish`）
       - 设置入口点使用 LogMonitor + ServiceMonitor 监控 IIS：
         `ENTRYPOINT [ "C:\\LogMonitor\\LogMonitor.exe", "C:\\ServiceMonitor.exe", "w3svc" ]`
   - 同步考虑“容器化设置”中的：
     - Windows Server SKU 与版本
     - 暴露端口
     - 容器运行账户
     - IIS 设置
     - GAC 注册
     - MSI 安装
     - COM 注册
     - 注册表键
     - 环境变量
     - 角色与功能
     - 文件/目录复制
   - 参考文末示例，但需按项目与设置定制。
   - 重要：如未明确要求 Full，应默认使用 Windows Server Core。
9. 在项目根目录创建 `.dockerignore`，至少包含以下条目，并结合“容器化设置”的附加模式：
   - packages/
   - bin/
   - obj/
   - .dockerignore
   - Dockerfile
   - .git/
   - .github/
   - .vs/
   - .vscode/
   - \*\*/node_modules/
   - \*.user
   - \*.suo
   - \*\*/.DS_Store
   - \*\*/Thumbs.db
   - 以及“容器化设置”指定的其他规则
10. 若提供了健康检查端点，在 Dockerfile 中添加 HEALTHCHECK 指令
11. 将 Dockerfile 作为 `<None Include="Dockerfile" />` 加入项目文件
12. 勾选 `progress.md` 任务： [ ] → [✓]
13. 持续执行直至所有任务完成并能成功构建镜像

## 构建与运行校验（Build and Runtime Verification）

完成 Dockerfile 后，执行镜像构建：

```bash
docker build -t aspnet-app:latest .
```

若构建失败，请根据错误信息修正 Dockerfile 或项目配置，并反馈成功/失败。

## 进度跟踪（Progress Tracking）

维护 `progress.md`（示例）：

```markdown
# Containerization Progress

## Environment Detection

- [ ] .NET Framework version detection (version: \_\_\_)
- [ ] Windows Server SKU selection (SKU: \_\_\_)
- [ ] Windows Server version selection (Version: \_\_\_)

## Configuration Changes

- [ ] Web.config modifications for configuration builders
- [ ] NuGet package source configuration (if applicable)
- [ ] Copy LogMonitorConfig.json and adjust if required by settings

## Containerization

- [ ] Dockerfile creation
- [ ] .dockerignore file creation
- [ ] Build stage created with SDK image
- [ ] sln, csproj, packages.config, and (if applicable) NuGet.config copied for package restore
- [ ] Runtime stage created with runtime image
- [ ] Non-root user configuration
- [ ] Dependency handling (GAC, MSI, COM, registry, additional files, etc.)
- [ ] Health check configuration (if applicable)
- [ ] Special requirements implementation

## Verification

- [ ] Review containerization settings and make sure that all requirements are met
- [ ] Docker build success
```

请勿在步骤之间等待确认。持续、系统地完成所有工作，直到 Docker 镜像成功构建为止。

你只有在所有复选框均被勾选后才算完成！包括成功构建镜像与处理构建中出现的问题。

## 参考资料（Reference Materials）

### 示例 Dockerfile（Example Dockerfile）

以下示例基于 Windows Server Core 运行 ASP.NET（.NET Framework）：

```dockerfile
# escape=`
# The escape directive changes the escape character from \ to `
# This is especially useful in Windows Dockerfiles where \ is the path separator

# ============================================================
# Stage 1: Build and publish the application
# ============================================================

FROM mcr.microsoft.com/dotnet/framework/sdk:4.8-windowsservercore-ltsc2022 AS build
ARG BUILD_CONFIGURATION=Release

SHELL ["powershell", "-command"]

WORKDIR /app

# Copy the solution and project files
COPY YourSolution.sln .
COPY YourProject/*.csproj ./YourProject/
COPY YourOtherProject/*.csproj ./YourOtherProject/

# Copy packages.config files
COPY YourProject/packages.config ./YourProject/
COPY YourOtherProject/packages.config ./YourOtherProject/

# Restore NuGet packages
RUN nuget restore YourSolution.sln

# Copy source code
COPY . .

# Build and publish the application to C:\publish
RUN msbuild /p:Configuration=$BUILD_CONFIGURATION `
            /p:WebPublishMethod=FileSystem `
            /p:PublishUrl=C:\publish `
            /p:DeployDefaultTarget=WebPublish

# ============================================================
# Stage 2: Final runtime image
# ============================================================

FROM mcr.microsoft.com/dotnet/framework/aspnet:4.8-windowsservercore-ltsc2022

SHELL ["powershell", "-command"]

WORKDIR /inetpub/wwwroot

# Copy from build stage
COPY --from=build /publish .

# Expose necessary ports - By default, IIS uses port 80
EXPOSE 80
# EXPOSE 443

# Copy LogMonitor
WORKDIR /LogMonitor
RUN curl -fSLo LogMonitor.exe https://github.com/microsoft/windows-container-tools/releases/download/v2.1.1/LogMonitor.exe

# Copy LogMonitorConfig.json from local files
COPY LogMonitorConfig.json .

# Set non-administrator user
USER ContainerUser

# Entry
ENTRYPOINT [ "C:\\LogMonitor\\LogMonitor.exe", "C:\\ServiceMonitor.exe", "w3svc" ]
```

## 如何定制本示例（Adapting this Example）

- 将 `YourSolution.sln`、`YourProject.csproj` 等替换为实际名称
- 依据项目与设置调整 Windows Server / .NET Framework 版本
- 视需求增删依赖安装步骤与中间阶段

## 关于阶段命名（Notes on Stage Naming）

- 通过 `AS stage-name` 为每个阶段命名
- 使用 `--from=stage-name` 从先前阶段复制文件
- 可包含多个不用于最终镜像的中间阶段

### LogMonitorConfig.json（参考内容）

此文件用于配置容器内日志监控，请保持如下内容完全一致：

```json
{
  "LogConfig": {
    "sources": [
      {
        "type": "EventLog",
        "startAtOldestRecord": true,
        "eventFormatMultiLine": false,
        "channels": [
          { "name": "system", "level": "Warning" },
          { "name": "application", "level": "Error" }
        ]
      },
      {
        "type": "File",
        "directory": "c:\\inetpub\\logs",
        "filter": "*.log",
        "includeSubdirectories": true,
        "includeFileNames": false
      },
      {
        "type": "ETW",
        "eventFormatMultiLine": false,
        "providers": [
          {
            "providerName": "IIS: WWW Server",
            "providerGuid": "3A2A4E84-4C21-4981-AE10-3FDA0D9B0F83",
            "level": "Information"
          },
          {
            "providerName": "Microsoft-Windows-IIS-Logging",
            "providerGuid": "7E8AD27F-B271-4EA2-A783-A47BDE29143B",
            "level": "Information"
          }
        ]
      }
    ]
  }
}
```

---

**免责声明**：本文件由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 自动本地化，可能存在不准确之处。若发现不当或错误翻译，请提交 [Issue](../../issues) 进行反馈。
