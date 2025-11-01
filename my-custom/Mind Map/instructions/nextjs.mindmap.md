## Next.js 最佳实践（速览，App Router）

### 这是什么/何时使用/为什么/如何做
- What: 2025 时点 Next.js 应用结构、组件分类、API 路由、命名、性能与安全指南。
- When: 新项目脚手架、迁移到 App Router、代码审查与问题定位时。
- Why: 统一项目结构、减少反模式、提升可维护性与性能。
- How: 使用 app/ 目录；区分 Server/Client 组件；API 路由在 app/api；严格类型与 ESLint；避免在 Server 组件内使用 next/dynamic ssr:false。

### 关键要点
- 结构: app/、public/、lib/、components/、contexts/、styles/、hooks/、types/；可选 src/。
- 组件: 默认 Server；需交互的使用 'use client'；Server 内直接引用 Client 组件，不用 next/dynamic ssr:false。
- API: 放置于 app/api/*/route.ts；导出 GET/POST 等；使用 Web/NextResponse API；参数校验（zod）。
- 命名: PascalCase 组件、camelCase hooks/utils、kebab-case 资产；类型/接口 PascalCase、常量 UPPER_SNAKE_CASE。
- 通用: TypeScript 严格、ESLint+Prettier、.env.local、安全头与输入净化、可访问性。
- 性能: Image/Font 优化、Suspense/loading、保持大部分逻辑在 Server 侧、控制客户端包体。

### 紧凑脑图
- 结构→组件划分→API 约定→命名→类型/Lint→性能→安全→文档

### 开发者示例问题（≥10）
- 如何从 pages/ 迁移到 app/ 并保持路由等价？
- 在 Server 组件中组合多个 client-only 子组件的正确姿势？
- app/api 的错误返回与状态码约定如何封装？
- 使用 zod 做输入校验与类型推断的范式？
- 如何压缩客户端包体并定位超大依赖？
- Suspense 与 streaming 在真实列表页的落地示例？
- next/font 与自托管字体的取舍与性能影响？
- 动态路由与并行/拦截路由的调试技巧？
- 中间件中做鉴权与本地化的边界？
- 何时使用 Edge vs Node 运行时？

—
Source: d:\mycode\awesome-copilot\instructions\nextjs.instructions.md | Generated: 2025-10-17
