---
description: 'R language and document formats (R, Rmd, Quarto): coding standards and Copilot guidance for idiomatic, safe, and consistent code generation.'
applyTo: '**/*.R, **/*.r, **/*.Rmd, **/*.rmd, **/*.qmd'
---

# R 编程语言说明

## 目的

帮助 GitHub Copilot 跨项目生成惯用、安全且可维护的 R 代码。

## 核心约定

- **匹配项目的风格。** 如果文件显示偏好（tidyverse 与基本 R、`%>%` 与 `|>`），请遵循它。
- **更喜欢清晰的矢量化代码。** 保持函数较小并避免隐藏的副作用。
- **限定示例/片段中的非基函数**，例如 `dplyr::mutate()`、`stringr::str_detect()`。在项目代码中，当这是回购规范时，使用 `library()` 是可以接受的。
- **命名：** `lower_snake_case` 用于对象/文件；避免名称中出现点。
- **副作用：** 切勿调用 `setwd()`；更喜欢项目相对路径（例如 `here::here()`）。
- **可重复性：** 使用 `withr::with_seed()` 在随机操作周围设置种子。
- **验证：**验证并约束用户输入；尽可能使用类型检查和白名单。
- **安全：** 避免 `eval(parse())`、未经验证的 shell 调用和未参数化的 SQL。

### 管道操作员

- **本机管道 `|>` (R ≥ 4.1.0)：** 首选 R ≥ 4.1（无额外依赖性）。
- **Magrittr 管道 `%>%`：** 在已提交给 magrittr 的项目中或当您需要 `.`、`%T>%` 或 `%$%` 等功能时继续使用。
- **保持一致：** 不要在同一脚本中混合 `|>` 和 `%>%` ，除非有明确的技术原因。

## 性能考虑因素

- **大型数据集：**考虑`data.table`；以您的工作量为基准。
- **dplyr 兼容性：** 使用 `dtplyr` 编写 dplyr 语法，自动转换为 data.table 操作以提高性能。
- **分析：** 使用 `profvis::profvis()` 来识别代码中的性能瓶颈。优化前的配置文件。
- **缓存：** 使用 `memoise::memoise()` 缓存昂贵的函数结果。对于重复的 API 调用或复杂的计算特别有用。
- **矢量化：** 优先选择矢量化操作而不是循环。使用 `purrr::map_*()` 系列或 `apply()` 系列来满足剩余的迭代需求。

## 模具和质量

- **格式：** `styler` （tidyverse 样式），两个空格缩进，约 100 个字符行。
- **Linting：** `lintr` 通过 `.lintr` 配置。
- **预提交：**考虑 `precommit` 自动进行 lint/format 挂钩。
- **文档：** roxygen2 用于导出函数（`@param`、`@return`、`@examples`）。
- **测试：**更喜欢易于单元测试的小型、纯粹、可组合的函数。
- **依赖关系：** 使用 `renv` 进行管理；添加包后的快照。
- **路径：**为了可移植性，更喜欢 `fs` 和 `here` 。

## 数据整理和 I/O

- **数据帧：** 更喜欢 tidyverse-heavy 文件中的 tibbles；否则基 `data.frame()` 就可以了。
- **迭代：** 在 tidyverse 代码中使用 `purrr` 。在基本样式代码中，更喜欢类型稳定的矢量化模式，例如 `vapply()`
   （对于原子输出）或 `Map()` （对于元素操作）而不是显式 `for` 循环，当它们提高清晰度或性能时。
- **字符串和日期：** 使用已存在的 `stringr`/`lubridate` ；否则使用明确的基本帮助器（例如，具有显式格式的 `nchar()`、`substr()`、`as.Date()`）。
- **I/O：**更喜欢显式的、类型化的读取器（例如，`readr::read_csv()`）；明确解析假设。

## 绘图

- 对于出版质量的绘图，首选 `ggplot2`。保持图层可读并标记轴和单位。

## 错误处理

- 在 tidyverse 上下文中，使用 `rlang::abort()` / `rlang::warn()` 作为结构化条件；在纯基代码中，使用 `stop()` / `warning()`。
- 对于可恢复操作：
- 当您想要相同类型的类型化后备值（更简单）时，请使用 `purrr::possibly()` 。
- 当您需要捕获结果和错误以供以后检查或记录时，请使用 `purrr::safely()`。
- 在基本 R 中使用 `tryCatch()` 进行细粒度控制或与非 tidyverse 代码兼容。
- 更喜欢一致的返回结构——正常流程的类型化输出，仅在需要错误详细信息时才使用结构化列表。

## 安全最佳实践

- **命令执行：** 优先使用 `processx::run()` 或 `sys::exec_wait()` 而不是 `system()`；验证并清理所有参数。
- **数据库查询：** 使用参数化 `DBI` 查询来防止 SQL 注入。
- **文件路径：** 规范和清理用户提供的路径（例如 `fs::path_sanitize()`），并根据白名单进行验证。
- **凭证：** 切勿对秘密进行硬编码。使用环境变量 (`Sys.getenv()`)、VCS 外部的配置或 `keyring`。

## 闪亮的

- 模块化重要应用程序的 UI 和服务器逻辑。使用 `eventReactive()` / `observeEvent()` 来实现显式依赖。
- 使用 `req()` 和清晰、用户友好的消息验证输入。
- 对数据库使用连接池（`pool`）；避免长期存在的全局对象。
- 隔离昂贵的计算，并更喜欢 `reactiveVal()` / `reactiveValues()` 对于小状态。

## R Markdown / 四开

- 保持大块的重点；更喜欢显式块选项（`echo`、`message`、`warning`）。
- 避免全局状态；更喜欢当地的帮手。将 `withr::with_seed()` 用于确定性块。

## 副驾驶特定指导

- 如果当前文件使用 tidyverse，**建议 tidyverse-first 模式**（例如，使用 `dplyr::across()` 而不是被取代的动词）。如果存在基本 R 风格，**使用基本习惯用法**。
- 限定建议中的非碱基调用（例如 `dplyr::mutate()`）。
- 当惯用时，建议循环上的矢量化或整洁的解决方案。
- 比起长管道，更喜欢小的辅助函数。
- 当多种方法等效时，优先考虑可读性和类型稳定性并解释权衡。

---

## 最少的例子

```r
# Base R variant
scores <- data.frame(id = 1:5, x = c(1, 3, 2, 5, 4))
safe_log <- function(x) tryCatch(log(x), error = function(e) NA_real_)
scores$z <- vapply(scores$x, safe_log, numeric(1))

# Tidyverse variant (if this file uses tidyverse)
result <- tibble::tibble(id = 1:5, x = c(1, 3, 2, 5, 4)) |>
dplyr::mutate(z = purrr::map_dbl(x, purrr::possibly(log, otherwise = NA_real_))) |>
dplyr::filter(z > 0)

# Example reusable helper with roxygen2 doc
#' Compute the z-score of a numeric vector
#' @param x A numeric vector
#' @return Numeric vector of z-scores
#' @examples z_score(c(1, 2, 3))
z_score <- function(x) (x - mean(x, na.rm = TRUE)) / stats::sd(x, na.rm = TRUE)
```
