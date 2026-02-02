---
applyTo: ['*']
description: "Comprehensive best practices for adopting new Java 21 features since the release of Java 17."
---

# Java 17 到 Java 21 升级指南

这些说明可帮助 GitHub Copilot 协助开发人员将 Java 项目从 JDK 17 升级到 JDK 21，重点关注新的语言功能、API 更改和最佳实践。

## JDK 18-21 中的主要语言特性

### 开关的模式匹配（JEP 441 - 21 中的标准）

**增强的 switch 表达式和语句**

使用 switch 结构时：
- 建议在适当的情况下将传统开关转换为模式匹配
- 使用模式匹配进行类型检查和解构
- 升级模式示例：
```java
// Old approach (Java 17)
public String processObject(Object obj) {
    if (obj instanceof String) {
        String s = (String) obj;
        return s.toUpperCase();
    } else if (obj instanceof Integer) {
        Integer i = (Integer) obj;
        return i.toString();
    }
    return "unknown";
}

// New approach (Java 21)
public String processObject(Object obj) {
    return switch (obj) {
        case String s -> s.toUpperCase();
        case Integer i -> i.toString();
        case null -> "null";
        default -> "unknown";
    };
}
```

- 支持保护模式：
```java
switch (obj) {
    case String s when s.length() > 10 -> "Long string: " + s;
    case String s -> "Short string: " + s;
    case Integer i when i > 100 -> "Large number: " + i;
    case Integer i -> "Small number: " + i;
    default -> "Other";
}
```

### 记录模式（JEP 440 - 21 中的标准）

**模式匹配中的解构记录**

处理记录时：
- 建议使用记录模式进行解构
- 结合 switch 表达式进行强大的数据处理
- 用法示例：
```java
public record Point(int x, int y) {}
public record ColoredPoint(Point point, Color color) {}

// Destructuring in switch
public String describe(Object obj) {
    return switch (obj) {
        case Point(var x, var y) -> "Point at (" + x + ", " + y + ")";
        case ColoredPoint(Point(var x, var y), var color) -> 
            "Colored point at (" + x + ", " + y + ") in " + color;
        default -> "Unknown shape";
    };
}
```

- 用于复杂模式匹配：
```java
// Nested record patterns
switch (shape) {
    case Rectangle(ColoredPoint(Point(var x1, var y1), var c1), 
                   ColoredPoint(Point(var x2, var y2), var c2)) 
        when c1 == c2 -> "Monochrome rectangle";
    case Rectangle r -> "Multi-colored rectangle";
}
```

### 虚拟线程（JEP 444 - 21 中的标准）

**轻量级并发**

使用并发时：
- 为高吞吐量、并发应用程序建议虚拟线程
- 使用 `Thread.ofVirtual()` 创建虚拟线程
- 迁移模式示例：
```java
// Old platform thread approach
ExecutorService executor = Executors.newFixedThreadPool(100);
executor.submit(() -> {
    // blocking I/O operation
    httpClient.send(request);
});

// New virtual thread approach
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    executor.submit(() -> {
        // blocking I/O operation - now scales to millions
        httpClient.send(request);
    });
}
```

- 使用结构化并发模式：
```java
// Structured concurrency (Preview)
try (var scope = new StructuredTaskScope.ShutdownOnFailure()) {
    Future<String> user = scope.fork(() -> fetchUser(userId));
    Future<String> order = scope.fork(() -> fetchOrder(orderId));
    
    scope.join();           // Join all subtasks
    scope.throwIfFailed();  // Propagate errors
    
    return processResults(user.resultNow(), order.resultNow());
}
```

### 字符串模板（JEP 430 - 21 中预览）

**安全字符串插值**

使用字符串格式时：
- 建议用于安全字符串插值的字符串模板（预览功能）
- 使用 `--enable-preview` 启用预览功能
- 用法示例：
```java
// Traditional concatenation
String message = "Hello, " + name + "! You have " + count + " messages.";

// String Templates (Preview)
String message = STR."Hello, \{name}! You have \{count} messages.";

// Safe HTML generation
String html = HTML."<p>User: \{username}</p>";

// Safe SQL queries  
PreparedStatement stmt = SQL."SELECT * FROM users WHERE id = \{userId}";
```

### 排序集合（JEP 431 - 21 中的标准）

**增强的收集接口**

