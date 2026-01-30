## What
- Svelte 5/SvelteKit 开发规范与最佳实践（runes: $state/$derived/$effect/$props/$bindable）
- TS 严格模式、文件式路由、组件职责单一、性能优先

## When
- 新建/重构 Svelte 5 与 SvelteKit 全栈应用
- 需要统一组件、状态、样式与数据加载范式时

## Why
- 更清晰的响应式心智模型（runes）与更强可维护性
- 借助 SvelteKit 的 SSR/路由/表单动作提升 DX 与性能

## How
- 结构
  - feature/domain 组织组件；展示与逻辑分离；可复用逻辑抽到函数/指令
  - SvelteKit: +layout/+page/+page.server/+server 路由与数据/动作
- 类型
  - tsconfig 严格；$props() 定义 props；svelte-check 持续校验
- Runes
  - $state 本地状态；$derived 计算；$effect 副作用清理；$bindable 双向绑定；迁移替代旧 stores
- 数据与缓存
  - load 函数区分 server/通用；invalidate()/invalidateAll()；乐观更新与离线处理
- 样式
  - 组件作用域 <style>；CSS 变量做主题；class: 条件样式；移动优先
- 性能
  - keyed each；懒加载与动态 import；派生值避免重复计算；代码分割/预加载
- 表单
  - use:enhance 渐进增强；服务端动作校验与错误回传；无障碍与可达性
- 错误/安全/可达性
  - +error.svelte 边界；输入校验与 @html 慎用；语义化标签、键盘导航、对比度
- 测试
  - Vitest/Testing Library 组件；Playwright E2E；axe 可达性

## Key Points
- 小而专一组件；插槽/片段组合；context 共享状态
- 使用 locals/通用工具抽象重复逻辑
- 遵循 SvelteKit 代码拆分与预取策略

## Compact Map
- 架构: 组件/路由/布局
- 类型: 严格/生成类型/$types
- 状态: $state/$derived/$effect/$bindable/context
- 数据: load/actions/invalidations
- 样式: scoped/CSS vars/utility
- 性能: keyed/lazy/split/profile
- 表单: enhance/校验/无障碍
- 安全: XSS/CSRF/HTTPS
- 测试: 单元/E2E/a11y

## Example Questions
1) 如何用 $state/$derived 重构旧 store 逻辑？
2) +page.server 与 +server 该放哪些逻辑？
3) use:enhance 表单如何处理校验与错误回显？
4) 何时使用 invalidate vs invalidateAll？
5) 列表渲染为何必须使用 keyed each？
6) 如何组织 feature 级组件与可复用逻辑？
7) 如何用 CSS 变量与 scoped 样式实现主题化？
8) 如何隔离副作用并在组件卸载时清理？
9) 懒加载与 svelte:component 的推荐场景？
10) SvelteKit 中错误边界与 SEO 需注意什么？
11) 如何配置 svelte-check 与 TS 严格类型？

Source: d:\mycode\awesome-copilot\instructions\svelte.instructions.md | Generated: 2025-10-17
