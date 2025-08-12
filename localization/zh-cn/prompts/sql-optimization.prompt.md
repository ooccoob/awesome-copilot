````prompt
---
mode: 'agent'
tools: ['changes', 'codebase', 'editFiles', 'problems']
description: '面向所有主流 SQL 数据库（MySQL、PostgreSQL、SQL Server、Oracle）的通用 SQL 性能优化助手，提供系统化的查询调优、索引策略与数据库性能分析。涵盖执行计划分析、分页优化、批量操作与性能监控等实践。'
tested_with: 'GitHub Copilot Chat (GPT-4o) - Validated July 20, 2025'
---

# SQL 性能优化助手

为 ${selection} 提供专家级 SQL 性能优化（若未选择则面向整个项目）。聚焦可跨 MySQL、PostgreSQL、SQL Server、Oracle 等数据库通用的优化技术。

## 🎯 核心优化领域

### 查询性能分析
```sql
-- ❌ 不佳：低效查询模式
SELECT * FROM orders o
WHERE YEAR(o.created_at) = 2024
  AND o.customer_id IN (
      SELECT c.id FROM customers c WHERE c.status = 'active'
  );

-- ✅ 推荐：合理的连接与可索引条件
SELECT o.id, o.customer_id, o.total_amount, o.created_at
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
WHERE o.created_at >= '2024-01-01'
  AND o.created_at < '2025-01-01'
  AND c.status = 'active';

-- 所需索引：
-- CREATE INDEX idx_orders_created_at ON orders(created_at);
-- CREATE INDEX idx_customers_status ON customers(status);
-- CREATE INDEX idx_orders_customer_id ON orders(customer_id);
```

### 索引策略优化
```sql
-- ❌ 不佳：盲目建立大而全的复合索引
CREATE INDEX idx_user_data ON users(email, first_name, last_name, created_at);

-- ✅ 推荐：匹配查询模式的复合索引
-- 针对“先按 email 过滤，再按 created_at 排序”的场景
CREATE INDEX idx_users_email_created ON users(email, created_at);

-- 全文/姓名搜索（示例）
CREATE INDEX idx_users_name ON users(last_name, first_name);

-- 用户状态查询（条件索引/局部索引示例）
CREATE INDEX idx_users_status_created ON users(status, created_at)
WHERE status IS NOT NULL;
```

### 子查询优化
```sql
-- ❌ 不佳：相关子查询
SELECT p.product_name, p.price
FROM products p
WHERE p.price > (
    SELECT AVG(price)
    FROM products p2
    WHERE p2.category_id = p.category_id
);

-- ✅ 推荐：窗口函数方案
SELECT product_name, price
FROM (
    SELECT product_name, price,
           AVG(price) OVER (PARTITION BY category_id) as avg_category_price
    FROM products
) ranked
WHERE price > avg_category_price;
```

## 📈 性能调优技巧

### JOIN 优化
```sql
-- ❌ 不佳：连接顺序与条件不友好
SELECT o.*, c.name, p.product_name
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.id
LEFT JOIN order_items oi ON o.id = oi.order_id
LEFT JOIN products p ON oi.product_id = p.id
WHERE o.created_at > '2024-01-01'
  AND c.status = 'active';

-- ✅ 推荐：在 JOIN 中尽早过滤，匹配执行计划
SELECT o.id, o.total_amount, c.name, p.product_name
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id AND c.status = 'active'
INNER JOIN order_items oi ON o.id = oi.order_id
INNER JOIN products p ON oi.product_id = p.id
WHERE o.created_at > '2024-01-01';
```

### 分页优化
```sql
-- ❌ 不佳：基于 OFFSET 的深分页（大偏移量极慢）
SELECT * FROM products
ORDER BY created_at DESC
LIMIT 20 OFFSET 10000;

-- ✅ 推荐：基于游标/时间戳的分页
SELECT * FROM products
WHERE created_at < '2024-06-15 10:30:00'
ORDER BY created_at DESC
LIMIT 20;

-- 或基于 ID 的游标
SELECT * FROM products
WHERE id > 1000
ORDER BY id
LIMIT 20;
```

### 聚合优化
```sql
-- ❌ 不佳：多次独立聚合
SELECT COUNT(*) FROM orders WHERE status = 'pending';
SELECT COUNT(*) FROM orders WHERE status = 'shipped';
SELECT COUNT(*) FROM orders WHERE status = 'delivered';

-- ✅ 推荐：条件聚合一次完成
SELECT
    COUNT(CASE WHEN status = 'pending' THEN 1 END) as pending_count,
    COUNT(CASE WHEN status = 'shipped' THEN 1 END) as shipped_count,
    COUNT(CASE WHEN status = 'delivered' THEN 1 END) as delivered_count
FROM orders;
```

## 🔍 查询反模式

### SELECT 性能问题
```sql
-- ❌ 反模式：SELECT *
SELECT * FROM large_table lt
JOIN another_table at ON lt.id = at.ref_id;

-- ✅ 推荐：显式列选择
SELECT lt.id, lt.name, at.value
FROM large_table lt
JOIN another_table at ON lt.id = at.ref_id;
```

