## 文档综述（What/When/Why/How）

- What：TUnit 测试最佳实践（.NET 8+、异步链式断言、生命周期钩子、并行控制、迁移指南）

- When：需要现代特性与更强生命周期钩子的测试场景

- Why：更灵活的异步断言与数据驱动、更丰富的并行与重试控制

- How：[Test] + [Arguments]/[MethodData]/[ClassData]；Before/After 钩子；Assert.That(...).And/Or；Repeat/Retry/ParallelLimit

## 示例提问（Examples）

- “将 xUnit 测试迁移到 TUnit，替换 Fact/Theory/InlineData 等”

- “为易波动用例增加 Retry 与 Timeout，并限制并行度”

## 结构化要点（CN/EN）

- 断言/Assert：await Assert.That().IsEqualTo/Throws

- 钩子/Hooks：Before/After(Test|Class|Assembly|Session)

- 数据/Data：[Arguments]/[MethodData]/[ClassData]

- 并行/Parallel：默认并行、NotInParallel、ParallelLimit

- 迁移/Migration：从 xUnit 映射

## 中文思维导图

- 基础结构
- 数据驱动
- 异步断言
- 生命周期钩子
- 并行/重试/超时
- 迁移路径

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\csharp-tunit.prompt.md

- 生成时间：2025-10-17
