## What / When / Why / How
- What: Astro 5.x 内容驱动、服务端优先的开发规范（Islands、Content Layer API、类型化内容）。
- When: 构建博客/文档/营销站/电商等内容站点时。
- Why: 近零 JS、极致性能、良好 SEO 与可维护内容模型。
- How: .astro 服务端渲染为主，按需水合；Content Collections + 新 Content Layer API；ClientRouter 视图切换；类型安全与优化链路。

## Key points
- 架构：Islands；MPA 优先；渐进增强；组件命名 PascalCase。
- TypeScript：使用 astro/tsconfigs/base；运行 astro sync 生成 .astro/types.d.ts；为组件 props 建接口。
- 内容层：src/content.config.ts 定义集合；loader: glob()/file()；getCollection()/getEntry() 类型安全。
- 视图切换：<ClientRouter />（v5 替代 ViewTransitions）；CSS 自定义过渡。
- 性能：默认 0 JS；client:* 指令按需；懒加载图片/组件；内容层加速构建。
- 样式与可访问性：组件内 scoped 样式；响应式；语义化+ARIA；或使用 Tailwind。
- API/SSR：src/pages/api；SSR 仅在需要时开启；中间件处理鉴权；安全用环境变量。
- SEO：OG/Twitter、站点地图、结构化数据；标题描述优化。
- 图片：<Image /> 响应式与 AVIF/WebP；懒加载；alt 文本。

## Compact map
- 内容: Collections+Schema
- 渲染: SSR/SSG+Islands
- 路由: ClientRouter 过渡
- 性能: 0 JS/懒加载
- SEO: 元数据/站点图
- 图片: <Image/> 优化

## Example questions (10+)
- Content Layer API 的 glob() 与旧式内容集合如何迁移？
- 如何为博客集合定义 schema 并生成类型？
- 何时需要 ClientRouter，何时保持纯 MPA？
- 在不牺牲可访问性的情况下实现视图过渡动画？
- 组件内收敛 JS 与按需水合的选择策略？
- 如何组织 layout 以复用 SEO/导航/脚注？
- 大量 Markdown 内容构建性能优化手段？
- SSR 场景下的鉴权与缓存策略？
- <Image/> 的 srcset 与占位策略如何配置？
- 与 React/Vue 岛组件共享状态的方式？

—
Source: d:\mycode\awesome-copilot\instructions\astro.instructions.md | Generated: {{timestamp}}
