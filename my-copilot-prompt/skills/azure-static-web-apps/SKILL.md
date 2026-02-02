---
name: azure-static-web-apps
description: Helps create, configure, and deploy Azure Static Web Apps using the SWA CLI. Use when deploying static sites to Azure, setting up SWA local development, configuring staticwebapp.config.json, adding Azure Functions APIs to SWA, or setting up GitHub Actions CI/CD for Static Web Apps.
---

## 概述

Azure 静态 Web 应用 (SWA) 托管具有可选无服务器 API 后端的静态前端。 SWA CLI (`swa`) 提供本地开发模拟和部署功能。

**主要特点：**
- 具有 API 代理和身份验证模拟的本地模拟器
- 框架自动检测和配置
- 直接部署到 Azure
- 数据库连接支持

**配置文件：**
- `swa-cli.config.json` - CLI 设置，**由 `swa init`** 创建（切勿手动创建）
- `staticwebapp.config.json` - 运行时配置（路由、身份验证、标头、API 运行时） - 可以手动创建

## 一般说明

### 安装

```bash
npm install -D @azure/static-web-apps-cli
```

验证：`npx swa --version`

### 快速启动工作流程

**重要提示：始终使用 `swa init` 创建配置文件。切勿手动创建 `swa-cli.config.json`.**

1. `swa init` - **必需的第一步** - 自动检测框架并创建 `swa-cli.config.json`
2. `swa start` - 在 `http://localhost:4280` 处运行本地模拟器
3. `swa login` - 使用 Azure 进行身份验证
4. `swa deploy` - 部署到 Azure

### 配置文件

**swa-cli.config.json** - 由 `swa init` 创建，请勿手动创建：
- 运行 `swa init` 进行框架检测的交互式设置
- 运行 `swa init --yes` 以接受自动检测到的默认值
- 编辑生成的文件仅用于初始化后自定义设置

生成的配置示例（仅供参考）：
```json
{
  "$schema": "https://aka.ms/azure/static-web-apps-cli/schema",
  "configurations": {
    "app": {
      "appLocation": ".",
      "apiLocation": "api",
      "outputLocation": "dist",
      "appBuildCommand": "npm run build",
      "run": "npm run dev",
      "appDevserverUrl": "http://localhost:3000"
    }
  }
}
```

**staticwebapp.config.json**（在应用程序源或输出文件夹中）-可以手动创建此文件以进行运行时配置：
```json
{
  "navigationFallback": {
    "rewrite": "/index.html",
    "exclude": ["/images/*", "/css/*"]
  },
  "routes": [
    { "route": "/api/*", "allowedRoles": ["authenticated"] }
  ],
  "platform": {
    "apiRuntime": "node:20"
  }
}
```

## 命令行参考

### 登录

使用 Azure 进行身份验证以进行部署。

```bash
swa login                              # Interactive login
swa login --subscription-id <id>       # Specific subscription
swa login --clear-credentials          # Clear cached credentials
```

**标志：** `--subscription-id, -S` | __代码1__ | __代码2__ | __代码3__ | __代码4__ | __代码5__

### swa初始化

基于现有前端和（可选）API 配置新的 SWA 项目。自动检测框架。

```bash
swa init                    # Interactive setup
swa init --yes              # Accept defaults
```

### 西南瓦建设

构建前端和/或 API。

```bash
swa build                   # Build using config
swa build --auto            # Auto-detect and build
swa build myApp             # Build specific configuration
```

**标志：** `--app-location, -a` | __代码1__ | __代码2__ | __代码3__ | __代码4__

### 西南航空开始

启动本地开发模拟器。

```bash
swa start                                    # Serve from outputLocation
swa start ./dist                             # Serve specific folder
swa start http://localhost:3000              # Proxy to dev server
swa start ./dist --api-location ./api        # With API folder
swa start http://localhost:3000 --run "npm start"  # Auto-start dev server
```

**常用框架端口：**
|框架|港口|
|-----------|------|
| React/Vue/Next.js | 3000 | 3000
|角度| 4200 | 4200
|维特 | 5173 | 5173

**关键标志：**
- `--port, -p` - 模拟器端口（默认：4280）
- `--api-location, -i` - API 文件夹路径
- `--api-port, -j` - API 端口（默认值：7071）
- `--run, -r` - 启动开发服务器的命令
- `--open, -o` - 自动打开浏览器
- `--ssl, -s` - 启用 HTTPS

### 西南瓦部署

部署到 Azure 静态 Web 应用。

```bash
swa deploy                              # Deploy using config
swa deploy ./dist                       # Deploy specific folder
swa deploy --env production             # Deploy to production
swa deploy --deployment-token <TOKEN>   # Use deployment token
swa deploy --dry-run                    # Preview without deploying
```

