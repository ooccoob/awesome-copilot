---
mode: 'agent'
tools: ['changes', 'codebase', 'edit/editFiles', 'problems']
description: 'PostgreSQL专用代码审查助手，专注于PostgreSQL最佳实践、反模式和独特的质量标准。涵盖JSONB操作、数组使用、自定义类型、模式设计、函数优化和PostgreSQL独有安全功能如行级安全（RLS）。'
tested_with: 'GitHub Copilot Chat (GPT-4o) - 验证日期2025年7月20日'
---

# PostgreSQL代码审查助手

为${selection}（如果没有选择则为整个项目）提供专业PostgreSQL代码审查。专注于PostgreSQL特定的最佳实践、反模式和PostgreSQL独有的质量标准。

## 🎯 PostgreSQL特定审查领域

### JSONB最佳实践
```sql
-- ❌ 差：低效的JSONB使用
SELECT * FROM orders WHERE data->>'status' = 'shipped';  -- 无索引支持

-- ✅ 好：可索引的JSONB查询
CREATE INDEX idx_orders_status ON orders USING gin((data->'status'));
SELECT * FROM orders WHERE data @> '{"status": "shipped"}';

-- ❌ 差：不考虑深度嵌套
UPDATE orders SET data = data || '{"shipping":{"tracking":{"number":"123"}}}';

-- ✅ 好：带验证的结构化JSONB
ALTER TABLE orders ADD CONSTRAINT valid_status
CHECK (data->>'status' IN ('pending', 'shipped', 'delivered'));
```

### 数组操作审查
```sql
-- ❌ 差：低效的数组操作
SELECT * FROM products WHERE 'electronics' = ANY(categories);  -- 无索引

-- ✅ 好：GIN索引数组查询
CREATE INDEX idx_products_categories ON products USING gin(categories);
SELECT * FROM products WHERE categories @> ARRAY['electronics'];

-- ❌ 差：循环中的数组连接
-- 这在函数/过程中会低效

-- ✅ 好：批量数组操作
UPDATE products SET categories = categories || ARRAY['new_category']
WHERE id IN (SELECT id FROM products WHERE condition);
```

### PostgreSQL模式设计审查
```sql
-- ❌ 差：不使用PostgreSQL功能
CREATE TABLE users (
    id INTEGER,
    email VARCHAR(255),
    created_at TIMESTAMP
);

-- ✅ 好：PostgreSQL优化模式
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    email CITEXT UNIQUE NOT NULL,  -- 不区分大小写的邮箱
    created_at TIMESTAMPTZ DEFAULT NOW(),
    metadata JSONB DEFAULT '{}',
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
);

-- 为元数据查询添加JSONB GIN索引
CREATE INDEX idx_users_metadata ON users USING gin(metadata);
```

### 自定义类型和域
```sql
-- ❌ 差：对特定数据使用通用类型
CREATE TABLE transactions (
    amount DECIMAL(10,2),
    currency VARCHAR(3),
    status VARCHAR(20)
);

-- ✅ 好：PostgreSQL自定义类型
CREATE TYPE currency_code AS ENUM ('USD', 'EUR', 'GBP', 'JPY');
CREATE TYPE transaction_status AS ENUM ('pending', 'completed', 'failed', 'cancelled');
CREATE DOMAIN positive_amount AS DECIMAL(10,2) CHECK (VALUE > 0);

CREATE TABLE transactions (
    amount positive_amount NOT NULL,
    currency currency_code NOT NULL,
    status transaction_status DEFAULT 'pending'
);
```

## 🔍 PostgreSQL特定反模式

### 性能反模式
- **避免PostgreSQL特定索引**：不为适当数据类型使用GIN/GiST
- **误用JSONB**：将JSONB当作简单字符串字段处理
- **忽略数组操作符**：使用低效的数组操作
- **错误的分区键选择**：未有效利用PostgreSQL分区

