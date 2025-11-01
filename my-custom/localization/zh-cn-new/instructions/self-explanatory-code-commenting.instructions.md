---
description: 'GitHub Copilot 编写注释以实现自解释代码和更少注释的指南。示例使用 JavaScript，但应适用于任何有注释的语言。'
applyTo: '**'
---

# 自解释代码注释指令

## 核心原则
**编写能说明自己的代码。仅在必要时解释为什么，而不是什么。**
大多数时候我们不需要注释。

## 注释指南

### ❌ 避免这些注释类型

**显而易见的注释**
```javascript
// 坏：陈述显而易见的内容
let counter = 0;  // 将计数器初始化为零
counter++;  // 计数器加一
```

**冗余注释**
```javascript
// 坏：注释重复代码
function getUserName() {
    return user.name;  // 返回用户的名称
}
```

**过时的注释**
```javascript
// 坏：注释与代码不匹配
// 按 5% 税率计算税款
const tax = price * 0.08;  // 实际是 8%
```

### ✅ 编写这些注释类型

**复杂业务逻辑**
```javascript
// 好：解释为什么使用这个特定计算
// 应用累进税级：1万以下 10%，超过部分 20%
const tax = calculateProgressiveTax(income, [0.10, 0.20], [10000]);
```

**非显而易见的算法**
```javascript
// 好：解释算法选择
// 使用 Floyd-Warshall 算法求所有节点对的最短路径
// 因为我们需要所有节点之间的距离
for (let k = 0; k < vertices; k++) {
    for (let i = 0; i < vertices; i++) {
        for (let j = 0; j < vertices; j++) {
            // ... 实现
        }
    }
}
```

**正则表达式模式**
```javascript
// 好：解释正则表达式匹配什么
// 匹配电子邮件格式：username@domain.extension
const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
```

**API 约束或陷阱**
```javascript
// 好：解释外部约束
// GitHub API 速率限制：认证用户每小时 5000 次请求
await rateLimiter.wait();
const response = await fetch(githubApiUrl);
```

## 决策框架

在编写注释之前，询问：
1. **代码是否不言自明？** → 不需要注释
2. **更好的变量/函数名称是否能消除需要？** → 重构
3. **这是否解释了为什么，而不是什么？** → 好的注释
4. **这会帮助未来的维护者吗？** → 好的注释

## 注释的特殊情况

### 公共 API
```javascript
/**
 * 使用标准公式计算复利。
 *
 * @param {number} principal - 初始投资金额
 * @param {number} rate - 年利率（作为小数，例如 5% 为 0.05）
 * @param {number} time - 时间周期（年）
 * @param {number} compoundFrequency - 每年复利计算次数（默认：1）
 * @returns {number} 复利后的最终金额
 */
function calculateCompoundInterest(principal, rate, time, compoundFrequency = 1) {
    // ... 实现
}
```

### 配置和常量
```javascript
// 好：解释来源或原因
const MAX_RETRIES = 3;  // 基于网络可靠性研究
const API_TIMEOUT = 5000;  // AWS Lambda 超时是 15 秒，留出缓冲
```

### 注释
```javascript
// TODO：安全审查后替换为适当的用户身份验证
// FIXME：生产环境中的内存泄漏 - 调查连接池
// HACK：库 v2.1.0 中错误的临时解决方案 - 升级后移除
// NOTE：此实现假设所有计算都使用 UTC 时区
// WARNING：此函数修改原始数组而不是创建副本
// PERF：如果在热路径中频繁调用，考虑缓存此结果
// SECURITY：在查询中使用前验证输入以防止 SQL 注入
// BUG：数组为空时的边缘情况失败 - 需要调查
// REFACTOR：将此逻辑提取到单独的工具函数中以提高可重用性
// DEPRECATED：使用 newApiFunction() 替代 - 这将在 v3.0 中移除
```

## 避免的反模式

### 死代码注释
```javascript
// 坏：不要注释掉代码
// const oldFunction = () => { ... };
const newFunction = () => { ... };
```

### 变更日志注释
```javascript
// 坏：不要在注释中维护历史
// John 于 2023-01-15 修改
// Sarah 于 2023-02-03 报告的错误已修复
function processData() {
    // ... 实现
}
```

### 分隔符注释
```javascript
// 坏：不要使用装饰性注释
//=====================================
// 工具函数
//=====================================
```

## 质量检查清单

在提交之前，确保您的注释：
- [ ] 解释为什么，而不是什么
- [ ] 语法正确且清晰
- [ ] 随着代码演变保持准确
- [ ] 为代码理解增加真正价值
- [ ] 位置适当（在它们描述的代码上方）
- [ ] 使用正确的拼写和专业语言

## 总结

记住：**最好的注释是您不需要编写的注释，因为代码本身就是自文档化的。**