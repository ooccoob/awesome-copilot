# Coding, security, and testing rules for WordPress plugins and themes - Instructions Mindmap

## 📊 摘要
Coding, security, and testing rules for WordPress plugins and themes

本指令提供了关于Coding, security, and testing rules for WordPress plugins and themes的核心规范和最佳实践,帮助开发者编写高质量、可维护的代码。

## 🎯 适用范围
- **文件类型**: `wp-content/plugins/**,wp-content/themes/**,**/*.php,**/*.inc,**/*.js,**/*.jsx,**/*.ts,**/*.tsx,**/*.css,**/*.scss,**/*.json`
- **技术栈**: 见文档详情
- **场景**: 开发和维护Coding, security, and testing rules for WordPress plugins and themes相关项目时使用

## 💡 核心规则与最佳实践

### 主要规范
- Never modify WordPress core. Extend via **actions** and **filters**.
- For plugins, always include a header and guard direct execution in entry PHP files.
- Use unique prefixes or PHP namespaces to avoid global collisions.
- Enqueue assets; never inline raw `<script>`/`<style>` in PHP templates.
- Make user‑facing strings translatable and load the correct text domain.
- Follow **WordPress Coding Standards (WPCS)** and write DocBlocks for public APIs.
- PHP: Prefer strict comparisons (`===`, `!==`) where appropriate. Be consistent with array syntax and spacing as per WPCS.
- JS: Match WordPress JS style; prefer `@wordpress/*` packages for block/editor code.

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
- Coding, security, and testing rules for WordPress plugins and themes
  - 适用范围
    - 文件类型: wp-content/plugins/**,wp-content/themes/**,**/*.php,**/*.inc,**/*.js,**/*.jsx,**/*.ts,**/*.tsx,**/*.css,**/*.scss,**/*.json
  - 核心规则
    - 1) Core Principles
    - 2) Coding Standards (PHP, JS, CSS, HTML)
    - 3) Security & Data Handling
    - 4) Internationalization (i18n)
    - 5) Performance
  - 最佳实践
    - 代码质量
    - 性能优化
    - 安全考虑
```

## 💾 保存说明
- 文件名: wordpress.instructions.mindmap.md
- 位置: Mind Map/instructions/
- 生成时间: 2025-10-13 19:58:01
- 文件类型: Instructions (编程规范/最佳实践)
