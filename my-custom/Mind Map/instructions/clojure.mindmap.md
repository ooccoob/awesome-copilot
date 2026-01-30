## What/When/Why/How

- What: Clojure REPL 优先的交互式开发规范：Calva 工具、结构化编辑、RCF、测试与命名、内联 def 调试。
- When: 需要快速验证/迭代/文档化用法、或修复 bracket/缩进问题时。
- Why: REPL 驱动减少猜测，保持可验证与可回溯；结构化编辑避免括号错配。
- How: 始终在已有 REPL 中评估；对齐/缩进守恒；先 REPL 再落文件；以 RCF 记录示例；谨慎 stdin；避免遮蔽内建符号。

## Key Points

- REPL: 不新开 REPL；用 Calva Evaluate；JSON 参数不过度转义。
- Docstrings: 在 defn 名称后、参数向量前；函数先定义再使用。
- 对齐: 向量/映射/列表多行竖直对齐，帮助括号平衡。
- 依赖: clojure.repl.deps/add-libs 动态引库(1.12+)。
- 结构编辑: 顶层表单插入/替换等工具；编辑后 (require 'ns :reload)。
- Inline def: 偏好内联 def 便于检查中间状态；返回值优于打印。
- 数据结构: 扁平化+命名空间关键字；参数列表直接解构；避免遮蔽核心函数。
- 测试: 在 REPL 运行 clojure.test；命名与断言信息清晰；testing 仅用于分组。
- RCF: (comment ...) 记录已验证用法与边界示例。

## Compact Map

- REPL-First → 校验后落盘
- Indent/Align → 括号平衡
- Inline def → 快速调试
- RCF → 用法文档
- Tests → REPL 运行/命名清晰
- Avoid Shadowing → 关键内建符号

## Example Questions (10+)

1) Calva REPL 工具的 JSON 参数如何正确转义？
2) defn 的 docstring 放置规则与用途？
3) 多行向量/映射怎样对齐避免括号错位？
4) 何时使用 add-libs 动态加载依赖？
5) :reload 的正确使用姿势？
6) 内联 def 与 println 相比的优势？
7) 避免遮蔽 core 符号的策略？
8) RCF 放哪些示例最有价值？
9) 测试断言消息与 testing 分组的取舍？
10) Babashka nREPL 与 stdin 的限制如何规避？
11) 结构化编辑工具的安全使用顺序？

---
Source: d:\mycode\awesome-copilot\instructions\clojure.instructions.md | Generated: 2025-10-17
