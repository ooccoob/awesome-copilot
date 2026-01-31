---
代理人：“代理人”
工具：['更改'、'搜索/代码库'、'编辑/编辑文件'、'问题']
描述：“通用 SQL 代码审查助手，可跨所有 SQL 数据库（MySQL、PostgreSQL、SQL Server、Oracle）执行全面的安全性、可维护性和代码质量分析。重点关注 SQL 注入预防、访问控制、代码标准和反模式检测。补充 SQL 优化提示以实现完整的开发覆盖。
ated_with: 'GitHub Copilot Chat (GPT-4o) - 2025 年 7 月 20 日验证'
---

# SQL 代码审查

对 ${selection}（或整个项目，如果没有选择）执行彻底的 SQL 代码审查，重点关注安全性、性能、可维护性和数据库最佳实践。

## 🔒 安全分析

### SQL注入预防
```sql
-- ❌ CRITICAL: SQL Injection vulnerability
query = "SELECT * FROM users WHERE id = " + userInput;
query = f"DELETE FROM orders WHERE user_id = {user_id}";

-- ✅ SECURE: Parameterized queries
-- PostgreSQL/MySQL
PREPARE stmt FROM 'SELECT * FROM users WHERE id = ?';
EXECUTE stmt USING @user_id;

-- SQL Server
EXEC sp_executesql N'SELECT * FROM users WHERE id = @id', N'@id INT', @id = @user_id;
```

### 访问控制和权限
- **最小权限原则**：授予所需的最低权限
- **基于角色的访问**：使用数据库角色而不是直接用户权限
- **架构安全**：正确的架构所有权和访问控制
- **函数/过程安全性**：查看 DEFINER 与 INVOKER 权限

### 数据保护
- **敏感数据暴露**：避免在具有敏感列的表上使用 SELECT *
- **审核日志记录**：确保记录敏感操作
- **数据屏蔽**：使用视图或函数屏蔽敏感数据
- **加密**：验证敏感数据的加密存储

## ⚡ 性能优化

### 查询结构分析
```sql
-- ❌ BAD: Inefficient query patterns
SELECT DISTINCT u.* 
FROM users u, orders o, products p
WHERE u.id = o.user_id 
AND o.product_id = p.id
AND YEAR(o.order_date) = 2024;

-- ✅ GOOD: Optimized structure
SELECT u.id, u.name, u.email
FROM users u
INNER JOIN orders o ON u.id = o.user_id
WHERE o.order_date >= '2024-01-01' 
AND o.order_date < '2025-01-01';
```

### 指数策略回顾
- **缺少索引**：识别需要索引的列
- **过度索引**：查找未使用或冗余的索引
- **复合索引**：复杂查询的多列索引
- **索引维护**：检查碎片或过时的索引

### 加盟优化
- **连接类型**：验证适当的连接类型（INNER、LEFT、EXISTS）
- **连接顺序**：首先针对较小的结果集进行优化
- **笛卡尔积**：识别并修复缺失的连接条件
- **子查询与 JOIN**：选择最有效的方法

### 聚合和窗口函数
```sql
-- ❌ BAD: Inefficient aggregation
SELECT user_id, 
       (SELECT COUNT(*) FROM orders o2 WHERE o2.user_id = o1.user_id) as order_count
FROM orders o1
GROUP BY user_id;

-- ✅ GOOD: Efficient aggregation
SELECT user_id, COUNT(*) as order_count
FROM orders
GROUP BY user_id;
```

## 🛠️ 代码质量和可维护性

### SQL 样式和格式
```sql
-- ❌ BAD: Poor formatting and style
select u.id,u.name,o.total from users u left join orders o on u.id=o.user_id where u.status='active' and o.order_date>='2024-01-01';

-- ✅ GOOD: Clean, readable formatting
SELECT u.id,
       u.name,
       o.total
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.status = 'active'
  AND o.order_date >= '2024-01-01';
```

### 命名约定
- **一致的命名**：表、列、约束遵循一致的模式
- **描述性名称**：数据库对象的清晰、有意义的名称
- **保留字**：避免使用数据库保留字作为标识符
- **区分大小写**：跨架构的大小写使用一致

### 架构设计审查
- **标准化**：适当的标准化水平（避免过度/标准化不足）
- **数据类型**：存储和性能的最佳数据类型选择
- **约束**：正确使用 PRIMARY KEY、FOREIGN KEY、CHECK、NOT NULL
- **默认值**：列的适当默认值

## 🗄️特定于数据库的最佳实践

### PostgreSQL
```sql
-- Use JSONB for JSON data
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    data JSONB NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- GIN index for JSONB queries
CREATE INDEX idx_events_data ON events USING gin(data);

-- Array types for multi-value columns
CREATE TABLE tags (
    post_id INT,
    tag_names TEXT[]
);
```

