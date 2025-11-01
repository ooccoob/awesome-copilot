---
applyTo: '*'
description: '适用于所有语言、框架和技术栈的最全面、实用且由工程师编写的性能优化指令。涵盖前端、后端和数据库最佳实践，提供可操作的指导、基于场景的检查清单、故障排除和专业技巧。'
---

# 性能优化最佳实践

## 介绍

性能不仅仅是一个流行词——它决定了用户是喜爱还是放弃一个产品。我亲眼看到过慢应用程序如何让用户感到沮丧、产生高昂的云账单，甚至失去客户。这本指南是我使用和审查过的最有效的真实世界性能实践的活集合，涵盖前端、后端和数据库层，以及高级主题。将其用作构建快速、高效和可扩展软件的参考、检查清单和灵感来源。

---

## 通用原则

- **先测量，后优化**：在优化前始终分析和测量。使用基准测试、性能分析器和监控工具来识别真正的瓶颈。猜测是性能的敌人。
  - *专业技巧*：使用 Chrome DevTools、Lighthouse、New Relic、Datadog、Py-Spy 或您语言的内置性能分析器。
- **为常见情况优化**：专注于优化最频繁执行的代码路径。不要在罕见的边缘情况上浪费时间，除非它们是关键的。
- **避免过早优化**：首先编写清晰、可维护的代码；仅在必要时优化。过早优化可能使代码更难阅读和维护。
- **最小化资源使用**：高效使用内存、CPU、网络和磁盘资源。始终问："这可以用更少的资源完成吗？"
- **偏好简单性**：简单的算法和数据结构通常更快且更容易优化。不要过度设计。
- **记录性能假设**：对任何性能关键或具有不明显优化的代码进行清晰注释。未来的维护者（包括您自己）会感谢您。
- **了解平台**：了解您的语言、框架和运行时的性能特征。在 Python 中快速的在 JavaScript 中可能慢，反之亦然。
- **自动化性能测试**：将性能测试和基准测试集成到您的 CI/CD 管道中。及早发现回归。
- **设置性能预算**：为加载时间、内存使用、API 延迟等定义可接受的限制。通过自动检查强制执行它们。

---

## 前端性能

### 渲染和 DOM
- **最小化 DOM 操作**：尽可能批量更新。频繁的 DOM 更改是昂贵的。
  - *反模式*：在循环中更新 DOM。相反，构建文档片段并一次性附加。
- **虚拟 DOM 框架**：高效使用 React、Vue 或类似框架——避免不必要的重新渲染。
  - *React 示例*：使用 `React.memo`、`useMemo` 和 `useCallback` 防止不必要的渲染。
- **列表中的键**：始终在列表中使用稳定的键来帮助虚拟 DOM 差异化。除非列表是静态的，否则避免使用数组索引作为键。
- **避免内联样式**：内联样式可能触发布局抖动。偏好 CSS 类。
- **CSS 动画**：使用 CSS 过渡/动画而不是 JavaScript 以获得更平滑的 GPU 加速效果。
- **延迟非关键渲染**：使用 `requestIdleCallback` 或类似功能将工作延迟到浏览器空闲时。

### 资源优化
- **图像压缩**：使用 ImageOptim、Squoosh 或 TinyPNG 等工具。网页交付偏好现代格式（WebP、AVIF）。
- **图标使用 SVG**：SVG 缩放良好，对于简单图形通常比 PNG 更小。
- **压缩和打包**：使用 Webpack、Rollup 或 esbuild 打包和压缩 JS/CSS。启用树摇移除死代码。
- **缓存头**：为静态资源设置长缓存头。使用缓存破坏进行更新。
- **懒加载**：对图像使用 `loading="lazy"`，对 JS 模块/组件使用动态导入。
- **字体优化**：仅使用您需要的字符集。子集化字体并使用 `font-display: swap`。

