---
描述：'GitHub Copilot 编写注释的指南，以通过更少的注释实现不言自明的代码。示例是 JavaScript 中的，但它应该适用于任何有注释的语言。
适用于：'**'
---

# 不言自明的代码注释说明

## 核心原则
**编写不言而喻的代码。仅在必要时发表评论以解释原因，而不是原因。**
大多数时候我们不需要评论。

## 评论指南

### ❌ 避免这些评论类型

**明显的评论**
```javascript
// Bad: States the obvious
let counter = 0;  // Initialize counter to zero
counter++;  // Increment counter by one
```

**多余的评论**
```javascript
// Bad: Comment repeats the code
function getUserName() {
    return user.name;  // Return the user's name
}
```

**过时的评论**
```javascript
// Bad: Comment doesn't match the code
// Calculate tax at 5% rate
const tax = price * 0.08;  // Actually 8%
```

### ✅ 写下这些评论类型

**复杂的业务逻辑**
```javascript
// Good: Explains WHY this specific calculation
// Apply progressive tax brackets: 10% up to 10k, 20% above
const tax = calculateProgressiveTax(income, [0.10, 0.20], [10000]);
```

**非显而易见的算法**
```javascript
// Good: Explains the algorithm choice
// Using Floyd-Warshall for all-pairs shortest paths
// because we need distances between all nodes
for (let k = 0; k < vertices; k++) {
    for (let i = 0; i < vertices; i++) {
        for (let j = 0; j < vertices; j++) {
            // ... implementation
        }
    }
}
```

**正则表达式模式**
```javascript
// Good: Explains what the regex matches
// Match email format: username@domain.extension
const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
```

**API 限制或陷阱**
```javascript
// Good: Explains external constraint
// GitHub API rate limit: 5000 requests/hour for authenticated users
await rateLimiter.wait();
const response = await fetch(githubApiUrl);
```

## 决策框架

在写评论之前，先问：
1. **代码是不言自明的吗？** → 不需要注释
2. **更好的变量/函数名称会消除这种需要吗？** → 重构
3. **这是否解释了为什么，而不是什么？** → 好评论
4. **这对未来的维护者有帮助吗？** → 好评论

## 特殊情况征求意见

### 公共API
```javascript
/**
 * Calculate compound interest using the standard formula.
 * 
 * @param {number} principal - Initial amount invested
 * @param {number} rate - Annual interest rate (as decimal, e.g., 0.05 for 5%)
 * @param {number} time - Time period in years
 * @param {number} compoundFrequency - How many times per year interest compounds (default: 1)
 * @returns {number} Final amount after compound interest
 */
function calculateCompoundInterest(principal, rate, time, compoundFrequency = 1) {
    // ... implementation
}
```

### 配置和常量
```javascript
// Good: Explains the source or reasoning
const MAX_RETRIES = 3;  // Based on network reliability studies
const API_TIMEOUT = 5000;  // AWS Lambda timeout is 15s, leaving buffer
```

### 注释
```javascript
// TODO: Replace with proper user authentication after security review
// FIXME: Memory leak in production - investigate connection pooling
// HACK: Workaround for bug in library v2.1.0 - remove after upgrade
// NOTE: This implementation assumes UTC timezone for all calculations
// WARNING: This function modifies the original array instead of creating a copy
// PERF: Consider caching this result if called frequently in hot path
// SECURITY: Validate input to prevent SQL injection before using in query
// BUG: Edge case failure when array is empty - needs investigation
// REFACTOR: Extract this logic into separate utility function for reusability
// DEPRECATED: Use newApiFunction() instead - this will be removed in v3.0
```

## 要避免的反模式

### 死代码注释
```javascript
// Bad: Don't comment out code
// const oldFunction = () => { ... };
const newFunction = () => { ... };
```

### 变更日志评论
```javascript
// Bad: Don't maintain history in comments
// Modified by John on 2023-01-15
// Fixed bug reported by Sarah on 2023-02-03
function processData() {
    // ... implementation
}
```

### 分频器评论
```javascript
// Bad: Don't use decorative comments
//=====================================
// UTILITY FUNCTIONS
//=====================================
```

## 质量检查表

在提交之前，请确保您的评论：
- [ ] 解释为什么，而不是什么
- [ ] 语法正确且清晰
- [ ] 随着代码的发展将保持准确
- [ ] 为代码理解增添真正的价值
- [ ] 放置在适当的位置（在它们描述的代码上方）
- [ ] 使用正确的拼写和专业语言

## 总结

请记住：**最好的注释是您不需要编写的注释，因为代码是自记录的。**
