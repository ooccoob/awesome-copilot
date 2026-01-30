---
description: '使用官方 rmcp SDK 和 async/await 模式在 Rust 中构建模型上下文协议服务器的最佳实践'
applyTo: '**/*.rs'
---

# Rust MCP 服务器开发最佳实践

本指南提供了使用官方 Rust SDK (`rmcp`) 构建模型上下文协议 (MCP) 服务器的最佳实践。

## 安装和设置

### 添加依赖

将 `rmcp` crate 添加到您的 `Cargo.toml`：

```toml
[dependencies]
rmcp = { version = "0.8.1", features = ["server"] }
tokio = { version = "1", features = ["full"] }
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
anyhow = "1.0"
tracing = "0.1"
tracing-subscriber = "0.3"
```

对于宏支持：

```toml
[dependencies]
rmcp-macros = "0.8"
schemars = { version = "0.8", features = ["derive"] }
```

### 项目结构

组织您的 Rust MCP 服务器项目：

```
my-mcp-server/
├── Cargo.toml
├── src/
│   ├── main.rs           # 服务器入口点
│   ├── handler.rs        # ServerHandler 实现
│   ├── tools/
│   │   ├── mod.rs
│   │   ├── calculator.rs
│   │   └── greeter.rs
│   ├── prompts/
│   │   ├── mod.rs
│   │   └── code_review.rs
│   └── resources/
│       ├── mod.rs
│       └── data.rs
└── tests/
    └── integration_tests.rs
```

## 服务器实现

### 基本服务器设置

使用 stdio 传输创建服务器：

```rust
use rmcp::{
    protocol::ServerCapabilities,
    server::{Server, ServerHandler},
    transport::StdioTransport,
};
use tokio::signal;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    tracing_subscriber::fmt::init();

    let handler = MyServerHandler::new();
    let transport = StdioTransport::new();

    let server = Server::builder()
        .with_handler(handler)
        .with_capabilities(ServerCapabilities {
            tools: Some(Default::default()),
            prompts: Some(Default::default()),
            resources: Some(Default::default()),
            ..Default::default()
        })
        .build(transport)?;

    server.run(signal::ctrl_c()).await?;

    Ok(())
}
```

### ServerHandler 实现

实现 `ServerHandler` trait：

```rust
use rmcp::{
    model::*,
    protocol::*,
    server::{RequestContext, ServerHandler, RoleServer},
    ErrorData,
};

pub struct MyServerHandler {
    tool_router: ToolRouter,
}

impl MyServerHandler {
    pub fn new() -> Self {
        Self {
            tool_router: Self::create_tool_router(),
        }
    }

    fn create_tool_router() -> ToolRouter {
        // 初始化并返回工具路由器
        ToolRouter::new()
    }
}

#[async_trait::async_trait]
impl ServerHandler for MyServerHandler {
    async fn list_tools(
        &self,
        _request: Option<PaginatedRequestParam>,
        _context: RequestContext<RoleServer>,
    ) -> Result<ListToolsResult, ErrorData> {
        let items = self.tool_router.list_all();
        Ok(ListToolsResult::with_all_items(items))
    }

    async fn call_tool(
        &self,
        request: CallToolRequestParam,
        context: RequestContext<RoleServer>,
    ) -> Result<CallToolResult, ErrorData> {
        let tcc = ToolCallContext::new(self, request, context);
        self.tool_router.call(tcc).await
    }
}
```

## 工具开发

### 使用宏开发工具

使用 `rmcp-macros` crate 简化工具定义：

