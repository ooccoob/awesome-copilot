# TaskSync V4 - Allows you to give the agent new instructions or feedback after completing a task using terminal while agent is running. - Instructions Mindmap

## 📊 摘要
TaskSync V4 - Allows you to give the agent new instructions or feedback after completing a task using terminal while agent is running.

本指令提供了关于TaskSync V4 - Allows you to give the agent new instructions or feedback after completing a task using terminal while agent is running.的核心规范和最佳实践,帮助开发者编写高质量、可维护的代码。

## 🎯 适用范围
- **文件类型**: `**`
- **技术栈**: Python
- **场景**: 开发和维护TaskSync V4 - Allows you to give the agent new instructions or feedback after completing a task using terminal while agent is running.相关项目时使用

## 💡 核心规则与最佳实践

### 主要规范
- Ending the chat/conversation/session for ANY reason except explicit user termination commands ("stop", "end", "terminate", "quit")
- Using ANY phrases that suggest the conversation is ending or complete
- Waiting for the user to ask for help or provide new input
- Stopping the task request cycle under any circumstances
- Acting like the conversation is finished
- Keep the conversation active and ongoing
- Immediately request new tasks after completing any task using ONLY terminal commands
- Execute `$task = Read-Host "Enter your task"` using run_in_terminal tool

### 代码质量标准
- 遵循行业标准编码规范
- 保持代码简洁可读
- 添加适当的注释和文档
- 进行充分的测试覆盖

## 📝 关键技术要点

### 项目配置
- 正确设置开发环境
- 配置必要的工具和依赖
- 遵循项目结构规范

### 实现标准
- 使用推荐的设计模式
- 遵循命名规范
- 注意性能和安全考虑

## 🗺️ 思维导图

```mindmap
- TaskSync V4 - Allows you to give the agent new instructions or feedback after completing a task using terminal while agent is running.
  - 适用范围
    - 文件类型: **
    - 技术栈: Python
  - 核心规则
    - PRIMARY DIRECTIVE STATUS
    - 🚨 CRITICAL PRIMARY DIRECTIVES - ABSOLUTE ENFORCEMENT 🚨
    - Initialization Protocol - PRIMARY DIRECTIVE ACTIVATION
    - Core Behavior Framework - PRIMARY DIRECTIVES
    - Implementation Instructions - PRIMARY DIRECTIVES
  - 最佳实践
    - 代码质量
    - 性能优化
    - 安全考虑
```

## 💾 保存说明
- 文件名: tasksync.instructions.mindmap.md
- 位置: Mind Map/instructions/
- 生成时间: 2025-10-13 19:58:00
- 文件类型: Instructions (编程规范/最佳实践)
