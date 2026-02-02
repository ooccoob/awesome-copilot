---
agent: 'agent'
tools: ['search/codebase', 'edit/editFiles', 'terminalCommand']
description: 'Containerize an ASP.NET Core project by creating Dockerfile and .dockerfile files customized for the project.'
---

# ASP.NET Core Docker 容器化提示

## 集装箱化请求

将以下设置中指定的 ASP.NET Core (.NET) 项目容器化，**专门**关注应用程序在 Linux Docker 容器中运行所需的更改。容器化应考虑此处指定的所有设置。

遵守容器化 .NET Core 应用程序的最佳实践，确保容器针对性能、安全性和可维护性进行优化。

## 容器化设置

提示的这一部分包含容器化 ASP.NET Core 应用程序所需的特定设置和配置。在运行此提示之前，请确保已填写设置所需的信息。请注意，在许多情况下，只需要前几个设置。如果后续设置不适用于正在容器化的项目，则可以将其保留为默认值。

任何未指定的设置都将设置为默认值。默认值在 `[square brackets]` 中提供。

### 项目基本信息
1. 容器化项目： 
   - __代码0__

2. 要使用的.NET版本：
   - __代码0__

3. Linux 发行版使用：
   - __代码0__

4. 用于 Docker 映像构建阶段的自定义基础映像（“无”以使用标准 Microsoft 基础映像）：
   - __代码0__

5. Docker 映像运行阶段的自定义基础映像（“无”以使用标准 Microsoft 基础映像）：
   - __代码0__   

### 容器配置
1. 容器镜像中必须暴露的端口：
   - 主要 HTTP 端口：`[e.g., 8080]`
   - 附加端口：`[List any additional ports, or "None"]`

2. 容器应以以下用户帐户运行：
   - __代码0__

3. 应用程序URL配置：
   - __代码0__

### 构建配置
1. 在构建容器映像之前必须执行的自定义构建步骤：
   - __代码0__

2. 构建容器镜像后必须执行的自定义构建步骤：
   - __代码0__

3. 必须配置的 NuGet 包源：
   - __代码0__

### 依赖关系
1. 容器镜像中必须安装的系统包：
   - __代码0__

2. 必须复制到容器映像的本机库：
   - __代码0__

3. 必须安装的其他 .NET 工具：
   - __代码0__

### 系统配置
1. 容器镜像中必须设置的环境变量：
   - __代码0__

### 文件系统
1. 需要复制到容器镜像的文件/目录：
   - __代码0__
   - 容器中的目标位置：`[Container paths, or "Not applicable"]`

2. 要从容器化中排除的文件/目录：
   - __代码0__

3. 应配置的卷安装点：
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

- ✅ 应用程序配置修改，以确保可以从环境变量中读取应用程序设置和连接字符串
- ✅ ASP.NET Core 应用程序的 Dockerfile 创建和配置
- ✅ 在 Dockerfile 中指定多个阶段来构建/发布应用程序并将输出复制到最终映像
- ✅ 配置 Linux 容器平台兼容性（Alpine、Ubuntu、Chiseled 或 Azure Linux (Mariner)）
- ✅ 正确处理依赖项（系统包、本机库、附加工具）
- ❌ 没有基础设施设置（假设单独处理）
- ❌ 除了容器化所需的代码之外，无需进行任何代码更改

## 执行流程

1. 查看上面的容器化设置以了解容器化要求
2. 创建一个 `progress.md` 文件以跟踪带有复选标记的更改
3. 通过检查 `TargetFramework` 元素来确定项目的 .csproj 文件中的 .NET 版本
4. 根据以下条件选择适当的 Linux 容器镜像：
   - 从项目中检测到的.NET版本
   - 容器化设置中指定的 Linux 发行版（Alpine、Ubuntu、Chiseled 或 Azure Linux (Mariner)）
   - 如果用户未在容器化设置中请求特定的基础映像，则基础映像必须是有效的 mcr.microsoft.com/dotnet 映像，其标签如下面的示例 Dockerfile 或文档中所示
   - 用于构建和运行时阶段的官方 Microsoft .NET 映像：
      - SDK 图像标签（用于构建阶段）：https://github.com/dotnet/dotnet-docker/blob/main/README.sdk.md
      - ASP.NET Core 运行时镜像标签：https://github.com/dotnet/dotnet-docker/blob/main/README.aspnet.md
      - .NET 运行时映像标签：https://github.com/dotnet/dotnet-docker/blob/main/README.runtime.md
