---
mode: 'agent'
tools: ['codebase', 'edit/editFiles', 'terminalCommand']
description: '通过为项目创建定制的Dockerfile和.dockerfile文件来容器化ASP.NET .NET Framework项目。'
---

# ASP.NET .NET Framework容器化提示

容器化下面容器化设置中指定的ASP.NET（.NET Framework）项目，**专门**专注于应用程序在Windows Docker容器中运行所需的更改。容器化应考虑这里指定的所有设置。

**记住**：这是一个.NET Framework应用程序，而不是.NET Core。容器化过程将与.NET Core应用程序的容器化过程不同。

## 容器化设置

本提示部分包含容器化ASP.NET（.NET Framework）应用程序所需的特定设置和配置。在运行此提示之前，确保设置已填写必要信息。请注意，在许多情况下，只需要前几个设置。如果不适用于正在容器化的项目，后面的设置可以保留为默认值。

任何未指定的设置将设置为默认值。默认值在`[方括号]`中提供。

### 基本项目信息
1. 要容器化的项目：
   - `[项目名称（提供.csproj文件的路径）]`

2. 要使用的Windows Server SKU：
   - `[Windows Server Core（默认）或Windows Server Full]`

3. 要使用的Windows Server版本：
   - `[2022、2019或2016（默认2022）]`

4. Docker镜像构建阶段的自定义基础镜像（"无"使用标准Microsoft基础镜像）：
   - `[指定构建阶段使用的基础镜像（默认无）]`

5. Docker镜像运行阶段的自定义基础镜像（"无"使用标准Microsoft基础镜像）：
   - `[指定运行阶段使用的基础镜像（默认无）]`

### 容器配置
1. 必须在容器镜像中暴露的端口：
   - 主要HTTP端口：`[例如，80]`
   - 附加端口：`[列出任何附加端口，或"无"]`

2. 容器应运行的用户账户：
   - `[用户账户，或默认为"ContainerUser"]`

3. 必须在容器镜像中配置的IIS设置：
   - `[列出任何特定IIS设置，或"无"]`

### 构建配置
1. 构建容器镜像之前必须执行的自定义构建步骤：
   - `[列出任何特定构建步骤，或"无"]`

2. 构建容器镜像之后必须执行的自定义构建步骤：
   - `[列出任何特定构建步骤，或"无"]`

### 依赖项
1. 应在容器镜像的GAC中注册的.NET程序集：
   - `[程序集名称和版本，或"无"]`

2. 必须复制到容器镜像并安装的MSI：
   - `[MSI名称和版本，或"无"]`

3. 必须在容器镜像中注册的COM组件：
   - `[COM组件名称，或"无"]`

### 系统配置
1. 必须添加到容器镜像的注册表项和值：
   - `[注册表路径和值，或"无"]`

2. 必须在容器镜像中设置的环境变量：
   - `[变量名称和值，或"使用默认值"]`

3. 必须在容器镜像中安装的Windows Server角色和功能：
   - `[角色/功能名称，或"无"]`

### 文件系统
1. 需要复制到容器镜像的文件/目录：
   - `[相对于项目根目录的路径，或"无"]`
   - 容器中的目标位置：`[容器路径，或"不适用"]`

2. 要从容器化中排除的文件/目录：
   - `[要排除的路径，或"无"]`

### .dockerignore配置
1. 要包含在`.dockerignore`文件中的模式（.dockerignore已有常见默认值；这些是附加模式）：
   - 附加模式：`[列出任何附加模式，或"无"]`

### 健康检查配置
1. 健康检查端点：
   - `[健康检查URL路径，或"无"]`

2. 健康检查间隔和超时：
   - `[间隔和超时值，或"使用默认值"]`

### 附加说明
1. 容器化项目必须遵循的其他说明：
   - `[特定要求，或"无"]`

2. 要解决的已知问题：
   - `[描述任何已知问题，或"无"]`

## 范围

- ✅ 应用配置修改，确保使用配置构建器从环境变量读取应用程序设置和连接字符串
- ✅ 为ASP.NET应用程序创建和配置Dockerfile
- ✅ 在Dockerfile中指定多个阶段来构建/发布应用程序并将输出复制到最终镜像
- ✅ Windows容器平台兼容性配置（Windows Server Core或Full）
- ✅ 依赖项的正确处理（GAC程序集、MSI、COM组件）
- ❌ 无基础架构设置（假设单独处理）
- ❌ 除了容器化所需的代码更改外，无其他代码更改

