---
applyTo: ['*']
description: "自 Java 17 发布以来采用 Java 21 新特性的综合最佳实践。"
---

# Java 17 到 Java 21 升级指南

这些指令帮助 GitHub Copilot 协助开发人员将 Java 项目从 JDK 17 升级到 JDK 21，重点关注新语言特性、API 更改和最佳实践。

## JDK 18-21 中的主要语言特性

### Switch 的模式匹配（JEP 441 - 21 中标准）

**增强的 Switch 表达式和语句**

处理 switch 构造时：
- 建议在适当的地方将传统 switch 转换为模式匹配
- 使用模式匹配进行类型检查和解构
- 升级模式示例：
```java
// 旧方法（Java 17）
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

// 新方法（Java 21）
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
    case String s when s.length() > 10 -> "长字符串: " + s;
    case String s -> "短字符串: " + s;
    case Integer i when i > 100 -> "大数字: " + i;
    case Integer i -> "小数字: " + i;
    default -> "其他";
}
```

### 记录模式（JEP 440 - 21 中标准）

**模式匹配中的解构记录**

处理记录时：
- 建议使用记录模式进行解构
- 与 switch 表达式结合以实现强大的数据处理
- 使用示例：
```java
public record Point(int x, int y) {}
public record ColoredPoint(Point point, Color color) {}

// Switch 中的解构
public String describe(Object obj) {
    return switch (obj) {
        case Point(var x, var y) -> "位于 (" + x + ", " + y + ") 的点";
        case ColoredPoint(Point(var x, var y), var color) ->
            "位于 (" + x + ", " + y + ") 的着色点，颜色为 " + color;
        default -> "未知形状";
    };
}
```

- 在复杂模式匹配中使用：
```java
// 嵌套记录模式
switch (shape) {
    case Rectangle(ColoredPoint(Point(var x1, var y1), var c1),
                   ColoredPoint(Point(var x2, var y2), var c2))
        when c1 == c2 -> "单色矩形";
    case Rectangle r -> "多色矩形";
}
```

### 虚拟线程（JEP 444 - 21 中标准）

**轻量级并发**

处理并发时：
- 建议为高吞吐量并发应用使用虚拟线程
- 使用 `Thread.ofVirtual()` 创建虚拟线程
- 迁移模式示例：
```java
// 旧平台线程方法
ExecutorService executor = Executors.newFixedThreadPool(100);
executor.submit(() -> {
    // 阻塞 I/O 操作
    httpClient.send(request);
});

// 新虚拟线程方法
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    executor.submit(() -> {
        // 阻塞 I/O 操作 - 现在可扩展到数百万
        httpClient.send(request);
    });
}
```

- 使用结构化并发模式：
```java
// 结构化并发（预览）
try (var scope = new StructuredTaskScope.ShutdownOnFailure()) {
    Future<String> user = scope.fork(() -> fetchUser(userId));
    Future<String> order = scope.fork(() -> fetchOrder(orderId));

    scope.join();           // 连接所有子任务
    scope.throwIfFailed();  // 传播错误

    return processResults(user.resultNow(), order.resultNow());
}
```

### 字符串模板（JEP 430 - 21 中预览）

**安全的字符串插值**

处理字符串格式化时：
- 建议使用字符串模板进行安全的字符串插值（预览功能）
- 使用 `--enable-preview` 启用预览功能
- 使用示例：
```java
// 传统连接
String message = "你好, " + name + "! 你有 " + count + " 条消息。";

// 字符串模板（预览）
String message = STR."你好, \{name}! 你有 \{count} 条消息。";

// 安全的 HTML 生成
String html = HTML."<p>用户: \{username}</p>";

// 安全的 SQL 查询
PreparedStatement stmt = SQL."SELECT * FROM users WHERE id = \{userId}";
```

### 有序集合（JEP 431 - 21 中标准）

**增强的集合接口**

