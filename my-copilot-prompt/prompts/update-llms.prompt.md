---
agent: 'agent'
description: 'Update the llms.txt file in the root folder to reflect changes in documentation or specifications following the llms.txt specification at https://llmstxt.org/'
tools: ['changes', 'search/codebase', 'edit/editFiles', 'extensions', 'web/fetch', 'githubRepo', 'openSimpleBrowser', 'problems', 'runTasks', 'search', 'search/searchResults', 'runCommands/terminalLastCommand', 'runCommands/terminalSelection', 'testFailure', 'usages', 'vscodeAPI']
---
# 更新 LLMs.txt 文件

更新存储库根目录中的现有 `llms.txt` 文件以反映文档、规范或存储库结构中的更改。该文件为大型语言模型 (LLM) 提供了高级指南，帮助您了解在哪里可以找到相关内容以了解存储库的用途和规范。

## 主要指令

更新现有的 `llms.txt` 文件以保持准确性并符合 llms.txt 规范，同时反映当前存储库结构和内容。该文件必须针对 LLM 消耗保持优化，同时保持人类可读。

## 分析和规划阶段

在更新 `llms.txt` 文件之前，您必须完成彻底的分析：

### 第 1 步：查看当前文件和规范
- 读取现有的 `llms.txt` 文件以了解当前结构
- 查看 https://llmstxt.org/ 上的官方规范，以确保持续合规
- 根据存储库更改确定可能需要更新的区域

### 第2步：存储库结构分析
- 使用适当的工具检查当前存储库结构
- 将当前结构与现有 `llms.txt` 中记录的结构进行比较
- 确定应包含的新目录、文件或文档
- 记下任何需要更新的已删除或重新定位的文件

### 第 3 步：内容发现和变更检测
- 识别新的自述文件及其位置
- 查找新的文档文件（`/docs/`、`/spec/` 等中的 `.md` 文件）
- 找到新的规范文件及其用途
- 发现新的配置文件及其相关性
- 查找新的示例文件和代码示例
- 确定现有文档结构的任何更改

### 第 4 步：创建更新计划
根据您的分析，创建一个结构化计划，其中包括：
- 保持准确性所需的更改
- 要添加到 llms.txt 的新文件
- 过时的参考资料将被删除或更新
- 组织改进以保持清晰度

## 实施要求

### 格式合规性
更新后的 `llms.txt` 文件必须按照规范保持这个精确的结构：

1. **H1 标题**：带有存储库/项目名称的单行（必需）
2. **块引用摘要**：块引用格式的简要描述（可选但推荐）
3. **其他详细信息**：零个或多个没有上下文标题的降价部分
4. **文件列表部分**：零个或多个包含链接降价列表的 H2 部分

### 内容要求

#### 所需元素
- **项目名称**：清晰的描述性标题如 H1
- **摘要**：解释存储库用途的简洁引用
- **关键文件**：按类别组织的基本文件（H2 部分）

#### 文件链接格式
每个文件链接必须遵循：`[descriptive-name](relative-url): optional description`

#### 部门组织
将文件组织成逻辑 H2 部分，例如：
- **文档**：核心文档文件
- **规格**：技术规格和要求
- **示例**：示例代码和使用示例
- **配置**：设置和配置文件
- **可选**：辅助文件（特殊含义 - 可以跳过较短的上下文）

### 内容指南

#### 语言和风格
- 使用简洁、清晰、明确的语言
- 避免使用没有解释的行话
- 为人类和法学硕士读者撰写
- 描述具体且信息丰富

#### 文件选择标准
包含以下文件：
- 解释存储库的目的和范围
- 提供必要的技术文档
- 显示使用示例和模式
- 定义接口和规范
- 包含配置和设置说明

排除以下文件：
- 纯粹是实现细节
- 包含冗余信息
- 是构建工件还是生成的内容
- 与理解项目无关

## 执行步骤

### 第 1 步：现状分析
1. 彻底读取现有的 `llms.txt` 文件
2. 彻底检查当前存储库结构
3. 将现有文件引用与实际存储库内容进行比较
4. 识别过时、缺失或不正确的参考文献
5. 注意当前文件的任何结构问题

