---
description: 'Automatically update README.md and documentation files when application code changes require documentation updates'
applyTo: '**/*.{md,js,mjs,cjs,ts,tsx,jsx,py,java,cs,go,rb,php,rs,cpp,c,h,hpp}'
---

# 更新代码更改文档

## 概述

通过自动检测 README.md、
API文档、配置指南等文档文件需要根据代码进行更新
修改。

## 指令部分和配置

本节的以下部分，`Instruction Sections and Configurable Instruction Sections`
和 `Instruction Configuration` 仅与此指令文件相关，并且是一个
方法轻松修改 Copilot 指令的实施方式。本质上是两部分
旨在打开或关闭实际副驾驶指令的部分或部分，并允许
何时以及如何实施本文档某些部分的自定义案例和条件。

### 指令部分和可配置指令部分

本文档中有几个说明部分。指令部分的开始是
由二级标题指示。将此称为**说明部分**。  一些指令
部分是可配置的。有些是不可配置的并且将始终使用。

可配置的指令部分不是必需的，并且受附加上下文的影响
和/或条件。将这些称为**可配置指令部分**。

**可配置的指令部分**将附加该部分的配置属性
二级标头，用反引号括起来（例如 `apply-this`）。将此称为
**可配置的属性**。

**可配置属性**将在**指令配置**中声明和定义
本节的一部分。它们是布尔值。如果 `true`，则应用、利用和/或遵循
该部分的说明。

每个 **可配置指令部分** 还将有一个跟随该部分的句子
二级标题，包含该部分的配置详细信息。将此称为**配置详细信息**。

**配置详细信息**是扩展可配置指令的规则子集
部分。这允许检查自定义案例和/或条件，从而确定最终结果
**可配置指令部分**的实现。

在解决如何应用**可配置指令部分**之前，请检查
**可配置属性**用于嵌套和/或相应的 `apply-condition`，并在确定 **可配置指令部分**的最终方法时利用 `apply-condition`。由
默认情况下，每个 **可配置属性** 的 `apply-condition` 未设置，但设置的示例
`apply-condition` 可能是这样的：

    - **应用条件**：
      __代码0__

所有**常量指令部分**和**可配置指令部分**的总和
将确定要遵循的完整说明。将此称为**编译指令**。

**编译的指令**取决于配置。各指令部分
包含在**编译的指令**中的内容将被解释和使用，就像一个单独的集合一样
独立于整个指令文件的指令。将此称为
**最终程序**。

### 指令配置

- **应用文档文件结构** : true
  - **应用条件**：未设置
- **应用文档验证**：true
  - **应用条件**：未设置
- **应用文档质量标准**：true
  - **应用条件**：未设置
- **应用自动化工具**：true
  - **应用条件**：未设置
- **应用文档模式**：true
  - **应用条件**：未设置
- **应用最佳实践**：true
  - **应用条件**：未设置
- **应用验证命令**：true
  - **应用条件**：未设置
- **应用维护计划**：true
  - **应用条件**：未设置
- **应用 git 集成** : false
  - **应用条件**：未设置

<!--
|配置属性|默认|描述 |何时启用/禁用 |
|-------------------------------|---------|-----------------------------------------------------------------------------|-------------------------------------------------------------|
|应用文档文件结构 |真实 |确保文档遵循一致的文件结构。                  |如果您想允许自由格式的文档组织，请禁用。    |
|应用文档验证 |真实 |验证文档是否与代码更改匹配。                           |如果在其他地方处理验证则禁用。               |
|应用文档质量标准 |真实 |执行文档质量标准。                                   |如果不需要质量标准，则禁用。              |
|应用自动化工具 |真实 |使用自动化工具更新文档。                              |如果您喜欢手动更新文档，请禁用。         |
|应用文档模式 |真实 |应用常见的文档模式和模板。                        |对于自定义或非常规文档样式禁用。  |
|应用最佳实践 |真实 |强制执行文档中的最佳实践。                                   |如果最佳实践不是优先事项，则禁用。               |
|应用验证命令 |真实 |运行验证命令以检查文档的正确性。                 |如果不需要验证则禁用。                        |
|应用维护计划 |真实 |安排定期文档维护。                                |如果维护管理方式不同，则禁用。              |
|应用 git 集成 |假 |将文档更新与 Git 工作流程集成。                        |如果您想要自动 Git 集成，请启用。               |
-->
## 何时更新文档

### 触发条件

在以下情况下自动检查是否需要更新文档：

- 添加了新特性或功能
- API端点、方法或接口发生变化
- 引入了重大变化
- 依赖关系或需求发生变化
- 配置选项或环境变量被修改
- 安装或设置过程发生变化
- 命令行界面或脚本已更新
- 文档中的代码示例已过时

## 文档更新规则

### README.md 更新

**在以下情况下始终更新 README.md：**

- 添加新特性或功能
  - 在“功能”部分添加功能描述
  - 包括使用示例（如果适用）
  - 更新目录（如果存在）

- 修改安装或设置过程
  - 更新“安装”或“入门”部分
  - 修改依赖关系要求
  - 更新先决条件列表

