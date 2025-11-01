## What/When/Why/How
- What: Power Apps Code Apps（TS+React+Power Platform SDK）开发速览
- When: 初始化项目、规范团队实践、集成连接器/AI/PowerBI、落地 CI/CD
- Why: 代码优先能力与 Power Platform 集成并存，兼顾速度、质量与合规
- How: 严格 TS 配置、Provider 初始化、服务/模型生成、组件化与可观测性

## Key Points
- 栈：Vite + TypeScript + React + @microsoft/power-apps（端口 3000）
- 结构：components/hooks/services/models/utils/types/PowerProvider
- TS：strict + verbatimModuleSyntax=false；路径别名 @/*
- 连接器：PAC CLI 生成 services/models；类型安全调用；错误/权限处理
- 集成：PCF 控件、Power BI 嵌入、AI Builder、PVA 聊天
- UX：Fluent UI、响应式、错误边界、Skeleton/占位加载
- 性能与离线：懒加载、tree-shaking、IndexedDB、SW、背景同步
- 安全：不在代码存 Secrets；Entra ID；DLP；HTTPS-only
- 测试与 CI：RTL/单元/集成；并行脚本 concurrently；构建与推送

## Compact Map
- Provider: initialize() 成功/失败处理；集中初始化日志
- Services: 由 PAC 生成；封装拦截器/重试；$expand/$filter
- PCF: React 包装器与事件通信；发布打包与部署
- PowerBI: 嵌入配置 + 过滤 + 导出；token 与权限
- AI: 文档处理/预测/情感/目标检测
- DevOps: dev/test/prod 配置、Key Vault、蓝绿/回滚

## Example Questions
1) tsconfig 是否启用 strict 且 verbatimModuleSyntax=false？
2) PowerProvider 初始化失败时是否有降级与错误提示？
3) 连接器调用是否封装重试/鉴权/错误边界并具备类型安全？
4) PCF 控件与 React 的数据/事件绑定是否清晰且可测试？
5) Power BI 嵌入是否做了过滤、权限与导出支持？
6) 是否实现了离线缓存、IndexedDB 与后台同步策略？
7) Secrets 是否全部通过 Key Vault/环境注入且未入库？
8) 是否有统一错误边界与日志采集（不含敏感信息）？
9) 并行与构建脚本是否按官方样例配置（dev/build/push）？
10) 多环境配置与回滚策略是否明确可审计？
11) 组件与 hooks 是否具备良好类型定义与单元测试？

Source: d:\mycode\awesome-copilot\instructions\power-apps-code-apps.instructions.md | Generated: 2025-10-17
