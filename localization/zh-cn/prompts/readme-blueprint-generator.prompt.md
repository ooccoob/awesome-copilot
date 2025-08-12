---
description: '智能生成 README.md 的提示：分析项目文档结构，产出结构化、跨引用充分、面向开发者的仓库文档；会扫描 .github/copilot 目录与 copilot-instructions.md，抽取技术栈、架构、开发流程、代码规范与测试方法等关键信息，并以规范 Markdown 输出。'
---

# README 生成器提示

通过分析 `.github/copilot` 目录中的文档与 `.github` 下的 `copilot-instructions.md`，为本仓库生成一份全面的 README.md。按以下步骤执行：

1. 扫描 `.github/copilot` 目录的全部文件，例如：
   - Architecture
   - Code_Exemplars
   - Coding_Standards
   - Project_Folder_Structure
   - Technology_Stack
   - Unit_Tests
   - Workflow_Analysis

2. 同时查看 `.github` 目录下的 `copilot-instructions.md`

3. 生成包含以下板块的 README.md：

## 项目名称与简介（Project Name and Description）
- 从文档中提取项目名称与主要目标
- 简要说明项目做什么

## 技术栈（Technology Stack）
- 列出主要技术、语言与框架
- 若有版本信息请包含
- 主要来源：Technology_Stack 文档

## 项目架构（Project Architecture）
- 提供高层架构概览
- 若文档中描述了图示，可考虑以文字方式说明
- 主要来源：Architecture 文档

## 快速开始（Getting Started）
- 基于技术栈提供安装指导
- 添加配置与环境准备步骤
- 列出前置条件

## 目录结构（Project Structure）
- 介绍文件夹组织
- 主要来源：Project_Folder_Structure 文档

## 关键特性（Key Features）
- 罗列主要功能点
- 综合多份文档提炼

## 开发流程（Development Workflow）
- 概述开发流程
- 若有分支策略，简要说明
- 主要来源：Workflow_Analysis 文档

## 代码规范（Coding Standards）
- 概述关键约定与规范
- 主要来源：Coding_Standards 文档

## 测试（Testing）
- 说明测试方法与工具
- 主要来源：Unit_Tests 文档

## 贡献（Contributing）
- 贡献指南
- 可参考 Code_Exemplars 与 copilot-instructions

## 许可证（License）
- 若有，包含许可证信息

请以规范 Markdown 格式编排：
- 清晰的标题与子标题
- 适当的代码块
- 便于阅读的列表
- 链接到其他文档
- 若有可用信息，可添加徽章（构建状态、版本等）

保持 README 简明而信息充分，聚焦新开发者/使用者需要了解的内容。
