---
applyTo: '**/*.Tests.ps1'
description: 'PowerShell Pester testing best practices based on Pester v5 conventions'
---

# PowerShell Pester v5 测试指南

本指南提供了有关使用 PowerShell Pester v5 模块创建自动化测试的 PowerShell 特定说明。请遵循 [powershell.instructions.md](./powershell.instructions-zh.md) 中的 PowerShell cmdlet 开发指南，了解一般 PowerShell 脚本编写最佳实践。

## 文件命名和结构

- **文件约定：** 使用 `*.Tests.ps1` 命名模式
- **放置：** 将测试文件放置在测试代码旁边或专用测试目录中
- **导入模式：** 使用`BeforeAll { . $PSScriptRoot/FunctionName.ps1 }`导入测试函数
- **无直接代码：** 将所有代码放入 Pester 块中（`BeforeAll`、`Describe`、`Context`、`It` 等）

## 测试结构层次结构

```powershell
BeforeAll { # Import tested functions }
Describe 'FunctionName' {
    Context 'When condition' {
        BeforeAll { # Setup for context }
        It 'Should behavior' { # Individual test }
        AfterAll { # Cleanup for context }
    }
}
```

## 核心关键词

- **`Describe`**：顶级分组，通常以正在测试的函数命名
- **`Context`**：针对特定场景在“描述”中进行子分组
- **`It`**：单独的测试用例，使用描述性名称
- **`Should`**：用于测试验证的断言关键字
- **`BeforeAll/AfterAll`**：每个块设置/拆卸一次
- **`BeforeEach/AfterEach`**：每次测试之前/之后的设置/拆卸

## 设置和拆卸

- **`BeforeAll`**：在包含块开始时运行一次，用于昂贵的操作
- **`BeforeEach`**：在块中的每个 `It` 之前运行，用于特定于测试的设置
- **`AfterEach`**：在每个 `It` 之后运行，即使测试失败也能保证
- **`AfterAll`**：在块末尾运行一次，用于清理
- **变量作用域**：`BeforeAll` 变量可用于子块（只读），`BeforeEach/It/AfterEach` 共享相同的作用域

## 断言（应该）

- **基本比较**：`-Be`、`-BeExactly`、`-Not -Be`
- **集合**：`-Contain`、`-BeIn`、`-HaveCount`
- **数字**：`-BeGreaterThan`、`-BeLessThan`、`-BeGreaterOrEqual`
- **字符串**：`-Match`、`-Like`、`-BeNullOrEmpty`
- **类型**：`-BeOfType`、`-BeTrue`、`-BeFalse`
- **文件**：`-Exist`、`-FileContentMatch`
- **例外**：`-Throw`、`-Not -Throw`

## 嘲笑

- **`Mock CommandName { ScriptBlock }`**：替换命令行为
- **`-ParameterFilter`**：仅当参数匹配条件时才模拟
- **`-Verifiable`**：将模拟标记为需要验证
- **`Should -Invoke`**：验证模拟被调用特定次数
- **`Should -InvokeVerifiable`**：验证所有可验证的模拟都被调用
- **范围**：模拟默认包含块范围

```powershell
Mock Get-Service { @{ Status = 'Running' } } -ParameterFilter { $Name -eq 'TestService' }
Should -Invoke Get-Service -Exactly 1 -ParameterFilter { $Name -eq 'TestService' }
```

## 测试用例（数据驱动测试）

使用 `-TestCases` 或 `-ForEach` 进行参数化测试：

```powershell
It 'Should return <Expected> for <Input>' -TestCases @(
    @{ Input = 'value1'; Expected = 'result1' }
    @{ Input = 'value2'; Expected = 'result2' }
) {
    Get-Function $Input | Should -Be $Expected
}
```

## 数据驱动测试

- **`-ForEach`**：可用于 `Describe`、`Context` 和 `It`，用于从数据生成多个测试
- **`-TestCases`**：`It` 块上 `-ForEach` 的别名（向后兼容）
- **哈希表数据**：每个项目定义测试中可用的变量（例如，`@{ Name = 'value'; Expected = 'result' }`）
- **数组数据**：对当前项目使用 `$_` 变量
- **模板**：在测试名称中使用 `<variablename>` 进行动态扩展

