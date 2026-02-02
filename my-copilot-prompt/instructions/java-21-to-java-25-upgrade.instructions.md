---
applyTo: ['*']
description: "Comprehensive best practices for adopting new Java 25 features since the release of Java 21."
---

# Java 21 到 Java 25 升级指南

这些说明可帮助 GitHub Copilot 协助开发人员将 Java 项目从 JDK 21 升级到 JDK 25，重点关注新的语言功能、API 更改和最佳实践。

## JDK 22-25 中的语言功能和 API 更改

### 模式匹配增强功能（JEP 455/488 - 23 中预览）

**模式、instanceof 和 switch 中的基本类型**

使用模式匹配时：
- 建议在 switch 表达式和 instanceof 检查中使用原始类型模式
- 传统交换机升级示例：
```java
// Old approach (Java 21)
switch (x.getStatus()) {
    case 0 -> "okay";
    case 1 -> "warning"; 
    case 2 -> "error";
    default -> "unknown status: " + x.getStatus();
}

// New approach (Java 25 Preview)
switch (x.getStatus()) {
    case 0 -> "okay";
    case 1 -> "warning";
    case 2 -> "error"; 
    case int i -> "unknown status: " + i;
}
```

- 使用 `--enable-preview` 标志启用预览功能
- 针对更复杂的条件建议防护模式：
```java
switch (x.getYearlyFlights()) {
    case 0 -> ...;
    case int i when i >= 100 -> issueGoldCard();
    case int i -> ... // handle 1-99 range
}
```

### 类文件 API（JEP 466/484 - 23 中的第二次预览，25 中的标准）

**用标准 API 取代 ASM**

当检测字节码操作或类文件处理时：
- 建议从 ASM 库迁移到标准类文件 API
- 使用 `java.lang.classfile` 包代替 `org.objectweb.asm`
- 迁移模式示例：
```java
// Old ASM approach
ClassReader reader = new ClassReader(classBytes);
ClassWriter writer = new ClassWriter(reader, 0);
// ... ASM manipulation

// New Class-File API approach
ClassModel classModel = ClassFile.of().parse(classBytes);
byte[] newBytes = ClassFile.of().transform(classModel, 
    ClassTransform.transformingMethods(methodTransform));
```

### Markdown 文档注释（JEP 467 - 23 中的标准）

**JavaDoc 现代化**

使用 JavaDoc 注释时：
- 建议将 HTML 密集型 JavaDoc 转换为 Markdown 语法
- 使用 `///` 作为 Markdown 文档注释
- 转换示例：
```java
// Old HTML JavaDoc
/**
 * Returns the <b>absolute</b> value of an {@code int} value.
 * <p>
 * If the argument is not negative, return the argument.
 * If the argument is negative, return the negation of the argument.
 * 
 * @param a the argument whose absolute value is to be determined
 * @return the absolute value of the argument
 */

// New Markdown JavaDoc  
/// Returns the **absolute** value of an `int` value.
///
/// If the argument is not negative, return the argument.
/// If the argument is negative, return the negation of the argument.
/// 
/// @param a the argument whose absolute value is to be determined
/// @return the absolute value of the argument
```

### 派生记录创建（JEP 468 - 23 中预览）

**记录增强**

处理记录时：
- 建议使用 `with` 表达式创建派生记录
- 启用派生记录创建的预览功能
- 示例模式：
```java
// Instead of manual record copying
public record Person(String name, int age, String email) {
    public Person withAge(int newAge) {
        return new Person(name, newAge, email);
    }
}

// Use derived record creation (Preview)
Person updated = person with { age = 30; };
```

### Stream Gatherers（JEP 473/485 - 23 中的第二次预览，25 中的标准）

**增强的流处理**

当处理复杂的流操作时：
- 建议使用 `Stream.gather()` 进行自定义中间操作
- 为内置收集器导入 `java.util.stream.Gatherers`
- 用法示例：
```java
// Custom windowing operations
List<List<String>> windows = stream
    .gather(Gatherers.windowSliding(3))
    .toList();

// Custom filtering with state
List<Integer> filtered = numbers.stream()
    .gather(Gatherers.fold(0, (state, element) -> {
        // Custom stateful logic
        return state + element > threshold ? element : null;
    }))
    .filter(Objects::nonNull)
    .toList();
```

## 迁移警告和弃用

### sun.misc.Unsafe 内存访问方法（JEP 471 - 23 中已弃用）

检测 `sun.misc.Unsafe` 使用时：
- 警告已弃用的内存访问方法
- 建议迁移到标准替代方案：
```java
// Deprecated: sun.misc.Unsafe memory access
Unsafe unsafe = Unsafe.getUnsafe();
unsafe.getInt(object, offset);

// Preferred: VarHandle API
VarHandle vh = MethodHandles.lookup()
    .findVarHandle(MyClass.class, "fieldName", int.class);
int value = (int) vh.get(object);

// Or for off-heap: Foreign Function & Memory API
MemorySegment segment = MemorySegment.ofArray(new int[10]);
int value = segment.get(ValueLayout.JAVA_INT, offset);
```