### 模式设计问题
- **不使用ENUM类型**：对有限值集使用VARCHAR
- **忽略约束**：缺少数据验证的CHECK约束
- **错误的数据类型**：使用VARCHAR而不是TEXT或CITEXT
- **缺少JSONB结构**：无验证的非结构化JSONB

### 函数和触发器问题
```sql
-- ❌ 差：低效的触发器函数
CREATE OR REPLACE FUNCTION update_modified_time()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();  -- 应该使用TIMESTAMPTZ
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- ✅ 好：优化的触发器函数
CREATE OR REPLACE FUNCTION update_modified_time()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- 仅在需要时设置触发器触发
CREATE TRIGGER update_modified_time_trigger
    BEFORE UPDATE ON table_name
    FOR EACH ROW
    WHEN (OLD.* IS DISTINCT FROM NEW.*)
    EXECUTE FUNCTION update_modified_time();
```

## 📊 PostgreSQL扩展使用审查

### 扩展最佳实践
```sql
-- ✅ 创建前检查扩展是否存在
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- ✅ 适当使用扩展
-- UUID生成
SELECT uuid_generate_v4();

-- 密码哈希
SELECT crypt('password', gen_salt('bf'));

-- 模糊文本匹配
SELECT word_similarity('postgres', 'postgre');
```

## 🛡️ PostgreSQL安全审查

### 行级安全（RLS）
```sql
-- ✅ 好：实现RLS
ALTER TABLE sensitive_data ENABLE ROW LEVEL SECURITY;

CREATE POLICY user_data_policy ON sensitive_data
    FOR ALL TO application_role
    USING (user_id = current_setting('app.current_user_id')::INTEGER);
```

### 权限管理
```sql
-- ❌ 差：过于宽泛的权限
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO app_user;

-- ✅ 好：细粒度权限
GRANT SELECT, INSERT, UPDATE ON specific_table TO app_user;
GRANT USAGE ON SEQUENCE specific_table_id_seq TO app_user;
```

## 🎯 PostgreSQL代码质量清单

### 模式设计
- [ ] 使用适当的PostgreSQL数据类型（CITEXT、JSONB、数组）
- [ ] 为约束值利用ENUM类型
- [ ] 实现适当的CHECK约束
- [ ] 使用TIMESTAMPTZ而不是TIMESTAMP
- [ ] 为可重用约束定义自定义域

### 性能考虑
- [ ] 适当的索引类型（JSONB/数组使用GIN，范围使用GiST）
- [ ] JSONB查询使用包含操作符（@>、?）
- [ ] 使用PostgreSQL特定操作符进行数组操作
- [ ] 正确使用窗口函数和CTE
- [ ] 高效使用PostgreSQL特定函数

### PostgreSQL功能利用
- [ ] 在适当时使用扩展
- [ ] 在有益处时用PL/pgSQL实现存储过程
- [ ] 利用PostgreSQL的高级SQL功能
- [ ] 使用PostgreSQL特定优化技术
- [ ] 在函数中实现适当的错误处理

### 安全和合规
- [ ] 在需要时实现行级安全（RLS）
- [ ] 适当的角色和权限管理
- [ ] 使用PostgreSQL内置加密函数
- [ ] 使用PostgreSQL功能实现审计跟踪

## 📝 PostgreSQL特定审查指南

1. **数据类型优化**：确保PostgreSQL特定类型被适当使用
2. **索引策略**：审查索引类型并确保PostgreSQL特定索引被利用
3. **JSONB结构**：验证JSONB模式设计和查询模式
4. **函数质量**：审查PL/pgSQL函数的效率和最佳实践
5. **扩展使用**：验证PostgreSQL扩展的适当使用
6. **性能功能**：检查PostgreSQL高级功能的利用
7. **安全实现**：审查PostgreSQL特定安全功能

专注于PostgreSQL的独特能力，并确保代码利用使PostgreSQL特殊的功能，而不是将其视为通用SQL数据库。