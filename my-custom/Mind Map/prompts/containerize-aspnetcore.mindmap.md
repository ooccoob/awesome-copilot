## 文档综述（What/When/Why/How）

- What：将 ASP.NET Core 应用容器化（Linux），生成多阶段 Dockerfile、.dockerignore 与可选健康检查

- When：需要使用 Debian/Alpine/Ubuntu/Chiseled/Azure Linux 等基础镜像并遵循最佳实践时

- Why：实现性能/安全/可维护的容器交付，运行非 root，最小化镜像与依赖

- How：SDK 构建/发布→ASP.NET 运行，设置 ASPNETCORE_URLS、暴露端口、安装必要系统包、配置 HEALTHCHECK

## 示例提问（Examples）

- “检测 .csproj TargetFramework，选择匹配的 mcr .NET SDK/ASP.NET 运行时镜像并生成 Dockerfile”

- “添加 .dockerignore 与非 root 用户运行（$APP_UID），配置 curl 健康检查”

- “根据需求选择 debian/alpine/chiseled/azurelinux 变体并说明差异”

## 结构化要点（CN/EN）

- 平台/Platform：Linux 容器 | Debian/Alpine/Ubuntu/Chiseled/Mariner

- 构建/Build：dotnet restore/build/publish | Multi-stage

- 运行/Run：ASPNETCORE_URLS 非 root | USER $APP_UID

- 健康/Health：curl/wget → HEALTHCHECK | Port expose

- 安全/Security：最小依赖、固定镜像标签、定期更新

## 中文思维导图

- 基础镜像
  - SDK/运行时版本
  - 发行版选择
- 构建与发布
  - 还原/构建/发布
  - 发布目录复制
- 运行配置
  - 环境变量/端口
  - 非 root 用户
- 健康检查
  - curl 端点
- 附加依赖
  - 系统包/原生库/工具

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\containerize-aspnetcore.prompt.md

- 生成时间：2025-10-17
