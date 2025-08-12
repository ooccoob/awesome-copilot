````prompt
---
mode: 'agent'
tools: ['changes', 'codebase', 'editFiles', 'problems']
description: '专注 PostgreSQL 独有特性、进阶数据类型与生态扩展的开发助手。覆盖 JSONB 操作、数组类型、自定义类型、范围/几何类型、全文检索、窗口函数与 PostgreSQL 拓展生态等主题。'
tested_with: 'GitHub Copilot Chat (GPT-4o) - Validated July 20, 2025'
---

# PostgreSQL 开发助手

为 ${selection} 提供专家级 PostgreSQL 指南（若未选择则面向整个项目）。聚焦 PostgreSQL 专有特性、优化范式与高级能力。

## 📌 PostgreSQL 专有特性

### JSONB 操作
```sql
-- 高级 JSONB 查询
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    data JSONB NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 使用 GIN 索引加速 JSONB
CREATE INDEX idx_events_data_gin ON events USING gin(data);

-- JSONB 包含与路径查询
SELECT * FROM events
WHERE data @> '{"type": "login"}'
  AND data #>> '{user,role}' = 'admin';

-- JSONB 聚合
SELECT jsonb_agg(data) FROM events WHERE data ? 'user_id';
```

### 数组操作
```sql
-- PostgreSQL 数组
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    tags TEXT[],
    categories INTEGER[]
);

-- 数组查询与操作
SELECT * FROM posts WHERE 'postgresql' = ANY(tags);
SELECT * FROM posts WHERE tags && ARRAY['database', 'sql'];
SELECT * FROM posts WHERE array_length(tags, 1) > 3;

-- 数组聚合
SELECT array_agg(DISTINCT category) FROM posts, unnest(categories) as category;
```

### 窗口函数与分析
```sql
-- 高级窗口函数
SELECT
    product_id,
    sale_date,
    amount,
    -- 运行累计
    SUM(amount) OVER (PARTITION BY product_id ORDER BY sale_date) as running_total,
    -- 移动平均
    AVG(amount) OVER (PARTITION BY product_id ORDER BY sale_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as moving_avg,
    -- 排名
    DENSE_RANK() OVER (PARTITION BY EXTRACT(month FROM sale_date) ORDER BY amount DESC) as monthly_rank,
    -- 前后值对比
    LAG(amount, 1) OVER (PARTITION BY product_id ORDER BY sale_date) as prev_amount
FROM sales;
```

### 全文检索
```sql
-- PostgreSQL 全文检索
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT,
    search_vector tsvector
);

-- 更新检索向量
UPDATE documents
SET search_vector = to_tsvector('english', title || ' ' || content);

-- GIN 索引用于检索性能
CREATE INDEX idx_documents_search ON documents USING gin(search_vector);

-- 检索查询
SELECT * FROM documents
WHERE search_vector @@ plainto_tsquery('english', 'postgresql database');

-- 结果排序
SELECT *, ts_rank(search_vector, plainto_tsquery('postgresql')) as rank
FROM documents
WHERE search_vector @@ plainto_tsquery('postgresql')
ORDER BY rank DESC;
```

## 🚀 PostgreSQL 性能调优

### 查询优化
```sql
-- 使用 EXPLAIN ANALYZE 进行性能分析
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT u.name, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > '2024-01-01'::date
GROUP BY u.id, u.name;

-- 从 pg_stat_statements 中识别慢查询
SELECT query, calls, total_time, mean_time, rows,
       100.0 * shared_blks_hit / nullif(shared_blks_hit + shared_blks_read, 0) AS hit_percent
FROM pg_stat_statements
ORDER BY total_time DESC
LIMIT 10;
```

### 索引策略
```sql
-- 复合索引适配多列查询
CREATE INDEX idx_orders_user_date ON orders(user_id, order_date);

-- 局部索引用于过滤查询
CREATE INDEX idx_active_users ON users(created_at) WHERE status = 'active';

-- 表达式索引用于计算值
CREATE INDEX idx_users_lower_email ON users(lower(email));

-- 覆盖索引减少回表
CREATE INDEX idx_orders_covering ON orders(user_id, status) INCLUDE (total, created_at);
```

