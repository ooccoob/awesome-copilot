---
适用于：'*'
描述：“最全面、最实用、由工程师编写的针对所有语言、框架和堆栈的性能优化说明。涵盖前端、后端和数据库最佳实践，以及可操作的指导、基于场景的清单、故障排除和专业提示。
---

# 性能优化最佳实践

## 简介

性能不仅仅是一个流行词——它是人们喜爱的产品和他们放弃的产品之间的区别。我亲眼目睹了缓慢的应用程序如何让用户感到沮丧、增加云费用，甚至失去客户。本指南是我使用和审查过的最有效、最真实的性能实践的生动集合，涵盖前端、后端和数据库层以及高级主题。将其用作构建快速、高效和可扩展软件的参考、清单和灵感来源。

---

## 一般原则

- **首先测量，其次优化：** 在优化之前始终进行分析和测量。使用基准测试、分析器和监控工具来识别真正的瓶颈。猜测是绩效的敌人。
  - *专业提示：* 使用 Chrome DevTools、Lighthouse、New Relic、Datadog、Py-Spy 等工具或您语言的内置分析器。
- **针对常见情况进行优化：** 重点优化最常执行的代码路径。不要在罕见的边缘情况上浪费时间，除非它们很关键。
- **避免过早优化：** 首先编写清晰、可维护的代码；仅在必要时进行优化。过早的优化会使代码更难阅读和维护。
- **最大限度地减少资源使用：**有效地使用内存、CPU、网络和磁盘资源。总是问：“这可以用更少的钱完成吗？”
- **更喜欢简单性：**简单的算法和数据结构通常更快、更容易优化。不要过度设计。
- **记录性能假设：** 清楚地注释任何对性能至关重要或具有不明显优化的代码。未来的维护者（包括您）会感谢您。
- **了解平台：**了解您的语言、框架和运行时的性能特征。 Python 中快的东西在 JavaScript 中可能会慢，反之亦然。
- **自动化性能测试：** 将性能测试和基准测试集成到您的 CI/CD 管道中。尽早发现回归现象。
- **设置性能预算：** 定义加载时间、内存使用、API 延迟等可接受的限制。通过自动检查强制执行。

---

## 前端性能

### 渲染和 DOM
- **最小化 DOM 操作：** 尽可能批量更新。频繁的 DOM 更改是昂贵的。
  - *反模式：* 循环更新 DOM。相反，构建一个文档片段并追加一次。
- **虚拟 DOM 框架：** 高效使用 React、Vue 或类似框架 — 避免不必要的重新渲染。
  - *React 示例：* 使用 `React.memo`、`useMemo` 和 `useCallback` 来防止不必要的渲染。
- **列表中的键：**始终在列表中使用稳定的键来帮助虚拟 DOM 比较。除非列表是静态的，否则避免使用数组索引作为键。
- **避免内联样式：**内联样式可能会触发布局抖动。更喜欢 CSS 类。
- **CSS 动画：** 通过 JavaScript 使用 CSS 过渡/动画，以获得更流畅、GPU 加速的效果。
- **推迟非关键渲染：** 使用 `requestIdleCallback` 或类似的方法推迟工作，直到浏览器空闲。

### 资产优化
- **图像压缩：** 使用 ImageOptim、Squoosh 或 TinyPNG 等工具。更喜欢现代格式（WebP、AVIF）进行网络交付。
- **用于图标的 SVG：** 对于简单图形，SVG 具有良好的缩放性，并且通常比 PNG 小。
- **缩小和捆绑：** 使用 Webpack、Rollup 或 esbuild 捆绑和缩小 JS/CSS。启用树摇动以删除死代码。
- **缓存标头：** 为静态资源设置长期缓存标头。使用缓存清除进行更新。
- **延迟加载：** 对图像使用 `loading="lazy"`，对 JS 模块/组件使用动态导入。
- **字体优化：** 仅使用您需要的字符集。对字体进行子集化并使用 `font-display: swap`。

### 网络优化
- **减少 HTTP 请求：** 合并文件、使用图像精灵和内联关键 CSS。
- **HTTP/2 和 HTTP/3：** 启用这些协议以进行复用并降低延迟。
- **客户端缓存：** 使用 Service Workers、IndexedDB 和 localStorage 进行离线和重复访问。
- **CDN：** 从靠近用户的 CDN 提供静态资产。使用多个 CDN 来实现冗余。
- **延迟/异步脚本：** 对于非关键 JS 使用 `defer` 或 `async` 以避免阻塞渲染。
- **预加载和预取：** 对关键资源使用 `<link rel="preload">` 和 `<link rel="prefetch">`。