```rust
use rmcp::{model::*, server::tool};
use schemars::JsonSchema;
use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema)]
pub struct CalculatorInput {
    /// First operand
    pub a: f64,
    /// Second operand
    pub b: f64,
    /// Operation to perform
    pub operation: String,
}

#[tool(description = "执行基本数学运算")]
pub async fn calculator(input: CalculatorInput) -> anyhow::Result<CallToolResult> {
    let result = match input.operation.as_str() {
        "add" => input.a + input.b,
        "subtract" => input.a - input.b,
        "multiply" => input.a * input.b,
        "divide" => {
            if input.b == 0.0 {
                return Err(anyhow::anyhow!("除零错误"));
            }
            input.a / input.b
        }
        _ => return Err(anyhow::anyhow!("未知操作：{}", input.operation)),
    };

    Ok(CallToolResult::success(vec![Content::text(
        format!("{} {} {} = {}", input.a, input.operation, input.b, result)
    )]))
}
```

### 手动工具实现

不使用宏手动实现工具：

```rust
use rmcp::{
    model::{CallToolRequestParam, CallToolResult, Content, Tool},
    server::{ToolCallContext, ToolHandler},
};

pub struct CalculatorTool;

#[async_trait::async_trait]
impl ToolHandler for CalculatorTool {
    fn name(&self) -> &str {
        "calculator"
    }

    fn description(&self) -> &str {
        "执行基本数学运算"
    }

    fn input_schema(&self) -> serde_json::Value {
        serde_json::json!({
            "type": "object",
            "properties": {
                "a": {
                    "type": "number",
                    "description": "第一个操作数"
                },
                "b": {
                    "type": "number",
                    "description": "第二个操作数"
                },
                "operation": {
                    "type": "string",
                    "enum": ["add", "subtract", "multiply", "divide"],
                    "description": "要执行的操作"
                }
            },
            "required": ["a", "b", "operation"]
        })
    }

    async fn call(
        &self,
        request: CallToolRequestParam,
        _context: ToolCallContext,
    ) -> Result<CallToolResult, rmcp::ErrorData> {
        let args = request.arguments.ok_or_else(|| {
            rmcp::ErrorData::invalid_params("缺少参数")
        })?;

        let a: f64 = serde_json::from_value(args["a"].clone())
            .map_err(|_| rmcp::ErrorData::invalid_params("无效的参数 a"))?;

        let b: f64 = serde_json::from_value(args["b"].clone())
            .map_err(|_| rmcp::ErrorData::invalid_params("无效的参数 b"))?;

        let operation: String = serde_json::from_value(args["operation"].clone())
            .map_err(|_| rmcp::ErrorData::invalid_params("无效的操作参数"))?;

        let result = match operation.as_str() {
            "add" => a + b,
            "subtract" => a - b,
            "multiply" => a * b,
            "divide" => {
                if b == 0.0 {
                    return Err(rmcp::ErrorData::invalid_params("除零错误"));
                }
                a / b
            }
            _ => return Err(rmcp::ErrorData::invalid_params(
                format!("未知操作：{}", operation)
            )),
        };

        Ok(CallToolResult::success(vec![Content::text(
            format!("{} {} {} = {}", a, operation, b, result)
        )]))
    }
}
```

## 提示开发

### 创建提示模板

```rust
use rmcp::{
    model::{GetPromptResult, Prompt, PromptMessage},
    server::{PromptCallContext, PromptHandler},
};

pub struct CodeReviewPrompt;

#[async_trait::async_trait]
impl PromptHandler for CodeReviewPrompt {
    fn name(&self) -> &str {
        "code_review"
    }

    fn description(&self) -> &str {
        "为代码提供审查反馈"
    }

    fn arguments(&self) -> Vec<PromptArgument> {
        vec![
            PromptArgument {
                name: "code".to_string(),
                description: Some("要审查的代码".to_string()),
                required: Some(true),
            },
            PromptArgument {
                name: "language".to_string(),
                description: Some("编程语言".to_string()),
                required: Some(false),
            },
        ]
    }

    async fn get(
        &self,
        request: GetPromptRequestParam,
        _context: PromptCallContext,
    ) -> Result<GetPromptResult, rmcp::ErrorData> {
        let args = request.arguments.unwrap_or_default();

        let code = args.get("code")
            .and_then(|v| v.as_str())
            .ok_or_else(|| rmcp::ErrorData::invalid_params("缺少代码参数"))?;

        let language = args.get("language")
            .and_then(|v| v.as_str())
            .unwrap_or("unknown");

        let description = format!("对 {} 代码的审查", language);
        let messages = vec![
            PromptMessage {
                role: PromptMessageRole::User,
                content: Content::text(format!(
                    "请审查以下 {} 代码并提供反馈：\n\n{}",
                    language, code
                )),
            },
        ];

        Ok(GetPromptResult {
            description,
            messages,
        })
    }
}
```

