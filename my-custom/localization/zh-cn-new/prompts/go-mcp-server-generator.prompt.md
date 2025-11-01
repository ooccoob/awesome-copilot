---
mode: agent
description: '使用官方github.com/modelcontextprotocol/go-sdk生成完整的Go MCP服务器项目，包含正确的结构、依赖和实现。'
---

# Go MCP服务器项目生成器

生成一个完整的、生产就绪的Go模型上下文协议（MCP）服务器项目。

## 项目要求

您将创建一个Go MCP服务器，包含：

1. **项目结构**：正确的Go模块布局
2. **依赖**：官方MCP SDK和必要的包
3. **服务器设置**：配置了传输的MCP服务器
4. **工具**：至少2-3个具有类型化输入/输出的有用工具
5. **错误处理**：正确的错误处理和上下文使用
6. **文档**：包含设置和使用说明的README
7. **测试**：基本测试结构

## 模板结构

```
myserver/
├── go.mod
├── go.sum
├── main.go
├── tools/
│   ├── tool1.go
│   └── tool2.go
├── resources/
│   └── resource1.go
├── config/
│   └── config.go
├── README.md
└── main_test.go
```

## go.mod模板

```go
module github.com/yourusername/{{PROJECT_NAME}}

go 1.23

require (
    github.com/modelcontextprotocol/go-sdk v1.0.0
)
```

## main.go模板

```go
package main

import (
    "context"
    "log"
    "os"
    "os/signal"
    "syscall"

    "github.com/modelcontextprotocol/go-sdk/mcp"
    "github.com/yourusername/{{PROJECT_NAME}}/config"
    "github.com/yourusername/{{PROJECT_NAME}}/tools"
)

func main() {
    cfg := config.Load()

    ctx, cancel := context.WithCancel(context.Background())
    defer cancel()

    // 处理优雅关闭
    sigCh := make(chan os.Signal, 1)
    signal.Notify(sigCh, os.Interrupt, syscall.SIGTERM)
    go func() {
        <-sigCh
        log.Println("Shutting down...")
        cancel()
    }()

    // 创建服务器
    server := mcp.NewServer(
        &mcp.Implementation{
            Name:    cfg.ServerName,
            Version: cfg.Version,
        },
        &mcp.Options{
            Capabilities: &mcp.ServerCapabilities{
                Tools:     &mcp.ToolsCapability{},
                Resources: &mcp.ResourcesCapability{},
                Prompts:   &mcp.PromptsCapability{},
            },
        },
    )

    // 注册工具
    tools.RegisterTools(server)

    // 运行服务器
    transport := &mcp.StdioTransport{}
    if err := server.Run(ctx, transport); err != nil {
        log.Fatalf("Server error: %v", err)
    }
}
```

## tools/tool1.go模板

```go
package tools

import (
    "context"
    "fmt"

    "github.com/modelcontextprotocol/go-sdk/mcp"
)

type Tool1Input struct {
    Param1 string `json:"param1" jsonschema:"required,description=First parameter"`
    Param2 int    `json:"param2,omitempty" jsonschema:"description=Optional second parameter"`
}

type Tool1Output struct {
    Result string `json:"result" jsonschema:"description=The result of the operation"`
    Status string `json:"status" jsonschema:"description=Operation status"`
}

func Tool1Handler(ctx context.Context, req *mcp.CallToolRequest, input Tool1Input) (
    *mcp.CallToolResult,
    Tool1Output,
    error,
) {
    // 验证输入
    if input.Param1 == "" {
        return nil, Tool1Output{}, fmt.Errorf("param1 is required")
    }

    // 检查上下文
    if ctx.Err() != nil {
        return nil, Tool1Output{}, ctx.Err()
    }

    // 执行操作
    result := fmt.Sprintf("Processed: %s", input.Param1)

    return nil, Tool1Output{
        Result: result,
        Status: "success",
    }, nil
}

func RegisterTool1(server *mcp.Server) {
    mcp.AddTool(server,
        &mcp.Tool{
            Name:        "tool1",
            Description: "Description of what tool1 does",
        },
        Tool1Handler,
    )
}
```

## tools/registry.go模板

```go
package tools

import "github.com/modelcontextprotocol/go-sdk/mcp"

func RegisterTools(server *mcp.Server) {
    RegisterTool1(server)
    RegisterTool2(server)
    // 在此处注册其他工具
}
```

## config/config.go模板

```go
package config

import "os"

type Config struct {
    ServerName string
    Version    string
    LogLevel   string
}

func Load() *Config {
    return &Config{
        ServerName: getEnv("SERVER_NAME", "{{PROJECT_NAME}}"),
        Version:    getEnv("VERSION", "v1.0.0"),
        LogLevel:   getEnv("LOG_LEVEL", "info"),
    }
}

func getEnv(key, defaultValue string) string {
    if value := os.Getenv(key); value != "" {
        return value
    }
    return defaultValue
}
```

## main_test.go模板

```go
package main

import (
    "context"
    "testing"

    "github.com/yourusername/{{PROJECT_NAME}}/tools"
)

func TestTool1Handler(t *testing.T) {
    ctx := context.Background()
    input := tools.Tool1Input{
        Param1: "test",
        Param2: 42,
    }

    result, output, err := tools.Tool1Handler(ctx, nil, input)
    if err != nil {
        t.Fatalf("Tool1Handler failed: %v", err)
    }

    if output.Status != "success" {
        t.Errorf("Expected status 'success', got '%s'", output.Status)
    }

    if result != nil {
        t.Error("Expected result to be nil")
    }
}
```

## README.md模板

```markdown
# {{PROJECT_NAME}}

使用Go构建的模型上下文协议（MCP）服务器。

## 描述

{{PROJECT_DESCRIPTION}}

## 安装

\`\`\`bash
go mod download
go build -o {{PROJECT_NAME}}
\`\`\`

## 使用

使用stdio传输运行服务器：

\`\`\`bash
./{{PROJECT_NAME}}
\`\`\`

## 配置

通过环境变量配置：

- `SERVER_NAME`：服务器名称（默认："{{PROJECT_NAME}}"）
- `VERSION`：服务器版本（默认："v1.0.0"）
- `LOG_LEVEL`：日志记录级别（默认："info"）

## 可用工具

### tool1
{{TOOL1_DESCRIPTION}}

**输入：**
- `param1`（字符串，必需）：第一个参数
- `param2`（整数，可选）：第二个参数

**输出：**
- `result`（字符串）：操作结果
- `status`（字符串）：操作状态

## 开发

运行测试：

\`\`\`bash
go test ./...
\`\`\`

构建：

\`\`\`bash
go build -o {{PROJECT_NAME}}
\`\`\`

## 许可证

MIT
```

## 生成指令

生成Go MCP服务器时：

1. **初始化模块**：创建具有正确模块路径的`go.mod`
2. **结构**：遵循模板目录结构
3. **类型安全**：为所有输入/输出使用带有JSON模式标签的结构体
4. **错误处理**：验证输入、检查上下文、包装错误
5. **文档**：添加清晰的描述和示例
6. **测试**：每个工具至少包含一个测试
7. **配置**：使用环境变量进行配置
8. **日志记录**：使用结构化日志记录（log/slog）
9. **优雅关闭**：正确处理信号
10. **传输**：默认为stdio，记录替代方案

## 最佳实践

- 保持工具专注且单一目的
- 为类型和函数使用描述性名称
- 在结构体标签中包含JSON模式文档
- 始终尊重上下文取消
- 返回描述性错误
- 保持main.go最小，逻辑放在包中
- 为工具处理器编写测试
- 记录所有导出的函数