### JavaScript 性能
- **避免阻塞主线程：** 将繁重的计算卸载给 Web Workers。
- **去抖动/限制事件：** 对于滚动、调整大小和输入事件，使用去抖动/限制来限制处理程序频率。
- **内存泄漏：** 清理事件监听器、间隔和 DOM 引用。使用浏览器开发工具检查分离的节点。
- **高效的数据结构：** 使用映射/集进行查找，使用 TypedArray 进行数值数据。
- **避免全局变量：** 全局变量可能导致内存泄漏和不可预测的性能。
- **避免深度对象克隆：** 仅在必要时使用浅拷贝或像 lodash 的 `cloneDeep` 这样的库。

### 辅助功能和性能
- **可访问组件：** 确保 ARIA 更新不过多。使用语义 HTML 来实现可访问性和性能。
- **屏幕阅读器性能：** 避免快速 DOM 更新，以免压倒辅助技术。

### 特定于框架的技巧
#### 反应
- 使用 `React.memo`、`useMemo` 和 `useCallback` 以避免不必要的渲染。
- 拆分大型组件并使用代码拆分（`React.lazy`、`Suspense`）。
- 避免渲染中的匿名函数；他们在每次渲染时都会创建新的参考。
- 使用 `ErrorBoundary` 优雅地捕获和处理错误。
- 使用 React DevTools Profiler 进行分析。

#### 角
- 对不需要频繁更新的组件使用 OnPush 更改检测。
- 避免模​​板中出现复杂的表达式；将逻辑移至组件类。
- 在 `ngFor` 中使用 `trackBy` 可以实现高效的列表渲染。
- 使用 Angular Router 延迟加载模块和组件。
- 使用 Angular DevTools 进行配置文件。

#### 维埃
- 在模板中的方法上使用计算属性进行缓存。
- 适当使用 `v-show` 与 `v-if` （`v-show` 更适合频繁切换可见性）。
- 使用 Vue Router 延迟加载组件和路由。
- 使用 Vue Devtools 进行配置。

### 常见的前端陷阱
- 在初始页面加载时加载大型 JS 包。
- 不压缩图像或使用过时的格式。
- 未能清理事件监听器，导致内存泄漏。
- 过度使用第三方库来完成简单的任务。
- 忽略移动性能（在真实设备上测试！）。

### 前端故障排除
- 使用 Chrome DevTools 的“性能”选项卡来记录和分析慢帧。
- 使用 Lighthouse 审核绩效并获取可行的建议。
- 使用 WebPageTest 进行实际负载测试。
- 监控核心 Web 生命体（LCP、FID、CLS）以获取以用户为中心的指标。

---

## 后端性能

### 算法与数据结构优化
- **选择正确的数据结构：** 用于顺序访问的数组、用于快速查找的哈希图、用于分层数据的树等。
- **高效算法：** 在适当的情况下使用二分搜索、快速排序或基于哈希的算法。
- **避免 O(n^2) 或更糟：** 配置文件嵌套循环和递归调用。重构以降低复杂性。
- **批处理：**批量处理数据以减少开销（例如批量数据库插入）。
- **流式传输：** 对大型数据集使用流式 API 以避免将所有内容加载到内存中。

### 并发和并行
- **异步 I/O：** 使用 async/await、回调或事件循环来避免阻塞线程。
- **线程/工作池：** 使用池来管理并发并避免资源耗尽。
- **避免竞争条件：** 在需要时使用锁、信号量或原子操作。
- **批量操作：**批量网络/数据库调用以减少往返。
- **反压：** 在队列和管道中实施反压以避免过载。

### 缓存
- **缓存昂贵的计算：**使用内存缓存（Redis、Memcached）来存储热数据。
- **缓存失效：** 使用基于时间 (TTL)、基于事件或手动失效。过时的缓存比没有缓存更糟糕。
- **分布式缓存：** 对于多服务器设置，请使用分布式缓存并注意一致性问题。
- **缓存踩踏保护：** 使用锁或请求合并来防止雷群问题。
- **不要缓存所有内容：** 有些数据太不稳定或太敏感而无法缓存。

