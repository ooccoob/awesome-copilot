---
description: 'Svelte 5 and SvelteKit development standards and best practices for component-based user interfaces and full-stack applications'
applyTo: '**/*.svelte, **/*.ts, **/*.js, **/*.css, **/*.scss, **/*.json'
---

# Svelte 5 和 SvelteKit 开发说明

使用基于符文的现代反应性、TypeScript 和性能优化构建高质量 Svelte 5 和 SvelteKit 应用程序的说明。

## 项目背景
- Svelte 5.x 与符文系统（$state、$衍生、$effect、$props、$bindable）
- SvelteKit 用于具有基于文件的路由的全栈应用程序
- TypeScript 可实现类型安全和更好的开发人员体验
- 具有 CSS 自定义属性的组件范围样式
- 渐进增强和性能优先的方法
- 具有优化功能的现代构建工具 (Vite)

## 核心概念

### 建筑
- 使用 Svelte 5 符文系统进行所有反应，而不是遗留商店
- 按功能或领域组织组件以实现可扩展性
- 将表示组件与逻辑密集型组件分开
- 将可重用逻辑提取为可组合函数
- 使用槽和片段实现正确的组件组合
- 使用 SvelteKit 基于文件的路由和适当的加载函数

### 组件设计
- 遵循组件的单一责任原则
- 默认使用 `<script lang="ts">` 和 runes 语法
- 保持组件较小并专注于一个问题
- 使用 TypeScript 注释实现正确的 prop 验证
- 使用 `{#snippet}` 块在组件内实现可重用的模板逻辑
- 使用槽进行组件组合和内容投影
- 传递 `children` 片段以实现灵活的父子组合
- 设计可测试和可重用的组件

## 反应性和状态

### Svelte 5 符文系统
- 使用 `$state()` 进行反应式本地状态管理
- 为计算值和昂贵的计算实现 `$derived()`
- 使用 `$derived.by()` 进行简单表达式之外的复杂计算
- 谨慎使用 `$effect()` - 更喜欢使用 `$derived` 或函数绑定来进行状态同步
- 实现 `$effect.pre()` 以在 DOM 更新之前运行代码
- 使用 `untrack()` 防止在效果中读/写相同状态时出现无限循环
- 使用 `$props()` 定义组件属性并使用 TypeScript 注释进行解构
- 使用 `$bindable()` 进行组件之间的双向数据绑定
- 从传统商店迁移到符文以获得更好的性能
- 直接覆盖乐观 UI 模式的派生值 (Svelte 5.25+)

### 状态管理
- 使用 `$state()` 作为本地组件状态
- 使用 `createContext()` 帮助程序在原始 `setContext`/`getContext` 上实现类型安全上下文
- 使用上下文 API 来共享组件树下的反应状态
- 避免 SSR 的全局 `$state` 模块 - 使用上下文来防止交叉请求数据泄漏
- 需要时使用 SvelteKit 存储全局应用程序状态
- 保持复杂数据结构的状态标准化
- 对于计算值，优先使用 `$derived()` 而不是 `$effect()`
- 为客户端数据实现适当的状态持久性

### 效果最佳实践
- **避免**使用 `$effect()` 来同步状态 - 使用 `$derived()` 代替
- **请**使用 `$effect()` 来产生副作用：分析、日志记录、DOM 操作
- **做**从效果中返回清理函数以进行正确的拆卸
- 当代码必须在 DOM 更新之前运行时（例如，滚动位置），请使用 `$effect.pre()`
- 使用 `$effect.root()` 在组件生命周期之外手动控制效果
- 使用 `untrack()` 读取状态而不在效果中创建依赖关系
- 请记住：effects 中的异步代码不会跟踪 `await` 之后的依赖关系

## SvelteKit 模式

### 路由和布局
- 将 `+page.svelte` 用于具有适当 SEO 的页面组件
- 实现 `+layout.svelte` 来共享布局和导航
- 使用 SvelteKit 基于文件的系统处理路由

### 数据加载和突变
- 使用 `+page.server.ts` 进行服务器端数据加载和 API 调用
- 在 `+page.server.ts` 中实现数据突变的表单操作
- 将 `+server.ts` 用于 API 端点和服务器端逻辑
- 使用 SvelteKit 的加载函数进行服务器端和通用数据获取
- 实现正确的加载、错误和成功状态
- 通过服务器加载函数中的承诺处理流数据
- 使用 `invalidate()` 和 `invalidateAll()` 进行缓存管理
- 实施乐观更新以获得更好的用户体验
- 优雅地处理离线场景和网络错误

### 表格和验证
- 使用 SvelteKit 的表单操作进行服务器端表单处理
- 使用 `use:enhance` 实现渐进增强
- 使用 `bind:value` 进行受控表单输入
- 验证客户端和服务器端的数据
- 处理文件上传和复杂表单场景
- 使用标签和 ARIA 属性实现适当的可访问性

## 用户界面和样式

### 造型
- 将组件范围的样式与 `<style>` 块一起使用
- 为主题和设计系统实现 CSS 自定义属性
- 使用 `class:` 指令进行条件样式设置
- 遵循 BEM 或实用程序优先的 CSS 约定
- 使用移动优先方法实施响应式设计
- 对于真正的全局样式，请谨慎使用 `:global()`

