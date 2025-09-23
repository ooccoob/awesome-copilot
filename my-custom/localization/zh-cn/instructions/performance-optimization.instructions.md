---
applyTo: "performance-optimization.instructions.md"
---

<!-- 本文件为自动翻译，供参考。请结合实际需求进行校对和完善。-->

# 性能优化最佳实践

## 简介

性能不仅仅是一个流行词——它决定了产品是被用户喜欢还是被抛弃。本指南收录了前端、后端、数据库等多层面的高效性能实践，适用于实际工程开发。请将其作为参考、检查清单和灵感源泉。

---

## 通用原则

- **先度量，后优化**：始终先用基准测试、分析器等工具定位瓶颈，避免盲目优化。
- **优化常用路径**：优先优化最频繁执行的代码。
- **避免过早优化**：先写清晰可维护的代码，必要时再优化。
- **最小化资源消耗**：高效使用内存、CPU、网络和磁盘。
- **追求简单**：简单的数据结构和算法通常更快更易优化。
- **记录性能假设**：对关键性能代码加注释，便于维护。
- **理解平台特性**：了解所用语言、框架、运行时的性能特性。
- **自动化性能测试**：将性能测试集成到 CI/CD。
- **设定性能预算**：为加载时间、内存、API 延迟等设定上限并自动检查。

---

## 前端性能

### 渲染与 DOM

- **最小化 DOM 操作**，批量更新。
- **高效使用虚拟 DOM 框架**，避免不必要的重渲染。
- **列表渲染用稳定 key**，避免用索引。
- **避免内联样式**，优先用 CSS 类。
- **动画用 CSS**，优于 JS。
- **延迟非关键渲染**，如用 `requestIdleCallback`。

### 资源优化

- **图片压缩**，优先用 WebP、AVIF。
- **图标用 SVG**。
- **JS/CSS 打包与压缩**，启用 tree-shaking。
- **合理设置缓存头**。
- **图片/模块懒加载**。
- **字体子集化与优化**。

### 网络优化

- **减少 HTTP 请求数**。
- **启用 HTTP/2/3**。
- **客户端缓存**，如 Service Worker。
- **CDN 加速**。
- **脚本 defer/async**。
- **预加载/预取关键资源**。

### JS 性能

- **避免主线程阻塞**，重计算用 Web Worker。
- **事件防抖/节流**。
- **清理事件监听，防内存泄漏**。
- **高效数据结构**，如 Map/Set。
- **避免全局变量和深拷贝**。

### 可访问性与性能

- **组件语义化**，避免过度 DOM 更新。

### 框架专用

#### React

- 用 `React.memo`、`useMemo`、`useCallback`。
- 组件拆分、代码分割。
- 避免渲染时匿名函数。
- 用 `ErrorBoundary`。
- 用 React DevTools 分析。

#### Angular

- 用 OnPush 检测。
- 模板逻辑移到类中。
- `ngFor` 用 `trackBy`。
- 路由懒加载。
- 用 Angular DevTools。

#### Vue

- 用 computed 属性。
- `v-show`/`v-if` 区分场景。
- 组件/路由懒加载。
- 用 Vue Devtools。

### 常见前端陷阱

- 首屏 JS 体积过大。
- 图片未压缩。
- 事件监听未清理。
- 滥用三方库。
- 忽视移动端性能。

### 前端排查

- 用 Chrome DevTools 性能面板。
- 用 Lighthouse 审计。
- 用 WebPageTest。
- 监控 Core Web Vitals。

---

## 后端性能

### 算法与数据结构

- **选对数据结构**。
- **高效算法**。
- **避免 O(n²) 及更差复杂度**。
- **批量处理**。
- **流式处理大数据**。

### 并发与并行

- **异步 IO**。
- **线程/Worker 池**。
- **避免竞态**。
- **批量网络/数据库操作**。
- **实现背压**。

### 缓存

