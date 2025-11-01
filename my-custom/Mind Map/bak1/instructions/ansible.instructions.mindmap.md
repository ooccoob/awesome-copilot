# Ansible conventions and best practices - Instructions Mindmap

## 📊 摘要
Ansible conventions and best practices

本指令提供了关于Ansible conventions and best practices的核心规范和最佳实践,帮助开发者编写高质量、可维护的代码。

## 🎯 适用范围
- **文件类型**: `**/*.yaml, **/*.yml`
- **技术栈**: 见文档详情
- **场景**: 开发和维护Ansible conventions and best practices相关项目时使用

## 💡 核心规则与最佳实践

### 主要规范
- Use Ansible to configure and manage infrastructure.
- Use version control for your Ansible configurations.
- Keep things simple; only use advanced features when necessary
- Give every play, block, and task a concise but descriptive `name`
- Use comments to provide additional context about **what**, **how**, and/or **why** something is being done
- Use dynamic inventory for cloud resources
- Use idempotent Ansible modules whenever possible; avoid `shell`, `command`, and `raw`, as they break idempotency
- Group related tasks together to improve readability and modularity

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
- Ansible conventions and best practices
  - 适用范围
    - 文件类型: **/*.yaml, **/*.yml
  - 核心规则
    - General Instructions
    - Secret Management
    - Style
    - Linting
  - 最佳实践
    - 代码质量
    - 性能优化
    - 安全考虑
```

## 💾 保存说明
- 文件名: ansible.instructions.mindmap.md
- 位置: Mind Map/instructions/
- 生成时间: 2025-10-13 19:57:52
- 文件类型: Instructions (编程规范/最佳实践)
