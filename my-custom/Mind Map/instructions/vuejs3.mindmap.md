## What
- Vue 3 + Composition API + TS 的工程规范：组件、Pinia、路由、数据获取、样式、性能、安全、测试与可达性

## When
- 新建/重构 Vue3 项目或沉淀最佳实践时

## Why
- 通过组合式 API、类型与可复用 composables 获得高可维护性与高性能

## How
- 架构
  - Composition API 与 composables/ 按域组织；展示组件 vs 容器组件；Pinia 按域拆 store
- TypeScript
  - <script setup lang="ts"> + defineProps/defineEmits/PropType；为路由 hooks、事件与复杂形状建类型
- 组件
  - 单一职责；PascalCase 组件名、kebab 文件名；slots/scoped slots 组合
- 状态
  - 本地 ref/reactive + computed；全局 Pinia defineStore（state/getters/actions）；插件做持久化/调试
- 组合式模式
  - 可复用 useXxx（useFetch/useAuth）；watch/watchEffect 精准依赖；onUnmounted 清理；有限 provide/inject
- 样式
  - <style scoped>/CSS Modules；Tailwind 可选；BEM/功能化命名；CSS 变量做主题；移动优先
- 性能
  - defineAsyncComponent 懒加载；<Suspense> 回退；v-once/v-memo；避免多余 watcher；DevTools 性能分析；Vite 摇树
- 数据
  - useFetch/Vue Query；显式加载/错误/成功；取消陈旧请求；乐观更新与回滚；缓存+后台再验证
- 错误
  - app.config.errorHandler；errorCaptured 局部边界；try/catch 友好提示与外部日志
- 表单
  - VeeValidate/@vueuse/form；受控 v-model；防抖校验；可复用多步表单逻辑
- 路由
  - Vue Router 4：嵌套路由/代码分割；守卫 beforeEach/beforeEnter；useRoute/useRouter；meta 做面包屑
- 安全/a11y
  - 避免 v-html；CSP；模板转义；HTTPS；token 放 HttpOnly；语义化+键盘导航+对比度
- 测试
  - Vue Test Utils+Jest；mock 路由/Pinia；E2E(Cypress/Playwright)；axe 可达性

## Key Points
- 组合式 API 与 composables 是复用与测试的核心
- 懒加载+Suspense 优化首屏与异步体验

## Compact Map
- 组件: SRP/slots
- 状态: Pinia/ref/reactive
- 数据: fetch/query/cancel
- 样式: scoped/Tailwind
- 性能: async/suspense/memo
- 错误: 全局/局部/日志
- 路由: 守卫/meta
- 安全: 转义/CSP/HttpOnly

## Example Questions
1) 何时应将逻辑抽为 composable 而非 mixin？
2) defineProps/defineEmits 的类型声明最佳方式？
3) Pinia action 与组件内异步应如何划分？
4) watch vs watchEffect 的适用差异？
5) 如何实现请求取消与乐观更新回滚？
6) 哪些组件适合 defineAsyncComponent？
7) 全局错误处理与 errorCaptured 如何协同？
8) 表单校验如何做去抖与可达性提示？
9) 路由守卫与 meta 面包屑如何组织？
10) 如何落地 CSP 并禁止风险性的 v-html？
11) E2E 测试应覆盖哪些关键路径？

Source: d:\mycode\awesome-copilot\instructions\vuejs3.instructions.md | Generated: 2025-10-17
