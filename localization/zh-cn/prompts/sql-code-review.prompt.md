````prompt
---
mode: 'agent'
tools: ['changes', 'codebase', 'editFiles', 'problems']
description: '面向所有主流 SQL 数据库（MySQL、PostgreSQL、SQL Server、Oracle）的通用 SQL 代码评审助手，从安全、性能、可维护性与最佳实践等方面进行全面审查。聚焦 SQL 注入防护、访问控制、代码规范与反模式检测，并与 SQL 优化提示互补。'
tested_with: 'GitHub Copilot Chat (GPT-4o) - Validated July 20, 2025'
---

# SQL 代码评审

对 ${selection} 进行全面 SQL 代码评审（若未选择则面向整个项目），重点关注安全性、性能、可维护性与数据库最佳实践。

## 🔒 安全分析

### SQL 注入防护
```sql
-- ❌ 严重：存在 SQL 注入风险
query = "SELECT * FROM users WHERE id = " + userInput;
query = f"DELETE FROM orders WHERE user_id = {user_id}";

-- ✅ 安全：使用参数化查询
-- PostgreSQL/MySQL
PREPARE stmt FROM 'SELECT * FROM users WHERE id = ?';
EXECUTE stmt USING @user_id;

-- SQL Server
EXEC sp_executesql N'SELECT * FROM users WHERE id = @id', N'@id INT', @id = @user_id;
```

### 访问控制与权限
- 最小权限原则：仅授予必要权限
- 角色化访问：优先使用角色而非直接赋权
- 架构安全：合理的 schema 所有权与访问控制
- 函数/过程安全：审查 DEFINER vs INVOKER 权限

### 数据保护
- 敏感数据暴露：避免在含敏感列的表上 SELECT *
- 审计日志：确保敏感操作有审计
- 数据脱敏：使用视图或函数脱敏
- 加密：敏感数据的加密存储

## ⚡ 性能优化

### 查询结构分析
```sql
-- ❌ 不佳：低效结构
SELECT DISTINCT u.*
FROM users u, orders o, products p
WHERE u.id = o.user_id
AND o.product_id = p.id
AND YEAR(o.order_date) = 2024;

-- ✅ 推荐：清晰结构与可索引条件
SELECT u.id, u.name, u.email
FROM users u
INNER JOIN orders o ON u.id = o.user_id
WHERE o.order_date >= '2024-01-01'
AND o.order_date < '2025-01-01';
```

### 索引策略审查
- 缺失索引：识别需要索引的列
- 过度索引：清理未用/冗余索引
- 复合索引：多列检索的序设计
- 索引维护：检查碎片与过期统计

### JOIN 优化
- JOIN 类型：核对 INNER/LEFT/EXISTS 的适用性
- JOIN 顺序：先处理小集合
- 笛卡尔积：修复缺失连接条件
- 子查询 vs JOIN：选择更优方案

### 聚合/窗口函数
```sql
-- ❌ 不佳：低效聚合
SELECT user_id,
       (SELECT COUNT(*) FROM orders o2 WHERE o2.user_id = o1.user_id) as order_count
FROM orders o1
GROUP BY user_id;

-- ✅ 推荐：一次聚合
SELECT user_id, COUNT(*) as order_count
FROM orders
GROUP BY user_id;
```

## 🧰 代码质量与可维护性

### SQL 风格与格式
```sql
-- ❌ 不佳：可读性差
select u.id,u.name,o.total from users u left join orders o on u.id=o.user_id where u.status='active' and o.order_date>='2024-01-01';

-- ✅ 推荐：整洁易读
SELECT u.id,
       u.name,
       o.total
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.status = 'active'
  AND o.order_date >= '2024-01-01';
```

### 命名约定
- 一致的命名：表、列、约束遵循统一规则
- 具描述性的名称：清晰表达含义
- 避免保留字：不要使用保留字作为标识符
- 大小写一致：全局保持一致

### 模型与架构审查
- 范式：适度范式化（避免过度/不足）
- 数据类型：存储与性能兼顾
- 约束：恰当使用 PK/FK/CHECK/NOT NULL
- 默认值：合理设置默认值