### 网络优化
- **减少 HTTP 请求**：合并文件，使用图像精灵，内联关键 CSS。
- **HTTP/2 和 HTTP/3**：启用这些协议以实现多路复用和更低延迟。
- **客户端缓存**：使用 Service Workers、IndexedDB 和 localStorage 进行离线和重复访问。
- **CDN**：从靠近用户的 CDN 提供静态资源。使用多个 CDN 实现冗余。
- **延迟/异步脚本**：对非关键 JS 使用 `defer` 或 `async` 以避免阻塞渲染。
- **预加载和预取**：对关键资源使用 `<link rel="preload">` 和 `<link rel="prefetch">`。

### JavaScript 性能
- **避免阻塞主线程**：将繁重计算卸载到 Web Workers。
- **事件防抖/节流**：对于滚动、调整大小和输入事件，使用防抖/节流来限制处理程序频率。
- **内存泄漏**：清理事件监听器、间隔和 DOM 引用。使用浏览器开发工具检查分离的节点。
- **高效数据结构**：使用 Maps/Sets 进行查找，使用 TypedArrays 处理数值数据。
- **避免全局变量**：全局变量可能导致内存泄漏和不可预测的性能。
- **避免深对象克隆**：仅在必要时使用浅拷贝或像 lodash 的 `cloneDeep` 这样的库。

### 可访问性和性能
- **可访问组件**：确保 ARIA 更新不过度。使用语义 HTML 以兼顾可访问性和性能。
- **屏幕阅读器性能**：避免可能压倒辅助技术的快速 DOM 更新。

### 框架特定技巧
#### React
- 使用 `React.memo`、`useMemo` 和 `useCallback` 避免不必要的渲染。
- 拆分大组件并使用代码分割（`React.lazy`、`Suspense`）。
- 避免渲染中的匿名函数；它们在每次渲染时创建新引用。
- 使用 `ErrorBoundary` 优雅地捕获和处理错误。
- 使用 React DevTools Profiler 进行性能分析。

#### Angular
- 对不需要频繁更新的组件使用 OnPush 变更检测。
- 避免模板中的复杂表达式；将逻辑移到组件类。
- 在 `ngFor` 中使用 `trackBy` 进行高效列表渲染。
- 使用 Angular 路由器懒加载模块和组件。
- 使用 Angular DevTools 进行性能分析。

#### Vue
- 在模板中使用计算属性而不是方法进行缓存。
- 适当使用 `v-show` vs `v-if`（`v-show` 更适合频繁切换可见性）。
- 使用 Vue 路由器懒加载组件和路由。
- 使用 Vue Devtools 进行性能分析。

### 常见前端陷阱
- 初始页面加载时加载大型 JS 包。
- 不压缩图像或使用过时格式。
- 未能清理事件监听器，导致内存泄漏。
- 为简单任务过度使用第三方库。
- 忽略移动性能（在真实设备上测试！）。

### 前端故障排除
- 使用 Chrome DevTools 的 Performance 标签记录和分析慢帧。
- 使用 Lighthouse 审计性能并获得可操作的建议。
- 使用 WebPageTest 进行真实世界的负载测试。
- 监控核心 Web 指标（LCP、FID、CLS）以获得用户中心指标。

---

## 后端性能

### 算法和数据结构优化
- **选择正确的数据结构**：数组用于顺序访问，哈希映射用于快速查找，树用于层次数据等。
- **高效算法**：在适当的地方使用二分查找、快速排序或基于哈希的算法。
- **避免 O(n²) 或更差**：分析嵌套循环和递归调用。重构以减少复杂度。
- **批处理**：批处理数据以减少开销（例如，批量数据库插入）。
- **流式处理**：对大数据集使用流式 API 以避免将所有内容加载到内存中。

### 并发和并行性
- **异步 I/O**：使用 async/await、回调或事件循环避免阻塞线程。
- **线程/工作线程池**：使用池管理并发并避免资源耗尽。
- **避免竞态条件**：在需要的地方使用锁、信号量或原子操作。
- **批量操作**：批处理网络/数据库调用以减少往返次数。
- **背压**：在队列和管道中实现背压以避免过载。

