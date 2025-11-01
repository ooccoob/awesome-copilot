---
description: '使用Jest编写JavaScript/TypeScript测试的最佳实践，包括模拟策略、测试结构和常见模式。'
mode: 'agent'
---

### 测试结构
- 使用`.test.ts`或`.test.js`后缀命名测试文件
- 将测试文件放在被测试代码旁边或专用的`__tests__`目录中
- 使用解释预期行为的描述性测试名称
- 使用嵌套的describe块来组织相关测试
- 遵循模式：`describe('Component/Function/Class', () => { it('should do something', () => {}) })`

### 有效模拟
- 模拟外部依赖项（API、数据库等）以隔离测试
- 对模块级别模拟使用`jest.mock()`
- 对特定函数模拟使用`jest.spyOn()`
- 使用`mockImplementation()`或`mockReturnValue()`定义模拟行为
- 在`afterEach`中使用`jest.resetAllMocks()`在测试之间重置模拟

### 测试异步代码
- 在测试中始终返回promise或使用async/await语法
- 对promise使用`resolves`/`rejects`匹配器
- 使用`jest.setTimeout()`为慢速测试设置适当的超时

### 快照测试
- 对UI组件或不常更改的复杂对象使用快照测试
- 保持快照小而专注
- 在提交前仔细查看快照变更

### 测试React组件
- 使用React Testing Library而不是Enzyme来测试组件
- 测试用户行为和组件可访问性
- 通过可访问性角色、标签或文本内容查询元素
- 使用`userEvent`而不是`fireEvent`以获得更真实的用户交互

## 常见Jest匹配器
- 基础：`expect(value).toBe(expected)`, `expect(value).toEqual(expected)`
- 真值性：`expect(value).toBeTruthy()`, `expect(value).toBeFalsy()`
- 数字：`expect(value).toBeGreaterThan(3)`, `expect(value).toBeLessThanOrEqual(3)`
- 字符串：`expect(value).toMatch(/pattern/)`, `expect(value).toContain('substring')`
- 数组：`expect(array).toContain(item)`, `expect(array).toHaveLength(3)`
- 对象：`expect(object).toHaveProperty('key', value)`
- 异常：`expect(fn).toThrow()`, `expect(fn).toThrow(Error)`
- 模拟函数：`expect(mockFn).toHaveBeenCalled()`, `expect(mockFn).toHaveBeenCalledWith(arg1, arg2)`