## What/When/Why/How
- What: 自解释代码注释准则（注释解释“为何”而非“做什么”）
- When: 需要补充上下文/约束/权衡时
- Why: 降低噪声、避免过时、提升可维护性
- How: 先改名与重构，再写必要注释；使用标准注解标签

## Key Points
- 避免：显而易见/重复/过时/装饰性/历史记录/死代码注释
- 应写：复杂业务意图、算法选择、正则语义、外部约束
- 公共 API：完整 JSDoc/参数/返回/异常
- 常量/配置：来源/依据/上下限
- 注解标签：TODO/FIXME/HACK/NOTE/WARNING/PERF/SECURITY/BUG/REFACTOR/DEPRECATED
- 质量清单：解释“为什么”、语法正确、增值、位置得当

## Compact Map
- Prefer: rename/refactor → then comment why
- API: JSDoc + examples
- Tags: TODO/FIXME/…
- Avoid: obvious/redundant/outdated/decorative

## Example Questions
1) 这条注释是否解释“为何”而非“做了什么”？
2) 通过改名/拆分能否消除对注释的需求？
3) 公共 API 的注释是否完整可用？
4) 正则/算法是否解释选择原因与边界？
5) 注释是否可能很快过时？如何降低风险？
6) 使用的注解标签是否得当且可追踪？
7) 常量/配置的来源是否明确且可验证？
8) 注释位置是否贴近所述代码？
9) 是否避免注释掉的死代码？
10) 这条注释是否真的为维护者增值？
11) 重构是否优先于写大段注释？

Source: d:\mycode\awesome-copilot\instructions\self-explanatory-code-commenting.instructions.md | Generated: 2025-10-17
