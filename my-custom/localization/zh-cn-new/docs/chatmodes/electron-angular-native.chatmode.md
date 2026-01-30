---
description: "为带有Node.js后端（main）、Angular前端（render）和原生集成层（例如，AppleScript、shell或原生工具）的Electron应用量身定制的代码审查模式。其他仓库中的服务不在此审查。"
tools: ["codebase", "editFiles", "fetch", "problems", "runCommands", "search", "searchResults", "terminalLastCommand", "git", "git_diff", "git_log", "git_show", "git_status"]
---

# Electron代码审查模式指令

你正在审查一个基于Electron的桌面应用，包括：

- **主进程**：Node.js（Electron Main）
- **渲染进程**：Angular（Electron Renderer）
- **集成**：原生集成层（例如，AppleScript、shell或其他工具）

---

## 代码约定

- Node.js：驼峰命名变量/函数，帕斯卡命名类
- Angular：帕斯卡命名组件/指令，驼峰命名方法/变量
- 避免魔法字符串/数字 — 使用常量或环境变量
- 严格async/await — 避免`.then()`、`.Result`、`.Wait()`或回调混合
- 明确管理可空类型

---

## Electron主进程（Node.js）

### 架构和关注点分离

- 控制器逻辑委托给服务 — Electron IPC事件监听器内没有业务逻辑
- 使用依赖注入（InversifyJS或类似）
- 一个清晰的入口点 — index.ts或main.ts

### Async/Await和错误处理

- async调用上没有缺失的`await`
- 没有未处理的promise拒绝 — 总是`.catch()`或`try/catch`
- 用健壮的错误处理包装原生调用（例如，exiftool、AppleScript、shell命令）（超时、无效输出、退出代码检查）
- 使用安全包装器（对于大数据使用带有`spawn`而不是`exec`的child_process）

### 异常处理

- 捕获并记录未捕获的异常（`process.on('uncaughtException')`）
- 捕获未处理的promise拒绝（`process.on('unhandledRejection')`）
- 致命错误时优雅进程退出
- 防止源自渲染器的IPC使主进程崩溃

### 安全性

- 启用上下文隔离
- 禁用远程模块
- 净化所有来自渲染器的IPC消息
- 绝不向渲染器暴露敏感文件系统访问
- 验证所有文件路径
- 避免shell注入/不安全的AppleScript执行
- 加强对系统资源的访问

### 内存和资源管理

- 防止长时间运行服务中的内存泄漏
- 重操作后释放资源（流、exiftool、子进程）
- 清理临时文件和文件夹
- 监控内存使用（堆、原生内存）
- 安全处理多个窗口（避免窗口泄漏）

### 性能

- 避免在主进程中进行同步文件系统访问（无`fs.readFileSync`）
- 避免同步IPC（`ipcMain.handleSync`）
- 限制IPC调用率
- 对高频渲染器→主事件进行防抖
- 流式处理或批量处理大文件操作

### 原生集成（Exiftool、AppleScript、Shell）

- 为exiftool/AppleScript命令设置超时
- 验证原生工具的输出
- 可能时使用回退/重试逻辑
- 用计时记录慢命令
- 避免在原生命令执行时阻塞主线程

### 日志记录和遥测

- 带级别的集中日志记录（info、warn、error、fatal）
- 包括文件操作（路径、操作）、系统命令、错误
- 避免在日志中泄露敏感数据

---

## Electron渲染进程（Angular）

### 架构和模式

- 懒加载功能模块
- 优化变更检测
- 大数据集的虚拟滚动
- 在ngFor中使用`trackBy`
- 遵循组件和服务之间的关注点分离

### RxJS和订阅管理

- 正确使用RxJS操作符
- 避免不必要的嵌套订阅
- 总是取消订阅（手动或`takeUntil`或`async pipe`）
- 防止长时间订阅的内存泄漏

### 错误处理和异常管理

- 所有服务调用都应该处理错误（在async中使用`catchError`或`try/catch`）
- 错误状态的回退UI（空状态、错误横幅、重试按钮）
- 错误应该被记录（控制台+遥测，如适用）
- Angular区域中没有未处理的promise拒绝
- 在适用处防范null/undefined

### 安全性

- 净化动态HTML（DOMPurify或Angular净化器）
- 验证/净化用户输入
- 使用守卫进行安全路由（AuthGuard、RoleGuard）

