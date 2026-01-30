---
description: 'Clojure特定编码模式、内联def使用、代码块模板和Clojure开发的命名空间处理。'
applyTo: '**/*.{clj,cljs,cljc,bb,edn.mdx?}'
---

# Clojure开发指令

## 代码评估工具使用

"使用repl"意味着使用Calva Backseat Driver的**评估Clojure代码**工具。它将您连接到与用户通过Calva连接的相同REPL。

- 始终留在Calva的REPL内，而不是从终端启动第二个REPL。
- 如果没有REPL连接，要求用户连接REPL，而不是尝试自己启动和连接它。

### REPL工具调用中的JSON字符串
调用REPL工具时不要过度转义JSON参数。

```json
{
  "namespace": "<current-namespace>",
  "replSessionKey": "cljs",
  "code": "(def foo \"something something\")"
}
```

## `defn`中的文档字符串
文档字符串应紧跟在函数名之后，参数向量之前。

```clojure
(defn my-function
  "此函数执行某些操作。"
  [arg1 arg2]
  ;; 函数体
  )
```

- 在使用函数之前定义函数——优先使用排序而不是`declare`，除非真正必要。

## 交互式编程（也称REPL驱动开发）

### 对齐数据结构元素以实现括号平衡
**在所有数据结构中垂直对齐多行元素：向量、映射、列表、集合、所有代码（因为Clojure代码是数据）。不对齐会导致括号平衡器错误地关闭括号，创建无效的表单。**

```clojure
;; ❌ 错误 - 向量元素不对齐
(select-keys m [:key-a
                :key-b
               :key-c])  ; 不对齐 → 错误的 ] 放置

;; ✅ 正确 - 向量元素对齐
(select-keys m [:key-a
                :key-b
                :key-c])  ; 正确对齐 → 正确的 ] 放置

;; ❌ 错误 - 映射条目不对齐
{:name "Alice"
 :age 30
:city "Oslo"}  ; 不对齐 → 错误的 } 放置

;; ✅ 正确 - 映射条目对齐
{:name "Alice"
 :age 30
 :city "Oslo"}  ; 正确对齐 → 正确的 } 放置
```

**关键**：括号平衡器依赖一致的缩进来确定结构。

### REPL依赖管理
使用`clojure.repl.deps/add-libs`在REPL会话期间进行动态依赖加载。

```clojure
(require '[clojure.repl.deps :refer [add-libs]])
(add-libs '{dk.ative/docjure {:mvn/version "1.15.0"}})
```

- 动态依赖加载需要Clojure 1.12或更高版本
- 非常适合库探索和原型设计

### 检查Clojure版本

```clojure
*clojure-version*
;; => {:major 1, :minor 12, :incremental 1, :qualifier nil}
```

### REPL可用性纪律

**当REPL不可用时绝不编辑代码文件。**当REPL评估返回指示REPL不可用的错误时，立即停止并通知用户。让用户在继续之前恢复REPL。

#### 为什么这很重要
- **交互式编程需要工作的REPL** - 您无法通过评估来验证行为
- **猜测会产生错误** - 未经测试的代码更改会引入错误

## 结构化编辑和REPL优先习惯
- 在接触文件之前在REPL中开发更改。
- 编辑Clojure文件时，始终使用结构化编辑工具，如**插入顶级表单**、**替换顶级表单**、**创建Clojure文件**和**追加代码**，并且始终先阅读它们的说明。

### 创建新文件
- 使用**创建Clojure文件**工具配合初始内容
- 遵循Clojure命名规则：命名空间使用kebab-case，文件路径使用匹配的snake_case（例如`my.project.ns` → `my/project/ns.clj`）。

### 重新加载命名空间
编辑文件后，在REPL中重新加载编辑的命名空间，以便更新的定义处于活动状态。

```clojure
(require 'my.namespace :reload)
```

## 评估前的代码缩进
一致的缩进对于帮助括号平衡器至关重要。

```clojure
;; ❌
(defn my-function [x]
(+ x 2))

;; ✅
(defn my-function [x]
  (+ x 2))
```

## 缩进偏好

将条件和主体保持在单独的行上：

```clojure
(when limit
  (println "Limit set to:" limit))
```

将`and`和`or`参数保持在单独的行上：

```clojure
(if (and condition-a
         condition-b)
  this
  that)
```

## 内联Def模式

优先使用内联def调试而不是println/console.log。

### 用于调试的内联`def`
- 内联`def`绑定在REPL工作期间保持中间状态可检查。
- 当内联绑定继续有助于探索时，将它们留在原位。

```clojure
(defn process-instructions [instructions]
  (def instructions instructions)
  (let [grouped (group-by :status instructions)]
    grouped))
```

- 实时检查保持可用。
- 调试周期保持快速。
- 迭代开发保持平滑。

当在聊天中向用户展示代码时，您也可以使用"内联def"，使用户可以轻松地从代码块内试验代码。用户可以使用Calva直接在您的代码块中评估代码。（但用户无法在那里编辑代码。）

## 返回值 > 打印副作用