## 资源开发

### 实现资源处理器

```rust
use rmcp::{
    model::{Content, ListResourcesResult, ReadResourceResult, Resource},
    server::{ReadResourceContext, ResourceHandler},
};

pub struct DataFileResource;

#[async_trait::async_trait]
impl ResourceHandler for DataFileResource {
    fn name(&self) -> &str {
        "data_file"
    }

    fn description(&self) -> &str {
        "提供对数据文件的访问"
    }

    fn uri(&self) -> &str {
        "data://example/file.txt"
    }

    fn mime_type(&self) -> Option<&str> {
        Some("text/plain")
    }

    async fn read(
        &self,
        _request: ReadResourceRequestParam,
        _context: ReadResourceContext,
    ) -> Result<ReadResourceResult, rmcp::ErrorData> {
        // 在实际实现中，这里会读取文件内容
        let content = "这是示例数据文件内容。".to_string();

        Ok(ReadResourceResult {
            contents: vec![Content::text(content)],
        })
    }
}
```

## 错误处理

### 自定义错误类型

```rust
use thiserror::Error;

#[derive(Error, Debug)]
pub enum ServerError {
    #[error("工具未找到：{name}")]
    ToolNotFound { name: String },

    #[error("参数无效：{message}")]
    InvalidParams { message: String },

    #[error("操作失败：{source}")]
    OperationFailed { source: anyhow::Error },
}

impl From<ServerError> for rmcp::ErrorData {
    fn from(err: ServerError) -> Self {
        match err {
            ServerError::ToolNotFound { .. } => rmcp::ErrorData::method_not_found(err.to_string()),
            ServerError::InvalidParams { .. } => rmcp::ErrorData::invalid_params(err.to_string()),
            ServerError::OperationFailed { .. } => rmcp::ErrorData::internal_error(err.to_string()),
        }
    }
}
```

### 错误处理模式

```rust
async fn safe_tool_execution(
    tool_name: &str,
    args: serde_json::Value,
) -> Result<CallToolResult, rmcp::ErrorData> {
    let result = async {
        // 执行工具逻辑
        execute_tool(tool_name, args).await
    }.await;

    match result {
        Ok(output) => Ok(CallToolResult::success(vec![Content::text(output)])),
        Err(err) => {
            tracing::error!("工具执行失败：{} - {:?}", tool_name, err);
            Err(rmcp::ErrorData::internal_error(format!(
                "工具 {} 执行失败：{}",
                tool_name, err
            )))
        }
    }
}
```

## 测试

### 单元测试

```rust
#[cfg(test)]
mod tests {
    use super::*;
    use rmcp::model::*;

    #[tokio::test]
    async fn test_calculator_add() {
        let tool = CalculatorTool;

        let request = CallToolRequestParam {
            name: "calculator".to_string(),
            arguments: Some(serde_json::json!({
                "a": 5.0,
                "b": 3.0,
                "operation": "add"
            })),
        };

        let context = create_test_context();
        let result = tool.call(request, context).await;

        assert!(result.is_ok());
        let call_result = result.unwrap();
        assert!(!call_result.isError);
        assert!(call_result.content[0].text().unwrap().contains("8"));
    }

    #[tokio::test]
    async fn test_calculator_divide_by_zero() {
        let tool = CalculatorTool;

        let request = CallToolRequestParam {
            name: "calculator".to_string(),
            arguments: Some(serde_json::json!({
                "a": 5.0,
                "b": 0.0,
                "operation": "divide"
            })),
        };

        let context = create_test_context();
        let result = tool.call(request, context).await;

        assert!(result.is_err());
        let error = result.unwrap_err();
        assert!(error.message.contains("除零"));
    }
}
```