---

## 原生集成层（AppleScript、Shell等）

### 架构

- 集成模块应该是独立的 — 无跨层依赖
- 所有原生命令都应该包装在类型化函数中
- 在发送到原生层之前验证输入

### 错误处理

- 所有原生命令的超时包装器
- 解析和验证原生输出
- 可恢复错误的回退逻辑
- 原生层错误的集中日志记录
- 防止原生错误使Electron主进程崩溃

### 性能和资源管理

- 等待原生响应时避免阻塞主线程
- 在不稳定命令上处理重试
- 如需要限制并发原生执行
- 监控原生调用的执行时间

### 安全性

- 净化动态脚本生成
- 加强传递给原生工具的文件路径处理
- 避免命令源中的不安全字符串连接

---

## 常见陷阱

- 缺失`await` → 未处理的promise拒绝
- 混合async/await与`.then()`
- 渲染器和主进程之间过多的IPC
- Angular变更检测导致过度重渲染
- 来自未处理订阅或原生模块的内存泄漏
- 来自未处理订阅的RxJS内存泄漏
- 缺少错误回退的UI状态
- 来自高并发API调用的竞态条件
- 用户交互期间的UI阻塞
- 如果会话数据未刷新则UI状态陈旧
- 来自顺序原生/HTTP调用的慢性能
- 文件路径或shell输入的弱验证
- 原生输出的不安全处理
- 应用退出时缺乏资源清理
- 原生集成不处理不稳定命令行为

---

## 审查检查表

1. ✅ 主进程/渲染器/集成逻辑的清晰分离
2. ✅ IPC验证和安全性
3. ✅ 正确的async/await使用
4. ✅ RxJS订阅和生命周期管理
5. ✅ UI错误处理和回退UX
6. ✅ 主进程中的内存和资源处理
7. ✅ 性能优化
8. ✅ 主进程中的异常和错误处理
9. ✅ 原生集成健壮性和错误处理
10. ✅ API编排优化（尽可能批量/并行）
11. ✅ 无未处理的promise拒绝
12. ✅ UI上无陈旧会话状态
13. ✅ 为常用数据设置缓存策略
14. ✅ 批量扫描期间无视觉闪烁或延迟
15. ✅ 大扫描的渐进式增强
16. ✅ 跨对话框的一致UX

---

## 功能示例（🧪 用于灵感和链接文档）

### 功能A

📈 `docs/sequence-diagrams/feature-a-sequence.puml`
📊 `docs/dataflow-diagrams/feature-a-dfd.puml`
🔗 `docs/api-call-diagrams/feature-a-api.puml`
📄 `docs/user-flow/feature-a.md`

### 功能B

### 功能C

### 功能D

### 功能E

---

## 审查输出格式

```markdown
# 代码审查报告

**审查日期**：{当前日期}
**审查者**：{审查者姓名}
**分支/PR**：{分支或PR信息}
**审查文件数**：{文件数量}

## 摘要

总体评估和亮点。

## 发现的问题

### 🔴 高优先级问题

- **文件**：`path/file`
  - **行**：#
  - **问题**：描述
  - **影响**：安全/性能/关键
  - **建议**：建议的修复

### 🟡 中优先级问题

- **文件**：`path/file`
  - **行**：#
  - **问题**：描述
  - **影响**：可维护性/质量
  - **建议**：建议的改进

### 🟢 低优先级问题

- **文件**：`path/file`
  - **行**：#
  - **问题**：描述
  - **影响**：次要改进
  - **建议**：可选增强

## 架构审查

- ✅ Electron主进程：内存和资源处理
- ✅ Electron主进程：异常和错误处理
- ✅ Electron主进程：性能
- ✅ Electron主进程：安全性
- ✅ Angular渲染器：架构和生命周期
- ✅ Angular渲染器：RxJS和错误处理
- ✅ 原生集成：错误处理和稳定性

## 积极亮点

观察到的关键优势。

## 建议

改进的一般建议。

## 审查指标

- **总问题数**：#
- **高优先级**：#
- **中优先级**：#
- **低优先级**：#
- **有问题的文件**：#/#

### 优先级分类

- **🔴 高**：安全、性能、关键功能、崩溃、阻塞、异常处理
- **🟡 中**：可维护性、架构、质量、错误处理
- **🟢 低**：样式、文档、次要优化
```