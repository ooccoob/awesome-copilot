---
描述：“可以使用 GitHub Copilot 为任何项目自定义通用代码审查说明”
适用于：'**'
排除代理：[“编码代理”]
---

# 通用代码审查说明

适用于 GitHub Copilot 的全面代码审查指南，可适用于任何项目。这些说明遵循即时工程的最佳实践，并提供代码质量、安全性、测试和架构审查的结构化方法。

## 评论语言

执行代码审查时，请用 **英语** 回复（或指定您的首选语言）。

> **自定义提示**：将“英语”替换为“葡萄牙语（巴西）”、“西班牙语”、“法语”等，更改为您的首选语言。

## 审查优先事项

执行代码审查时，请按以下顺序确定问题的优先级：

### 🔴 关键（块合并）
- **安全**：漏洞、暴露的秘密、身份验证/授权问题
- **正确性**：逻辑错误、数据损坏风险、竞争条件
- **重大变更**：API 合约更改，无需版本控制
- **数据丢失**：数据丢失或损坏的风险

### 🟡 重要（需要讨论）
- **代码质量**：严重违反SOLID原则，过度重复
- **测试覆盖率**：缺少关键路径或新功能的测试
- **性能**：明显的性能瓶颈（N+1查询、内存泄漏）
- **架构**：与既定模式的显着偏差

### 🟢 建议（非阻塞改进）
- **可读性**：命名不佳，逻辑复杂，可以简化
- **优化**：性能改进而不影响功能
- **最佳实践**：与惯例的微小偏差
- **文档**：注释/文档缺失或不完整

## 一般审查原则

执行代码审查时，请遵循以下原则：

1. **具体**：参考确切的行、文件，并提供具体示例
2. **提供背景**：解释为什么某件事是一个问题以及潜在的影响
3. **建议解决方案**：在适用时显示更正的代码，而不仅仅是错误的地方
4. **具有建设性**：专注于改进代码，而不是批评作者
5. **认可良好实践**：认可编写良好的代码和智能解决方案
6. **务实**：并非每项建议都需要立即实施
7. **对相关评论进行分组**：避免对同一主题进行多条评论

## 代码质量标准

执行代码审查时，请检查：

### 干净的代码
- 变量、函数和类的描述性且有意义的名称
- 单一职责原则：每个函数/类只做好一件事
- DRY（Don’t Repeat Yourself）：无代码重复
- 函数应该小而集中（最好 < 20-30 行）
- 避免深度嵌套代码（最多 3-4 层）
- 避免使用幻数和字符串（使用常量）
- 代码应该是自记录的；仅在必要时发表评论

### 示例
```javascript
// ❌ BAD: Poor naming and magic numbers
function calc(x, y) {
    if (x > 100) return y * 0.15;
    return y * 0.10;
}

// ✅ GOOD: Clear naming and constants
const PREMIUM_THRESHOLD = 100;
const PREMIUM_DISCOUNT_RATE = 0.15;
const STANDARD_DISCOUNT_RATE = 0.10;

function calculateDiscount(orderTotal, itemPrice) {
    const isPremiumOrder = orderTotal > PREMIUM_THRESHOLD;
    const discountRate = isPremiumOrder ? PREMIUM_DISCOUNT_RATE : STANDARD_DISCOUNT_RATE;
    return itemPrice * discountRate;
}
```

### 错误处理
- 在适当的级别进行适当的错误处理
- 有意义的错误消息
- 没有静默失败或被忽略的异常
- 快速失败：尽早验证输入
- 使用适当的错误类型/异常

### 示例
```python
# ❌ BAD: Silent failure and generic error
def process_user(user_id):
    try:
        user = db.get(user_id)
        user.process()
    except:
        pass

# ✅ GOOD: Explicit error handling
def process_user(user_id):
    if not user_id or user_id <= 0:
        raise ValueError(f"Invalid user_id: {user_id}")

    try:
        user = db.get(user_id)
    except UserNotFoundError:
        raise UserNotFoundError(f"User {user_id} not found in database")
    except DatabaseError as e:
        raise ProcessingError(f"Failed to retrieve user {user_id}: {e}")

    return user.process()
```

## 安全审查

执行代码审查时，检查安全问题：

- **敏感数据**：代码或日志中没有密码、API 密钥、令牌或 PII
- **输入验证**：所有用户输入都经过验证和清理
- **SQL注入**：使用参数化查询，从不使用字符串连接
- **身份验证**：访问资源之前进行适当的身份验证检查
- **授权**：验证用户是否有权执行操作
- **密码学**：使用已建立的库，切勿推出自己的加密货币
- **依赖项安全**：检查依赖项中的已知漏洞

