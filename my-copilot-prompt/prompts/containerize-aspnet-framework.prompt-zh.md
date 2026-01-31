---
代理人：“代理人”
工具：['搜索/代码库'、'编辑/编辑文件'、'终端命令']
描述：“通过创建为项目定制的 Dockerfile 和 .dockerfile 文件来容器化 ASP.NET .NET Framework 项目。”
---

# ASP.NET .NET Framework 容器化提示

对下面容器化设置中指定的 ASP.NET (.NET Framework) 项目进行容器化，**仅**关注应用程序在 Windows Docker 容器中运行所需的更改。容器化应考虑此处指定的所有设置。

**记住：**这是一个 .NET Framework 应用程序，而不是 .NET Core。容器化过程将不同于 .NET Core 应用程序的容器化过程。

## 容器化设置

提示的这一部分包含容器化 ASP.NET (.NET Framework) 应用程序所需的特定设置和配置。在运行此提示之前，请确保已填写设置所需的信息。请注意，在许多情况下，只需要前几个设置。如果后续设置不适用于正在容器化的项目，则可以将其保留为默认值。

任何未指定的设置都将设置为默认值。默认值在 `[square brackets]` 中提供。

### 项目基本信息
1. 容器化项目： 
   - __代码0__

2. 要使用的 Windows Server SKU：
   - __代码0__

3. 要使用的 Windows Server 版本：
   - __代码0__

4. 用于 Docker 映像构建阶段的自定义基础映像（“无”以使用标准 Microsoft 基础映像）：
   - __代码0__

5. Docker 映像运行阶段的自定义基础映像（“无”以使用标准 Microsoft 基础映像）：
   - __代码0__   

### 容器配置
1. 容器镜像中必须暴露的端口：
   - 主要 HTTP 端口：`[e.g., 80]`
   - 附加端口：`[List any additional ports, or "None"]`

2. 容器应以以下用户帐户运行：
   - __代码0__

3. 必须在容器映像中配置的 IIS 设置：
   - __代码0__

### 构建配置
1. 在构建容器映像之前必须执行的自定义构建步骤：
   - __代码0__

2. 构建容器镜像后必须执行的自定义构建步骤：
   - __代码0__

### 依赖关系
1. 应在容器映像的 GAC 中注册的 .NET 程序集：
   - __代码0__

2. 必须复制到容器映像并安装的 MSI：
   - __代码0__

3. 必须在容器镜像中注册的COM组件：
   - __代码0__

### 系统配置
1. 必须添加到容器映像的注册表项和值：
   - __代码0__

2. 容器镜像中必须设置的环境变量：
   - __代码0__

3. 容器映像中必须安装的 Windows Server 角色和功能：
   - __代码0__

### 文件系统
1. 需要复制到容器镜像的文件/目录：
   - __代码0__
   - 容器中的目标位置：`[Container paths, or "Not applicable"]`

2. 要从容器化中排除的文件/目录：
   - __代码0__

### .dockerignore 配置
1. 要包含在 `.dockerignore` 文件中的模式（.dockerignore 已经具有通用默认值；这些是附加模式）：
   - 附加模式：`[List any additional patterns, or "None"]`

### 健康检查配置
1. 健康检查端点：
   - __代码0__

2. 健康检查间隔和超时时间：
   - __代码0__

### 附加说明
1. 容器化项目必须遵循的其他说明：
   - __代码0__

2. 需要解决的已知问题：
   - __代码0__

## 适用范围

- ✅ 应用程序配置修改，以确保使用配置构建器从环境变量中读取应用程序设置和连接字符串
- ✅ ASP.NET 应用程序的 Dockerfile 创建和配置
- ✅ 在 Dockerfile 中指定多个阶段来构建/发布应用程序并将输出复制到最终映像
- ✅ 配置 Windows 容器平台兼容性（Windows Server Core 或 Full）
- ✅ 正确处理依赖项（GAC 程序集、MSI、COM 组件）
- ❌ 没有基础设施设置（假设单独处理）
- ❌ 除了容器化所需的代码之外，无需进行任何代码更改

## 执行流程

