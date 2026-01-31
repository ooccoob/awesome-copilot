---
描述：“Clojure 特定的编码模式、内联 def 用法、代码块模板和 Clojure 开发的命名空间处理。”
applyTo: '**/*.{clj,cljs,cljc,bb,edn.mdx?}'
---

# Clojure 开发说明

## 代码评估工具的使用

“使用 repl”意味着使用 Calva Backseat Driver 的 **Evaluate Clojure Code** 工具。它将您连接到与用户通过 Calva 连接到的相同 REPL。

- 始终留在 Calva 的 REPL 内，而不是从终端启动第二个 REPL。
- 如果没有 REPL 连接，请要求用户连接 REPL，而不是尝试自己启动并连接它。

### REPL 工具调用中的 JSON 字符串
调用 REPL 工具时不要过度转义 JSON 参数。

```json
{
  "namespace": "<current-namespace>",
  "replSessionKey": "cljs",
  "code": "(def foo \"something something\")"
}
```

## `defn` 中的文档字符串
文档字符串紧接在函数名称之后和参数向量之前。

```clojure
(defn my-function
  "This function does something."
  [arg1 arg2]
  ;; function body
  )
```

- 在使用之前定义函数——除非确实有必要，否则优先使用 `declare` 进行排序。

## 交互式编程（又名 REPL 驱动开发）

### 对齐数据结构元素以实现括号平衡
**始终在所有数据结构中垂直对齐多行元素：向量、映射、列表、集合、所有代码（因为 Clojure 代码是数据）。未对准会导致括号平衡器错误地关闭括号，从而创建无效的表格。**

```clojure
;; ❌ Wrong - misaligned vector elements
(select-keys m [:key-a
                :key-b
               :key-c])  ; Misalignment → incorrect ] placement

;; ✅ Correct - aligned vector elements
(select-keys m [:key-a
                :key-b
                :key-c])  ; Proper alignment → correct ] placement

;; ❌ Wrong - misaligned map entries
{:name "Alice"
 :age 30
:city "Oslo"}  ; Misalignment → incorrect } placement

;; ✅ Correct - aligned map entries
{:name "Alice"
 :age 30
 :city "Oslo"}  ; Proper alignment → correct } placement
```

**关键**：支架平衡器依靠一致的压痕来确定结构。

### REPL 依赖管理
在 REPL 会话期间使用 `clojure.repl.deps/add-libs` 进行动态依赖项加载。

```clojure
(require '[clojure.repl.deps :refer [add-libs]])
(add-libs '{dk.ative/docjure {:mvn/version "1.15.0"}})
```

- 动态依赖加载需要 Clojure 1.12 或更高版本
- 非常适合图书馆探索和原型设计

### 检查 Clojure 版本

```clojure
*clojure-version*
;; => {:major 1, :minor 12, :incremental 1, :qualifier nil}
```

### REPL 可用性规则

**当 REPL 不可用时，切勿编辑代码文件。** 当 REPL 评估返回错误表明 REPL 不可用时，请立即停止并通知用户。让用户在继续之前恢复 REPL。

#### 为什么这很重要
- **交互式编程需要有效的 REPL** - 如果没有评估，您就无法验证行为
- **猜测会产生错误** - 未经测试而更改代码会引入错误

## 结构编辑和 REPL 优先习惯
- 在接触文件之前在 REPL 中进行更改。
- 编辑 Clojure 文件时，请始终使用结构编辑工具，例如 **插入顶级表单**、**替换顶级表单**、**创建 Clojure 文件**和 **附加代码**，并始终先阅读其说明。

### 创建新文件
- 使用带有初始内容的 **创建 Clojure 文件** 工具
- 遵循 Clojure 命名规则：名称空间采用 kebab-case 格式，文件路径采用匹配的 Snake_case 格式（例如 `my.project.ns` → `my/project/ns.clj`）。

### 重新加载命名空间
编辑文件后，在 REPL 中重新加载已编辑的命名空间，以便更新的定义处于活动状态。

```clojure
(require 'my.namespace :reload)
```

## 评估前的代码缩进
一致的压痕对于帮助支架平衡器至关重要。

```clojure
;; ❌
(defn my-function [x]
(+ x 2))

;; ✅
(defn my-function [x]
  (+ x 2))
```

## 缩进首选项

将条件和主体放在不同的行上：

```clojure
(when limit
  (println "Limit set to:" limit))
```

将 `and` 和 `or` 参数保留在不同的行上：

```clojure
(if (and condition-a
         condition-b)
  this
  that)
```

## 内联定义模式

优先使用内联 def 调试而不是 println/console.log。

### 用于调试的内联 `def`
- 内联 `def` 绑定在 REPL 工作期间保持中间状态可检查。
- 当内联绑定继续帮助探索时，将它们保留在适当的位置。

```clojure
(defn process-instructions [instructions]
  (def instructions instructions)
  (let [grouped (group-by :status instructions)]
    grouped))
```

- 实时检查保持可用。
- 调试周期保持快速。
- 迭代开发依然顺利。

在聊天中显示用户代码时，您还可以使用“内联定义”，以便用户可以轻松地在代码块中试验代码。用户可以使用 Calva 直接在代码块中评估代码。 （但用户无法在那里编辑代码。）

## 返回值 > 打印副作用

更喜欢使用 REPL 并从评估中返回值，而不是将内容打印到标准输出。