### 集成测试

```rust
#[tokio::test]
async fn test_server_integration() -> anyhow::Result<()> {
    let handler = MyServerHandler::new();
    let transport = StdioTransport::new();

    let server = Server::builder()
        .with_handler(handler)
        .with_capabilities(ServerCapabilities::builder()
            .tools(Some(Default::default()))
            .build())
        .build(transport)?;

    // 模拟客户端连接和工具调用
    let client = create_test_client(server).await?;

    let tools = client.list_tools(None).await?;
    assert!(!tools.tools.is_empty());

    let result = client.call_tool(CallToolRequestParam {
        name: "calculator".to_string(),
        arguments: Some(serde_json::json!({
            "a": 10.0,
            "b": 5.0,
            "operation": "subtract"
        })),
    }).await?;

    assert!(!result.isError);
    Ok(())
}
```

## 性能优化

### 并发处理

```rust
use tokio::sync::Semaphore;

pub struct ConcurrentToolHandler {
    semaphore: Semaphore,
    tools: HashMap<String, Box<dyn ToolHandler + Send + Sync>>,
}

impl ConcurrentToolHandler {
    pub fn new(max_concurrent: usize) -> Self {
        Self {
            semaphore: Semaphore::new(max_concurrent),
            tools: HashMap::new(),
        }
    }

    pub async fn call_tool_concurrent(
        &self,
        request: CallToolRequestParam,
        context: ToolCallContext,
    ) -> Result<CallToolResult, rmcp::ErrorData> {
        let _permit = self.semaphore.acquire().await
            .map_err(|_| rmcp::ErrorData::internal_error("信号量获取失败".to_string()))?;

        if let Some(tool) = self.tools.get(&request.name) {
            tool.call(request, context).await
        } else {
            Err(rmcp::ErrorData::method_not_found(format!(
                "工具 {} 未找到",
                request.name
            )))
        }
    }
}
```

### 缓存机制

```rust
use std::collections::LRU;
use tokio::sync::RwLock;

pub struct CachedToolHandler {
    cache: Arc<RwLock<Lru<String, CallToolResult>>>,
    inner: Box<dyn ToolHandler>,
}

impl CachedToolHandler {
    pub fn new(inner: Box<dyn ToolHandler>, cache_size: usize) -> Self {
        Self {
            cache: Arc::new(RwLock::new(LRU::new(
                std::num::NonZeroUsize::new(cache_size).unwrap()
            ))),
            inner,
        }
    }

    async fn get_cache_key(&self, request: &CallToolRequestParam) -> String {
        format!("{}:{:?}", request.name, request.arguments)
    }
}

#[async_trait::async_trait]
impl ToolHandler for CachedToolHandler {
    fn name(&self) -> &str {
        self.inner.name()
    }

    fn description(&self) -> &str {
        self.inner.description()
    }

    fn input_schema(&self) -> serde_json::Value {
        self.inner.input_schema()
    }

    async fn call(
        &self,
        request: CallToolRequestParam,
        context: ToolCallContext,
    ) -> Result<CallToolResult, rmcp::ErrorData> {
        let cache_key = self.get_cache_key(&request).await;

        // 检查缓存
        {
            let cache = self.cache.read().await;
            if let Some(result) = cache.get(&cache_key) {
                return Ok(result.clone());
            }
        }

        // 执行工具
        let result = self.inner.call(request, context).await?;

        // 更新缓存
        {
            let mut cache = self.cache.write().await;
            cache.put(cache_key, result.clone());
        }

        Ok(result)
    }
}
```

## 日志记录和监控

### 结构化日志记录

