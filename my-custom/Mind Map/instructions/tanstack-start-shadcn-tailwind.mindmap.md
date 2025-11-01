## What
- 基于 TanStack Start + React + Shadcn/ui + Tailwind 的工程规范与模式（Zod 校验、Query 状态）

## When
- 新建或重构 TS 严格模式的 SSR/CSR 混合站点

## Why
- 一致的数据获取/校验/错误与加载边界，提高 DX 与可靠性

## How
- 技术栈
  - TS5 严格、TanStack Start 路由/SSR、Shadcn/ui、Tailwind、Zod、TanStack Query
- 组件
  - 函数组件+显式 Props；无障碍标签/ARIA；UI 组件优先复用 Shadcn
- 数据
  - Route Loader 承担首屏/SSR/SEO 关键数据；Query 处理频繁更新与乐观更新
- 校验
  - Zod 模式定义与 safeParse；集中定义 schemas.ts
- 路由
  - 文件式；每个路由提供 errorBoundary/pendingBoundary
- 导入
  - 统一 '@/..' 别名，避免相对地狱
- 样式
  - Tailwind 响应式与组合变体；cn()/variants 组合

## Key Points
- Loader vs Query 职责清晰
- Zod 全量覆盖外部数据
- 错误/加载边界必备

## Compact Map
- 栈: TS/Start/Shadcn/Tailwind/Query/Zod
- 路由: 文件式 + error/pending
- 数据: Loader 首屏 | Query 更新
- 校验: schema/safeParse
- UI: 组件复用/可达性
- 导入: '@/'

## Example Questions
1) 哪些数据应放在 Route Loader 而非 Query？
2) 如何为路由声明 errorBoundary/pendingBoundary？
3) Zod schema 如何组织与复用？
4) React Query 何时设置 refetchInterval？
5) 如何用乐观更新避免闪烁？
6) '@/ 别名' 在工具链中如何配置？
7) Shadcn 组件何时应扩展而非重写？
8) SSR 与 CSR 数据源如何统一类型？
9) Loader 返回的数据如何进行 SEO 处理？
10) 表单校验在 Loader/Action/Client 各放哪里？
11) cn 与变体如何组合复杂样式？

Source: d:\mycode\awesome-copilot\instructions\tanstack-start-shadcn-tailwind.instructions.md | Generated: 2025-10-17
