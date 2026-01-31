# 🎯 代理技能

代理技能是独立的文件夹，其中包含说明和捆绑资源，可增强专门任务的 AI 功能。根据[客服人员技能规范](https://agentskills.io/specification)，每个技能都包含一个 `SKILL.md` 文件，其中包含客服人员按需加载的详细说明。

技能与其他原语的不同之处在于支持代理在执行专门任务时可以利用的捆绑资产（脚本、代码示例、参考数据）。
### 如何使用代理技能

**内含内容：**
- 每个技能都是一个包含 `SKILL.md` 指令文件的文件夹
- 技能可能包括帮助脚本、代码模板或参考数据
- 技能遵循代理技能规范以实现最大兼容性

**何时使用：**
- 技能非常适合受益于捆绑资源的复杂、可重复工作流程
- 当您需要代码模板、帮助实用程序或参考数据以及说明时，请使用技能
- 技能提供渐进式披露 - 仅在特定任务需要时加载

**用途：**
- 浏览下面的技能表以查找相关能力
- 将技能文件夹复制到本地技能目录
- 在提示中参考技能或让客服人员自动发现它们

|名称 |描述 |捆绑资产 |
| ---- | ----------- | -------------- |
| [代理评估](../skills/agentic-eval/SKILL-zh.md) |用于评估和改进人工智能代理输出的模式和技术。在以下情况下使用此技能：<br />- 实施自我批评和反思循环<br />- 为质量关键的生成构建评估器优化器管道<br />- 创建测试驱动的代码细化工作流程<br />- 设计基于评估准则或 LLM 作为法官的评估系统<br />- 向座席输出（代码、报告、分析）添加迭代改进<br />- 衡量和提高座席响应质量 |无 |
| [appinsights-instrumentation](../skills/appinsights-instrumentation/SKILL-zh.md) |检测 Web 应用程序以将有用的遥测数据发送到 Azure App Insights | `LICENSE.txt`<br />`examples/appinsights.bicep`<br />`references/ASPNETCORE.md`<br />`references/AUTO.md`<br />`references/NODEJS.md`<br />`references/PYTHON.md`<br />`scripts/appinsights.ps1` |
| [azure-部署-预检](../skills/azure-deployment-preflight/SKILL-zh.md) |对 Azure 的 Bicep 部署执行全面的预检验证，包括模板语法验证、假设分析和权限检查。在部署到 Azure 之前使用此技能来预览更改、识别潜在问题并确保部署成功。当用户提及部署到 Azure、验证 Bicep 文件、检查部署权限、预览基础结构更改、运行假设或准备 azd 供应时激活。 | __代码0__<br />__代码1__<br />__代码2__ |
| [azure-devops-cli](../skills/azure-devops-cli/SKILL-zh.md) |通过 CLI 管理 Azure DevOps 资源，包括项目、存储库、管道、构建、拉取请求、工作项、工件和服务端点。使用 Azure DevOps、az 命令、devops 自动化、CI/CD 或用户提及 Azure DevOps CLI 时使用。 |无 |
| [azure 资源可视化工具](../skills/azure-resource-visualizer/SKILL-zh.md) |分析 Azure 资源组并生成详细的 Mermaid 架构图，显示各个资源之间的关系。当用户请求其 Azure 资源的图表或帮助了解资源之间的相互关系时，请使用此技能。 | __代码0__<br />__代码1__ |
| [azure 角色选择器](../skills/azure-role-selector/SKILL-zh.md) |当用户请求指导将哪个角色分配给给定所需权限的身份时，此代理可以帮助他们了解能够以最少权限访问满足要求的角色以及如何应用该角色。 | __代码0__ |
| [azure-static-web-apps](../skills/azure-static-web-apps/SKILL-zh.md) |帮助使用 SWA CLI 创建、配置和部署 Azure 静态 Web 应用。将静态站点部署到 Azure、设置 SWA 本地开发、配置 staticwebapp.config.json、将 Azure Functions API 添加到 SWA 或设置静态 Web 应用的 GitHub Actions CI/CD 时使用。 |无 |
| [chrome-devtools](../skills/chrome-devtools/SKILL-zh.md) |使用 Chrome DevTools MCP 进行专家级浏览器自动化、调试和性能分析。用于与网页交互、捕获屏幕截图、分析网络流量和分析性能。 |无 |
| [copilot-sdk](../skills/copilot-sdk/SKILL-zh.md) |使用 GitHub Copilot SDK 构建代理应用程序。在应用程序中嵌入 AI 代理、创建自定义工具、实施流响应、管理会话、连接到 MCP 服务器或创建自定义代理时使用。在 Copilot SDK、GitHub SDK、代理应用程序、嵌入 Copilot、可编程代理、MCP 服务器、自定义代理上触发。 |无 |
| [gh-cli](../skills/gh-cli/SKILL-zh.md) | GitHub CLI (gh) 全面参考存储库、问题、拉取请求、操作、项目、发布、要点、代码空间、组织、扩展以及命令行中的所有 GitHub 操作。 |无 |
| [git-提交](../skills/git-commit/SKILL-zh.md) |通过传统的提交消息分析、智能暂存和消息生成来执行 git commit。当用户要求提交更改、创建 git 提交或提及“/commit”时使用。支持：(1) 自动检测更改的类型和范围，(2) 根据差异生成常规提交消息，(3) 具有可选类型/范围/描述覆盖的交互式提交，(4) 用于逻辑分组的智能文件暂存 |无 |
| [github-问题](../skills/github-issues/SKILL-zh.md) |使用 MCP 工具创建、更新和管理 GitHub 问题。当用户想要创建错误报告、功能请求或任务问题、更新现有问题、添加标签/受让人/里程碑或管理问题工作流程时，请使用此技能。触发“创建问题”、“提交错误”、“请求功能”、“更新问题 X”或任何 GitHub 问题管理任务等请求。 | __代码0__ |
| [图像操作图像魔术](../skills/image-manipulation-image-magick/SKILL-zh.md) |使用 ImageMagick 处理和操作图像。支持调整大小、格式转换、批处理和检索图像元数据。在处理图像、创建缩略图、调整壁纸大小或执行批量图像操作时使用。 |无 |
| [遗留电路模型](../skills/legacy-circuit-mockups/SKILL-zh.md) |使用 HTML5 Canvas 绘图技术生成面包板电路模型和可视化图表。当需要创建电路布局、可视化电子元件布局、绘制面包板图、模型 6502 构建、生成复古计算机原理图或设计复古电子项目时使用。支持555定时器、W65C02S微处理器、28C256 EEPROM、W65C22 VIA芯片、7400系列逻辑门、LED、电阻、电容、开关、按钮、晶体和电线。 | __code0__<br />__code1__<br />__code2__<br />__code3__<br />__code4__<br />__code5__<br />__code6__<br />__code7__<br />__code8__<br />__code9__<br />__code10__<br />__code11__<br />__code12__<br />__code13__<br />__代码14__<br />__代码15__<br />__代码16__<br />__代码17__<br />__代码18__<br />__代码19__ |
| [制作技能模板](../skills/make-skill-template/SKILL-zh.md) |根据提示或复制此模板为 GitHub Copilot 创建新的代理技能。当被要求“创建一项技能”、“制定一项新技能”、“搭建一项技能”时，或者在使用捆绑资源构建专门的 AI 功能时使用。生成具有正确 frontmatter、目录结构和可选 script/references/assets 文件夹的 SKILL.md 文件。 |无 |
| [mcp-cli](../skills/mcp-cli/SKILL-zh.md) |通过 CLI 的 MCP（模型上下文协议）服务器接口。当您需要通过 MCP 服务器与外部工具、API 或数据源交互、列出可用的 MCP 服务器/工具或从命令行调用 MCP 工具时使用。 |无 |
| [微软代码参考](../skills/microsoft-code-reference/SKILL-zh.md) |查找 Microsoft API 参考、查找工作代码示例并验证 SDK 代码是否正确。使用 Azure SDK、.NET 库或 Microsoft API 时使用 — 查找正确的方法、检查参数、获取工作示例或排除错误。通过查询官方文档来捕获幻觉方法、错误签名和不推荐使用的模式。 |无 |
| [微软文档](../skills/microsoft-docs/SKILL-zh.md) |查询 Microsoft 官方文档以了解概念、查找教程并了解服务的工作原理。用于 Azure、.NET、Microsoft 365、Windows、Power Platform 和所有 Microsoft 技术。从 learn.microsoft.com 和其他 Microsoft 官方网站获取准确的最新信息 — 体系结构概述、快速入门、配置指南、限制和最佳实践。 |无 |
| [nuget-manager](../skills/nuget-manager/SKILL-zh.md) |管理 .NET 项目/解决方案中的 NuGet 包。添加、删除或更新 NuGet 包版本时请使用此技能。它强制使用 `dotnet` CLI 进行包管理，并仅在更新版本时提供严格的直接文件编辑程序。 |无 |
| [plantuml-ascii](../skills/plantuml-ascii/SKILL-zh.md) |使用 PlantUML 文本模式生成 ASCII 艺术图。当用户要求创建 ASCII 图表、基于文本的图表、终端友好图表或提及 plantuml ascii、文本图表、ascii 艺术图表时使用。支持：将 PlantUML 图转换为 ASCII 艺术图，以 ASCII 格式创建序列图、类图、流程图，使用 -utxt 标志生成 Unicode 增强的 ASCII 艺术图 |无 |
| [prd](../skills/prd/SKILL-zh.md) |为软件系统和人工智能支持的功能生成高质量的产品需求文档 (PRD)。包括执行摘要、用户故事、技术规范和风险分析。 |无 |
| [refactor](../skills/refactor/SKILL-zh.md) |外科手术式代码重构可在不改变行为的情况下提高可维护性。涵盖提取函数、重命名变量、分解上帝函数、提高类型安全性、消除代码异味以及应用设计模式。比 repo-rebuilder 不那么剧烈；用于逐步改进。 |无 |
| [scoutqa-测试](../skills/scoutqa-test/SKILL-zh.md) |当用户要求“测试此网站”、“运行探索性测试”、“检查可访问性问题”、“验证登录流程是否有效”、“查找此页面上的错误”或请求自动 QA 测试时，应使用此技能。使用 ScoutQA CLI 触发 Web 应用程序测试场景，包括冒烟测试、可访问性审核、电子商务流和用户流验证。重要提示：在实现 Web 应用程序功能后主动使用此技能来验证它们是否正常工作 - 不要等待用户要求进行测试。 |无 |
| [雪花语义视图](../skills/snowflake-semanticview/SKILL-zh.md) |使用 Snowflake CLI (snow) 创建、更改和验证 Snowflake 语义视图。当要求使用 CREATE/ALTER SEMANTIC VIEW 构建语义视图/语义层定义或对其进行故障排除时使用，通过 CLI 针对 Snowflake 验证语义视图 DDL，或指导 Snowflake CLI 安装和连接设置。 |无 |
| [vscode-ext-命令](../skills/vscode-ext-commands/SKILL-zh.md) |在 VS Code 扩展中贡献命令的指南。指示命名约定、可见性、本地化和其他相关属性，遵循 VS Code 扩展开发指南、库和良好实践 |无 |
| [vscode-ext-本地化](../skills/vscode-ext-localization/SKILL-zh.md) | VS Code 扩展的正确本地化指南，遵循 VS Code 扩展开发指南、库和良好实践 |无 |
| [网页设计审阅者](../skills/web-design-reviewer/SKILL-zh.md) |此技能可以对本地或远程运行的网站进行目视检查，以识别和修复设计问题。触发“审查网站设计”、“检查用户界面”、“修复布局”、“查找设计问题”等请求。检测响应式设计、可访问性、视觉一致性和布局破坏方面的问题，然后在源代码级别执行修复。 | __代码0__<br />__代码1__ |
| [网络应用程序测试](../skills/webapp-testing/SKILL-zh.md) |使用 Playwright 与本地 Web 应用程序交互并测试本地 Web 应用程序的工具包。支持验证前端功能、调试 UI 行为、捕获浏览器屏幕截图以及查看浏览器日志。 | __代码0__ |
| [workiq-copilot](../skills/workiq-copilot/SKILL-zh.md) |指导 Copilot CLI 了解如何使用 WorkIQ CLI/MCP 服务器查询 Microsoft 365 Copilot 数据（电子邮件、会议、文档、团队、人员）以获取实时上下文、摘要和建议。 |无 |
