---
description: 'Svelte 5和SvelteKit开发标准和最佳实践，用于基于组件的用户界面和全栈应用程序'
applyTo: '**/*.svelte, **/*.ts, **/*.js, **/*.css, **/*.scss, **/*.json'
---

# Svelte 5和SvelteKit开发指令

使用现代runes-based响应性、TypeScript和性能优化构建高质量Svelte 5和SvelteKit应用程序的指令。

## 项目上下文
- Svelte 5.x，具有runes系统（$state, $derived, $effect, $props, $bindable）
- SvelteKit用于具有基于文件路由的全栈应用程序
- TypeScript用于类型安全和更好的开发体验
- 具有CSS自定义属性的组件范围样式
- 渐进增强和性能优先方法
- 现代构建工具（Vite）配合优化

## 开发标准

### 架构
- 对所有响应性使用Svelte 5 runes系统而不是遗留stores
- 按功能或域组织组件以实现可扩展性
- 将展示组件与重逻辑组件分离
- 将可重用逻辑提取到可组合函数中
- 使用插槽和片段实施适当的组件组合
- 使用SvelteKit的基于文件的路由配合适当的load函数

### TypeScript集成
- 在`tsconfig.json`中启用严格模式以获得最大类型安全
- 使用`$props()`语法定义组件props接口
- 类型化事件处理器、refs和SvelteKit生成的类型
- 对可重用组件使用泛型类型
- 利用SvelteKit生成的`$types.ts`文件
- 使用`svelte-check`实施适当的类型检查

### 组件设计
- 遵循组件单一职责原则
- 默认使用带runes语法的`<script lang="ts">`
- 保持组件小且专注于一个关注点
- 使用TypeScript实施适当的prop验证
- 使用插槽和片段进行灵活组合
- 设计组件可测试和可重用

### Svelte 5 Runes系统
- 使用`$state()`进行响应式本地状态管理
- 实施`$derived()`进行计算值和昂贵计算
- 使用`$effect()`进行具有适当清理的副作用
- 使用`$props()`和解构定义组件props
- 使用`$bindable()`进行组件间的双向数据绑定
- 从遗留stores迁移到runes以获得更好性能

### 状态管理
- 对本地组件状态使用`$state()`
- 使用`setContext`/`getContext`的上下文API进行共享状态
- 在需要时对全局应用程序状态使用SvelteKit stores
- 对复杂数据结构保持状态规范化
- 对计算值使用派生状态
- 对客户端数据实施适当的状态持久化

### SvelteKit模式
- 对具有适当SEO的页面组件使用`+page.svelte`
- 实施`+layout.svelte`进行共享布局和导航
- 使用`+page.server.ts`进行服务器端数据加载和API调用
- 在`+page.server.ts`中实施表单actions进行数据变更
- 使用`+server.ts`进行API端点和服务器端逻辑
- 使用SvelteKit的基于文件系统处理路由

### 样式
- 使用带有`<style>`块的组件范围样式
- 实施CSS自定义属性进行主题化和设计系统
- 使用`class:`指令进行条件样式化
- 遵循BEM或实用程序优先CSS约定
- 使用移动优先方法实施响应式设计
- 谨慎使用`:global()`进行真正的全局样式

### 性能优化
- 使用键控的`{#each}`块进行高效列表渲染
- 使用动态导入和`svelte:component`实施懒加载
- 使用`$derived()`进行昂贵计算以避免不必要的重新计算
- 利用SvelteKit的自动代码分割和预加载
- 通过树摇和适当导入优化包大小
- 使用Svelte DevTools分析以识别性能瓶颈

### 数据获取
- 使用SvelteKit的load函数进行服务器端和通用数据获取
- 实施适当的加载、错误和成功状态
- 在服务器load函数中使用promises处理流式数据
- 使用`invalidate()`和`invalidateAll()`进行缓存管理
- 实施乐观更新以获得更好的用户体验
- 优雅处理离线场景和网络错误

### 错误处理
- 实施`+error.svelte`页面进行路由级错误边界
- 在load函数和表单actions中使用try/catch块
- 提供有意义的错误消息和回退UI
- 适当记录错误以便调试和监控
- 在表单中使用适当的用户反馈处理验证错误
- 使用SvelteKit的错误和重定向助手

### 表单和验证
- 使用SvelteKit的表单actions进行服务器端表单处理
- 使用`use:enhance`实施渐进增强
- 对受控表单输入使用`bind:value`
- 客户端和服务器端都验证数据
- 处理文件上传和复杂表单场景
- 使用标签和ARIA属性实施适当的可访问性

### 测试
- 使用Vitest和Testing Library为组件编写单元测试
- 测试组件行为，而不是实现细节
- 使用Playwright进行用户工作流的端到端测试
- 适当模拟SvelteKit的load函数和stores
- 彻底测试表单actions和API端点
- 使用axe-core实施可访问性测试

### 安全性
- 清理用户输入以防止XSS攻击
- 谨慎使用`@html`指令并验证HTML内容
- 使用SvelteKit实施适当的CSRF保护
- 在load函数和表单actions中验证和清理数据
- 对所有外部API调用和生产部署使用HTTPS
- 使用适当的会话管理安全存储敏感数据

### 可访问性
- 使用语义HTML元素和适当的标题层次结构
- 为所有交互元素实施键盘导航
- 提供适当的ARIA标签和描述
- 确保颜色对比符合WCAG指南
- 使用屏幕阅读器和可访问性工具进行测试
- 为动态内容实施焦点管理

## 实施过程
1. 使用TypeScript和所需适配器初始化SvelteKit项目
2. 使用适当的文件夹组织设置项目结构
3. 定义TypeScript接口和组件props
4. 使用Svelte 5 runes实施核心组件
5. 使用SvelteKit添加路由、布局和导航
6. 实施数据加载和表单处理
7. 使用自定义属性和响应式设计添加样式系统
8. 实施错误处理和加载状态
9. 添加全面的测试覆盖
10. 优化性能和包大小
11. 确保可访问性合规
12. 使用适当的SvelteKit适配器部署

## 附加指南
- 遵循Svelte的命名约定（组件使用PascalCase，函数使用camelCase）
- 使用eslint-plugin-svelte的ESLint和Prettier保持代码一致性
- 保持依赖项最新并审计安全漏洞
- 使用JSDoc记录复杂组件和逻辑
- 使用Svelte DevTools进行调试和性能分析
- 使用SvelteKit的元标签和结构化数据实施适当的SEO
- 为不同部署阶段使用环境变量进行配置

## 常见模式
- 使用插槽进行灵活UI组合的无渲染组件
- 用于横切关注点和DOM操作的自定义指令
- 用于可重用模板逻辑的基于片段的组合
- 用于应用程序范围状态管理的上下文提供者
- 用于表单和交互功能的渐进增强
- 使用客户端水合的服务器端渲染以获得最佳性能