### 第二步：内容规划
1. 确定主要目的陈述是否需要更新
2. 如果需要，查看并更新摘要块引用
3. 计划添加新文件和目录
4. 计划删除过时或移动的内容
5. 如果需要的话重新组织部分以获得更好的清晰度

### 第 3 步：文件更新
1. 更新存储库根目录中现有的 `llms.txt` 文件
2. 保持遵守确切的格式规范
3. 添加带有适当描述的新文件引用
4. 删除或更新过时的参考文献
5. 确保所有链接都是有效的相对路径

### 第 4 步：验证
1. 验证是否持续符合 https://llmstxt.org/ 规范
2. 检查所有链接是否有效且可访问
3. 确保该文件仍然作为有效的 LLM 导航工具
4. 确认文件仍然可供人类和机器读取

## 品质保证

### 格式验证
- 带有项目名称的 H1 标题
- ✅ 块引用摘要（如果包含）
- ✅ 文件列表的 H2 部分
- ✅ 正确的 Markdown 链接格式
- ✅ 没有损坏或无效的链接
- ✅ 始终保持一致的格式

### 内容验证
- ✅ 语言清晰、不含糊
- ✅ 全面覆盖重要文件
- ✅ 内容的逻辑组织
- ✅ 适当的文件描述
- ✅ 作为有效的 LLM 导航工具

### 规格合规性
- ✅ 完全遵循 https://llmstxt.org/ 格式
- ✅ 使用所需的 Markdown 结构
- ✅ 适当实施可选部分
- ✅ 文件位于存储库根目录 (`/llms.txt`)

## 更新策略

### 添加过程
添加新内容时：
1. 确定新文件的适当部分
2. 为链接创建清晰的描述性名称
3. 撰写简洁但内容丰富的描述
4. 保持章节内的字母顺序或逻辑顺序
5. 考虑新的内容类型是否需要新的部分

### 去除过程
删除过时的内容时：
1. 验证文件确实已删除或重新定位
2. 检查重新定位的文件是否应该更新而不是删除
3. 如果整个部分变空，请将其删除
4. 如果需要，更新交叉引用

### 重组过程
重组内容时：
1. 保持从一般到具体的逻辑流程
2. 将重要文档保留在主要部分中
3. 如果适用，请将次要内容移至“可选”部分
4. 确保新组织改善法学硕士导航

`llms.txt` 的示例结构：

```txt
# [Repository Name]

> [Concise description of the repository's purpose and scope]

[Optional additional context paragraphs without headings]

## Documentation

- [Main README](README-zh.md): Primary project documentation and getting started guide
- [Contributing Guide](CONTRIBUTING-zh.md): Guidelines for contributing to the project
- [Code of Conduct](CODE_OF_CONDUCT-zh.md): Community guidelines and expectations

## Specifications

- [Technical Specification](spec/technical-spec-zh.md): Detailed technical requirements and constraints
- [API Specification](spec/api-spec-zh.md): Interface definitions and data contracts

## Examples

- [Basic Example](examples/basic-usage-zh.md): Simple usage demonstration
- [Advanced Example](examples/advanced-usage-zh.md): Complex implementation patterns

## Configuration

- [Setup Guide](docs/setup-zh.md): Installation and configuration instructions
- [Deployment Guide](docs/deployment-zh.md): Production deployment guidelines

## Optional

- [Architecture Documentation](docs/architecture-zh.md): Detailed system architecture
- [Design Decisions](docs/decisions-zh.md): Historical design decision records
```

## 成功标准

更新后的 `llms.txt` 文件应该：
1. 准确反映当前存储库结构和内容
2. 保持符合 llms.txt 规范
3. 提供重要文档的清晰导航
4. 删除过时或不正确的引用
5. 包括新的重要文件和文档
6. 保持逻辑组织以方便LLM消费
7. 始终使用清晰、明确的语言
8. 继续有效地服务人类和机器阅读器
