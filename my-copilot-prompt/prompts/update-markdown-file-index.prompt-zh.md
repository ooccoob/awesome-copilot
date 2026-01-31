---
代理人：“代理人”
描述：“使用指定文件夹中的文件索引/表更新 Markdown 文件部分。”
工具：['更改'，'搜索/代码库'，'编辑/编辑文件'，'扩展'，'网络/获取'，'findTestFiles'，'githubRepo'，'openSimpleBrowser'，'问题'，'runCommands'，'runTasks'，'runTests'，'搜索'，'搜索/searchResults'， 'runCommands/terminalLastCommand'、'runCommands/terminalSelection'、'testFailure'、'用法'、'vscodeAPI']
---
# 更新 Markdown 文件索引

使用文件夹 `${input:folder}` 中的文件索引/表更新 markdown 文件 `${file}`。

## 工艺流程

1. **扫描**：读取目标markdown文件`${file}`以了解现有结构
2. **发现**：列出指定文件夹`${input:folder}`匹配模式`${input:pattern}`中的所有文件
3. **分析**：确定是否存在要更新或创建新结构的现有表/索引部分
4. **结构**：根据文件类型和现有内容生成适当的表格/列表格式
5. **更新**：替换现有部分或使用文件索引添加新部分
6. **验证**：确保 Markdown 语法有效且格式一致

## 文件分析

对于每个发现的文件，提取：

- **名称**：基于上下文的带或不带扩展名的文件名
- **类型**：文件扩展名和类别（例如，`.md`、`.js`、`.py`）
- **描述**：第一行注释、标题或推断目的
- **大小**：供参考的文件大小（可选）
- **修改**：上次修改日期（可选）

## 表结构选项

根据文件类型和现有内容选择格式：

### 选项 1：简单列表

```markdown
## Files in ${folder}

- [filename.ext](path/to/filename.ext) - Description
- [filename2.ext](path/to/filename2.ext) - Description
```

### 选项 2：详细表

|文件 |类型 |描述 |
|------|------|-------------|
| [文件名.ext](path/to/filename.ext) |扩展|描述 |
| [文件名2.ext](path/to/filename2.ext) |扩展|描述 |

### 选项 3：分类部分

使用单独的部分或子表按类型/类别对文件进行分组。

## 更新策略

- 🔄 **更新现有**：如果表/索引部分存在，则在保留结构的同时替换内容
- ➕ **添加新**：如果没有现有部分，则使用最适合的格式创建新部分
- 📋 **保留**：维护现有的 Markdown 格式、标题级别和文档流程
- 🔗 **链接**：使用存储库中文件链接的相对路径

## 部分标识

查找具有以下模式的现有部分：

- 标题包含：“索引”、“文件”、“内容”、“目录”、“列表”
- 具有与文件相关的列的表
- 带有文件链接的列表
- HTML 注释标记文件索引部分

## 要求

- 保留现有的 Markdown 结构和格式
- 使用文件链接的相对路径
- 包括可用的文件描述
- 默认按字母顺序对文件进行排序
- 处理文件名中的特殊字符
- 验证所有生成的 Markdown 语法
