## What / When / Why / How

- What: Playwright 测试专家模式（先探索站点，再生成/运行/迭代测试）
- When: 需要提升端到端测试质量与稳定性时
- Why: 通过真实交互探索与快照定位选择器，减少脆弱性
- How: 浏览→快照→定位器→生成 TS 测试→运行→诊断→修复→文档

## Key Points

- 工具：Playwright MCP 导航/快照/诊断；必要时先启动 dev server
- 先探索后编码：识别关键用户流与选择器
- 结构化测试：可维护、可复用、分层封装（Page Object）
- 执行与迭代：运行、定位失败原因、修复直到稳定通过
- 输出：测试结构与覆盖范围说明

## Compact Map

- 探索站点→识别流→定位器与约定
- 生成 TS 测试→运行→修复
- 稳定化策略与报告

## Example Questions (10+)

- 站点的关键用户流有哪些？各流的起止条件是什么？
- 哪些选择器最稳定（role/aria/testid/label）？
- 需要哪些前置数据与鉴权步骤？
- 如何分层封装 Page Object 以复用？
- 哪些测试应并行执行，哪些需串行？
- flakiness 的主要来源及缓解策略？
- CI 环境下的浏览器与缓存策略如何配置？
- 截图/视频/trace 的采集与留存策略？
- 重试与超时设置如何权衡速度与稳定？
- 覆盖率（路由/元素/断言）如何衡量？
- 本轮新增测试的变更影响面在哪里？

---
Source: d:\mycode\awesome-copilot\chatmodes\playwright-tester.chatmode.md
Generated: {{timestamp}}
