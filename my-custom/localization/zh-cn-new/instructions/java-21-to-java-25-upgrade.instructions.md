---
applyTo: ['*']
description: "自 Java 21 发布以来采用 Java 25 新特性的综合最佳实践。"
---

# Java 21 到 Java 25 升级指南

这些指令帮助 GitHub Copilot 协助开发人员将 Java 项目从 JDK 21 升级到 JDK 25，重点关注新语言特性、API 更改和最佳实践。

## JDK 22-25 中的语言特性和 API 更改

### 模式匹配增强（JEP 455/488 - 23 中预览）

**模式、instanceof 和 switch 中的原始类型**

处理模式匹配时：
- 建议在 switch 表达式和 instanceof 检查中使用原始类型模式
- 从传统 switch 升级的示例：
```java
// 旧方法（Java 21）
switch (x.getStatus()) {
    case 0 -> "正常";
    case 1 -> "警告";
    case 2 -> "错误";
    default -> "未知状态: " + x.getStatus();
}

// 新方法（Java 25 预览）
switch (x.getStatus()) {
    case 0 -> "正常";
    case 1 -> "警告";
    case 2 -> "错误";
    case int i -> "未知状态: " + i;
}
```

- 使用 `--enable-preview` 标志启用预览功能
- 建议对更复杂的条件使用保护模式：
```java
switch (x.getYearlyFlights()) {
    case 0 -> ...;
    case int i when i >= 100 -> issueGoldCard();
    case int i -> ... // 处理 1-99 范围
}
```

### 类文件 API（JEP 466/484 - 23 中第二次预览，25 中标准）

**用标准 API 替换 ASM**

检测字节码操作或类文件处理时：
- 建议从 ASM 库迁移到标准类文件 API
- 使用 `java.lang.classfile` 包而不是 `org.objectweb.asm`
- 迁移模式示例：
```java
// 旧的 ASM 方法
ClassReader reader = new ClassReader(classBytes);
ClassWriter writer = new ClassWriter(reader, 0);
// ... ASM 操作

// 新的类文件 API 方法
ClassModel classModel = ClassFile.of().parse(classBytes);
byte[] newBytes = ClassFile.of().transform(classModel,
    ClassTransform.transformingMethods(methodTransform));
```

### Markdown 文档注释（JEP 467 - 23 中标准）

**JavaDoc 现代化**

处理 JavaDoc 注释时：
- 建议将 HTML 繁重的 JavaDoc 转换为 Markdown 语法
- 对 Markdown 文档注释使用 `///`
- 转换示例：
```java
// 旧的 HTML JavaDoc
/**
 * 返回 {@code int} 值的<b>绝对</b>值。
 * <p>
 * 如果参数不为负数，返回参数。
 * 如果参数为负数，返回参数的否定。
 *
 * @param a 要确定其绝对值的参数
 * @return 参数的绝对值
 */

// 新的 Markdown JavaDoc
/// 返回 `int` 值的**绝对**值。
///
/// 如果参数不为负数，返回参数。
/// 如果参数为负数，返回参数的否定。
///
/// @param a 要确定其绝对值的参数
/// @return 参数的绝对值
```

### 派生记录创建（JEP 468 - 23 中预览）

**记录增强**

处理记录时：
- 建议使用 `with` 表达式创建派生记录
- 为派生记录创建启用预览功能
- 模式示例：
```java
// 而不是手动记录复制
public record Person(String name, int age, String email) {
    public Person withAge(int newAge) {
        return new Person(name, newAge, email);
    }
}

// 使用派生记录创建（预览）
Person updated = person with { age = 30; };
```

### 流收集器（JEP 473/485 - 23 中第二次预览，25 中标准）

**增强的流处理**

处理复杂流操作时：
- 建议使用 `Stream.gather()` 进行自定义中间操作
- 导入 `java.util.stream.Gatherers` 获取内置收集器
- 使用示例：
```java
// 自定义窗口操作
List<List<String>> windows = stream
    .gather(Gatherers.windowSliding(3))
    .toList();

// 带状态的自定义过滤
List<Integer> filtered = numbers.stream()
    .gather(Gatherers.fold(0, (state, element) -> {
        // 自定义有状态逻辑
        return state + element > threshold ? element : null;
    }))
    .filter(Objects::nonNull)
    .toList();
```

## 迁移警告和弃用