1. 查看上面的容器化设置以了解容器化要求
2. 创建一个 `progress.md` 文件以跟踪带有复选标记的更改
3. 通过检查 `TargetFrameworkVersion` 元素来确定项目的 .csproj 文件中的 .NET Framework 版本
4. 根据以下条件选择适当的 Windows Server 容器映像：
   - 从项目中检测到的 .NET Framework 版本
   - 容器化设置中指定的 Windows Server SKU（核心或完整）
   - 容器化设置中指定的 Windows Server 版本（2016、2019 或 2022）
   - Windows Server Core 标签可以在以下位置找到：https://github.com/microsoft/dotnet-framework-docker/blob/main/README.aspnet.md#full-tag-listing
5. 确保安装了所需的 NuGet 包。如果缺少，**请勿**安装它们。如果未安装，用户必须手动安装。如果未安装，请暂停执行此提示，并要求用户使用 Visual Studio NuGet 包管理器或 Visual Studio 包管理器控制台安装它们。需要以下包：
   - __代码0__
6. 修改 `web.config` 文件以添加配置构建器部分和设置，以从环境变量中读取应用程序设置和连接字符串：
   - 在 configSections 中添加 ConfigBuilders 部分
   - 在根目录中添加 configBuilders 部分
   - 为appSettings 和connectionStrings 配置EnvironmentConfigBuilder
   - 示例模式：
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
7. 通过复制此提示末尾的引用 `LogMonitorConfig.json` 文件，在将创建 Dockerfile 的文件夹中创建 `LogMonitorConfig.json` 文件。文件的内容**不得** 不得修改，并且应与参考内容完全匹配，除非容器化设置中的说明另有指定。
   - 特别是，请确保要记录的问题级别不会更改，因为对 EventLog 源使用 `Information` 级别会导致不必要的噪音。
8. 在项目根目录下创建一个Dockerfile来容器化应用程序
   - Dockerfile 应使用多个阶段：
     - 构建阶段：使用 Windows Server Core 映像构建应用程序
       - 构建阶段必须使用 `mcr.microsoft.com/dotnet/framework/sdk` 基础镜像，除非在设置文件中指定了自定义基础镜像
       - 首先复制 sln、csproj 和packages.config 文件
       - 复制 NuGet.config（如果存在）并配置任何私有源
       - 恢复 NuGet 包       
       - 然后，复制其余源代码并使用 MSBuild 构建应用程序并将其发布到 C:\publish
     - 最后阶段：使用选定的 Windows Server 映像运行应用程序
       - 最后阶段必须使用 `mcr.microsoft.com/dotnet/framework/aspnet` 基础镜像，除非在设置文件中指定了自定义基础镜像
       - 将 `LogMonitorConfig.json` 文件复制到容器中的目录（例如 C:\LogMonitor）
       - 从 Microsoft 存储库下载 LogMonitor.exe 到同一目录
           - 正确的 LogMonitor.exe URL 是：https://github.com/microsoft/windows-container-tools/releases/download/v2.1.1/LogMonitor.exe
       - 将工作目录设置为 C:\inetpub\wwwroot
       - 将发布的输出从构建阶段（在 C:\publish 中）复制到最终图像
       - 设置容器的入口点以运行 LogMonitor.exe 和 ServiceMonitor.exe 来监视 IIS 服务
           - __代码0__
   - 请务必考虑容器化设置中的所有要求：
     - Windows Server SKU 和版本
     - 暴露端口
     - 容器的用户帐户
     - IIS 设置
     - GAC大会注册
     - 微星安装
     - COM组件注册
     - 注册表项
     - 环境变量
     - Windows 角色和功能
     - 文件/目录复制
   - 按照本提示末尾提供的示例对 Dockerfile 进行建模，但确保它根据特定项目要求和设置进行自定义。
   - **重要：** 使用 Windows Server Core 基础映像，除非用户在设置文件中**特别请求**完整的 Windows Server 映像
9. 在项目根目录中创建 `.dockerignore` 文件，以排除 Docker 镜像中不必要的文件。 `.dockerignore` 文件 **必须** 至少包含以下元素以及容器化设置中指定的其他模式：
   - 包/
   - 垃圾箱/
   - 对象/
   - .dockerignore
   - Dockerfile
   - .git/
   - .github/
   - .vs/
   - .vscode/
   - ** /节点模块/
   - *.用户
   - *.suo
   - **/.DS_Store
   - **/大拇指.db
   - 容器化设置中指定的任何其他模式
10. 如果在设置中指定，则配置运行状况检查：
   - 如果提供了健康检查端点，则将 HEALTHCHECK 指令添加到 Dockerfile