### 过渡和动画
- 使用 `transition:` 指令进行进入/退出动画（淡入淡出、滑动、缩放、飞行）
- 使用 `in:` 和 `out:` 进行单独的进入/退出转换
- 使用 `flip` 实现 `animate:` 指令以实现平滑的列表重新排序
- 为品牌运动设计创建自定义过渡
- 使用 `|local` 修饰符仅在直接更改时触发转换
- 将过渡与带键的 `{#each}` 块组合起来以实现列表动画

## TypeScript 和工具

### TypeScript 集成
- 在 `tsconfig.json` 中启用严格模式以获得最大类型安全性
- 使用 TypeScript 注释 props：`let { name }: { name: string } = $props()`
- 类型事件处理程序、引用和 SvelteKit 生成的类型
- 对可重用组件使用泛型类型
- 利用 SvelteKit 生成的 `$types.ts` 文件
- 使用 `svelte-check` 实施正确的类型检查
- 尽可能使用类型推断来减少样板代码

### 开发工具
- 将 ESLint 与 eslint-plugin-svelte 和 Prettier 结合使用以实现代码一致性
- 使用 Svelte DevTools 进行调试和性能分析
- 保持依赖项最新并审核安全漏洞
- 使用 JSDoc 记录复杂的组件和逻辑
- 遵循 Svelte 的命名约定（组件采用 PascalCase，函数采用 CamelCase）

## 生产准备情况

### 性能优化
- 使用带键的 `{#each}` 块进行高效的列表渲染
- 使用动态导入和 `<svelte:component>` 实现延迟加载
- 使用 `$derived()` 进行昂贵的计算以避免不必要的重新计算
- 对于需要多个语句的复杂派生值，请使用 `$derived.by()`
- 避免使用 `$effect()` 来表示派生状态 - 它的效率低于 `$derived()`
- 利用 SvelteKit 的自动代码分割和预加载
- 通过 Tree Shaking 和正确的导入来优化包大小
- 使用 Svelte DevTools 进行分析以识别性能瓶颈
- 在抽象中使用 `$effect.tracking()` 有条件地创建反应式侦听器

### 错误处理
- 为路由级错误边界实现 `+error.svelte` 页面
- 在加载函数和表单操作中使用 try/catch 块
- 提供有意义的错误消息和后备 UI
- 适当记录错误以进行调试和监控
- 通过适当的用户反馈处理表单中的验证错误
- 使用 SvelteKit 的 `error()` 和 `redirect()` 帮助程序获得正确的响应
- 使用 `$effect.pending()` 跟踪待处理的承诺以获取加载状态

### 测试
- 使用 Vitest 和测试库为组件编写单元测试
- 测试组件行为，而不是实现细节
- 使用 Playwright 对用户工作流程进行端到端测试
- 模拟 SvelteKit 的加载函数并适当存储
- 彻底测试表单操作和 API 端点
- 使用 axe-core 实施可访问性测试

### 安全性
- 清理用户输入以防止 XSS 攻击
- 小心使用 `@html` 指令并验证 HTML 内容
- 使用 SvelteKit 实施适当的 CSRF 保护
- 验证和清理加载函数和表单操作中的数据
- 对所有外部 API 调用和生产部署使用 HTTPS
- 通过适当的会话管理安全地存储敏感数据

### 无障碍
- 使用语义 HTML 元素和正确的标题层次结构
- 为所有交互元素实现键盘导航
- 提供正确的 ARIA 标签和描述
- 确保颜色对比度符合 WCAG 准则
- 使用屏幕阅读器和辅助工具进行测试
- 对动态内容实施焦点管理

### 部署
- 使用环境变量进行不同部署阶段的配置
- 使用 SvelteKit 的元标记和结构化数据实施适当的 SEO
- 根据托管平台使用适当的 SvelteKit 适配器进行部署

## 实施流程
1. 使用 TypeScript 和所需的适配器初始化 SvelteKit 项目
2. 使用正确的文件夹组织设置项目结构
3. 定义 TypeScript 接口和组件属性
4. 使用 Svelte 5 runes 实现核心组件
5. 使用 SvelteKit 添加路由、布局和导航
6. 实现数据加载和表单处理
7. 添加具有自定义属性和响应式设计的样式系统
8. 实现错误处理和加载状态
9. 添加全面的测试覆盖范围
10. 优化性能和捆绑包大小
11. 确保无障碍合规性
12. 使用适当的 SvelteKit 适配器进行部署

## 常见模式
- 带插槽的无渲染组件可实现灵活的 UI 组合
- 用于横切关注点和 DOM 操作的自定义操作（`use:` 指令）
- `{#snippet}` 块用于组件内可重用的模板逻辑
- 具有 `createContext()` 的类型安全上下文，用于组件树状态共享
- 使用 `use:enhance` 逐步增强表单和交互功能
- 服务器端渲染与客户端水合以获得最佳性能
- 用于双向绑定的函数绑定 (`bind:value={() => value, setValue}`)
- 避免使用 `$effect()` 进行状态同步 - 使用 `$derived()` 或回调代替
