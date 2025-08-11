---
applyTo: "reactjs.instructions.md"
---

<!-- 本文件为自动翻译，供参考。请结合实际需求进行校对和完善。-->

# ReactJS 开发标准与最佳实践

## 1. 组件结构与组织

- **推荐使用函数组件和 Hooks**，避免类组件。
- **每个组件单独一个文件，命名用 PascalCase**。
- **通用组件放在 `components/`，页面级组件放在 `pages/` 或 `views/`**。
- **样式可用 CSS Modules、styled-components 或 Tailwind**，避免全局样式污染。

## 2. 状态管理

- **优先用 React 内部状态（useState/useReducer）管理本地状态**。
- **全局状态推荐用 Context、Redux、Recoil、Zustand 等**。
- **避免不必要的全局状态，提升组件复用性和可维护性**。

## 3. 代码风格与质量

- **统一用 ESLint + Prettier**，并在 CI 强制检查。
- **变量、函数、组件命名语义化，避免缩写和拼音**。
- **Props 用 TypeScript interface/type 明确类型**。
- **避免魔法数字和硬编码字符串，使用常量或配置项**。

## 4. 性能优化

- **用 React.memo、useMemo、useCallback 避免不必要的渲染**。
- **列表渲染用稳定 key，避免用索引**。
- **大数据列表用虚拟滚动（如 react-window）**。
- **懒加载组件和图片，提升首屏速度**。

## 5. 可访问性与国际化

- **组件语义化，合理使用 ARIA 属性**。
- **表单控件用 label 关联**。
- **国际化推荐用 react-intl、i18next 等库**。

## 6. 测试

- **用 React Testing Library、Jest 编写单元和集成测试**。
- **测试文件与组件同级，命名为 `*.test.tsx` 或 `*.spec.tsx`**。
- **测试覆盖率目标 80% 以上**。

## 7. 依赖与安全

- **依赖用 npm/yarn/pnpm 管理，锁定版本**。
- **定期运行 `npm audit` 检查安全漏洞**。
- **敏感信息不得硬编码，配置用环境变量**。

## 8. 质量检查清单

- [ ] 组件结构清晰，命名规范
- [ ] 状态管理合理
- [ ] 类型定义齐全
- [ ] 性能优化到位
- [ ] 可访问性达标
- [ ] 测试覆盖率达标
- [ ] 依赖和安全合规

---

免责声明：本翻译仅供参考，具体实践请结合实际项目需求和最新官方文档。
