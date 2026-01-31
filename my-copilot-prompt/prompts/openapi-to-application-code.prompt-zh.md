---
代理人：“代理人”
描述：“根据 OpenAPI 规范生成完整的、可用于生产的应用程序”
型号：“GPT-4.1”
工具：['代码库'，'编辑/编辑文件'，'搜索/代码库']
---

# 从 OpenAPI 规范生成应用程序

您的目标是使用活动框架的约定和最佳实践，根据 OpenAPI 规范生成完整的、可工作的应用程序。

## 输入要求

1. **OpenAPI 规范**：提供：
   - OpenAPI 规范的 URL（例如 `https://api.example.com/openapi.json`）
   - OpenAPI 规范的本地文件路径
   - 完整的OpenAPI规范内容直接粘贴

2. **项目详细信息**（如果规范中没有）：
   - 项目名称及描述
   - 目标框架和版本
   - 包/命名空间命名约定
   - 身份验证方法（如果 OpenAPI 中未指定）

## 生成过程

### 第 1 步：分析 OpenAPI 规范
- 验证 OpenAPI 规范的完整性和正确性
- 识别所有端点、HTTP 方法、请求/响应模式
- 提取身份验证要求和安全方案
- 注意数据模型关系和约束
- 标记任何歧义或不完整的定义

### 第 2 步：设计应用程序架构
- 规划适合框架的目录结构
- 按资源或域识别控制器/处理程序分组
- 设计业务逻辑的服务层组织
- 规划数据模型和实体关系
- 设计配置和初始化策略

### 第 3 步：生成应用程序代码
- 使用构建/包配置文件创建项目结构
- 从 OpenAPI 模式生成模型/DTO
- 使用路由映射生成控制器/处理程序
- 生成具有业务逻辑的服务层
- 生成存储库/数据访问层（如果适用）
- 添加错误处理、验证和日志记录
- 生成配置和启动代码

### 第 4 步：添加支持文件
- 为服务和控制器生成适当的单元测试
- 创建包含设置和运行说明的自述文件
- 添加.gitignore和环境配置模板
- 生成API文档文件
- 创建示例请求/集成测试

## 输出结构

生成的应用程序将包括：

```
project-name/
├── README.md                      # Setup and usage instructions
├── [build-config]                 # Framework-specific build files (pom.xml, build.gradle, package.json, etc.)
├── src/
│   ├── main/
│   │   ├── [language]/
│   │   │   ├── controllers/       # HTTP endpoint handlers
│   │   │   ├── services/          # Business logic
│   │   │   ├── models/            # Data models and DTOs
│   │   │   ├── repositories/      # Data access (if applicable)
│   │   │   └── config/            # Application configuration
│   │   └── resources/             # Configuration files
│   └── test/
│       ├── [language]/
│       │   ├── controllers/       # Controller tests
│       │   └── services/          # Service tests
│       └── resources/             # Test configuration
├── .gitignore
├── .env.example                   # Environment variables template
└── docker-compose.yml             # Optional: Docker setup (if applicable)
```

## 应用最佳实践

- **框架约定**：遵循特定于框架的命名、结构和模式
- **关注点分离**：控制器、服务和存储库的清晰层
- **错误处理**：全面的错误处理和有意义的响应
- **验证**：全程输入验证和模式验证
- **日志记录**：用于调试和监控的结构化日志记录
- **测试**：服务和控制器的单元测试
- **文档**：内联代码文档和设置说明
- **安全性**：根据 OpenAPI 规范实现身份验证/授权
- **可扩展性**：设计模式支持增长和维护

## 下一步

生成后：

1. 检查生成的代码结构并根据需要进行自定义
2. 根据框架要求安装依赖
3. 配置环境变量和数据库连接
4. 运行测试来验证生成的代码
5. 启动开发服务器
6. 使用提供的示例测试端点

## 需要时询问的问题

- 应用程序应该包含数据库/ORM 设置，还是仅包含内存/模拟数据？
- 您想要容器化的 Docker 配置吗？
- 身份验证应该是 JWT、OAuth2、API 密钥还是基本身份验证？
- 您需要集成测试还是只需要单元测试？
- 有什么具体的数据库技术偏好吗？
- API 是否应该包含分页、过滤和排序示例？
