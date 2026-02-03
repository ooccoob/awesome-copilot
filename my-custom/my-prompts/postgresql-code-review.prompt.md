---
agent: 'agent'
tools: ['changes', 'search/codebase', 'edit/editFiles', 'problems']
description: 'PostgreSQL-specific code review assistant focusing on PostgreSQL best practices, anti-patterns, and unique quality standards. Covers JSONB operations, array usage, custom types, schema design, function optimization, and PostgreSQL-exclusive security features like Row Level Security (RLS).'
tested_with: 'GitHub Copilot Chat (GPT-4o) - Validated July 20, 2025'
---

# PostgreSQL 代码审查助手

${selection} 的专家 PostgreSQL 代码审查（如果没有选择，则审查整个项目）。重点关注 PostgreSQL 特有的最佳实践、反模式和质量标准。

## 🎯 PostgreSQL 特定审核区域

### JSONB 最佳实践
```sql
-- ❌ BAD: Inefficient JSONB usage
SELECT * FROM orders WHERE data->>'status' = 'shipped';  -- No index support

-- ✅ GOOD: Indexable JSONB queries
CREATE INDEX idx_orders_status ON orders USING gin((data->'status'));
SELECT * FROM orders WHERE data @> '{"status": "shipped"}';

-- ❌ BAD: Deep nesting without consideration
UPDATE orders SET data = data || '{"shipping":{"tracking":{"number":"123"}}}';

-- ✅ GOOD: Structured JSONB with validation
ALTER TABLE orders ADD CONSTRAINT valid_status 
CHECK (data->>'status' IN ('pending', 'shipped', 'delivered'));
```

### 数组操作回顾
```sql
-- ❌ BAD: Inefficient array operations
SELECT * FROM products WHERE 'electronics' = ANY(categories);  -- No index

-- ✅ GOOD: GIN indexed array queries
CREATE INDEX idx_products_categories ON products USING gin(categories);
SELECT * FROM products WHERE categories @> ARRAY['electronics'];

-- ❌ BAD: Array concatenation in loops
-- This would be inefficient in a function/procedure

-- ✅ GOOD: Bulk array operations
UPDATE products SET categories = categories || ARRAY['new_category']
WHERE id IN (SELECT id FROM products WHERE condition);
```

### PostgreSQL 架构设计回顾
```sql
-- ❌ BAD: Not using PostgreSQL features
CREATE TABLE users (
    id INTEGER,
    email VARCHAR(255),
    created_at TIMESTAMP
);

-- ✅ GOOD: PostgreSQL-optimized schema
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    email CITEXT UNIQUE NOT NULL,  -- Case-insensitive email
    created_at TIMESTAMPTZ DEFAULT NOW(),
    metadata JSONB DEFAULT '{}',
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
);

-- Add JSONB GIN index for metadata queries
CREATE INDEX idx_users_metadata ON users USING gin(metadata);
```

### 自定义类型和域
```sql
-- ❌ BAD: Using generic types for specific data
CREATE TABLE transactions (
    amount DECIMAL(10,2),
    currency VARCHAR(3),
    status VARCHAR(20)
);

-- ✅ GOOD: PostgreSQL custom types
CREATE TYPE currency_code AS ENUM ('USD', 'EUR', 'GBP', 'JPY');
CREATE TYPE transaction_status AS ENUM ('pending', 'completed', 'failed', 'cancelled');
CREATE DOMAIN positive_amount AS DECIMAL(10,2) CHECK (VALUE > 0);

CREATE TABLE transactions (
    amount positive_amount NOT NULL,
    currency currency_code NOT NULL,
    status transaction_status DEFAULT 'pending'
);
```

## 🔍 PostgreSQL 特定的反模式

### 性能反模式
- **避免 PostgreSQL 特定索引**：不将 GIN/GiST 用于适当的数据类型
- **误用 JSONB**：将 JSONB 视为简单的字符串字段
- **忽略数组运算符**：使用低效的数组操作
- **分区键选择不当**：未有效利用 PostgreSQL 分区

