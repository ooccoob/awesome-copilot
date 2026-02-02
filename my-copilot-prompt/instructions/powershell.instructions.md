---
applyTo: '**/*.ps1,**/*.psm1'
description: 'PowerShell cmdlet and scripting best practices based on Microsoft guidelines'
---

# PowerShell Cmdlet 开发指南

本指南提供特定于 PowerShell 的说明，以帮助 GitHub Copilot 生成惯用语，
安全且可维护的脚本。它符合 Microsoft 的 PowerShell cmdlet 开发指南。

## 命名约定

- **动词-名词格式：**
  - 使用批准的 PowerShell 动词 (Get-Verb)
  - 使用单数名词
  - 动词和名词的帕斯卡命名法
  - 避免特殊字符和空格

- **参数名称：**
  - 使用帕斯卡命名法
  - 选择清晰、描述性的名称
  - 使用单数形式，除非总是多个
  - 遵循 PowerShell 标准名称

- **变量名称：**
  - 对公共变量使用 PascalCase
  - 私有变量使用驼峰命名法
  - 避免缩写
  - 使用有意义的名称

- **避免别名：**
  - 使用完整的 cmdlet 名称
  - 避免在脚本中使用别名（例如，使用 Get-ChildItem 而不是 gci）
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
        # Logic here
    }
}
```

## 参数设计

- **标准参数：**
  - 使用通用参数名称（`Path`、`Name`、`Force`）
  - 遵循内置 cmdlet 约定
  - 对专业术语使用别名
  - 文档参数用途

- **参数名称：**
  - 使用单数形式，除非总是多个
  - 选择清晰、描述性的名称
  - 遵循 PowerShell 约定
  - 使用 PascalCase 格式

- **类型选择：**
  - 使用常见的 .NET 类型
  - 实施适当的验证
  - 考虑使用 ValidateSet 来获得有限的选项
  - 尽可能启用制表符补全

- **开关参数：**
  - 使用 [switch] 作为布尔标志
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
        # Logic here
    }
}
```

## 管道和输出

- **管道输入：**
  - 使用 `ValueFromPipeline` 进行直接对象输入
  - 使用 `ValueFromPipelineByPropertyName` 进行属性映射
  - 实现管道处理的 Begin/Process/End 块
  - 记录管道输入要求

- **输出对象：**
  - 返回丰富的对象，而不是格式化文本
  - 将 PSCustomObject 用于结构化数据
  - 避免使用 Write-Host 进行数据输出
  - 启用下游 cmdlet 处理

- **管道流：**
  - 一次输出一个对象
  - 使用进程块进行流式传输
  - 避免收集大型数组
  - 启用立即处理

- **直通模式：**
  - 默认情况下，操作 cmdlet 没有输出
  - 实现 `-PassThru` 开关以返回对象
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
        # Process each resource individually
        Write-Verbose "Processing resource: $Name"

        $resource = [PSCustomObject]@{
            Name        = $Name
            Status      = $Status
            LastUpdated = $timestamp
            UpdatedBy   = $env:USERNAME
        }

        # Only output if PassThru is specified
        if ($PassThru.IsPresent) {
            Write-Output $resource
        }
    }

    end {
        Write-Verbose 'Resource status update process completed'
    }
}
```

## 错误处理和安全

- **应流程实施：**
  - 使用 `[CmdletBinding(SupportsShouldProcess = $true)]`
  - 设置适当的 `ConfirmImpact` 级别
  - 调用 `$PSCmdlet.ShouldProcess()` 进行系统更改
  - 使用 `ShouldContinue()` 进行额外确认

- **消息流：**
  - `Write-Verbose` 了解 `-Verbose` 的操作细节
  - `Write-Warning` 用于警告情况
  - `Write-Error` 用于非终止错误
  - `throw` 用于终止错误
  - 除用户界面文本外，避免使用 `Write-Host`

- **错误处理模式：**
  - 使用 try/catch 块进行错误管理
  - 设置适当的 ErrorAction 首选项
  - 返回有意义的错误消息
  - 需要时使用 ErrorVariable
  - 包括正确的终止与非终止错误处理
  - 在具有 `[CmdletBinding()]` 的高级函数中，优先使用 `$PSCmdlet.WriteError()` 而不是 `Write-Error`
  - 在具有 `[CmdletBinding()]` 的高级函数中，优先使用 `$PSCmdlet.ThrowTerminatingError()` 而不是 `throw`
  - 使用类别、目标和异常详细信息构造正确的 ErrorRecord 对象

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
            # Validation
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

            # Confirmation
            $shouldProcessMessage = "Remove user account '$Username'"
            if ($Force -or $PSCmdlet.ShouldProcess($Username, $shouldProcessMessage)) {
                Write-Verbose "Removing user account: $Username"

                # Main operation
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

## 文档和风格

- **基于评论的帮助：** 包括任何面向公众的函数或 cmdlet 的基于评论的帮助。在函数内部，添加 `<# ... #>` 帮助注释，至少包含：
  - `.SYNOPSIS` 简要说明
  - `.DESCRIPTION` 详细解释
  - 具有实际用途的 `.EXAMPLE` 部分
  - `.PARAMETER` 描述
  - `.OUTPUTS` 返回的输出类型
  - `.NOTES` 附加信息

- **一致的格式：**
  - 遵循一致的 PowerShell 风格
  - 使用适当的缩进（建议 4 个空格）
  - 左大括号与语句位于同一行
  - 新行上的右大括号
  - 在管道运算符之后使用换行符
  - 函数和参数名称的 PascalCase
  - 避免不必要的空白

- **管道支持：**
  - 为管道函数实现 Begin/Process/End 块
  - 在适当的情况下使用 ValueFromPipeline
  - 支持按属性名称管道输入
  - 返回正确的对象，而不是格式化文本

- **避免别名：** 使用完整的 cmdlet 名称和参数
  - 避免在脚本中使用别名（例如，使用 Get-ChildItem 而不是 gci）；交互式 shell 使用时可以使用别名。
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
                # Resource creation logic here
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
