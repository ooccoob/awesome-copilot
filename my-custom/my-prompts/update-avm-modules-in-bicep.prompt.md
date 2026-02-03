---
agent: 'agent'
description: 'Update Azure Verified Modules (AVM) to latest versions in Bicep files.'
tools: ['search/codebase', 'think', 'changes', 'web/fetch', 'search/searchResults', 'todos', 'edit/editFiles', 'search', 'runCommands', 'bicepschema', 'azure_get_schema_for_Bicep']
---
# 更新 Bicep 文件中的 Azure 验证模块

更新 Bicep 文件 `${file}` 以使用最新的 Azure 验证模块 (AVM) 版本。将进度更新限制为非重大更改。除了最终的输出表和摘要之外，不要输出其他信息。

## 工艺流程

1. **扫描**：从 `${file}` 中提取 AVM 模块和当前版本
1. **识别**：列出使用 `#search` 工具匹配 `avm/res/{service}/{resource}` 使用的所有唯一 AVM 模块
1. **检查**：使用 `#fetch` 工具从 MCR 获取每个 AVM 模块的最新版本：`https://mcr.microsoft.com/v2/bicep/avm/res/{service}/{resource}/tags/list`
1. **比较**：解析语义版本以识别需要更新的 AVM 模块
1. **审查**：对于重大更改，请使用 `#fetch` 工具从以下位置获取文档：`https://github.com/Azure/bicep-registry-modules/tree/main/avm/res/{service}/{resource}`
1. **更新**：使用 `#editFiles` 工具应用版本更新和参数更改
1. **验证**：使用 `#runCommands` 工具运行 `bicep lint` 和 `bicep build` 以确保合规性。
1. **输出**：以表格格式总结更改，并附有更新摘要。

## 工具使用

始终使用工具 `#search`、`#searchResults`、`#fetch`、`#editFiles`、`#runCommands`、`#todos`（如果可用）。避免编写代码来执行任务。

## 重大变革政策

⚠️ **如果更新涉及以下内容，请暂停批准**：

- 不兼容的参数更改
- 安全/合规性修改
- 行为改变

## 输出格式

仅在带有图标的表格中显示结果：

```markdown
| Module | Current | Latest | Status | Action | Docs |
|--------|---------|--------|--------|--------|------|
| avm/res/compute/vm | 0.1.0 | 0.2.0 | 🔄 | Updated | [📖](link) |
| avm/res/storage/account | 0.3.0 | 0.3.0 | ✅ | Current | [📖](link) |

### Summary of Updates

Describe updates made, any manual reviews needed or issues encountered.
```

## 图标

- 🔄 已更新
- ✅ 目前
- ⚠️需要人工审核
- ❌ 失败
- 📖 文档

## 要求

- 仅使用 MCR 标签 API 进行版本发现
- 解析 JSON 标签数组并按语义版本控制排序
- 维护 Bicep 文件的有效性和 linting 合规性
