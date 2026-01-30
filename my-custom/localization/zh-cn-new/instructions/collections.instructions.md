---
description: '创建和管理awesome-copilot集合的指南'
applyTo: 'collections/*.collection.yml'
---

# 集合开发

## 集合指令

在awesome-copilot仓库中处理集合时：

- 提交前始终使用`node validate-collections.js`验证集合
- 遵循既定的YAML模式作为集合清单
- 仅引用仓库中现有文件
- 使用描述性集合ID，包含小写字母、数字和连字符
- 保持集合专注于特定工作流或主题
- 测试所有引用的项目是否协同工作良好

## 集合结构

- **必填字段**：id、name、description、items
- **可选字段**：tags、display
- **项目要求**：path必须存在，kind必须匹配文件扩展名
- **显示选项**：ordering（alpha/manual）、show_badge（true/false）

## 验证规则

- 集合ID在所有集合中必须唯一
- 文件路径必须存在且匹配项目类型
- 标签必须仅使用小写字母、数字和连字符
- 集合必须包含1-50个项目
- 描述必须为1-500个字符

## 最佳实践

- 将3-10个相关项目分组以获得最佳可用性
- 使用清晰、描述性的名称和描述
- 添加相关标签以提高可发现性
- 测试集合支持的完整工作流
- 确保项目有效互补

## 文件组织

- 集合不需要文件重组
- 项目可以位于仓库中的任何位置
- 使用从仓库根目录开始的相对路径
- 维护现有目录结构（prompts/、instructions/、chatmodes/）

## 生成过程

- 集合通过`update-readme.js`自动生成README文件
- 单个集合页面在collections/目录中创建
- 主集合概览生成为README.collections.md
- 为每个项目自动创建VS Code安装徽章