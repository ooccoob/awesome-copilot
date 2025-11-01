## What / When / Why / How

- What: Accessibility mode（无障碍优先编码模式）
- When: 任何 UI/前端/可视化交互改动，或需满足 WCAG 2.1 时
- Why: 确保所有用户可用，降低合规与口碑风险
- How: 以可达性四大原则（可感知/可操作/可理解/健壮）驱动代码与校验

## Key Points

- HTML 语义化与 ARIA 正确使用（label-for、role、aria-*）
- 键盘可操作性与焦点管理（Tab 序、可见焦点指示）
- 对比度/色彩非唯一信号/放大缩放适配
- 多媒体字幕/替代文本（img alt）
- 动态内容的可达性（aria-live、焦点迁移）
- 自动化校验：axe-core/pa11y 常态化执行

## Compact Map

- 结构
  - 语义标签：header/main/nav/section/article/footer
  - 表单：label/aria-label/aria-describedby
- 交互
  - 键盘可达：Enter/Space、Esc、方向键
  - 焦点环与顺序、弹窗开闭时焦点管理
- 呈现
  - 对比度≥4.5:1；不依赖颜色编码
  - 响应式与缩放 200% 仍可用
- 动态
  - aria-live/role=alert 更新提示
  - 验证错误的可读播报
- 校验
  - 本地/CI 集成 axe/pa11y

## Example Questions (10+)

- 此组件的语义化结构是否合理？需要哪些 ARIA 属性？
- 键盘导航路径与焦点顺序如何定义与测试？
- 当前配色是否达到对比度标准？有备选主题吗？
- 表单校验错误如何无障碍提示（读屏/视觉）？
- 动态插入的 DOM 如何通知辅助技术（aria-live）？
- 图片/图标/按钮是否都有合适的替代文本？
- 模态弹窗打开/关闭时焦点如何迁移与恢复？
- 有没有为复杂控件提供键盘操作指南？
- 我们如何在 CI 中执行 axe/pa11y 并阻断不合规变更？
- 第三方组件库的可达性缺陷如何规避或补丁？
- 需要哪些 E2E 无障碍用例来覆盖关键路径？

---
Source: d:\mycode\awesome-copilot\chatmodes\accesibility.chatmode.md
Generated: {{timestamp}}
