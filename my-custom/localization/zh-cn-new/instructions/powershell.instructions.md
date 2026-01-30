---
applyTo: '**/*.ps1,**/*.psm1'
description: '基于 Microsoft 指南的 PowerShell cmdlet 和脚本最佳实践'
---

# PowerShell Cmdlet 开发指南

本指南提供 PowerShell 特定指令，帮助 GitHub Copilot 生成符合语言习惯、
安全且可维护的脚本。它与 Microsoft 的 PowerShell cmdlet 开发指南保持一致。

## 命名约定

- **动词-名词格式：**
  - 使用批准的 PowerShell 动词 (Get-Verb)
  - 使用单数名词
  - 动词和名词都使用 PascalCase
  - 避免特殊字符和空格

- **参数名称：**
  - 使用 PascalCase
  - 选择清晰、描述性的名称
  - 除非总是多个，否则使用单数形式
  - 遵循 PowerShell 标准名称

- **变量名称：**
  - 公共变量使用 PascalCase
  - 私有变量使用 camelCase
  - 避免缩写
  - 使用有意义的名称

- **避免别名：**
  - 使用完整的 cmdlet 名称
  - 避免在脚本中使用别名（例如：使用 Get-ChildItem 而不是 gci）
  - 记录任何自定义别名
  - 使用完整的参数名称

### 示例

```powershell
function Get-UserProfile {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$Username,

        [Parameter()]
        [ValidateSet('Basic', 'Detailed')]
        [string]$ProfileType = 'Basic'
    )

    process {
        # 逻辑在这里
    }
}
```

## 参数设计

- **标准参数：**
  - 使用通用参数名称（`Path`、`Name`、`Force`）
  - 遵循内置 cmdlet 约定
  - 为专业术语使用别名
  - 记录参数用途

- **参数名称：**
  - 除非总是多个，否则使用单数形式
  - 选择清晰、描述性的名称
  - 遵循 PowerShell 约定
  - 使用 PascalCase 格式

- **类型选择：**
  - 使用常见的 .NET 类型
  - 实施适当的验证
  - 考虑为有限选项使用 ValidateSet
  - 尽可能启用 tab 补全

- **开关参数：**
  - 对布尔标志使用 [switch]
  - 避免 $true/$false 参数
  - 省略时默认为 $false
  - 使用清晰的操作名称

### 示例

```powershell
function Set-ResourceConfiguration {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$Name,

        [Parameter()]
        [ValidateSet('Dev', 'Test', 'Prod')]
        [string]$Environment = 'Dev',

        [Parameter()]
        [switch]$Force,

        [Parameter()]
        [ValidateNotNullOrEmpty()]
        [string[]]$Tags
    )

    process {
        # 逻辑在这里
    }
}
```

## 管道和输出

- **管道输入：**
  - 对直接对象输入使用 `ValueFromPipeline`
  - 对属性映射使用 `ValueFromPipelineByPropertyName`
  - 为管道处理实施 Begin/Process/End 块
  - 记录管道输入要求

- **输出对象：**
  - 返回丰富的对象，而不是格式化文本
  - 对结构化数据使用 PSCustomObject
  - 避免为数据输出使用 Write-Host
  - 启用下游 cmdlet 处理

- **管道流式传输：**
  - 一次输出一个对象
  - 使用 process 块进行流式传输
  - 避免收集大型数组
  - 启用立即处理

- **传递模式：**
  - 操作 cmdlet 默认无输出
  - 实施 `-PassThru` 开关用于对象返回
  - 使用 `-PassThru` 返回修改/创建的对象
  - 使用详细/警告进行状态更新

### 示例

```powershell
function Update-ResourceStatus {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, ValueFromPipeline, ValueFromPipelineByPropertyName)]
        [string]$Name,

        [Parameter(Mandatory)]
        [ValidateSet('Active', 'Inactive', 'Maintenance')]
        [string]$Status,

        [Parameter()]
        [switch]$PassThru
    )

    begin {
        Write-Verbose 'Starting resource status update process'
        $timestamp = Get-Date
    }

    process {
        # 单独处理每个资源
        Write-Verbose "Processing resource: $Name"

        $resource = [PSCustomObject]@{
            Name        = $Name
            Status      = $Status
            LastUpdated = $timestamp
            UpdatedBy   = $env:USERNAME
        }

        # 仅在指定 PassThru 时输出
        if ($PassThru.IsPresent) {
            Write-Output $resource
        }
    }

    end {
        Write-Verbose 'Resource status update process completed'
    }
}
```

## 错误处理和安全性

- **ShouldProcess 实施：**
  - 使用 `[CmdletBinding(SupportsShouldProcess = $true)]`
  - 设置适当的 `ConfirmImpact` 级别
  - 为系统更改调用 `$PSCmdlet.ShouldProcess()`
  - 为额外确认使用 `ShouldContinue()`

- **消息流：**
  - `Write-Verbose` 用于带有 `-Verbose` 的操作详细信息
  - `Write-Warning` 用于警告条件
  - `Write-Error` 用于非终止错误
  - `throw` 用于终止错误
  - 除了用户界面文本外避免 `Write-Host`