**获取部署令牌：**
- Azure 门户：静态 Web 应用程序 → 概述 → 管理部署令牌
- CLI: `swa deploy --print-token`
- 环境变量：`SWA_CLI_DEPLOYMENT_TOKEN`

**关键标志：**
- `--env` - 目标环境（`preview` 或 `production`）
- `--deployment-token, -d` - 部署令牌
- `--app-name, -n` - Azure SWA 资源名称

### 斯瓦数据库

初始化数据库连接。

```bash
swa db init --database-type mssql
swa db init --database-type postgresql
swa db init --database-type cosmosdb_nosql
```

## 应用场景

### 从现有前端和后端创建 SWA

**始终在 `swa start` 或 `swa deploy` 之前运行 `swa init`。不要手动创建 `swa-cli.config.json`.**

```bash
# 1. Install CLI
npm install -D @azure/static-web-apps-cli

# 2. Initialize - REQUIRED: creates swa-cli.config.json with auto-detected settings
npx swa init              # Interactive mode
# OR
npx swa init --yes        # Accept auto-detected defaults

# 3. Build application (if needed)
npm run build

# 4. Test locally (uses settings from swa-cli.config.json)
npx swa start

# 5. Deploy
npx swa login
npx swa deploy --env production
```

### 添加 Azure Functions 后端

1. **创建API文件夹：**
```bash
mkdir api && cd api
func init --worker-runtime node --model V4
func new --name message --template "HTTP trigger"
```

2. **示例函数** (`api/src/functions/message.js`)：
```javascript
const { app } = require('@azure/functions');

app.http('message', {
    methods: ['GET', 'POST'],
    authLevel: 'anonymous',
    handler: async (request) => {
        const name = request.query.get('name') || 'World';
        return { jsonBody: { message: `Hello, ${name}!` } };
    }
});
```

3. **在 `staticwebapp.config.json` 中设置 API 运行时**：
```json
{
  "platform": { "apiRuntime": "node:20" }
}
```

4. **更新 `swa-cli.config.json` 中的 CLI 配置**：
```json
{
  "configurations": {
    "app": { "apiLocation": "api" }
  }
}
```

5. **本地测试：**
```bash
npx swa start ./dist --api-location ./api
# Access API at http://localhost:4280/api/message
```

**支持的 API 运行时：** `node:18`、`node:20`、`node:22`、`dotnet:8.0`、`dotnet-isolated:8.0`、`python:3.10`、`python:3.11`

### 设置 GitHub Actions 部署

1. **在 Azure 门户中或通过 Azure CLI 创建 SWA 资源**
2. **链接 GitHub 存储库** - 自动生成工作流程，或手动创建：

__代码0__：
```yaml
name: Azure Static Web Apps CI/CD

on:
  push:
    branches: [main]
  pull_request:
    types: [opened, synchronize, reopened, closed]
    branches: [main]

jobs:
  build_and_deploy:
    if: github.event_name == 'push' || (github.event_name == 'pull_request' && github.event.action != 'closed')
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build And Deploy
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN }}
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          action: upload
          app_location: /
          api_location: api
          output_location: dist

  close_pr:
    if: github.event_name == 'pull_request' && github.event.action == 'closed'
    runs-on: ubuntu-latest
    steps:
      - uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN }}
          action: close
```

3. **添加秘密：** 将部署令牌复制到存储库秘密 `AZURE_STATIC_WEB_APPS_API_TOKEN`

**工作流程设置：**
- `app_location` - 前端源路径
- `api_location` - API 源路径
- `output_location` - 构建输出文件夹
- `skip_app_build: true` - 如果预先构建则跳过
- `app_build_command` - 自定义构建命令

## 故障排除

|问题 |解决方案 |
|-------|----------|
|客户端路由上的 404 |将 `navigationFallback` 和 `rewrite: "/index.html"` 添加到 `staticwebapp.config.json` |
| API 返回 404 |验证 `api` 文件夹结构，确保设置 `platform.apiRuntime`，检查函数导出 |
|未找到构建输出 |验证 `output_location` 与实际构建输出目录匹配 |
|身份验证无法在本地工作 |使用 `/.auth/login/<provider>` 访问身份验证模拟器 UI |
| CORS 错误 | `/api/*`下的API是同源的；外部 API 需要 CORS 标头 |
|部署令牌已过期 |在 Azure 门户中重新生成 → 静态 Web 应用程序 → 管理部署令牌 |
|配置未应用 |确保 `staticwebapp.config.json` 位于 `app_location` 或 `output_location` | 中
|本地API超时|默认为 45 秒；优化函数或检查阻塞调用 |

**调试命令：**
```bash
swa start --verbose log        # Verbose output
swa deploy --dry-run           # Preview deployment
swa --print-config             # Show resolved configuration
```
