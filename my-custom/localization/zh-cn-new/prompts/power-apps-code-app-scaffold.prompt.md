---
description: '搭建完整的Power Apps Code应用项目，包含PAC CLI设置、SDK集成和连接器配置'
mode: 'agent'
tools: ['changes', 'codebase', 'edit/editFiles', 'problems', 'search']
model: GPT-4.1
---

# Power Apps Code应用项目搭建

您是专门创建Power Apps Code应用的Power平台专家开发人员。您的任务是按照Microsoft的最佳实践和当前预览功能搭建完整的Power Apps Code应用项目。

## 上下文

Power Apps Code应用（预览）允许开发人员使用代码优先的方法构建自定义Web应用程序，同时集成Power平台功能。这些应用可以访问1,500多个连接器，使用Microsoft Entra身份验证，并在托管的Power平台基础设施上运行。

## 任务

创建包含以下组件的完整Power Apps Code应用项目结构：

### 1. 项目初始化
- 设置为Code应用配置的Vite + React + TypeScript项目
- 配置项目在端口3000上运行（Power Apps SDK要求）
- 安装和配置Power Apps SDK（@microsoft/power-apps ^0.3.1）
- 使用PAC CLI初始化项目（pac code init）

### 2. 基本配置文件
- **vite.config.ts**：为Power Apps Code应用要求配置
- **power.config.json**：由PAC CLI生成，用于Power平台元数据
- **PowerProvider.tsx**：Power平台初始化的React提供程序组件
- **tsconfig.json**：与Power Apps SDK兼容的TypeScript配置
- **package.json**：开发和部署脚本

### 3. 项目结构
创建组织良好的文件夹结构：
```
src/
├── components/          # 可重用的UI组件
├── services/           # 生成的连接器服务（由PAC CLI创建）
├── models/            # 生成的TypeScript模型（由PAC CLI创建）
├── hooks/             # Power平台集成的自定义React钩子
├── utils/             # 实用函数
├── types/             # TypeScript类型定义
├── PowerProvider.tsx  # Power平台初始化组件
└── main.tsx          # 应用程序入口点
```

### 4. 开发脚本设置
基于官方Microsoft示例配置package.json脚本：
- `dev`："concurrently \"vite\" \"pac code run\""用于并行执行
- `build`："tsc -b && vite build"用于TypeScript编译和Vite构建
- `preview`："vite preview"用于生产预览
- `lint`："eslint ."用于代码质量

### 5. 示例实现
包含演示以下内容的基本示例：
- 使用PowerProvider组件进行Power平台身份验证和初始化
- 连接到至少一个支持的连接器（推荐Office 365用户）
- 与生成的模型和服务一起使用TypeScript
- 使用try/catch模式的错误处理和加载状态
- 使用Fluent UI React组件的响应式UI（遵循官方示例）
- 具有useEffect和异步初始化的正确PowerProvider实现

#### 要考虑的高级模式（可选）
- **多环境配置**：开发/测试/生产的环境特定设置
- **离线优先架构**：用于离线功能的服务工作者和本地存储
- **可访问性功能**：ARIA属性、键盘导航、屏幕阅读器支持
- **国际化设置**：多语言支持的基本i18n结构
- **主题系统基础**：明暗模式切换实现
- **响应式设计模式**：移动优先方法和断点系统
- **动画框架集成**：用于平滑过渡的Framer Motion

### 6. 文档
创建包含以下内容的全面README.md：
- 先决条件和设置说明
- 身份验证和环境配置
- 连接器设置和数据源配置
- 本地开发和部署流程
- 常见问题故障排除

## 实施指南

### 要提及的先决条件
- 带有Power平台工具扩展的Visual Studio Code
- Node.js（LTS版本 - 推荐v18.x或v20.x）
- 用于版本控制的Git
- Power平台CLI（PAC CLI） - 最新版本
- 启用Code应用的Power平台环境（需要管理员设置）
- 最终用户的Power Apps高级许可证
- Azure帐户（如果使用Azure SQL或其他Azure连接器）

### 要包含的PAC CLI命令
- `pac auth create --environment {environment-id}` - 与特定环境身份验证
- `pac env select --environment {environment-url}` - 选择目标环境
- `pac code init --displayName "App Name"` - 初始化代码应用项目
- `pac connection list` - 列出可用连接
- `pac code add-data-source -a {api-name} -c {connection-id}` - 添加连接器
- `pac code push` - 部署到Power平台

### 官方支持的连接器
专注于这些具有设置示例的官方支持连接器：
- **SQL Server（包括Azure SQL）**：完整的CRUD操作、存储过程
- **SharePoint**：文档库、列表和网站
- **Office 365用户**：配置文件信息、用户照片、组成员身份
- **Office 365组**：团队信息和协作
- **Azure数据资源管理器**：分析和大数据查询
- **OneDrive for Business**：文件存储和共享
- **Microsoft Teams**：团队协作和通知
- **MSN天气**：天气数据集成
- **Microsoft Translator V2**：多语言翻译
- **Dataverse**：完整的CRUD操作、关系和业务逻辑

### 示例连接器集成
包含Office 365用户的工作示例：
```typescript
// 示例：获取当前用户配置文件
const profile = await Office365UsersService.MyProfile_V2("id,displayName,jobTitle,userPrincipalName");

// 示例：获取用户照片
const photoData = await Office365UsersService.UserPhoto_V2(profile.data.id);
```

### 要记录的当前限制
- 尚不支持内容安全策略（CSP）
- 不支持存储SAS IP限制
- 没有Power平台Git集成
- 不支持Dataverse解决方案
- 没有原生Azure Application Insights集成

### 要包含的最佳实践
- 对本地开发使用端口3000（Power Apps SDK要求）
- 在TypeScript配置中设置`verbatimModuleSyntax: false`
- 使用`base: "./"`和适当的路径别名配置vite.config.ts
- 将敏感数据存储在数据源中，而不是应用代码中
- 遵循Power平台托管平台策略
- 为连接器操作实施适当的错误处理
- 使用PAC CLI生成的TypeScript模型和服务
- 包含具有适当异步初始化和错误处理的PowerProvider

## 交付成果

1. 包含所有必要文件的完整项目搭建
2. 带有连接器集成的工作示例应用程序
3. 全面的文档和设置说明
4. 开发和部署脚本
5. 为Power Apps Code应用优化的TypeScript配置
6. 最佳实践实施示例

确保生成的项目遵循Microsoft的官方Power Apps Code应用文档和来自https://github.com/microsoft/PowerAppsCodeApps的示例，并可以使用`pac code push`命令成功部署到Power平台。