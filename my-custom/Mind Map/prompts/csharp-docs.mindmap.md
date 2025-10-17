## 文档综述（What/When/Why/How）

- What：C# XML 注释与文档化最佳实践提示词

- When：需要补齐公共/内部 API 文档以提升可发现性与在线文档质量时

- Why：统一风格与粒度，便于 IDE/Doc 工具消费

- How：按成员类型（方法/构造/属性/异常）给出具体标签与措辞准则，涵盖示例/引用/继承文档

## 示例提问（Examples）

- “为该公共 API 补全 `<summary>/<param>/<returns>/<exception>` 并使用 `<see cref>` 引用相关类型”

- “布尔返回/参数的措辞遵循 true/false 模式”

## 结构化要点（CN/EN）

- 通用/General：summary/remarks/see/seealso/inheritdoc

- 方法/Methods：param/typeparam/returns

- 属性/Props：Gets/sets/value/默认值

- 构造/Ctors：初始化措辞

- 异常/Exceptions：条件化描述

## 中文思维导图

- 标签用法
- 成员分类
- 措辞规范
- 参考与继承
- 边界与示例

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\csharp-docs.prompt.md

- 生成时间：2025-10-17