11. 通过将以下项添加到项目文件中，将 dockerfile 添加到项目中：`<None Include="Dockerfile" />`
12. 将任务标记为已完成：[ ] → [✓]
13. 继续，直到所有任务完成且 Docker 构建成功

## 构建和运行时验证

Dockerfile 完成后，确认 Docker 构建成功。使用以下命令构建 Docker 镜像：

```bash
docker build -t aspnet-app:latest .
```

如果构建失败，请查看错误消息并对 Dockerfile 或项目配置进行必要的调整。报告成功/失败。

## 进度追踪

维护一个具有以下结构的 `progress.md` 文件：
```markdown
# Containerization Progress

## Environment Detection
- [ ] .NET Framework version detection (version: ___)
- [ ] Windows Server SKU selection (SKU: ___)
- [ ] Windows Server version selection (Version: ___)

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

步骤之间不要暂停进行确认。有条不紊地继续，直到应用程序被容器化并且 Docker 构建成功。

**直到标记了所有复选框才算完成！** 这包括成功构建 Docker 映像并解决构建过程中出现的任何问题。

## 参考资料

### Dockerfile 示例

使用 Windows Server Core 基础映像的 ASP.NET (.NET Framework) 应用程序的示例 Dockerfile。

```dockerfile
# escape=`
# The escape directive changes the escape character from \ to `
# This is especially useful in Windows Dockerfiles where \ is the path separator

# ============================================================
# Stage 1: Build and publish the application
# ============================================================

# Base Image - Select the appropriate .NET Framework version and Windows Server Core version
# Possible tags include:
# - 4.8.1-windowsservercore-ltsc2025 (Windows Server 2025)
# - 4.8-windowsservercore-ltsc2022 (Windows Server 2022)
# - 4.8-windowsservercore-ltsc2019 (Windows Server 2019)
# - 4.8-windowsservercore-ltsc2016 (Windows Server 2016)
# - 4.7.2-windowsservercore-ltsc2019 (Windows Server 2019)
# - 4.7.2-windowsservercore-ltsc2016 (Windows Server 2016)
# - 4.7.1-windowsservercore-ltsc2016 (Windows Server 2016)
# - 4.7-windowsservercore-ltsc2016 (Windows Server 2016)
# - 4.6.2-windowsservercore-ltsc2016 (Windows Server 2016)
# - 3.5-windowsservercore-ltsc2025 (Windows Server 2025)
# - 3.5-windowsservercore-ltsc2022 (Windows Server 2022)
# - 3.5-windowsservercore-ltsc2019 (Windows Server 2019)
# - 3.5-windowsservercore-ltsc2019 (Windows Server 2016)
# Uses the .NET Framework SDK image for building the application
FROM mcr.microsoft.com/dotnet/framework/sdk:4.8-windowsservercore-ltsc2022 AS build
ARG BUILD_CONFIGURATION=Release

# Set the default shell to PowerShell
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

# Perform custom pre-build steps here, if needed

# Build and publish the application to C:\publish
RUN msbuild /p:Configuration=$BUILD_CONFIGURATION `
            /p:WebPublishMethod=FileSystem `
            /p:PublishUrl=C:\publish `
            /p:DeployDefaultTarget=WebPublish

# Perform custom post-build steps here, if needed

# ============================================================
# Stage 2: Final runtime image
# ============================================================

# Base Image - Select the appropriate .NET Framework version and Windows Server Core version
# Possible tags include:
# - 4.8.1-windowsservercore-ltsc2025 (Windows Server 2025)
# - 4.8-windowsservercore-ltsc2022 (Windows Server 2022)
# - 4.8-windowsservercore-ltsc2019 (Windows Server 2019)
# - 4.8-windowsservercore-ltsc2016 (Windows Server 2016)
# - 4.7.2-windowsservercore-ltsc2019 (Windows Server 2019)
# - 4.7.2-windowsservercore-ltsc2016 (Windows Server 2016)
# - 4.7.1-windowsservercore-ltsc2016 (Windows Server 2016)
# - 4.7-windowsservercore-ltsc2016 (Windows Server 2016)
# - 4.6.2-windowsservercore-ltsc2016 (Windows Server 2016)
# - 3.5-windowsservercore-ltsc2025 (Windows Server 2025)
# - 3.5-windowsservercore-ltsc2022 (Windows Server 2022)
# - 3.5-windowsservercore-ltsc2019 (Windows Server 2019)
# - 3.5-windowsservercore-ltsc2019 (Windows Server 2016)
# Uses the .NET Framework ASP.NET image for running the application
FROM mcr.microsoft.com/dotnet/framework/aspnet:4.8-windowsservercore-ltsc2022

# Set the default shell to PowerShell
SHELL ["powershell", "-command"]

WORKDIR /inetpub/wwwroot

# Copy from build stage
COPY --from=build /publish .

# Add any additional environment variables needed for your application (uncomment and modify as needed)
# ENV KEY=VALUE

# Install MSI packages (uncomment and modify as needed)
# COPY ./msi-installers C:/Installers
# RUN Start-Process -Wait -FilePath 'msiexec.exe' -ArgumentList '/i', 'C:\Installers\your-package.msi', '/quiet', '/norestart'

# Install custom Windows Server roles and features (uncomment and modify as needed)
# RUN dism /Online /Enable-Feature /FeatureName:YOUR-FEATURE-NAME

# Add additional Windows features (uncomment and modify as needed)
# RUN Add-WindowsFeature Some-Windows-Feature; `
#    Add-WindowsFeature Another-Windows-Feature

