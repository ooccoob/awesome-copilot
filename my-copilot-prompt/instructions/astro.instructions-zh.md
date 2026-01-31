---
描述：“内容驱动网站的 Astro 开发标准和最佳实践”
applyTo: '**/*.astro, **/*.ts, **/*.js, **/*.md, **/*.mdx'
---

# Astro 开发说明

遵循内容驱动、服务器优先架构和现代最佳实践构建高质量 Astro 应用程序的说明。

## 项目背景
- 具有岛屿架构和内容层 API 的 Astro 5.x
- TypeScript 可实现类型安全并通过自动生成类型提供更好的 DX
- 内容驱动的网站（博客、营销、电子商务、文档）
- 具有选择性客户端水合作用的服务器优先渲染
- 支持多种 UI 框架（React、Vue、Svelte、Solid 等）
- 默认情况下，静态站点生成 (SSG) 具有可选的服务器端渲染 (SSR)
- 通过现代内容加载和构建优化增强性能

## 开发标准

### 建筑
- 拥抱岛屿架构：默认服务器渲染，选择性水合
- 使用内容集合组织内容以进行类型安全的 Markdown/MDX 管理
- 按功能或内容类型构建项目以实现可扩展性
- 使用基于组件的架构并明确关注点分离
- 实施渐进增强模式
- 遵循多页面应用程序 (MPA) 方法而不是单页面应用程序 (SPA) 模式

### TypeScript 集成
- 使用推荐的 v5.0 设置配置 `tsconfig.json`：
```json
{
  "extends": "astro/tsconfigs/base",
  "include": [".astro/types.d.ts", "**/*"],
  "exclude": ["dist"]
}
```
- 在 `.astro/types.d.ts` 中自动生成的类型（替换 `src/env.d.ts`）
- 运行 `astro sync` 来生成/更新类型定义
- 使用 TypeScript 接口定义组件 props
- 利用内容集合和内容层 API 自动生成的类型

### 组件设计
- 将 `.astro` 组件用于静态、服务器渲染的内容
- 仅在需要交互时导入框架组件（React、Vue、Svelte）
- 遵循 Astro 的组件脚本结构：frontmatter 位于顶部，template 位于下方
- 遵循 PascalCase 约定使用有意义的组件名称
- 保持组件的集中性和可组合性
- 实施适当的道具验证和默认值

### 内容集

#### 现代内容层 API (v5.0+)
- 使用新的内容层 API 在 `src/content.config.ts` 中定义集合
- 使用内置加载器：`glob()` 用于基于文件的内容，`file()` 用于单个文件
- 通过新的加载系统利用增强的性能和可扩展性
- 内容层 API 示例：
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

#### 旧版集合（向后兼容）
- 仍然通过自动 glob() 实现支持旧版 `type: 'content'` 集合
- 通过添加显式 `loader` 配置来迁移现有集合
- 使用带有 `getCollection()` 和 `getEntry()` 的类型安全查询
- 通过 frontmatter 验证和自动生成的类型来构建内容

### 查看转换和客户端路由
- 在布局头中使用 `<ClientRouter />` 组件启用（从 v5.0 中的 `<ViewTransitions />` 重命名）
- 从 `astro:transitions` 导入：`import { ClientRouter } from 'astro:transitions'`
- 提供类似 SPA 的导航，无需重新加载整个页面
- 使用 CSS 和 view-transition-name 自定义过渡动画
- 使用持久岛维护跨页面导航的状态
- 使用 `transition:persist` 指令来保留组件状态

### 性能优化
- 默认为零 JavaScript - 仅在需要时添加交互性
- 策略性地使用客户端指令（`client:load`、`client:idle`、`client:visible`）
- 实现图像和组件的延迟加载
- 使用 Astro 的内置优化来优化静态资源
- 利用内容层 API 加快内容加载和构建速度
- 通过避免不必要的客户端 JavaScript 来最小化包大小

### 造型
- 默认情况下在 `.astro` 组件中使用作用域样式
- 需要时实施 CSS 预处理（Sass、Less）
- 将 CSS 自定义属性用于主题和设计系统
- 遵循移动优先的响应式设计原则
- 通过语义 HTML 和适当的 ARIA 属性确保可访问性
- 考虑使用实用程序优先的框架（Tailwind CSS）进行快速开发

### 客户端交互
- 将框架组件（React、Vue、Svelte）用于交互元素
- 根据用户交互模式选择正确的水合策略
- 在框架边界内实施状态管理
- 仔细处理客户端路由以保持 MPA 优势
- 使用 Web 组件实现与框架无关的交互
- 使用商店或自定义事件在岛屿之间共享状态

### API 路由和 SSR
- 在 `src/pages/api/` 中创建 API 路由以实现动态功能
- 使用正确的 HTTP 方法和状态代码
- 实施请求验证和错误处理
- 启用 SSR 模式以满足动态内容要求
- 使用中间件进行身份验证和请求处理
- 安全地处理环境变量

### SEO 和元管理
- 使用 Astro 的内置 SEO 组件和元标记管理
- 实施适当的开放图谱和 Twitter 卡元数据
- 自动生成站点地图以获得更好的搜索索引
- 使用语义 HTML 结构以获得更好的可访问性和 SEO
- 为丰富的摘要实施结构化数据 (JSON-LD)
- 优化搜索引擎的页面标题和描述

### 图像优化
- 使用Astro的`<Image />`组件进行自动优化
- 通过正确的 srcset 生成来实现响应式图像
- 对现代浏览器使用 WebP 和 AVIF 格式
- 延迟加载首屏下方的图像
- 提供适当的替代文本以实现可访问性
- 在构建时优化图像以获得更好的性能

### 数据获取
- 在构建时在组件 frontmatter 中获取数据
- 使用动态导入进行条件数据加载
- 对外部 API 调用实施正确的错误处理
- 在构建过程中缓存昂贵的操作
- 使用 Astro 的内置 fetch 和自动 TypeScript 推理
- 适当处理加载状态和回退

### 构建和部署
- 使用 Astro 的内置优化来优化静态资源
- 配置静态 (SSG) 或混合 (SSR) 渲染的部署
- 使用环境变量进行配置管理
- 为生产版本启用压缩和缓存

## Astro v5.0 主要更新

### 重大变化
- **ClientRouter**：使用 `<ClientRouter />` 而不是 `<ViewTransitions />`
- **TypeScript**：`.astro/types.d.ts` 中自动生成的类型（运行 `astro sync`）
- **内容层 API**：新的 `glob()` 和 `file()` 加载器可增强性能

### 迁移示例
```typescript
// Modern Content Layer API
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({ title: z.string(), pubDate: z.date() })
});
```

## 实施指南

### 开发流程
1. 将 `npm create astro@latest` 与 TypeScript 模板结合使用
2. 使用适当的加载器配置内容层 API
3. 使用 `astro sync` 设置 TypeScript 以生成类型
4. 使用Islands Architecture创建布局组件
5. 通过 SEO 和性能优化实施内容页面

### Astro 特定最佳实践
- **岛屿架构**：服务器优先，使用客户端指令进行选择性水合作用
- **内容层 API**：使用 `glob()` 和 `file()` 加载器进行可扩展的内容管理
- **零 JavaScript**：默认静态渲染，仅在需要时添加交互性
- **视图转换**：使用 `<ClientRouter />` 启用类似 SPA 的导航
- **类型安全**：利用资源库中自动生成的类型
- **性能**：通过内置图像优化和最少的客户端捆绑包进行优化
