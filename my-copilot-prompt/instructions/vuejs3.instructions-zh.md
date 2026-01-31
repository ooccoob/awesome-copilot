---
描述：“VueJS 3 开发标准以及 Composition API 和 TypeScript 的最佳实践”
applyTo: '**/*.vue, **/*.ts, **/*.js, **/*.scss'
---

# VueJS 3 开发说明

使用 Composition API、TypeScript 和现代最佳实践构建高质量 VueJS 3 应用程序的说明。

## 项目背景
- Vue 3.x 默认使用 Composition API
- 用于类型安全的 TypeScript
- 具有 `<script setup>` 语法的单文件组件 (`.vue`)
- 现代构建工具（Vite 推荐）
- Pinia 用于应用程序状态管理
- 官方 Vue 风格指南和最佳实践

## 开发标准

### 建筑
- 与选项 API 相比，更喜欢组合 API（`setup` 函数和可组合项）
- 按功能或领域组织组件和可组合项以实现可扩展性
- 将以 UI 为中心的组件（演示）与以逻辑为中心的组件（容器）分开
- 将可重用逻辑提取到 `composables/` 目录中的可组合函数中
- 按域构建存储模块 (Pinia)，并具有明确定义的操作、状态和 getter

### TypeScript 集成
- 在 `tsconfig.json` 中启用 `strict` 模式以获得最大类型安全性
- 将 `defineComponent` 或 `<script setup lang="ts">` 与 `defineProps` 和 `defineEmits` 一起使用
- 利用 `PropType<T>` 来获取类型化的 props 和默认值
- 对复杂的 prop 和状态形状使用接口或类型别名
- 定义事件处理程序、引用和 `useRoute`/`useRouter` 挂钩的类型
- 在适用的情况下实现通用组件和可组合项

### 组件设计
- 坚持组件的单一责任原则
- 使用 PascalCase 作为组件名称，使用 kebab-case 作为文件名
- 保持组件较小并专注于一个问题
- 为了简洁和提高性能，使用 `<script setup>` 语法
- 使用 TypeScript 验证 props；仅在必要时使用运行时检查
- 支持插槽和作用域插槽以实现灵活的组合

### 状态管理
- 使用 Pinia 进行全局状态：使用 `defineStore` 定义存储
- 对于简单的本地状态，请在 `setup` 中使用 `ref` 和 `reactive`
- 使用 `computed` 表示派生状态
- 保持复杂结构的状态标准化
- 使用 Pinia 存储中的操作来实现异步逻辑
- 利用存储插件进行持久化或调试

### 组合 API 模式
- 为共享逻辑创建可重用的可组合项，例如 `useFetch`、`useAuth`
- 使用 `watch` 和 `watchEffect` 以及精确的依赖项列表
- `onUnmounted` 或 `watch` 清理回调中的清理副作用
- 谨慎使用 `provide`/`inject` 进行深度依赖注入
- 使用 `useAsyncData` 或第三方数据实用程序（Vue Query）

### 造型
- 将 `<style scoped>` 用于组件级样式或 CSS 模块
- 考虑使用实用程序优先的框架（Tailwind CSS）来快速设计样式
- 类命名遵循 BEM 或函数式 CSS 约定
- 利用 CSS 自定义属性进行主题化和设计标记
- 使用 CSS Grid 和 Flexbox 实施移动优先的响应式设计
- 确保样式可访问（对比度、焦点状态）

### 性能优化
- 具有动态导入和 `defineAsyncComponent` 的延迟加载组件
- 使用 `<Suspense>` 进行异步组件加载后备
- 对静态或不经常更改的元素应用 `v-once` 和 `v-memo`
- 使用 Vue DevTools Performance 选项卡进行配置
- 避免不必要的观察；尽可能首选 `computed`
- Tree-shake 未使用的代码并利用 Vite 的优化功能

### 数据获取
- 使用 `useFetch` (Nuxt) 等可组合项或 Vue Query 等库
- 显式处理加载、错误和成功状态
- 取消组件卸载或参数更改的陈旧请求
- 实施乐观更新并在失败时回滚
- 缓存响应并使用后台重新验证

### 错误处理
- 使用全局错误处理程序 (`app.config.errorHandler`) 处理未捕获的错误
- 将有风险的逻辑包装在 `try/catch` 中；提供用户友好的消息
- 在组件中使用 `errorCaptured` 钩子作为局部边界
- 优雅地显示后备 UI 或错误警报
- 将错误记录到外部服务（Sentry、LogRocket）

### 表格和验证
- 使用 VeeValidate 或 @vueuse/form 等库进行声明性验证
- 使用受控的 `v-model` 绑定构建表单
- 通过去抖动验证模糊或输入以提高性能
- 在可组合项中处理文件上传和复杂的多步骤表单
- 确保可访问的标签、错误公告和焦点管理

### 路由
- 将 Vue Router 4 与 `createRouter` 和 `createWebHistory` 一起使用
- 实现嵌套路由和路由级代码分割
- 使用导航守卫保护路线（`beforeEnter`、`beforeEach`）
- 在 `setup` 中使用 `useRoute` 和 `useRouter` 进行编程导航
- 正确管理查询参数和动态段
- 通过路由元字段实现面包屑数据

### 测试
- 使用 Vue Test Utils 和 Vitest 编写单元测试
- 关注行为，而不是实施细节
- 使用 `mount` 和 `shallowMount` 进行组件隔离
- 根据需要模拟全局插件（路由器、Pinia）
- 使用 Cypress 或 Playwright 添加端到端测试
- 使用 axe-core 集成测试可访问性

### 安全性
- 避免使用 `v-html`；严格清理任何 HTML 输入
- 使用 CSP 标头减轻 XSS 和注入攻击
- 验证和转义模板和指令中的数据
- 对所有 API 请求使用 HTTPS
- 将敏感令牌存储在仅限 HTTP 的 cookie 中，而不是 `localStorage`

### 无障碍
- 使用语义 HTML 元素和 ARIA 属性
- 管理模式和动态内容的焦点
- 为交互组件提供键盘导航
- 为图像和图标添加有意义的 `alt` 文本
- 确保色彩对比度符合 WCAG AA 标准

## 实施流程
1. 规划组件和可组合架构
2. 使用 Vue 3 和 TypeScript 初始化 Vite 项目
3. 定义 Pinia 存储和可组合项
4. 创建核心 UI 组件和布局
5. 集成路线和导航
6. 实现数据获取和状态逻辑
7. 构建具有验证和错误状态的表单
8. 添加全局错误处理和后备 UI
9. 添加单元和E2E测试
10. 优化性能和捆绑包大小
11. 确保无障碍合规性
12. 文档组件、可组合项和存储

## 附加指南
- 遵循 Vue 的官方风格指南 (vuejs.org/style-guide)
- 使用 ESLint（带有 `plugin:vue/vue3-recommended`）和 Prettier 来保证代码一致性
- 编写有意义的提交消息并维护干净的 git 历史记录
- 保持依赖项最新并审核漏洞
- 使用 JSDoc/TSDoc 记录复杂逻辑
- 使用 Vue DevTools 进行调试和分析

## 常见模式
- 无渲染组件和作用域插槽可实现灵活的 UI
- 使用提供/注入的复合组件
- 针对跨领域关注点的自定义指令
- 模态和叠加的传送
- 全球实用程序的插件系统（i18n、分析）
- 用于参数化逻辑的可组合工厂
