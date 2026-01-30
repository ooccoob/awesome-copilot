## What/When/Why/How
- What: 将JDK 17项目升级到JDK 21的实践要点与代码改造清单。
- When: 采用JDK 21（LTS）或引入其特性（如虚拟线程、switch模式匹配、记录模式、Sequenced Collections等）。
- Why: 获得性能、并发、可读性、安全与API能力提升（UTF-8默认、简单Web服务器、KEM等）。
- How: 分阶段升级构建环境→语言特性→并发/GC→弃用项替换→预览特性按需开启与回归测试。

## Key Points
- 语言特性：switch模式匹配(JEP 441)、记录模式(JEP 440)、未命名模式与变量(JEP 443/预览)、字符串模板(JEP 430/预览)。
- 并发：虚拟线程(JEP 444)、结构化并发(预览)；以阻塞I/O为主的高并发强烈受益。
- 集合：SequencedCollection/Set/Map(JEP 431) 提供 first/last/reversed 等一致API。
- 运行时/IO：UTF-8默认(JEP 400)、简单HTTP服务器(JEP 408)、InetAddress SPI(JEP 418)。
- 安全&加密：KEM API(JEP 452)。
- 弃用/警告：finalization弃用(JEP 421)→Cleaner/try-with-resources；动态Agent加载告警(JEP 451)。
- 构建：Maven/Gradle 配置 --enable-preview 仅在使用预览特性时启用；测试插件也需配置。
- GC：可评估 Generational ZGC(JEP 439)。

## Compact Map
Java17→21
- Build: 升级JDK/插件→启用预览(可选)
- Lang: switch/record patterns, templates(预览), unnamed(_)
- Concurrency: 虚拟线程 + 结构化并发
- Collections: Sequenced*
- Runtime: UTF-8默认, jwebserver
- Security: KEM
- Deprecations: finalize→Cleaner, 动态Agent→启动加载
- GC: Gen ZGC 按需

## Migration Checklist
- [ ] instanceof链→switch模式匹配
- [ ] 记录结构解构→record patterns
- [ ] ThreadLocal→ScopedValue(预览)或保留
- [ ] Platform threads→Virtual threads(适用时)
- [ ] 去掉显式UTF-8常量
- [ ] 移除finalize，改Cleaner/try-with-resources
- [ ] 采用SequencedCollection API
- [ ] 仅在用到预览时添加 --enable-preview

## Example Questions (≥10)
- 如何把 instanceof 链重写为 switch 模式匹配？
- 记录类型如何用 record pattern 解构并在 switch 中匹配？
- 何时该将线程池迁移为虚拟线程？有哪些陷阱？
- 结构化并发该如何在聚合查询中落地？
- 如何开启/配置 --enable-preview 以使用字符串模板？
- SequencedCollection 在 List/LinkedHashSet 上的常见用法有哪些？
- 默认UTF-8带来哪些可删除的冗余代码？
- 如何将 finalize 替换为 Cleaner 模式？
- Generational ZGC 何时优于 G1？如何验证？
- 动态Agent加载的告警该如何处理与替代？

Source: d:\mycode\awesome-copilot\instructions\java-17-to-java-21-upgrade.instructions.md | Generated: 2025-10-17
