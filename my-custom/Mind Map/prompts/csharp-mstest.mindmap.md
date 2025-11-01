## 文档综述（What/When/Why/How）

- What：MSTest 单元测试最佳实践（结构、数据驱动、断言、组织、Mock）

- When：使用 MSTest 或维护现有 MSTest 测试套件时

- Why：提升可读性与稳定性，建立一致的生命周期与数据驱动模式

- How：TestClass/TestMethod；Initialize/Cleanup（Test/Class/Assembly）；DataRow/DynamicData；清晰断言与分类

## 示例提问（Examples）

- “将此方法改造为 DataRow 数据驱动并添加失败消息”

- “为组件引入 Moq 隔离依赖并按 TestCategory 组织”

## 结构化要点（CN/EN）

- 结构/Structure：TestClass/TestMethod，AAA，命名规范

- 数据/Data：DataRow/DynamicData/TestProperty

- 断言/Assertions：AreEqual/AreSame/IsTrue/StringAssert/CollectionAssert/Throws

- 生命周期/Lifecycle：Initialize/Cleanup（Test/Class/Assembly）

- 组织/Org：TestCategory/Priority/Owner

## 中文思维导图

- 工程与依赖
- 生命周期
- 数据驱动
- 断言族
- Mock 与隔离
- 分类与优先级

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\csharp-mstest.prompt.md

- 生成时间：2025-10-17
