---
mode: agent
description: '使用官方io.modelcontextprotocol:kotlin-sdk库生成完整的Kotlin MCP服务器项目，包含正确的结构、依赖和实现。'
---

# Kotlin MCP服务器项目生成器

生成一个完整的、生产就绪的Kotlin模型上下文协议（MCP）服务器项目。

## 项目要求

您将创建一个Kotlin MCP服务器，包含：

1. **项目结构**：基于Gradle的Kotlin项目布局
2. **依赖**：官方MCP SDK、Ktor和kotlinx库
3. **服务器设置**：配置了传输的MCP服务器
4. **工具**：至少2-3个具有类型化输入/输出的有用工具
5. **错误处理**：正确的异常处理和验证
6. **文档**：包含设置和使用说明的README
7. **测试**：具有协程的基本测试结构

## 模板结构

```
myserver/
├── build.gradle.kts
├── settings.gradle.kts
├── gradle.properties
├── src/
│   ├── main/
│   │   └── kotlin/
│   │       └── com/example/myserver/
│   │           ├── Main.kt
│   │           ├── Server.kt
│   │           ├── config/
│   │           │   └── Config.kt
│   │           └── tools/
│   │               ├── Tool1.kt
│   │               └── Tool2.kt
│   └── test/
│       └── kotlin/
│           └── com/example/myserver/
│               └── ServerTest.kt
└── README.md
```

## build.gradle.kts模板

```kotlin
plugins {
    kotlin("jvm") version "2.1.0"
    kotlin("plugin.serialization") version "2.1.0"
    application
}

group = "com.example"
version = "1.0.0"

repositories {
    mavenCentral()
}

dependencies {
    implementation("io.modelcontextprotocol:kotlin-sdk:0.7.2")

    // 用于传输的Ktor
    implementation("io.ktor:ktor-server-netty:3.0.0")
    implementation("io.ktor:ktor-client-cio:3.0.0")

    // 序列化
    implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.7.3")

    // 协程
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.9.0")

    // 日志记录
    implementation("io.github.oshai:kotlin-logging-jvm:7.0.0")
    implementation("ch.qos.logback:logback-classic:1.5.12")

    // 测试
    testImplementation(kotlin("test"))
    testImplementation("org.jetbrains.kotlinx:kotlinx-coroutines-test:1.9.0")
}

application {
    mainClass.set("com.example.myserver.MainKt")
}

tasks.test {
    useJUnitPlatform()
}

kotlin {
    jvmToolchain(17)
}
```

## settings.gradle.kts模板

```kotlin
rootProject.name = "{{PROJECT_NAME}}"
```

## Main.kt模板

```kotlin
package com.example.myserver

import io.modelcontextprotocol.kotlin.sdk.server.StdioServerTransport
import kotlinx.coroutines.runBlocking
import io.github.oshai.kotlinlogging.KotlinLogging

private val logger = KotlinLogging.logger {}

fun main() = runBlocking {
    logger.info { "Starting MCP server..." }

    val config = loadConfig()
    val server = createServer(config)

    // 使用stdio传输
    val transport = StdioServerTransport()

    logger.info { "Server '${config.name}' v${config.version} ready" }
    server.connect(transport)
}
```

## Server.kt模板

```kotlin
package com.example.myserver

import io.modelcontextprotocol.kotlin.sdk.server.Server
import io.modelcontextprotocol.kotlin.sdk.server.ServerOptions
import io.modelcontextprotocol.kotlin.sdk.Implementation
import io.modelcontextprotocol.kotlin.sdk.ServerCapabilities
import com.example.myserver.tools.registerTools

fun createServer(config: Config): Server {
    val server = Server(
        serverInfo = Implementation(
            name = config.name,
            version = config.version
        ),
        options = ServerOptions(
            capabilities = ServerCapabilities(
                tools = ServerCapabilities.Tools(),
                resources = ServerCapabilities.Resources(
                    subscribe = true,
                    listChanged = true
                ),
                prompts = ServerCapabilities.Prompts(listChanged = true)
            )
        )
    ) {
        config.description
    }

    // 注册所有工具
    server.registerTools()

    return server
}
```

## Config.kt模板

```kotlin
package com.example.myserver.config

import kotlinx.serialization.Serializable

@Serializable
data class Config(
    val name: String = "{{PROJECT_NAME}}",
    val version: String = "1.0.0",
    val description: String = "{{PROJECT_DESCRIPTION}}"
)

fun loadConfig(): Config {
    return Config(
        name = System.getenv("SERVER_NAME") ?: "{{PROJECT_NAME}}",
        version = System.getenv("VERSION") ?: "1.0.0",
        description = System.getenv("DESCRIPTION") ?: "{{PROJECT_DESCRIPTION}}"
    )
}
```

## Tool1.kt模板

