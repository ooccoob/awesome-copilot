---
mode: 'agent'
tools: ['changes', 'codebase', 'edit/editFiles', 'problems']
description: '通用SQL代码审查助手，对所有SQL数据库（MySQL、PostgreSQL、SQL Server、Oracle）进行全面的安全性、可维护性和代码质量分析。专注于SQL注入防护、访问控制、代码标准和反模式检测。补充SQL优化提示以获得完整的开发覆盖。'
tested_with: 'GitHub Copilot Chat (GPT-4o) - 验证日期2025年7月20日'
---

# SQL代码审查

对${selection}（如果没有选择则为整个项目）进行彻底的SQL代码审查，重点关注安全性、性能、可维护性和数据库最佳实践。

## 🔒 安全分析

### SQL注入防护
```sql
-- ❌ 关键：SQL注入漏洞
query = "SELECT * FROM users WHERE id = " + userInput;
query = f"DELETE FROM orders WHERE user_id = {user_id}";

-- ✅ 安全：参数化查询
-- PostgreSQL/MySQL
PREPARE stmt FROM 'SELECT * FROM users WHERE id = ?';
EXECUTE stmt USING @user_id;

-- SQL Server
EXEC sp_executesql N'SELECT * FROM users WHERE id = @id', N'@id INT', @id = @user_id;
```

### 访问控制和权限
- **最小权限原则**：授予最小所需权限
- **基于角色的访问**：使用数据库角色而不是直接用户权限
- **模式安全**：适当的模式所有权和访问控制
- **函数/过程安全**：审查DEFINER与INVOKER权限

### 数据保护
- **敏感数据暴露**：避免对具有敏感列的表使用SELECT *
- **审计日志**：确保敏感操作被记录
- **数据掩码**：使用视图或函数掩码敏感数据
- **加密**：验证敏感数据的加密存储

## ⚡ 性能优化

### 查询结构分析
```sql
-- ❌ 差：低效查询模式
SELECT DISTINCT u.*
FROM users u, orders o, products p
WHERE u.id = o.user_id
AND o.product_id = p.id
AND YEAR(o.order_date) = 2024;

-- ✅ 好：优化结构
SELECT u.id, u.name, u.email
FROM users u
INNER JOIN orders o ON u.id = o.user_id
WHERE o.order_date >= '2024-01-01'
AND o.order_date < '2025-01-01';
```

### 索引策略审查
- **缺失索引**：识别需要索引的列
- **过度索引**：查找未使用或冗余的索引
- **复合索引**：为复杂查询创建多列索引
- **索引维护**：检查碎片化或过时的索引

### JOIN优化
- **JOIN类型**：验证适当的JOIN类型（INNER vs LEFT vs EXISTS）
- **JOIN顺序**：优先优化较小结果集
- **笛卡尔积**：识别并修复缺失的JOIN条件
- **子查询vs JOIN**：选择最有效的方法

### 聚合和窗口函数
```sql
-- ❌ 差：低效聚合
SELECT user_id,
       (SELECT COUNT(*) FROM orders o2 WHERE o2.user_id = o1.user_id) as order_count
FROM orders o1
GROUP BY user_id;

-- ✅ 好：高效聚合
SELECT user_id, COUNT(*) as order_count
FROM orders
GROUP BY user_id;
```

## 🛠️ 代码质量和可维护性

### SQL样式和格式
```sql
-- ❌ 差：格式和样式不佳
select u.id,u.name,o.total from users u left join orders o on u.id=o.user_id where u.status='active' and o.order_date>='2024-01-01';

-- ✅ 好：清晰、可读的格式
SELECT u.id,
       u.name,
       o.total
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.status = 'active'
  AND o.order_date >= '2024-01-01';
```

### 命名约定
- **一致命名**：表、列、约束遵循一致的模式
- **描述性名称**：为数据库对象使用清晰、有意义的名称
- **保留字**：避免使用数据库保留字作为标识符
- **大小写敏感性**：在整个模式中保持一致的大小写使用

### 模式设计审查
- **规范化**：适当的规范化级别（避免过度/不足规范化）
- **数据类型**：选择存储和性能的最佳数据类型
- **约束**：正确使用PRIMARY KEY、FOREIGN KEY、CHECK、NOT NULL
- **默认值**：为列设置适当的默认值

## 🗄️ 数据库特定最佳实践

### PostgreSQL
```sql
-- 对JSON数据使用JSONB
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    data JSONB NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 为JSONB查询创建GIN索引
CREATE INDEX idx_events_data ON events USING gin(data);

-- 对多值列使用数组类型
CREATE TABLE tags (
    post_id INT,
    tag_names TEXT[]
);
```

