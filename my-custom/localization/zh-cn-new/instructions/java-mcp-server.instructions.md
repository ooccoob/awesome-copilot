---
description: '使用官方 MCP Java SDK 与响应式流和 Spring 集成构建 Java MCP 服务器的最佳实践和模式。'
applyTo: "**/*.java, **/pom.xml, **/build.gradle, **/build.gradle.kts"
---

# Java MCP 服务器开发指南

在 Java 中构建 MCP 服务器时，请遵循使用官方 Java SDK 的这些最佳实践和模式。

## 依赖项

将 MCP Java SDK 添加到您的 Maven 项目：

```xml
<dependencies>
    <dependency>
        <groupId>io.modelcontextprotocol.sdk</groupId>
        <artifactId>mcp</artifactId>
        <version>0.14.1</version>
    </dependency>
</dependencies>
```

或者对于 Gradle：

```kotlin
dependencies {
    implementation("io.modelcontextprotocol.sdk:mcp:0.14.1")
}
```

## 服务器设置

使用构建器模式创建 MCP 服务器：

```java
import io.mcp.server.McpServer;
import io.mcp.server.McpServerBuilder;
import io.mcp.server.transport.StdioServerTransport;

McpServer server = McpServerBuilder.builder()
    .serverInfo("my-server", "1.0.0")
    .capabilities(capabilities -> capabilities
        .tools(true)
        .resources(true)
        .prompts(true))
    .build();

// 使用 stdio 传输启动
StdioServerTransport transport = new StdioServerTransport();
server.start(transport).subscribe();
```

## 添加工具

向服务器注册工具处理器：

```java
import io.mcp.server.tool.Tool;
import io.mcp.server.tool.ToolHandler;
import reactor.core.publisher.Mono;

// 定义工具
Tool searchTool = Tool.builder()
    .name("search")
    .description("搜索信息")
    .inputSchema(JsonSchema.object()
        .property("query", JsonSchema.string()
            .description("搜索查询")
            .required(true))
        .property("limit", JsonSchema.integer()
            .description("最大结果数")
            .defaultValue(10)))
    .build();

// 注册工具处理器
server.addToolHandler("search", (arguments) -> {
    String query = arguments.get("query").asText();
    int limit = arguments.has("limit")
        ? arguments.get("limit").asInt()
        : 10;

    // 执行搜索
    List<String> results = performSearch(query, limit);

    return Mono.just(ToolResponse.success()
        .addTextContent("找到 " + results.size() + " 个结果")
        .build());
});
```

## 添加资源

为数据访问实现资源处理器：

```java
import io.mcp.server.resource.Resource;
import io.mcp.server.resource.ResourceHandler;

// 注册资源列表处理器
server.addResourceListHandler(() -> {
    List<Resource> resources = List.of(
        Resource.builder()
            .name("数据文件")
            .uri("resource://data/example.txt")
            .description("示例数据文件")
            .mimeType("text/plain")
            .build()
    );
    return Mono.just(resources);
});

// 注册资源读取处理器
server.addResourceReadHandler((uri) -> {
    if (uri.equals("resource://data/example.txt")) {
        String content = loadResourceContent(uri);
        return Mono.just(ResourceContent.text(content, uri));
    }
    throw new ResourceNotFoundException(uri);
});

// 注册资源订阅处理器
server.addResourceSubscribeHandler((uri) -> {
    subscriptions.add(uri);
    log.info("客户端订阅了 {}", uri);
    return Mono.empty();
});
```

## 添加提示

为模板化对话实现提示处理器：

```java
import io.mcp.server.prompt.Prompt;
import io.mcp.server.prompt.PromptMessage;
import io.mcp.server.prompt.PromptArgument;

// 注册提示列表处理器
server.addPromptListHandler(() -> {
    List<Prompt> prompts = List.of(
        Prompt.builder()
            .name("analyze")
            .description("分析主题")
            .argument(PromptArgument.builder()
                .name("topic")
                .description("要分析的主题")
                .required(true)
                .build())
            .argument(PromptArgument.builder()
                .name("depth")
                .description("分析深度")
                .required(false)
                .build())
            .build()
    );
    return Mono.just(prompts);
});

// 注册提示获取处理器
server.addPromptGetHandler((name, arguments) -> {
    if (name.equals("analyze")) {
        String topic = arguments.getOrDefault("topic", "general");
        String depth = arguments.getOrDefault("depth", "basic");

        List<PromptMessage> messages = List.of(
            PromptMessage.user("请分析这个主题: " + topic),
            PromptMessage.assistant("我将提供对 " + topic + " 的 " + depth + " 级分析")
        );

        return Mono.just(PromptResult.builder()
            .description(topic + " 的 " + depth + " 级分析")
            .messages(messages)
            .build());
    }
    throw new PromptNotFoundException(name);
});
```

