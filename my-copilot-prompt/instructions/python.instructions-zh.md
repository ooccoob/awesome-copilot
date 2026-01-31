---
描述：“Python 编码约定和指南”
适用于：'**/*.py'
---

# Python 编码约定

## Python指令

- 为每个函数写下清晰简洁的注释。
- 确保函数具有描述性名称并包含类型提示。
- 提供遵循 PEP 257 约定的文档字符串。
- 使用 `typing` 模块进行类型注释（例如 `List[str]`、`Dict[str, int]`）。
- 将复杂的功能分解为更小、更易于管理的功能。

## 一般说明

- 始终优先考虑可读性和清晰度。
- 对于与算法相关的代码，请包括所使用方法的解释。
- 编写具有良好可维护性实践的代码，包括对为什么做出某些设计决策的评论。
- 处理边缘情况并编写清晰的异常处理。
- 对于库或外部依赖项，请在注释中提及它们的用法和目的。
- 使用一致的命名约定并遵循特定于语言的最佳实践。
- 编写简洁、高效、惯用且易于理解的代码。

## 代码风格和格式

- 遵循 Python 的 **PEP 8** 风格指南。
- 保持适当的缩进（每级缩进使用 4 个空格）。
- 确保行不超过 79 个字符。
- 将函数和类文档字符串紧接在 `def` 或 `class` 关键字之后。
- 在适当的情况下使用空行来分隔函数、类和代码块。

## 边缘情况和测试

- 始终包含应用程序关键路径的测试用例。
- 考虑常见的边缘情况，例如空输入、无效数据类型和大型数据集。
- 包括对边缘情况的评论以及这些情况下的预期行为。
- 为函数编写单元测试，并使用解释测试用例的文档字符串记录它们。

## 正确文档的示例

```python
def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle given the radius.
    
    Parameters:
    radius (float): The radius of the circle.
    
    Returns:
    float: The area of the circle, calculated as π * radius^2.
    """
    import math
    return math.pi * radius ** 2
```
