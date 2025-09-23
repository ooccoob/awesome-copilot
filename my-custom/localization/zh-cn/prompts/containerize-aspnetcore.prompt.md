````prompt
---
mode: 'agent'
tools: ['codebase', 'editFiles', 'terminalCommand']
description: '通过为项目创建 Dockerfile 与 .dockerignore，并根据项目特性定制，完成 ASP.NET Core 应用容器化。'
---

# ASP.NET Core Docker 容器化提示

## 容器化需求

对下述设置中指定的 ASP.NET Core（.NET）项目进行容器化，专注于使其在 Linux Docker 容器中运行所需的变更。容器化应遵循此处所有设置。

遵循 .NET Core 容器化最佳实践，确保镜像在性能、安全与可维护性方面优化。

## 容器化设置

此部分包含项目容器化的具体配置。运行本提示前，请填写必要设置。多数场景仅需最前几项，后续若不适用可使用默认值。

未指定项将采用默认值，默认以 [方括号] 标示。

### 基本项目信息
1. 待容器化项目：
   - `[ProjectName (提供 .csproj 路径)]`

2. 目标 .NET 版本：
   - `[8.0 或 9.0（默认 8.0）]`

3. 目标 Linux 发行版：
   - `[debian, alpine, ubuntu, chiseled, Azure Linux (mariner)（默认 debian）]`

4. 构建阶段自定义基础镜像（“None” 表示使用微软官方镜像）：
   - `[构建阶段基础镜像，默认 None]`

5. 运行阶段自定义基础镜像（“None” 表示使用微软官方镜像）：
   - `[运行阶段基础镜像，默认 None]`

### 容器配置
1. 需要暴露的端口：
   - 主 HTTP 端口：`[如 8080]`
   - 其他端口：`[列出或填 "None"]`

2. 容器运行用户：
   - `[用户账户，默认 "$APP_UID"]`

3. 应用 URL 配置：
   - `[指定 ASPNETCORE_URLS，默认 "http://+:8080"]`

### 构建配置
1. 构建镜像前需执行的自定义步骤：
   - `[列出或填 "None"]`

2. 构建镜像后需执行的自定义步骤：
   - `[列出或填 "None"]`

3. 需要配置的 NuGet 源：
   - `[列出私有源与认证方式，或填 "None"]`

### 依赖项
1. 需在镜像内安装的系统包：
   - `[按目标发行版填写包名，或 "None"]`

2. 需复制到镜像内的本地/原生库：
   - `[库名称与路径，或 "None"]`

3. 需要安装的 .NET 工具：
   - `[工具名与版本，或 "None"]`

### 系统配置
1. 需设置的环境变量：
   - `[变量名=值，或 "Use defaults"]`

### 文件系统
1. 需复制到镜像内的文件/目录：
   - `[相对项目根的路径，或 "None"]`
   - 目标容器路径：`[容器内路径，或 "N/A"]`

2. 容器化时应排除的文件/目录：
   - `[路径或 "None"]`

3. 需要配置的数据卷：
   - `[持久化路径，或 "None"]`

### .dockerignore 配置
1. 需加入 .dockerignore 的附加模式（在默认基础上追加）：
   - 附加模式：`[列出或 "None"]`

### 健康检查配置
1. 健康检查端点：
   - `[URL 路径，或 "None"]`

2. 健康检查间隔与超时：
   - `[间隔与超时，或 "Use defaults"]`

### 其他说明
1. 必须遵循的额外说明：
   - `[具体要求，或 "None"]`

2. 需处理的已知问题：
   - `[问题描述，或 "None"]`

## 范围

- ✅ 调整应用配置，使可从环境变量读取设置与连接串
- ✅ 为 ASP.NET Core 应用创建并配置 Dockerfile
- ✅ 使用多阶段构建：build/publish → 复制至最终镜像
- ✅ 适配 Linux 平台（Alpine、Ubuntu、Chiseled、Azure Linux）
- ✅ 正确处理依赖（系统包、原生库、额外工具）
- ❌ 不包含基础设施层面的搭建
- ❌ 不进行容器化之外的代码改动

## 执行流程

1. 审阅以上容器化设置，确认约束
2. 创建 `progress.md` 以勾选方式跟踪变更
3. 从 .csproj 的 `TargetFramework` 获取 .NET 版本
4. 依据以下选择基础镜像：
   - 项目检测到的 .NET 版本
   - 设置中指定的 Linux 发行版（Alpine/Ubuntu/Chiseled/Azure Linux）
   - 若未指定自定义基础镜像，必须使用 mcr.microsoft.com/dotnet 官方镜像并采用有效 tag（参见下方或官方文档）
   - 官方 .NET 镜像：
      - SDK（构建阶段）：https://github.com/dotnet/dotnet-docker/blob/main/README.sdk.md
      - ASP.NET Core 运行时：https://github.com/dotnet/dotnet-docker/blob/main/README.aspnet.md
      - .NET 运行时：https://github.com/dotnet/dotnet-docker/blob/main/README.runtime.md
5. 在项目根创建 Dockerfile 完成容器化
   - 使用多阶段：
     - 构建阶段：使用 .NET SDK 镜像
       - 先复制 csproj
       - 存在则复制 NuGet.config 并配置私有源
       - 还原 NuGet 包
       - 再复制其余源码并构建与发布到 /app/publish
     - 最终阶段：使用选定的运行时镜像
       - 工作目录 /app
       - 按指示设置用户（默认非 root，如 `$APP_UID`）
       - 从构建阶段复制发布产物
   - 同时满足设置中的要求：
     - .NET 版本与发行版
     - 暴露端口
     - 容器运行用户
     - ASPNETCORE_URLS
     - 系统包安装
     - 原生库依赖
     - 额外 .NET 工具
     - 环境变量
     - 文件/目录复制
     - 卷挂载
     - 健康检查