### 缓存
- **缓存昂贵计算**：对热数据使用内存缓存（Redis、Memcached）。
- **缓存失效**：使用基于时间（TTL）、基于事件或手动失效。陈旧缓存比没有缓存更糟糕。
- **分布式缓存**：对于多服务器设置，使用分布式缓存并注意一致性问题。
- **缓存雪崩保护**：使用锁或请求合并防止雪崩问题。
- **不要缓存所有内容**：某些数据过于易变或敏感，不适合缓存。

### API 和网络
- **最小化负载**：使用 JSON，压缩响应（gzip、Brotli），避免发送不必要的数据。
- **分页**：始终对大结果集进行分页。对实时数据使用游标。
- **速率限制**：保护 API 免受滥用和过载。
- **连接池**：为数据库和外部服务重用连接。
- **协议选择**：使用 HTTP/2、gRPC 或 WebSockets 进行高吞吐量、低延迟通信。

### 日志记录和监控
- **最小化热路径中的日志记录**：过度日志记录可能减慢关键代码。
- **结构化日志记录**：使用 JSON 或键值日志以便更容易解析和分析。
- **监控一切**：延迟、吞吐量、错误率、资源使用。使用 Prometheus、Grafana、Datadog 或类似工具。
- **警报**：为性能回归和资源耗尽设置警报。

### 语言/框架特定技巧
#### Node.js
- 使用异步 API；避免阻塞事件循环（例如，生产中绝不使用 `fs.readFileSync`）。
- 使用集群或工作线程处理 CPU 密集型任务。
- 限制并发打开连接以避免资源耗尽。
- 使用流处理大文件或网络数据。
- 使用 `clinic.js`、`node --inspect` 或 Chrome DevTools 进行性能分析。

#### Python
- 使用内置数据结构（`dict`、`set`、`deque`）以获得速度。
- 使用 `cProfile`、`line_profiler` 或 `Py-Spy` 进行性能分析。
- 使用 `multiprocessing` 或 `asyncio` 实现并行性。
- 避免代码中的 GIL 瓶颈；使用 C 扩展或子进程。
- 使用 `lru_cache` 进行记忆化。

#### Java
- 使用高效集合（`ArrayList`、`HashMap` 等）。
- 使用 VisualVM、JProfiler 或 YourKit 进行性能分析。
- 使用线程池（`Executors`）进行并发。
- 为堆和垃圾回收调整 JVM 选项（`-Xmx`、`-Xms`、`-XX:+UseG1GC`）。
- 使用 `CompletableFuture` 进行异步编程。

#### .NET
- 对 I/O 密集型操作使用 `async/await`。
- 使用 `Span<T>` 和 `Memory<T>` 进行高效内存访问。
- 使用 dotTrace、Visual Studio Profiler 或 PerfView 进行性能分析。
- 在适当的地方池化对象和连接。
- 使用 `IAsyncEnumerable<T>` 处理流数据。

### 常见后端陷阱
- Web 服务器中的同步/阻塞 I/O。
- 不为数据库使用连接池。
- 过度缓存或缓存敏感/易变数据。
- 忽略异步代码中的错误处理。
- 不监控或不对性能回归发出警报。

### 后端故障排除
- 使用火焰图可视化 CPU 使用情况。
- 使用分布式跟踪（OpenTelemetry、Jaeger、Zipkin）跟踪跨服务的请求延迟。
- 使用堆转储和内存分析器查找泄漏。
- 记录慢查询和 API 调用以供分析。

---

## 数据库性能

### 查询优化
- **索引**：在经常查询、过滤或连接的列上使用索引。监控索引使用情况并删除未使用的索引。
- **避免 SELECT ***：仅选择您需要的列。减少 I/O 和内存使用。
- **参数化查询**：防止 SQL 注入并改进计划缓存。
- **查询计划**：分析和优化查询执行计划。在 SQL 数据库中使用 `EXPLAIN`。
- **避免 N+1 查询**：使用连接或批量查询避免循环中的重复查询。
- **限制结果集**：对大表使用 `LIMIT`/`OFFSET` 或游标。

