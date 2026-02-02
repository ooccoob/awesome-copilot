---
agent: "agent"
description: "Write a coding standards document for a project using the coding styles from the file(s) and/or folder(s) passed as arguments in the prompt."
tools: ['createFile', 'editFiles', 'web/fetch', 'githubRepo', 'search', 'testFailure']
---

# 从文件写入编码标准

使用文件的现有语法来建立项目的标准和风格指南。如果传递多个文件或文件夹，则循环遍历文件夹中的每个文件或多个文件，将文件的数据附加到临时内存或文件中，然后在完成时使用临时数据作为单个实例；就好像它是标准和样式指南所依据的文件名一样。

## 规则和配置

下面是一组准配置 `boolean` 和 `string[]` 变量。处理 `true` 或每个变量的其他值的条件位于二级标题 `## Variable and Parameter Configuration Conditions` 下。

提示的参数有文本定义。有一个必需参数 **`${fileName}`**，以及多个可选参数 **`${folderName}`**、**`${instructions}`** 和任何 **`[configVariableAsParameter]`**。

### 配置变量

* 添加标准测试=假；
* 添加自述文件=假；
* addToREADMEInsertions = ["atBegin", "middle", "beforeEnd", "bestFitUsingContext"];
  - 默认为 **beforeEnd**。
* 创建新文件=真；
* fetchStyleURL = true;
* 发现不一致=真；
* 修复不一致= true；
* newFileName = ["CONTRIBUTING.md", "STYLE.md", "CODE_OF_CONDUCT.md", "CODING_STANDARDS.md", "DEVELOPING.md", "CONTRIBUTION_GUIDE.md", "GUIDELINES.md", "PROJECT_STANDARDS.md", "BEST_PRACTICES.md", “黑客.md”]；
  - 对于 `${newFileName}` 中的每个文件，如果文件不存在，则使用该文件名和 `break`，否则继续使用 `${newFileName}` 的下一个文件名。
* 输出规范提示=假；
* useTemplate = "详细"; // 或“v”
  - 可能的值为 `[["v", "verbose"], ["m", "minimal"], ["b", "best fit"], ["custom"]]`。
  - 选择提示文件底部二级标题 `## Coding Standards Templates` 下的两个示例模板之一，或使用其他更适合的组合。
  - 如果**自定义**，则按请求应用。

### 配置变量作为提示参数

如果任何变量名称按原样传递给提示，或者作为类似但明确相关的文本值传递给提示，则使用传递给提示的值覆盖默认变量值。

### 提示参数

* **fileName** = 将根据以下方面进行分析的文件的名称：缩进、变量命名、注释、条件过程、函数过程以及文件编码语言的其他语法相关数据。
* folderName = 文件夹的名称，用于将多个文件中的数据提取到一个聚合数据集中，该数据集将根据以下方面进行分析：缩进、变量命名、注释、条件过程、函数过程以及文件编码语言的其他与语法相关的数据。
* 说明 = 将为特殊情况提供的附加说明、规则和程序。
* [configVariableAsParameter] = 如果传递，将覆盖配置变量的默认状态。示例：
  - useTemplate = 如果传递将覆盖配置 `${useTemplate}` 默认值。值为 `[["v", "verbose"], ["m", "minimal"], ["b", "best fit"]]`。

#### 必需和可选参数

* **文件名** - 必填
* 文件夹名称 - *可选*
* 说明 - *可选*
* [configVariableAsParameter] - *可选*

## 变量和参数配置条件

### __代码0__

* 如果为 true，则将 `${fixInconsistencies}` 切换为 false。

### __代码0__

* 将编码标准插入到 `README.md` 中，而不是输出到提示符或创建新文件。
* 如果为 true，则将 `${createNewFile}` 和 `${outputSpecToPrompt}` 都切换为 false。

### __代码0__

* 如果 `${addToREADME}` 为 true，则将编码标准数据插入到 `README.md` 文件的 **开头** 标题后面。

### __代码0__

* 如果 `${addToREADME}` 为 true，则将编码标准数据插入到 `README.md` 文件的 **中间**，更改标准标题标题以匹配 `README.md` 组合的标题。

### __代码0__

* 如果 `${addToREADME}` 为 true，则在 `README.md` 文件的 **end** 插入编码标准数据，在最后一个字符后插入新行，然后在新行上插入数据。

### __代码0__

* 如果 `${addToREADME}` 为真，则根据 `README.md` 组成和数据流的上下文，将编码标准数据插入到 `README.md` 文件的 **最佳拟合行** 处。

### __代码0__

* 编码标准文件完成后，编写一个测试文件以确保传递给它的一个或多个文件符合编码标准。

### __代码0__

