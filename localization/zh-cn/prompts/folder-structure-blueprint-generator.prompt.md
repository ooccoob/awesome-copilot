```prompt
---
description: '面向多技术栈的项目目录结构分析与蓝图生成提示词。可自动识别项目类型（.NET、Java、React、Angular、Python、Node.js、Flutter），生成包含可视化选项、命名约定、文件放置模式与可扩展模板的详细蓝图，以维持跨栈一致的代码组织。'
---

# 项目目录结构蓝图生成器

## 配置变量

${PROJECT_TYPE="Auto-detect|.NET|Java|React|Angular|Python|Node.js|Flutter|Other"}
<!-- 选择主要技术栈 -->

${INCLUDES_MICROSERVICES="Auto-detect|true|false"}
<!-- 是否为微服务架构 -->

${INCLUDES_FRONTEND="Auto-detect|true|false"}
<!-- 是否包含前端组件 -->

${IS_MONOREPO="Auto-detect|true|false"}
<!-- 是否为包含多个项目的 monorepo -->

${VISUALIZATION_STYLE="ASCII|Markdown List|Table"}
<!-- 目录可视化风格 -->

${DEPTH_LEVEL=1-5}
<!-- 详细展开的目录层级数 -->

${INCLUDE_FILE_COUNTS=true|false}
<!-- 是否包含文件数统计 -->

${INCLUDE_GENERATED_FOLDERS=true|false}
<!-- 是否包含自动生成的目录 -->

${INCLUDE_FILE_PATTERNS=true|false}
<!-- 是否记录文件命名/放置模式 -->

${INCLUDE_TEMPLATES=true|false}
<!-- 是否附带新建功能/组件/服务等模板 -->

## 生成提示

"请分析该项目的目录结构并创建一份权威的 'Project_Folders_Structure_Blueprint.md' 文档，用作维持一致代码组织的基准指南。遵循以下方法：

### 初始自动识别阶段

${PROJECT_TYPE == "Auto-detect" ?
"扫描目录以识别项目类型的关键文件：
- 通过解决方案/项目文件（.sln, .csproj, .fsproj, .vbproj）识别 .NET 项目
- 通过构建文件（pom.xml, build.gradle, settings.gradle）识别 Java 项目
- 通过 package.json 及依赖识别 JS/TS 项目
- 检查框架特征文件（angular.json、react-scripts、next.config.js 等）
- 检查 Python 标识（requirements.txt、setup.py、pyproject.toml）
- 检查移动端标识（pubspec.yaml、android/ios 目录）
- 记录所有发现的技术栈标识及版本" :
"聚焦于 ${PROJECT_TYPE} 项目结构"}

${IS_MONOREPO == "Auto-detect" ?
"判断是否为 monorepo：
- 是否存在多个独立项目（各自配置文件）
- 是否存在工作区配置（lerna.json、nx.json、turborepo.json 等）
- 是否存在跨项目引用与共享依赖
- 根层是否有统一编排脚本与配置" : ""}

${INCLUDES_MICROSERVICES == "Auto-detect" ?
"检查微服务架构特征：
- 多个服务目录且结构相似/重复
- 各服务是否有独立 Dockerfile 或部署配置
- 服务间通信（API、消息队列）
- 服务注册/发现配置
- API 网关配置
- 跨服务共享库/工具" : ""}

${INCLUDES_FRONTEND == "Auto-detect" ?
"识别前端组件：
- Web 资源目录（wwwroot、public、dist、static）
- UI 框架结构（components、modules、pages）
- 前端构建配置（webpack、vite、rollup 等）
- 样式组织（CSS、SCSS、styled-components）
- 静态资源（images、fonts、icons）的组织方式" : ""}

### 1. 结构总览

提供 ${PROJECT_TYPE == "Auto-detect" ? "已识别项目类型" : PROJECT_TYPE} 的高层组织原则与目录结构概览：

- 记录目录结构体现的总体架构思路
- 标注主要组织原则（按功能、按分层、按领域等）
- 记录代码库中重复出现的结构模式
- 在可推断的情况下补充结构设计的意图

${IS_MONOREPO == "Auto-detect" ?
"若识别为 monorepo，说明各项目的组织与相互关系。" :
IS_MONOREPO ? "说明 monorepo 的组织方式与项目关系。" : ""}

${INCLUDES_MICROSERVICES == "Auto-detect" ?
"若识别为微服务，描述服务的结构与组织方式。" :
INCLUDES_MICROSERVICES ? "描述微服务的结构与组织方式。" : ""}

### 2. 目录可视化

${VISUALIZATION_STYLE == "ASCII" ?
"以 ASCII 树形展示目录层级，深度为 ${DEPTH_LEVEL}。" : ""}

${VISUALIZATION_STYLE == "Markdown List" ?
"使用嵌套 Markdown 列表展示目录层级，深度为 ${DEPTH_LEVEL}。" : ""}

${VISUALIZATION_STYLE == "Table" ?
"以表格列出路径、用途、内容类型与约定。" : ""}

${INCLUDE_GENERATED_FOLDERS ?
"包含所有目录（含自动生成目录）。" :
"排除自动生成目录（如 bin/、obj/、node_modules/ 等）。"}

### 3. 关键目录分析

逐个记录重要目录的用途、内容与模式：

${PROJECT_TYPE == "Auto-detect" ?
"针对每种识别出的技术栈，按观察到的使用模式分析目录结构：" : ""}

${(PROJECT_TYPE == ".NET" || PROJECT_TYPE == "Auto-detect") ?
"#### .NET 项目结构（如识别到）

- **解决方案组织**：
  - 项目分组与关联
  - 解决方案文件夹组织模式
  - 多目标框架的项目模式

- **项目组织**：
  - 内部目录结构模式
  - 源码组织方法
  - 资源组织
  - 项目依赖与引用

- **领域/特性组织**：
  - 业务领域/功能的划分
  - 领域边界的约束模式

- **分层组织**：
  - 关注点分离（Controllers、Services、Repositories 等）
  - 分层间的依赖与交互

- **配置管理**：
  - 配置文件位置与用途
  - 环境配置划分
  - 机密管理策略

- **测试项目组织**：
  - 测试项目结构与命名
  - 测试类别组织
  - 测试数据与 mock 存放" : ""}

${(PROJECT_TYPE == "React" || PROJECT_TYPE == "Angular" || PROJECT_TYPE == "Auto-detect") ?
"#### UI 项目结构（如识别到）

- **组件组织**：
  - 组件目录结构模式
  - 分组策略（按功能、类型等）
  - 公共组件与特性组件

- **状态管理**：
  - 状态相关文件组织
  - 全局状态 store 结构
  - 本地状态模式

- **路由组织**：
  - 路由定义位置
  - 页面/视图组件组织
  - 路由参数管理

- **API 集成**：
  - API 客户端组织
  - 服务层结构
  - 数据获取模式

- **资源管理**：
  - 静态资源组织
  - 图片/媒体目录结构
  - 字体与图标管理

- **样式组织**：
  - CSS/SCSS 目录
  - 主题组织
  - 样式模块模式" : ""}

### 4. 文件放置模式

${INCLUDE_FILE_PATTERNS ?
"记录各类型文件应如何放置：

- **配置文件**：
  - 各类配置的存放位置
  - 按环境划分的配置模式

- **模型/实体定义**：
  - 领域模型位置
  - DTO 的位置
  - 模式/Schema 的位置

- **业务逻辑**：
  - 服务实现位置
  - 业务规则组织
  - 工具与辅助函数

- **接口定义**：
  - 接口与抽象的存放
  - 接口的分组与组织

- **测试文件**：
  - 单元测试位置模式
  - 集成测试放置
  - 测试工具与 mock

- **文档文件**：
  - API 文档位置
  - 内部文档组织
  - README 分布" :
"说明关键文件类型在项目中的位置。"}

### 5. 命名与组织约定
记录在全项目观察到的命名与组织约定：

- **文件命名**：
  - 大小写风格（PascalCase、camelCase、kebab-case）
  - 前后缀模式
  - 文件名中的类型标识

- **目录命名**：
  - 不同目录类型的命名约定
  - 层级命名模式
  - 分组与归类约定

- **命名空间/模块模式**：
  - 命名空间/模块与目录的对应关系
  - import/using 组织
  - 内部与公共 API 的边界

- **组织模式**：
  - 代码共址策略
  - 特性封装方法
  - 横切关注点的组织

### 6. 导航与开发工作流
给出在该结构下进行开发的导航建议：

- **入口点**：
  - 应用入口文件
  - 关键配置起点
  - 初学者阅读路径

- **常见开发任务**：
  - 新增功能应放何处
  - 扩展现有能力的方式
  - 新增测试放置位置
  - 修改配置的位置

- **依赖模式**：
  - 目录间依赖的流向
  - import/引用模式
  - 依赖注入注册位置

${INCLUDE_FILE_COUNTS ?
"- **内容统计**：
  - 每目录文件数量
  - 代码分布指标
  - 复杂度集中区域" : ""}

### 7. 构建与产物组织
描述构建流程与产物结构：

- **构建配置**：
  - 构建脚本位置与作用
  - 构建流水线组织
  - 构建任务定义

- **产物结构**：
  - 编译/构建输出位置
  - 产物组织模式
  - 分发包结构

- **环境差异**：
  - 开发/生产的差异
  - 环境配置策略
  - 构建变体组织

### 8. 技术栈特定组织

${(PROJECT_TYPE == ".NET" || PROJECT_TYPE == "Auto-detect") ?
"#### .NET 特定结构模式（如识别到）

- **项目文件组织**：
  - 项目文件结构与模式
  - 目标框架配置
  - PropertyGroup 组织
  - ItemGroup 模式

- **程序集组织**：
  - 程序集命名
  - 多程序集架构
  - 程序集引用模式

- **资源组织**：
  - 内嵌资源
  - 本地化文件结构
  - 静态 Web 资源

- **包管理**：
  - NuGet 配置位置
  - 包引用组织
  - 版本管理" : ""}

${(PROJECT_TYPE == "Java" || PROJECT_TYPE == "Auto-detect") ?
"#### Java 特定结构模式（如识别到）

- **包层级**：
  - 包的命名与嵌套
  - 领域与技术包的划分
  - 可见性与访问模式

- **构建工具组织**：
  - Maven/Gradle 结构
  - 模块组织
  - 插件配置模式

- **资源组织**：
  - 资源目录结构
  - 按环境划分的资源
  - Properties 文件组织" : ""}

${(PROJECT_TYPE == "Node.js" || PROJECT_TYPE == "Auto-detect") ?
"#### Node.js 特定结构模式（如识别到）

- **模块组织**：
  - CommonJS 与 ESM 的组织
  - 内部模块模式
  - 第三方依赖管理

- **脚本组织**：
  - npm/yarn 脚本模式
  - 工具脚本位置
  - 开发工具脚本

- **配置管理**：
  - 配置文件位置
  - 环境变量管理
  - 机密管理方法" : ""}

### 9. 扩展与演进
说明如何在保持约定的前提下扩展结构：

- **扩展点**：
  - 如何新增模块/功能
  - 插件/扩展目录模式
  - 自定义目录结构

- **可扩展性模式**：
  - 面向大型特性的扩展方式
  - 拆分大型模块的方法
  - 代码分片策略

- **重构模式**：
  - 常见重构做法
  - 结构变更的管理
  - 渐进式重组模式

${INCLUDE_TEMPLATES ?
"### 10. 结构模板

为遵循项目约定的新建组件提供模板：

- **新增功能模板**：
  - 新功能的目录骨架
  - 必需文件及位置
  - 命名模式

- **新增组件模板**：
  - 典型组件的目录
  - 必备文件
  - 与现有结构的集成点

- **新增服务模板**：
  - 新服务的结构
  - 接口与实现位置
  - 配置与注册

- **测试结构模板**：
  - 测试项目/文件的目录
  - 测试文件组织模板
  - 测试资源组织" : ""}

### ${INCLUDE_TEMPLATES ? "11" : "10"}. 结构约束与治理

记录结构的维持与约束方式：

- **结构校验**：
  - 强制结构的工具/脚本
  - 构建中的结构合规检查
  - 与结构相关的 lint 规则

- **文档实践**：
  - 如何记录结构变更
  - 在何处记录架构决策
  - 结构演进历史

最后请包含一节“如何维护本蓝图”与“最近更新时间”。
"

---

**免责声明**：本文件由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 自动本地化，可能存在不准确之处。若发现不当或错误翻译，请提交 [Issue](https://github.com/ooccoob/datafill/issues) 进行反馈。
```
