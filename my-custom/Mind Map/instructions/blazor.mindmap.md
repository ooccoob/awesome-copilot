## What/When/Why/How

- What: Blazor 组件/应用模式：结构、命名、生命周期、状态/缓存、性能、测试、安全。
- When: 开发/重构 Razor 组件与服务、接入 API、优化渲染与状态管理时。
- Why: 降低重渲染成本、增强可测试性与可靠性、统一代码风格与命名。
- How: 遵循组件生命周期(OnInitializedAsync/OnParametersSetAsync)、合理 @bind、DI 注入服务、使用 StateHasChanged/ShouldRender 控制渲染、分离复杂逻辑到 code-behind/服务。

## Key Points

- 命名: 组件/方法/公有成员 PascalCase；私有字段 camelCase；接口前缀 I。
- 生命周期: 善用异步避免阻塞 UI；事件用 EventCallback 传最小数据。
- 性能: 减少不必要渲染；ShouldRender 精细控制；小组件内联函数，复杂逻辑挪至服务。
- 状态: 基础用 CascadingParameter/EventCallback；复杂用 Fluxor/BlazorState；WASM 用 localStorage/sessionStorage；Server 用 Scoped + StateContainer。
- 缓存: IMemoryCache/分布式缓存；API 结果按需缓存。
- API: HttpClient + 异常处理与反馈。
- 测试: xUnit/NUnit/MSTest；Moq/NSubstitute；调试结合浏览器与 VS 工具。
- 安全: 身份认证(Identity/JWT)/HTTPS/CORS。
- 文档: Swagger/OpenAPI；XML 注释增强模型与方法说明。

## Compact Map

- Code Style → 命名/分层/异步
- Rendering → ShouldRender/StateHasChanged
- State → 基础/高级库/持久化
- Cache → IMemoryCache/分布式
- API → HttpClient+错误处理
- Test → 单元/集成/Mock
- Security → Auth/HTTPS/CORS

## Example Questions (10+)

1) ShouldRender 适用哪些场景？
2) 何时用 CascadingParameter vs Fluxor？
3) Server 模式如何做会话内状态共享？
4) WASM 中缓存 API 响应的策略？
5) 组件事件参数传递如何减小开销？
6) 如何隔离复杂 UI 逻辑到服务/代码隐藏？
7) 大列表渲染如何避免卡顿？
8) HttpClient 出错时如何统一用户提示？
9) 如何为组件编写可维护的单元测试？
10) 与 Swagger/OpenAPI 的对齐方式？
11) DI 生命周期在 Server 与 WASM 的注意点？

---
Source: d:\mycode\awesome-copilot\instructions\blazor.instructions.md | Generated: 2025-10-17
