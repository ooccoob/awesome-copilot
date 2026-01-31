---
描述：“创作 GNU Make Makefile 的最佳实践”
applyTo: "**/Makefile, **/makefile, **/*.mk, **/GNUmakefile"
---

# Makefile 开发说明

有关编写干净、可维护且可移植的 GNU Make Makefile 的说明。这些说明基于 [GNU Make 手册](https://www.gnu.org/software/make/manual/)。

## 一般原则

- 编写遵循 GNU Make 约定的清晰且可维护的 makefile
- 使用清楚表明其用途的描述性目标名称
- 保留默认目标（第一个目标）作为最常见的构建操作
- 编写规则和方法时，优先考虑可读性而不是简洁性
- 添加注释来解释复杂的规则、变量或不明显的行为

## 命名约定

- 将您的 makefile 命名为 `Makefile` （建议用于可见性）或 `makefile`
- 仅对与其他 make 实现不兼容的 GNU Make 特定功能使用 `GNUmakefile`
- 使用标准变量名称：`objects`、`OBJECTS`、`objs`、`OBJS`、`obj` 或 `OBJ` 作为目标文件列表
- 内置变量名使用大写（例如 `CC`、`CFLAGS`、`LDFLAGS`）
- 使用反映其操作的描述性目标名称（例如，`clean`、`install`、`test`）

## 文件结构

- 将默认目标（主要构建目标）作为 makefile 中的第一条规则
- 将相关目标逻辑地组合在一起
- 在 makefile 顶部规则之前定义变量
- 使用 `.PHONY` 声明不代表文件的目标
- 使用以下内容构建 makefile：变量，然后是规则，然后是虚假目标

```makefile
# Variables
CC = gcc
CFLAGS = -Wall -g
objects = main.o utils.o

# Default goal
all: program

# Rules
program: $(objects)
	$(CC) -o program $(objects)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Phony targets
.PHONY: clean all
clean:
	rm -f program $(objects)
```

## 变量和替换

- 使用变量避免重复并提高可维护性
- 使用 `:=` （简单扩展）定义变量以进行立即计算，使用 `=` 进行递归扩展
- 使用 `?=` 设置可以覆盖的默认值
- 使用 `+=` 附加到现有变量
- 使用 `$(VARIABLE)` 而非 `$VARIABLE` 引用变量（除非是单个字符）
- 在配方中使用自动变量（`$@`、`$<`、`$^`、`$?`、`$*`）使规则更加通用

```makefile
# Simple expansion (evaluates immediately)
CC := gcc

# Recursive expansion (evaluates when used)
CFLAGS = -Wall $(EXTRA_FLAGS)

# Conditional assignment
PREFIX ?= /usr/local

# Append to variable
CFLAGS += -g
```

## 规则和先决条件

- 明确区分目标、先决条件和方法
- 对标准编译使用隐式规则（例如，`.c` 到 `.o`）
- 按逻辑顺序列出先决条件（仅按顺序之前的正常先决条件）
- 对不应触发重建的目录和依赖项使用仅顺序先决条件（在 `|` 之后）
- 包括所有实际依赖项以确保正确重建
- 避免目标之间的循环依赖
- 请记住，像 `$^` 这样的自动变量中省略了仅限订单的先决条件，因此如果需要，请显式引用它们

下面的示例显示了将对象编译到 `obj/` 目录中的模式规则。该目录本身被列为仅订单先决条件，因此它是在编译之前创建的，但在其时间戳更改时不会强制重新编译。

```makefile
# Normal prerequisites
program: main.o utils.o
	$(CC) -o $@ $^

# Order-only prerequisites (directory creation)
obj/%.o: %.c | obj
	$(CC) $(CFLAGS) -c $< -o $@

obj:
	mkdir -p obj
```

## 食谱和命令

- 每个配方行以 **制表符** （不是空格）开始，除非 `.RECIPEPREFIX` 被更改
- 在适当的时候使用 `@` 前缀来抑制命令回显
- 使用 `-` 前缀忽略特定命令的错误（谨慎使用）
- 当相关命令必须一起执行时，将相关命令与 `&&` 或 `;` 组合在同一行
- 保持食谱可读；使用反斜杠延续将长命令分成多行
- 需要时在配方中使用 shell 条件和循环

```makefile
# Silent command
clean:
	@echo "Cleaning up..."
	@rm -f $(objects)

# Ignore errors
.PHONY: clean-all
clean-all:
	-rm -rf build/
	-rm -rf dist/

# Multi-line recipe with proper continuation
install: program
	install -d $(PREFIX)/bin && \
		install -m 755 program $(PREFIX)/bin
```

## 虚假目标

- 始终使用 `.PHONY` 声明虚假目标，以避免与同名文件发生冲突
- 使用虚假目标执行 `clean`、`install`、`test`、`all` 等操作
- 将虚假目标声明放在规则定义附近或 makefile 末尾

```makefile
.PHONY: all clean test install

all: program

clean:
	rm -f program $(objects)

test: program
	./run-tests.sh

install: program
	install -m 755 program $(PREFIX)/bin
```

## 模式规则和隐式规则

- 使用模式规则 (`%.o: %.c`) 进行通用转换
- 适当时利用内置的隐式规则（GNU Make 知道如何将 `.c` 编译为 `.o`）
- 覆盖隐式规则变量（如 `CC`、`CFLAGS`）而不是重写规则
- 仅当内置规则不足时才定义自定义模式规则

```makefile
# Use built-in implicit rules by setting variables
CC = gcc
CFLAGS = -Wall -O2

# Custom pattern rule for special cases
%.pdf: %.md
	pandoc $< -o $@
```

## 分割长线

- 使用反斜杠换行符 (`\`) 分割长行以提高可读性
- 请注意，反斜杠换行符在非配方上下文中会转换为单个空格
- 在配方中，反斜杠换行保留 shell 的行延续
- 避免反斜杠后尾随空格

### 不添加空格的拆分

如果需要在不添加空格的情况下分割行，可以使用特殊技术：插入 `$ ` （美元空格），后跟反斜杠换行符。 `$ ` 指的是具有单空格名称的变量，该变量不存在并且扩展为空，从而有效地连接行而不插入空格。

```makefile
# Concatenate strings without adding whitespace
# The following creates the value "oneword"
var := one$ \
       word

# This is equivalent to:
# var := oneword
```

```makefile
# Variable definition split across lines
sources = main.c \
          utils.c \
          parser.c \
          handler.c

# Recipe with long command
build: $(objects)
	$(CC) -o program $(objects) \
	      $(LDFLAGS) \
	      -lm -lpthread
```

## 包括其他 Makefile

- 使用 `include` 指令在 makefile 之间共享通用定义
- 使用 `-include` （或 `sinclude`）包含可选的 makefile，不会出现错误
- 将 `include` 指令放在可能影响包含文件的变量定义之后
- 将 `include` 用于共享变量、模式规则或公共目标

```makefile
# Include common settings
include config.mk

# Include optional local configuration
-include local.mk
```

## 有条件指令

- 对特定于平台或配置的规则使用条件指令（`ifeq`、`ifneq`、`ifdef`、`ifndef`）
- 将条件放在 makefile 级别，而不是在配方中（在配方中使用 shell 条件）
- 保持条件简单且有据可查

```makefile
# Platform-specific settings
ifeq ($(OS),Windows_NT)
    EXE_EXT = .exe
else
    EXE_EXT =
endif

program: main.o
	$(CC) -o program$(EXE_EXT) main.o
```

## 自动先决条件

- 自动生成标头依赖项，而不是手动维护它们
- 使用 `-MMD` 和 `-MP` 等编译器标志生成具有依赖项的 `.d` 文件
- 使用 `-include $(deps)` 包含生成的依赖文件以避免错误（如果它们不存在）

```makefile
objects = main.o utils.o
deps = $(objects:.o=.d)

# Include dependency files
-include $(deps)

# Compile with automatic dependency generation
%.o: %.c
	$(CC) $(CFLAGS) -MMD -MP -c $< -o $@
```

## 错误处理和调试

- 使用 `$(error text)` 或 `$(warning text)` 函数进行构建时诊断
- 使用 `make -n` （试运行）测试 makefile 以查看命令而不执行
- 使用 `make -p` 打印规则和变量的数据库以进行调试
- 在 makefile 的开头验证所需的变量和工具

```makefile
# Check for required tools
ifeq ($(shell which gcc),)
    $(error "gcc is not installed or not in PATH")
endif

# Validate required variables
ifndef VERSION
    $(error VERSION is not defined)
endif
```

## 清洁目标

- 始终提供 `clean` 目标来删除生成的文件
- 将 `clean` 声明为虚假文件以避免与名为“clean”的文件发生冲突
- 如果文件不存在，则将 `-` 前缀与 `rm` 命令一起使用以忽略错误
- 考虑单独的 `clean` （删除对象）和 `distclean` （删除所有生成的文件）目标

```makefile
.PHONY: clean distclean

clean:
	-rm -f $(objects)
	-rm -f $(deps)

distclean: clean
	-rm -f program config.mk
```

## 便携性考虑因素

- 如果需要移植到其他 make 实现，请避免使用 GNU Make 特定的功能
- 使用标准 shell 命令（首选 POSIX shell 结构）
- 使用 `make -B` 进行测试以强制重建所有目标
- 记录任何特定于平台的要求或使用的 GNU Make 扩展

## 性能优化

- 对于不需要递归扩展的变量使用 `:=` （更快）
- 避免不必要地使用创建子进程的 `$(shell ...)`
- 有效地订购先决条件（最常更改的文件放在最后）
- 通过确保目标不冲突来安全地使用并行构建 (`make -j`)

## 文档和评论

- 添加标题注释来解释 makefile 的用途
- 记录非明显变量设置及其影响
- 在注释中包含使用示例或目标
- 为复杂规则或特定于平台的解决方法添加内联注释

```makefile
# Makefile for building the example application
#
# Usage:
#   make          - Build the program
#   make clean    - Remove generated files
#   make install  - Install to $(PREFIX)
#
# Variables:
#   CC       - C compiler (default: gcc)
#   PREFIX   - Installation prefix (default: /usr/local)

# Compiler and flags
CC ?= gcc
CFLAGS = -Wall -Wextra -O2

# Installation directory
PREFIX ?= /usr/local
```

## 特殊目标

- 对非文件目标使用 `.PHONY`
- 使用 `.PRECIOUS` 保存中间文件
- 使用 `.INTERMEDIATE` 将文件标记为中间文件（自动删除）
- 使用 `.SECONDARY` 防止删除中间文件
- 如果配方失败，请使用 `.DELETE_ON_ERROR` 删除目标
- 使用 `.SILENT` 抑制所有配方的回显（谨慎使用）

```makefile
# Don't delete intermediate files
.SECONDARY:

# Delete targets if recipe fails
.DELETE_ON_ERROR:

# Preserve specific files
.PRECIOUS: %.o
```

## 常见模式

### 标准项目结构

```makefile
CC = gcc
CFLAGS = -Wall -O2
objects = main.o utils.o parser.o

.PHONY: all clean install

all: program

program: $(objects)
	$(CC) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	-rm -f program $(objects)

install: program
	install -d $(PREFIX)/bin
	install -m 755 program $(PREFIX)/bin
```

### 管理多个程序

```makefile
programs = prog1 prog2 prog3

.PHONY: all clean

all: $(programs)

prog1: prog1.o common.o
	$(CC) -o $@ $^

prog2: prog2.o common.o
	$(CC) -o $@ $^

prog3: prog3.o
	$(CC) -o $@ $^

clean:
	-rm -f $(programs) *.o
```

## 要避免的反模式

- 不要以空格而不是制表符开始食谱行
- 当可以使用通配符或函数生成文件列表时，避免对其进行硬编码
- 不要使用 `$(shell ls ...)` 来获取文件列表（使用 `$(wildcard ...)` 代替）
- 避免配方中出现复杂的 shell 脚本（移至单独的脚本文件）
- 不要忘记将虚假目标声明为 `.PHONY`
- 避免目标之间的循环依赖
- 除非绝对必要，否则不要使用递归 make (`$(MAKE) -C subdir`)