```powershell
# Hashtable approach
It 'Returns <Expected> for <Name>' -ForEach @(
    @{ Name = 'test1'; Expected = 'result1' }
    @{ Name = 'test2'; Expected = 'result2' }
) { Get-Function $Name | Should -Be $Expected }

# Array approach
It 'Contains <_>' -ForEach 'item1', 'item2' { Get-Collection | Should -Contain $_ }
```

## 标签

- **适用于**：`Describe`、`Context` 和 `It` 块
- **过滤**：将 `-TagFilter` 和 `-ExcludeTagFilter` 与 `Invoke-Pester` 一起使用
- **通配符**：标签支持`-like`通配符，实现灵活过滤

```powershell
Describe 'Function' -Tag 'Unit' {
    It 'Should work' -Tag 'Fast', 'Stable' { }
    It 'Should be slow' -Tag 'Slow', 'Integration' { }
}

# Run only fast unit tests
Invoke-Pester -TagFilter 'Unit' -ExcludeTagFilter 'Slow'
```

## 跳过

- **`-Skip`**：可用于 `Describe`、`Context` 和 `It` 以跳过测试
- **有条件**：使用 `-Skip:$condition` 进行动态跳过
- **运行时跳过**：在测试执行期间使用 `Set-ItResult -Skipped` （安装/拆卸仍然运行）

```powershell
It 'Should work on Windows' -Skip:(-not $IsWindows) { }
Context 'Integration tests' -Skip { }
```

## 错误处理

- **Continue on Failure**：使用 `Should.ErrorAction = 'Continue'` 收集多个失败
- **停止关键**：使用 `-ErrorAction Stop` 作为前提条件
- **测试异常**：使用`{ Code } | Should -Throw`进行异常测试

## 最佳实践

- **描述性名称**：使用清晰的测试描述来解释行为
- **AAA 模式**：安排（设置）、行动（执行）、断言（验证）
- **独立测试**：每个测试应该是独立的
- **避免别名**：使用完整的 cmdlet 名称（`Where-Object` 而不是 `?`）
- **单一职责**：如果可能，每个测试一个断言
- **测试文件组织**：将相关测试分组到上下文块中。上下文块可以嵌套。

## 测试模式示例

```powershell
BeforeAll {
    . $PSScriptRoot/Get-UserInfo.ps1
}

Describe 'Get-UserInfo' {
    Context 'When user exists' {
        BeforeAll {
            Mock Get-ADUser { @{ Name = 'TestUser'; Enabled = $true } }
        }

        It 'Should return user object' {
            $result = Get-UserInfo -Username 'TestUser'
            $result | Should -Not -BeNullOrEmpty
            $result.Name | Should -Be 'TestUser'
        }

        It 'Should call Get-ADUser once' {
            Get-UserInfo -Username 'TestUser'
            Should -Invoke Get-ADUser -Exactly 1
        }
    }

    Context 'When user does not exist' {
        BeforeAll {
            Mock Get-ADUser { throw "User not found" }
        }

        It 'Should throw exception' {
            { Get-UserInfo -Username 'NonExistent' } | Should -Throw "*not found*"
        }
    }
}
```

## 配置

当调用 `Invoke-Pester` 来控制执行行为时，配置在 **外部** 测试文件中定义。

```powershell
# Create configuration (Pester 5.2+)
$config = New-PesterConfiguration
$config.Run.Path = './Tests'
$config.Output.Verbosity = 'Detailed'
$config.TestResult.Enabled = $true
$config.TestResult.OutputFormat = 'NUnitXml'
$config.Should.ErrorAction = 'Continue'
Invoke-Pester -Configuration $config
```

**关键部分**：运行（路径、退出）、过滤器（标签、排除标签）、输出（详细程度）、测试结果（启用、输出格式）、代码覆盖（启用、路径）、应该（错误操作）、调试
