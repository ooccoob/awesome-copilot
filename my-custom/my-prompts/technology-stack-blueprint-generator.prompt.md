---
description: 'Comprehensive technology stack blueprint generator that analyzes codebases to create detailed architectural documentation. Automatically detects technology stacks, programming languages, and implementation patterns across multiple platforms (.NET, Java, JavaScript, React, Python). Generates configurable blueprints with version information, licensing details, usage patterns, coding conventions, and visual diagrams. Provides implementation-ready templates and maintains architectural consistency for guided development.'
agent: 'agent'
---

# 全面的技术堆栈蓝图生成器

## 配置变量
${PROJECT_TYPE="Auto-detect|.NET|Java|JavaScript|React.js|React Native|Angular|Python|Other"} <!-- 主要技术 -->
${DEPTH_LEVEL="Basic|Standard|Compressive|Implementation-Ready"} <!-- 分析深度 -->
${INCLUDE_VERSIONS=true|false} <!-- 包含版本信息-->
${INCLUDE_LICENSES=true|false} <!-- 包含许可证信息 -->
${INCLUDE_DIAGRAMS=true|false} <!-- 生成架构图 -->
${INCLUDE_USAGE_PATTERNS=true|false} <!-- 包含代码使用模式 -->
${INCLUDE_CONVENTIONS=true|false} <!-- 文档编码约定 -->
${OUTPUT_FORMAT="Markdown|JSON|YAML|HTML"} <!-- 选择输出格式 -->
${CATEGORIZATION="技术类型|层次|目的"} <!-- 组织方式 -->

## 生成的提示

“分析代码库并生成 ${DEPTH_LEVEL} 技术堆栈蓝图，该蓝图彻底记录技术和实现模式，以促进一致的代码生成。使用以下方法：

### 1.技术鉴定阶段
- ${PROJECT_TYPE == “自动检测”？ “扫描代码库中的项目文件、配置文件和依赖项，以确定正在使用的所有技术堆栈”：“关注 ${PROJECT_TYPE} 技术”}
- 通过检查文件扩展名和内容来识别所有编程语言
- 分析配置文件（package.json、.csproj、pom.xml等）以提取依赖项
- 检查构建脚本和管道定义以获取工具信息
- ${INCLUDE_VERSIONS ？ "从包文件和配置中提取精确的版本信息" : "跳过版本详细信息"}
- ${INCLUDE_LICENSES ？ “记录所有依赖项的许可证信息”：“”}

### 2、核心技术分析

