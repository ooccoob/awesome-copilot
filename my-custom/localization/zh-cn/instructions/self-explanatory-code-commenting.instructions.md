---
applyTo: "self-explanatory-code-commenting.instructions.md"
---

<!-- 本文件为自动翻译，供参考。请结合实际需求进行校对和完善。-->

# 自解释代码注释规范

## 核心原则

**让代码自我表达，仅在必要时解释“为什么”，而非“做什么”。**
我们大多数时候不需要注释。

## 注释指南

### ❌ 避免以下注释类型

**显而易见的注释**

```javascript
// 错误：陈述了显而易见的内容
let counter = 0; // 初始化计数器为零
counter++; // 计数器加一
```

**冗余注释**

```javascript
// 错误：注释重复了代码
function getUserName() {
  return user.name; // 返回用户名称
}
```

**过时注释**

```javascript
// 错误：注释与代码不符
// 按 5% 税率计算
const tax = price * 0.08; // 实际为 8%
```

### ✅ 推荐以下注释类型

**复杂业务逻辑**

```javascript
// 好：解释为何这样计算
// 分段税率：1 万以内 10%，超出部分 20%
const tax = calculateProgressiveTax(income, [0.1, 0.2], [10000]);
```

**非显而易见算法**

```javascript
// 好：解释算法选择
// 用 Floyd-Warshall 算法求所有点对最短路径
for (let k = 0; k < vertices; k++) {
  for (let i = 0; i < vertices; i++) {
    for (let j = 0; j < vertices; j++) {
      // ... 实现 ...
    }
  }
}
```

**正则表达式**

```javascript
// 好：解释正则含义
// 匹配邮箱格式：username@domain.extension
const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
```

**API 限制或注意事项**

```javascript
// 好：解释外部约束
// GitHub API 限流：认证用户每小时 5000 次
await rateLimiter.wait();
const response = await fetch(githubApiUrl);
```

## 决策框架

写注释前请自问：

1. **代码是否自解释？** → 不需要注释
2. **更好的命名能否消除注释？** → 优先重构
3. **是否解释了“为什么”而非“做什么”？** → 好注释
4. **能否帮助后续维护者？** → 好注释

## 特殊注释场景

### 公共 API

```javascript
/**
 * 用标准公式计算复利。
 *
 * @param {number} principal - 初始本金
 * @param {number} rate - 年利率（如 0.05 表示 5%）
 * @param {number} time - 年数
 * @param {number} compoundFrequency - 每年复利次数（默认 1）
 * @returns {number} 复利后金额
 */
function calculateCompoundInterest(principal, rate, time, compoundFrequency = 1) {
  // ... 实现 ...
}
```

### 配置与常量

```javascript
// 好：解释来源或原因
const MAX_RETRIES = 3; // 基于网络可靠性研究
const API_TIMEOUT = 5000; // AWS Lambda 超时 15s，留缓冲
```

### 注解

```javascript
// TODO: 安全评审后替换为正式认证
// FIXME: 生产环境内存泄漏，需排查连接池
// HACK: 兼容库 v2.1.0 的 bug，升级后移除
// NOTE: 假定所有计算均为 UTC 时区
// WARNING: 此函数会修改原数组
// PERF: 热路径建议缓存结果
// SECURITY: 查询前需校验输入防 SQL 注入
// BUG: 空数组时有边界问题，需排查
// REFACTOR: 建议提取为工具函数
// DEPRECATED: 请用 newApiFunction()，本方法将废弃
```

## 反模式

### 注释死代码

```javascript
// 错误：不要注释掉代码
// const oldFunction = () => { ... };
const newFunction = () => { ... };
```

### 注释变更历史

```javascript
// 错误：不要用注释维护历史
// 2023-01-15 John 修改
// 2023-02-03 Sarah 修复 bug
function processData() {
  // ... 实现 ...
}
```

### 分隔线注释

```javascript
// 错误：不要用装饰性注释
//=====================================
// 工具函数
//=====================================
```

## 质量检查清单

提交前请确保：

- [ ] 注释解释“为什么”而非“做什么”
- [ ] 语法正确、表达清晰
- [ ] 随代码演进保持准确
- [ ] 有助于理解
- [ ] 注释放在所描述代码上方
- [ ] 拼写和用语专业

## 总结

记住：**最好的注释是代码本身已自解释，无需额外说明。**