### sun.misc.Unsafe 内存访问方法（JEP 471 - 23 中弃用）

检测 `sun.misc.Unsafe` 使用时：
- 警告已弃用的内存访问方法
- 建议迁移到标准替代方案：
```java
// 已弃用：sun.misc.Unsafe 内存访问
Unsafe unsafe = Unsafe.getUnsafe();
unsafe.getInt(object, offset);

// 首选：VarHandle API
VarHandle vh = MethodHandles.lookup()
    .findVarHandle(MyClass.class, "fieldName", int.class);
int value = (int) vh.get(object);

// 或对于堆外：外部函数和内存 API
MemorySegment segment = MemorySegment.ofArray(new int[10]);
int value = segment.get(ValueLayout.JAVA_INT, offset);
```

### JNI 使用警告（JEP 472 - 24 中警告）

检测 JNI 使用时：
- 警告即将到来的 JNI 使用限制
- 建议为使用 JNI 的应用程序添加 `--enable-native-access` 标志
- 推荐尽可能迁移到外部函数和内存 API
- 为本地访问添加 module-info.java 条目：
```java
module com.example.app {
    requires jdk.unsupported; // 用于剩余的 JNI 使用
}
```

## 垃圾收集更新

### ZGC 分代模式（JEP 474 - 23 中默认）

配置垃圾收集时：
- 默认 ZGC 现在使用分代模式
- 如果明确使用非分代 ZGC，请更新 JVM 标志：
```bash
# 显式非分代模式（将显示弃用警告）
-XX:+UseZGC -XX:-ZGenerational

# 默认分代模式
-XX:+UseZGC
```

### G1 改进（JEP 475 - 24 中实现）

使用 G1GC 时：
- 不需要代码更改 - 内部 JVM 优化
- 使用 C2 编译器可能会看到改进的编译性能

## 向量 API（JEP 469 - 25 中第八次孵化器）

处理数值计算时：
- 建议使用向量 API 进行 SIMD 操作（仍在孵化中）
- 添加 `--add-modules jdk.incubator.vector`
- 使用示例：
```java
import jdk.incubator.vector.*;

// 传统标量计算
for (int i = 0; i < a.length; i++) {
    c[i] = a[i] + b[i];
}

// 向量化计算
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
- 向编译器参数添加 `--enable-preview`
- 向运行时参数添加 `--enable-preview`
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

- Gradle 配置：
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
3. **处理警告**：解决来自 JEP 471/472 的弃用警告
4. **启用预览功能**：如果使用模式匹配或其他预览功能
5. **彻底测试**：特别是使用 JNI 或 sun.misc.Unsafe 的应用程序
6. **性能测试**：使用新的 ZGC 默认值验证 GC 行为

### 代码审查检查清单

审查 Java 25 升级代码时：
- [ ] 用类文件 API 替换 ASM 使用
- [ ] 将复杂的 HTML JavaDoc 转换为 Markdown
- [ ] 在适用的地方在 switch 表达式中使用原始模式
- [ ] 将 sun.misc.Unsafe 替换为 VarHandle 或 FFM API
- [ ] 为 JNI 使用添加本地访问权限
- [ ] 对复杂流操作使用流收集器
- [ ] 为预览功能更新构建配置

### 测试考虑

- 使用 `--enable-preview` 标志测试预览功能
- 验证 JNI 应用程序在本地访问警告下工作
- 使用新的 ZGC 分代模式进行性能测试
- 验证使用 Markdown 注释的 JavaDoc 生成

## 常见陷阱

1. **预览功能依赖**：不要在没有明确文档的情况下在库代码中使用预览功能
2. **本地访问**：直接或间接使用 JNI 的应用程序可能需要 `--enable-native-access` 配置
3. **Unsafe 迁移**：不要延迟从 sun.misc.Unsafe 迁移 - 弃用警告表明未来将移除
4. **模式匹配范围**：原始模式适用于所有原始类型，不仅仅是 int
5. **记录增强**：派生记录创建在 Java 23 中需要预览标志

## 性能考虑

- ZGC 分代模式可能会改善大多数工作负载的性能
- 类文件 API 减少 ASM 相关开销
- 流收集器为复杂流操作提供更好的性能
- G1GC 改进减少 JIT 编译开销

请在将 Java 25 升级部署到生产系统之前，在暂存环境中进行彻底测试。