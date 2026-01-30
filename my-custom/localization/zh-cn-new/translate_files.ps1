# 批量翻译脚本 - 翻译 awesome-copilot 项目中的 .md 文件到中文
# 注意：这个脚本将逐个处理文件，但需要手动翻译每个文件

$sourceFolders = @(
    "D:\mycode\awesome-copilot\chatmodes",
    "D:\mycode\awesome-copilot\instructions",
    "D:\mycode\awesome-copilot\prompts"
)

$targetBase = "D:\mycode\awesome-copilot\my-custom\localization\zh-cn-new"

$totalFiles = 0
$processedFiles = 0

Write-Host "开始扫描所有 .md 文件..." -ForegroundColor Green

foreach ($sourceFolder in $sourceFolders) {
    $folderName = Split-Path $sourceFolder -Leaf
    $targetFolder = Join-Path $targetBase $folderName

    Write-Host "正在处理文件夹: $folderName" -ForegroundColor Yellow

    $files = Get-ChildItem -Path $sourceFolder -Filter "*.md" -Recurse
    $totalFiles += $files.Count

    Write-Host "找到 $($files.Count) 个 .md 文件在 $folderName 文件夹中" -ForegroundColor Cyan

    foreach ($file in $files) {
        $relativePath = $file.FullName.Replace($sourceFolder, "").TrimStart("\")
        $targetFile = Join-Path $targetFolder $relativePath

        Write-Host "需要翻译: $($file.Name) -> $targetFile" -ForegroundColor White
    }
}

Write-Host "`n总计发现 $totalFiles 个 .md 文件需要翻译" -ForegroundColor Magenta
Write-Host "由于需要人工翻译质量，请逐个处理文件。" -ForegroundColor Yellow