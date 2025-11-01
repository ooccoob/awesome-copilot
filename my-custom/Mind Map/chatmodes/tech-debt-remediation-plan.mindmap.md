## What / When / Why / How

- What: 技术债治理计划（分析产出Markdown方案，不改代码）
- When: 需要可执行的技术债清理路线图
- Why: 降风险、提质量、控成本，便于跨团队协作
- How: 指标评估→标准化章节→表格总览→详细方案→GitHub 集成

## Key Points

- 核心指标(1-5)：易改性/影响/Risk(🟢🟡🔴)
- 章节：Overview/Explanation/Requirements/Steps/Testing
- 常见债务：测试缺失、文档缺失、结构不佳、耦合、废弃依赖、TODO/FIXME
- 输出：先Summary表，再Detailed Plan
- GitHub：search_issues→使用 chore_request 模板→引用既有 issue

## Compact Map

- 发现债务→评分→计划文档→任务化→验证→回归

## Example Questions (10+)

- 此债务的业务影响与优先级？
- 易改性/影响/风险各自评分与依据？
- 前置条件与依赖清单？
- 具体可执行步骤与负责人？
- 验证方法与验收标准？
- 是否涉及架构/依赖升级？
- 是否已有相关 issue/PR 可复用？
- 对测试与文档的补全策略？
- 回滚与观察窗口？
- 交付节奏与里程碑？

---
Source: d:\mycode\awesome-copilot\chatmodes\tech-debt-remediation-plan.chatmode.md
Generated: {{timestamp}}
