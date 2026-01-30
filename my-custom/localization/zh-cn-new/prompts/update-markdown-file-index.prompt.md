---
mode: 'agent'
description: '使用来自指定文件夹的文件索引/表格更新markdown文件节。'
tools: ['changes', 'codebase', 'edit/editFiles', 'extensions', 'fetch', 'findTestFiles', 'githubRepo', 'openSimpleBrowser', 'problems', 'runCommands', 'runTasks', 'runTests', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI']
---
# 更新Markdown文件索引

使用来自文件夹`${input:folder}`的文件索引/表格更新markdown文件`${file}`。

## 流程

1. **扫描**：读取目标markdown文件`${file}`以了解现有结构
2. **发现**：列出指定文件夹`${input:folder}`中匹配模式`${input:pattern}`的所有文件
3. **分析**：识别是否存在要更新的现有表格/索引节，或创建新结构
4. **结构**：基于文件类型和现有内容生成适当的表格/列表格式
5. **更新**：替换现有节或添加包含文件索引的新节
6. **验证**：确保markdown语法有效且格式一致

## 文件分析

对于每个发现的文件，提取：

- **名称**：根据上下文选择带或不带扩展名的文件名
- **类型**：文件扩展名和类别（例如`.md`、`.js`、`.py`）
- **描述**：第一行注释、标题或推断的目的
- **大小**：文件大小供参考（可选）
- **修改**：最后修改日期（可选）

## 表格结构选项

根据文件类型和现有内容选择格式：

### 选项1：简单列表

```markdown
## ${folder}中的文件

- [filename.ext](path/to/filename.ext) - 描述
- [filename2.ext](path/to/filename2.ext) - 描述
```

### 选项2：详细表格

| 文件 | 类型 | 描述 |
|------|------|-------------|
| [filename.ext](path/to/filename.ext) | 扩展名 | 描述 |
| [filename2.ext](path/to/filename2.ext) | 扩展名 | 描述 |

### 选项3：分类节

按类型/类别对文件进行分组，使用单独的节或子表格。

## 更新策略

- 🔄 **更新现有**：如果存在表格/索引节，在保持结构的同时替换内容
- ➕ **添加新**：如果没有现有节，使用最合适格式创建新节
- 📋 **保留**：保持现有markdown格式、标题级别和文档流程
- 🔗 **链接**：对仓库内的文件链接使用相对路径

## 节识别

查找具有这些模式的现有节：

- 包含"index"、"files"、"contents"、"directory"、"list"的标题
- 包含文件相关列的表格
- 包含文件链接的列表
- 标记文件索引节的HTML注释

## 要求

- 保留现有markdown结构和格式
- 对文件链接使用相对路径
- 在可用时包含文件描述
- 默认按字母顺序对文件排序
- 处理文件名中的特殊字符
- 验证所有生成的markdown语法