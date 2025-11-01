---
description: 'R 语言和文档格式（R、Rmd、Quarto）：符合语言习惯、安全且一致的代码生成的编码标准和 Copilot 指导。'
applyTo: '**/*.R, **/*.r, **/*.Rmd, **/*.rmd, **/*.qmd'
---

# R 编程语言指令

## 目的

帮助 GitHub Copilot 在项目中生成符合语言习惯、安全且可维护的 R 代码。

## 核心约定

- **匹配项目风格。** 如果文件显示偏好（tidyverse vs. base R、`%>%` vs. `|>`），请遵循它。
- **优先使用清晰、向量化代码。** 保持函数小，避免隐藏副作用。
- **在示例/片段中限定非基础函数**，例如：`dplyr::mutate()`、`stringr::str_detect()`。在项目代码中，当这是仓库规范时，使用 `library()` 是可接受的。
- **命名**：对象/文件使用 `lower_snake_case`；避免名称中的点。
- **副作用**：永不调用 `setwd()`；优先使用项目相对路径（例如：`here::here()`）。
- **可重现性**：使用 `withr::with_seed()` 在随机操作周围本地设置种子。
- **验证**：验证和约束用户输入；尽可能使用类型检查和允许列表。
- **安全性**：避免 `eval(parse())`、未验证的 shell 调用和非参数化 SQL。

### 管道操作符

- **原生管道 `|>`（R ≥ 4.1.0）**：在 R ≥ 4.1 中优先使用（无额外依赖）。
- **Magrittr 管道 `%>%`**：在已经承诺使用 magrittr 或当您需要如 `.`、`%T>%` 或 `%$%` 等功能的项目中继续使用。
- **保持一致**：除非有明确的技术原因，否则不要在同一脚本中混合使用 `|>` 和 `%>%`。

## 性能考虑

- **大数据集**：考虑 `data.table`；使用您的工作负载进行基准测试。
- **dplyr 兼容性**：使用 `dtplyr` 编写 dplyr 语法，自动转换为 data.table 操作以获得性能提升。
- **性能分析**：使用 `profvis::profvis()` 识别代码中的性能瓶颈。在优化之前进行分析。
- **缓存**：使用 `memoise::memoise()` 缓存昂贵的函数结果。特别适用于重复的 API 调用或复杂计算。
- **向量化**：优先使用向量化操作而不是循环。对剩余的迭代需求使用 `purrr::map_*()` 系列或 `apply()` 系列。

## 工具和质量

- **格式化**：`styler`（tidyverse 风格）、两空格缩进、~100 字符行。
- **代码检查**：通过 `.lintr` 配置的 `lintr`。
- **预提交**：考虑 `precommit` 钩子自动代码检查/格式化。
- **文档**：导出函数的 roxygen2（`@param`、`@return`、`@examples`）。
- **测试**：优先使用小型、纯、可组合的函数，这些函数易于单元测试。
- **依赖项**：使用 `renv` 管理；添加包后进行快照。
- **路径**：为可移植性优先使用 `fs` 和 `here`。

## 数据处理和 I/O

- **数据框**：在重度使用 tidyverse 的文件中优先使用 tibbles；否则基础 `data.frame()` 也可以。
- **迭代**：在 tidyverse 代码中使用 `purrr`。在基础风格代码中，优先使用类型稳定、向量化的模式，如 `vapply()`（对于原子输出）或 `Map()`（对于逐元素操作），而不是显式 `for` 循环，当它们提高清晰性或性能时。
- **字符串和日期**：在已存在的地方使用 `stringr`/`lubridate`；否则使用清晰的基础辅助函数（例如：`nchar()`、`substr()`、带显式格式的 `as.Date()`）。
- **I/O**：优先使用显式、类型化的读取器（例如：`readr::read_csv()`）；使解析假设显式化。

## 绘图

- 为出版质量的图优先使用 `ggplot2`。保持图层可读并标记坐标轴和单位。

## 错误处理

- 在 tidyverse 上下文中，使用 `rlang::abort()` / `rlang::warn()` 进行结构化条件；在仅基础代码中，使用 `stop()` / `warning()`。
- 对于可恢复操作：
- 当您想要相同类型的类型化回退值时使用 `purrr::possibly()`（更简单）。
- 当您需要捕获结果和错误以便以后检查或日志记录时使用 `purrr::safely()`。
- 在基础 R 中使用 `tryCatch()` 进行细粒度控制或与非 tidyverse 代码的兼容性。
- 优先使用一致的返回结构——正常流的类型化输出，仅在需要错误详细信息时使用结构化列表。

## 安全最佳实践

- **命令执行**：优先使用 `processx::run()` 或 `sys::exec_wait()` 而不是 `system()`；验证和清理所有参数。
- **数据库查询**：使用参数化 `DBI` 查询防止 SQL 注入。
- **文件路径**：规范化和清理用户提供的路径（例如：`fs::path_sanitize()`），并根据允许列表进行验证。
- **凭据**：永不硬编码秘密。使用环境变量（`Sys.getenv()`）、VCS 外的配置或 `keyring`。

## Shiny

- 为非平凡应用模块化 UI 和服务器逻辑。使用 `eventReactive()` / `observeEvent()` 进行显式依赖。
- 使用 `req()` 和清晰、用户友好的消息验证输入。
- 对数据库使用连接池（`pool`）；避免长期存在的全局对象。
- 隔离昂贵的计算，对小状态优先使用 `reactiveVal()` / `reactiveValues()`。

## R Markdown / Quarto

- 保持块专注；优先使用显式块选项（`echo`、`message`、`warning`）。
- 避免全局状态；优先使用本地辅助函数。对确定性块使用 `withr::with_seed()`。

## Copilot 特定指导

- 如果当前文件使用 tidyverse，**建议 tidyverse 优先模式**（例如：`dplyr::across()` 而不是被取代的动词）。如果存在 base-R 风格，**使用基础习惯用法**。
- 在建议中限定非基础调用（例如：`dplyr::mutate()`）。
- 当符合语言习惯时，建议向量化或 tidy 解决方案而不是循环。
- 优先使用小型辅助函数而不是长管道。
- 当多种方法等效时，优先考虑可读性和类型稳定性并解释权衡。

---

## 最小示例

```r
# Base R 变体
scores <- data.frame(id = 1:5, x = c(1, 3, 2, 5, 4))
safe_log <- function(x) tryCatch(log(x), error = function(e) NA_real_)
scores$z <- vapply(scores$x, safe_log, numeric(1))

# Tidyverse 变体（如果此文件使用 tidyverse）
result <- tibble::tibble(id = 1:5, x = c(1, 3, 2, 5, 4)) |>
dplyr::mutate(z = purrr::map_dbl(x, purrr::possibly(log, otherwise = NA_real_))) |>
dplyr::filter(z > 0)

# 带有 roxygen2 文档的可重用辅助函数示例
#' 计算数值向量的 z 分数
#' @param x 数值向量
#' @return z 分数的数值向量
#' @examples z_score(c(1, 2, 3))
z_score <- function(x) (x - mean(x, na.rm = TRUE)) / stats::sd(x, na.rm = TRUE)
```