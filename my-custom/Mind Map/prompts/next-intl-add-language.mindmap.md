## What
- 在 Next.js + next-intl 项目中新增语言：翻译 messages、更新路由与中间件、更新语言切换组件。

## When to use
- 需要正式支持新语言并确保路由与 UI 切换一致。

## Why it matters
- 一致的 i18n 体验，降低 404/路由错配与文案缺失风险。

## How (关键流程)
- 翻译 messages/en.json → 新语言 json
- 更新 src/i18n/routing.ts 与 src/middleware.ts 的受支持语言/默认策略
- 更新 src/components/language-toggle.tsx 选项与显示
- 自测：路径、切换、默认重定向、缺失键兜底

## Example questions (≥10)
1. 目标语言为 fr，请基于 en.json 生成 fr.json 的初始翻译并标注未译键。
2. 在 routing.ts/middleware.ts 中新增 fr 支持，给出差异补丁。
3. 在 language-toggle.tsx 中加入 fr 选项并保持排序与图标一致。
4. 如何检测 messages 中的缺失键并在构建阶段失败？
5. 提供 e2e 自测用例：默认语言、直达路由、切换后保留路径、SSR。
6. 解释 locale 路由前缀与 domain-based 路由的差异与配置样例。
7. 生成一个脚本同步 en.json 的新键到各语言。
8. 在 CI 中对比校验所有语言键集合一致性的方案。
9. 给出 Fallback 策略：缺失键回退到 en 并标注日志。
10. 生成发布说明模板，提醒前端/文案回归检查点。

## Key points
- CN: 键一致性校验、路由与中间件同步、切换组件更新、CI 保障
- EN: Key consistency, routing/middleware sync, toggle update, CI guardrails

## Mind map (简要)
- 翻译 → 路由 → 中间件 → 切换 → 校验/CI → 测试

---
Source file: d:\mycode\awesome-copilot\prompts\next-intl-add-language.prompt.md
Generated: 2025-10-17T00:00:00Z
