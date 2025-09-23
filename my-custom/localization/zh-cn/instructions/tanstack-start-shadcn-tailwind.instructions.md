---
applyTo: "tanstack-start-shadcn-tailwind.instructions.md"
---

<!-- 本文件为自动翻译，供参考。请结合实际需求进行校对和完善。-->

# TanStack Start 应用开发规范

## 1. 结构与组织

- **推荐用标准目录结构**：`app/` 路由、`components/` 组件、`lib/` 工具、`styles/` 样式等。
- **按功能分组，避免深层嵌套**。
- **所有源代码建议放在 `src/` 下**。

## 2. 组件与样式

- **组件用 PascalCase 命名，单文件单组件**。
- **样式优先用 Tailwind CSS，避免全局样式污染**。
- **可复用组件放 `components/`，页面专用组件放对应路由目录**。

## 3. 状态与数据

- **本地状态用 React useState/useReducer**。
- **全局状态推荐用 TanStack Query、Zustand 等**。
- **数据获取用 TanStack Query，避免在组件中直接 fetch**。

## 4. 代码风格与质量

- **统一用 ESLint + Prettier**，CI 强制检查。
- **变量、函数、组件命名语义化，避免缩写和拼音**。
- **Props 用 TypeScript 明确类型**。
- **避免魔法数字和硬编码字符串**。

## 5. 性能与可访问性

- **用 React.memo、useMemo、useCallback 优化渲染**。
- **列表渲染用稳定 key**。
- **组件语义化，合理用 ARIA 属性**。

## 6. 测试

- **用 Vitest/React Testing Library 编写测试**。
- **测试文件与组件同级，命名为 `*.test.tsx`**。
- **测试覆盖率目标 80% 以上**。

## 7. 依赖与安全

- **依赖用 pnpm/yarn/npm 管理，锁定版本**。
- **定期运行 `pnpm audit` 检查安全**。
- **敏感信息用环境变量管理**。

## 8. 质量检查清单

- [ ] 结构清晰，命名规范
- [ ] 组件和样式分离
- [ ] 状态和数据管理合理
- [ ] 类型定义齐全
- [ ] 性能和可访问性达标
- [ ] 测试覆盖率达标
- [ ] 依赖和安全合规

---

免责声明：本翻译仅供参考，具体实践请结合实际项目需求和最新官方文档。