5. 在项目根目录下创建一个Dockerfile来容器化应用程序
   - Dockerfile 应使用多个阶段：
     - 构建阶段：使用 .NET SDK 映像构建应用程序
       - 首先复制 csproj 文件
       - 复制 NuGet.config（如果存在）并配置任何私有源
       - 恢复 NuGet 包
       - 然后，复制其余源代码并构建应用程序并将其发布到 /app/publish
     - 最后阶段：使用选定的.NET运行时映像来运行应用程序
       - 将工作目录设置为/app
       - 按照指示设置用户（默认情况下为非 root 用户（例如 `$APP_UID`））
         - 除非在容器化设置中另有指示，否则*不需要*创建新用户。使用 `$APP_UID` 变量指定用户帐户。
       - 将发布的输出从构建阶段复制到最终图像
   - 请务必考虑容器化设置中的所有要求：
     - .NET 版本和 Linux 发行版
     - 暴露端口
     - 容器的用户帐户
     - ASPNETCORE_URLS 配置
     - 系统包安装
     - 本机库依赖项
     - 其他 .NET 工具
     - 环境变量
     - 文件/目录复制
     - 卷挂载点
     - 健康检查配置
6. 在项目根目录中创建 `.dockerignore` 文件，以排除 Docker 镜像中不必要的文件。 `.dockerignore` 文件 **必须** 至少包含以下元素以及容器化设置中指定的其他模式：
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
7. 如果在容器化设置中指定，则配置运行状况检查：
   - 如果提供了健康检查端点，则将 HEALTHCHECK 指令添加到 Dockerfile
   - 使用curl或wget检查健康端点
8. 将任务标记为已完成：[ ] → [✓]
9. 继续，直到所有任务完成且 Docker 构建成功

## 构建和运行时验证

Dockerfile 完成后，确认 Docker 构建成功。使用以下命令构建 Docker 镜像：

```bash
docker build -t aspnetcore-app:latest .
```

如果构建失败，请查看错误消息并对 Dockerfile 或项目配置进行必要的调整。报告成功/失败。

## 进度追踪

维护一个具有以下结构的 `progress.md` 文件：
```markdown
# Containerization Progress

## Environment Detection
- [ ] .NET version detection (version: ___)
- [ ] Linux distribution selection (distribution: ___)

## Configuration Changes
- [ ] Application configuration verification for environment variable support
- [ ] NuGet package source configuration (if applicable)

## Containerization
- [ ] Dockerfile creation
- [ ] .dockerignore file creation
- [ ] Build stage created with SDK image
- [ ] csproj file(s) copied for package restore
- [ ] NuGet.config copied if applicable
- [ ] Runtime stage created with runtime image
- [ ] Non-root user configuration
- [ ] Dependency handling (system packages, native libraries, tools, etc.)
- [ ] Health check configuration (if applicable)
- [ ] Special requirements implementation

## Verification
- [ ] Review containerization settings and make sure that all requirements are met
- [ ] Docker build success
```

步骤之间不要暂停进行确认。有条不紊地继续，直到应用程序被容器化并且 Docker 构建成功。

**直到标记了所有复选框才算完成！** 这包括成功构建 Docker 映像并解决构建过程中出现的任何问题。

## Dockerfile 示例

使用 Linux 基础映像的 ASP.NET Core (.NET) 应用程序的示例 Dockerfile。

