---
mode: 'agent'
tools: ['codebase', 'edit/editFiles', 'terminalCommand']
description: '通过为项目创建定制的Dockerfile和.dockerfile文件来容器化ASP.NET Core项目。'
---

# ASP.NET Core Docker容器化提示

## 容器化请求

容器化下面设置中指定的ASP.NET Core（.NET）项目，**专门**专注于应用程序在Linux Docker容器中运行所需的更改。容器化应考虑这里指定的所有设置。

遵循容器化.NET Core应用程序的最佳实践，确保容器针对性能、安全性和可维护性进行了优化。

## 容器化设置

本提示部分包含容器化ASP.NET Core应用程序所需的特定设置和配置。在运行此提示之前，确保设置已填写必要信息。请注意，在许多情况下，只需要前几个设置。如果不适用于正在容器化的项目，后面的设置可以保留为默认值。

任何未指定的设置将设置为默认值。默认值在`[方括号]`中提供。

### 基本项目信息
1. 要容器化的项目：
   - `[项目名称（提供.csproj文件的路径）]`

2. 要使用的.NET版本：
   - `[8.0或9.0（默认8.0）]`

3. 要使用的Linux发行版：
   - `[debian、alpine、ubuntu、chiseled或Azure Linux（mariner）（默认debian）]`

4. Docker镜像构建阶段的自定义基础镜像（"无"使用标准Microsoft基础镜像）：
   - `[指定构建阶段使用的基础镜像（默认无）]`

5. Docker镜像运行阶段的自定义基础镜像（"无"使用标准Microsoft基础镜像）：
   - `[指定运行阶段使用的基础镜像（默认无）]`

### 容器配置
1. 必须在容器镜像中暴露的端口：
   - 主要HTTP端口：`[例如，8080]`
   - 附加端口：`[列出任何附加端口，或"无"]`

2. 容器应运行的用户账户：
   - `[用户账户，或默认为"$APP_UID"]`

3. 应用程序URL配置：
   - `[指定ASPNETCORE_URLS，或默认为"http://+:8080"]`

### 构建配置
1. 构建容器镜像之前必须执行的自定义构建步骤：
   - `[列出任何特定构建步骤，或"无"]`

2. 构建容器镜像之后必须执行的自定义构建步骤：
   - `[列出任何特定构建步骤，或"无"]`

3. 必须配置的NuGet包源：
   - `[列出任何具有身份验证详细信息的私有NuGet源，或"无"]`

### 依赖项
1. 必须在容器镜像中安装的系统包：
   - `[所选Linux发行版的包名称，或"无"]`

2. 必须复制到容器镜像的本机库：
   - `[库名称和路径，或"无"]`

3. 必须安装的附加.NET工具：
   - `[工具名称和版本，或"无"]`

### 系统配置
1. 必须在容器镜像中设置的环境变量：
   - `[变量名称和值，或"使用默认值"]`

### 文件系统
1. 需要复制到容器镜像的文件/目录：
   - `[相对于项目根目录的路径，或"无"]`
   - 容器中的目标位置：`[容器路径，或"不适用"]`

2. 要从容器化中排除的文件/目录：
   - `[要排除的路径，或"无"]`

3. 应配置的卷挂载点：
   - `[持久数据的卷路径，或"无"]`

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

- ✅ 应用配置修改，确保应用程序设置和连接字符串可以从环境变量读取
- ✅ 为ASP.NET Core应用程序创建和配置Dockerfile
- ✅ 在Dockerfile中指定多个阶段来构建/发布应用程序并将输出复制到最终镜像
- ✅ Linux容器平台兼容性配置（Alpine、Ubuntu、Chiseled或Azure Linux（Mariner））
- ✅ 依赖项的正确处理（系统包、本机库、附加工具）
- ❌ 无基础架构设置（假设单独处理）
- ❌ 除了容器化所需的代码更改外，无其他代码更改

## 执行流程

1. 审查上面的容器化设置以了解容器化要求
2. 创建一个`progress.md`文件，用复选标记跟踪更改
3. 通过检查项目.csproj文件中的`TargetFramework`元素确定.NET版本
4. 根据以下内容选择适当的Linux容器镜像：
   - 从项目检测到的.NET版本
   - 容器化设置中指定的Linux发行版（Alpine、Ubuntu、Chiseled或Azure Linux（Mariner））
   - 如果用户在容器化设置中没有请求特定的基础镜像，则基础镜像必须是有效的mcr.microsoft.com/dotnet镜像，带有如下例Dockerfile或文档中所示的标签
   - 构建和运行阶段的官方Microsoft .NET镜像：
      - SDK镜像标签（用于构建阶段）：https://github.com/dotnet/dotnet-docker/blob/main/README.sdk.md
      - ASP.NET Core运行时镜像标签：https://github.com/dotnet/dotnet-docker/blob/main/README.aspnet.md
      - .NET运行时镜像标签：https://github.com/dotnet/dotnet-docker/blob/main/README.runtime.md
