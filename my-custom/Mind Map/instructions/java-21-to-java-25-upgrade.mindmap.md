## What/When/Why/How
- What: 将JDK 21项目升级至JDK 25的关键变化、预览/标准特性与迁移注意事项。
- When: 需要使用 Class-File API、Markdown文档注释、Stream Gatherers、原生访问策略调整等能力时。
- Why: 更强的字节码处理官方API、更现代的文档注释、更丰富的流处理能力、GC与性能优化。
- How: 升级构建链→消除弃用/告警→按需启用预览→验证GC→全链路回归。

## Key Points
- Class-File API（23预览→25标准）：替代 ASM，包 java.lang.classfile。
- Markdown 文档注释(JEP 467)：使用 /// 风格与 Markdown 语法。
- Stream Gatherers(JEP 473/485)：window/fold 等状态增强流操作。
- 模式匹配增强(JEP 455/488 预览)：原生类型模式与 guard。
- 派生记录创建(JEP 468 预览)：with 表达式派生记录。
- sun.misc.Unsafe 访问弃用(JEP 471)：迁移至 VarHandle 或 FFM API。
- JNI 限制警告(JEP 472/24)：需要 --enable-native-access 或迁移 FFM。
- GC：ZGC 代际化默认(23)；G1/C2 编译优化(24)。
- Vector API(仍孵化)：需 --add-modules jdk.incubator.vector。

## Compact Map
21→25 升级
- Build: 置顶JDK/插件，必要时 --enable-preview
- Bytecode: ASM→Class-File API
- Docs: JavaDoc→Markdown注释
- Streams: Gatherers 窗口/折叠
- Patterns: 原始类型匹配 + when 守卫
- Records: with 派生(预览)
- Unsafe/JNI: VarHandle/FFM + 原生访问配置
- GC: ZGC 默认代际

## Migration Checklist
- [ ] 替换 ASM 为 Class-File API（或封装兼容层）
- [ ] 迁移 sun.misc.Unsafe → VarHandle/FFM
- [ ] 审核 JNI 用法并配置 --enable-native-access
- [ ] 引入 Gatherers 改写复杂流
- [ ] 采用 Markdown 文档注释规范
- [ ] 评估 ZGC 参数；移除非代际显式设置
- [ ] 仅在使用预览/孵化特性时添加 flags

## Example Questions (≥10)
- Class-File API 如何完成最小等价改造以替代 ASM？
- 何时应将 Unsafe 迁移为 VarHandle，何时使用 FFM？
- Gatherers 对窗口/状态类计算能带来哪些简化？
- Markdown 文档注释的迁移策略与工具链支持如何配置？
- 原生访问受限下现有 JNI 方案如何最小化改造继续运行？
- 如何为预览/孵化特性配置 Maven/Gradle 与测试插件？
- ZGC 代际默认后应如何验证停顿与吞吐改善？
- 原始类型模式匹配的典型用例有哪些？
- with 派生记录在不可变建模中的价值与边界？
- 如何组织代码以便日后关闭预览特性仍可编译？

Source: d:\mycode\awesome-copilot\instructions\java-21-to-java-25-upgrade.instructions.md | Generated: 2025-10-17