优先使用REPL和评估的返回值，而不是向stdout打印内容。

## 从`stdin`读取
- 当Clojure代码使用`(read-line)`时，它将通过VS Code提示用户。
- 避免在Babashka的nREPL中进行stdin读取，因为它缺乏stdin支持。
- 如果REPL阻塞，要求用户重启REPL。

## 数据结构偏好

我们尽量保持数据结构尽可能扁平，大量依赖命名空间关键字并优化为易于解构。通常在应用程序中我们使用命名空间关键字，最常见的是"合成"命名空间。

直接在参数列表中解构键。

```clojure
(defn handle-user-request
  [{:user/keys [id name email]
    :request/keys [method path headers]
    :config/keys [timeout debug?]}]
  (when debug?
    (println "Processing" method path "for" name)))
```

除许多好处外，这还保持函数签名透明。

### 避免隐藏内置函数
必要时重命名传入键以避免隐藏核心函数。

```clojure
(defn create-item
  [{:prompt-sync.file/keys [path uri]
    file-name :prompt-sync.file/name
    file-type :prompt-sync.file/type}]
  #js {:label file-name
       :type file-type})
```

要保持空闲的常见符号：
- `class`
- `count`
- `empty?`
- `filter`
- `first`
- `get`
- `key`
- `keyword`
- `map`
- `merge`
- `name`
- `reduce`
- `rest`
- `set`
- `str`
- `symbol`
- `type`
- `update`

## 避免不必要的包装函数
除非名称真正阐明组合，否则不要包装核心函数。

```clojure
(remove (set exclusions) items) ; 包装函数不会使这更清晰
```

## 用于文档的丰富注释表单（RCF）

丰富注释表单`(comment ...)`与直接REPL评估有不同的目的。在文件编辑中使用RCF来**记录您已在REPL中验证的函数的使用模式和示例**。

### 何时使用RCF
- **REPL验证后** - 在文件中记录工作示例
- **使用文档** - 显示函数的预期使用方式
- **探索保留** - 在代码库中保留有用的REPL发现
- **示例场景** - 演示边界情况和典型用法

### RCF模式
RCF = 丰富注释表单。

当加载文件时，RCF中的代码不会被评估，这使它们非常适合记录示例用法，因为人类可以随时轻松评估其中的代码。

```clojure
(defn process-user-data
  "处理带有验证的用户数据"
  [{:user/keys [name email] :as user-data}]
  ;; 此处实现
  )

(comment
  ;; 基本用法
  (process-user-data {:user/name "John" :user/email "john@example.com"})

  ;; 边界情况 - 缺少邮箱
  (process-user-data {:user/name "Jane"})

  ;; 集成示例
  (->> users
       (map process-user-data)
       (filter :valid?))

  :rcf) ; 注释块结束的可选标记
```

### RCF vs REPL工具使用
```clojure
;; 在聊天中 - 显示直接REPL评估：
(in-ns 'my.namespace)
(let [test-data {:user/name "example"}]
  (process-user-data test-data))

;; 在文件中 - 使用RCF记录：
(comment
  (process-user-data {:user/name "example"})
  :rcf)
```

## 测试

### 从REPL运行测试
重新加载目标命名空间并从REPL执行测试以获得即时反馈。

```clojure
(require '[my.project.some-test] :reload)
(clojure.test/run-tests 'my.project.some-test)
(cljs.test/run-tests 'my.project.some-test)
```

- 更紧密的REPL集成。
- 专注执行。
- 更简单的调试。
- 直接访问测试数据。

在调查失败时，优先从测试命名空间内运行单个测试变量。

### 使用REPL优先TDD工作流
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
      "填充为3的单位数，无标记空间")
  (is (= " 42" (editor-util/format-line-number 42 3 0))
      "填充为3的双位数，无标记空间"))
```

#### 好处
- 在提交更改之前验证行为
- 具有即时反馈的增量开发
- 捕获已知良好行为的测试
- 使用失败的测试开始新工作以锁定意图

### 测试命名和消息传递
保持`deftest`名称具有描述性（区域/事物风格），没有冗余的`-test`后缀。

### 测试断言消息样式
将期望消息直接附加到`is`，仅在分组多个相关断言时使用`testing`块。

```clojure
(deftest line-marker-formatting
  (is (= "→" (editor-util/format-line-marker true))
      "目标行获得标记")
  (is (= "" (editor-util/format-line-marker false))
      "非目标获得空字符串"))

(deftest context-line-extraction
  (testing "中心上下文提取"
    (let [result (editor-util/get-context-lines "line 1\nline 2\nline 3" 2 3)]
      (is (= 3 (count (str/split-lines result)))
          "应该有3行")
      (is (str/includes? result "→")
          "应该有标记"))))
```

指导原则：
- 保持断言消息明确期望。
- 使用`testing`对相关检查进行分组。
- 保持kebab-case名称，如`line-marker-formatting`或`context-line-extraction`。

## 快乐的交互式编程

记得在您的工作中优先使用REPL。请记住用户看不到您评估什么。也看不到结果。在聊天中与用户沟通您评估什么以及您得到什么结果。