---
applyTo: "**"
---

# 面向 LLM 的 Next.js 最佳实践 (2025)

_最后更新：2025 年 7 月_

本文档总结了构建、结构化和维护 Next.js 应用程序的最新、权威的最佳实践。它旨在供 LLM 和开发者使用，以确保代码质量、可维护性和可扩展性。

---

## 1. 项目结构和组织

- **使用 `app/` 目录**（App Router）处理所有新项目。优先选择它而不是传统的 `pages/` 目录。
- **顶级文件夹：**
  - `app/` — 路由、布局、页面和路由处理器
  - `public/` — 静态资源（图像、字体等）
  - `lib/` — 共享实用程序、API 客户端和逻辑
  - `components/` — 可重用的 UI 组件
  - `contexts/` — React 上下文提供程序
  - `styles/` — 全局和模块化样式表
  - `hooks/` — 自定义 React hooks
  - `types/` — TypeScript 类型定义
- **并置**：将文件（组件、样式、测试）放置在使用它们附近，但避免深度嵌套结构。
- **路由组**：使用括号（例如，`(admin)`）对路由进行分组，而不影响 URL 路径。
- **私有文件夹**：使用 `_` 前缀（例如，`_internal`）来选择退出路由并指示实现细节。

- **功能文件夹**：对于大型应用程序，按功能分组（例如，`app/dashboard/`、`app/auth/`）。
- **使用 `src/`**（可选）：将所有源代码放在 `src/` 中，以与配置文件分离。

## 2.1. 服务器和客户端组件集成 (App Router)

**永远不要在服务器组件内使用带有 `{ ssr: false }` 的 `next/dynamic`。** 这不受支持，并将导致构建/运行时错误。

**正确方法：**

- 如果您需要在服务器组件内使用客户端组件（例如，使用 hooks、浏览器 API 或仅客户端库的组件），您必须：
  1. 将所有仅客户端逻辑/UI 移动到专门的客户端组件（在顶部带有 `'use client'`）。
  2. 在服务器组件中直接导入并使用该客户端组件（不需要 `next/dynamic`）。
  3. 如果需要组合多个仅客户端元素（例如，带有个人资料下拉菜单的导航栏），创建一个包含所有这些元素的单一客户端组件。

**示例：**

```tsx
// 服务器组件
import DashboardNavbar from "@/components/DashboardNavbar";

export default async function DashboardPage() {
  // ...服务器逻辑...
  return (
    <>
      <DashboardNavbar /> {/* 这是一个客户端组件 */}
      {/* ...服务器渲染页面的其余部分... */}
    </>
  );
}
```

**原因：**

- 服务器组件不能使用仅客户端功能或禁用 SSR 的动态导入。
- 客户端组件可以在服务器组件内渲染，但反之亦然。

**总结：**
始终将仅客户端的 UI 移动到客户端组件中，并在您的服务器组件中直接导入它。永远不要在服务器组件中使用带有 `{ ssr: false }` 的 `next/dynamic`。

---

## 2. 组件最佳实践

- **组件类型：**
  - **服务器组件**（默认）：用于数据获取、繁重逻辑和非交互式 UI。
  - **客户端组件**：在顶部添加 `'use client'`。用于交互性、状态或浏览器 API。
- **何时创建组件：**
  - 如果 UI 模式被多次重用。
  - 如果页面的一部分是复杂或自包含的。
  - 如果它提高了可读性或可测试性。
- **命名约定：**
  - 对组件文件和导出使用 `PascalCase`（例如，`UserCard.tsx`）。
  - 对 hooks 使用 `camelCase`（例如，`useUser.ts`）。
  - 对静态资源使用 `snake_case` 或 `kebab-case`（例如，`logo_dark.svg`）。
  - 将上下文提供程序命名为 `XyzProvider`（例如，`ThemeProvider`）。
- **文件命名：**
  - 使组件名称与文件名匹配。
  - 对于单导出文件，默认导出组件。
  - 对于多个相关组件，使用 `index.ts` 桶文件。
- **组件位置：**
  - 将共享组件放在 `components/` 中。
  - 将特定路由的组件放在相关路由文件夹内。
- **Props：**
  - 为 props 使用 TypeScript 接口。
  - 优先使用显式 props 类型和默认值。
- **测试：**
  - 将测试与组件并置（例如，`UserCard.test.tsx`）。

## 3. 命名约定（通用）

- **文件夹**：`kebab-case`（例如，`user-profile/`）
- **文件**：组件使用 `PascalCase`，实用程序/hooks 使用 `camelCase`，静态资源使用 `kebab-case`
- **变量/函数**：`camelCase`
- **类型/接口**：`PascalCase`
- **常量**：`UPPER_SNAKE_CASE`

## 4. API 路由（路由处理器）

- **优先选择 API 路由而不是 Edge Functions**，除非您需要超低延迟或地理分布。
- **位置**：将 API 路由放置在 `app/api/` 中（例如，`app/api/users/route.ts`）。
- **HTTP 方法**：导出以 HTTP 动词命名的异步函数（`GET`、`POST` 等）。
- **请求/响应**：使用 Web `Request` 和 `Response` API。对于高级功能使用 `NextRequest`/`NextResponse`。
- **动态段**：对动态 API 路由使用 `[param]`（例如，`app/api/users/[id]/route.ts`）。
- **验证**：始终验证和清理输入。使用像 `zod` 或 `yup` 这样的库。
- **错误处理**：返回适当的 HTTP 状态代码和错误消息。
- **身份验证**：使用中间件或服务器端会话检查保护敏感路由。

## 5. 通用最佳实践

- **TypeScript**：为所有代码使用 TypeScript。在 `tsconfig.json` 中启用 `strict` 模式。
- **ESLint 和 Prettier**：强制执行代码样式和 linting。使用官方的 Next.js ESLint 配置。
- **环境变量**：将机密存储在 `.env.local` 中。永远不要将机密提交到版本控制。
- **测试**：使用 Jest、React Testing Library 或 Playwright。为所有关键逻辑和组件编写测试。
- **可访问性**：使用语义化 HTML 和 ARIA 属性。使用屏幕阅读器进行测试。
- **性能**：
  - 使用内置的图像和字体优化。
  - 为异步数据使用 Suspense 和加载状态。
  - 避免大型客户端包；将大部分逻辑保留在服务器组件中。
- **安全性**：
  - 清理所有用户输入。
  - 在生产环境中使用 HTTPS。
  - 设置安全的 HTTP 头。
- **文档**：
  - 编写清晰的 README 和代码注释。
  - 记录公共 API 和组件。

# 避免不必要的示例文件

除非用户特别要求实时示例、Storybook 故事或明确的文档组件，否则不要在主代码库中创建示例/演示文件（如 ModalExample.tsx）。默认情况下保持存储库干净并以生产为中心。

# 始终使用最新的文档和指南

- 对于每个 nextjs 相关请求，首先搜索最新的 nextjs 文档、指南和示例。
- 如果可用，使用以下工具获取和搜索文档：
  - `resolve_library_id` 来解析文档中的包/库名称。
  - `get_library_docs` 获取最新文档。
