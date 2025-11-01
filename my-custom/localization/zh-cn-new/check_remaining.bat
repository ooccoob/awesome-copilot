@echo off
setlocal enabledelayedexpansion

echo 识别需要翻译的文件...
cd /d "D:\mycode\awesome-copilot\chatmodes"

echo 剩余需要翻译的39个文件：
echo.

set count=0
for %%f in (*.chatmode.md) do (
    if not exist "D:\mycode\awesome-copilot\my-custom\localization\zh-cn-new\chatmodes\%%f" (
        set /a count+=1
        echo !count!. %%f
    )
)

echo.
echo 总计需要翻译的文件数量：!count!
pause