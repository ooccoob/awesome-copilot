---
description: '全面的技术堆栈蓝图生成器，分析代码库以创建详细的架构文档。自动检测技术堆栈、编程语言和跨多个平台（.NET、Java、JavaScript、React、Python）的实现模式。生成带有版本信息、许可详细信息、使用模式、编码约定和可视化图表的可配置蓝图。提供实现就绪的模板并维护架构一致性以指导开发。'
mode: 'agent'
---

# 全面技术堆栈蓝图生成器

## 配置变量
${PROJECT_TYPE="自动检测|.NET|Java|JavaScript|React.js|React Native|Angular|Python|其他"} <!-- 主要技术 -->
${DEPTH_LEVEL="基础|标准|全面|实现就绪"} <!-- 分析深度 -->
${INCLUDE_VERSIONS=true|false} <!-- 包含版本信息 -->
${INCLUDE_LICENSES=true|false} <!-- 包含许可信息 -->
${INCLUDE_DIAGRAMS=true|false} <!-- 生成架构图表 -->
${INCLUDE_USAGE_PATTERNS=true|false} <!-- 包含代码使用模式 -->
${INCLUDE_CONVENTIONS=true|false} <!-- 记录编码约定 -->
${OUTPUT_FORMAT="Markdown|JSON|YAML|HTML"} <!-- 选择输出格式 -->
${CATEGORIZATION="技术类型|层|目的"} <!-- 组织方法 -->

## 生成的提示

"分析代码库并生成${DEPTH_LEVEL}技术堆栈蓝图，彻底记录技术和实现模式以促进一致的代码生成。使用以下方法：

### 1. 技术识别阶段
- ${PROJECT_TYPE == "自动检测" ? "扫描代码库的项目文件、配置文件和依赖项以确定所有使用的技术堆栈" : "专注于${PROJECT_TYPE}技术"}
- 通过检查文件扩展名和内容识别所有编程语言
- 分析配置文件（package.json、.csproj、pom.xml等）以提取依赖项
- 检查构建脚本和管道定义以获取工具信息
- ${INCLUDE_VERSIONS ? "从包文件和配置中提取精确的版本信息" : "跳过版本详情"}
- ${INCLUDE_LICENSES ? "记录所有依赖项的许可信息" : ""}

### 2. 核心技术分析