### 示例
```java
// ❌ BAD: SQL injection vulnerability
String query = "SELECT * FROM users WHERE email = '" + email + "'";

// ✅ GOOD: Parameterized query
PreparedStatement stmt = conn.prepareStatement(
    "SELECT * FROM users WHERE email = ?"
);
stmt.setString(1, email);
```

```javascript
// ❌ BAD: Exposed secret in code
const API_KEY = "sk_live_abc123xyz789";

// ✅ GOOD: Use environment variables
const API_KEY = process.env.API_KEY;
```

## 检测标准

执行代码审查时，验证测试质量：

- **覆盖率**：关键路径和新功能必须经过测试
- **测试名称**：描述性名称，解释正在测试的内容
- **测试结构**：清晰的 Arrange-Act-Assert 或 Give-When-Then 模式
- **独立性**：测试不应依赖于彼此或外部状态
- **断言**：使用特定的断言，避免通用的assertTrue/assertFalse
- **边缘情况**：测试边界条件、空值、空集合
- **适当模拟**：模拟外部依赖项，而不是域逻辑

### 示例
```typescript
// ❌ BAD: Vague name and assertion
test('test1', () => {
    const result = calc(5, 10);
    expect(result).toBeTruthy();
});

// ✅ GOOD: Descriptive name and specific assertion
test('should calculate 10% discount for orders under $100', () => {
    const orderTotal = 50;
    const itemPrice = 20;

    const discount = calculateDiscount(orderTotal, itemPrice);

    expect(discount).toBe(2.00);
});
```

## 性能考虑因素

执行代码审查时，检查性能问题：

- **数据库查询**：避免 N+1 查询，使用适当的索引
- **算法**：适合用例的时间/空间复杂度
- **缓存**：利用缓存进行昂贵或重复的操作
- **资源管理**：正确清理连接、文件、流
- **分页**：大型结果集应该分页
- **延迟加载**：仅在需要时加载数据

### 示例
```python
# ❌ BAD: N+1 query problem
users = User.query.all()
for user in users:
    orders = Order.query.filter_by(user_id=user.id).all()  # N+1!

# ✅ GOOD: Use JOIN or eager loading
users = User.query.options(joinedload(User.orders)).all()
for user in users:
    orders = user.orders
```

## 建筑与设计

执行代码审查时，验证架构原则：

- **关注点分离**：层/模块之间的清晰界限
- **依赖方向**：高层模块不依赖于低层细节
- **界面隔离**：更喜欢小型、集中的界面
- **松耦合**：组件应该是可独立测试的
- **高内聚**：相关功能组合在一起
- **一致的模式**：遵循代码库中既定的模式

## 文件标准

执行代码审查时，请检查文档：

- **API 文档**：必须记录公共 API（用途、参数、返回）
- **复杂逻辑**：不明显的逻辑应该有解释性注释
- **自述文件更新**：添加功能或更改设置时更新自述文件
- **重大变更**：清楚地记录任何重大变更
- **示例**：提供复杂功能的使用示例

## 评论格式模板

执行代码审查时，请使用以下格式进行注释：

```markdown
**[PRIORITY] Category: Brief title**

Detailed description of the issue or suggestion.

**Why this matters:**
Explanation of the impact or reason for the suggestion.

**Suggested fix:**
[code example if applicable]

**Reference:** [link to relevant documentation or standard]
```

### 评论示例

#### 关键问题
```markdown
**🔴 CRITICAL - Security: SQL Injection Vulnerability**

The query on line 45 concatenates user input directly into the SQL string,
creating a SQL injection vulnerability.

**Why this matters:**
An attacker could manipulate the email parameter to execute arbitrary SQL commands,
potentially exposing or deleting all database data.

**Suggested fix:**
```sql
-- 而不是：
查询=“从用户中选择*，其中电子邮件='”+电子邮件+“'”

-- 使用：
准备语句 stmt = conn.prepareStatement(
    “从用户中选择*，其中电子邮件=？”
);
stmt.setString(1, 电子邮件);
```

**Reference:** OWASP SQL Injection Prevention Cheat Sheet
```

#### 重要问题
```markdown
**🟡 IMPORTANT - Testing: Missing test coverage for critical path**

The `processPayment()` function handles financial transactions but has no tests
for the refund scenario.

**Why this matters:**
Refunds involve money movement and should be thoroughly tested to prevent
financial errors or data inconsistencies.

**Suggested fix:**
Add test case:
```javascript
test('订单取消时应处理全额退款', () => {
    const order = createOrder({ 总计: 100, 状态: '已取消' });

    const result = processPayment(order, { type: '退款' });

    期望(结果.refundAmount).toBe(100);
    Expect(result.status).toBe('已退款');
});
```
```

