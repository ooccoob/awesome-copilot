```instructions
---
description: '编写 Go 代码时遵循惯用 Go 实践和社区标准的指令'
applyTo: '**/*.go,**/go.mod,**/go.sum'
---

# Go 开发指令

编写 Go 代码时请遵循惯用 Go 实践和社区标准。以下内容参考 [Effective Go](https://go.dev/doc/effective_go)、[Go Code Review Comments](https://go.dev/wiki/CodeReviewComments) 和 [Google Go Style Guide](https://google.github.io/styleguide/go/)。

## 通用指令
- 编写简单、清晰、惯用的 Go 代码
- 优先考虑清晰和简洁，避免炫技
- 遵循“最小惊讶原则”
- 保持主流程左对齐（减少缩进）
- 及早返回，减少嵌套
- 让零值有意义
- 为导出类型、函数、方法和包写文档
- 用 Go modules 管理依赖

## 命名规范
### 包
- 包名用小写单词
- 避免下划线、连字符或混合大小写
- 名称应描述包的功能而非内容
- 避免通用名如 util、common、base
- 包名用单数

### 变量与函数
- 用 camelCase 或 MixedCaps，避免下划线
- 名字简短但具描述性
- 单字母变量仅用于极短作用域（如循环）
- 导出名首字母大写，未导出名小写
- 避免重复（如 http.HTTPServer，推荐 http.Server）

### 接口
- 尽量用 -er 结尾（如 Reader、Writer、Formatter）
- 单方法接口用方法名（如 Read → Reader）
- 接口应小而专注

### 常量
- 导出常量用 MixedCaps，未导出用 mixedCaps
- 用 const 块分组相关常量
- 建议用类型常量提升类型安全

## 代码风格与格式化
### 格式化
- 必须用 gofmt 格式化代码
- 用 goimports 自动管理 import
- 行长适中，注重可读性
- 用空行分隔逻辑块

### 注释
- 注释用完整句子
- 以被描述对象名开头
- 包注释以“Package [name]”开头
- 多用行注释（//），块注释（/* */）仅用于包文档
- 注重“为什么”，除非“做什么”很复杂

### 错误处理
- 函数调用后立即检查错误
- 除非有充分理由（需注释），不要用 _ 忽略错误
- 用 fmt.Errorf + %w 包装错误
- 需特定错误判断时自定义错误类型
- 错误返回值放最后，变量名用 err
- 错误信息小写且不加标点

## 架构与项目结构
### 包组织
- 遵循标准 Go 项目结构
- main 包放在 cmd/ 目录
- 可复用包放 pkg/ 或 internal/
- internal/ 用于不对外暴露的包
- 相关功能归为一包，避免循环依赖

### 依赖管理
- 用 Go modules（go.mod/go.sum）
- 依赖尽量精简
- 定期更新依赖修复安全问题
- 用 go mod tidy 清理无用依赖
- 必要时才 vendor 依赖

## 类型安全与语言特性
### 类型定义
- 定义类型提升语义和类型安全
- 用 struct tag 做 JSON/XML/数据库映射
- 优先显式类型转换
- 类型断言要检查第二返回值

### 指针与值
- 大 struct 或需修改 receiver 用指针
- 小 struct 或需不可变用值
- 同一类型方法集保持一致
- 选指针/值 receiver 时考虑零值

### 接口与组合
- 接收接口，返回具体类型
- 接口应小（1-3 方法最佳）
- 用嵌入实现组合
- 接口定义应靠近使用处
- 非必要不导出接口

## 并发
### 协程
- 库中不主动创建 goroutine，由调用方控制
- 明确 goroutine 退出方式
- 用 sync.WaitGroup 或 channel 等待 goroutine
- 防 goroutine 泄漏，确保清理

### 通道
- 用 channel 进行 goroutine 间通信
- 不要通过共享内存通信，应通过通信共享内存
- 只由发送方关闭 channel
- 已知容量时用缓冲 channel
- 非阻塞操作用 select

### 同步
- 用 sync.Mutex 保护共享状态
- 临界区尽量小
- 多读场景用 sync.RWMutex
- 能用 channel 就不用锁
- 用 sync.Once 做一次性初始化

## 错误处理模式
### 创建错误
- 静态错误用 errors.New
- 动态错误用 fmt.Errorf
- 领域错误用自定义类型
- 导出错误变量做哨兵错误
- 用 errors.Is/As 判断错误

### 错误传递
- 向上传递错误时加上下文
- 不要既 log 又 return 错误（二选一）
- 在合适层级处理错误
- 复杂调试可用结构化错误

## API 设计
### HTTP 处理器
- 简单处理器用 http.HandlerFunc
- 需状态的实现 http.Handler
- 横切关注用中间件
- 设置合适状态码和 header
- 错误友好处理并返回合适响应

### JSON API
- 用 struct tag 控制 JSON 编解码
- 校验输入数据
- 可选字段用指针
- 复杂场景用 json.RawMessage 延迟解析
- 妥善处理 JSON 错误

## 性能优化
### 内存管理
- 热路径减少分配
- 复用对象（如 sync.Pool）
- 小 struct 用值 receiver
- 已知长度的 slice 预分配
- 避免不必要的字符串转换

### 性能分析
- 用内置 pprof 工具
- 对关键路径做基准测试
- 优先算法优化
- 用 testing.B 做基准

## 测试
### 测试组织
- 白盒测试与被测代码同包
- 黑盒测试用 _test 包后缀
- 测试文件以 _test.go 结尾
- 测试文件与被测代码同目录

### 编写测试
- 多用表驱动测试
- 测试命名用 Test_函数名_场景
- 用 t.Run 做子测试
- 覆盖成功和错误场景
- 谨慎使用 testify 等库

### 测试辅助
- 辅助函数加 t.Helper()
- 复杂场景用测试夹具
- 测试/基准用 testing.TB
- 用 t.Cleanup 清理资源

## 安全最佳实践
### 输入校验
- 校验所有外部输入
- 强类型防止非法状态
- SQL 前先清理数据
- 用户输入的文件路径需谨慎
- 针对不同场景（HTML/SQL/shell）做转义

### 加密
- 用标准库 crypto 包
- 不要自造加密算法
- 随机数用 crypto/rand
- 密码用 bcrypt 等存储
- 网络通信用 TLS

## 文档
### 代码文档
- 所有导出符号都要注释
- 注释以符号名开头
- 必要时加示例
- 文档紧贴代码
- 代码变更及时更新文档

### README 与文档文件
- 提供清晰的安装说明
- 记录依赖和要求
- 提供用例
- 记录配置项
- 加入故障排查

## 工具与开发流程
### 常用工具
- go fmt：格式化
- go vet：可疑代码检查
- golint/golangci-lint：额外 lint
- go test：测试
- go mod：依赖管理
- go generate：代码生成

### 开发实践
- 提交前先跑测试
- 用 pre-commit 钩子做格式化和 lint
- 保持提交原子且聚焦
- 写有意义的提交信息
- 提交前审查 diff

## 常见陷阱
- 不检查错误
- 忽略竞态
- goroutine 泄漏
- 忘用 defer 清理
- 并发修改 map
- 不理解 nil interface 与 nil 指针
- 忘记关闭资源（文件、连接）
- 不必要用全局变量
- 滥用空接口（interface{}）
- 忽略类型零值

---

> 本文件为自动翻译，仅供参考。如有歧义请以英文原文为准。
```
