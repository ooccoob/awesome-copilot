## What/When/Why/How
- What: Dev Box 镜像定义与维护要点（组件、版本、合规、自动化）
- When: 创建/更新开发镜像、提高一致性与可复现性
- Why: 降低开发环境漂移与新成员落地成本
- How: 清单式定义、版本固定、签名/信任、自动构建与验证

## Key Points
- 定义: 列出 SDK/工具/扩展；固定版本与来源
- 安全: 只用可信源；签名校验；最小权限
- 自动化: 通过管道构建镜像并运行验证脚本
- 维护: 定期补丁、变更日志、回滚策略
- 性能: 预热常用依赖缓存；缩小镜像体积

## Compact Map
清单→版本→安全→自动化→验证→维护→性能

## Example Questions (10+)
1) 生成包含 .NET/Node/Java 的 Dev Box 镜像定义草案
2) 设计版本锁定与安全源策略
3) 在 CI 中自动构建并运行验证脚本
4) 镜像变更日志规范与回滚流程
5) 预热包管理器缓存以加速开发
6) 如何检查许可证与合规项？
7) 将团队工具与 VSCode 扩展纳入镜像
8) 提供检测陈旧依赖的自动扫描
9) 镜像体积优化策略
10) 在 PR 中对镜像变更进行审查清单

Source: d:\mycode\awesome-copilot\instructions\devbox-image-definition.instructions.md | Generated: 2025-10-17T00:00:00Z## Dev Box Image Definition（YAML）要点

- What: 为 Microsoft Dev Box Team Customizations 编写 YAML（内置任务、验证、密钥、安全与故障排查）。
- When: 生成/审阅镜像定义、组合安装/脚本/克隆任务、处理 msstore、注入机密时。
- Why: 保障任务可用与可移植，避免上下文/权限错误，提升可维护与安全。
- How: 先检查工具可用性→列出可用任务→仅使用可用任务→内置任务用 `~/` 前缀→Key Vault 管理机密→区分 system/user 上下文。

### 关键要点
- 工具检测: 先试用 MCP 任务生成器；若不可用，建议启用并解释收益。
- 列出任务: `devbox customizations list-tasks`，仅用其输出中的任务/参数。
- 内置任务: `~/winget`、`~/powershell`、`~/gitclone` 必须带 `~/` 前缀。
- 机密: 使用 `{{KV_SECRET_URI}}`；运行时解析；本地测试可能需临时明文（提交前务必移除）。
- 上下文: `tasks`(系统) 安装系统级软件；`userTasks`(用户) VS Code 扩展、MS Store 等。
- msstore: 需放在 `userTasks`；使用 winget CLI 直调时添加接受协议参数。
- CLI: `apply-tasks` 应用、`list-tasks` 查看；管理员权限与日志位置（ProgramData\...\customizations\...\stderr.log）。
- PowerShell: 避免双引号陷阱；必要时转义；大文件下载可用 azcopy/存储；抑制进度条。

### Compact Map
Tools→TasksList→Intrinsic~/→SecretsKV→System vs User→msstore→CLI→Logs→PS Tips

### 示例问题
1) 何时必须使用 `~/winget` 而非 CLI 直调？
2) `tasks` 与 `userTasks` 的划分与迁移策略？
3) 如何在本地验证 YAML 同时避免机密泄露？
4) msstore 包安装失败的常见原因与排障路径？
5) PowerShell 内联脚本双引号问题如何规避？
6) 大文件下载时如何选择更高效手段？
7) 任务不可用时的替代策略（如 `~/powershell`）？
8) 如何缓存/记录 list-tasks 输出并保持 1 小时内新鲜？
9) 发生 “System tasks are not allowed...” 错误的应对？
10) YAML 验证工具在何时优先于手工生成？

Source: d:\mycode\awesome-copilot\instructions\devbox-image-definition.instructions.md | Generated: 2025-10-17T00:00:00Z
