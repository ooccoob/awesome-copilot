---
description: '内容驱动网站的Astro开发标准和最佳实践'
applyTo: '**/*.astro, **/*.ts, **/*.js, **/*.md, **/*.mdx'
---

# Astro开发指令

遵循内容驱动、服务器优先架构和现代最佳实践构建高质量Astro应用程序的指令。

## 项目上下文
- Astro 5.x，采用Islands架构和Content Layer API
- TypeScript用于类型安全和更好的开发体验，配合自动生成的类型
- 内容驱动网站（博客、营销、电子商务、文档）
- 服务器优先渲染，选择性客户端水合
- 支持多种UI框架（React、Vue、Svelte、Solid等）
- 默认静态站点生成（SSG），可选服务器端渲染（SSR）
- 通过现代内容加载和构建优化增强性能

## 开发标准

### 架构
- 拥抱Islands架构：默认服务器渲染，选择性水合
- 使用Content Collections组织内容，实现类型安全的Markdown/MDX管理
- 按功能或内容类型构建项目以实现可扩展性
- 使用基于组件的架构，具有清晰的关注点分离
- 实施渐进增强模式
- 遵循多页应用（MPA）方法而不是单页应用（SPA）模式

### TypeScript集成
- 使用推荐的v5.0设置配置`tsconfig.json`：
```json
{
  "extends": "astro/tsconfigs/base",
  "include": [".astro/types.d.ts", "**/*"],
  "exclude": ["dist"]
}
```
- 类型在`.astro/types.d.ts`中自动生成（替换`src/env.d.ts`）
- 运行`astro sync`生成/更新类型定义
- 使用TypeScript接口定义组件props
- 利用内容集合和Content Layer API的自动生成类型

### 组件设计
- 使用`.astro`组件进行静态、服务器渲染的内容
- 仅在需要交互性时导入框架组件（React、Vue、Svelte）
- 遵循Astro的组件脚本结构：顶部frontmatter，下方模板
- 使用有意义的组件名称，遵循PascalCase约定
- 保持组件专注和可组合
- 实施适当的prop验证和默认值

### Content Collections

#### 现代Content Layer API（v5.0+）
- 使用新的Content Layer API在`src/content.config.ts`中定义集合
- 使用内置加载器：基于文件内容的`glob()`，单个文件的`file()`
- 利用新的加载系统增强性能和可扩展性
- Content Layer API示例：
```typescript
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    pubDate: z.date(),
    tags: z.array(z.string()).optional()
  })
});
```

#### 遗留集合（向后兼容）
- 遗留`type: 'content'`集合仍通过自动glob()实现支持
- 通过添加显式`loader`配置迁移现有集合
- 使用`getCollection()`和`getEntry()`进行类型安全查询
- 使用frontmatter验证和自动生成类型构建内容

### View Transitions和客户端路由
- 在布局head中使用`<ClientRouter />`组件启用（v5.0中从`<ViewTransitions />`重命名）
- 从`astro:transitions`导入：`import { ClientRouter } from 'astro:transitions'`
- 提供类似SPA的导航，无需完整页面重新加载
- 使用CSS和view-transition-name自定义过渡动画
- 使用持久化islands在页面导航间保持状态
- 使用`transition:persist`指令保留组件状态

### 性能优化
- 默认零JavaScript - 仅在需要时添加交互性
- 策略性地使用客户端指令（`client:load`、`client:idle`、`client:visible`）
- 为图像和组件实施懒加载
- 使用Astro的内置优化优化静态资源
- 利用Content Layer API加快内容加载和构建
- 通过避免不必要的客户端JavaScript最小化包大小

### 样式
- 默认在`.astro`组件中使用作用域样式
- 需要时实施CSS预处理（Sass、Less）
- 使用CSS自定义属性进行主题化和设计系统
- 遵循移动优先响应式设计原则
- 使用语义HTML和适当的ARIA属性确保可访问性
- 考虑实用程序优先框架（Tailwind CSS）进行快速开发

### 客户端交互性
- 使用框架组件（React、Vue、Svelte）进行交互元素
- 根据用户交互模式选择正确的水合策略
- 在框架边界内实施状态管理
- 谨慎处理客户端路由以保持MPA优势
- 使用Web Components进行框架无关的交互性
- 使用存储或自定义事件在islands间共享状态

### API路由和SSR
- 在`src/pages/api/`中创建API路由以实现动态功能
- 使用适当的HTTP方法和状态码
- 实施请求验证和错误处理
- 为动态内容需求启用SSR模式
- 使用中间件进行身份验证和请求处理
- 安全处理环境变量

### SEO和元管理
- 使用Astro的内置SEO组件和元标签管理
- 实施适当的Open Graph和Twitter Card元数据
- 自动生成站点地图以改善搜索索引
- 使用语义HTML结构改善可访问性和SEO
- 实施结构化数据（JSON-LD）以获得丰富摘要
- 为搜索引擎优化页面标题和描述

### 图像优化
- 使用Astro的`<Image />`组件进行自动优化
- 实施具有适当srcset生成的响应式图像
- 为现代浏览器使用WebP和AVIF格式
- 懒加载折叠以下的图像
- 为可访问性提供适当的alt文本
- 在构建时优化图像以获得更好性能

### 数据获取
- 在组件frontmatter中在构建时获取数据
- 使用动态导入进行条件数据加载
- 为外部API调用实施适当的错误处理
- 在构建过程中缓存昂贵操作
- 使用Astro的内置fetch与自动TypeScript推断
- 适当处理加载状态和回退

### 构建和部署
- 使用Astro的内置优化优化静态资源
- 为静态（SSG）或混合（SSR）渲染配置部署
- 使用环境变量进行配置管理
- 为生产构建启用压缩和缓存

## 关键Astro v5.0更新

### 破坏性更改
- **ClientRouter**：使用`<ClientRouter />`而不是`<ViewTransitions />`
- **TypeScript**：在`.astro/types.d.ts`中自动生成类型（运行`astro sync`）
- **Content Layer API**：新的`glob()`和`file()`加载器以增强性能

### 迁移示例
```typescript
// 现代Content Layer API
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({ title: z.string(), pubDate: z.date() })
});
```

## 实施指南

### 开发工作流
1. 使用TypeScript模板通过`npm create astro@latest`创建
2. 使用适当的加载器配置Content Layer API
3. 使用`astro sync`进行类型生成设置TypeScript
4. 使用Islands架构创建布局组件
5. 实施具有SEO和性能优化的内容页面

### Astro特定最佳实践
- **Islands架构**：服务器优先，使用客户端指令进行选择性水合
- **Content Layer API**：使用`glob()`和`file()`加载器进行可扩展内容管理
- **零JavaScript**：默认静态渲染，仅在需要时添加交互性
- **View Transitions**：使用`<ClientRouter />`启用类似SPA的导航
- **类型安全**：利用Content Collections的自动生成类型
- **性能**：使用内置图像优化和最小客户端包进行优化