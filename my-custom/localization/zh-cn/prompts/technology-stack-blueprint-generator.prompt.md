---
description: '综合技术栈蓝图生成器：分析代码库以生成详尽的架构化文档。可自动检测多平台（.NET、Java、JavaScript、React、Python）的技术栈、语言与实现模式；生成可配置蓝图（含版本、许可、用法、规范与图示），并提供可落地模板以保持架构一致性。'
---

# 综合技术栈蓝图生成器

## 配置变量
${PROJECT_TYPE="Auto-detect|.NET|Java|JavaScript|React.js|React Native|Angular|Python|Other"} <!-- 主技术方向 -->
${DEPTH_LEVEL="Basic|Standard|Comprehensive|Implementation-Ready"} <!-- 分析深度 -->
${INCLUDE_VERSIONS=true|false} <!-- 是否包含版本信息 -->
${INCLUDE_LICENSES=true|false} <!-- 是否包含许可信息 -->
${INCLUDE_DIAGRAMS=true|false} <!-- 是否生成架构图 -->
${INCLUDE_USAGE_PATTERNS=true|false} <!-- 是否包含用法模式 -->
${INCLUDE_CONVENTIONS=true|false} <!-- 是否记录编码规范 -->
${OUTPUT_FORMAT="Markdown|JSON|YAML|HTML"} <!-- 输出格式 -->
${CATEGORIZATION="Technology Type|Layer|Purpose"} <!-- 分类方式 -->

## 生成的 Prompt

```markdown
"分析代码库并生成一份 ${DEPTH_LEVEL} 的技术栈蓝图，完整记录技术与实现模式，以支持一致性的代码生成。采用如下方法：

### 1. 技术识别阶段
- ${PROJECT_TYPE == "Auto-detect" ? "扫描项目/配置文件与依赖以识别所用技术栈" : "聚焦 ${PROJECT_TYPE} 技术"}
- 通过扩展名与内容识别所有编程语言
- 分析配置文件（package.json、.csproj、pom.xml 等）提取依赖
- 检查构建脚本与流水线定义以识别工具
- ${INCLUDE_VERSIONS ? "从包/配置文件提取精确版本信息" : "跳过版本信息"}
- ${INCLUDE_LICENSES ? "记录所有依赖的许可证信息" : ""}

### 2. 核心技术分析

${PROJECT_TYPE == ".NET" || PROJECT_TYPE == "Auto-detect" ? "#### .NET 栈（如检测到）
- 目标框架与语言版本
- NuGet 依赖（带版本与用途说明）
- 项目结构与组织模式
- 配置方式（appsettings.json、IOptions 等）
- 认证机制（Identity、JWT 等）
- API 设计（REST、GraphQL、Minimal API 等）
- 数据访问（EF Core、Dapper 等）
- 依赖注入模式
- 中间件管线组成" : ""}

${PROJECT_TYPE == "Java" || PROJECT_TYPE == "Auto-detect" ? "#### Java 栈（如检测到）
- JDK 版本与核心框架
- Maven/Gradle 依赖（含版本与用途）
- 包结构组织
- Spring Boot 使用与配置
- 注解模式
- 依赖注入方案
- 数据访问（JPA、JDBC 等）
- API 设计（Spring MVC、JAX-RS 等）" : ""}

${PROJECT_TYPE == "JavaScript" || PROJECT_TYPE == "Auto-detect" ? "#### JavaScript 栈（如检测到）
- ECMAScript 版本与转译配置
- npm 依赖按用途分类
- 模块系统（ESM、CommonJS）
- 构建工具（webpack、Vite 等）与配置
- TypeScript 使用与配置
- 测试框架与模式" : ""}

${PROJECT_TYPE == "React.js" || PROJECT_TYPE == "Auto-detect" ? "#### React（如检测到）
- React 版本与关键模式（Hooks vs Class）
- 状态管理（Context、Redux、Zustand 等）
- 组件库（MUI、Chakra 等）
- 路由
- 表单处理策略
- API 集成模式
- 组件测试方法" : ""}

${PROJECT_TYPE == "Python" || PROJECT_TYPE == "Auto-detect" ? "#### Python（如检测到）
- Python 版本与关键语言特性
- 依赖与虚拟环境
- Web 框架（Django、Flask、FastAPI）
- ORM 使用模式
- 项目结构
- API 设计模式" : ""}

### 3. 实施模式与规范
${INCLUDE_CONVENTIONS ?
"记录各技术区域的编码规范与模式：

#### 命名规范
- 类/类型命名
- 方法/函数命名
- 变量命名
- 文件命名与组织
- 接口/抽象类型模式

#### 代码组织
- 文件结构
- 目录层次
- 组件/模块边界
- 职责分离

#### 通用模式
- 错误处理
- 日志
- 配置访问
- 认证/授权
- 校验策略
- 测试模式" : ""}

### 4. 用例示例
${INCLUDE_USAGE_PATTERNS ?
"提取具有代表性的代码示例：

#### API 实现
- 标准控制器/端点实现
- 请求 DTO 模式
- 响应格式
- 校验方法
- 错误处理

#### 数据访问
- 仓储模式实现
- 实体/模型定义
- 查询模式
- 事务处理

#### 服务层
- Service 类实现
- 业务逻辑组织
- 横切关注点
- 依赖注入

#### UI 组件（如适用）
- 组件结构
- 状态管理
- 事件处理
- API 集成" : ""}

### 5. 技术栈地图
${DEPTH_LEVEL == "Comprehensive" || DEPTH_LEVEL == "Implementation-Ready" ?
"绘制全面的技术地图：

#### 核心框架使用
- 主要框架与具体用法
- 框架配置与定制
- 扩展点

#### 集成点
- 组件间集成
- 认证流
- 前后端数据流
- 三方服务集成

#### 开发工具链
- IDE 约定
- 代码分析工具
- Linter/Formatter 配置
- 构建与部署流水线
- 测试框架与方法

#### 基础设施
- 部署环境
- 容器技术
- 云服务
- 监控与日志" : ""}

### 6. 技术特定实现细节

${PROJECT_TYPE == ".NET" || PROJECT_TYPE == "Auto-detect" ?
"#### .NET 实现细节（如检测到）
- 依赖注入
- 控制器模式与路由约定
- 数据访问/ORM 配置
- 关系定义与查询优化
- API 端点组织与参数绑定
- 语言特性与惯用法
" : ""}

${PROJECT_TYPE == "React.js" || PROJECT_TYPE == "Auto-detect" ?
"#### React 实现细节（如检测到）
- 组件结构与 Props 约定
- 自定义 Hook 风格
- useState/useEffect 模式
- Context 使用
- 状态管理库配置
- 样式方法与主题
- 响应式设计
" : ""}

### 7. 新代码实施蓝图
${DEPTH_LEVEL == "Implementation-Ready" ?
"基于分析输出：文件/类模板、常用片段、实施清单、集成点、测试与文档要求。" : ""}

${INCLUDE_DIAGRAMS ?
"### 8. 技术关系图
- 技术栈图
- 依赖关系
- 组件关系
- 数据流
" : ""}

### ${INCLUDE_DIAGRAMS ? "9" : "8"}. 技术决策背景
- 记录技术选型原因
- 识别遗留/弃用技术及迁移路径
- 边界与约束

将输出格式化为 ${OUTPUT_FORMAT}，并按 ${CATEGORIZATION} 分类；保存为 `Technology_Stack_Blueprint.${OUTPUT_FORMAT == "Markdown" ? "md" : OUTPUT_FORMAT.toLowerCase()}`
"
```
