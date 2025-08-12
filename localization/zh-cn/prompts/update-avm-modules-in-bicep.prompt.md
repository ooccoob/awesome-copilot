---
mode: 'agent'
description: '将 Bicep 文件中的 Azure Verified Modules (AVM) 升级至最新版本。'
tools: ['changes', 'codebase', 'editFiles', 'fetch', 'runCommands', 'azure_get_deployment_best_practices', 'azure_get_schema_for_Bicep']
---

# 在 Bicep 中更新 Azure Verified Modules

将 `${file}` 中使用的 AVM 模块升级到最新版本。

## 流程

1. 扫描：从 `${file}` 中提取 AVM 模块及其当前版本。
2. 查询：访问 MCR：`https://mcr.microsoft.com/v2/bicep/avm/res/{service}/{resource}/tags/list` 获取最新版本。
3. 对比：按语义化版本规则比较版本并识别可更新项。
4. 评审：若存在潜在破坏性变更，查看：`https://github.com/Azure/bicep-registry-modules/tree/main/avm/res/{service}/{resource}`。
5. 更新：应用版本与参数变更。
6. 校验：运行 `bicep lint` 确认证合规。

## 破坏性变更策略

⚠️ 如更新涉及以下情况需暂停等待批准：
- 不兼容的参数变更
- 安全/合规调整
- 行为变化

## 输出格式

以表格展示：

| Module | Current | Latest | Status | Action | Docs |
|--------|---------|--------|--------|--------|------|
| avm/res/compute/vm | 0.1.0 | 0.2.0 | 🔄 | Updated | [📖](link) |
| avm/res/storage/account | 0.3.0 | 0.3.0 | ✅ | Current | [📖](link) |

## 图标

- 🔄 已更新
- ✅ 已是最新
- ⚠️ 需要人工评审
- ❌ 失败
- 📖 文档

## 要求

- 仅使用 MCR tags API 获取版本
- 解析 JSON tags，并按语义化版本排序
- 保持 Bicep 文件有效且通过 linter 检查
