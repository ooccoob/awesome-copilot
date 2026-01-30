---
post_title: "java-junit.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "java-junit-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "java", "testing", "junit", "mockito"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Java JUnit prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个专门用于生成 Java 单元测试代码的提示词，主要使用 JUnit 和 Mockito 框架。

## When

- 在为 Java 类或方法编写单元测试时。
- 当需要为复杂的业务逻辑或边界条件创建测试用例时。
- 在学习或实践测试驱动开发 (TDD) 时。

## Why

- 快速生成高质量、可维护的单元测试代码，提高开发效率。
- 确保测试覆盖率，提高代码质量和稳定性。
- 推广单元测试的最佳实践，如 Arrange-Act-Assert 模式和模拟对象的使用。

## How

- 使用 `/java-junit` 命令并提供你想要测试的 Java 类或方法。
- AI 将分析代码，并为公共方法生成相应的测试方法。
- 生成的测试将使用 JUnit 的 `@Test` 注解，并使用 Mockito 来模拟依赖项。

## Key points (英文+中文对照)

- Unit Testing (单元测试)
- Test-Driven Development (TDD, 测试驱动开发)
- Mocking (模拟)
- Code Coverage (代码覆盖率)

## 使用场景

### 1. 为 Service 层方法生成测试 (Generating Tests for Service Layer Methods)

- **用户故事**: 作为一名 Java 开发人员，我完成了一个 `UserService`，现在需要为它的 `createUser` 方法编写单元测试。
- **例 1**: `/java-junit [selection=UserService.java] 为这个`UserService` 的 `createUser` 方法生成单元测试。请模拟 `UserRepository`的依赖。`
- **例 2**: `/java-junit [selection=ProductService.java] 为`getProductById`方法编写测试，包括找到产品和找不到产品的两种情况。`

### 2. 测试异常处理 (Testing Exception Handling)

- **用户故事**: 作为一名后端工程师，我需要确保我的代码在遇到无效输入时能正确抛出异常。
- **例 1**: `/java-junit [selection=OrderService.java] 为`placeOrder` 方法编写一个测试，验证当库存不足时是否会抛出 `InsufficientStockException`。`
- **例 2**: `/java-junit 给我一个使用`assertThrows`来测试异常的 JUnit 5 示例。`

### 3. 参数化测试 (Parameterized Tests)

- **用户故事**: 作为一名 QA 工程师，我需要用多组不同的输入数据来测试一个计算器类的 `add` 方法。
- **例 1**: `/java-junit [selection=Calculator.java] 为`add` 方法创建一个 JUnit 5 参数化测试，使用 `@CsvSource`提供多组输入和预期的输出。`

### 4. 测试私有方法 (Testing Private Methods - via Public Methods)

- **用户故事**: 作为一名开发人员，我有一个复杂的私有方法，我想通过测试调用它的公共方法来间接验证其逻辑。
- **例 1**: `/java-junit [selection=ReportGenerator.java]`ReportGenerator` 有一个公共方法 `generate`，它内部调用了一个复杂的私有方法`calculateMetrics`。请编写`generate` 方法的测试，以覆盖 `calculateMetrics`的不同逻辑分支。`

## 原始文件

- [java-junit.prompt.md](../../prompts/java-junit.prompt.md)