处理集合时：
- 使用新的 `SequencedCollection`、`SequencedSet`、`SequencedMap` 接口
- 在集合类型间统一访问第一个/最后一个元素
- 使用示例：
```java
// Lists、Deques、LinkedHashSet 等上可用的新方法
List<String> list = List.of("第一个", "中间", "最后一个");
String first = list.getFirst();  // "第一个"
String last = list.getLast();    // "最后一个"
List<String> reversed = list.reversed(); // ["最后一个", "中间", "第一个"]

// 适用于任何 SequencedCollection
SequencedSet<String> set = new LinkedHashSet<>();
set.addFirst("开始");
set.addLast("结束");
String firstElement = set.getFirst();
```

### 未命名模式和变量（JEP 443 - 21 中预览）

**简化的模式匹配**

处理模式匹配时：
- 对不需要的值使用未命名模式 `_`
- 简化 switch 表达式和记录模式
- 使用示例：
```java
// 忽略未使用的变量
switch (ball) {
    case RedBall(_) -> "红球";     // 不关心大小
    case BlueBall(var size) -> "大小为 " + size + " 的蓝球";
}

// 忽略记录的部分
switch (point) {
    case Point(var x, _) -> "X 坐标: " + x; // 忽略 Y
    case ColoredPoint(Point(_, var y), _) -> "Y 坐标: " + y;
}

// 带未命名变量的异常处理
try {
    riskyOperation();
} catch (IOException | SQLException _) {
    // 不需要异常详情
    handleError();
}
```

### 作用域值（JEP 446 - 21 中预览）

**改进的上下文传播**

处理线程本地数据时：
- 考虑将作用域值作为 ThreadLocal 的现代替代方案
- 为虚拟线程提供更好的性能和更清晰的语义
- 使用示例：
```java
// 定义作用域值
private static final ScopedValue<String> USER_ID = ScopedValue.newInstance();

// 设置和使用作用域值
ScopedValue.where(USER_ID, "user123")
    .run(() -> {
        processRequest(); // 可以在调用链的任何地方访问 USER_ID.get()
    });

// 在嵌套方法中
public void processRequest() {
    String userId = USER_ID.get(); // "user123"
    // 使用用户上下文处理
}
```

## API 增强和新特性

### 默认 UTF-8（JEP 400 - 18 中标准）

处理文件 I/O 时：
- UTF-8 现在是所有平台上的默认字符集
- 在预期使用 UTF-8 的地方移除显式字符集规范
- 简化示例：
```java
// 旧的显式 UTF-8 规范
Files.readString(path, StandardCharsets.UTF_8);
Files.writeString(path, content, StandardCharsets.UTF_8);

// 新的默认行为（Java 18+）
Files.readString(path);  // 默认使用 UTF-8
Files.writeString(path, content);  // 默认使用 UTF-8
```

### 简单 Web 服务器（JEP 408 - 18 中标准）

需要基本 HTTP 服务器时：
- 使用内置的 `jwebserver` 命令或 `com.sun.net.httpserver` 增强
- 非常适合测试和开发
- 使用示例：
```java
// 命令行
$ jwebserver -p 8080 -d /path/to/files

// 编程使用
HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);
server.createContext("/", new SimpleFileHandler(Path.of("/tmp")));
server.start();
```

### Internet 地址解析 SPI（JEP 418 - 19 中标准）

处理自定义 DNS 解析时：
- 实现 `InetAddressResolverProvider` 进行自定义地址解析
- 对服务发现和测试场景很有用

### 密钥封装机制 API（JEP 452 - 21 中标准）

处理后量子密码学时：
- 使用 KEM API 进行密钥封装机制
- 使用示例：
```java
KeyPairGenerator kpg = KeyPairGenerator.getInstance("ML-KEM");
KeyPair kp = kpg.generateKeyPair();

KEM kem = KEM.getInstance("ML-KEM");
KEM.Encapsulator encapsulator = kem.newEncapsulator(kp.getPublic());
KEM.Encapsulated encapsulated = encapsulator.encapsulate();
```

## 弃用和警告

### 终结弃用（JEP 421 - 18 中弃用）