## 响应式流模式

Java SDK 使用响应式流（Project Reactor）进行异步处理：

```java
// 为单个结果返回 Mono
server.addToolHandler("process", (args) -> {
    return Mono.fromCallable(() -> {
        String result = expensiveOperation(args);
        return ToolResponse.success()
            .addTextContent(result)
            .build();
    }).subscribeOn(Schedulers.boundedElastic());
});

// 为流式结果返回 Flux
server.addResourceListHandler(() -> {
    return Flux.fromIterable(getResources())
        .map(r -> Resource.builder()
            .uri(r.getUri())
            .name(r.getName())
            .build())
        .collectList();
});
```

## 同步门面

对于阻塞用例，使用同步 API：

```java
import io.mcp.server.McpSyncServer;

McpSyncServer syncServer = server.toSyncServer();

// 阻塞工具处理器
syncServer.addToolHandler("greet", (args) -> {
    String name = args.get("name").asText();
    return ToolResponse.success()
        .addTextContent("你好, " + name + "!")
        .build();
});
```

## 传输配置

### Stdio 传输

对于本地子进程通信：

```java
import io.mcp.server.transport.StdioServerTransport;

StdioServerTransport transport = new StdioServerTransport();
server.start(transport).block();
```

### HTTP 传输（Servlet）

对于基于 HTTP 的服务器：

```java
import io.mcp.server.transport.ServletServerTransport;
import jakarta.servlet.http.HttpServlet;

public class McpServlet extends HttpServlet {
    private final McpServer server;
    private final ServletServerTransport transport;

    public McpServlet() {
        this.server = createMcpServer();
        this.transport = new ServletServerTransport();
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) {
        transport.handleRequest(server, req, resp).block();
    }
}
```

## Spring Boot 集成

使用 Spring Boot starter 进行无缝集成：

```xml
<dependency>
    <groupId>io.modelcontextprotocol.sdk</groupId>
    <artifactId>mcp-spring-boot-starter</artifactId>
    <version>0.14.1</version>
</dependency>
```

使用 Spring 配置服务器：

```java
import org.springframework.context.annotation.Configuration;
import io.mcp.spring.McpServerConfigurer;

@Configuration
public class McpConfiguration {

    @Bean
    public McpServerConfigurer mcpServerConfigurer() {
        return server -> server
            .serverInfo("spring-server", "1.0.0")
            .capabilities(cap -> cap
                .tools(true)
                .resources(true)
                .prompts(true));
    }
}
```

将处理器注册为 Spring bean：

```java
import org.springframework.stereotype.Component;
import io.mcp.spring.ToolHandler;

@Component
public class SearchToolHandler implements ToolHandler {

    @Override
    public String getName() {
        return "search";
    }

    @Override
    public Tool getTool() {
        return Tool.builder()
            .name("search")
            .description("搜索信息")
            .inputSchema(JsonSchema.object()
                .property("query", JsonSchema.string().required(true)))
            .build();
    }

    @Override
    public Mono<ToolResponse> handle(JsonNode arguments) {
        String query = arguments.get("query").asText();
        return Mono.just(ToolResponse.success()
            .addTextContent("搜索结果: " + query)
            .build());
    }
}
```

## 错误处理

使用 MCP 异常进行适当的错误处理：

```java
server.addToolHandler("risky", (args) -> {
    return Mono.fromCallable(() -> {
        try {
            String result = riskyOperation(args);
            return ToolResponse.success()
                .addTextContent(result)
                .build();
        } catch (ValidationException e) {
            return ToolResponse.error()
                .message("无效输入: " + e.getMessage())
                .build();
        } catch (Exception e) {
            log.error("意外错误", e);
            return ToolResponse.error()
                .message("发生内部错误")
                .build();
        }
    });
});
```

## JSON 模式构建

使用流畅的模式构建器：