### API和网络
- **最小化有效负载：**使用 JSON，压缩响应（gzip、Brotli），并避免发送不必要的数据。
- **分页：** 始终对大型结果集进行分页。使用游标获取实时数据。
- **速率限制：** 保护 API 免遭滥用和过载。
- **连接池：** 重用数据库和外部服务的连接。
- **协议选择：** 使用 HTTP/2、gRPC 或 WebSocket 进行高吞吐量、低延迟通信。

### 记录和监控
- **最大限度地减少热路径中的日志记录：** 过多的日志记录会减慢关键代码的速度。
- **结构化日志记录：** 使用 JSON 或键值日志更容易解析和分析。
- **监控一切：** 延迟、吞吐量、错误率、资源使用情况。使用 Prometheus、Grafana、Datadog 或类似工具。
- **警报：** 设置性能下降和资源耗尽警报。

### 特定于语言/框架的技巧
#### Node.js
- 使用异步API；避免阻塞事件循环（例如，永远不要在生产中使用 `fs.readFileSync` ）。
- 使用集群或工作线程来执行 CPU 密集型任务。
- 限制并发打开连接以避免资源耗尽。
- 使用流进行大文件或网络数据处理。
- 使用 `clinic.js`、`node --inspect` 或 Chrome DevTools 进行配置文件。

#### 蟒蛇
- 使用内置数据结构（`dict`、`set`、`deque`）来提高速度。
- 使用 `cProfile`、`line_profiler` 或 `Py-Spy` 进行配置文件。
- 使用 `multiprocessing` 或 `asyncio` 实现并行性。
- 避免 CPU 密集型代码中的 GIL 瓶颈；使用 C 扩展或子进程。
- 使用 `lru_cache` 进行记忆。

#### 爪哇
- 使用高效的集合（`ArrayList`、`HashMap` 等）。
- 使用 VisualVM、JProfiler 或 YourKit 进行分析。
- 使用线程池 (`Executors`) 实现并发。
- 调整堆和垃圾收集的 JVM 选项（`-Xmx`、`-Xms`、`-XX:+UseG1GC`）。
- 使用 `CompletableFuture` 进行异步编程。

#### .NET
- 使用 `async/await` 进行 I/O 密集型操作。
- 使用 `Span<T>` 和 `Memory<T>` 进行高效的内存访问。
- 使用 dotTrace、Visual Studio Profiler 或 PerfView 进行分析。
- 在适当的情况下池化对象和连接。
- 使用 `IAsyncEnumerable<T>` 来传输数据。

### 常见的后端陷阱
- Web 服务器中的同步/阻塞 I/O。
- 不使用数据库连接池。
- 过度缓存或缓存敏感/易失数据。
- 忽略异步代码中的错误处理。
- 不监控性能下降或发出警报。

### 后端故障排除
- 使用火焰图可视化 CPU 使用情况。
- 使用分布式跟踪（OpenTelemetry、Jaeger、Zipkin）来跟踪跨服务的请求延迟。
- 使用堆转储和内存分析器来查找泄漏。
- 记录慢速查询和 API 调用以进行分析。

---

## 数据库性能

### 查询优化
- **索引：** 在经常查询、过滤或连接的列上使用索引。监视索引使用情况并删除未使用的索引。
- **避免 SELECT *:** 仅选择您需要的列。减少 I/O 和内存使用。
- **参数化查询：** 防止 SQL 注入并改进计划缓存。
- **查询计划：**分析和优化查询执行计划。在 SQL 数据库中使用 `EXPLAIN`。
- **避免 N+1 查询：** 使用联接或批量查询来避免循环中的重复查询。
- **限制结果集：** 对大型表使用 `LIMIT`/`OFFSET` 或游标。

### 架构设计
- **标准化：** 标准化以减少冗余，但如果需要，则针对读取繁重的工作负载进行非标准化。
- **数据类型：** 使用最有效的数据类型并设置适当的约束。
- **分区：** 对大型表进行分区以实现可扩展性和可管理性。
- **归档：**定期归档或清除旧数据，以保持表小而快。
- **外键：** 使用它们来保证数据完整性，但要注意高写入场景中的性能权衡。