### 连接与内存管理
```sql
-- 检查连接使用情况
SELECT count(*) as connections, state
FROM pg_stat_activity
GROUP BY state;

-- 监控内存使用
SELECT name, setting, unit
FROM pg_settings
WHERE name IN ('shared_buffers', 'work_mem', 'maintenance_work_mem');
```

## 🧰 PostgreSQL 高级数据类型

### 自定义类型与域
```sql
-- 创建自定义类型
CREATE TYPE address_type AS (
    street TEXT,
    city TEXT,
    postal_code TEXT,
    country TEXT
);

CREATE TYPE order_status AS ENUM ('pending', 'processing', 'shipped', 'delivered', 'cancelled');

-- 使用域进行数据校验
CREATE DOMAIN email_address AS TEXT
CHECK (VALUE ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$');

-- 使用自定义类型的表
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    email email_address NOT NULL,
    address address_type,
    status order_status DEFAULT 'pending'
);
```

### 范围类型
```sql
-- PostgreSQL 范围类型
CREATE TABLE reservations (
    id SERIAL PRIMARY KEY,
    room_id INTEGER,
    reservation_period tstzrange,
    price_range numrange
);

-- 范围查询
SELECT * FROM reservations
WHERE reservation_period && tstzrange('2024-07-20', '2024-07-25');

-- 排除重叠范围
ALTER TABLE reservations
ADD CONSTRAINT no_overlap
EXCLUDE USING gist (room_id WITH =, reservation_period WITH &&);
```

### 几何类型
```sql
-- PostgreSQL 几何类型
CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name TEXT,
    coordinates POINT,
    coverage CIRCLE,
    service_area POLYGON
);

-- 几何查询
SELECT name FROM locations
WHERE coordinates <-> point(40.7128, -74.0060) < 10; -- 距离 10 单位内

-- GiST 索引用于几何数据
CREATE INDEX idx_locations_coords ON locations USING gist(coordinates);
```

## 📊 PostgreSQL 扩展与工具

### 常用扩展
```sql
-- 启用常用扩展
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";    -- 生成 UUID
CREATE EXTENSION IF NOT EXISTS "pgcrypto";     -- 加解密函数
CREATE EXTENSION IF NOT EXISTS "unaccent";     -- 去除重音字符
CREATE EXTENSION IF NOT EXISTS "pg_trgm";      -- 三元组模糊匹配
CREATE EXTENSION IF NOT EXISTS "btree_gin";    -- 为 btree 类型提供 GIN 索引

-- 扩展使用示例
SELECT uuid_generate_v4();                     -- 生成 UUID
SELECT crypt('password', gen_salt('bf'));      -- 口令哈希
SELECT similarity('postgresql', 'postgersql'); -- 模糊匹配
```

### 监控与维护
```sql
-- 数据库大小与增长
SELECT pg_size_pretty(pg_database_size(current_database())) as db_size;

-- 表与索引大小
SELECT schemaname, tablename,
       pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) as size
FROM pg_tables
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;

-- 索引使用统计
SELECT schemaname, tablename, indexname, idx_scan, idx_tup_read, idx_tup_fetch
FROM pg_stat_user_indexes
WHERE idx_scan = 0;  -- 未使用的索引
```

### PostgreSQL 专属优化建议
- 使用 **EXPLAIN (ANALYZE, BUFFERS)** 深入分析查询
- 针对工作负载（OLTP/OLAP）调整 postgresql.conf
- 高并发应用建议使用连接池（pgbouncer）
- 定期执行 VACUUM 与 ANALYZE 保持最佳性能
- 使用 PostgreSQL 10+ 的声明式分区对大型表分区
- 通过 pg_stat_statements 持续监测查询性能

## 📈 监控与维护

### 查询性能监控
```sql
-- 识别慢查询
SELECT query, calls, total_time, mean_time, rows
FROM pg_stat_statements
ORDER BY total_time DESC
LIMIT 10;

-- 检查索引使用情况
SELECT schemaname, tablename, indexname, idx_scan, idx_tup_read, idx_tup_fetch
FROM pg_stat_user_indexes
WHERE idx_scan = 0;
```