### 模式设计
- **规范化**：规范化以减少冗余，但在必要时为读取密集型工作负载反规范化。
- **数据类型**：使用最高效的数据类型并设置适当的约束。
- **分区**：对大表进行分区以实现可扩展性和可管理性。
- **归档**：定期归档或清除旧数据以保持表小而快。
- **外键**：使用它们进行数据完整性，但在高写入场景中要注意性能权衡。

### 事务
- **短事务**：保持事务尽可能短以减少锁争用。
- **隔离级别**：使用满足一致性需求的最低隔离级别。
- **避免长时间运行的事务**：它们可能阻塞其他操作并增加死锁。

### 缓存和复制
- **读取副本**：用于扩展读取密集型工作负载。监控复制延迟。
- **缓存查询结果**：对频繁访问的查询使用 Redis 或 Memcached。
- **写穿透/写后**：为您的一致性需求选择正确的策略。
- **分片**：将数据分布在多个服务器上以实现可扩展性。

### NoSQL 数据库
- **为访问模式设计**：为您的需求查询对数据建模。
- **避免热分区**：均匀分布写入/读取。
- **无界增长**：注意无界数组或文档。
- **分片和复制**：用于可扩展性和可用性。
- **一致性模型**：了解最终一致性 vs 强一致性并适当选择。

### 常见数据库陷阱
- 缺少或未使用的索引。
- 生产查询中的 SELECT *。
- 不监控慢查询。
- 忽略复制延迟。
- 不归档旧数据。

### 数据库故障排除
- 使用慢查询日志识别瓶颈。
- 使用 `EXPLAIN` 分析查询计划。
- 监控缓存命中/未命中比率。
- 使用数据库特定的监控工具（pg_stat_statements、MySQL Performance Schema）。

---

## 性能代码审查检查清单

- [ ] 是否存在任何明显的算法低效（O(n²) 或更差）？
- [ ] 数据结构是否适合其用途？
- [ ] 是否存在不必要的计算或重复工作？
- [ ] 缓存是否在适当的地方使用，失效是否正确处理？
- [ ] 数据库查询是否优化、索引并避免 N+1 问题？
- [ ] 大负载是否分页、流式处理或分块？
- [ ] 是否存在任何内存泄漏或无界资源使用？
- [ ] 网络请求是否最小化、批处理并在失败时重试？
- [ ] 资源是否优化、压缩并高效提供？
- [ ] 热路径中是否存在任何阻塞操作？
- [ ] 热路径中的日志记录是否最小化和结构化？
- [ ] 性能关键代码路径是否已记录和测试？
- [ ] 是否有性能敏感代码的自动测试或基准测试？
- [ ] 是否有性能回归警报？
- [ ] 是否存在任何反模式（例如，SELECT *、阻塞 I/O、全局变量）？

---

## 高级主题

### 性能分析和基准测试
- **性能分析器**：使用特定语言的性能分析器（Chrome DevTools、Py-Spy、VisualVM、dotTrace 等）识别瓶颈。
- **微基准测试**：为关键代码路径编写微基准测试。使用 `benchmark.js`、`pytest-benchmark` 或 Java 的 JMH。
- **A/B 测试**：通过 A/B 或金丝雀发布测量优化的真实世界影响。
- **持续性能测试**：将性能测试集成到 CI/CD 中。使用 k6、Gatling 或 Locust 等工具。

### 内存管理
- **资源清理**：始终及时释放资源（文件、套接字、数据库连接）。
- **对象池化**：对频繁创建/销毁的对象使用（例如，数据库连接、线程）。
- **堆监控**：监控堆使用和垃圾回收。为工作负载调整 GC 设置。
- **内存泄漏**：使用泄漏检测工具（Valgrind、LeakCanary、Chrome DevTools）。

### 可扩展性
- **水平扩展**：设计无状态服务，使用分片/分区和负载均衡器。
- **自动扩展**：使用云自动扩展组并设置合理阈值。
- **瓶颈分析**：识别和解决单点故障。
- **分布式系统**：使用幂等操作、重试和断路器。