```rust
use tracing::{info, warn, error, instrument};

#[instrument(skip(self, context))]
async fn call_tool(
    &self,
    request: CallToolRequestParam,
    context: ToolCallContext,
) -> Result<CallToolResult, rmcp::ErrorData> {
    info!(
        tool_name = %request.name,
        args = ?request.arguments,
        "调用工具"
    );

    let start = std::time::Instant::now();

    let result = match self.execute_tool(&request, &context).await {
        Ok(result) => {
            info!(
                duration_ms = start.elapsed().as_millis(),
                "工具执行成功"
            );
            result
        }
        Err(err) => {
            error!(
                error = %err,
                duration_ms = start.elapsed().as_millis(),
                "工具执行失败"
            );
            return Err(err);
        }
    };

    Ok(result)
}
```

### 指标收集

```rust
use std::sync::atomic::{AtomicU64, Ordering};

pub struct Metrics {
    pub tool_calls_total: AtomicU64,
    pub tool_errors_total: AtomicU64,
    pub avg_execution_time_ms: AtomicU64,
}

impl Metrics {
    pub fn new() -> Self {
        Self {
            tool_calls_total: AtomicU64::new(0),
            tool_errors_total: AtomicU64::new(0),
            avg_execution_time_ms: AtomicU64::new(0),
        }
    }

    pub fn record_tool_call(&self, duration_ms: u64, success: bool) {
        self.tool_calls_total.fetch_add(1, Ordering::Relaxed);

        if !success {
            self.tool_errors_total.fetch_add(1, Ordering::Relaxed);
        }

        // 简单的移动平均
        let current_avg = self.avg_execution_time_ms.load(Ordering::Relaxed);
        let new_avg = (current_avg + duration_ms) / 2;
        self.avg_execution_time_ms.store(new_avg, Ordering::Relaxed);
    }
}
```

## 部署和运维

### Docker 部署

```dockerfile
FROM rust:1.75 as builder

WORKDIR /app
COPY Cargo.toml Cargo.lock ./
COPY src ./src

RUN cargo build --release

FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y ca-certificates && rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/target/release/my-mcp-server /usr/local/bin/

ENTRYPOINT ["my-mcp-server"]
```

### 配置管理

```rust
use serde::Deserialize;

#[derive(Debug, Deserialize)]
pub struct Config {
    pub server: ServerConfig,
    pub logging: LoggingConfig,
    pub tools: ToolsConfig,
}

#[derive(Debug, Deserialize)]
pub struct ServerConfig {
    pub max_concurrent_requests: usize,
    pub request_timeout_ms: u64,
}

#[derive(Debug, Deserialize)]
pub struct LoggingConfig {
    pub level: String,
    pub format: String,
}

impl Config {
    pub fn from_file(path: &str) -> anyhow::Result<Self> {
        let content = std::fs::read_to_string(path)?;
        let config: Config = toml::from_str(&content)?;
        Ok(config)
    }

    pub fn from_env() -> Self {
        Config {
            server: ServerConfig {
                max_concurrent_requests: std::env::var("MAX_CONCURRENT_REQUESTS")
                    .ok()
                    .and_then(|s| s.parse().ok())
                    .unwrap_or(100),
                request_timeout_ms: std::env::var("REQUEST_TIMEOUT_MS")
                    .ok()
                    .and_then(|s| s.parse().ok())
                    .unwrap_or(30000),
            },
            logging: LoggingConfig {
                level: std::env::var("LOG_LEVEL").unwrap_or_else(|_| "info".to_string()),
                format: std::env::var("LOG_FORMAT").unwrap_or_else(|_| "json".to_string()),
            },
            tools: ToolsConfig::default(),
        }
    }
}
```

## 总结

使用 Rust 和 `rmcp` SDK 构建 MCP 服务器提供了：
- 类型安全的 API 定义
- 高性能的异步处理
- 强大的错误处理
- 优秀的测试支持
- 丰富的生态系统集成

遵循这些最佳实践将帮助您构建可靠、高性能的 MCP 服务器。