# Install MSI packages if needed (uncomment and modify as needed)
# COPY ./msi-installers C:/Installers
# RUN Start-Process -Wait -FilePath 'msiexec.exe' -ArgumentList '/i', 'C:\Installers\your-package.msi', '/quiet', '/norestart'

# Register assemblies in GAC if needed (uncomment and modify as needed)
# COPY ./assemblies C:/Assemblies
# RUN C:\Windows\Microsoft.NET\Framework64\v4.0.30319\gacutil -i C:/Assemblies/YourAssembly.dll

# Register COM components if needed (uncomment and modify as needed)
# COPY ./com-components C:/Components
# RUN regsvr32 /s C:/Components/YourComponent.dll

# Add registry keys if needed (uncomment and modify as needed)
# RUN New-Item -Path 'HKLM:\Software\YourApp' -Force; `
#     Set-ItemProperty -Path 'HKLM:\Software\YourApp' -Name 'Setting' -Value 'Value'

# Configure IIS settings if needed (uncomment and modify as needed)
# RUN Import-Module WebAdministration; `
#     Set-ItemProperty 'IIS:\AppPools\DefaultAppPool' -Name somePropertyName -Value 'SomePropertyValue'; `
#     Set-ItemProperty 'IIS:\Sites\Default Web Site' -Name anotherPropertyName -Value 'AnotherPropertyValue'

# Expose necessary ports - By default, IIS uses port 80
EXPOSE 80
# EXPOSE 443  # Uncomment if using HTTPS

# Copy LogMonitor from the microsoft/windows-container-tools repository
WORKDIR /LogMonitor
RUN curl -fSLo LogMonitor.exe https://github.com/microsoft/windows-container-tools/releases/download/v2.1.1/LogMonitor.exe

# Copy LogMonitorConfig.json from local files
COPY LogMonitorConfig.json .

# Set non-administrator user
USER ContainerUser

# Override the container's default entry point to take advantage of the LogMonitor
ENTRYPOINT [ "C:\\LogMonitor\\LogMonitor.exe", "C:\\ServiceMonitor.exe", "w3svc" ]
```

## 调整此示例

**注意：** 根据容器化设置中的具体要求自定义此模板。 

改编此示例 Dockerfile 时：

1. 将 `YourSolution.sln`、`YourProject.csproj` 等替换为您的实际文件名
2. 根据需要调整 Windows Server 和 .NET Framework 版本
3. 根据您的需求修改依赖安装步骤，删除不需要的
4. 根据您的特定工作流程的需要添加或删除阶段

## 舞台命名注意事项

- `AS stage-name` 语法给每个阶段一个名称
- 使用 `--from=stage-name` 复制前一阶段的文件
- 您可以有多个最终图像中未使用的中间阶段

### 日志监控配置.json

应在项目目录的根目录中创建 LogMonitorConfig.json 文件。用于配置LogMonitor工具，该工具监控容器中的日志。该文件的内容应如下所示，以确保正确的日志记录功能：
```json
{
  "LogConfig": {
    "sources": [
      {
        "type": "EventLog",
        "startAtOldestRecord": true,
        "eventFormatMultiLine": false,
        "channels": [
          {
            "name": "system",
            "level": "Warning"
          },
          {
            "name": "application",
            "level": "Error"
          }
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
