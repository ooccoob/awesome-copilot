---
description: "使用 Jest 编写 JavaScript/TypeScript 测试的最佳实践（含 Mock 策略、结构与常见模式）"
---

### 测试结构

- 测试文件以 `.test.ts` 或 `.test.js` 结尾
- 测试文件与被测代码同目录或放在 `__tests__` 目录
- 使用描述性测试名，表达期望行为
- 使用嵌套的 describe 块组织相关测试
- 建议模式：`describe('组件/函数/类', () => { it('应当…', () => {}) })`

### 有效的 Mock

- 对外部依赖（API、数据库等）进行 Mock 以隔离测试
- 使用 `jest.mock()` 进行模块级 Mock
- 使用 `jest.spyOn()` 对特定函数进行 Mock
- 使用 `mockImplementation()` 或 `mockReturnValue()` 定义 Mock 行为
- 在 `afterEach` 中用 `jest.resetAllMocks()` 重置 Mock

### 测试异步代码

- 测试中返回 Promise 或使用 async/await
- 使用 `resolves`/`rejects` 断言 Promise
- 对慢测试使用 `jest.setTimeout()` 设置合适超时

### 快照测试

- 适用于 UI 组件或变更不频繁的复杂对象
- 保持快照小而聚焦
- 提交前仔细审阅快照变更

### 测试 React 组件

- 使用 React Testing Library 替代 Enzyme
- 关注用户行为与可访问性
- 通过可访问性角色、标签或文本内容查询元素
- 使用 `userEvent` 替代 `fireEvent` 提升交互真实度

## 常见 Jest 匹配器

- 基本：`expect(value).toBe(expected)`、`toEqual`
- 真值：`toBeTruthy()`、`toBeFalsy()`
- 数字：`toBeGreaterThan(3)`、`toBeLessThanOrEqual(3)`
- 字符串：`toMatch(/pattern/)`、`toContain('substr')`
- 数组：`toContain(item)`、`toHaveLength(3)`
- 对象：`toHaveProperty('key', value)`
- 异常：`toThrow()`、`toThrow(Error)`
- Mock：`toHaveBeenCalled()`、`toHaveBeenCalledWith(arg1, arg2)`

```

```