使用集合时：
- 使用新的 `SequencedCollection`、`SequencedSet`、`SequencedMap` 接口
- 跨集合类型统一访问第一个/最后一个元素
- 用法示例：
```java
// New methods available on Lists, Deques, LinkedHashSet, etc.
List<String> list = List.of("first", "middle", "last");
String first = list.getFirst();  // "first"
String last = list.getLast();    // "last"
List<String> reversed = list.reversed(); // ["last", "middle", "first"]

// Works with any SequencedCollection
SequencedSet<String> set = new LinkedHashSet<>();
set.addFirst("start");
set.addLast("end");
String firstElement = set.getFirst();
```

### 未命名模式和变量（JEP 443 - 21 中的预览）

**简化的模式匹配**

使用模式匹配时：
- 对不需要的值使用未命名模式 `_`
- 简化 switch 表达式并记录模式
- 用法示例：
```java
// Ignore unused variables
switch (ball) {
    case RedBall(_) -> "Red ball";     // Don't care about size
    case BlueBall(var size) -> "Blue ball size " + size;
}

// Ignore parts of records
switch (point) {
    case Point(var x, _) -> "X coordinate: " + x; // Ignore Y
    case ColoredPoint(Point(_, var y), _) -> "Y coordinate: " + y;
}

// Exception handling with unnamed variables
try {
    riskyOperation();
} catch (IOException | SQLException _) {
    // Don't need exception details
    handleError();
}
```

### 范围值（JEP 446 - 21 中的预览）

**改进的上下文传播**

使用线程本地数据时：
- 将范围值视为 ThreadLocal 的现代替代方案
- 虚拟线程更好的性能和更清晰的语义
- 用法示例：
```java
// Define scoped value
private static final ScopedValue<String> USER_ID = ScopedValue.newInstance();

// Set and use scoped value
ScopedValue.where(USER_ID, "user123")
    .run(() -> {
        processRequest(); // Can access USER_ID.get() anywhere in call chain
    });

// In nested method
public void processRequest() {
    String userId = USER_ID.get(); // "user123"
    // Process with user context
}
```

## API 增强和新功能

### 默认 UTF-8（JEP 400 - 18 中的标准）

使用文件 I/O 时：
- UTF-8 现在是所有平台上的默认字符集
- 删除预期使用 UTF-8 的显式字符集规范
- 简化示例：
```java
// Old explicit UTF-8 specification
Files.readString(path, StandardCharsets.UTF_8);
Files.writeString(path, content, StandardCharsets.UTF_8);

// New default behavior (Java 18+)
Files.readString(path);  // Uses UTF-8 by default
Files.writeString(path, content);  // Uses UTF-8 by default
```

### 简单 Web 服务器（JEP 408 - 18 中的标准）

当需要基本的HTTP服务器时：
- 使用内置 `jwebserver` 命令或 `com.sun.net.httpserver` 增强功能
- 非常适合测试和开发
- 用法示例：
```java
// Command line
$ jwebserver -p 8080 -d /path/to/files

// Programmatic usage
HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);
server.createContext("/", new SimpleFileHandler(Path.of("/tmp")));
server.start();
```

### 互联网地址解析 SPI（JEP 418 - 19 中的标准）

使用自定义 DNS 解析时：
- 实现 `InetAddressResolverProvider` 进行自定义地址解析
- 对于服务发现和测试场景很有用

### 密钥封装机制 API（JEP 452 - 21 中的标准）

使用后量子密码学时：
- 使用KEM API进行密钥封装机制
- 用法示例：
```java
KeyPairGenerator kpg = KeyPairGenerator.getInstance("ML-KEM");
KeyPair kp = kpg.generateKeyPair();

KEM kem = KEM.getInstance("ML-KEM");
KEM.Encapsulator encapsulator = kem.newEncapsulator(kp.getPublic());
KEM.Encapsulated encapsulated = encapsulator.encapsulate();
```

## 弃用和警告

### 最终弃用（JEP 421 - 18 中弃用）

当遇到 `finalize()` 方法时：
- 删除 Finalize 方法并使用替代方法
- 建议 Cleaner API 或 try-with-resources
- 迁移示例：
```java
// Deprecated finalize approach
@Override
protected void finalize() throws Throwable {
    cleanup();
}

// Modern approach with Cleaner
private static final Cleaner CLEANER = Cleaner.create();

public MyResource() {
    cleaner.register(this, new CleanupTask(nativeResource));
}

private static class CleanupTask implements Runnable {
    private final long nativeResource;
    
    CleanupTask(long nativeResource) {
        this.nativeResource = nativeResource;
    }
    
    public void run() {
        cleanup(nativeResource);
    }
}
```

