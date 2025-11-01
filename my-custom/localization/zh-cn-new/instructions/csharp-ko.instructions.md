---
description: 'C# 应用程序开发的代码编写规范 by @jgkim999'
applyTo: '**/*.cs'
---

# C# 代码编写规范

## 命名规范 (Naming Conventions)

一致的命名规范是代码可读性的关键。建议遵循 Microsoft 的指南。

| 元素 | 命名规范 | 示例 |
|------|-----------|------|
| 接口 | 前缀 'I' + PascalCase | `IAsyncRepository`, `ILogger` |
| 公共(public)成员 | 帕斯卡命名法 (PascalCase) | `public int MaxCount;`, `public void GetData()` |
| 参数、局部变量 | 驼峰命名法 (camelCase) | `int userCount`, `string customerName` |
| 私有/内部字段 | 下划线(_) + 驼峰命名法 | `private string _connectionString;` |
| 常量 (const) | 帕斯卡命名法 (PascalCase) | `public const int DefaultTimeout = 5000;` |
| 泛型类型参数 | 前缀 'T' + 描述性名称 | `TKey`, `TValue`, `TResult` |
| 异步方法 | 'Async' 后缀 | `GetUserAsync`, `DownloadFileAsync` |

## 代码格式和可读性 (Formatting & Readability)

一致的格式使代码在视觉上更易于解析。

| 项目 | 规则 | 说明 |
|------|------|------|
| 缩进 | 使用4个空格 | 使用4个空格而不是制表符。cs文件必须使用4个空格。 |
| 括号 | 始终使用大括号 {} | 即使控制语句(if、for、while等)只有一行，也要始终使用大括号。 |
| 空行 | 逻辑分隔 | 在方法定义、属性定义、逻辑分隔的代码块之间添加空行。 |
| 语句编写 | 一行一个语句 | 一行只编写一个语句。 |
| var关键字 | 仅在类型明确时使用 | 只有在能从右侧明确推断变量类型时才使用var。 |
| 命名空间 | 使用文件范围命名空间 | 在C# 10及以上版本中，使用文件范围命名空间减少不必要的缩进。 |
| 注释 | 编写XML格式注释 | 为编写的class或函数始终编写xml格式的注释。 |

## 语言功能使用 (Language Features)

利用最新的C#功能使代码更简洁高效。

| 功能 | 说明 | 示例/参考 |
|------|------|------|
| 异步编程 | 对I/O绑定工作使用async/await | `async Task<string> GetDataAsync()` |
| ConfigureAwait | 在库代码中减少上下文切换开销 | `await SomeMethodAsync().ConfigureAwait(false)` |
| LINQ | 查询和操作集合数据 | `users.Where(u => u.IsActive).ToList()` |
| 表达式主体成员 | 简洁表达简单的方法/属性 | `public string Name => _name;` |
| 可空引用类型 | 编译时防止NullReferenceException | `#nullable enable` |
| using声明 | 简洁处理IDisposable对象 | `using var stream = new FileStream(...);` |

## 性能和异常处理 (Performance & Exception Handling)

构建健壮快速应用程序的指南。

### 异常处理

只捕获可以处理的具体异常。避免捕获像catch (Exception)这样的一般异常。

不要使用异常来控制程序流程。异常应该只用于意外错误情况。

### 性能

当重复连接字符串时，使用StringBuilder而不是+运算符。

使用Entity Framework Core时，对只读查询使用.AsNoTracking()来提高性能。

避免不必要的对象分配，特别是在循环内要特别注意。

## 安全性 (Security)

编写安全代码的基本原则。

| 安全领域 | 规则 | 说明 |
|------|------|------|
| 输入验证 | 验证所有外部数据 | 不要信任来自外部（用户、API等）的所有数据，始终进行有效性验证。 |
| SQL注入防护 | 使用参数化查询 | 始终使用参数化查询或Entity Framework等ORM来防止SQL注入攻击。 |
| 敏感数据保护 | 使用配置管理工具 | 不要在源代码中硬编码密码、连接字符串、API密钥等，而要使用Secret Manager、Azure Key Vault等。 |

应该将这些规则集成到项目的.editorconfig文件和团队的代码审查流程中，以持续保持高质量代码。