5. 在项目目录根目录创建Dockerfile来容器化应用程序
   - Dockerfile应使用多个阶段：
     - 构建阶段：使用.NET SDK镜像构建应用程序
       - 首先复制.csproj文件
       - 如果存在，复制NuGet.config并配置任何私有源
       - 恢复NuGet包
       - 然后，复制其余源代码并构建和发布应用程序到/app/publish
     - 最终阶段：使用选定的.NET运行时镜像运行应用程序
       - 将工作目录设置为/app
       - 按指示设置用户（默认情况下，为非root用户（例如，`$APP_UID`））
         - 除非在容器化设置中另有指示，否则*不*需要创建新用户。使用`$APP_UID`变量指定用户账户。
       - 将发布的输出从构建阶段复制到最终镜像
   - 确保考虑容器化设置中的所有要求：
     - .NET版本和Linux发行版
     - 暴露的端口
     - 容器的用户账户
     - ASPNETCORE_URLS配置
     - 系统包安装
     - 本机库依赖项
     - 附加.NET工具
     - 环境变量
     - 文件/目录复制
     - 卷挂载点
     - 健康检查配置
6. 在项目目录根目录创建.dockerignore文件，从Docker镜像中排除不必要的文件。.dockerignore文件**必须**至少包含以下元素以及容器化设置中指定的附加模式：
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
7. 如果在容器化设置中指定，配置健康检查：
   - 如果提供了健康检查端点，向Dockerfile添加HEALTHCHECK指令
   - 使用curl或wget检查健康端点
8. 标记任务为已完成：[ ] → [✓]
9. 继续直到所有任务完成且Docker构建成功

## 构建和运行时验证

一旦Dockerfile完成，确认Docker构建成功。使用以下命令构建Docker镜像：

```bash
docker build -t aspnetcore-app:latest .
```

如果构建失败，审查错误消息并对Dockerfile或项目配置进行必要调整。报告成功/失败。

## 进度跟踪

维护一个具有以下结构的`progress.md`文件：
```markdown
# 容器化进度

## 环境检测
- [ ] .NET版本检测（版本：___）
- [ ] Linux发行版选择（发行版：___）

## 配置更改
- [ ] 应用程序配置验证环境变量支持
- [ ] NuGet包源配置（如果适用）

## 容器化
- [ ] Dockerfile创建
- [ ] .dockerignore文件创建
- [ ] 使用SDK镜像创建构建阶段
- [ ] 复制.csproj文件以进行包恢复
- [ ] 如果适用，复制NuGet.config
- [ ] 使用运行时镜像创建运行时阶段
- [ ] 非root用户配置
- [ ] 依赖项处理（系统包、本机库、工具等）
- [ ] 健康检查配置（如果适用）
- [ ] 特殊要求实施

## 验证
- [ ] 审查容器化设置并确保满足所有要求
- [ ] Docker构建成功
```

不要在步骤之间暂停确认。继续系统性地直到应用程序已容器化且Docker构建成功。

**在所有复选框标记完成之前您还没有完成！**这包括成功构建Docker镜像并解决构建过程中出现的任何问题。

## 示例Dockerfile

使用Linux基础镜像的ASP.NET Core（.NET）应用程序的示例Dockerfile。