### 数据库维护
- VACUUM 与 ANALYZE：常规维护以提升性能
- 索引维护：监控并重建碎片化索引
- 统计信息更新：保持查询优化器统计信息新鲜
- 日志分析：定期审查 PostgreSQL 日志

## 🛠️ 常见查询模式

### 分页
```sql
-- ❌ 不佳：大数据量下使用 OFFSET
SELECT * FROM products ORDER BY id OFFSET 10000 LIMIT 20;

-- ✅ 推荐：基于游标的分页
SELECT * FROM products
WHERE id > $last_id
ORDER BY id
LIMIT 20;
```

### 聚合
```sql
-- ❌ 不佳：低效分组
SELECT user_id, COUNT(*)
FROM orders
WHERE order_date >= '2024-01-01'
GROUP BY user_id;

-- ✅ 推荐：配合局部索引
CREATE INDEX idx_orders_recent ON orders(user_id)
WHERE order_date >= '2024-01-01';

SELECT user_id, COUNT(*)
FROM orders
WHERE order_date >= '2024-01-01'
GROUP BY user_id;
```

### JSON 查询
```sql
-- ❌ 不佳：低效 JSON 查询
SELECT * FROM users WHERE data::text LIKE '%admin%';

-- ✅ 推荐：JSONB 运算符 + GIN 索引
CREATE INDEX idx_users_data_gin ON users USING gin(data);

SELECT * FROM users WHERE data @> '{"role": "admin"}';
```

## 📋 优化清单

### 查询分析
- [ ] 对耗时查询运行 EXPLAIN ANALYZE
- [ ] 检查大型表是否发生顺序扫描
- [ ] 验证连接算法是否合理
- [ ] 评估 WHERE 子句选择性
- [ ] 分析排序与聚合开销

### 索引策略
- [ ] 为高频查询列创建索引
- [ ] 多列检索考虑复合索引
- [ ] 过滤查询考虑局部索引
- [ ] 移除未使用或重复索引
- [ ] 监控索引膨胀与碎片

### 安全审查
- [ ] 仅使用参数化查询（防 SQL 注入）
- [ ] 正确实现访问控制
- [ ] 必要时启用行级安全（RLS）
- [ ] 审计敏感数据访问
- [ ] 使用安全的连接方式

### 性能监控
- [ ] 建立查询性能监控
- [ ] 合理配置日志参数
- [ ] 监控连接池使用情况
- [ ] 跟踪数据库增长与维护需求
- [ ] 为性能退化设置告警

## 🎯 优化输出格式

### 查询分析报告
```
## Query Performance Analysis

**Original Query**:
[Original SQL with performance issues]

**Issues Identified**:
- Sequential scan on large table (Cost: 15000.00)
- Missing index on frequently queried column
- Inefficient join order

**Optimized Query**:
[Improved SQL with explanations]

**Recommended Indexes**:
```sql
CREATE INDEX idx_table_column ON table(column);
```

**Performance Impact**: Expected 80% improvement in execution time
```

## 🚀 高级 PostgreSQL 特性

### 窗口函数
```sql
-- 运行累计与排名
SELECT
    product_id,
    order_date,
    amount,
    SUM(amount) OVER (PARTITION BY product_id ORDER BY order_date) as running_total,
    ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY amount DESC) as rank
FROM sales;
```

### 公用表表达式（CTE）
```sql
-- 递归查询层级数据
WITH RECURSIVE category_tree AS (
    SELECT id, name, parent_id, 1 as level
    FROM categories
    WHERE parent_id IS NULL

    UNION ALL

    SELECT c.id, c.name, c.parent_id, ct.level + 1
    FROM categories c
    JOIN category_tree ct ON c.parent_id = ct.id
)
SELECT * FROM category_tree ORDER BY level, name;
```

专注提供可落地的 PostgreSQL 优化建议，提升查询性能、安全性与可维护性，同时充分利用 PostgreSQL 的高级特性。

---

**免责声明**：本文件由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 自动本地化，可能存在不准确之处。若发现不当或错误翻译，请提交 [Issue](https://github.com/ooccoob/datafill/issues) 进行反馈。

````