* 使用 `${newFileName}` 中的值或可能的值之一创建一个新文件。
* 如果为 true，则将 `${outputSpecToPrompt}` 和 `${addToREADME}` 都切换为 false。

### __代码0__

* 另外，使用从嵌套在第三级标题 `### Fetch Links` 下的链接获取的数据作为上下文，为新文件、提示或 `README.md` 创建标准、规范和样式数据。
* 对于 `### Fetch Links` 中的每个相关项目，运行 `#fetch ${item}`。

### __代码0__

* 评估与缩进、换行、注释、条件和函数嵌套、引号包装器（即字符串的 `'` 或 `"` 等）相关的语法，并进行分类。
* 对于每个类别，进行计数，如果一项与计数中的大多数不匹配，则提交到临时内存。
* 根据 `${fixInconsistencies}` 的状态，编辑并修复低计数类别以匹配大多数类别，或输出以提示临时内存中存储的不一致。

### __代码0__

* 使用临时存储器中存储的不一致来编辑和修复语法数据的低计数类别，以匹配大多数相应的语法数据。

### __代码0__

* 如果专门定义为 `string`，则使用 `${newFileName}` 中的值创建一个新文件。

### __代码0__

* 如果 **NOT** 明确定义为 `string`，而是 `object` 或数组，则通过应用以下规则使用 `${newFileName}` 中的值创建一个新文件：
  - 对于 `${newFileName}` 中的每个文件名，如果文件不存在，则使用该文件名和 `break`，否则继续下一个。

### __代码0__

* 将编码标准输出到提示符中，而不是创建文件或添加到 README 中。
* 如果为 true，则将 `${createNewFile}` 和 `${addToREADME}` 都切换为 false。

### __代码0__

* 在编写编码标准数据时，使用三级标题`### "v", "verbose"`下的数据作为指导模板。

### __代码0__

* 在编写编码标准数据时，使用三级标题`### "m", "minimal"`下的数据作为指导模板。

### __代码0__

* 根据从 `${fileName}` 中提取的数据，使用三级标题 `### "v", "verbose"` 或 `### "m", "minimal"` 下的数据，并在编写编码标准数据时使用最合适的作为指导模板。

### __代码0__

* 在编写编码标准数据时，使用自定义提示、说明、模板或其他作为指导模板传递的数据。

## **如果** __代码0__

根据编程语言，对于下面列表中的每个链接，如果编程语言为 `${fileName} == [<Language> Style Guide]`，则运行 `#fetch (URL)`。

### 获取链接

