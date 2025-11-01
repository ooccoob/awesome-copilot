## Node.js + JavaScript + Vitest 规范（速览）

### 这是什么/何时使用/为什么/如何做
- What: Node.js(20+ ESM) JavaScript 编码与 Vitest 测试约定。
- When: 新增特性/修复缺陷需配套测试；评审与发布前自检。
- Why: 保障可维护性与质量，避免引入多余依赖。
- How: ESM、async/await、内置模块优先、promisify、避免 null、函数优先于类、描述性命名。

### 关键要点
- 依赖: 能用内置就不用外部；新增前先征询。
- 异步: 统一 async/await；避免回调地狱；util.promisify。
- 风格: 简洁自解释；必要时少量注释；undefined 代替 null；函数式优先。
- 测试: Vitest；覆盖边界与异常；不为可测性改动生产代码。
- 文档: 重要变更更新 README；对外回答保持用户语言，代码统一英文。

### 紧凑脑图
- 语言与运行时→依赖策略→异步范式→风格与命名→测试策略→文档约定

### 开发者示例问题（≥10）
- 何时需要引入第三方库而不是内置模块？
- 如何将 callback 风格 API 封装为 promise？
- 错误边界与异常路径的单测示例如何设计？
- 如何组织测试数据与夹具以避免耦合？
- ESM 与 CJS 混用时的兼容策略？
- CI 中如何收集与门禁覆盖率？
- 定时器与异步重试在 Vitest 中的稳定写法？
- 何时选择函数 vs 类的抽象？
- undefined 替换 null 的迁移注意事项？
- 如何避免为覆盖率而改动实现细节？

—
Source: d:\mycode\awesome-copilot\instructions\nodejs-javascript-vitest.instructions.md | Generated: 2025-10-17