```java
import io.mcp.json.JsonSchema;

JsonSchema schema = JsonSchema.object()
    .property("name", JsonSchema.string()
        .description("用户名")
        .minLength(1)
        .maxLength(100)
        .required(true))
    .property("age", JsonSchema.integer()
        .description("用户年龄")
        .minimum(0)
        .maximum(150))
    .property("email", JsonSchema.string()
        .description("电子邮件地址")
        .format("email")
        .required(true))
    .property("tags", JsonSchema.array()
        .items(JsonSchema.string())
        .uniqueItems(true))
    .additionalProperties(false)
    .build();
```

## 日志记录和可观察性

使用 SLF4J 进行日志记录：

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

private static final Logger log = LoggerFactory.getLogger(MyMcpServer.class);

server.addToolHandler("process", (args) -> {
    log.info("工具调用: process, 参数: {}", args);

    return Mono.fromCallable(() -> {
        String result = process(args);
        log.debug("处理成功完成");
        return ToolResponse.success()
            .addTextContent(result)
            .build();
    }).doOnError(error -> {
        log.error("处理失败", error);
    });
});
```

使用 Reactor 传播上下文：

```java
import reactor.util.context.Context;

server.addToolHandler("traced", (args) -> {
    return Mono.deferContextual(ctx -> {
        String traceId = ctx.get("traceId");
        log.info("使用 traceId 处理: {}", traceId);

        return Mono.just(ToolResponse.success()
            .addTextContent("已处理")
            .build());
    });
});
```

## 测试

使用同步 API 编写测试：

```java
import org.junit.jupiter.api.Test;
import static org.assertj.core.api.Assertions.assertThat;

class McpServerTest {

    @Test
    void testToolHandler() {
        McpServer server = createTestServer();
        McpSyncServer syncServer = server.toSyncServer();

        JsonNode args = objectMapper.createObjectNode()
            .put("query", "test");

        ToolResponse response = syncServer.callTool("search", args);

        assertThat(response.isError()).isFalse();
        assertThat(response.getContent()).hasSize(1);
    }
}
```

## Jackson 集成

SDK 使用 Jackson 进行 JSON 序列化。根据需要自定义：

```java
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;

ObjectMapper mapper = new ObjectMapper();
mapper.registerModule(new JavaTimeModule());

// 使用自定义映射器和服务器
McpServer server = McpServerBuilder.builder()
    .objectMapper(mapper)
    .build();
```

## 内容类型

在响应中支持多种内容类型：

```java
import io.mcp.server.content.Content;

server.addToolHandler("multi", (args) -> {
    return Mono.just(ToolResponse.success()
        .addTextContent("纯文本响应")
        .addImageContent(imageBytes, "image/png")
        .addResourceContent("resource://data", "application/json", jsonData)
        .build());
});
```

## 服务器生命周期

正确管理服务器生命周期：

```java
import reactor.core.Disposable;

Disposable serverDisposable = server.start(transport).subscribe();

// 优雅关闭
Runtime.getRuntime().addShutdownHook(new Thread(() -> {
    log.info("正在关闭 MCP 服务器");
    serverDisposable.dispose();
    server.stop().block();
}));
```

## 常见模式

### 请求验证

```java
server.addToolHandler("validate", (args) -> {
    if (!args.has("required_field")) {
        return Mono.just(ToolResponse.error()
            .message("缺少 required_field")
            .build());
    }

    return processRequest(args);
});
```

### 异步操作

```java
server.addToolHandler("async", (args) -> {
    return Mono.fromCallable(() -> callExternalApi(args))
        .timeout(Duration.ofSeconds(30))
        .onErrorResume(TimeoutException.class, e ->
            Mono.just(ToolResponse.error()
                .message("操作超时")
                .build()))
        .subscribeOn(Schedulers.boundedElastic());
});
```

### 资源缓存

```java
private final Map<String, String> cache = new ConcurrentHashMap<>();

server.addResourceReadHandler((uri) -> {
    return Mono.fromCallable(() ->
        cache.computeIfAbsent(uri, this::loadResource))
        .map(content -> ResourceContent.text(content, uri));
});
```

## 最佳实践

1. **对异步操作和背压使用响应式流**
2. **为企业应用程序利用 Spring Boot** starter
3. **实现适当的错误处理**并带有特定错误消息
4. **使用 SLF4J** 进行日志记录，而不是 System.out
5. **在工具和提示处理器中验证输入**
6. **支持优雅关闭**并适当清理资源
7. **对阻塞操作使用有界弹性调度器**
8. **在响应式链中传播上下文**以实现可观察性
9. **为简单起见使用同步 API** 进行测试
10. **遵循 Java 命名约定**（方法使用驼峰命名，类使用帕斯卡命名）