- 添加新的 CLI 命令或选项
  - 记录命令语法和示例
  - 包括选项说明和默认值
  - 添加使用示例

- 更改配置选项
  - 更新配置示例
  - 记录新的环境变量
  - 更新配置文件模板

### API 文档更新

**在以下情况下同步 API 文档：**

- 添加新端点
  - 记录 HTTP 方法、路径、参数
  - 包括请求/响应示例
  - 更新 OpenAPI/Swagger 规范

- 端点签名更改
  - 更新参数列表
  - 修改响应模式
  - 记录重大变更

- 身份验证或授权更改
  - 更新认证示例
  - 修改安全要求
  - 更新 API 密钥/令牌文档

### 代码示例同步

**在以下情况下验证并更新代码示例：**

- 函数签名改变
  - 使用该函数更新所有代码片段
  - 验证示例仍然可以编译/运行
  - 如果需要更新导入语句

- API接口变更
  - 更新示例请求和响应
  - 修改客户端代码示例
  - 更新SDK使用示例

- 最佳实践不断发展
  - 替换示例中过时的模式
  - 更新以使用当前推荐的方法
  - 添加旧模式的弃用通知

### 配置文档

**在以下情况下更新配置文档：**

- 添加了新的环境变量
  - 添加到 .env.example 文件
  - README.md 或 docs/configuration.md 中的文档
  - 包括默认值和描述

- 配置文件结构更改
  - 更新示例配置文件
  - 记录新选项
  - 标记已弃用的选项

- 部署配置更改
  - 更新 Docker/Kubernetes 配置
  - 修改部署指南
  - 更新基础设施即代码示例

### 迁移和重大变更

**在以下情况下创建迁移指南：**

- 发生重大 API 更改
  - 记录发生的变化
  - 提供之前/之后的示例
  - 包括分步迁移说明

- 主要版本更新
  - 列出所有重大变更
  - 提供升级清单
  - 包括常见的迁移问题和解决方案

- 弃用功能
  - 明确标记已弃用的功能
  - 建议替代方法
  - 包括删除时间表

## 文档文件结构 `apply-doc-file-structure`

如果 `apply-doc-file-structure == true`，则应用以下可配置指令部分。

### 标准文档文件

维护这些文档文件并根据需要进行更新：