${PROJECT_TYPE == ".NET" || PROJECT_TYPE == "自动检测" ? "#### .NET堆栈分析（如果检测到）
- 从项目文件检测的目标框架和语言版本
- 所有NuGet包引用及版本和目的注释
- 项目结构和组织模式
- 配置方法（appsettings.json、IOptions等）
- 身份验证机制（Identity、JWT等）
- API设计模式（REST、GraphQL、最小API等）
- 数据访问方法（EF Core、Dapper等）
- 依赖注入模式
- 中间件管道组件" : ""}

${PROJECT_TYPE == "Java" || PROJECT_TYPE == "自动检测" ? "#### Java堆栈分析（如果检测到）
- JDK版本和核心框架
- 所有Maven/Gradle依赖项及版本和目的
- 包结构组织
- Spring Boot使用和配置
- 注解模式
- 依赖注入方法
- 数据访问技术（JPA、JDBC等）
- API设计（Spring MVC、JAX-RS等）" : ""}

${PROJECT_TYPE == "JavaScript" || PROJECT_TYPE == "自动检测" ? "#### JavaScript堆栈分析（如果检测到）
- ECMAScript版本和转译器设置
- 按目的分类的所有npm依赖项
- 模块系统（ESM、CommonJS）
- 构建工具（webpack、Vite等）及配置
- TypeScript使用和配置
- 测试框架和模式" : ""}

${PROJECT_TYPE == "React.js" || PROJECT_TYPE == "自动检测" ? "#### React分析（如果检测到）
- React版本和关键模式（hooks vs. 类组件）
- 状态管理方法（Context、Redux、Zustand等）
- 组件库使用（Material-UI、Chakra等）
- 路由实现
- 表单处理策略
- API集成模式
- 组件测试方法" : ""}

${PROJECT_TYPE == "Python" || PROJECT_TYPE == "自动检测" ? "#### Python分析（如果检测到）
- Python版本和使用的关键语言特性
- 包依赖项和虚拟环境设置
- Web框架详细信息（Django、Flask、FastAPI）
- ORM使用模式
- 项目结构组织
- API设计模式" : ""}

### 3. 实现模式和约定
${INCLUDE_CONVENTIONS ?
"记录每个技术领域的编码约定和模式：

#### 命名约定
- 类/类型命名模式
- 方法/函数命名模式
- 变量命名约定
- 文件命名和组织约定
- 接口/抽象类模式

#### 代码组织
- 文件结构和组织
- 文件夹层次模式
- 组件/模块边界
- 代码分离和职责模式

#### 常见模式
- 错误处理方法
- 日志记录模式
- 配置访问
- 身份验证/授权实现
- 验证策略
- 测试模式" : ""}

### 4. 使用示例
${INCLUDE_USAGE_PATTERNS ?
"提取显示标准实现模式的代表性代码示例：

#### API实现示例
- 标准控制器/端点实现
- 请求DTO模式
- 响应格式化
- 验证方法
- 错误处理

#### 数据访问示例
- 存储库模式实现
- 实体/模型定义
- 查询模式
- 事务处理

#### 服务层示例
- 服务类实现
- 业务逻辑组织
- 横切关注点集成
- 依赖注入使用

#### UI组件示例（如果适用）
- 组件结构
- 状态管理模式
- 事件处理
- API集成模式" : ""}

### 5. 技术堆栈映射
${DEPTH_LEVEL == "全面" || DEPTH_LEVEL == "实现就绪" ?
"创建包含以下内容的全面技术映射：

#### 核心框架使用
- 项目中使用的主要框架及其特定用途
- 框架特定的配置和自定义
- 扩展点和自定义

#### 集成点
- 不同技术组件如何集成
- 组件间的身份验证流
- 前端和后端间的数据流
- 第三方服务集成模式

#### 开发工具
- IDE设置和约定
- 代码分析工具
- 带配置的代码检查器和格式化器
- 构建和部署管道
- 测试框架和方法

#### 基础设施
- 部署环境详细信息
- 容器技术
- 使用的云服务
- 监控和日志记录基础设施" : ""}

### 6. 技术特定实现细节

${PROJECT_TYPE == ".NET" || PROJECT_TYPE == "自动检测" ?
"#### .NET实现细节（如果检测到）
- **依赖注入模式**：
  - 服务注册方法（Scoped/Singleton/Transient模式）
  - 配置绑定模式

- **控制器模式**：
  - 基控制器使用
  - 操作结果类型和模式
  - 路由属性约定
  - 过滤器使用（授权、验证等）

- **数据访问模式**：
  - ORM配置和使用
  - 实体配置方法
  - 关系定义
  - 查询模式和优化方法

- **API设计模式**（如果使用）：
  - 端点组织
  - 参数绑定方法
  - 响应类型处理

- **使用的语言特性**：
  - 从代码检测特定语言特性
  - 识别常见模式和习惯用法
  - 注意任何特定于版本的特性" : ""}

${PROJECT_TYPE == "React.js" || PROJECT_TYPE == "自动检测" ?
"#### React实现细节（如果检测到）
- **组件结构**：
  - 函数vs.类组件
  - Props接口定义
  - 组件组合模式

- **Hook使用模式**：
  - 自定义Hook实现风格
  - useState模式
  - useEffect清理方法
  - Context使用模式

- **状态管理**：
  - 本地vs.全局状态决策
  - 状态管理库模式
  - 存储配置
  - 选择器模式

- **样式方法**：
  - CSS方法论（CSS模块、styled-components等）
  - 主题实现
  - 响应式设计模式" : ""}

### 7. 新代码实现的蓝图
${DEPTH_LEVEL == "实现就绪" ?
"基于分析，提供实施新功能的详细蓝图：

- **文件/类模板**：常见组件类型的标准结构
- **代码片段**：常见操作的即用型代码模式
- **实现检查清单**：端到端实施功能的标准步骤
- **集成点**：如何将新代码与现有系统连接
- **测试要求**：不同组件类型的标准测试模式
- **文档要求**：新功能的标准文档模式" : ""}

${INCLUDE_DIAGRAMS ?
"### 8. 技术关系图表
- **堆栈图表**：完整技术堆栈的可视化表示
- **依赖流**：不同技术如何交互
- **组件关系**：主要组件如何相互依赖
- **数据流**：数据如何流经技术堆栈" : ""}

### ${INCLUDE_DIAGRAMS ? "9" : "8"}. 技术决策上下文
- 记录技术选择的明显原因
- 注意标记为替换的任何遗留或弃用技术
- 识别技术约束和边界
- 记录技术升级路径和兼容性考虑

以${OUTPUT_FORMAT}格式输出，并按${CATEGORIZATION}分类技术。

将输出保存为'Technology_Stack_Blueprint.${OUTPUT_FORMAT == "Markdown" ? "md" : OUTPUT_FORMAT.toLowerCase()}'
"