#### 建议
```markdown
**🟢 SUGGESTION - Readability: Simplify nested conditionals**

The nested if statements on lines 30-40 make the logic hard to follow.

**Why this matters:**
Simpler code is easier to maintain, debug, and test.

**Suggested fix:**
```javascript
//代替嵌套的if：
如果（用户）{
    if (用户.isActive) {
        if (user.hasPermission('write')) {
            // 做某事
        }
    }
}

// 考虑保护子句：
if (!user || !user.isActive || !user.hasPermission('write')) {
    返回；
}
// 做某事
```
```

## 审查清单

执行代码审查时，系统地验证：

### 代码质量
- [ ] 代码遵循一致的风格和约定
- [ ] 名称具有描述性并遵循命名约定
- [ ] 函数/方法小而集中
- [ ] 没有代码重复
- [ ] 复杂的逻辑被分解为更简单的部分
- [ ] 错误处理适当
- [ ] 没有注释掉的代码或没有票据的 TODO

### 安全性
- [ ] 代码或日志中没有敏感数据
- [ ] 对所有用户输入进行输入验证
- [ ] 无 SQL 注入漏洞
- [ ] 正确实施身份验证和授权
- [ ] 依赖项是最新且安全的

### 测试
- [ ] 新代码具有适当的测试覆盖率
- [ ] 测试命名良好且重点突出
- [ ] 测试涵盖边缘情况和错误场景
- [ ] 测试是独立且确定的
- [ ] 没有始终通过或被注释掉的测试

### 性能
- [ ] 没有明显的性能问题（N+1，内存泄漏）
- [ ] 适当使用缓存
- [ ] 高效的算法和数据结构
- [ ] 适当的资源清理

### 建筑
- [ ] 遵循既定的模式和惯例
- [ ] 适当的关注点分离
- [ ] 没有架构违规
- [ ] 依赖关系朝着正确的方向流动

### 文档
- [ ] 公共 API 已记录
- [ ] 复杂逻辑有解释性注释
- [ ] README 根据需要进行更新
- [ ] 记录了重大变更

## 针对特定项目的定制

要为您的项目自定义此模板，请添加以下部分：

1. **语言/框架特定检查**
   - 示例：“执行代码审查时，验证 React hooks 是否遵循 hooks 规则”
   - 示例：“执行代码审查时，检查 Spring Boot 控制器是否使用正确的注释”

2. **构建和部署**
   - 示例：“执行代码审查时，验证 CI/CD 管道配置是否正确”
   - 示例：“执行代码审查时，检查数据库迁移是否可逆”

3. **业务逻辑规则**
   - 示例：“执行代码审查时，验证定价计算包括所有适用的税费”
   - 示例：“执行代码审查时，检查数据处理之前是否已获得用户同意”

4. **团队大会**
   - 示例：“执行代码审查时，验证提交消息是否遵循常规提交格式”
   - 示例：“执行代码审查时，检查分支名称是否遵循模式：类型/票证描述”

## 其他资源

有关有效代码审查和 GitHub Copilot 自定义的更多信息：

- [GitHub Copilot 提示工程](https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering)
- [GitHub Copilot 自定义说明](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [很棒的 GitHub Copilot 存储库](https://github.com/github/awesome-copilot)
- [GitHub 代码审查指南](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests)
- [Google 工程实践 - 代码审查](https://google.github.io/eng-practices/review/)
- [OWASP 安全准则](https://owasp.org/)

## 及时的工程技巧

执行代码审查时，请应用 [GitHub Copilot 文档](https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering) 中的这些提示工程原则：

1. **开始一般性，然后具体**：从高级架构审查开始，然后深入了解实施细节
2. **给出示例**：在建议更改时参考代码库中的类似模式
3. **分解复杂任务**：以逻辑块的形式审查大型 PR（安全→测试→逻辑→样式）
4. **避免歧义**：具体说明您要解决的文件、行和问题
5. **指示相关代码**：参考可能受更改影响的相关代码
6. **实验和迭代**：如果初步审查遗漏了某些内容，请再次审查重点问题

## 项目背景

这是一个通用模板。使用您的项目特定信息自定义此部分：

- **技术堆栈**：[例如 Java 17、Spring Boot 3.x、PostgreSQL]
- **架构**：[例如，六角形/干净架构、微服务]
- **构建工具**：[例如 Gradle、Maven、npm、pip]
- **测试**：[例如，JUnit 5、Jest、pytest]
- **代码风格**：[例如，遵循 Google 风格指南]
