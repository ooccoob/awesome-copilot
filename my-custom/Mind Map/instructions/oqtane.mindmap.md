## Oqtane 模块开发模式（速览）

### 这是什么/何时使用/为什么/如何做
- What: Oqtane 框架下的 Blazor 模块开发规范与客户端/服务器配套模式。
- When: 新增/维护 Oqtane 模块、规划客户端服务与服务器控制器/仓储时。
- Why: 统一模块结构与命名，复用基类与状态，提升可维护性与性能。
- How: 参考主仓库模式；客户端 Razor 动作文件继承 ModuleBase；复杂逻辑抽服务继承 ServiceBase；服务调用服务端 API；服务端 Controller→Service/Repository 分层。

### 关键要点
- Blazor 规范: 生命周期（OnInitializedAsync 等）、@bind、DI、分离关注点。
- 命名: 组件/方法/公开成员 PascalCase；私有字段 camelCase；接口前缀 I。
- C# 版本: 使用最新 C#（示例提到 13），合理使用记录类型/模式匹配/全局 using。
- Oqtane: 模块目录结构；PageState/SiteState 等内置状态；日志/错误边界；模块间通信。
- 性能: 异步 API、减少不必要渲染、ShouldRender/StateHasChanged、事件回调最小化负载。
- 缓存: IMemoryCache/分布式缓存；WASM 使用 local/sessionStorage；API 结果缓存。
- 测试: xUnit/NUnit/MSTest；Moq/NSubstitute；VS 调试与诊断工具。
- 安全: 认证与授权（User.Roles）；HTTPS/CORS；日志合规。

### 紧凑脑图
- 结构: Client Razor/ServiceBase → Server Controller/Service/Repo → DI/状态/缓存
- 质量: 命名/生命周期/错误与日志/测试
- 运维: 安全/性能/缓存/部署

### 开发者示例问题（≥10）
- 一个模块的客户端动作结构应如何拆分与命名？
- ServiceBase 与服务器 Controller 的路由与契约如何对齐？
- 复杂模块的数据加载如何避免重复渲染？
- PageState 与 SiteState 的使用边界？
- 何时将逻辑下沉至服务端仓储层？
- 如何为模块编写可复用的集成测试样板？
- 服务端异常如何在客户端优雅呈现？
- 何时选择分布式缓存以共享状态？
- 日志与错误收集的最小可行方案？
- 模块版本升级的兼容性与迁移策略？

—
Source: d:\mycode\awesome-copilot\instructions\oqtane.instructions.md | Generated: 2025-10-17
