---
description: '智能README.md生成提示，分析项目文档结构并创建全面的仓库文档。扫描.github/copilot目录文件和copilot-instructions.md以提取项目信息、技术栈、架构、开发工作流程、编码标准和测试方法，同时生成格式良好的markdown文档，包含适当的格式、交叉引用和面向开发者的内容。'

mode: 'agent'
---

# README生成器提示

通过分析.github/copilot目录中的文档文件和copilot-instructions.md文件为此仓库生成全面的README.md。请遵循以下步骤：

1. 扫描.github/copilot文件夹中的所有文件，例如：
   - Architecture（架构）
   - Code_Exemplars（代码示例）
   - Coding_Standards（编码标准）
   - Project_Folder_Structure（项目文件夹结构）
   - Technology_Stack（技术栈）
   - Unit_Tests（单元测试）
   - Workflow_Analysis（工作流分析）

2. 同时审查.github文件夹中的copilot-instructions.md文件

3. 使用以下部分创建README.md：

## 项目名称和描述
- 从文档中提取项目名称和主要目的
- 包含项目功能的简明描述

## 技术栈
- 列出使用的主要技术、语言和框架
- 在可用时包含版本信息
- 主要从Technology_Stack文件获取此信息

## 项目架构
- 提供架构的高级概述
- 考虑在文档中描述时包含简单图表
- 从Architecture文件获取信息

## 入门指南
- 基于技术栈包含安装说明
- 添加设置和配置步骤
- 包含任何先决条件

## 项目结构
- 文件夹组织的简要概述
- 从Project_Folder_Structure文件获取信息

## 主要功能
- 列出项目的主要功能和特性
- 从各种文档文件中提取

## 开发工作流程
- 总结开发过程
- 在可用时包含分支策略信息
- 从Workflow_Analysis文件获取信息

## 编码标准
- 总结关键编码标准和约定
- 从Coding_Standards文件获取信息

## 测试
- 解释测试方法和工具
- 从Unit_Tests文件获取信息

## 贡献
- 为项目贡献提供指导
- 引用任何代码示例以获取指导
- 从Code_Exemplars和copilot-instructions获取信息

## 许可证
- 在可用时包含许可证信息

使用适当的Markdown格式化README，包括：
- 清晰的标题和子标题
- 适当的代码块
- 用于提高可读性的列表
- 指向其他文档文件的链接
- 如果信息可用，则为构建状态、版本等添加徽章

保持README简洁而信息丰富，专注于新开发者或用户需要了解的项目信息。