## 从 `stdin` 读取
- 当 Clojure 代码使用 `(read-line)` 时，它会通过 VS Code 提示用户。
- 避免在 Babashka 的 nREPL 中读取标准输入，因为它缺乏标准输入支持。
- 如果 REPL 阻塞，请用户重新启动它。

## 数据结构首选项

我们尝试使数据结构尽可能平坦，严重依赖命名空间关键字并进行优化以轻松解构。通常，在应用程序中，我们使用命名空间关键字，并且最常见的是“合成”命名空间。

直接在参数列表中解构键。

```clojure
(defn handle-user-request
  [{:user/keys [id name email]
    :request/keys [method path headers]
    :config/keys [timeout debug?]}]
  (when debug?
    (println "Processing" method path "for" name)))
```

这有很多好处，其中之一是使函数签名保持透明。

### 避免内置阴影
必要时重命名传入的键以避免隐藏核心功能。

```clojure
(defn create-item
  [{:prompt-sync.file/keys [path uri]
    file-name :prompt-sync.file/name
    file-type :prompt-sync.file/type}]
  #js {:label file-name
       :type file-type})
```

保持免费的常用符号：
- __代码0__
- __代码0__
- __代码0__
- __代码0__
- __代码0__
- __代码0__
- __代码0__
- __代码0__
- __代码0__
- __代码0__
- __代码0__
- __代码0__
- __代码0__
- __代码0__
- __代码0__
- __代码0__
- __代码0__
- __代码0__

## 避免不必要的包装函数
除非名称真正阐明了组成，否则不要包装核心功能。

```clojure
(remove (set exclusions) items) ; a wrapper function would not make this clearer
```

## 用于文档的丰富评论表 (RCF)

丰富注释表单 `(comment ...)` 的用途与直接 REPL 评估不同。在文件编辑中使用 RCF 来**记录已在 REPL 中验证的函数的使用模式和示例**。

### 何时使用 RCF
- **REPL 验证后** - 在文件中记录工作示例
- **使用文档** - 显示如何使用函数
- **探索保留** - 在代码库中保留有用的 REPL 发现
- **示例场景** - 演示边缘情况和典型用法

### RCF 模式
RCF = 丰富的评论表格。

当文件加载时，RCF 中的代码不会被评估，这使得它们非常适合记录示例用法，因为人们可以轻松地随意评估其中的代码。

```clojure
(defn process-user-data
  "Processes user data with validation"
  [{:user/keys [name email] :as user-data}]
  ;; implementation here
  )

(comment
  ;; Basic usage
  (process-user-data {:user/name "John" :user/email "john@example.com"})

  ;; Edge case - missing email
  (process-user-data {:user/name "Jane"})

  ;; Integration example
  (->> users
       (map process-user-data)
       (filter :valid?))

  :rcf) ; Optional marker for end of comment block
```

### RCF 与 REPL 工具使用
```clojure
;; In chat - show direct REPL evaluation:
(in-ns 'my.namespace)
(let [test-data {:user/name "example"}]
  (process-user-data test-data))

;; In files - document with RCF:
(comment
  (process-user-data {:user/name "example"})
  :rcf)
```

## 测试

### 从 REPL 运行测试
重新加载目标命名空间并从 REPL 执行测试以获得即时反馈。

```clojure
(require '[my.project.some-test] :reload)
(clojure.test/run-tests 'my.project.some-test)
(cljs.test/run-tests 'my.project.some-test)
```

- 更紧密的 REPL 集成。
- 集中执行。
- 调试更简单。
- 直接访问测试数据。

在调查故障时，更喜欢从测试命名空间内运行单独的测试变量。

### 使用 REPL-First TDD 工作流程
在编辑文件之前使用真实数据进行迭代。

```clojure
(def sample-text "line 1\nline 2\nline 3\nline 4\nline 5")

(defn format-line-number [n padding marker-len]
  (let [num-str (str n)
        total-padding (- padding marker-len)]
    (str (apply str (repeat (- total-padding (count num-str)) " "))
         num-str)))

(deftest line-number-formatting
  (is (= "  5" (editor-util/format-line-number 5 3 0))
      "Single digit with padding 3, no marker space")
  (is (= " 42" (editor-util/format-line-number 42 3 0))
      "Double digit with padding 3, no marker space"))
```

#### 好处
- 提交更改之前验证行为
- 增量开发并立即反馈
- 捕获已知良好行为的测试
- 通过失败的测试开始新的工作以锁定意图

### 测试命名和消息传递
保持 `deftest` 名称具有描述性（区域/事物样式），没有多余的 `-test` 后缀。

### 测试断言消息样式
仅在对多个相关断言进行分组时才使用 `testing` 块，将期望消息直接附加到 `is`。

```clojure
(deftest line-marker-formatting
  (is (= "→" (editor-util/format-line-marker true))
      "Target line gets marker")
  (is (= "" (editor-util/format-line-marker false))
      "Non-target gets empty string"))

(deftest context-line-extraction
  (testing "Centered context extraction"
    (let [result (editor-util/get-context-lines "line 1\nline 2\nline 3" 2 3)]
      (is (= 3 (count (str/split-lines result)))
          "Should have 3 lines")
      (is (str/includes? result "→")
          "Should have marker"))))
```

指南：
- 保持断言消息明确地表达期望。
- 使用 `testing` 对相关检查进行分组。
- 保持短横线命名，例如 `line-marker-formatting` 或 `context-line-extraction`。

## 快乐互动编程

请记住在您的工作中更喜欢 REPL。请记住，用户看不到您的评价。也没有结果。在聊天中与用户交流您的评估和反馈。

