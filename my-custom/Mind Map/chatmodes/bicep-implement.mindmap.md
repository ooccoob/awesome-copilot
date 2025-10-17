## What / When / Why / How

- What: Azure Bicep 基础设施代码实现专家
- When: 需要快速产出可编译、可部署、符合最佳实践的 .bicep 文件
- Why: 通过自动化校验/格式化/编译保证质量与一致性
- How: 解析目标→生成路径→restore/build/format/lint→修复直至通过

## Key Points

- 输出路径约定：infra/bicep/{goal}
- 工具链：bicep restore/build --stdout/format/lint（警告也当问题处理）
- AVM 输入二次校验（azure_get_azure_verified_module）
- 仅生成 .bicep 文件，避免无关产物
- 成功标准：编译通过、无 lint 问题、无硬编码机密

## Compact Map

- 需求→输出路径确认
- 生成 .bicep（参数/变量/资源/输出）
- 本地校验：restore/build/format/lint
- 版本/API/AVM 参数核验
- 清理临时产物，提交变更

## Example Questions (10+)

- 该模板的 goal 与输出路径是否确认？
- 需要哪些参数（param）与默认值？
- 资源 API 版本与区域支持情况如何？
- 是否存在可用 AVM 模块以替代手写？
- 依赖的资源输出如何对接（outputs→params）？
- 有哪些策略/诊断/加固设置必须开启？
- 编译/格式/静态检查是否全部通过？
- 需要提供哪些示例 param 文件便于复现？
- 如何在 CI 中集成 bicep lint/build 流水线？
- 是否有回滚与销毁策略文档？
- 是否清理了临时 ARM JSON 产物？

---
Source: d:\mycode\awesome-copilot\chatmodes\bicep-implement.chatmode.md
Generated: {{timestamp}}
