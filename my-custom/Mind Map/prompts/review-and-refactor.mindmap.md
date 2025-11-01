## Review & Refactor — Mind Map

### What
- 按仓库内指令与规范，审查并必要时重构代码，确保可维护性与一致性。

### When
- 引入大功能前/后，测试波动、风格不一致或技术债堆积时。

### Why
- 降低复杂度，提升可读性与可测试性，维持长期健康。

### How
- 阅读 .github/instructions 与 copilot-instructions → 全面审查 → 最小变更重构 → 保持文件结构 → 运行测试验证。

### Key Points (中/英)
- 规范/Guidelines
- 一致性/Consistency
- 小步提交/Small Refactors
- 覆盖率/Tests pass
- 兼容性/Compatibility

### Compact map
- Inputs: standards + codebase
- Actions: review → refactor (minimal) → test → iterate
- Constraints: 不拆文件、不破坏 API、保留行为

### Example Questions (≥10)
- 如何从指令文件中提炼最关键的代码规范检查表？
- 哪些坏味道优先重构？为什么？
- 如何划定“最小可行重构”边界以降低风险？
- 有哪些可自动化的安全重构手法？
- 如何保证公共 API 行为不变（增加回归测试）？
- 风格统一（命名/布局/注释）最有效的策略是什么？
- 复杂方法拆分的通用划分原则？
- 重构后的构建/测试验证闭环如何设计？
- 对于跨模块影响，如何分批提交与验证？
- 何时该放弃重构而记录技术债及还款计划？

---
- Source: d:\mycode\awesome-copilot\prompts\review-and-refactor.prompt.md
- Generated: 2025-10-17
