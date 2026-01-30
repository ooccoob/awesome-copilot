## What / When / Why / How

- What: Electron + Angular + Native 能力专家
- When: 构建跨平台桌面应用并集成原生能力时
- Why: 统一技术栈、复用 Web 能力并接入系统 API
- How: 跨进程架构（main/renderer/preload）+ 安全策略 + 打包与更新

## Key Points

- 安全：contextIsolation，禁用 nodeIntegration，IPC 白名单
- Native：Node-API/Bindings/ffi；调用摄像头/串口/文件系统等
- 打包：electron-builder/forge；签名与自动更新
- Angular 集成：Zone/ChangeDetection、路由与状态管理
- 调试与测试：e2e（Playwright），单测，sourcemap

## Compact Map

- 架构：main/renderer/preload/IPC
- 安全：权限最小化
- 原生：封装与错误处理
- 打包：平台签名/更新
- 集成：Angular 模块化

## Example Questions (10+)

- 哪些原生能力必须通过 preload 暴露？
- IPC 通道与数据契约如何定义与校验？
- 自动更新与签名在各平台的差异是什么？
- Angular 的变更检测策略如何优化以控资源？
- 摄像头/串口/文件系统的权限模型如何设计？
- 打包体积与启动性能如何优化？
- 崩溃与日志收集机制如何实现？
- 何时使用 Node-API vs. 现成绑定 vs. ffi？
- e2e/单测如何模拟原生模块？
- 多实例/单实例策略如何实现？
- 发布渠道与版本策略如何制定？

---
Source: d:\mycode\awesome-copilot\chatmodes\electron-angular-native.chatmode.md
Generated: {{timestamp}}