### 交易
- **短事务：** 保持事务尽可能短以减少锁争用。
- **隔离级别：** 使用满足一致性需求的最低隔离级别。
- **避免长时间运行的事务：** 它们会阻塞其他操作并增加死锁。

### 缓存和复制
- **只读副本：** 用于扩展读取繁重的工作负载。监控复制延迟。
- **缓存查询结果：** 使用 Redis 或 Memcached 进行频繁访问的查询。
- **直写式/后写式：** 根据您的一致性需求选择正确的策略。
- **分片：** 将数据分布在多个服务器上以实现可扩展性。

### NoSQL 数据库
- **针对访问模式进行设计：** 针对您需要的查询对数据进行建模。
- **避免热分区：**均匀分布写入/读取。
- **无界增长：** 观察无界数组或文档。
- **分片和复制：** 用于可扩展性和可用性。
- **一致性模型：**了解最终一致性与强一致性并进行适当选择。

### 常见的数据库陷阱
- 缺少或未使用的索引。
- 在生产查询中选择 *。
- 不监控慢速查询。
- 忽略复制滞后。
- 不归档旧数据。

### 数据库故障排除
- 使用慢查询日志来识别瓶颈。
- 使用 `EXPLAIN` 分析查询计划。
- 监控缓存命中/未命中率。
- 使用特定于数据库的监控工具（pg_stat_statements、MySQL Performance Schema）。

---

## 性能代码审查清单

- [ ] 是否存在任何明显的算法效率低下（O(n^2) 或更糟）？
- [ ] 数据结构适合它们的使用吗？
- [ ] 是否存在不必要的计算或重复工作？
- [ ] 是否在适当的地方使用了缓存，并且是否正确处理了失效？
- [ ] 数据库查询是否经过优化、索引且没有 N+1 问题？
- [ ] 大型有效负载是否分页、流式传输或分块？
- [ ] 是否存在内存泄漏或无限制的资源使用？
- [ ] 网络请求是否被最小化、批量化并在失败时重试？
- [ ] 资产是否得到优化、压缩和有效服务？
- [ ] 热路径中是否存在阻塞操作？
- [ ] 热路径中的日志记录是否已最小化且结构化？
- [ ] 是否对性能关键的代码路径进行了记录和测试？
- [ ] 是否有针对性能敏感代码的自动化测试或基准测试？
- [ ] 是否有性能回归警报？
- [ ] 是否存在任何反模式（例如 SELECT *、阻塞 I/O、全局变量）？

---

## 高级主题

### 分析和基准测试
- **分析器：** 使用特定于语言的分析器（Chrome DevTools、Py-Spy、VisualVM、dotTrace 等）来识别瓶颈。
- **微基准：** 为关键代码路径编写微基准。对于 Java，使用 `benchmark.js`、`pytest-benchmark` 或 JMH。
- **A/B 测试：** 通过 A/B 或金丝雀版本衡量优化的实际影响。
- **持续性能测试：** 将性能测试集成到 CI/CD 中。使用 k6、Gatrin 或 Locust 等工具。

### 内存管理
- **资源清理：** 始终及时释放资源（文件、套接字、数据库连接）。
- **对象池：**用于频繁创建/销毁的对象（例如数据库连接、线程）。
- **堆监控：** 监控堆使用情况和垃圾回收。根据您的工作负载调整 GC 设置。
- **内存泄漏：** 使用泄漏检测工具（Valgrind、LeakCanary、Chrome DevTools）。

### 可扩展性
- **水平扩展：**设计无状态服务，使用分片/分区和负载均衡器。
- **自动缩放：** 使用云自动缩放组并设置合理的阈值。
- **瓶颈分析：** 识别并解决单点故障。
- **分布式系统：** 使用幂等操作、重试和断路器。

### 安全性和性能
- **高效加密：** 使用硬件加速且维护良好的加密库。
- **验证：**有效验证输入；避免在热路径中使用正则表达式。
- **速率限制：** 防止 DoS 攻击而不伤害合法用户。

### 移动性能
- **启动时间：** 延迟加载功能，推迟繁重的工作，并最小化初始包大小。
- **图像/资产优化：** 使用响应式图像并压缩资产以获得移动带宽。
- **高效存储：** 使用 SQLite、Realm 或平台优化的存储。
- **分析：** 使用 Android Profiler、Instruments (iOS) 或 Firebase 性能监控。

