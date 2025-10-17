## 文档综述（What/When/Why/How）

- What：xUnit 单元测试最佳实践（结构、数据驱动、断言、组织、Mock）

- When：新建/重构测试工程或制定团队测试规范时

- Why：提升测试可读性、稳定性与覆盖，避免反模式

- How：AAA 模式；Fact/Theory；Inline/Member/ClassData；Fixtures；清晰断言与隔离

## 示例提问（Examples）

- “将此测试改为 Theory + InlineData，并补充异常断言”

- “为多个测试类共享上下文使用 IClassFixture 示例”

## 结构化要点（CN/EN）

- 结构/Structure：AAA，命名 Method_Scenario_Expected

- 数据/Data：Inline/Member/ClassData，自定义 DataAttribute

- 断言/Assertions：Equal/Same/Throws/Contains/Matches

- 组织/Org：Trait、集合夹具、输出帮助

- 隔离/Isolation：Moq/NSubstitute，接口驱动

## 中文思维导图

- 工程与依赖
- 测试结构
- 数据驱动
- 断言清单
- Mock 与隔离
- 组织与分类

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\csharp-xunit.prompt.md

- 生成时间：2025-10-17
