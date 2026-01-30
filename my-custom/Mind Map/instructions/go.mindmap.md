## What/When/Why/How
- What: Go 代码风格/架构/并发/错误处理/HTTP 客户端与 I/O 指南
- When: 编写/评审 Go 代码，设计包结构与并发模型时
- Why: 可读、可测、无竞态、零值友好，避免常见陷阱
- How: idiomatic Go；包命名与导出约定；INPC 无；早返回；上下文优先

## Key Points
- 命名: 包小写单词；避免 util/common；导出用大写首字母
- 结构: cmd/pkg/internal；避免循环依赖；最小化模块
- 错误: 立刻检查；fmt.Errorf("...: %w", err) 包装；errors.Is/As
- 并发: 明确退出路径；WaitGroup/通道；避免泄漏；select 非阻塞
- 同步: Mutex/RWMutex 小临界区；Once 初始化
- HTTP 客户端: 每次调用构造请求；不要在 client 存 per-request 状态；关闭 Body
- I/O: Reader 一次性；需多次读取则缓存到 []byte 并重建 Reader；Pipe 严格顺序写入
- JSON/API: 结构体 tag；指针表示可选；校验输入
- 测试: 表驱动；t.Helper/t.Cleanup；白盒/黑盒
- 性能: 预分配 slice；strings.Builder；sync.Pool；先分析再优化

## Compact Map
命名→结构→错误→并发→同步→HTTP→I/O→JSON→测试→性能

## Example Questions (10+)
1) 生成一个 cmd/app 与 internal 包的项目骨架
2) 设计 HTTP 客户端封装，避免请求状态泄漏
3) 使用 context 控制超时与取消的示例
4) Reader 复读方案：缓存为 []byte 并重建 reader
5) io.Pipe 串流 multipart 的正确用法与注意事项
6) 错误包装与统一返回策略
7) 使用 ServeMux(Go>=1.22) 的路由示例
8) 表驱动单测与 t.Helper 的使用
9) Goroutine 泄漏的排查与修复
10) 大量字符串拼接的性能优化（strings.Builder）

Source: d:\mycode\awesome-copilot\instructions\go.instructions.md | Generated: 2025-10-17T00:00:00Z
