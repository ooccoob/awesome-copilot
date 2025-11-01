## What/When/Why/How
- What: 从 JDK 11 升级到 17 的语言特性、API 与构建配置迁移要点
- When: 升级构建链、引入 Records/Sealed/Pattern Matching/Text Blocks 等
- Why: 提升可读性/性能/安全；拥抱现代 Java 范式
- How: 渐进迁移（构建→清理废弃→语言增强→性能调优），配合测试/基准

## Key Points
- 语言: Records(16)、Sealed(17)、instanceof 模式匹配(16)、Switch 表达式(14)、文本块(15)
- 运行时: Helpful NPE(14)、PRNG(17)、Unix 域套接字(16)、NVM 映射(14)
- 安全/序列化: 反序列化过滤器(17)
- 构建: Maven/Gradle 设置 release=17；预览特性需 --enable-preview
- 废弃: SecurityManager/Applet/Nashorn 移除与替代
- GC/启动: ZGC/Shenandoah、CDS/Dynamic CDS
- 策略: 记录数据类→record；受限继承→sealed；多分支→switch 表达式

## Compact Map
构建→清理废弃→语言增强→运行时改进→安全→GC/性能→测试/基准

## Example Questions (10+)
1) 将数据类重构为 record 并加校验构造器
2) 设计一个 sealed 层次并与 switch+pattern 配合
3) instanceof 链改为模式匹配的重写示例
4) 文本块替换多行 SQL/HTML 的范式
5) Maven/Gradle 配置到 Java 17（含预览）
6) 移除 SecurityManager 依赖的替代方案
7) 使用新 PRNG API 的并行随机示例
8) 启用 ZGC 并收集 GC 日志的参数
9) 创建与加载自定义 CDS 归档
10) 升级回归测试清单与性能基线制定

Source: d:\mycode\awesome-copilot\instructions\java-11-to-java-17-upgrade.instructions.md | Generated: 2025-10-17T00:00:00Z
