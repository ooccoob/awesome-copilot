## What / When / Why / How
- What: Angular 开发规范（TS 严格模式、Standalone、Signals、DI、RxJS、OnPush 等）。
- When: 新建/改造 Angular 应用、实现数据获取/状态管理/表单/路由/样式与测试时。
- Why: 可维护、性能优、可测试、一致且可扩展。
- How: 独立组件+特性分层；信号与 RxJS 组合；HttpClient+拦截器；路由懒加载；表单强类型；拦截错误；SSR/SSG 可选；Jasmine/Karma/Cypress 测试。

## Key points
- 架构：Standalone 优先；特性域组织；懒加载；清晰职责（容器 vs 展示）。
- TypeScript：开启 strict；接口/类型明确；守卫与联合类型；错误处理用 catchError。
- 组件：生命周期最佳实践；>=19 优先函数式 input/output 等；ChangeDetectionStrategy.OnPush。
- 样式：SCSS+主题；响应式；a11y 与语义化。
- 状态：signal()/computed()/effect()；与 RxJS 配合 AsyncPipe；加载/错误状态显式化。
- 数据：HttpClient 强类型；inject()；shareReplay 缓存；全局拦截器统一错误与鉴权。
- 安全：路由守卫；拦截器注入令牌/CSRF；表单校验与自定义校验器；避免直接 DOM 操作。
- 性能：懒加载、OnPush、trackBy、SSR/SSG 视需要。
- 测试：TestBed、HttpClientTestingModule、信号更新测试、端到端（Cypress/Playwright）。

## Compact map
- 架构: Standalone/懒加载
- 类型: strict/接口/守卫
- 组件: OnPush/指令/管道
- 状态: signals+RxJS
- 数据: HttpClient/拦截器
- 安全: 守卫/CSRF/校验
- 性能: trackBy/SSR
- 测试: 单元/集成/E2E

## Example questions (10+)
- 何时选 signals，何时保持 Observable？
- 如何在 OnPush 下最小化变更检测与提升渲染？
- 拦截器如何统一处理 401/403 并刷新令牌？
- 表单强类型与自定义校验器该如何组织？
- computed vs effect 的边界与内存泄漏防范？
- 大表格如何配合 trackBy 与虚拟滚动？
- SSR 与 SSG 在 SEO 与数据获取上的权衡？
- Feature 级路由如何拆分与保护（守卫/Resolver）？
- shareReplay 缓存何时失效与如何回收？
- 组件库（Material）主题化与可访问性要点？
- Angular 19 函数式输入输出迁移注意点？

—
Source: d:\mycode\awesome-copilot\instructions\angular.instructions.md | Generated: {{timestamp}}
