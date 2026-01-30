## Ruby MCP Server Generator — Mind Map

### What
- 使用官方 Ruby MCP SDK 生成可运行、含工具/提示/资源与测试的完整服务器项目。

### When
- 需要快速搭建可集成的 MCP 服务器与最小演示/测试覆盖时。

### Why
- 降低脚手架成本，统一结构与质量门槛，便于扩展与集成。

### How
- 询问项目参数→生成 Gemfile/Rakefile/lib/bin/test/README→实现工具/提示/资源→加测试与 RuboCop→提供运行与集成示例。

### Key Points (中/英)
- 工具/Tools
- 提示/Prompts
- 资源/Resources
- 结构/Structure
- 测试/Tests
- 传输/Transport (stdio)

### Compact map
- Files: Gemfile, Rakefile, lib/*, bin/mcp-server, test/*, README
- Tools: greet, calculate (schema + annotations)
- Prompts: code_review
- Resources: example-data
- Usage: bundle exec bin/mcp-server

### Example Questions (≥10)
- 如何参数化项目名与命名空间以符合 Ruby 规范？
- 工具输入/输出 schema 与注解如何设计更健壮？
- 何时需要 is_error 与结构化内容返回？
- 如何组织 prompts 与资源读取回调？
- Rake 任务如何串起测试与 RuboCop？
- 如何与 Claude Desktop/HTTP 集成？
- 生产可用的日志与错误处理建议？
- 如何扩展更多工具并保持目录清晰？
- 测试如何覆盖边界情况（除零/非法操作）？
- 发布与版本化（VERSION 常量）如何管理？

---
- Source: d:\mycode\awesome-copilot\prompts\ruby-mcp-server-generator.prompt.md
- Generated: 2025-10-17