- **错误处理模式：**
  - 使用 try/catch 块进行错误管理
  - 设置适当的 ErrorAction 偏好
  - 返回有意义的错误消息
  - 需要时使用 ErrorVariable
  - 包含适当的终止与非终止错误处理
  - 在带有 `[CmdletBinding()]` 的高级函数中，优先使用 `$PSCmdlet.WriteError()` 而不是 `Write-Error`
  - 在带有 `[CmdletBinding()]` 的高级函数中，优先使用 `$PSCmdlet.ThrowTerminatingError()` 而不是 `throw`
  - 构建包含类别、目标和异常详情的适当 ErrorRecord 对象

- **非交互式设计：**
  - 通过参数接受输入
  - 避免在脚本中使用 `Read-Host`
  - 支持自动化场景
  - 记录所有必需的输入

### 示例

```powershell
function Remove-UserAccount {
    [CmdletBinding(SupportsShouldProcess = $true, ConfirmImpact = 'High')]
    param(
        [Parameter(Mandatory, ValueFromPipeline)]
        [ValidateNotNullOrEmpty()]
        [string]$Username,

        [Parameter()]
        [switch]$Force
    )

    begin {
        Write-Verbose 'Starting user account removal process'
        $ErrorActionPreference = 'Stop'
    }

    process {
        try {
            # 验证
            if (-not (Test-UserExists -Username $Username)) {
                $errorRecord = [System.Management.Automation.ErrorRecord]::new(
                    [System.Exception]::new("User account '$Username' not found"),
                    'UserNotFound',
                    [System.Management.Automation.ErrorCategory]::ObjectNotFound,
                    $Username
                )
                $PSCmdlet.WriteError($errorRecord)
                return
            }

            # 确认
            $shouldProcessMessage = "Remove user account '$Username'"
            if ($Force -or $PSCmdlet.ShouldProcess($Username, $shouldProcessMessage)) {
                Write-Verbose "Removing user account: $Username"

                # 主要操作
                Remove-ADUser -Identity $Username -ErrorAction Stop
                Write-Warning "User account '$Username' has been removed"
            }
        } catch [Microsoft.ActiveDirectory.Management.ADException] {
            $errorRecord = [System.Management.Automation.ErrorRecord]::new(
                $_.Exception,
                'ActiveDirectoryError',
                [System.Management.Automation.ErrorCategory]::NotSpecified,
                $Username
            )
            $PSCmdlet.ThrowTerminatingError($errorRecord)
        } catch {
            $errorRecord = [System.Management.Automation.ErrorRecord]::new(
                $_.Exception,
                'UnexpectedError',
                [System.Management.Automation.ErrorCategory]::NotSpecified,
                $Username
            )
            $PSCmdlet.ThrowTerminatingError($errorRecord)
        }
    }

    end {
        Write-Verbose 'User account removal process completed'
    }
}
```

## 文档和样式

- **基于注释的帮助**：为任何面向公众的函数或 cmdlet 包含基于注释的帮助。在函数内，添加带有至少以下内容的 `<# ... #>` 帮助注释：
  - `.SYNOPSIS` 简要描述
  - `.DESCRIPTION` 详细解释
  - `.EXAMPLE` 包含实际用法的部分
  - `.PARAMETER` 描述
  - `.OUTPUTS` 返回的输出类型
  - `.NOTES` 附加信息

- **一致的格式化：**
  - 遵循一致的 PowerShell 样式
  - 使用适当的缩进（推荐 4 个空格）
  - 开括号与语句在同一行
  - 闭括号在新行
  - 管道操作符后使用换行符
  - 函数和参数名称使用 PascalCase
  - 避免不必要的空白

- **管道支持：**
  - 为管道函数实施 Begin/Process/End 块
  - 在适当的地方使用 ValueFromPipeline
  - 支持按属性名称的管道输入
  - 返回适当的对象，而不是格式化文本

- **避免别名**：使用完整的 cmdlet 名称和参数
  - 避免在脚本中使用别名（例如：使用 Get-ChildItem 而不是 gci）；别名在交互式 shell 使用中是可接受的。
  - 使用 `Where-Object` 而不是 `?` 或 `where`
  - 使用 `ForEach-Object` 而不是 `%`
  - 使用 `Get-ChildItem` 而不是 `ls` 或 `dir`

## 完整示例：端到端 Cmdlet 模式

```powershell
function New-Resource {
    [CmdletBinding(SupportsShouldProcess = $true, ConfirmImpact = 'Medium')]
    param(
        [Parameter(Mandatory = $true,
            ValueFromPipeline = $true,
            ValueFromPipelineByPropertyName = $true)]
        [ValidateNotNullOrEmpty()]
        [string]$Name,

        [Parameter()]
        [ValidateSet('Development', 'Production')]
        [string]$Environment = 'Development'
    )

    begin {
        Write-Verbose 'Starting resource creation process'
    }

    process {
        try {
            if ($PSCmdlet.ShouldProcess($Name, 'Create new resource')) {
                # 资源创建逻辑在这里
                Write-Output ([PSCustomObject]@{
                        Name        = $Name
                        Environment = $Environment
                        Created     = Get-Date
                    })
            }
        } catch {
            $errorRecord = [System.Management.Automation.ErrorRecord]::new(
                $_.Exception,
                'ResourceCreationFailed',
                [System.Management.Automation.ErrorCategory]::NotSpecified,
                $Name
            )
            $PSCmdlet.ThrowTerminatingError($errorRecord)
        }
    }

    end {
        Write-Verbose 'Completed resource creation process'
    }
}
```