- [C 风格指南](https://users.ece.cmu.edu/~eno/coding/CCodingStandard.html)
- [C# 风格指南](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions)
- [C++ 风格指南](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines)
- [Go 风格指南](https://github.com/golang-standards/project-layout)
- [Java 风格指南](https://coderanch.com/wiki/718799/Style)
- [AngularJS 应用风格指南](https://github.com/mgechev/angularjs-style-guide)
- [jQuery 风格指南](https://contribute.jquery.org/style-guide/js/)
- [JavaScript 风格指南](https://www.w3schools.com/js/js_conventions.asp)
- [JSON 样式指南](https://google.github.io/styleguide/jsoncstyleguide.xml)
- [Kotlin 风格指南](https://kotlinlang.org/docs/coding-conventions.html)
- [Markdown 风格指南](https://cirosantilli.com/markdown-style-guide/)
- [Perl 风格指南](https://perldoc.perl.org/perlstyle)
- [PHP 风格指南](https://phptherightway.com/)
- [Python 风格指南](https://peps.python.org/pep-0008/)
- [Ruby 风格指南](https://rubystyle.guide/)
- [Rust 风格指南](https://github.com/rust-lang/rust/tree/HEAD/src/doc/style-guide/src)
- [Swift 风格指南](https://www.swift.org/documentation/api-design-guidelines/)
- [TypeScript 风格指南](https://www.typescriptlang.org/docs/handbook/declaration-files/do-s-and-don-ts.html)
- [Visual Basic 风格指南](https://en.wikibooks.org/wiki/Visual_Basic/Coding_Standards)
- [Shell 脚本风格指南](https://google.github.io/styleguide/shellguide.html)
- [Git 使用风格指南](https://github.com/agis/git-style-guide)
- [PowerShell 风格指南](https://github.com/PoshCode/PowerShellPracticeAndStyle)
- [CSS](https://cssguidelin.es/)
- [Sass 风格指南](https://sass-guidelin.es/)
- [HTML 样式指南](https://github.com/marcobiedermann/html-style-guide)
- [Linux 内核风格指南](https://www.kernel.org/doc/html/latest/process/coding-style.html)
- [Node.js 风格指南](https://github.com/felixge/node-style-guide)
- [SQL 风格指南](https://www.sqlstyle.guide/)
- [角度风格指南](https://angular.dev/style-guide)
- [Vue 风格指南](https://vuejs.org/style-guide/rules-strongly-recommended.html)
- [Django 风格指南](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/)
- [SystemVerilog 风格指南](https://github.com/lowRISC/style-guides/blob/master/VerilogCodingStyle.md)

## 编码标准模板

### __代码0__

```text
    ```markdown
    ## 一、简介
    *   **目的：** 简要解释为什么要建立编码标准（例如，为了提高代码质量、可维护性和团队协作）。
    *   **范围：** 定义本规范适用的语言、项目或模块。

    ## 2. 命名约定
    *   **变量：** `camelCase`
    *   **函数/方法：** `PascalCase` 或 `camelCase`。
    *   **类/结构：** `PascalCase`。
    *   **常量：** `UPPER_SNAKE_CASE`。

    ## 3. 格式和风格
    *   **缩进：** 每个缩进（或制表符）使用 4 个空格。
    *   **行长度：** 将行限制为最多 80 或 120 个字符。
    *   **大括号：** 使用“K&R”样式（在同一行上打开大括号）或“Allman”样式（在新行上打开大括号）。
    *   **空行：** 指定用于分隔逻辑代码块的空行数。

    ## 4.评论
    *   **文档字符串/函数注释：** 描述函数的用途、参数和返回值。
    *   **内联评论：** 解释复杂或不明显的逻辑。
    *   **文件头：** 指定文件头中应包含哪些信息，例如作者、日期和文件描述。

    ## 5. 错误处理
    *   **一般：** 如何处理和记录错误。
    *   **细节：** 使用哪些异常类型，以及错误消息中包含哪些信息。

    ## 6. 最佳实践和反模式
    *   **一般：** 列出要避免的常见反模式（例如全局变量、幻数）。
    *   **特定于语言：** 基于项目编程语言的具体建议。

    ## 7. 例子
    *   提供一个小代码示例，演示规则的正确应用。
    *   提供一个错误实现的小代码示例以及如何修复它。

    ## 8. 贡献和执行
    *   解释如何执行标准（例如，通过代码审查）。
    *   提供为标准文档本身做出贡献的指南。
    ```
```

### __代码0__

```text
    ```markdown

    # 风格指南

    本文档定义了该项目中使用的样式和约定。
    除非另有说明，所有贡献均应遵循这些规则。

    ## 1. 通用代码风格

    - 优先考虑清晰性而非简洁性。
    - 保持函数和方法小而集中。
    - 避免重复逻辑；更喜欢共享助手/实用程序。
    - 删除未使用的变量、导入、代码路径和文件。

    ## 2. 命名约定

    使用描述性名称。避免使用缩写，除非众所周知。

|项目 |大会 |示例|
    |-----------------|----------------------|--------------------|
    |变量| __代码0__ | __代码1__ |
    |功能| __代码0__ | __代码1__ |
    |常数 | __代码0__ | __代码1__ |
    |类型/结构 | __代码0__ | __代码1__ |
    |文件名| __代码0__ | __代码1__ |

    ## 3. 格式规则

    - 缩进：**4 个空格**
    - 行长度：**最多 100 个字符**
    - 编码：**UTF-8**，无BOM
    - 以换行符结束文件

    ### 大括号（C 语言示例，根据您的语言进行调整）

        ```c
        if (condition) {
            do_something();
        } else {
            do_something_else();
        }
        ```

    ### 间距

    - 关键字后一个空格：`if (x)`，而不是 `if(x)`
    - 顶级函数之间有一个空行

    ## 4. 评论和文档

    - 解释*为什么*，而不是*什么*，除非意图不清楚。
    - 随着代码更改，保持注释保持最新。
    - 公共函数应包括目的和参数的简短描述。

    推荐标签：

        ```text
        TODO: follow-up work
        FIXME: known incorrect behavior
        NOTE: non-obvious design decision
        ```

    ## 5. 错误处理

    - 明确处理错误情况。
    - 避免无声的失败；返回错误或适当地记录它们。
    - 在失败返回之前清理资源（文件、内存、句柄）。

    ## 6. 提交和审查实践

    ### 提交
    - 每次提交一个逻辑更改。
    - 编写清晰的提交消息：

        ```text
        Short summary (max ~50 chars)
        Optional longer explanation of context and rationale.
        ```

    ### 评论
    - 保持拉取请求相当小。
    - 在评审讨论中保持尊重和建设性。
    - 如果您不同意，请解决所要求的更改或解释。

    ## 7. 测试

    - 为新功能编写测试。
    - 测试应该是确定性的（没有播种就没有随机性）。
    - 优先选择可读的测试用例而不是复杂的测试抽象。

    ## 8. 本指南的变更

    风格不断演变。
    通过提出问题或发送更新此文档的补丁来提出改进建议。
    ```
```