## 📚 数据库特定最佳实践

### PostgreSQL
```sql
-- 使用 JSONB 存储 JSON
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    data JSONB NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- JSONB 的 GIN 索引
CREATE INDEX idx_events_data ON events USING gin(data);

-- 数组类型用于多值
CREATE TABLE tags (
    post_id INT,
    tag_names TEXT[]
);
```

### MySQL
```sql
-- 选择合适的存储引擎
CREATE TABLE sessions (
    id VARCHAR(128) PRIMARY KEY,
    data TEXT,
    expires TIMESTAMP
) ENGINE=InnoDB;

-- InnoDB 优化示例
ALTER TABLE large_table
ADD INDEX idx_covering (status, created_at, id);
```

### SQL Server
```sql
-- 合理的数据类型选择
CREATE TABLE products (
    id BIGINT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    created_at DATETIME2 DEFAULT GETUTCDATE()
);

-- 列存储索引用于分析场景
CREATE COLUMNSTORE INDEX idx_sales_cs ON sales;
```

### Oracle
```sql
-- 使用序列实现自增
CREATE SEQUENCE user_id_seq START WITH 1 INCREMENT BY 1;

CREATE TABLE users (
    id NUMBER DEFAULT user_id_seq.NEXTVAL PRIMARY KEY,
    name VARCHAR2(255) NOT NULL
);
```

## 🧪 测试与验证

### 数据一致性检查
```sql
-- 参照完整性
SELECT o.user_id
FROM orders o
LEFT JOIN users u ON o.user_id = u.id
WHERE u.id IS NULL;

-- 基础一致性
SELECT COUNT(*) as inconsistent_records
FROM products
WHERE price < 0 OR stock_quantity < 0;
```

### 性能测试
- 执行计划：审查并记录
- 负载测试：使用真实数据量
- 压力测试：并发下验证
- 回归测试：优化不破坏功能

## 🚫 常见反模式

### N+1 查询
```sql
-- ❌ 不佳：应用层 N+1
for user in users:
    orders = query("SELECT * FROM orders WHERE user_id = ?", user.id)

-- ✅ 推荐：一次性查询
SELECT u.*, o.*
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;
```

### 过度使用 DISTINCT
```sql
-- ❌ 不佳：用 DISTINCT 掩盖连接问题
SELECT DISTINCT u.name
FROM users u, orders o
WHERE u.id = o.user_id;

-- ✅ 推荐：正确连接 + GROUP BY
SELECT u.name
FROM users u
INNER JOIN orders o ON u.id = o.user_id
GROUP BY u.name;
```

### WHERE 中函数误用
```sql
-- ❌ 不佳：函数导致索引失效
SELECT * FROM orders
WHERE YEAR(order_date) = 2024;

-- ✅ 推荐：范围查询可用索引
SELECT * FROM orders
WHERE order_date >= '2024-01-01'
  AND order_date < '2025-01-01';
```

## 📝 评审输出模板

### 问题条目模板
```
## [PRIORITY] [CATEGORY]: [Brief Description]

**Location**: [对象名及必要的行号]
**Issue**: [问题详述]
**Security Risk**: [若适用]
**Performance Impact**: [成本/耗时影响]
**Recommendation**: [具体修复建议与示例]

**Before**:
```sql
-- 有问题的 SQL
```

**After**:
```sql
-- 改进后的 SQL
```

**Expected Improvement**: [性能/安全收益]
```

### 汇总评估
- 安全分： [1-10]
- 性能分： [1-10]
- 可维护性分： [1-10]
- 模型设计分： [1-10]

### 三个最高优先级行动
1. 关键安全修复：清除 SQL 注入风险
2. 性能优化：补齐缺失索引或优化查询
3. 代码质量：统一命名与完善文档

提供可执行、与数据库无关的改进建议，并在适当位置点明平台特定优化与最佳实践。

---

**免责声明**：本文件由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 自动本地化，可能存在不准确之处。若发现不当或错误翻译，请提交 [Issue](https://github.com/ooccoob/datafill/issues) 进行反馈。

````