遇到 `finalize()` 方法时：
- 移除 finalize 方法并使用替代方案
- 建议使用 Cleaner API 或 try-with-resources
- 迁移示例：
```java
// 已弃用的 finalize 方法
@Override
protected void finalize() throws Throwable {
    cleanup();
}

// 使用 Cleaner 的现代方法
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

### 动态代理加载（JEP 451 - 21 中警告）

处理代理或检测时：
- 如果需要，添加 `-XX:+EnableDynamicAgentLoading` 来抑制警告
- 考虑在启动时加载代理而不是动态加载
- 更新工具以使用启动代理加载

## 构建配置更新

### 预览功能

对于使用预览功能的项目：
- 向编译器和运行时添加 `--enable-preview`
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

- Gradle 配置：
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
-Djdk.virtualThreadScheduler.parallelism=N  # 设置承载线程数
-Djdk.virtualThreadScheduler.maxPoolSize=N  # 设置最大池大小
```

## 运行时和 GC 改进

### 分代 ZGC（JEP 439 - 21 中可用）

配置垃圾收集时：
- 尝试分代 ZGC 以获得更好的性能
- 使用以下方式启用：`-XX:+UseZGC -XX:+ZGenerational`
- 监控分配模式和 GC 行为

## 迁移策略

### 逐步升级过程

1. **更新构建工具**：确保 Maven/Gradle 支持 JDK 21
2. **语言特性采用**：
   - 从 switch 的模式匹配开始（标准）
   - 在有益的地方添加记录模式
   - 考虑为 I/O 密集型应用使用虚拟线程
3. **预览功能**：仅在特定用例需要时启用
4. **测试**：全面测试，特别是并发更改
5. **性能**：使用新的 GC 选项进行基准测试

### 代码审查检查清单

审查 Java 21 升级代码时：
- [ ] 将适当的 instanceof 链转换为 switch 表达式
- [ ] 使用记录模式进行数据解构
- [ ] 在适当的地方将 ThreadLocal 替换为 ScopedValues
- [ ] 考虑为高并发场景使用虚拟线程
- [ ] 移除显式 UTF-8 字符集规范
- [ ] 将 finalize() 方法替换为 Cleaner 或 try-with-resources
- [ ] 对第一个/最后一个访问模式使用 SequencedCollection 方法
- [ ] 仅对使用的预览功能添加预览标志

### 常见迁移模式

1. **Switch 增强**：
   ```java
   // 从 instanceof 链到 switch 表达式
   if (obj instanceof String s) return processString(s);
   else if (obj instanceof Integer i) return processInt(i);
   // 变为：
   return switch (obj) {
       case String s -> processString(s);
       case Integer i -> processInt(i);
       default -> processDefault(obj);
   };
   ```

2. **虚拟线程采用**：
   ```java
   // 从平台线程到虚拟线程
   Executors.newFixedThreadPool(200)
   // 变为：
   Executors.newVirtualThreadPerTaskExecutor()
   ```

3. **记录模式使用**：
   ```java
   // 从手动解构到记录模式
   if (point instanceof Point p) {
       int x = p.x();
       int y = p.y();
   }
   // 变为：
   if (point instanceof Point(var x, var y)) {
       // 直接使用 x 和 y
   }
   ```

## 性能考虑

- 虚拟线程在阻塞 I/O 方面表现出色，但可能不会使 CPU 密集型任务受益
- 分代 ZGC 可以减少大多数应用程序的 GC 开销
- Switch 中的模式匹配通常比 instanceof 链更高效
- SequencedCollection 方法提供对第一个/最后一个元素的 O(1) 访问
- 对于虚拟线程，作用域值的开销比 ThreadLocal 更低

## 测试建议

- 在高并发下测试虚拟线程应用程序
- 验证模式匹配涵盖所有预期情况
- 对分代 ZGC 与其他收集器进行性能测试
- 验证跨不同平台的 UTF-8 默认行为
- 在生产使用前彻底测试预览功能

请记住，仅在明确需要时启用预览功能，并在部署到生产环境之前在暂存环境中进行彻底测试。