### JNI 使用警告（JEP 472 - 24 中的警告）

检测JNI使用情况时：
- 警告即将到来的 JNI 使用限制
- 建议为使用 JNI 的应用程序添加 `--enable-native-access` 标志
- 建议尽可能迁移到外部函数和内存 API
- 添加 module-info.java 条目以进行本机访问：
```java
module com.example.app {
    requires jdk.unsupported; // for remaining JNI usage
}
```

## 垃圾收集更新

### ZGC 分代模式（JEP 474 - 默认为 23）

配置垃圾收集时：
- 默认 ZGC 现在使用分代模式
- 如果显式使用非分代 ZGC，则更新 JVM 标志：
```bash
# Explicit non-generational mode (will show deprecation warning)
-XX:+UseZGC -XX:-ZGenerational

# Default generational mode
-XX:+UseZGC
```

### G1 改进（JEP 475 - 24 年实施）

使用 G1GC 时：
- 无需更改代码 - 内部 JVM 优化
- 使用 C2 编译器可能会提高编译性能

## Vector API（JEP 469 - 25 个孵化器中的第八个）

进行数值计算时：
- 建议用于 SIMD 操作的 Vector API（仍在孵化中）
- 添加 `--add-modules jdk.incubator.vector`
- 用法示例：
```java
import jdk.incubator.vector.*;

// Traditional scalar computation
for (int i = 0; i < a.length; i++) {
    c[i] = a[i] + b[i];
}

// Vectorized computation
var species = IntVector.SPECIES_PREFERRED;
for (int i = 0; i < a.length; i += species.length()) {
    var va = IntVector.fromArray(species, a, i);
    var vb = IntVector.fromArray(species, b, i);
    var vc = va.add(vb);
    vc.intoArray(c, i);
}
```

## 编译和构建配置

### 预览功能

对于使用预览功能的项目：
- 将 `--enable-preview` 添加到编译器参数
- 将 `--enable-preview` 添加到运行时参数
- Maven 配置：
```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <configuration>
        <release>25</release>
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
        languageVersion = JavaLanguageVersion.of(25)
    }
}

tasks.withType<JavaCompile> {
    options.compilerArgs.add("--enable-preview")
}

tasks.withType<Test> {
    jvmArgs("--enable-preview")
}
```

## 迁移策略

### 逐步升级过程

1. **更新构建工具**：确保 Maven/Gradle 支持 JDK 25
2. **更新依赖项**：检查 JDK 25 兼容性
3. **处理警告**：解决 JEP 471/472 中的弃用警告
4. **启用预览功能**：如果使用模式匹配或其他预览功能
5. **彻底测试**：特别是对于使用 JNI 或 sun.misc.Unsafe 的应用程序
6. **性能测试**：使用新的 ZGC 默认值验证 GC 行为

### 代码审查清单

在检查 Java 25 升级代码时：
- [ ] 用 Class-File API 替换 ASM 使用
- [ ] 将复杂的 HTML JavaDoc 转换为 Markdown
- [ ] 在适用的情况下在 switch 表达式中使用原始模式
- [ ] 将 sun.misc.Unsafe 替换为 VarHandle 或 FFM API
- [ ] 添加 JNI 使用的本机访问权限
- [ ] 使用流收集器进行复杂的流操作
- [ ] 更新预览功能的构建配置

### 测试注意事项

- 使用 `--enable-preview` 标志测试预览功能
- 验证 JNI 应用程序是否可以处理本机访问警告
- 新ZGC生成模式的性能测试
- 使用 Markdown 注释验证 JavaDoc 生成

## 常见陷阱

1. **预览功能依赖关系**：如果没有明确的文档，请勿在库代码中使用预览功能
2. **Native Access**：直接或间接使用 JNI 的应用程序可能需要 `--enable-native-access` 配置
3. **不安全迁移**：不要延迟从 sun.misc.Unsafe 迁移 - 弃用警告表明将来会删除
4. **模式匹配范围**：原始模式适用于所有原始类型，而不仅仅是 int
5. **记录增强**：派生记录创建需要 Java 23 中的预览标志

## 性能考虑因素

- ZGC 分代模式可以提高大多数工作负载的性能
- 类文件 API 减少了 ASM 相关的开销
- 流收集器为复杂的流操作提供更好的性能
- G1GC 改进减少了 JIT 编译开销

请记住，在将 Java 25 升级部署到生产系统之前，要在临时环境中进行彻底测试。
