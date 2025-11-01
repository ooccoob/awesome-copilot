## Power Apps Code App 脚手架（思维导图）

- What
  - 基于 Vite+React+TS 的 Code App 工程脚手架
  - 集成 Power Apps SDK、PAC CLI、连接器与示例页面
- When
  - 新建 Code App；建设示例以演示 O365 Users/Dataverse 接入
- Why
  - 统一目录/脚本/SDK 初始化与最佳实践
  - 降低预览特性接入与部署复杂度
- How
  - 初始化：vite + TS；端口 3000；安装 @microsoft/power-apps；pac code init
  - 结构：components/services/models/hooks/utils/types/PowerProvider/main
  - 脚本：dev 并行（vite + pac code run）；build/preview/lint
  - 示例：PowerProvider 鉴权初始化；O365 Users 个人信息与头像
  - 文档：前置条件、环境/鉴权、连接器、部署、常见问题
  - 限制：CSP/IP 限制/无 Dataverse 解决方案/无 App Insights 原生

- Key Points (CN/EN)
  - Port 3000 required; PAC CLI flows
  - Generated models/services usage
  - Error handling + loading states
  - Fluent UI + a11y/i18n/theme

- Example Questions (≥10)
  1) 本机 Node 版本与 PAC CLI 版本如何校验与要求？
  2) 如何以并发方式同时启动 vite 与 pac code run？
  3) O365 Users 示例最小可行代码与错误处理是什么？
  4) 连接器添加/更新与环境选择的命令序列？
  5) TypeScript 配置（verbatimModuleSyntax 等）如何设置？
  6) Vite base 与别名如何配置以适配 Code Apps？
  7) 常见 CSP/端口限制问题如何定位？
  8) 部署到环境的最小步骤与验证路径是什么？
  9) 多环境 dev/test/prod 如何管理？
  10) 如何在不泄漏机密的前提下调试连接器？

- Compact Mind Map
  - 初始化→结构→脚本→示例→文档→限制

- Source: prompts/power-apps-code-app-scaffold.prompt.md
- Generated: 2025-10-17