### 云和无服务器
- **冷启动：**最大限度地减少依赖性并使功能保持温暖。
- **资源分配：** 调整无服务器功能的内存/CPU。
- **托管服务：** 使用托管缓存、队列和数据库来实现可扩展性。
- **成本优化：** 将云成本作为性能指标进行监控和优化。

---

## 实际例子

### 示例 1：在 JavaScript 中消除用户输入的抖动
```javascript
// BAD: Triggers API call on every keystroke
input.addEventListener('input', (e) => {
  fetch(`/search?q=${e.target.value}`);
});

// GOOD: Debounce API calls
let timeout;
input.addEventListener('input', (e) => {
  clearTimeout(timeout);
  timeout = setTimeout(() => {
    fetch(`/search?q=${e.target.value}`);
  }, 300);
});
```

### 示例2：高效的SQL查询
```sql
-- BAD: Selects all columns and does not use an index
SELECT * FROM users WHERE email = 'user@example.com';

-- GOOD: Selects only needed columns and uses an index
SELECT id, name FROM users WHERE email = 'user@example.com';
```

### 示例 3：在 Python 中缓存昂贵的计算
```python
# BAD: Recomputes result every time
result = expensive_function(x)

# GOOD: Cache result
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_function(x):
    ...
result = expensive_function(x)
```

### 示例 4：延迟加载 HTML 中的图像
```html
<!-- BAD: Loads all images immediately -->
<img src="large-image.jpg" />

<!-- GOOD: Lazy loads images -->
<img src="large-image.jpg" loading="lazy" />
```

### 示例 5：Node.js 中的异步 I/O
```javascript
// BAD: Blocking file read
const data = fs.readFileSync('file.txt');

// GOOD: Non-blocking file read
fs.readFile('file.txt', (err, data) => {
  if (err) throw err;
  // process data
});
```

### 示例 6：分析 Python 函数
```python
import cProfile
import pstats

def slow_function():
    ...

cProfile.run('slow_function()', 'profile.stats')
p = pstats.Stats('profile.stats')
p.sort_stats('cumulative').print_stats(10)
```

### 示例 7：在 Node.js 中使用 Redis 进行缓存
```javascript
const redis = require('redis');
const client = redis.createClient();

function getCachedData(key, fetchFunction) {
  return new Promise((resolve, reject) => {
    client.get(key, (err, data) => {
      if (data) return resolve(JSON.parse(data));
      fetchFunction().then(result => {
        client.setex(key, 3600, JSON.stringify(result));
        resolve(result);
      });
    });
  });
}
```

---

## 参考文献和进一步阅读
- [Google 网络基础知识：性能](https://web.dev/performance/)
- [MDN 网络文档：性能](https://developer.mozilla.org/en-US/docs/Web/Performance)
- [OWASP：性能测试](https://owasp.org/www-project-performance-testing/)
- [Microsoft 性能最佳实践](https://learn.microsoft.com/en-us/azure/architecture/best-practices/performance)
- [PostgreSQL性能优化](https://wiki.postgresql.org/wiki/Performance_Optimization)
- [MySQL性能调优](https://dev.mysql.com/doc/refman/8.0/en/optimization.html)
- [Node.js 性能最佳实践](https://nodejs.org/en/docs/guides/simple-profiling/)
- [Python 性能技巧](https://docs.python.org/3/library/profile.html)
- [Java 性能调优](https://www.oracle.com/java/technologies/javase/performance.html)
- [.NET 性能指南](https://learn.microsoft.com/en-us/dotnet/standard/performance/)
- [网页测试](https://www.webpagetest.org/)
- [灯塔](https://developers.google.com/web/tools/lighthouse)
- [普罗米修斯](https://prometheus.io/)
- [格拉法纳](https://grafana.com/)
- [k6 负载测试](https://k6.io/)
- [加特林](https://gatling.io/)
- [蝗虫](https://locust.io/)
- [开放遥测](https://opentelemetry.io/)
- [耶格](https://www.jaegertracing.io/)
- [Zipkin](https://zipkin.io/)

---

## 结论

性能优化是一个持续的过程。始终测量、分析和迭代。使用这些最佳实践、清单和故障排除提示来指导您的高性能、可扩展且高效的软件的开发和代码审查。如果您有新的技巧或经验教训，请将它们添加到此处 - 让我们不断完善本指南！

---

<!-- 性能优化说明结束 -->
