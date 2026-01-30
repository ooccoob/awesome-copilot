---
mode: 'agent'
description: '在Bicep文件中将Azure验证模块（AVM）更新到最新版本。'
tools: ['codebase', 'think', 'changes', 'fetch', 'searchResults', 'todos', 'edit/editFiles', 'search', 'runCommands', 'bicepschema', 'azure_get_schema_for_Bicep']
---
# 在Bicep文件中更新Azure验证模块

将Bicep文件`${file}`更新为使用最新的Azure验证模块（AVM）版本。限制进度更新为非破坏性更改。除了最终输出表格和摘要外，不输出其他信息。

## 流程

1. **扫描**：从`${file}`提取AVM模块和当前版本
2. **识别**：使用`#search`工具匹配`avm/res/{service}/{resource}`，列出所有使用的唯一AVM模块
3. **检查**：使用`#fetch`工具从MCR获取每个AVM模块的最新版本：`https://mcr.microsoft.com/v2/bicep/avm/res/{service}/{resource}/tags/list`
4. **比较**：解析语义版本以识别需要更新的AVM模块
5. **审查**：对于破坏性更改，使用`#fetch`工具从以下位置获取文档：`https://github.com/Azure/bicep-registry-modules/tree/main/avm/res/{service}/{resource}`
6. **更新**：使用`#editFiles`工具应用版本更新和参数更改
7. **验证**：使用`#runCommands`工具运行`bicep lint`和`bicep build`以确保合规性
8. **输出**：以表格格式总结更改，并在下方提供更新摘要

## 工具使用

如果可用，始终使用工具`#search`、`#searchResults`、`#fetch`、`#editFiles`、`#runCommands`、`#todos`。避免编写代码来执行任务。

## 破坏性更改策略

⚠️ 如果更新涉及以下内容，请**暂停等待批准**：

- 不兼容的参数更改
- 安全/合规性修改
- 行为更改

## 输出格式

仅使用图标在表格中显示结果：

```markdown
| 模块 | 当前版本 | 最新版本 | 状态 | 操作 | 文档 |
|--------|---------|--------|--------|--------|------|
| avm/res/compute/vm | 0.1.0 | 0.2.0 | 🔄 | 已更新 | [📖](链接) |
| avm/res/storage/account | 0.3.0 | 0.3.0 | ✅ | 当前版本 | [📖](链接) |

### 更新摘要

描述所做的更新、需要的任何手动审查或遇到的问题。
```

## 图标

- 🔄 已更新
- ✅ 当前版本
- ⚠️ 需要手动审查
- ❌ 失败
- 📖 文档

## 要求

- 仅使用MCR标签API进行版本发现
- 解析JSON标签数组并按语义版本排序
- 维护Bicep文件有效性和linting合规性