6. 在项目根创建 `.dockerignore`，至少包含以下条目并追加设置中指定模式：
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
   - 以及设置中指定的附加模式
7. 若指定健康检查：
   - 在 Dockerfile 中添加 HEALTHCHECK 指令
   - 使用 curl 或 wget 检查健康端点
8. 将任务依次由 [ ] 置为 [✓]
9. 持续执行直至 Docker 构建成功

## 构建与运行验证

完成 Dockerfile 后，执行构建：

```bash
docker build -t aspnetcore-app:latest .
```

若构建失败，请依据错误调整 Dockerfile 或项目配置，并报告成功/失败情况。

## 进度跟踪

维护 `progress.md`（勾选项）：
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

执行过程无需等待确认。按部就班直至容器化完成且镜像构建通过。

**只有当所有复选项打勾时才算完成！** 包括成功构建镜像及解决构建问题。

## 示例 Dockerfile

以下示例适用于 Linux 基础镜像的 ASP.NET Core 应用。

```dockerfile
# ============================================================
# Stage 1: Build and publish the application
# ============================================================

# 基础镜像（SDK）：选择合适的 .NET SDK 版本与 Linux 发行版
FROM mcr.microsoft.com/dotnet/sdk:8.0-bookworm-slim AS build
ARG BUILD_CONFIGURATION=Release

WORKDIR /src

# 先复制项目文件，提升缓存命中
COPY ["YourProject/YourProject.csproj", "YourProject/"]
COPY ["YourOtherProject/YourOtherProject.csproj", "YourOtherProject/"]

# 若存在则复制 NuGet 配置
COPY ["NuGet.config", "."]

# 还原 NuGet 包
RUN dotnet restore "YourProject/YourProject.csproj"

# 复制源码
COPY . .

# 可选：执行自定义预构建步骤
# RUN echo "Running pre-build steps..."

# 构建与发布
WORKDIR "/src/YourProject"
RUN dotnet build "YourProject.csproj" -c $BUILD_CONFIGURATION -o /app/build

# 发布
RUN dotnet publish "YourProject.csproj" -c $BUILD_CONFIGURATION -o /app/publish /p:UseAppHost=false

# 可选：执行自定义后置步骤
# RUN echo "Running post-build steps..."

# ============================================================
# Stage 2: Final runtime image
# ============================================================

# 基础镜像（ASP.NET 运行时）
FROM mcr.microsoft.com/dotnet/aspnet:8.0-bookworm-slim AS final

# 如需安装系统包（按需开启并调整）
# RUN apt-get update && apt-get install -y \
#     curl \
#     wget \
#     ca-certificates \
#     libgdiplus \
#     && rm -rf /var/lib/apt/lists/*

# 如需安装 .NET 工具（按需开启并调整）
# RUN dotnet tool install --global dotnet-ef --version 8.0.0
# ENV PATH="$PATH:/root/.dotnet/tools"

WORKDIR /app

# 复制发布产物
COPY --from=build /app/publish .

# 可选：复制额外文件
# COPY ./config/appsettings.Production.json .
# COPY ./certificates/ ./certificates/

# 环境变量
ENV ASPNETCORE_ENVIRONMENT=Production
ENV ASPNETCORE_URLS=http://+:8080

# 可选：应用专用环境变量
# ENV CONNECTIONSTRINGS__DEFAULTCONNECTION="your-connection-string"
# ENV FEATURE_FLAG_ENABLED=true

# 可选：证书配置
# ENV ASPNETCORE_Kestrel__Certificates__Default__Path=/app/certificates/app.pfx
# ENV ASPNETCORE_Kestrel__Certificates__Default__Password=your_password

# 暴露端口
EXPOSE 8080
# EXPOSE 8081  # 若启用 HTTPS

# 健康检查所需的 curl（按需选择）
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# 健康检查
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# 可选：持久化卷
# VOLUME ["/app/data", "/app/logs"]

# 安全：使用非 root 用户
USER $APP_UID

# 入口点
ENTRYPOINT ["dotnet", "YourProject.dll"]
```

## 变体说明

### Alpine Linux
镜像体积更小：

```dockerfile
FROM mcr.microsoft.com/dotnet/sdk:8.0-alpine AS build
# ...
FROM mcr.microsoft.com/dotnet/aspnet:8.0-alpine AS final
RUN apk update && apk add --no-cache curl ca-certificates
```

### Ubuntu Chiseled
攻击面更小：

```dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:8.0-jammy-chiseled AS final
# 注意：Chiseled 极简，额外依赖可能需要换用其它基础镜像
```

### Azure Linux (Mariner)
针对 Azure 优化：

```dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:8.0-azurelinux3.0 AS final
RUN tdnf update -y && tdnf install -y curl ca-certificates && tdnf clean all
```

## 阶段命名说明

- 使用 `AS stage-name` 为阶段命名
- 使用 `--from=stage-name` 从之前阶段复制
- 可存在未被最终镜像使用的中间阶段
- `final` 阶段即最终镜像

## 安全最佳实践

- 生产环境务必使用非 root 用户
- 使用明确的镜像标签而非 latest
- 最小化安装的包数量
- 及时更新基础镜像
- 使用多阶段构建避免将构建依赖带入最终镜像

---

**免责声明**：本文件由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 自动本地化，可能存在不准确之处。若发现不当或错误翻译，请提交 [Issue](https://github.com/ooccoob/datafill/issues) 进行反馈。

````