- **README.md**：项目概述、快速入门、基本使用
- **CHANGELOG.md**：版本历史记录和面向用户的更改
- **docs/**：详细文档
  - `installation.md`：设置和安装指南
  - `configuration.md`：配置选项和示例
  - `api.md`：API参考文档
  - `contributing.md`：贡献指南
  - `migration-guides/`：版本迁移指南
- **示例/**：工作代码示例和教程

### 变更日志管理

**添加变更日志条目：**

- 新功能（在“添加”部分下）
- 错误修复（在“已修复”部分下）
- 重大变更（在带有 **BREAKING** 前缀的“已更改”部分下）
- 已弃用的功能（在“已弃用”部分下）
- 删除的功能（在“删除”部分下）
- 安全修复（在“安全”部分下）

**变更日志格式：**

    ```markdown
    ## [Version] - YYYY-MM-DD

    ### Added
    - New feature description with reference to PR/issue

    ### Changed
    - **BREAKING**: Description of breaking change
    - Other changes

    ### Fixed
    - Bug fix description
    ```

## 文件验证 `apply-doc-verification`

如果 `apply-doc-verification == true`，则应用以下可配置指令部分。

### 应用更改之前

**检查文档完整性：**

1. 所有新的公共 API 均已记录
2. 代码示例编译并运行
3. 文档中的链接有效
4. 配置示例准确
5. 安装步骤是最新的
6. README.md 反映当前状态

### 文档测试

**包括文档验证：**

#### 示例任务

- 验证文档中的代码示例编译/运行
- 检查是否有损坏的内部/外部链接
- 根据架构验证配置示例
- 确保 API 示例与当前实现匹配

    ```bash
    # Example validation commands
    npm run docs:check         # Verify docs build
    npm run docs:test-examples # Test code examples
    npm run docs:lint         # Check for issues
    ```

## 文档质量标准 `apply-doc-quality-standard`

如果 `apply-doc-quality-standard == true`，则应用以下可配置指令部分。

### 写作指南

- 使用清晰、简洁的语言
- 包括工作代码示例
- 提供基本和高级示例
- 使用一致的术语
- 包括错误处理示例
- 记录边缘情况和限制

### 代码示例格式

    ```markdown
    ### Example: [Clear description of what example demonstrates]

    \`\`\`language
    // Include necessary imports/setup
    import { function } from 'package';

    // Complete, runnable example
    const result = function(parameter);
    console.log(result);
    \`\`\`

    **Output:**
    \`\`\`
    expected output
    \`\`\`
    ```

### API文档格式

    ```markdown
    ### `functionName(param1, param2)`

    Brief description of what the function does.

    **Parameters:**
    - `param1` (type): Description of parameter
    - `param2` (type, optional): Description with default value

    **Returns:**
    - `type`: Description of return value

    **Example:**
    \`\`\`language
    const result = functionName('value', 42);
    \`\`\`

    **Throws:**
    - `ErrorType`: When and why error is thrown
    ```

## 自动化和工具 `apply-automation-tooling`

如果 `apply-automation-tooling == true`，则应用以下可配置指令部分。

### 文档生成

**使用可用的自动化工具：**

#### 自动化工具示例

- JavaScript/TypeScript 的 JSDoc/TSDoc
- 用于 Python 的 Sphinx/pdoc
- Java 的 Javadoc
- C# 的 xmldoc
- Go 的 godoc
- Rust 的 rustdoc

### 文档检查

**验证文档：**

- Markdown 短绒 (markdownlint)
- 链接检查器（markdown-link-check）
- 拼写检查器 (cspell)
- 代码示例验证器

### 更新前的钩子

**添加预提交检查：**

- 文档构建成功
- 没有损坏的链接
- 代码示例有效
- 存在更改的更改日志条目

## 常见文档模式 `apply-doc-patterns`

如果 `apply-doc-patterns == true`，则应用以下可配置指令部分。

### 功能文档模板

    ```markdown
    ## Feature Name

    Brief description of the feature.

    ### Usage

    Basic usage example with code snippet.

    ### Configuration

    Configuration options with examples.

    ### Advanced Usage

    Complex scenarios and edge cases.

    ### Troubleshooting

    Common issues and solutions.
    ```

### API端点文档模板

    ```markdown
    ### `HTTP_METHOD /api/endpoint`

    Description of what the endpoint does.

    **Request:**
    \`\`\`json
    {
      "param": "value"
    }
    \`\`\`

    **Response:**
    \`\`\`json
    {
      "result": "value"
    }
    \`\`\`

    **Status Codes:**
    - 200: Success
    - 400: Bad request
    - 401: Unauthorized
    ```

## 最佳实践`apply-best-practices`

如果 `apply-best-practices == true`，则应用以下可配置指令部分。

### 要做的事

- ✅ 在代码更改时在同一提交中更新文档
- ✅ 包括申请前要审查的更改之前/之后的示例
- ✅ 在提交之前测试代码示例
- ✅ 使用一致的格式和术语
- ✅ 记录限制和边缘情况
- ✅ 提供重大变更的迁移路径
- ✅ 保持文档干燥（链接而不是重复）

### 不该做的事

- ❌ 提交代码更改而不更新文档
- ❌ 在文档中保留过时的示例
- ❌ 记录尚不存在的功能
- ❌ 使用含糊或模棱两可的语言
- ❌ 忘记更新变更日志
- ❌ 忽略损坏的链接或失败的示例
- ❌ 记录用户不需要的实施细节

## 验证示例命令 `apply-validation-commands`

如果 `apply-validation-commands == true`，则应用以下可配置指令部分。

应用于您的项目以进行文档验证的示例脚本：

```json
{
  "scripts": {
    "docs:build": "Build documentation",
    "docs:test": "Test code examples in docs",
    "docs:lint": "Lint documentation files",
    "docs:links": "Check for broken links",
    "docs:spell": "Spell check documentation",
    "docs:validate": "Run all documentation checks"
  }
}
```

## 维护计划`apply-maintenance-schedule`

如果 `apply-maintenance-schedule == true`，则应用以下可配置指令部分。

### 定期回顾

- **每月**：检查文档的准确性
- **每个版本**：更新版本号和示例
- **每季度**：检查是否有过时的模式或已弃用的功能
- **每年**：全面的文件审核

### 弃用流程

弃用功能时：

1. 在文档中添加弃用通知
2. 更新示例以使用推荐的替代方案
3. 创建迁移指南
4. 使用弃用通知更新变更日志
5. 设定移除时间表
6. 在下一个主要版本中，删除已弃用的功能和文档

## Git 集成 `apply-git-integration`

如果 `apply-git-integration == true`，则应用以下可配置指令部分。

### 拉取请求要求

**文档必须在代码更改时在同一 PR 中更新：**

- 在功能 PR 中记录新功能
- 代码更改时更新示例
- 添加包含代码更改的更改日志条目
- 接口更改时更新 API 文档

### 文件审查

**在代码审查期间，验证：**

- 文档准确描述了更改
- 例子清晰、完整
- 没有未记录的重大变更
- 变更日志条目是适当的
- 如果需要，可提供迁移指南

## 审查清单

在考虑文档完整并得出**最终程序**之前：

- [ ] **编译指令**基于**常量指令部分**和
**可配置的指令部分**
- [ ] README.md 反映当前项目状态
- [ ] 所有新功能均已记录
- [ ] 代码示例经过测试并且可以工作
- [ ] API文档完整准确
- [ ] 配置示例是最新的
- [ ] 重大变更记录在迁移指南中
- [ ] CHANGELOG.md 已更新
- [ ] 链接有效且未损坏
- [ ] 安装说明是最新的
- [ ] 环境变量已记录

## 更新有关代码更改的文档 目标

- 尽可能让文档靠近代码
- 使用文档生成器作为 API 参考
- 维护随代码一起发展的动态文档
- 将文档视为功能完整性的一部分
- 在代码审查中审查文档
- 使文档易于查找和导航
