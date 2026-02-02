---
description: 'Shell scripting best practices and conventions for bash, sh, zsh, and other shells'
applyTo: '**/*.sh'
---

# Shell 脚本编写指南

有关为 bash、sh、zsh 和其他 shell 编写干净、安全且可维护的 shell 脚本的说明。

## 一般原则

- 生成干净、简单且简洁的代码
- 确保脚本易于阅读和理解
- 添加有助于理解脚本如何工作的注释
- 生成简洁的回显输出以提供执行状态
- 避免不必要的回显输出和过多的日志记录
- 如果可用，请使用 shellcheck 进行静态分析
- 除非另有说明，假设脚本用于自动化和测试而不是生产系统
- 首选安全扩展：双引号变量引用 (`"$var"`)，为了清晰起见，使用 `${var}`，并避免 `eval`
- 当可移植性要求允许时，使用现代 Bash 功能（`[[ ]]`、`local`、数组）；仅在需要时才回退到 POSIX 结构
- 为结构化数据选择可靠的解析器，而不是临时文本处理

## 错误处理和安全

- 始终启用 `set -euo pipefail` 以在出现错误时快速失败、捕获未设置的变量以及表面管道故障
- 执行前验证所有必需参数
- 提供带有上下文的清晰错误消息
- 使用 `trap` 清理临时资源或处理脚本终止时的意外退出
- 使用 `readonly` （或 `declare -r`）声明不可变值以防止意外重新分配
- 使用 `mktemp` 安全地创建临时文件或目录，并确保它们在清理处理程序中被删除

## 脚本结构

- 除非另有说明，否则以清晰的 shebang 开头：`#!/bin/bash`
- 包含解释脚本用途的标题注释
- 为顶部的所有变量定义默认值
- 使用可重用代码块的函数
- 创建可重用的函数，而不是重复类似的代码块
- 保持主执行流程清晰易读

## 使用 JSON 和 YAML

- 优先使用专用解析器（对于 JSON，使用 `jq`，对于 YAML，使用 `yq`，或者对于通过 `yq` 转换的 JSON，使用 `jq`），而不是使用 `grep`、`awk` 或 shell 字符串拆分进行临时文本处理
- 当 `jq`/`yq` 不可用或不合适时，请选择您的环境中可用的下一个最可靠的解析器，并明确如何安全地使用它
- 验证所需字段是否存在并显式处理丢失/无效的数据路径（例如，通过检查 `jq` 退出状态或使用 `// empty`）
- 引用 jq/yq 过滤器以防止 shell 扩展，并在需要纯字符串时首选 `--raw-output`
- 将解析器错误视为致命错误：在使用结果之前与 `set -euo pipefail` 组合或测试命令成功
- 在脚本顶部记录解析器依赖项，如果需要但未安装 `jq`/`yq` （或替代工具），则会快速失败并显示有用的消息

```bash
#!/bin/bash

# ============================================================================
# Script Description Here
# ============================================================================

set -euo pipefail

cleanup() {
    # Remove temporary resources or perform other teardown steps as needed
    if [[ -n "${TEMP_DIR:-}" && -d "$TEMP_DIR" ]]; then
        rm -rf "$TEMP_DIR"
    fi
}

trap cleanup EXIT

# Default values
RESOURCE_GROUP=""
REQUIRED_PARAM=""
OPTIONAL_PARAM="default-value"
readonly SCRIPT_NAME="$(basename "$0")"

TEMP_DIR=""

# Functions
usage() {
    echo "Usage: $SCRIPT_NAME [OPTIONS]"
    echo "Options:"
    echo "  -g, --resource-group   Resource group (required)"
    echo "  -h, --help            Show this help"
    exit 0
}

validate_requirements() {
    if [[ -z "$RESOURCE_GROUP" ]]; then
        echo "Error: Resource group is required"
        exit 1
    fi
}

main() {
    validate_requirements

    TEMP_DIR="$(mktemp -d)"
    if [[ ! -d "$TEMP_DIR" ]]; then
        echo "Error: failed to create temporary directory" >&2
        exit 1
    fi
    
    echo "============================================================================"
    echo "Script Execution Started"
    echo "============================================================================"
    
    # Main logic here
    
    echo "============================================================================"
    echo "Script Execution Completed"
    echo "============================================================================"
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -g|--resource-group)
            RESOURCE_GROUP="$2"
            shift 2
            ;;
        -h|--help)
            usage
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Execute main function
main "$@"

```
