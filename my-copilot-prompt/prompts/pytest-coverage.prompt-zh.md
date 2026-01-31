---
代理人：代理人
描述：“运行具有覆盖率的 pytest 测试，发现缺少覆盖率的行，并将覆盖率提高到 100%。”
---

测试的目标是覆盖所有代码行。

使用以下内容生成覆盖率报告：

pytest --cov --cov-report=注释：cov_annotate

如果您要检查特定模块的覆盖范围，可以这样指定：

pytest --cov=your_module_name --cov-report=annotate:cov_annotate

您还可以指定要运行的特定测试，例如：

pytest 测试/test_your_module.py --cov=your_module_name --cov-report=annotate:cov_annotate

打开cov_annotate目录可以查看带注释的源代码。
每个源文件将有一个文件。如果文件的源覆盖率为 100%，则意味着所有行都被测试覆盖，因此您不需要打开该文件。

对于测试覆盖率低于 100% 的每个文件，在 cov_annotate 中找到匹配的文件并检查该文件。

如果一行以 ! （感叹号），表示该行未被测试覆盖。
添加测试以覆盖缺失的行。

继续运行测试并提高覆盖率，直到覆盖所有线路。
