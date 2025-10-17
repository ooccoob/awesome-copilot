## 文档综述（What/When/Why/How）

- What：将 ASP.NET（.NET Framework）应用容器化（Windows 容器），生成 Dockerfile/.dockerignore 与变更说明

- When：需要在 Windows Server Core/Full 上以 IIS 运行传统 .NET Framework Web 应用时

- Why：标准化镜像构建与运行，支持环境变量配置、依赖注册与健康检查，提升交付一致性

- How：多阶段构建（SDK→ASP.NET），配置 web.config ConfigBuilders，复制 LogMonitorConfig.json，按设置处理端口/IIS/依赖

## 示例提问（Examples）

- “检测 TargetFrameworkVersion 并选择匹配的 Windows Server Core 基础镜像生成 Dockerfile”

- “在 web.config 中启用 Environment ConfigBuilder 读取 appSettings/connectionStrings”

- “添加 .dockerignore、健康检查与依赖（GAC/MSI/COM/Registry）处理示例”

## 结构化要点（CN/EN）

- 平台/Platform：Windows 容器 + IIS | Windows container + IIS

- 构建/Build：mcr sdk → publish；运行：mcr aspnet | Multi-stage build

- 配置/Config：ConfigBuilders 环境变量注入 | Env-based settings

- 监控/Monitor：LogMonitor + ServiceMonitor 入口 | ENTRYPOINT LogMonitor

- 清单/Checklist：端口、用户、IIS、依赖、健康检查、进度跟踪

## 中文思维导图

- 镜像选择
  - Windows 版本/SKU
  - .NET FW 版本匹配
- 多阶段构建
  - 还原/发布
  - 运行镜像与复制
- 配置注入
  - web.config builders
  - 环境变量
- 运行监控
  - LogMonitor 配置
  - 健康检查
- 依赖处理
  - GAC/MSI/COM/Registry

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\containerize-aspnet-framework.prompt.md

- 生成时间：2025-10-17
