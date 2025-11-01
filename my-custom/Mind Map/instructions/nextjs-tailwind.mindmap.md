## Next.js + Tailwind 规范（速览）

### 这是什么/何时使用/为什么/如何做
- What: 基于 Next.js(App Router)+Tailwind+TS 的工程与样式最佳实践。
- When: 新建项目/界面重构/样式体系治理时。
- Why: 提升一致性与生产力，保障性能与可访问性。
- How: 严格类型、RSC 优先、语义化 HTML、响应式与暗色模式、容器查询、优化图片与字体。

### 关键要点
- 架构: Server/Client 分层；按特性分组路由；错误边界；Suspense。
- TypeScript: strict、类型守卫、zod 运行时校验。
- 样式: 约定色板；组件化 utilities；暗色模式；容器查询；避免深度嵌套。
- 状态: RSC 承载服务端状态；客户端用 hooks；loading/error/optimistic。
- 数据: 服务端直连 DB/API；缓存与失效；重试与错误处理。
- 安全: 输入校验、鉴权、CSRF、防刷、API 安全。
- 性能: next/image 与 next/font；prefetch；code splitting；bundle 控制。

### 紧凑脑图
- 结构→类型→样式→数据→状态→安全→性能→测试

### 开发者示例问题（≥10）
- 如何在 Tailwind 中抽象设计令牌并复用？
- RSC 中的数据缓存与 revalidate 的策略？
- 表单的客户端校验与服务端校验如何协同？
- 图片与字体优化的度量与回归基线？
- 容器查询在多断点布局下的最佳实践？
- 深色模式的系统偏好与手动切换如何并存？
- 组件库与自定义样式的边界如何定义？
- Bundle 分析与按路由拆分策略？
- 国际化与方向性样式（LTR/RTL）如何处理？
- E2E 测试如何覆盖视觉回归与交互？

—
Source: d:\mycode\awesome-copilot\instructions\nextjs-tailwind.instructions.md | Generated: 2025-10-17