## 执行流程

1. 审查上面的容器化设置以了解容器化要求
2. 创建一个`progress.md`文件，用复选标记跟踪更改
3. 通过检查项目.csproj文件中的`TargetFrameworkVersion`元素确定.NET Framework版本
4. 根据以下内容选择适当的Windows Server容器镜像：
   - 从项目检测到的.NET Framework版本
   - 容器化设置中指定的Windows Server SKU（Core或Full）
   - 容器化设置中指定的Windows Server版本（2016、2019或2022）
   - Windows Server Core标签可以在以下位置找到：https://github.com/microsoft/dotnet-framework-docker/blob/main/README.aspnet.md#full-tag-listing
5. 确保安装了所需的NuGet包。**不要**如果缺少则安装这些包。如果它们没有安装，用户必须手动安装。如果它们没有安装，暂停执行此提示并要求用户使用Visual Studio NuGet包管理器或Visual Studio包管理器控制台安装它们。需要以下包：
   - `Microsoft.Configuration.ConfigurationBuilders.Environment`
6. 修改`web.config`文件以添加配置构建器部分和设置，以从环境变量读取应用程序设置和连接字符串：
   - 在configSections中添加ConfigBuilders部分
   - 在根目录中添加configBuilders部分
   - 为appSettings和connectionStrings配置EnvironmentConfigBuilder
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
       <!-- 现有应用程序设置 -->
     </appSettings>
     <connectionStrings configBuilders="Environment">
       <!-- 现有连接字符串 -->
     </connectionStrings>
     ```
7. 通过复制本提示末尾的参考`LogMonitorConfig.json`文件，在将创建Dockerfile的文件夹中创建一个`LogMonitorConfig.json`文件。除非容器化设置中的说明另有指定，否则文件内容**不得**修改，应与参考内容完全匹配。
   - 特别是，确保要记录的问题级别不要更改，因为对EventLog源使用`Information`级别会导致不必要的噪音。
8. 在项目目录根目录创建Dockerfile来容器化应用程序
   - Dockerfile应使用多个阶段：
     - 构建阶段：使用Windows Server Core镜像构建应用程序
       - 构建阶段**必须**使用`mcr.microsoft.com/dotnet/framework/sdk`基础镜像，除非在设置文件中指定了自定义基础镜像
       - 首先复制sln、csproj和packages.config文件
       - 如果存在，复制NuGet.config并配置任何私有源
       - 恢复NuGet包
       - 然后，复制其余源代码并使用MSBuild构建和发布应用程序到C:\publish
     - 最终阶段：使用选定的Windows Server镜像运行应用程序
       - 最终阶段**必须**使用`mcr.microsoft.com/dotnet/framework/aspnet`基础镜像，除非在设置文件中指定了自定义基础镜像
       - 将`LogMonitorConfig.json`文件复制到容器中的目录（例如，C:\LogMonitor）
       - 从Microsoft存储库下载LogMonitor.exe到同一目录
           - 正确的LogMonitor.exe URL是：https://github.com/microsoft/windows-container-tools/releases/download/v2.1.1/LogMonitor.exe
       - 将工作目录设置为C:\inetpub\wwwroot
       - 将构建阶段的发布输出（在C:\publish中）复制到最终镜像
       - 将容器的入口点设置为运行LogMonitor.exe与ServiceMonitor.exe来监控IIS服务
           - `ENTRYPOINT [ "C:\\LogMonitor\\LogMonitor.exe", "C:\\ServiceMonitor.exe", "w3svc" ]`
   - 确保考虑容器化设置中的所有要求：
     - Windows Server SKU和版本
     - 暴露的端口
     - 容器的用户账户
     - IIS设置
     - GAC程序集注册
     - MSI安装
     - COM组件注册
     - 注册表项
     - 环境变量
     - Windows角色和功能
     - 文件/目录复制
   - 在本提示末尾提供的示例之后建模Dockerfile，但确保它根据特定项目要求和设置进行自定义。
   - **重要**：使用Windows Server Core基础镜像，除非用户在设置文件中**特别请求**了完整的Windows Server镜像
9. 在项目目录根目录创建.dockerignore文件，从Docker镜像中排除不必要的文件。.dockerignore文件**必须**至少包含以下元素以及容器化设置中指定的附加模式：
   - packages/
   - bin/
   - obj/
   - .dockerignore
   - Dockerfile
   - .git/
   - .github/
   - .vs/
   - .vscode/
   - **/node_modules/
   - *.user
   - *.suo
   - **/.DS_Store
   - **/Thumbs.db
   - 容器化设置中指定的任何附加模式
10. 如果在设置中指定，配置健康检查：
    - 如果提供了健康检查端点，向Dockerfile添加HEALTHCHECK指令
11. 通过将以下项目添加到项目文件中来将dockerfile添加到项目：`<None Include="Dockerfile" />`
12. 标记任务为已完成：[ ] → [✓]
13. 继续直到所有任务完成且Docker构建成功

## 构建和运行时验证

一旦Dockerfile完成，确认Docker构建成功。使用以下命令构建Docker镜像：

```bash
docker build -t aspnet-app:latest .
```

如果构建失败，审查错误消息并对Dockerfile或项目配置进行必要调整。报告成功/失败。

## 进度跟踪

维护一个具有以下结构的`progress.md`文件：
```markdown
# 容器化进度