- **缓存高消耗计算**。
- **合理失效策略**。
- **分布式缓存注意一致性**。
- **防止缓存击穿**。
- **不要滥用缓存**。

### API 与网络

- **最小化响应体**，压缩传输。
- **分页大结果集**。
- **限流**。
- **连接池**。
- **协议选择**。

### 日志与监控

- **热路径减少日志**。
- **结构化日志**。
- **全链路监控**。
- **告警配置**。

### 语言/框架专用

#### Node.js

- 用异步 API，避免阻塞。
- 用 cluster/worker 处理 CPU 密集任务。
- 限制并发连接数。
- 用流处理大文件。
- 用 `clinic.js`、`node --inspect` 分析。

#### Python

- 用内建高效数据结构。
- 用 `cProfile`、`Py-Spy` 分析。
- 用多进程/asyncio。
- CPU 密集用 C 扩展。
- 用 `lru_cache`。

#### Java

- 用高效集合。
- 用 VisualVM、JProfiler 分析。
- 用线程池。
- JVM 参数调优。
- 用 `CompletableFuture`。

#### .NET

- 用 async/await。
- 用 Span/Memory 优化内存。
- 用 dotTrace 分析。
- 对象/连接池化。
- 用 IAsyncEnumerable 流式处理。

### 常见后端陷阱

- 阻塞 IO。
- 数据库未用连接池。
- 缓存滥用。
- 异步错误未处理。
- 未监控性能。

### 后端排查

- 用火焰图分析 CPU。
- 用分布式追踪。
- 堆转储查内存泄漏。
- 日志慢查询。

---

## 数据库性能

### 查询优化

- **加索引**。
- **避免 SELECT \*。**
- **参数化查询**。
- **分析执行计划**。
- **避免 N+1 查询**。
- **结果集分页**。

### 模式设计

- **规范化/反规范化权衡**。
- **高效数据类型**。
- **分区大表**。
- **定期归档老数据**。
- **外键权衡**。

### 事务

- **短事务**。
- **合适隔离级别**。
- **避免长事务**。

### 缓存与复制

- **读写分离**。
- **缓存查询结果**。
- **写穿/写回策略**。
- **分片**。

### NoSQL

- **按访问模式建模**。
- **避免热点分区**。
- **防止文档无限增长**。
- **理解一致性模型**。

### 常见数据库陷阱

- 缺索引。
- SELECT \*。
- 未监控慢查询。
- 忽视复制延迟。
- 未归档老数据。

### 数据库排查

- 慢查询日志。
- EXPLAIN 分析。
- 监控缓存命中率。
- 用专用监控工具。

---

## 性能代码审查清单

- [ ] 有无明显算法低效？
- [ ] 数据结构是否合适？
- [ ] 有无重复计算？
- [ ] 是否合理使用缓存？
- [ ] 数据库查询是否优化？
- [ ] 大数据是否分页/流式？
- [ ] 有无内存泄漏？
- [ ] 网络请求是否最小化？
- [ ] 资源是否压缩优化？
- [ ] 热路径有无阻塞操作？
- [ ] 日志是否合理？
- [ ] 性能关键路径有无注释和测试？
- [ ] 有无自动化性能测试？
- [ ] 有无性能告警？
- [ ] 有无反模式？

---

## 高级主题

### 分析与基准测试

- 用专用分析器定位瓶颈。
- 写微基准测试。
- A/B 测试优化效果。
- 性能测试集成到 CI/CD。

### 内存管理

- 及时释放资源。
- 对象池化。
- 监控堆和 GC。
- 用工具查内存泄漏。

### 可扩展性

- 水平扩展。
- 自动扩容。
- 识别单点瓶颈。
- 分布式系统用幂等、重试、熔断。

### 安全与性能

- 用高效加密库。
- 高效输入校验。
- 限流防 DoS。

### 移动端性能

- 启动优化、懒加载。
- 图片/资源压缩。
- 高效存储方案。
- 用平台分析工具。