```dockerfile
# ============================================================
# 阶段1：构建和发布应用程序
# ============================================================

# 基础镜像 - 选择适当的.NET SDK版本和Linux发行版
# 可能的标签包括：
# - 8.0-bookworm-slim (Debian 12)
# - 8.0-noble (Ubuntu 24.04)
# - 8.0-alpine (Alpine Linux)
# - 9.0-bookworm-slim (Debian 12)
# - 9.0-noble (Ubuntu 24.04)
# - 9.0-alpine (Alpine Linux)
# 使用.NET SDK镜像构建应用程序
FROM mcr.microsoft.com/dotnet/sdk:8.0-bookworm-slim AS build
ARG BUILD_CONFIGURATION=Release

WORKDIR /src

# 首先复制项目文件以获得更好的缓存
COPY ["YourProject/YourProject.csproj", "YourProject/"]
COPY ["YourOtherProject/YourOtherProject.csproj", "YourOtherProject/"]

# 如果存在，复制NuGet配置
COPY ["NuGet.config", "."]

# 恢复NuGet包
RUN dotnet restore "YourProject/YourProject.csproj"

# 复制源代码
COPY . .

# 如果需要，在这里执行自定义预构建步骤
# RUN echo "运行预构建步骤..."

# 构建和发布应用程序
WORKDIR "/src/YourProject"
RUN dotnet build "YourProject.csproj" -c $BUILD_CONFIGURATION -o /app/build

# 发布应用程序
RUN dotnet publish "YourProject.csproj" -c $BUILD_CONFIGURATION -o /app/publish /p:UseAppHost=false

# 如果需要，在这里执行自定义构建后步骤
# RUN echo "运行构建后步骤..."

# ============================================================
# 阶段2：最终运行时镜像
# ============================================================

# 基础镜像 - 选择适当的.NET运行时版本和Linux发行版
# 可能的标签包括：
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
# 使用.NET运行时镜像运行应用程序
FROM mcr.microsoft.com/dotnet/aspnet:8.0-bookworm-slim AS final

# 如果需要，安装系统包（取消注释并根据需要修改）
# RUN apt-get update && apt-get install -y \
#     curl \
#     wget \
#     ca-certificates \
#     libgdiplus \
#     && rm -rf /var/lib/apt/lists/*

# 如果需要，安装附加的.NET工具（取消注释并根据需要修改）
# RUN dotnet tool install --global dotnet-ef --version 8.0.0
# ENV PATH="$PATH:/root/.dotnet/tools"

WORKDIR /app

# 从构建阶段复制发布的应用程序
COPY --from=build /app/publish .

# 如果需要，复制附加文件（取消注释并根据需要修改）
# COPY ./config/appsettings.Production.json .
# COPY ./certificates/ ./certificates/

# 设置环境变量
ENV ASPNETCORE_ENVIRONMENT=Production
ENV ASPNETCORE_URLS=http://+:8080

# 如果需要，添加自定义环境变量（取消注释并根据需要修改）
# ENV CONNECTIONSTRINGS__DEFAULTCONNECTION="your-connection-string"
# ENV FEATURE_FLAG_ENABLED=true

# 如果需要，配置SSL/TLS证书（取消注释并根据需要修改）
# ENV ASPNETCORE_Kestrel__Certificates__Default__Path=/app/certificates/app.pfx
# ENV ASPNETCORE_Kestrel__Certificates__Default__Password=your_password

# 暴露应用程序监听的端口
EXPOSE 8080
# EXPOSE 8081  # 如果使用HTTPS，取消注释

# 如果尚未安装curl，则安装curl用于健康检查
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# 配置健康检查
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# 如果需要，为持久数据创建卷（取消注释并根据需要修改）
# VOLUME ["/app/data", "/app/logs"]

# 为了安全切换到非root用户
USER $APP_UID

# 设置应用程序的入口点
ENTRYPOINT ["dotnet", "YourProject.dll"]
```

## 调整此示例

**注意**：基于容器化设置中的特定要求自定义此模板。

调整此示例Dockerfile时：

1. 将`YourProject.csproj`、`YourProject.dll`等替换为您的实际项目名称
2. 根据需要调整.NET版本和Linux发行版
3. 根据您的要求修改依赖项安装步骤并删除任何不必要的步骤
4. 配置特定于您的应用程序的环境变量
5. 根据您的特定工作流需要添加或删除阶段
6. 更新健康检查端点以匹配您应用程序的健康检查路由

## Linux发行版变体

### Alpine Linux
为了更小的镜像大小，您可以使用Alpine Linux：

```dockerfile
FROM mcr.microsoft.com/dotnet/sdk:8.0-alpine AS build
# ... 构建步骤 ...

FROM mcr.microsoft.com/dotnet/aspnet:8.0-alpine AS final
# 使用apk安装包
RUN apk update && apk add --no-cache curl ca-certificates
```

### Ubuntu Chiseled
为了最小的攻击面，考虑使用chiseled镜像：

```dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:8.0-jammy-chiseled AS final
# 注意：Chiseled镜像的包最少，所以您可能需要为附加依赖项使用不同的基础
```

### Azure Linux (Mariner)
为了Azure优化的容器：

```dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:8.0-azurelinux3.0 AS final
# 使用tdnf安装包
RUN tdnf update -y && tdnf install -y curl ca-certificates && tdnf clean all
```

## 阶段命名说明

- `AS stage-name`语法为每个阶段命名
- 使用`--from=stage-name`从先前阶段复制文件
- 您可以有多个不在最终镜像中使用的中间阶段
- `final`阶段是成为最终容器镜像的阶段

## 安全最佳实践

- 在生产环境中始终以非root用户运行
- 使用特定镜像标签而不是`latest`
- 最小化已安装包的数量
- 保持基础镜像更新
- 使用多阶段构建将构建依赖项从最终镜像中排除