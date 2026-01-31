---
描述：“剧作家基于官方文档的 Python AI 测试生成说明。”
适用于：'**'
---

# Playwright Python 测试生成说明

## 测试写作指南

### 代码质量标准
- **定位器**：优先考虑面向用户、基于角色的定位器（get_by_role、get_by_label、get_by_text），以实现弹性和可访问性。
- **断言**：通过 Expect API 使用自动重试 Web 优先断言（例如，expect(page).to_have_title(...)）。避免使用expect(locator).to_be_visible()，除非专门测试元素可见性的变化，因为更具体的断言通常更可靠。
- **超时**：依靠 Playwright 的内置自动等待机制。避免硬编码等待或增加默认超时。
- **清晰度**：使用描述性测试标题（例如 def test_navigation_link_works():) 清楚地说明其意图。添加注释只是为了解释复杂的逻辑，而不是为了描述“单击按钮”之类的简单操作。

### 测试结构
- **导入**：每个测试文件都应以 from playwright.sync_api import 页面开头，期望如此。
- **夹具**：使用页面：页面夹具作为测试函数中的参数来与浏览器页面交互。
- **设置**：将 page.goto() 等导航步骤放在每个测试函数的开头。对于在多个测试之间共享的设置操作，请使用标准 Pytest 固定装置。

### 文件组织
- **位置**：将测试文件存储在专用的tests/目录中或遵循现有的项目结构。
- **命名**：测试文件必须遵循 test_<feature-or-page>.py 命名约定才能被 Pytest 发现。
- **范围**：针对每个主要应用程序功能或页面一个测试文件。

## 断言最佳实践
- **元素计数**：使用expect(locator).to_have_count()断言定位器找到的元素数量。
- **文本内容**：使用expect(locator).to_have_text()进行精确文本匹配，使用expect(locator).to_contain_text()进行部分匹配。
- **导航**：使用expect(page).to_have_url()来验证页面URL。
- **断言风格**：为了更可靠的 UI 测试，优先使用 `expect` 而不是 `assert`。


## 示例

```python
import re
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    # Go to the starting url before each test.
    page.goto("https://playwright.dev/")

def test_main_navigation(page: Page):
    expect(page).to_have_url("https://playwright.dev/")

def test_has_title(page: Page):
    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.get_by_role("link", name="Get started").click()
    
    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
```

## 测试执行策略

1. **执行**：使用 pytest 命令从终端运行测试。
2. **调试失败**：分析测试失败并确定根本原因
