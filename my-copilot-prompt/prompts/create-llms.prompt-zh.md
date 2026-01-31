---
代理人：“代理人”
描述：“根据 https://llmstxt.org/ 上的 llms.txt 规范，根据存储库结构从头开始创建 llms.txt 文件”
工具：['更改'、'搜索/代码库'、'编辑/编辑文件'、'扩展'、'web/fetch'、'githubRepo'、'openSimpleBrowser'、'问题'、'runTasks'、'搜索'、'搜索/searchResults'、'runCommands/terminalLastCommand'、'runCommands/terminalSelection'、'testFailure'、 '用法'，'vscodeAPI']
---
# 从存储库结构创建 LLMs.txt 文件

按照 https://llmstxt.org/ 上的官方 llms.txt 规范，在存储库的根目录中从头开始创建一个新的 `llms.txt` 文件。该文件为大型语言模型 (LLM) 提供了高级指南，帮助您了解在哪里可以找到相关内容以了解存储库的用途和规范。

## 主要指令

创建一个全面的 `llms.txt` 文件，作为法学硕士有效理解和导航存储库的入口点。该文件必须符合 llms.txt 规范，并针对 LLM 消耗进行优化，同时保持人类可读。

## 分析和规划阶段

在创建 `llms.txt` 文件之前，您必须完成彻底的分析：

### 第 1 步：查看 llms.txt 规范

- 查看 https://llmstxt.org/ 上的官方规范以确保完全合规
- 了解所需的格式结构和指南
- 注意具体markdown结构要求

### 第2步：存储库结构分析

- 使用适当的工具检查完整的存储库结构
- 确定存储库的主要目的和范围
- 编录所有重要目录及其用途
- 列出对 LLM 理解有价值的关键文件

### 第 3 步：内容发现

- 识别自述文件及其位置
- 查找文档文件（`/docs/`、`/spec/` 等中的 `.md` 文件）
- 找到规范文件及其用途
- 发现配置文件及其相关性
- 查找示例文件和代码示例
- 识别任何现有的文档结构

### 第 4 步：制定实施计划

根据您的分析，创建一个结构化计划，其中包括：

- 存储库目的和范围摘要
- 用于理解 LLM 的重要文件的优先顺序列表
- 提供额外上下文的辅助文件
- llms.txt 文件的组织结构

## 实施要求

### 格式合规性

`llms.txt` 文件必须按照规范遵循以下精确结构：

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

### 第 1 步：存储库分析

1. 彻底检查存储库结构
2. 阅读主要 README.md 以了解该项目
3. 识别所有文档目录和文件
4. 目录规范文件及其用途
5. 查找示例文件和配置文件

### 第二步：内容规划

1. 确定主要目的陈述
2. 为块引用写一个简洁的摘要
3. 将识别的文件分组为逻辑类别
4. 根据 LLM 理解的重要性对文件进行优先级排序
5. 为每个文件链接创建描述

### 第 3 步：创建文件

1. 在存储库根目录中创建 `llms.txt` 文件
2. 遵循确切的格式规范
3. 包括所有必需的部分
4. 使用正确的 Markdown 格式
5. 确保所有链接都是有效的相对路径

### 第 4 步：验证
1. 验证是否符合 https://llmstxt.org/ 规范
2. 检查所有链接是否有效且可访问
3. 确保该文件作为有效的 LLM 导航工具
4. 确认文件是人类和机器可读的

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

## 结构模板示例

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

创建的 `llms.txt` 文件应该：
1. 使法学硕士能够快速了解存储库的用途
2. 提供重要文档的清晰导航
3. 严格遵循官方llms.txt规范
4. 全面而又简洁
5. 有效地为人类和机器读者提供服务
6. 包括用于项目理解的所有关键文件
7. 始终使用清晰、明确的语言
8. 逻辑地组织内容以便于消费
