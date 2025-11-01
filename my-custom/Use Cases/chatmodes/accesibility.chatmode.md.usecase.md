---
post_title: "accesibility — 用例"
post_slug: "accesibility-use-cases"
tags: ['chatmode','accessibility','usecase']
ai_note: '根据 chatmodes/accesibility.chatmode.md 生成的中文用例'
summary: '用于可访问性审计、修复建议与可用性测试脚本生成的场景示例。'
post_date: '2025-10-20'
---

<!-- markdownlint-disable MD041 -->

什么

- 针对网页/应用的可访问性检查、建议与可复用测试脚本或文案修正。

何时

- 在发布迭代前做无障碍合规检查、或在设计阶段嵌入可访问性考量以降低后期返工。

为什么

- 保障不同能力用户的可用体验，符合 WCAG 要求并降低法律与用户风险。

如何

- 提供页面 URL / 代码片段 / 设计稿并指定目标 WCAG 等级；请求生成问题清单、修复步骤和可执行的测试用例。

关键要点 (EN / ZH)

- EN: WCAG-focused checks; assistive technology considerations; remediation steps.
- ZH: 面向 WCAG 的检查；辅助技术兼容性；修复步骤与验证方法。

示例场景

1) 快速页面无障碍检查
- 示例提示："检查 https://example.com/login 页面并列出违反 WCAG 2.1 AA 的点与优先级修复建议。"
- 预期产出：问题清单、修复代码片段与优先级。

2) 生成可执行测试脚本
- 示例提示："为主要表单生成 Playwright/selenium 的可访问性检查脚本，包括键盘导航与 ARIA 验证。"
- 预期产出：可直接运行的测试脚本示例与说明。

3) 无障碍文案重写
- 示例提示："把按钮文案‘点击这里’替换成更语义化的文本并给出 3 个备选。"
- 预期产出：三条语义化文案与适用场景说明。

4) 辅助设备兼容建议
- 示例提示："评估该页面与屏幕阅读器 NVDA/VoiceOver 的兼容性并提出改进点。"
- 预期产出：兼容性问题列表与针对性修复建议。

5) 可访问性验收准则清单
- 示例提示："为团队提供一页可执行的可访问性验收检查清单（移动与桌面）。"
- 预期产出：一页清单，可用于 PR 审查流程。

原始 chatmode: ../../../../chatmodes/accesibility.chatmode.md
---
post_title: "accesibility.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "accessibility-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "wcag", "a11y"]
ai_note: "Generated with AI assistance."
summary: "将 WCAG 2.1 落到具体开发流程：从需求、设计、实现到验证，默认无障碍优先。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 在本仓库的代码生成与修改中，系统性嵌入 WCAG 2.1 四大原则与落地清单（HTML/CSS/JS），并标准化验证工具链（pa11y、axe-core）。

## When

- 新功能/页面开发、样式改造、交互重构、主题与多语言适配、第三方组件接入与升级时。

## Why

- 无障碍是强需求：提升可达性、法律合规、公共价值与商业覆盖；越早介入，返工成本越低。

## How

- 以“可感知、可操作、可理解、健壮”为纲：采用语义化 HTML、可达的交互、清晰的文案与错误提示、正确的 ARIA 与对比度；在 CI 中集成 pa11y/axe 扫描，PR 必过。

## Key points (英文+中文对照)

- Perceivable（可感知）
- Operable（可操作）
- Understandable（可理解）
- Robust（健壮）
- Automate checks（自动化校验）

## 使用场景

### 1. 新页面搭建（New page scaffolding）

- 用户故事：作为前端开发者，我希望从骨架就满足语义化与键盘可达。
- 例 1："生成页面骨架，包含 `main`/`nav`/`section`，并提供跳转到主内容的 skip link。"
- 例 2："设置 `html` 的 `lang` 属性，并规范文档标题层级，禁止跳级。"
- 例 3："示例图片包含合理 alt；装饰图使用空 alt。"
- 例 4："初始样式包含可见的 focus ring 与对比度变量。"
- 例 5："输出 pa11y 与 axe 的本地运行脚本。"

### 2. 表单可达性（Accessible forms）

- 用户故事：作为交互工程师，我要确保表单可被屏幕阅读器与键盘操作顺畅使用。
- 例 1："为控件添加 `label for`，或使用 `aria-label` / `aria-labelledby`。"
- 例 2："错误信息关联控件并使用 aria-live=polite。"
- 例 3："校验失败时，将焦点移动到第一个错误。"
- 例 4："提供必填说明，避免仅颜色提示。"
- 例 5："对日期/组合控件提供键盘操作说明。"

### 3. 动态内容与焦点管理（Dynamic content & focus）

- 用户故事：作为前端开发者，我要在对话框、抽屉与动态列表更新时，正确管理焦点与朗读。
- 例 1："打开对话框时聚焦首个可交互元素，关闭后将焦点还原。"
- 例 2："列表增删使用 aria-live 区域播报变更。"
- 例 3："自定义组件实现 roving tabindex。"
- 例 4："避免强制滚动与焦点陷阱。"
- 例 5："避免 3 次/秒以上闪烁动画。"

### 4. 主题与对比度（Theming & contrast）

- 用户故事：作为样式工程师，我要确保多主题与缩放下仍满足对比度与可读性。
- 例 1："使用 CSS 变量集中管理颜色，提供高对比主题。"
- 例 2："采用 rem/em 相对单位，支持浏览器缩放。"
- 例 3："为焦点态/悬停态提供清晰可见的指示。"
- 例 4："图标与文本组合同时提供文本标签。"
- 例 5："对图表提供数据表与文本摘要。"

### 5. CI 校验与准入门槛（CI gating）

- 用户故事：作为项目维护者，我需要将无障碍检查纳入 PR 准入。
- 例 1："在 CI 工作流中添加 pa11y 与 axe 扫描步骤。"
- 例 2："为关键页面配置基线 URL 与阈值。"
- 例 3："将报告上传为构件并在失败时阻断合并。"
- 例 4："对误报进行白名单标注并跟踪有效期。"
- 例 5："在 PR 模板添加可达性自检清单。"

## 原始文件

- [chatmodes/accesibility.chatmode.md](../../../chatmodes/accesibility.chatmode.md)