### MySQL
```sql
-- Use appropriate storage engines
CREATE TABLE sessions (
    id VARCHAR(128) PRIMARY KEY,
    data TEXT,
    expires TIMESTAMP
) ENGINE=InnoDB;

-- Optimize for InnoDB
ALTER TABLE large_table 
ADD INDEX idx_covering (status, created_at, id);
```

### SQL服务器
```sql
-- Use appropriate data types
CREATE TABLE products (
    id BIGINT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    created_at DATETIME2 DEFAULT GETUTCDATE()
);

-- Columnstore indexes for analytics
CREATE COLUMNSTORE INDEX idx_sales_cs ON sales;
```

### 甲骨文
```sql
-- Use sequences for auto-increment
CREATE SEQUENCE user_id_seq START WITH 1 INCREMENT BY 1;

CREATE TABLE users (
    id NUMBER DEFAULT user_id_seq.NEXTVAL PRIMARY KEY,
    name VARCHAR2(255) NOT NULL
);
```

## 🧪 测试和验证

### 数据完整性检查
```sql
-- Verify referential integrity
SELECT o.user_id 
FROM orders o 
LEFT JOIN users u ON o.user_id = u.id 
WHERE u.id IS NULL;

-- Check for data consistency
SELECT COUNT(*) as inconsistent_records
FROM products 
WHERE price < 0 OR stock_quantity < 0;
```

### 性能测试
- **执行计划**：查看查询执行计划
- **负载测试**：使用实际数据量测试查询
- **压力测试**：验证并发负载下的性能
- **回归测试**：确保优化不会破坏功能

## 📊 常见反模式

### N+1查询问题
```sql
-- ❌ BAD: N+1 queries in application code
for user in users:
    orders = query("SELECT * FROM orders WHERE user_id = ?", user.id)

-- ✅ GOOD: Single optimized query
SELECT u.*, o.*
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;
```

### 过度使用 DISTINCT
```sql
-- ❌ BAD: DISTINCT masking join issues
SELECT DISTINCT u.name 
FROM users u, orders o 
WHERE u.id = o.user_id;

-- ✅ GOOD: Proper join without DISTINCT
SELECT u.name
FROM users u
INNER JOIN orders o ON u.id = o.user_id
GROUP BY u.name;
```

### WHERE 子句中的函数误用
```sql
-- ❌ BAD: Functions prevent index usage
SELECT * FROM orders 
WHERE YEAR(order_date) = 2024;

-- ✅ GOOD: Range conditions use indexes
SELECT * FROM orders 
WHERE order_date >= '2024-01-01' 
  AND order_date < '2025-01-01';
```

## 📋 SQL 审查清单

### 安全性
- [ ] 所有用户输入均已参数化
- [ ] 没有使用字符串连接的动态 SQL 构造
- [ ] 适当的访问控制和权限
- [ ] 敏感数据得到妥善保护
- [ ] SQL注入攻击媒介被消除

### 性能
- [ ] 经常查询的列存在索引
- [ ] 没有不必要的 SELECT * 语句
- [ ] JOIN 已优化并使用适当的类型
- [ ] WHERE 子句是选择性的并使用索引
- [ ] 子查询被优化或转换为 JOIN

### 代码质量
- [ ] 一致的命名约定
- [ ] 正确的格式和缩进
- [ ] 复杂逻辑有意义的注释
- [ ] 使用适当的数据类型
- [ ] 实施错误处理

### 架构设计
- [ ] 表已正确标准化
- [ ] 约束强制数据完整性
- [ ] 索引支持查询模式
- [ ] 外键关系定义
- [ ] 默认值合适

## 🎯 检查输出格式

### 问题模板
```
## [PRIORITY] [CATEGORY]: [Brief Description]

**Location**: [Table/View/Procedure name and line number if applicable]
**Issue**: [Detailed explanation of the problem]
**Security Risk**: [If applicable - injection risk, data exposure, etc.]
**Performance Impact**: [Query cost, execution time impact]
**Recommendation**: [Specific fix with code example]

**Before**:
```sql
-- 有问题的 SQL
```

**After**:
```sql
-- 改进的 SQL
```

**Expected Improvement**: [Performance gain, security benefit]
```

### 总结评估
- **安全评分**：[1-10] - SQL注入保护、访问控制
- **性能得分**：[1-10] - 查询效率、索引使用情况
- **可维护性得分**：[1-10] - 代码质量、文档
- **模式质量得分**：[1-10] - 设计模式、规范化

### 3 大优先行动
1. **[重要安全修复]**：解决 SQL 注入漏洞
2. **【性能优化】**：添加缺失索引或优化查询
3. **[代码质量]**：改进命名约定和文档

专注于提供可操作的、与数据库无关的建议，同时强调特定于平台的优化和最佳实践。
