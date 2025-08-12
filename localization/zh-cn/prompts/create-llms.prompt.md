---
mode: "agent"
description: "依据 https://llmstxt.org/ 规范，从仓库结构生成 llms.txt 文件。"
tools: ["changes", "codebase", "editFiles", "extensions", "fetch", "githubRepo", "openSimpleBrowser", "problems", "runTasks", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI"]
---

# 从仓库结构创建 LLMs.txt

在仓库根目录新建 `llms.txt` 文件，遵循 https://llmstxt.org/ 官方规范。该文件为大语言模型（LLM）提供入口指导，帮助理解仓库目的与规格位置。

## 首要指令

创建一份全面的 `llms.txt`，既满足规范、又便于 LLM 消费，同时保持对人类可读。

## 分析与规划阶段

在创建文件前，请完成全面分析：

### 步骤 1：阅读 llms.txt 规范

- 阅读 https://llmstxt.org/ 官方规范以确保完全合规
- 理解所需的格式结构与指南
- 注意具体的 Markdown 结构要求

### 步骤 2：仓库结构分析

- 使用合适工具审视完整仓库结构
- 识别仓库的主要目的与范围
- 盘点重要目录及其用途
- 列出对 LLM 有价值的关键文件

### 步骤 3：内容发现

- 识别各处 README 文件
- 寻找文档文件（/docs/、/spec/ 等目录下的 .md）
- 定位规格文件及其用途
- 发现配置文件及其相关性
- 查找示例文件与代码样例
- 识别现有文档体系

### 步骤 4：实施计划

基于分析，制定结构化计划，包含：

- 仓库目的与范围摘要
- 按优先级排序的关键文件清单
- 次要文件（提供附加上下文）
- llms.txt 的章节组织

## 实施要求

### 格式合规

`llms.txt` 文件必须遵循以下结构：

1. **H1 标题**：单行的仓库/项目名称（必需）
2. **引用块简介**：简短描述（可选但推荐）
3. **附加内容**：零个或多个无标题的上下文段落
4. **文件清单章节**：零个或多个 H2 标题，内含链接列表

### 内容要求

#### 必要要素

- **项目名称**：清晰的 H1 标题
- **摘要**：简洁的引用块描述
- **关键文件**：按类别组织的要点列表

#### 文件链接格式

每个链接按如下格式：`[描述性名称](相对路径): 可选说明`

#### 章节组织建议

将文件分组到以下 H2：

- **Documentation**：核心文档
- **Specifications**：技术规格与需求
- **Examples**：示例代码与用法
- **Configuration**：安装与配置
- **Optional**：次要文件（特殊语义——可为简短上下文而跳过）

### 内容指南

#### 语言与风格

- 使用简洁、清晰、无歧义的语言
- 避免无解释的行话
- 同时考虑人类与 LLM 读者
- 描述需具体且信息量充分

#### 文件选择标准

包含：

- 解释仓库目的与范围的文件
- 关键技术文档
- 展示用法与模式的示例
- 定义接口与规格的文件
- 包含配置与安装步骤的文件

排除：

- 纯实现细节
- 冗余信息
- 构建产物或生成文件
- 与理解项目无关内容

## 执行步骤

### 步骤 1：仓库分析

1. 全量审视仓库结构
2. 阅读主 README.md 以理解项目
3. 识别所有文档目录与文件
4. 盘点规格文件与用途
5. 查找示例与配置文件

### 步骤 2：内容规划

1. 明确主要目的陈述
2. 撰写引用块简介
3. 将文件按逻辑类别分组
4. 依据对 LLM 的重要性排序
5. 为每个链接撰写说明

### 步骤 3：文件创建

1. 在仓库根创建 `llms.txt`
2. 严格遵循规范格式
3. 包含所有必需章节
4. 使用正确的 Markdown 格式
5. 确保所有相对路径有效

### 步骤 4：校验

1. 验证与 https://llmstxt.org/ 规范一致
2. 确认所有链接有效可访问
3. 确认其作为 LLM 导航入口的有效性
4. 同时具备人机可读性

## 质量保证

### 格式校验

- ✅ H1 标题
- ✅ 引用块简介（如包含）
- ✅ H2 文件清单章节
- ✅ 正确的 Markdown 链接
- ✅ 无损坏或无效链接
- ✅ 全文格式一致

### 内容校验

- ✅ 语言清晰无歧义
- ✅ 覆盖关键文件
- ✅ 组织逻辑清晰
- ✅ 链接说明恰当
- ✅ 有效的 LLM 导航工具

### 规范一致性

- ✅ 严格遵循 https://llmstxt.org/
- ✅ 使用所需 Markdown 结构
- ✅ 恰当使用可选章节
- ✅ 文件路径：仓库根（/llms.txt）

## 示例结构模板

```txt
# [Repository Name]

> [简要说明仓库的目的与范围]

[可选的无标题上下文段落]

## Documentation

- [Main README](README.md): 主项目文档与快速开始
- [Contributing Guide](CONTRIBUTING.md): 贡献指南
- [Code of Conduct](CODE_OF_CONDUCT.md): 社区规范

## Specifications

- [Technical Specification](spec/technical-spec.md): 技术要求与约束
- [API Specification](spec/api-spec.md): 接口定义与数据契约

## Examples

- [Basic Example](examples/basic-usage.md): 基础用法示例
- [Advanced Example](examples/advanced-usage.md): 复杂实现示例

## Configuration

- [Setup Guide](docs/setup.md): 安装与配置
- [Deployment Guide](docs/deployment.md): 生产部署指南

## Optional

- [Architecture Documentation](docs/architecture.md): 系统架构
- [Design Decisions](docs/decisions.md): 历史设计决策
```

## 成功标准

所创建的 `llms.txt` 应：

1. 使 LLM 快速理解仓库目的
2. 提供清晰的关键文档导航
3. 严格遵循官方规范
4. 全面同时简明
5. 同时服务人机读者
6. 包含项目理解所需关键文件
7. 全程语言清晰无歧义
8. 内容组织逻辑易于消费

```

```