### 云与无服务器

- 冷启动优化。
- 合理分配资源。
- 用托管服务。
- 关注云成本。

---

## 实用示例

### 示例 1：JS 输入防抖

```javascript
// BAD: 每次输入都请求
input.addEventListener("input", (e) => {
  fetch(`/search?q=${e.target.value}`);
});

// GOOD: 防抖
let timeout;
input.addEventListener("input", (e) => {
  clearTimeout(timeout);
  timeout = setTimeout(() => {
    fetch(`/search?q=${e.target.value}`);
  }, 300);
});
```

### 示例 2：高效 SQL 查询

```sql
-- BAD: SELECT *
SELECT * FROM users WHERE email = 'user@example.com';

-- GOOD: 只查需要的字段且用索引
SELECT id, name FROM users WHERE email = 'user@example.com';
```

### 示例 3：Python 计算缓存

```python
# BAD: 每次都算
result = expensive_function(x)

# GOOD: 用缓存
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_function(x):
    ...
result = expensive_function(x)
```

### 示例 4：HTML 图片懒加载

```html
<!-- BAD: 立即加载所有图片 -->
<img src="large-image.jpg" />

<!-- GOOD: 懒加载 -->
<img src="large-image.jpg" loading="lazy" />
```

### 示例 5：Node.js 异步 IO

```javascript
// BAD: 阻塞读文件
const data = fs.readFileSync("file.txt");

// GOOD: 非阻塞
fs.readFile("file.txt", (err, data) => {
  if (err) throw err;
  // process data
});
```

### 示例 6：Python 性能分析

```python
import cProfile
import pstats

def slow_function():
    ...

cProfile.run('slow_function()', 'profile.stats')
p = pstats.Stats('profile.stats')
p.sort_stats('cumulative').print_stats(10)
```

### 示例 7：Node.js 用 Redis 缓存

```javascript
const redis = require("redis");
const client = redis.createClient();

function getCachedData(key, fetchFunction) {
  return new Promise((resolve, reject) => {
    client.get(key, (err, data) => {
      if (data) return resolve(JSON.parse(data));
      fetchFunction().then((result) => {
        client.setex(key, 3600, JSON.stringify(result));
        resolve(result);
      });
    });
  });
}
```

---

## 参考资料

- [Google Web Fundamentals: Performance](https://web.dev/performance/)
- [MDN Web Docs: Performance](https://developer.mozilla.org/zh-CN/docs/Web/Performance)
- [OWASP: Performance Testing](https://owasp.org/www-project-performance-testing/)
- [Microsoft 性能最佳实践](https://learn.microsoft.com/zh-cn/azure/architecture/best-practices/performance)
- [PostgreSQL 性能优化](https://wiki.postgresql.org/wiki/Performance_Optimization)
- [MySQL 性能调优](https://dev.mysql.com/doc/refman/8.0/en/optimization.html)
- [Node.js 性能最佳实践](https://nodejs.org/en/docs/guides/simple-profiling/)
- [Python 性能技巧](https://docs.python.org/zh-cn/3/library/profile.html)
- [Java 性能调优](https://www.oracle.com/java/technologies/javase/performance.html)
- [.NET 性能指南](https://learn.microsoft.com/zh-cn/dotnet/standard/performance/)
- [WebPageTest](https://www.webpagetest.org/)
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)
- [k6 性能测试](https://k6.io/)
- [Gatling](https://gatling.io/)
- [Locust](https://locust.io/)
- [OpenTelemetry](https://opentelemetry.io/)
- [Jaeger](https://www.jaegertracing.io/)
- [Zipkin](https://zipkin.io/)

---

## 总结

性能优化是持续过程。请结合本指南、清单和排查建议，持续度量、分析和迭代优化。如有新经验，欢迎补充！

---

免责声明：本翻译仅供参考，具体实践请结合实际项目需求和最新官方文档。