${PROJECT_TYPE == ".NET" || PROJECT_TYPE ==“自动检测”？ “#### .NET 堆栈分析（如果检测到）
- 目标框架和语言版本（从项目文件中检测）
- 所有 NuGet 包引用以及版本和用途注释
- 项目结构和组织模式
- 配置方式（appsettings.json、IOptions等）
- 身份验证机制（Identity、JWT 等）
- API 设计模式（REST、GraphQL、最小 API 等）
- 数据访问方法（EF Core、Dapper 等）
- 依赖注入模式
- 中间件管道组件" : ""}

${PROJECT_TYPE == "Java" || PROJECT_TYPE ==“自动检测”？ “#### Java 堆栈分析（如果检测到）
- JDK版本和核心框架
- 所有 Maven/Gradle 依赖项及其版本和用途
- 包结构组织
- Spring Boot 使用和配置
- 注释模式
- 依赖注入方法
- 数据访问技术（JPA、JDBC 等）
- API 设计（Spring MVC、JAX-RS 等）" : ""}

${PROJECT_TYPE == "JavaScript" || PROJECT_TYPE ==“自动检测”？ “#### JavaScript 堆栈分析（如果检测到）
- ECMAScript 版本和转译器设置
- 按用途分类的所有 npm 依赖项
- 模块系统（ESM、CommonJS）
- 使用配置构建工具（webpack、Vite 等）
- TypeScript 的使用和配置
- 测试框架和模式" : ""}

${PROJECT_TYPE == "React.js" || PROJECT_TYPE ==“自动检测”？ “#### 反应分析（如果检测到）
- React 版本和关键模式（钩子与类组件）
- 状态管理方法（Context、Redux、Zustand 等）
- 组件库使用（Material-UI、Chakra等）
- 路由实现
- 表单处理策略
- API集成模式
- 组件测试方法" : ""}

${PROJECT_TYPE == "Python" || PROJECT_TYPE ==“自动检测”？ “#### Python 分析（如果检测到）
- Python 版本和使用的主要语言功能
- 包依赖关系和虚拟环境设置
- Web 框架详细信息（Django、Flask、FastAPI）
- ORM 使用模式
- 项目结构组织
- API 设计模式" : ""}

### 3. 实施模式和惯例
${INCLUDE_CONVENTIONS ？ 
“每个技术领域的文档编码约定和模式：

#### 命名约定
- 类/类型命名模式
- 方法/函数命名模式
- 变量命名约定
- 文件命名和组织约定
- 接口/抽象类模式

#### 代码组织
- 文件结构和组织
- 文件夹层次结构模式
- 组件/模块边界
- 代码分离和责任模式

#### 常见模式
- 错误处理方法
- 记录模式
- 配置访问
- 认证/授权实现
- 验证策略
- 测试模式" : ""}

### 4. 使用示例
${INCLUDE_USAGE_PATTERNS ？ 
“提取显示标准实现模式的代表性代码示例：

#### API实现示例
- 标准控制器/端点实施
- 请求 DTO 模式
- 响应格式
- 验证方法
- 错误处理

#### 数据访问示例
- 存储库模式实现
- 实体/模型定义
- 查询模式
- 交易处理

#### 服务层示例
- 服务类实现
- 业务逻辑组织
- 跨领域关注点整合
- 依赖注入使用

#### UI 组件示例（如果适用）
- 组件结构
- 状态管理模式
- 事件处理
- API 集成模式" : ""}

### 5. 技术栈图
${DEPTH_LEVEL == "全面" || DEPTH_LEVEL ==“实施就绪”？ 
“创建一个全面的技术地图，包括：

#### 核心框架使用
- 主要框架及其在项目中的具体用途
- 特定于框架的配置和定制
- 扩展点和自定义

#### 整合点
- 不同技术组件如何集成
- 组件之间的身份验证流程
- 前端和后端之间的数据流
- 第三方服务集成模式

#### 开发工具
- IDE 设置和约定
- 代码分析工具
- 带配置的 Linters 和格式化程序
- 构建和部署管道
- 测试框架和方法

#### 基础设施
- 部署环境详情
- 容器技术
- 使用的云服务
- 监控和记录基础设施" : ""}

### 6. 特定技术的实施细节

${PROJECT_TYPE == ".NET" || PROJECT_TYPE ==“自动检测”？ 
“#### .NET 实现详细信息（如果检测到）
- **依赖注入模式**：
  - 服务注册方法（Scoped/Singleton/Transient 模式）
  - 配置绑定模式
  
- **控制器模式**：
  - 基本控制器使用
  - 行动结果类型和模式
  - 路由属性约定
  - 过滤器使用（授权、验证等）
  
- **数据访问模式**：
  - ORM配置和使用
  - 实体配置方式
  - 关系定义
  - 查询模式和优化方法
  
- **API 设计模式**（如果使用）：
  - 端点组织
  - 参数绑定方法
  - 响应类型处理
  
- **使用的语言特征**：
  - 从代码中检测特定语言功能
  - 识别常见模式和习语
  - 请注意任何特定版本相关的功能" : ""}

${PROJECT_TYPE == "React.js" || PROJECT_TYPE ==“自动检测”？ 
“#### React 实现细节（如果检测到）
- **组件结构**：
  - 函数与类组件
  - Props 接口定义
  - 组件构成模式
  
- **挂钩使用模式**：
  - 自定义钩子实现风格
  - 使用状态模式
  - useEffect 清理方法
  - 上下文使用模式
  
- **状态管理**：
  - 本地与全球国家决策
  - 状态管理库模式
  - 店铺配置
  - 选择器模式
  
- **造型方法**：
  - CSS 方法论（CSS 模块、样式组件等）
  - 主题实施
  - 响应式设计模式" : ""}

### 7. 新代码实施蓝图
${DEPTH_LEVEL ==“实施就绪”？ 
“根据分析，提供实现新功能的详细蓝图：

- **文件/类模板**：常见组件类型的标准结构
- **代码片段**：常见操作的现成代码模式
- **实施清单**：端到端实施功能的标准步骤
- **集成点**：如何将新代码与现有系统连接
- **测试要求**：不同组件类型的标准测试模式
- **文档要求**：新功能的标准文档模式" : ""}

${INCLUDE_DIAGRAMS ？ 
“### 8.技术关系图
- **堆栈图**：完整技术堆栈的可视化表示
- **依赖流**：不同技术如何交互
- **组件关系**：主要组件如何相互依赖
- **数据流**：数据如何流经技术栈" : ""}

### ${INCLUDE_DIAGRAMS ？ “9”：“8”}。技术决策背景
- 记录技术选择的明显原因
- 记下任何标记为替换的遗留或已弃用的技术
- 确定技术限制和边界
- 记录技术升级路径和兼容性注意事项

将输出格式化为 ${OUTPUT_FORMAT} 并按 ${CATEGORIZATION} 对技术进行分类。

将输出保存为 'Technology_Stack_Blueprint.${OUTPUT_FORMAT == "Markdown" ？ “md”：OUTPUT_FORMAT.toLowerCase()}'
"