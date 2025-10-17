## What/When/Why/How
- What: React（19+）现代开发规范（TS/Hook/数据/性能/无障碍）
- When: 新建或重构 React 应用/组件库时
- Why: 可维护、可测试与高性能体验
- How: 函数组件 + 自定义 Hook + 语义化结构 + 现代数据层

## Key Points
- 架构：按特性分层；组件组合优于继承；容器/展示分离
- TS：严格模式；Props/State/事件/泛型类型化
- 状态：useState/useReducer/useContext；跨域用 RTK/Zustand
- 数据：React Query/SWR；加载/错误/缓存/乐观更新
- Hooks：依赖数组正确；清理；useMemo/useCallback 谨慎
- 样式：CSS Modules/Styled；响应式与主题；可达性语义
- 性能：React.memo；lazy+Suspense；虚拟列表；拆包与摇树
- 错误：Error Boundary；降级 UI；日志采集
- 表单：受控组件；校验（RHF/Formik）；可达性
- 路由：嵌套路由/保护；按路由懒加载

## Compact Map
- Components: SRP + composition + custom hooks
- Data: query cache + optimistic + cancel
- Perf: memo/lazy/virtualize
- A11y: roles/labels/contrast

## Example Questions
1) 组件是否单一职责且 props 类型完整？
2) 副作用依赖是否准确并包含清理？
3) 大列表是否使用虚拟滚动与窗口化？
4) 数据请求是否处理竞态/取消/重试？
5) 是否有 Error Boundary 与降级体验？
6) 可达性语义/对比度/键盘导航是否合规？
7) 路由是否懒加载并正确处理保护？
8) 表单校验是否无侵入且具可访问性？
9) 性能瓶颈是否用 Profiler/DevTools 验证？
10) 依赖是否最新且启用 ESLint/Prettier？
11) 复杂 Hook 是否拥有文档与测试？

Source: d:\mycode\awesome-copilot\instructions\reactjs.instructions.md | Generated: 2025-10-17