```kotlin
package com.example.myserver.tools

import io.modelcontextprotocol.kotlin.sdk.server.Server
import io.modelcontextprotocol.kotlin.sdk.CallToolRequest
import io.modelcontextprotocol.kotlin.sdk.CallToolResult
import io.modelcontextprotocol.kotlin.sdk.TextContent
import kotlinx.serialization.json.buildJsonObject
import kotlinx.serialization.json.put
import kotlinx.serialization.json.putJsonObject
import kotlinx.serialization.json.putJsonArray

fun Server.registerTool1() {
    addTool(
        name = "tool1",
        description = "Description of what tool1 does",
        inputSchema = buildJsonObject {
            put("type", "object")
            putJsonObject("properties") {
                putJsonObject("param1") {
                    put("type", "string")
                    put("description", "First parameter")
                }
                putJsonObject("param2") {
                    put("type", "integer")
                    put("description", "Optional second parameter")
                }
            }
            putJsonArray("required") {
                add("param1")
            }
        }
    ) { request: CallToolRequest ->
        // 提取和验证参数
        val param1 = request.params.arguments["param1"] as? String
            ?: throw IllegalArgumentException("param1 is required")
        val param2 = (request.params.arguments["param2"] as? Number)?.toInt() ?: 0

        // 执行工具逻辑
        val result = performTool1Logic(param1, param2)

        CallToolResult(
            content = listOf(
                TextContent(text = result)
            )
        )
    }
}

private fun performTool1Logic(param1: String, param2: Int): String {
    // 在此处实现工具逻辑
    return "Processed: $param1 with value $param2"
}
```

## tools/ToolRegistry.kt模板

```kotlin
package com.example.myserver.tools

import io.modelcontextprotocol.kotlin.sdk.server.Server

fun Server.registerTools() {
    registerTool1()
    registerTool2()
    // 在此处注册其他工具
}
```

## ServerTest.kt模板

```kotlin
package com.example.myserver

import kotlinx.coroutines.test.runTest
import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertFalse

class ServerTest {

    @Test
    fun `test server creation`() = runTest {
        val config = Config(
            name = "test-server",
            version = "1.0.0",
            description = "Test server"
        )

        val server = createServer(config)

        assertEquals("test-server", server.serverInfo.name)
        assertEquals("1.0.0", server.serverInfo.version)
    }

    @Test
    fun `test tool1 execution`() = runTest {
        val config = Config()
        val server = createServer(config)

        // 测试工具执行
        // 注意：您需要实现适当的测试实用程序
        // 用于在服务器中调用工具
    }
}
```

## README.md模板

```markdown
# {{PROJECT_NAME}}

使用Kotlin构建的模型上下文协议（MCP）服务器。

## 描述

{{PROJECT_DESCRIPTION}}

## 系统要求

- Java 17或更高版本
- Kotlin 2.1.0

## 安装

构建项目：

\`\`\`bash
./gradlew build
\`\`\`

## 使用

使用stdio传输运行服务器：

\`\`\`bash
./gradlew run
\`\`\`

或构建并运行jar：

\`\`\`bash
./gradlew installDist
./build/install/{{PROJECT_NAME}}/bin/{{PROJECT_NAME}}
\`\`\`

## 配置

通过环境变量配置：

- `SERVER_NAME`：服务器名称（默认："{{PROJECT_NAME}}"）
- `VERSION`：服务器版本（默认："1.0.0"）
- `DESCRIPTION`：服务器描述

## 可用工具

### tool1
{{TOOL1_DESCRIPTION}}

**输入：**
- `param1`（字符串，必需）：第一个参数
- `param2`（整数，可选）：第二个参数

**输出：**
- 操作的文本结果

## 开发

运行测试：

\`\`\`bash
./gradlew test
\`\`\`

构建：

\`\`\`bash
./gradlew build
\`\`\`

以自动重新加载运行（开发）：

\`\`\`bash
./gradlew run --continuous
\`\`\`

## 多平台

此项目使用Kotlin多平台，可以针对JVM、Wasm和iOS。
参见`build.gradle.kts`了解平台配置。

## 许可证

MIT
```

## 生成指令

生成Kotlin MCP服务器时：

1. **Gradle设置**：创建具有所有依赖的正确`build.gradle.kts`
2. **包结构**：遵循Kotlin包约定
3. **类型安全**：使用数据类和kotlinx.serialization
4. **协程**：所有操作都应该是挂起函数
5. **错误处理**：使用Kotlin异常和验证
6. **JSON模式**：使用`buildJsonObject`进行工具模式
7. **测试**：包含协程测试实用程序
8. **日志记录**：使用kotlin-logging进行结构化日志记录
9. **配置**：使用数据类和环境变量
10. **文档**：为公共API使用KDoc注释

## 最佳实践

- 对所有异步操作使用挂起函数
- 利用Kotlin的空安全和类型系统
- 对结构化数据使用数据类
- 应用kotlinx.serialization进行JSON处理
- 对结果类型使用密封类
- 使用Result/Either模式实现正确的错误处理
- 使用kotlinx-coroutines-test编写测试
- 使用依赖注入提高可测试性
- 遵循Kotlin编码约定
- 使用有意义的名称和KDoc注释

## 传输选项

### Stdio传输
```kotlin
val transport = StdioServerTransport()
server.connect(transport)
```

### SSE传输（Ktor）
```kotlin
embeddedServer(Netty, port = 8080) {
    mcp {
        Server(/*...*/) { "Description" }
    }
}.start(wait = true)
```

## 多平台配置

对于多平台项目，添加到`build.gradle.kts`：

```kotlin
kotlin {
    jvm()
    js(IR) { nodejs() }
    wasmJs()

    sourceSets {
        commonMain.dependencies {
            implementation("io.modelcontextprotocol:kotlin-sdk:0.7.2")
        }
    }
}
```