### MySQL
```sql
-- 使用适当的存储引擎
CREATE TABLE sessions (
    id VARCHAR(128) PRIMARY KEY,
    data TEXT,
    expires TIMESTAMP
) ENGINE=InnoDB;

-- 为InnoDB优化
ALTER TABLE large_table
ADD INDEX idx_covering (status, created_at, id);
```

### SQL Server
```sql
-- 使用适当的数据类型
CREATE TABLE products (
    id BIGINT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    created_at DATETIME2 DEFAULT GETUTCDATE()
);

-- 为分析创建列存储索引
CREATE COLUMNSTORE INDEX idx_sales_cs ON sales;
```

### Oracle
```sql
-- 使用序列进行自增
CREATE SEQUENCE user_id_seq START WITH 1 INCREMENT BY 1;

CREATE TABLE users (
    id NUMBER DEFAULT user_id_seq.NEXTVAL PRIMARY KEY,
    name VARCHAR2(255) NOT NULL
);
```

## 🧪 测试和验证

### 数据完整性检查
```sql
-- 验证引用完整性
SELECT o.user_id
FROM orders o
LEFT JOIN users u ON o.user_id = u.id
WHERE u.id IS NULL;

-- 检查数据一致性
SELECT COUNT(*) as inconsistent_records
FROM products
WHERE price < 0 OR stock_quantity < 0;
```

### 性能测试
- **执行计划**：审查查询执行计划
- **负载测试**：使用真实数据量测试查询
- **压力测试**：验证并发负载下的性能
- **回归测试**：确保优化不会破坏功能

## 📊 常见反模式

### N+1查询问题
```sql
-- ❌ 差：应用程序代码中的N+1查询
for user in users:
    orders = query("SELECT * FROM orders WHERE user_id = ?", user.id)

-- ✅ 好：单个优化查询
SELECT u.*, o.*
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;
```

### 过度使用DISTINCT
```sql
-- ❌ 差：DISTINCT掩盖JOIN问题
SELECT DISTINCT u.name
FROM users u, orders o
WHERE u.id = o.user_id;

-- ✅ 好：正确的JOIN不使用DISTINCT
SELECT u.name
FROM users u
INNER JOIN orders o ON u.id = o.user_id
GROUP BY u.name;
```

### WHERE子句中的函数误用
```sql
-- ❌ 差：函数阻止索引使用
SELECT * FROM orders
WHERE YEAR(order_date) = 2024;

-- ✅ 好：范围条件使用索引
SELECT * FROM orders
WHERE order_date >= '2024-01-01'
  AND order_date < '2025-01-01';
```

## 📋 SQL审查清单

### 安全性
- [ ] 所有用户输入都已参数化
- [ ] 没有使用字符串连接的动态SQL构建
- [ ] 适当的访问控制和权限
- [ ] 敏感数据得到适当保护
- [ ] SQL注入攻击向量已消除

### 性能
- [ ] 为频繁查询的列创建了索引
- [ ] 没有不必要的SELECT *语句
- [ ] JOIN已优化并使用适当类型
- [ ] WHERE子句具有选择性并使用索引
- [ ] 子查询已优化或转换为JOIN

### 代码质量
- [ ] 一致的命名约定
- [ ] 适当的格式和缩进
- [ ] 为复杂逻辑提供有意义的注释
- [ ] 使用了适当的数据类型
- [ ] 实现了错误处理

### 模式设计
- [ ] 表已正确规范化
- [ ] 约束强制数据完整性
- [ ] 索引支持查询模式
- [ ] 定义了外键关系
- [ ] 默认值是适当的

## 🎯 审查输出格式

### 问题模板
```
## [优先级] [类别]：[简要描述]

**位置**：[表/视图/过程名称和适用行号]
**问题**：[问题的详细解释]
**安全风险**：[如适用 - 注入风险、数据暴露等]
**性能影响**：[查询成本、执行时间影响]
**建议**：[包含代码示例的具体修复方案]

**之前**：
```sql
-- 有问题的SQL
```

**之后**：
```sql
-- 改进的SQL
```

**预期改进**：[性能提升、安全效益]
```

### 摘要评估
- **安全评分**：[1-10] - SQL注入防护、访问控制
- **性能评分**：[1-10] - 查询效率、索引使用
- **可维护性评分**：[1-10] - 代码质量、文档
- **模式质量评分**：[1-10] - 设计模式、规范化

### 前3个优先行动
1. **[关键安全修复]**：解决SQL注入漏洞
2. **[性能优化]**：添加缺失索引或优化查询
3. **[代码质量]**：改进命名约定和文档

专注于提供可操作的、数据库无关的建议，同时突出平台特定的优化和最佳实践。