### WHERE 子句优化
```sql
-- ❌ 不佳：WHERE 中使用函数，破坏索引
SELECT * FROM orders
WHERE UPPER(customer_email) = 'JOHN@EXAMPLE.COM';

-- ✅ 推荐：索引友好写法
SELECT * FROM orders
WHERE customer_email = 'john@example.com';
-- 可考虑：CREATE INDEX idx_orders_email ON orders(LOWER(customer_email));
```

### OR vs UNION 优化
```sql
-- ❌ 不佳：复杂 OR 条件
SELECT * FROM products
WHERE (category = 'electronics' AND price < 1000)
   OR (category = 'books' AND price < 50);

-- ✅ 推荐：利用 UNION（或 UNION ALL）便于优化
SELECT * FROM products WHERE category = 'electronics' AND price < 1000
UNION ALL
SELECT * FROM products WHERE category = 'books' AND price < 50;
```

## 📊 与数据库无关的优化

### 批量操作
```sql
-- ❌ 不佳：逐行插入
INSERT INTO products (name, price) VALUES ('Product 1', 10.00);
INSERT INTO products (name, price) VALUES ('Product 2', 15.00);
INSERT INTO products (name, price) VALUES ('Product 3', 20.00);

-- ✅ 推荐：批量插入
INSERT INTO products (name, price) VALUES
('Product 1', 10.00),
('Product 2', 15.00),
('Product 3', 20.00);
```

### 临时表使用
```sql
-- ✅ 推荐：复杂计算时使用临时表
CREATE TEMPORARY TABLE temp_calculations AS
SELECT customer_id,
       SUM(total_amount) as total_spent,
       COUNT(*) as order_count
FROM orders
WHERE created_at >= '2024-01-01'
GROUP BY customer_id;

-- 基于临时表做进一步计算
SELECT c.name, tc.total_spent, tc.order_count
FROM temp_calculations tc
JOIN customers c ON tc.customer_id = c.id
WHERE tc.total_spent > 1000;
```

## 🛠️ 索引管理

### 设计原则
```sql
-- ✅ 推荐：覆盖索引（示例）
CREATE INDEX idx_orders_covering
ON orders(customer_id, created_at)
INCLUDE (total_amount, status);  -- SQL Server 语法
-- 其他数据库：CREATE INDEX idx_orders_covering ON orders(customer_id, created_at, total_amount, status);
```

### 局部索引策略
```sql
-- ✅ 推荐：特定条件下的索引
CREATE INDEX idx_orders_active
ON orders(created_at)
WHERE status IN ('pending', 'processing');
```

## 📈 性能监控查询

### 慢查询识别（示例）
```sql
-- 各数据库语法有所差异

-- MySQL:
SELECT query_time, lock_time, rows_sent, rows_examined, sql_text
FROM mysql.slow_log
ORDER BY query_time DESC;

-- PostgreSQL:
SELECT query, calls, total_time, mean_time
FROM pg_stat_statements
ORDER BY total_time DESC;

-- SQL Server:
SELECT
    qs.total_elapsed_time/qs.execution_count as avg_elapsed_time,
    qs.execution_count,
    SUBSTRING(qt.text, (qs.statement_start_offset/2)+1,
        ((CASE qs.statement_end_offset WHEN -1 THEN DATALENGTH(qt.text)
        ELSE qs.statement_end_offset END - qs.statement_start_offset)/2)+1) as query_text
FROM sys.dm_exec_query_stats qs
CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) qt
ORDER BY avg_elapsed_time DESC;
```

## 🏁 通用优化检查清单

### 查询结构
- [ ] 生产查询避免 SELECT *
- [ ] 使用合适的 JOIN 类型（INNER/LEFT/RIGHT）
- [ ] 在 WHERE 中尽早过滤
- [ ] 适当使用 EXISTS 替代 IN 子查询
- [ ] 避免破坏索引的函数调用

### 索引策略
- [ ] 高频列具备索引
- [ ] 复合索引的列序合理
- [ ] 避免过度索引（影响写性能）
- [ ] 适用时采用覆盖索引
- [ ] 针对特定模式使用局部索引

### 数据类型与模型
- [ ] 合理的数据类型选择
- [ ] 适度范式化（OLTP 3NF，OLAP 适当反范式）
- [ ] 利用约束辅助优化器
- [ ] 大表分区（按需）

### 查询模式
- [ ] 使用 LIMIT/TOP 控制结果集
- [ ] 实施高效分页策略
- [ ] 批量处理批量变更
- [ ] 避免 N+1 查询问题
- [ ] 重复查询使用预处理/参数化

### 性能测试
- [ ] 使用真实数据量测试
- [ ] 分析执行计划
- [ ] 持续监测查询性能
- [ ] 为慢查询设置告警
- [ ] 定期分析索引使用

## 📜 优化方法论

1. 识别：使用数据库工具定位慢查询
2. 分析：检查执行计划并定位瓶颈
3. 优化：应用相应优化技术
4. 测试：验证性能改进
5. 监控：持续跟踪性能指标
6. 迭代：定期回顾与优化

专注可量化的性能收益，并使用贴近真实的数据规模与访问模式验证优化效果。

---

**免责声明**：本文件由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 自动本地化，可能存在不准确之处。若发现不当或错误翻译，请提交 [Issue](https://github.com/ooccoob/datafill/issues) 进行反馈。

````