### 动态代理加载（JEP 451 - 21 中的警告）

使用代理或仪器时：
- 如果需要，添加 `-XX:+EnableDynamicAgentLoading` 以抑制警告
- 考虑在启动时加载代理而不是动态加载
- 更新工具以使用启动代理加载

## 构建配置更新

### 预览功能

对于使用预览功能的项目：
- 将 `--enable-preview` 添加到编译器和运行时
- Maven 配置：
```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <configuration>
        <release>21</release>
        <compilerArgs>
            <arg>--enable-preview</arg>
        </compilerArgs>
    </configuration>
</plugin>

<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <configuration>
        <argLine>--enable-preview</argLine>
    </configuration>
</plugin>
```

- 梯度配置：
```kotlin
java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(21)
    }
}

tasks.withType<JavaCompile> {
    options.compilerArgs.add("--enable-preview")
}

tasks.withType<Test> {
    jvmArgs("--enable-preview")
}
```

### 虚拟线程配置

对于使用虚拟线程的应用程序：
- 不需要特殊的 JVM 标志（21 中的标准功能）
- 考虑这些系统属性进行调试：
```bash
-Djdk.virtualThreadScheduler.parallelism=N  # Set carrier thread count
-Djdk.virtualThreadScheduler.maxPoolSize=N  # Set max pool size
```

## 运行时和 GC 改进

### 世代 ZGC（JEP 439 - 提供 21 种版本）

配置垃圾收集时：
- 尝试 Generational ZGC 以获得更好的性能
- 启用：`-XX:+UseZGC -XX:+ZGenerational`
- 监控分配模式和 GC 行为

## 迁移策略

### 逐步升级过程

1. **更新构建工具**：确保 Maven/Gradle 支持 JDK 21
2. **语言功能采用**： 
   - 从 switch 的模式匹配开始（标准）
   - 在有益的地方添加记录模式
   - 考虑为 I/O 密集型应用程序使用虚拟线程
3. **预览功能**：仅在特定用例需要时启用
4. **测试**：特别针对并发更改的全面测试
5. **性能**：使用新 GC 选项进行基准测试

### 代码审查清单

在检查 Java 21 升级代码时：
- [ ] 将适当的instanceof链转换为switch表达式
- [ ] 使用记录模式进行数据解构
- [ ] 在适当的情况下将 ThreadLocal 替换为 ScopedValues
- [ ] 高并发场景考虑虚拟线程
- [ ] 删除显式的 UTF-8 字符集规范
- [ ] 将 Finalize() 方法替换为 Cleaner 或 try-with-resources
- [ ] 对第一个/最后一个访问模式使用 SequencedCollection 方法
- [ ] 仅为正在使用的预览功能添加预览标志

### 常见的迁移模式

1. **开关增强**：
   ```java
   // From instanceof chains to switch expressions
   if (obj instanceof String s) return processString(s);
   else if (obj instanceof Integer i) return processInt(i);
   // becomes:
   return switch (obj) {
       case String s -> processString(s);
       case Integer i -> processInt(i);
       default -> processDefault(obj);
   };
   ```

2. **虚拟线程采用**：
   ```java
   // From platform threads to virtual threads
   Executors.newFixedThreadPool(200)
   // becomes:
   Executors.newVirtualThreadPerTaskExecutor()
   ```

3. **记录模式用法**：
   ```java
   // From manual destructuring to record patterns
   if (point instanceof Point p) {
       int x = p.x();
       int y = p.y();
   }
   // becomes:
   if (point instanceof Point(var x, var y)) {
       // use x and y directly
   }
   ```

## 性能考虑因素

- 虚拟线程在阻塞 I/O 方面表现出色，但可能无法使 CPU 密集型任务受益
- 分代 ZGC 可以减少大多数应用程序的 GC 开销
- switch 中的模式匹配通常比 instanceof 链更有效
- SequencedCollection 方法提供对第一个/最后一个元素的 O(1) 访问
- 对于虚拟线程来说，作用域值的开销比 ThreadLocal 低

## 测试建议

- 高并发下测试虚拟线程应用
- 验证模式匹配涵盖所有预期情况
- 世代 ZGC 与其他收集器的性能测试
- 验证跨不同平台的 UTF-8 默认行为
- 在生产使用之前彻底测试预览功能

请记住，仅在特别需要时才启用预览功能，并在部署到生产之前在临时环境中进行彻底测试。
