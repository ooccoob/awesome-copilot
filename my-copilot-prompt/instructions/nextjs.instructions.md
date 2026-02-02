---
description: "Best practices for building Next.js (App Router) apps with modern caching, tooling, and server/client boundaries (aligned with Next.js 16.1.1)."
applyTo: '**/*.tsx, **/*.ts, **/*.jsx, **/*.js, **/*.css'
---

# Next.js 法学硕士最佳实践 (2026)

_最后更新时间：2026 年 1 月（与 Next.js 16.1.1 一致）_

本文档总结了构建、构建和维护 Next.js 应用程序的最新、权威的最佳实践。它供法学硕士和开发人员使用，以确保代码质量、可维护性和可扩展性。

---

## 1. 项目结构和组织

- **对所有新项目使用 `app/` 目录** (App Router)。优先使用它而不是旧的 `pages/` 目录。
- **顶级文件夹：**
  - `app/` — 路由、布局、页面和路由处理程序
  - `public/` — 静态资源（图像、字体等）
  - `lib/` — 共享实用程序、API 客户端和逻辑
  - `components/` — 可重用的 UI 组件
  - `contexts/` — React 上下文提供者
  - `styles/` — 全局和模块化样式表
  - `hooks/` — 自定义 React 钩子
  - `types/` — TypeScript 类型定义
- **共置：** 将文件（组件、样式、测试）放置在它们使用的地方附近，但避免深层嵌套的结构。
- **路由组：** 使用括号（例如，`(admin)`）对路由进行分组，而不影响 URL 路径。
- **私有文件夹：** 以 `_` 为前缀（例如 `_internal`）以选择退出路由和信号实现细节。

- **功能文件夹：** 对于大型应用程序，按功能分组（例如 `app/dashboard/`、`app/auth/`）。
- **使用 `src/`** （可选）：将所有源代码放在 `src/` 中以与配置文件分开。

## 2.1.服务器和客户端组件集成（App Router）

**切勿在服务器组件内将 `next/dynamic` 与 `{ ssr: false }` 一起使用。** 这不受支持，并且会导致构建/运行时错误。

**正确方法：**

- 如果您需要在服务器组件内使用客户端组件（例如，使用钩子、浏览器 API 或仅限客户端的库的组件），则必须：
  1. 将所有仅客户端逻辑/UI 移至专用客户端组件（顶部带有 `'use client'`）。
  2. 直接在服务器组件中导入并使用该客户端组件（不需要 `next/dynamic`）。
  3. 如果您需要组合多个仅客户端元素（例如，带有配置文件下拉列表的导航栏），请创建一个包含所有这些元素的客户端组件。

**示例：**

```tsx
// Server Component
import DashboardNavbar from "@/components/DashboardNavbar";

export default async function DashboardPage() {
  // ...server logic...
  return (
    <>
      <DashboardNavbar /> {/* This is a Client Component */}
      {/* ...rest of server-rendered page... */}
    </>
  );
}
```

**为什么：**

- 服务器组件无法使用仅客户端功能或禁用 SSR 的动态导入。
- 客户端组件可以在服务器组件内呈现，但反之则不行。

**概括：**
始终将仅限客户端的 UI 移至客户端组件中，并将其直接导入到服务器组件中。切勿在服务器组件中将 `next/dynamic` 与 `{ ssr: false }` 一起使用。

## 2.2. Next.js 16+ 异步请求 API (App Router)

- **假设请求绑定数据在服务器组件和路由处理程序中是异步的。** 在 Next.js 16 中，`cookies()`、`headers()` 和 `draftMode()` 等 API 在 App Router 中是异步的。
- **小心路由属性：** `params` / `searchParams` 可能是服务器组件中的 Promise。更喜欢对它们进行 `await` 处理，而不是将它们视为普通对象。
- **避免意外动态渲染：** 访问请求数据（cookies/headers/searchParams）会选择动态行为的路由。有意识地阅读它们，并在适当的时候将动态部分隔离在 `Suspense` 边界后面。

---

## 2. 组件最佳实践

- **组件类型：**
  - **服务器组件**（默认）：用于数据获取、繁重逻辑和非交互式 UI。
  - **客户端组件：** 在顶部添加 `'use client'`。用于交互、状态或浏览器 API。
- **何时创建组件：**
  - 如果一个 UI 模式被重复使用多次。
  - 如果页面的一部分很复杂或独立。
  - 如果它提高了可读性或可测试性。
- **命名约定：**
  - 将 `PascalCase` 用于组件文件和导出（例如 `UserCard.tsx`）。
  - 使用 `camelCase` 作为钩子（例如 `useUser.ts`）。
  - 对静态资源使用 `snake_case` 或 `kebab-case`（例如 `logo_dark.svg`）。
  - 将上下文提供程序命名为 `XyzProvider`（例如 `ThemeProvider`）。
- **文件命名：**
  - 将组件名称与文件名匹配。
  - 对于单个导出文件，默认导出组件。
  - 对于多个相关组件，请使用 `index.ts` 桶文件。
- **组件位置：**
  - 将共享组件放置在 `components/` 中。
  - 将特定于路线的组件放置在相关路线文件夹内。
- **道具：**
  - 使用 TypeScript 接口作为 props。
  - 更喜欢显式的 prop 类型和默认值。
