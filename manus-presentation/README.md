Manus 演示 PPT 生成器

说明

此目录包含演示幻灯片的 Markdown 源（`slides.md`）和一个简单的 Python 脚本 `scripts/generate_pptx.py`，用于将 Markdown 切片转换为 PowerPoint（.pptx）。

先决条件

- 本机已安装 Python 3.x
- 安装依赖：`python -m pip install python-pptx`

在 Windows PowerShell 下运行示例

```powershell
cd d:\mycode\awesome-copilot\manus-presentation
python -m pip install python-pptx
python scripts\generate_pptx.py slides.md output\manus_demo.pptx
```

生成结果

- 输出文件：`output\manus_demo.pptx`，可用 PowerPoint 或 LibreOffice 打开用于演示。

可选：如果你希望我直接在仓库里运行并生成 PPTX，请允许我执行命令（我会先检查环境）。
