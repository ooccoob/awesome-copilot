---
描述：“使用 Jest 编写 JavaScript/TypeScript 测试的最佳实践，包括模拟策略、测试结构和常见模式。”
代理人：“代理人”
---

### 测试结构
- 使用 `.test.ts` 或 `.test.js` 后缀命名测试文件
- 将测试文件放在要测试的代码旁边或专用的 `__tests__` 目录中
- 使用描述性测试名称来解释预期行为
- 使用嵌套的描述块来组织相关测试
- 遵循模式：`describe('Component/Function/Class', () => { it('should do something', () => {}) })`

### 有效的模拟
- 模拟外部依赖项（API、数据库等）来隔离您的测试
- 使用 `jest.mock()` 进行模块级模拟
- 使用 `jest.spyOn()` 进行特定函数模拟
- 使用 `mockImplementation()` 或 `mockReturnValue()` 定义模拟行为
- 使用 `afterEach` 中的 `jest.resetAllMocks()` 重置测试之间的模拟

### 测试异步代码
- 在测试中始终返回 Promise 或使用 async/await 语法
- 使用 `resolves`/`rejects` 匹配器进行承诺
- 使用 `jest.setTimeout()` 为慢速测试设置适当的超时

### 快照测试
- 对不经常更改的 UI 组件或复杂对象使用快照测试
- 保持快照小而集中
- 在提交之前仔细检查快照更改

### 测试 React 组件
- 使用 React 测试库而不是 Enzyme 来测试组件
- 测试用户行为和组件可访问性
- 按辅助功能角色、标签或文本内容查询元素
- 使用 `userEvent` 而不是 `fireEvent` 来实现更真实的用户交互

## 常见笑话匹配器
- 基本：`expect(value).toBe(expected)`、`expect(value).toEqual(expected)`
- 真实性：`expect(value).toBeTruthy()`、`expect(value).toBeFalsy()`
- 数字：`expect(value).toBeGreaterThan(3)`、`expect(value).toBeLessThanOrEqual(3)`
- 字符串：`expect(value).toMatch(/pattern/)`、`expect(value).toContain('substring')`
- 数组：`expect(array).toContain(item)`、`expect(array).toHaveLength(3)`
- 对象：`expect(object).toHaveProperty('key', value)`
- 例外：`expect(fn).toThrow()`、`expect(fn).toThrow(Error)`
- 模拟函数：`expect(mockFn).toHaveBeenCalled()`、`expect(mockFn).toHaveBeenCalledWith(arg1, arg2)`