- **测试：**
  - 将测试与组件放在一起（例如 `UserCard.test.tsx`）。

## 3. 命名约定（一般）

- **文件夹：** `kebab-case`（例如，`user-profile/`）
- **文件：** `PascalCase` 用于组件，`camelCase` 用于实用程序/挂钩，`kebab-case` 用于静态资产
- **变量/函数：** `camelCase`
- **类型/接口：** `PascalCase`
- **常量：** `UPPER_SNAKE_CASE`

## 4. API 路由（路由处理程序）

- **优先选择 API 路由而不是边缘功能**，除非您需要超低延迟或地理分布。
- **位置：** 将 API 路由放置在 `app/api/` 中（例如 `app/api/users/route.ts`）。
- **HTTP 方法：** 导出以 HTTP 动词（`GET`、`POST` 等）命名的异步函数。
- **请求/响应：** 使用 Web `Request` 和 `Response` API。使用 `NextRequest`/`NextResponse` 来实现高级功能。
- **动态段：** 使用 `[param]` 进行动态 API 路由（例如 `app/api/users/[id]/route.ts`）。
- **验证：** 始终验证和清理输入。使用 `zod` 或 `yup` 等库。
- **错误处理：** 返回适当的 HTTP 状态代码和错误消息。
- **身份验证：** 使用中间件或服务器端会话检查来保护敏感路由。

### Route Handler 使用说明（性能）

- **不要从服务器组件调用您自己的路由处理程序**（例如，`fetch('/api/...')`）只是为了重用逻辑。更喜欢将共享逻辑提取到模块中（例如 `lib/`）并直接调用它以避免额外的服务器跳跃。

## 5. 一般最佳实践

- **TypeScript：** 对所有代码使用 TypeScript。在 `tsconfig.json` 中启用 `strict` 模式。
- **ESLint 和 Prettier：** 强制执行代码样式和 linting。使用官方 Next.js ESLint 配置。在 Next.js 16 中，更喜欢通过 ESLint CLI（而不是 `next lint`）运行 ESLint。
- **环境变量：** 将机密存储在 `.env.local` 中。切勿将秘密提交给版本控制。
  - 在 Next.js 16 中，`serverRuntimeConfig` / `publicRuntimeConfig` 被删除。请改用环境变量。
  - `NEXT_PUBLIC_` 变量**在构建时内联**（构建后更改它们不会影响已部署的构建）。
  - 如果您确实需要在动态上下文中对 env 进行运行时评估，请遵循 Next.js 指南（例如，在读取 `process.env` 之前调用 `connection()`）。
- **测试：** 使用 Jest、React 测试库或 Playwright。为所有关键逻辑和组件编写测试。
- **辅助功能：** 使用语义 HTML 和 ARIA 属性。使用屏幕阅读器进行测试。
- **性能：**
  - 使用内置图像和字体优化。
  - 与传统缓存模式相比，更喜欢 **缓存组件** (`cacheComponents` + `use cache`)。
  - 对异步数据使用挂起和加载状态。
  - 避免大量客户捆绑；将大部分逻辑保留在服务器组件中。
- **安全：**
  - 清理所有用户输入。
  - 在生产中使用 HTTPS。
  - 设置安全 HTTP 标头。
  - 更喜欢服务器操作和路由处理程序的服务器端授权；永远不要相信客户的输入。
- **文件：**
  - 编写清晰的自述文件和代码注释。
  - 记录公共 API 和组件。

## 6. 缓存和重新验证（Next.js 16 个缓存组件）

- **在 App Router 中首选缓存组件进行记忆/缓存**。
  - 通过 `cacheComponents: true` 在 `next.config.*` 中启用。
  - 使用 **`use cache` 指令** 将组件/函数选择为缓存。
- **有意使用缓存标记和生命周期：**
  - 使用 `cacheTag(...)` 将缓存结果与标签关联起来。
  - 使用 `cacheLife(...)` 控制缓存生命周期（预设或配置的配置文件）。
- **重新验证指南：**
  - 在大多数情况下，首选 `revalidateTag(tag, 'max')` （重新验证时失效）。
  - 单参数形式 `revalidateTag(tag)` 已被保留/已弃用。
  - 当您需要“读您所写”/即时一致性时，请在**服务器操作**中使用 `updateTag(...)` 。
- **新代码避免使用 `unstable_cache`** ；将其视为遗留并迁移到缓存组件。

## 7. 工具更新 (Next.js 16)

- **Turbopack 是默认的开发捆绑器。** 通过 `next.config.*` 中的顶级 `turbopack` 字段进行配置（不要使用已删除的 `experimental.turbo`）。
- **通过 `typedRoutes` 键入的路由是稳定的**（需要 TypeScript）。

# 避免不必要的示例文件

不要在主代码库中创建示例/演示文件（如 ModalExample.tsx），除非用户特别请求实时示例、Storybook 故事或明确的文档组件。默认情况下保持存储库干净并以生产为中心。

# 始终使用最新的文档和指南

- 对于每个 nextjs 相关请求，首先搜索最新的 nextjs 文档、指南和示例。
- 使用以下工具来获取和搜索文档（如果可用）：
  - `resolve_library_id` 解析文档中的包/库名称。
  - `get_library_docs` 获取最新文档。