## 环境检测
- [ ] .NET Framework版本检测（版本：___）
- [ ] Windows Server SKU选择（SKU：___）
- [ ] Windows Server版本选择（版本：___）

## 配置更改
- [ ] Web.config修改以配置构建器
- [ ] NuGet包源配置（如果适用）
- [ ] 复制LogMonitorConfig.json并根据设置要求进行调整

## 容器化
- [ ] Dockerfile创建
- [ ] .dockerignore文件创建
- [ ] 使用SDK镜像创建构建阶段
- [ ] 复制sln、csproj、packages.config以及（如果适用）NuGet.config以进行包恢复
- [ ] 使用运行时镜像创建运行时阶段
- [ ] 非root用户配置
- [ ] 依赖项处理（GAC、MSI、COM、注册表、附加文件等）
- [ ] 健康检查配置（如果适用）
- [ ] 特殊要求实施

## 验证
- [ ] 审查容器化设置并确保满足所有要求
- [ ] Docker构建成功
```

不要在步骤之间暂停确认。继续系统性地直到应用程序已容器化且Docker构建成功。

**在所有复选框标记完成之前您还没有完成！**这包括成功构建Docker镜像并解决构建过程中出现的任何问题。

## 参考资料

### 示例Dockerfile

使用Windows Server Core基础镜像的ASP.NET（.NET Framework）应用程序的示例Dockerfile。

```dockerfile
# escape=`
# escape指令将转义字符从\更改为`
# 这在Windows Dockerfile中特别有用，其中\是路径分隔符

# ============================================================
# 阶段1：构建和发布应用程序
# ============================================================

# 基础镜像 - 选择适当的.NET Framework版本和Windows Server Core版本
# 可能的标签包括：
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
# 使用.NET Framework SDK镜像构建应用程序
FROM mcr.microsoft.com/dotnet/framework/sdk:4.8-windowsservercore-ltsc2022 AS build
ARG BUILD_CONFIGURATION=Release

# 将默认shell设置为PowerShell
SHELL ["powershell", "-command"]

WORKDIR /app

