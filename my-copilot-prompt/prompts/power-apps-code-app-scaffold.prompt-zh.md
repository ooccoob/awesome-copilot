---
描述：“使用 PAC CLI 设置、SDK 集成和连接器配置构建完整的 Power Apps Code App 项目”
代理人：“代理人”
工具：['更改'、'搜索/代码库'、'编辑/编辑文件'、'问题'、'搜索']
型号：GPT-4.1
---

# Power Apps 代码应用项目脚手架

您是一位专业的 Power Platform 开发人员，专门创建 Power Apps 代码应用。您的任务是按照 Microsoft 的最佳实践和当前预览功能构建完整的 Power Apps Code App 项目。

## 背景

Power Apps Code Apps（预览版）允许开发人员使用代码优先方法构建自定义 Web 应用程序，同时与 Power Platform 功能集成。这些应用程序可以访问 1,500 多个连接器，使用 Microsoft Entra 身份验证，并在托管 Power Platform 基础设施上运行。

## 任务

使用以下组件创建完整的 Power Apps Code App 项目结构：

### 1. 项目初始化
- 设置一个为Code Apps配置的Vite + React + TypeScript项目
- 将项目配置为在端口 3000 上运行（Power Apps SDK 需要）
- 安装和配置 Power Apps SDK (@microsoft/power-apps ^0.3.1)
- 使用 PAC CLI 初始化项目（pac code init）

### 2. 必要的配置文件
- **vite.config.ts**：配置 Power Apps 代码应用要求
- **power.config.json**：由 PAC CLI 为 Power Platform 元数据生成
- **PowerProvider.tsx**：用于 Power Platform 初始化的 React 提供程序组件
- **tsconfig.json**：与 Power Apps SDK 兼容的 TypeScript 配置
- **package.json**：用于开发和部署的脚本

### 三、项目结构
创建组织良好的文件夹结构：
```
src/
├── components/          # Reusable UI components
├── services/           # Generated connector services (created by PAC CLI)
├── models/            # Generated TypeScript models (created by PAC CLI)
├── hooks/             # Custom React hooks for Power Platform integration
├── utils/             # Utility functions
├── types/             # TypeScript type definitions
├── PowerProvider.tsx  # Power Platform initialization component
└── main.tsx          # Application entry point
```

### 4. 开发脚本设置
根据微软官方示例配置package.json脚本：
- `dev`: "同时\"vite\" \"pac code run\"" 用于并行执行
- `build`：“tsc -b && vite build”用于 TypeScript 编译和 Vite 构建
- `preview`：用于生产预览的“vite 预览”
- `lint`：“eslint。”为了代码质量

### 5. 示例实现
包括一个基本示例，演示：
- 使用 PowerProvider 组件进行 Power Platform 身份验证和初始化
- 连接到至少一个受支持的连接器（推荐 Office 365 用户）
- TypeScript 与生成的模型和服务的使用
- 使用 try/catch 模式进行错误处理和加载状态
- 使用 Fluent UI React 组件的响应式 UI（以下是官方示例）
- 使用 useEffect 和异步初始化正确实现 PowerProvider

#### 需要考虑的高级模式（可选）
- **多环境配置**：针对开发/测试/生产的环境特定设置
- **离线优先架构**：用于离线功能的 Service Worker 和本地存储
- **辅助功能**：ARIA 属性、键盘导航、屏幕阅读器支持
- **国际化设置**：多语言支持的基本 i18n 结构
- **主题系统基础**：明暗模式切换实现
- **响应式设计模式**：带有断点系统的移动优先方法
- **动画框架集成**：Framer Motion 可实现平滑过渡

### 6. 文档
使用以下内容创建全面的 README.md：
- 先决条件和设置说明
- 认证及环境配置
- 连接器设置和数据源配置
- 本地开发和部署流程
- 常见问题故障排除

## 实施指南

### 需要提及的先决条件
- 带有 Power Platform Tools 扩展的 Visual Studio Code
- Node.js（LTS 版本 - 推荐 v18.x 或 v20.x）
- Git 用于版本控制
- Power Platform CLI (PAC CLI) - 最新版本
- 启用了代码应用的 Power Platform 环境（需要管理员设置）
- 面向最终用户的 Power Apps Premium 许可证
- Azure 帐户（如果使用 Azure SQL 或其他 Azure 连接器）

### 要包含的 PAC CLI 命令
- `pac auth create --environment {environment-id}` - 使用特定环境进行身份验证
- `pac env select --environment {environment-url}` - 选择目标环境
- `pac code init --displayName "App Name"` - 初始化代码应用程序项目
- `pac connection list` - 列出可用连接
- `pac code add-data-source -a {api-name} -c {connection-id}` - 添加连接器
- `pac code push` - 部署到 Power Platform

### 官方支持的连接器
通过设置示例重点关注这些官方支持的连接器：
- **SQL Server（包括 Azure SQL）**：完整的 CRUD 操作、存储过程
- **SharePoint**：文档库、列表和网站
- **Office 365 用户**：个人资料信息、用户照片、组成员身份
- **Office 365 组**：团队信息和协作
- **Azure 数据资源管理器**：分析和大数据查询
- **OneDrive for Business**：文件存储和共享
- **Microsoft Teams**：团队协作和通知
- **MSN Weather**：天气数据集成
- **微软翻译V2**：多语言翻译
- **Dataverse**：完整的 CRUD 操作、关系和业务逻辑

### 连接器集成示例
包括 Office 365 用户的工作示例：
```typescript
// Example: Get current user profile
const profile = await Office365UsersService.MyProfile_V2("id,displayName,jobTitle,userPrincipalName");

// Example: Get user photo
const photoData = await Office365UsersService.UserPhoto_V2(profile.data.id);
```

### 当前文档的限制
- 尚不支持内容安全策略 (CSP)
- 不支持存储 SAS IP 限制
- 没有 Power Platform Git 集成
- 不支持 Dataverse 解决方案
- 没有本机 Azure Application Insights 集成

### 包含的最佳实践
- 使用端口 3000 进行本地开发（Power Apps SDK 需要）
- 在 TypeScript 配置中设置 `verbatimModuleSyntax: false`
- 使用 `base: "./"` 和正确的路径别名配置 vite.config.ts
- 将敏感数据存储在数据源中，而不是应用程序代码中
- 遵循 Power Platform 托管平台政策
- 对连接器操作实施正确的错误处理
- 使用 PAC CLI 生成的 TypeScript 模型和服务
- 包括具有适当异步初始化和错误处理的 PowerProvider

## 可交付成果

1. 包含所有必要文件的完整项目脚手架
2. 具有连接器集成的工作示例应用程序
3. 全面的文档和设置说明
4. 开发和部署脚本
5. 针对 Power Apps 代码应用优化的 TypeScript 配置
6. 最佳实践实施示例

确保生成的项目遵循 Microsoft 官方 Power Apps Code Apps 文档和 https://github.com/microsoft/PowerAppsCodeApps 中的示例，并且可以使用 `pac code push` 命令成功部署到 Power Platform。


