## Dart 与 Flutter 实践要点

- What: Effective Dart 风格/文档/用法/设计 + Flutter 架构与工程实践（MVVM、仓储、依赖注入、路由、测试）。
- When: 编写 Dart/Flutter 代码、定义模型/函数/库、设计应用架构与测试时。
- Why: 一致、简洁、可维护；降低缺陷与重构成本；提升可测试性与扩展性。
- How: 遵循 DO/DON'T/PREFER/AVOID/CONSIDER 准则；MVVM 分层与单向数据流；不可变模型；依赖注入与 go_router。

### 关键要点
- Style: `dart format`；标识符 UpperCamelCase/lowerCamelCase/lowercase_with_underscores；导入排序；80 列优先。
- Docs: 使用 `///` 文档注释；首句摘要；避免冗余；方括号引用；示例与代码块用反引号围栏。
- Usage: 集合字面量；避免 `List.from()` 滥用；字符串插值；避免多余的 `cast()`/forEach；tear-off 优先。
- Design: 命名一致；避免 one-member 抽象类与全静态类；更偏好纯 mixin/class；类型注解策略清晰。
- 异常与异步: 避免无 on 的 catch；`rethrow`；优先 async/await；少用 Completer；Stream 用高阶方法。
- Flutter 架构: UI/数据层分离；仓储模式；MVVM（ViewModel+View）；ChangeNotifier/Listenables；不在 Widget 放业务逻辑。
- 数据: 单向数据流；不可变模型；freezed/built_value 代码生成；必要时区分 API 模型与领域模型。
- 工程: provider 依赖注入；go_router 导航；统一命名（HomeViewModel/HomeScreen/UserRepository）。
- 测试: 服务/仓储/ViewModel 单测；视图组件测试；使用 fakes 提升可测性。

### Compact Map
Style→Docs→Usage→Design→Errors/Async→MVVM→Repo→State→DI→Routing→Testing

### 示例问题
1) 何时优先使用 `freezed` 生成不可变模型？
2) View 与 ViewModel 的边界与依赖关系如何把控？
3) 单向数据流下如何处理中大型表单状态？
4) go_router 的嵌套路由与守卫策略实践？
5) 文档注释里如何正确引用标识符并插入示例？
6) 避免 `cast()` 的替代写法有哪些？
7) ChangeNotifier 与 Riverpod/Bloc 的取舍与迁移策略？
8) 如何在 Widget 测试中隔离网络与存储依赖？
9) 代码生成对构建时长的影响与权衡？
10) 库/包的导入排序自动化与 Lint 配置建议？

Source: d:\mycode\awesome-copilot\instructions\dart-n-flutter.instructions.md | Generated: 2025-10-17T00:00:00Z