# 复制解决方案和项目文件
COPY YourSolution.sln .
COPY YourProject/*.csproj ./YourProject/
COPY YourOtherProject/*.csproj ./YourOtherProject/

# 复制packages.config文件
COPY YourProject/packages.config ./YourProject/
COPY YourOtherProject/packages.config ./YourOtherProject/

# 恢复NuGet包
RUN nuget restore YourSolution.sln

# 复制源代码
COPY . .

# 如果需要，在这里执行自定义预构建步骤

# 构建和发布应用程序到C:\publish
RUN msbuild /p:Configuration=$BUILD_CONFIGURATION `
            /p:WebPublishMethod=FileSystem `
            /p:PublishUrl=C:\publish `
            /p:DeployDefaultTarget=WebPublish

# 如果需要，在这里执行自定义构建后步骤

# ============================================================
# 阶段2：最终运行时镜像
# ============================================================

# 基础镜像 - 选择适当的.NET Framework版本和Windows Server Core版本
# 可能的标签包括：
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
# 使用.NET Framework ASP.NET镜像运行应用程序
FROM mcr.microsoft.com/dotnet/framework/aspnet:4.8-windowsservercore-ltsc2022

# 将默认shell设置为PowerShell
SHELL ["powershell", "-command"]

WORKDIR /inetpub/wwwroot

# 从构建阶段复制
COPY --from=build /publish .

# 为您的应用程序添加任何所需的附加环境变量（取消注释并根据需要修改）
# ENV KEY=VALUE

# 如果需要，安装MSI包（取消注释并根据需要修改）
# COPY ./msi-installers C:/Installers
# RUN Start-Process -Wait -FilePath 'msiexec.exe' -ArgumentList '/i', 'C:\Installers\your-package.msi', '/quiet', '/norestart'

# 如果需要，安装自定义Windows Server角色和功能（取消注释并根据需要修改）
# RUN dism /Online /Enable-Feature /FeatureName:YOUR-FEATURE-NAME

# 如果需要，添加附加Windows功能（取消注释并根据需要修改）
# RUN Add-WindowsFeature Some-Windows-Feature; `
#    Add-WindowsFeature Another-Windows-Feature

# 如果需要，安装MSI包（取消注释并根据需要修改）
# COPY ./msi-installers C:/Installers
# RUN Start-Process -Wait -FilePath 'msiexec.exe' -ArgumentList '/i', 'C:\Installers\your-package.msi', '/quiet', '/norestart'

# 如果需要，在GAC中注册程序集（取消注释并根据需要修改）
# COPY ./assemblies C:/Assemblies
# RUN C:\Windows\Microsoft.NET\Framework64\v4.0.30319\gacutil -i C:/Assemblies/YourAssembly.dll

# 如果需要，注册COM组件（取消注释并根据需要修改）
# COPY ./com-components C:/Components
# RUN regsvr32 /s C:/Components/YourComponent.dll

# 如果需要，添加注册表项（取消注释并根据需要修改）
# RUN New-Item -Path 'HKLM:\Software\YourApp' -Force; `
#     Set-ItemProperty -Path 'HKLM:\Software\YourApp' -Name 'Setting' -Value 'Value'

# 如果需要，配置IIS设置（取消注释并根据需要修改）
# RUN Import-Module WebAdministration; `
#     Set-ItemProperty 'IIS:\AppPools\DefaultAppPool' -Name somePropertyName -Value 'SomePropertyValue'; `
#     Set-ItemProperty 'IIS:\Sites\Default Web Site' -Name anotherPropertyName -Value 'AnotherPropertyValue'

# 暴露必要端口 - 默认情况下，IIS使用端口80
EXPOSE 80
# EXPOSE 443  # 如果使用HTTPS，取消注释

# 从microsoft/windows-container-tools存储库复制LogMonitor
WORKDIR /LogMonitor
RUN curl -fSLo LogMonitor.exe https://github.com/microsoft/windows-container-tools/releases/download/v2.1.1/LogMonitor.exe

# 从本地文件复制LogMonitorConfig.json
COPY LogMonitorConfig.json .

# 设置非管理员用户
USER ContainerUser

# 覆盖容器的默认入口点以利用LogMonitor
ENTRYPOINT [ "C:\\LogMonitor\\LogMonitor.exe", "C:\\ServiceMonitor.exe", "w3svc" ]
```

## 调整此示例

**注意**：基于容器化设置中的特定要求自定义此模板。

调整此示例Dockerfile时：

1. 将`YourSolution.sln`、`YourProject.csproj`等替换为您的实际文件名
2. 根据需要调整Windows Server和.NET Framework版本
3. 根据您的要求修改依赖项安装步骤并删除任何不必要的步骤
4. 根据您的特定工作流需要添加或删除阶段

## 阶段命名说明

- `AS stage-name`语法为每个阶段命名
- 使用`--from=stage-name`从先前阶段复制文件
- 您可以有多个不在最终镜像中使用的中间阶段

### LogMonitorConfig.json

LogMonitorConfig.json文件应在项目目录根目录中创建。它用于配置LogMonitor工具，该工具监控容器中的日志。此文件的内容应完全如下所示，以确保正确的日志功能：
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