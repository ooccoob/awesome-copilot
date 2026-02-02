---
description: 'Guidelines for building TanStack Start applications'
applyTo: '**/*.ts, **/*.tsx, **/*.js, **/*.jsx, **/*.css, **/*.scss, **/*.json'
---

# TanStack 入门 Shadcn/ui 开发指南

您是一位专业的 TypeScript 开发人员，专门从事具有现代 React 模式的 TanStack Start 应用程序。

## 技术堆栈
- TypeScript（严格模式）
- TanStack Start（路由和 SSR）
- Shadcn/ui（UI组件）
- Tailwind CSS（样式）
- 佐德（验证）
- TanStack 查询（客户端状态）

## 代码风格规则

- 切勿使用 `any` 类型 - 始终使用正确的 TypeScript 类型
- 优先选择函数组件而不是类组件
- 始终使用 Zod 模式验证外部数据
- 包括所有路线的错误和待定边界
- 遵循 ARIA 属性的辅助功能最佳实践

## 组件模式

使用具有适当 TypeScript 接口的函数组件：

```typescript
interface ButtonProps {
  children: React.ReactNode;
  onClick: () => void;
  variant?: 'primary' | 'secondary';
}

export default function Button({ children, onClick, variant = 'primary' }: ButtonProps) {
  return (
    <button onClick={onClick} className={cn(buttonVariants({ variant }))}>
      {children}
    </button>
  );
}
```

## 数据获取

使用路线加载器用于：
- 渲染所需的初始页面数据
- SSR要求
- SEO 关键数据

使用 React 查询：
- 经常更新数据
- 可选/辅助数据
- 乐观更新的客户端突变

```typescript
// Route Loader
export const Route = createFileRoute('/users')({
  loader: async () => {
    const users = await fetchUsers()
    return { users: userListSchema.parse(users) }
  },
  component: UserList,
})

// React Query
const { data: stats } = useQuery({
  queryKey: ['user-stats', userId],
  queryFn: () => fetchUserStats(userId),
  refetchInterval: 30000,
});
```

## Zod验证

始终验证外部数据。在 `src/lib/schemas.ts` 中定义模式：

```typescript
export const userSchema = z.object({
  id: z.string(),
  name: z.string().min(1).max(100),
  email: z.string().email().optional(),
  role: z.enum(['admin', 'user']).default('user'),
})

export type User = z.infer<typeof userSchema>

// Safe parsing
const result = userSchema.safeParse(data)
if (!result.success) {
  console.error('Validation failed:', result.error.format())
  return null
}
```

## 路线

使用基于文件的路由在 `src/routes/` 中构建路由。始终包含错误和待定边界：

```typescript
export const Route = createFileRoute('/users/$id')({
  loader: async ({ params }) => {
    const user = await fetchUser(params.id);
    return { user: userSchema.parse(user) };
  },
  component: UserDetail,
  errorBoundary: ({ error }) => (
    <div className="text-red-600 p-4">Error: {error.message}</div>
  ),
  pendingBoundary: () => (
    <div className="flex items-center justify-center p-4">
      <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary" />
    </div>
  ),
});
```

## 用户界面组件

始终更喜欢 Shadcn/ui 组件而不是自定义组件：

```typescript
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';

<Card>
  <CardHeader>
    <CardTitle>User Details</CardTitle>
  </CardHeader>
  <CardContent>
    <Button onClick={handleSave}>Save</Button>
  </CardContent>
</Card>
```

使用 Tailwind 进行响应式设计的样式设计：

```typescript
<div className="flex flex-col gap-4 p-6 md:flex-row md:gap-6">
  <Button className="w-full md:w-auto">Action</Button>
</div>
```

## 无障碍

首先使用语义 HTML。仅当不存在等效语义时才添加 ARIA：

```typescript
// ✅ Good: Semantic HTML with minimal ARIA
<button onClick={toggleMenu}>
  <MenuIcon aria-hidden="true" />
  <span className="sr-only">Toggle Menu</span>
</button>

// ✅ Good: ARIA only when needed (for dynamic states)
<button
  aria-expanded={isOpen}
  aria-controls="menu"
  onClick={toggleMenu}
>
  Menu
</button>

// ✅ Good: Semantic form elements
<label htmlFor="email">Email Address</label>
<input id="email" type="email" />
{errors.email && (
  <p role="alert">{errors.email}</p>
)}
```

## 文件组织

```
src/
├── components/ui/    # Shadcn/ui components
├── lib/schemas.ts    # Zod schemas
├── routes/          # File-based routes
└── routes/api/      # Server routes (.ts)
```

## 进口标准

对所有内部导入使用 `@/` 别名：

```typescript
// ✅ Good
import { Button } from '@/components/ui/button'
import { userSchema } from '@/lib/schemas'

// ❌ Bad
import { Button } from '../components/ui/button'
```

## 添加组件

需要时安装Shadcn组件：

```bash
npx shadcn@latest add button card input dialog
```

## 常见模式

- 始终使用 Zod 验证外部数据
- 使用路由加载器获取初始数据，使用 React Query 获取更新
- 包括所有路线上的错误/待定边界
- 更喜欢 Shadcn 组件而不是自定义 UI
- 一致地使用 `@/` 导入
- 遵循可访问性最佳实践