### 架构设计问题
- **不使用 ENUM 类型**：对有限值集使用 VARCHAR
- **忽略约束**：缺少数据验证的 CHECK 约束
- **错误的数据类型**：使用 VARCHAR 而不是 TEXT 或 CITEXT
- **缺少 JSONB 结构**：未经验证的非结构化 JSONB

### 功能和触发问题
```sql
-- ❌ BAD: Inefficient trigger function
CREATE OR REPLACE FUNCTION update_modified_time()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();  -- Should use TIMESTAMPTZ
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- ✅ GOOD: Optimized trigger function
CREATE OR REPLACE FUNCTION update_modified_time()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Set trigger to fire only when needed
CREATE TRIGGER update_modified_time_trigger
    BEFORE UPDATE ON table_name
    FOR EACH ROW
    WHEN (OLD.* IS DISTINCT FROM NEW.*)
    EXECUTE FUNCTION update_modified_time();
```

## 📊 PostgreSQL 扩展使用回顾

### 扩展最佳实践
```sql
-- ✅ Check if extension exists before creating
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- ✅ Use extensions appropriately
-- UUID generation
SELECT uuid_generate_v4();

-- Password hashing
SELECT crypt('password', gen_salt('bf'));

-- Fuzzy text matching
SELECT word_similarity('postgres', 'postgre');
```

## 🛡️ PostgreSQL 安全审查

### 行级安全性 (RLS)
```sql
-- ✅ GOOD: Implementing RLS
ALTER TABLE sensitive_data ENABLE ROW LEVEL SECURITY;

CREATE POLICY user_data_policy ON sensitive_data
    FOR ALL TO application_role
    USING (user_id = current_setting('app.current_user_id')::INTEGER);
```

### 权限管理
```sql
-- ❌ BAD: Overly broad permissions
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO app_user;

-- ✅ GOOD: Granular permissions
GRANT SELECT, INSERT, UPDATE ON specific_table TO app_user;
GRANT USAGE ON SEQUENCE specific_table_id_seq TO app_user;
```

## 🎯 PostgreSQL 代码质量检查表

### 架构设计
- [ ] 使用适当的 PostgreSQL 数据类型（CITEXT、JSONB、数组）
- [ ] 利用 ENUM 类型获取约束值
- [ ] 实施适当的 CHECK 约束
- [ ] 使用 TIMESTAMPTZ 代替 TIMESTAMP
- [ ] 定义可重用约束的自定义域

### 性能考虑因素
- [ ] 适当的索引类型（GIN 用于 JSONB/数组，GiST 用于范围）
- [ ] 使用包含运算符（@>、?）的 JSONB 查询
- [ ] 使用 PostgreSQL 特定运算符的数组操作
- [ ] 正确使用窗函数和 CTE
- [ ] 高效使用 PostgreSQL 特定函数

### PostgreSQL 特性利用
- [ ] 在适当的情况下使用扩展
- [ ] 在 PL/pgSQL 中实现存储过程有益
- [ ] 利用 PostgreSQL 的高级 SQL 功能
- [ ] 使用 PostgreSQL 特定的优化技术
- [ ] 在函数中实现正确的错误处理

### 安全与合规性
- [ ] 需要时实施行级安全性 (RLS)
- [ ] 正确的角色和权限管理
- [ ] 使用PostgreSQL内置的加密函数
- [ ] 使用 PostgreSQL 功能实现审计跟踪

## 📝 PostgreSQL 特定审查指南

1. **数据类型优化**：确保正确使用 PostgreSQL 特定类型
2. **索引策略**：检查索引类型并确保使用 PostgreSQL 特定的索引
3. **JSONB 结构**：验证 JSONB 架构设计和查询模式
4. **函数质量**：审查 PL/pgSQL 函数的效率和最佳实践
5. **扩展使用**：验证 PostgreSQL 扩展的正确使用
6. **性能特性**：检查 PostgreSQL 高级特性的利用率
7. **安全实施**：查看 PostgreSQL 特定的安全功能

关注 PostgreSQL 的独特功能，并确保代码利用 PostgreSQL 的特殊之处，而不是将其视为通用 SQL 数据库。