### 安全和性能
- **高效加密**：使用硬件加速和维护良好的加密库。
- **验证**：高效验证输入；避免热路径中的正则表达式。
- **速率限制**：防止 DoS 而不伤害合法用户。

### 移动性能
- **启动时间**：懒加载功能，延迟繁重工作，最小化初始包大小。
- **图像/资源优化**：使用响应式图像并为移动带宽压缩资源。
- **高效存储**：使用 SQLite、Realm 或平台优化的存储。
- **性能分析**：使用 Android Profiler、Instruments (iOS) 或 Firebase Performance Monitoring。

### 云和无服务器
- **冷启动**：最小化依赖项并保持函数温暖。
- **资源分配**：为无服务器函数调整内存/CPU。
- **托管服务**：使用托管缓存、队列和数据库以实现可扩展性。
- **成本优化**：监控和优化云成本作为性能指标。

---

## 实际示例

### 示例 1：在 JavaScript 中对用户输入防抖
```javascript
// 错误：每次击键都触发 API 调用
input.addEventListener('input', (e) => {
  fetch(`/search?q=${e.target.value}`);
});

// 正确：防抖 API 调用
let timeout;
input.addEventListener('input', (e) => {
  clearTimeout(timeout);
  timeout = setTimeout(() => {
    fetch(`/search?q=${e.target.value}`);
  }, 300);
});
```

### 示例 2：高效 SQL 查询
```sql
-- 错误：选择所有列且不使用索引
SELECT * FROM users WHERE email = 'user@example.com';

-- 正确：仅选择需要的列并使用索引
SELECT id, name FROM users WHERE email = 'user@example.com';
```

### 示例 3：在 Python 中缓存昂贵计算
```python
# 错误：每次重新计算结果
result = expensive_function(x)

# 正确：缓存结果
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_function(x):
    ...
result = expensive_function(x)
```

### 示例 4：在 HTML 中懒加载图像
```html
<!-- 错误：立即加载所有图像 -->
<img src="large-image.jpg" />

<!-- 正确：懒加载图像 -->
<img src="large-image.jpg" loading="lazy" />
```

### 示例 5：在 Node.js 中异步 I/O
```javascript
// 错误：阻塞文件读取
const data = fs.readFileSync('file.txt');

// 正确：非阻塞文件读取
fs.readFile('file.txt', (err, data) => {
  if (err) throw err;
  // 处理数据
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

### 示例 7：在 Node.js 中使用 Redis 缓存
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

## 参考和进一步阅读
- [Google Web 基础：性能](https://web.dev/performance/)
- [MDN Web 文档：性能](https://developer.mozilla.org/en-US/docs/Web/Performance)
- [OWASP：性能测试](https://owasp.org/www-project-performance-testing/)
- [Microsoft 性能最佳实践](https://learn.microsoft.com/en-us/azure/architecture/best-practices/performance)
- [PostgreSQL 性能优化](https://wiki.postgresql.org/wiki/Performance_Optimization)
- [MySQL 性能调优](https://dev.mysql.com/doc/refman/8.0/en/optimization.html)
- [Node.js 性能最佳实践](https://nodejs.org/en/docs/guides/simple-profiling/)
- [Python 性能技巧](https://docs.python.org/3/library/profile.html)
- [Java 性能调优](https://www.oracle.com/java/technologies/javase/performance.html)
- [.NET 性能指南](https://learn.microsoft.com/en-us/dotnet/standard/performance/)
- [WebPageTest](https://www.webpagetest.org/)
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)
- [k6 负载测试](https://k6.io/)
- [Gatling](https://gatling.io/)
- [Locust](https://locust.io/)
- [OpenTelemetry](https://opentelemetry.io/)
- [Jaeger](https://www.jaegertracing.io/)
- [Zipkin](https://zipkin.io/)

---

## 结论

性能优化是一个持续的过程。始终测量、分析和迭代。使用这些最佳实践、检查清单和故障排除技巧来指导您的开发和代码审查，以构建高性能、可扩展和高效的软件。如果您有新的技巧或经验教训，请在此添加——让这本指南不断成长！

---

<!-- 性能优化指令结束 -->