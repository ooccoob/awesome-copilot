---
名称： mcp-cli
描述：通过 CLI 的 MCP（模型上下文协议）服务器接口。当您需要通过 MCP 服务器与外部工具、API 或数据源交互、列出可用的 MCP 服务器/工具或从命令行调用 MCP 工具时使用。
---

# MCP-CLI

通过命令行访问 MCP 服务器。 MCP 支持与 GitHub、文件系统、数据库和 API 等外部系统进行交互。

## 命令

|命令 |输出|
| ---------------------------------- | ------------------------------- |
| __代码0__ |列出所有服务器和工具名称 |
| __代码0__ |显示带参数的工具 |
| __代码0__ |获取工具 JSON 架构 |
| __代码0__ |带参数调用工具 |
| __代码0__ |按名称搜索工具 |

**添加 `-d` 以包含描述**（例如 `mcp-cli filesystem -d`）

## 工作流程

1. **发现**：`mcp-cli` → 查看可用的服务器和工具
2. **探索**：`mcp-cli <server>` → 查看带参数的工具
3. **检查**：`mcp-cli <server>/<tool>` → 获取完整的 JSON 输入模式
4. **执行**：`mcp-cli <server>/<tool> '<json>'` → 使用参数运行

## 示例

```bash
# List all servers and tool names
mcp-cli

# See all tools with parameters
mcp-cli filesystem

# With descriptions (more verbose)
mcp-cli filesystem -d

# Get JSON schema for specific tool
mcp-cli filesystem/read_file

# Call the tool
mcp-cli filesystem/read_file '{"path": "./README.md"}'

# Search for tools
mcp-cli grep "*file*"

# JSON output for parsing
mcp-cli filesystem/read_file '{"path": "./README.md"}' --json

# Complex JSON with quotes (use heredoc or stdin)
mcp-cli server/tool <<EOF
{"content": "Text with 'quotes' inside"}
EOF

# Or pipe from a file/command
cat args.json | mcp-cli server/tool

# Find all TypeScript files and read the first one
mcp-cli filesystem/search_files '{"path": "src/", "pattern": "*.ts"}' --json | jq -r '.content[0].text' | head -1 | xargs -I {} sh -c 'mcp-cli filesystem/read_file "{\"path\": \"{}\"}"'
```

## 选项

|旗帜|目的|
| ------------ | ------------------------- |
| __代码0__ |用于脚本编写的 JSON 输出 |
| __代码0__ |原始文本内容 |
| __代码0__ |包括描述 |

## 退出代码

- `0`：成功
- `1`：客户端错误（参数错误，缺少配置）
- `2`：服务器错误（工具失败）
- `3`：网络错误