```dockerfile
# ============================================================
# Stage 1: Build and publish the application
# ============================================================

# Base Image - Select the appropriate .NET SDK version and Linux distribution
# Possible tags include:
# - 8.0-bookworm-slim (Debian 12)
# - 8.0-noble (Ubuntu 24.04)
# - 8.0-alpine (Alpine Linux)
# - 9.0-bookworm-slim (Debian 12)
# - 9.0-noble (Ubuntu 24.04)
# - 9.0-alpine (Alpine Linux)
# Uses the .NET SDK image for building the application
FROM mcr.microsoft.com/dotnet/sdk:8.0-bookworm-slim AS build
ARG BUILD_CONFIGURATION=Release

WORKDIR /src

# Copy project files first for better caching
COPY ["YourProject/YourProject.csproj", "YourProject/"]
COPY ["YourOtherProject/YourOtherProject.csproj", "YourOtherProject/"]

# Copy NuGet configuration if it exists
COPY ["NuGet.config", "."]

# Restore NuGet packages
RUN dotnet restore "YourProject/YourProject.csproj"

# Copy source code
COPY . .

# Perform custom pre-build steps here, if needed
# RUN echo "Running pre-build steps..."

# Build and publish the application
WORKDIR "/src/YourProject"
RUN dotnet build "YourProject.csproj" -c $BUILD_CONFIGURATION -o /app/build

# Publish the application
RUN dotnet publish "YourProject.csproj" -c $BUILD_CONFIGURATION -o /app/publish /p:UseAppHost=false

# Perform custom post-build steps here, if needed
# RUN echo "Running post-build steps..."

# ============================================================
# Stage 2: Final runtime image
# ============================================================

# Base Image - Select the appropriate .NET runtime version and Linux distribution
# Possible tags include:
# - 8.0-bookworm-slim (Debian 12)
# - 8.0-noble (Ubuntu 24.04)
# - 8.0-alpine (Alpine Linux)
# - 8.0-noble-chiseled (Ubuntu 24.04 Chiseled)
# - 8.0-azurelinux3.0 (Azure Linux)
# - 9.0-bookworm-slim (Debian 12)
# - 9.0-noble (Ubuntu 24.04)
# - 9.0-alpine (Alpine Linux)
# - 9.0-noble-chiseled (Ubuntu 24.04 Chiseled)
# - 9.0-azurelinux3.0 (Azure Linux)
# Uses the .NET runtime image for running the application
FROM mcr.microsoft.com/dotnet/aspnet:8.0-bookworm-slim AS final

# Install system packages if needed (uncomment and modify as needed)
# RUN apt-get update && apt-get install -y \
#     curl \
#     wget \
#     ca-certificates \
#     libgdiplus \
#     && rm -rf /var/lib/apt/lists/*

# Install additional .NET tools if needed (uncomment and modify as needed)
# RUN dotnet tool install --global dotnet-ef --version 8.0.0
# ENV PATH="$PATH:/root/.dotnet/tools"

WORKDIR /app

# Copy published application from build stage
COPY --from=build /app/publish .

# Copy additional files if needed (uncomment and modify as needed)
# COPY ./config/appsettings.Production.json .
# COPY ./certificates/ ./certificates/

# Set environment variables
ENV ASPNETCORE_ENVIRONMENT=Production
ENV ASPNETCORE_URLS=http://+:8080

# Add custom environment variables if needed (uncomment and modify as needed)
# ENV CONNECTIONSTRINGS__DEFAULTCONNECTION="your-connection-string"
# ENV FEATURE_FLAG_ENABLED=true

# Configure SSL/TLS certificates if needed (uncomment and modify as needed)
# ENV ASPNETCORE_Kestrel__Certificates__Default__Path=/app/certificates/app.pfx
# ENV ASPNETCORE_Kestrel__Certificates__Default__Password=your_password

# Expose the port the application listens on
EXPOSE 8080
# EXPOSE 8081  # Uncomment if using HTTPS

# Install curl for health checks if not already present
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Configure health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# Create volumes for persistent data if needed (uncomment and modify as needed)
# VOLUME ["/app/data", "/app/logs"]

# Switch to non-root user for security
USER $APP_UID

# Set the entry point for the application
ENTRYPOINT ["dotnet", "YourProject.dll"]
```

## 调整此示例

**注意：** 根据容器化设置中的具体要求自定义此模板。

改编此示例 Dockerfile 时：

1. 将 `YourProject.csproj`、`YourProject.dll` 等替换为您的实际项目名称
2. 根据需要调整.NET版本和Linux发行版
3. 根据您的需求修改依赖安装步骤，删除不需要的
4. 配置特定于您的应用程序的环境变量
5. 根据您的特定工作流程的需要添加或删除阶段
6. 更新健康检查端点以匹配您的应用程序的健康检查路由

## Linux 发行版本

### 阿尔卑斯Linux
对于较小的图像尺寸，您可以使用 Alpine Linux：

```dockerfile
FROM mcr.microsoft.com/dotnet/sdk:8.0-alpine AS build
# ... build steps ...

FROM mcr.microsoft.com/dotnet/aspnet:8.0-alpine AS final
# Install packages using apk
RUN apk update && apk add --no-cache curl ca-certificates
```

### Ubuntu 凿刻
为了最小化攻击面，请考虑使用轮廓分明的图像：

```dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:8.0-jammy-chiseled AS final
# Note: Chiseled images have minimal packages, so you may need to use a different base for additional dependencies
```

### Azure Linux（水手）
对于 Azure 优化的容器：

```dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:8.0-azurelinux3.0 AS final
# Install packages using tdnf
RUN tdnf update -y && tdnf install -y curl ca-certificates && tdnf clean all
```

## 舞台命名注意事项

- `AS stage-name` 语法给每个阶段一个名称
- 使用 `--from=stage-name` 复制前一阶段的文件
- 您可以有多个最终图像中未使用的中间阶段
- `final` 阶段是成为最终容器镜像的阶段

## 安全最佳实践

- 在生产中始终以非 root 用户身份运行
- 使用特定图像标签而不是 `latest`
- 最小化安装的软件包数量
- 保持基础镜像更新
- 使用多阶段构建从最终映像中排除构建依赖项
