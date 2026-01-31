---
名称：图像处理-图像-magick
描述：使用 ImageMagick 处理和操作图像。支持调整大小、格式转换、批处理和检索图像元数据。在处理图像、创建缩略图、调整壁纸大小或执行批量图像操作时使用。
兼容性：需要安装 ImageMagick 并在 PATH 上以 `magick` 形式提供。为 PowerShell (Windows) 和 Bash (Linux/macOS) 提供跨平台示例。
---

# 使用 ImageMagick 进行图像处理

该技能可以使用 ImageMagick 执行图像处理和操作任务
跨 Windows、Linux 和 macOS 系统。

## 何时使用此技能

当您需要执行以下操作时，请使用此技能：

- 调整图像大小（单个或批量）
- 获取图像尺寸和元数据
- 图像格式之间的转换
- 创建缩略图
- 处理不同屏幕尺寸的壁纸
- 具有特定标准的批量处理多个图像

## 先决条件

- 系统上安装了 ImageMagick
- **Windows**：带有 ImageMagick 的 PowerShell 可用作 `magick`（或 `C:\Program Files\ImageMagick-*\magick.exe`）
- **Linux/macOS**：通过包管理器安装 ImageMagick 的 Bash（`apt`、`brew` 等）

## 核心能力

### 1. 图像信息

- 获取图像尺寸（宽x高）
- 检索详细的元数据（格式、色彩空间等）
- 识别图像格式

### 2. 调整图像大小

- 调整单个图像的大小
- 批量调整多张图像的大小
- 创建具有特定尺寸的缩略图
- 保持纵横比

### 3. 批处理

- 根据尺寸处理图像
- 过滤和处理特定文件类型
- 将转换应用于多个文件

## 使用示例

### 示例 0：解析 `magick` 可执行文件

**PowerShell（Windows）：**
```powershell
# Prefer ImageMagick on PATH
$magick = (Get-Command magick -ErrorAction SilentlyContinue)?.Source

# Fallback: common install pattern under Program Files
if (-not $magick) {
    $magick = Get-ChildItem "C:\\Program Files\\ImageMagick-*\\magick.exe" -ErrorAction SilentlyContinue |
        Select-Object -First 1 -ExpandProperty FullName
}

if (-not $magick) {
    throw "ImageMagick not found. Install it and/or add 'magick' to PATH."
}
```

**Bash (Linux/macOS)：**
```bash
# Check if magick is available on PATH
if ! command -v magick &> /dev/null; then
    echo "ImageMagick not found. Install it using your package manager:"
    echo "  Ubuntu/Debian: sudo apt install imagemagick"
    echo "  macOS: brew install imagemagick"
    exit 1
fi
```

### 示例 1：获取图像尺寸

**PowerShell（Windows）：**
```powershell
# For a single image
& $magick identify -format "%wx%h" path/to/image.jpg

# For multiple images
Get-ChildItem "path/to/images/*" | ForEach-Object { 
    $dimensions = & $magick identify -format "%f: %wx%h`n" $_.FullName
    Write-Host $dimensions 
}
```

**Bash (Linux/macOS)：**
```bash
# For a single image
magick identify -format "%wx%h" path/to/image.jpg

# For multiple images
for img in path/to/images/*; do
    magick identify -format "%f: %wx%h\n" "$img"
done
```

### 示例 2：调整图像大小

**PowerShell（Windows）：**
```powershell
# Resize a single image
& $magick input.jpg -resize 427x240 output.jpg

# Batch resize images
Get-ChildItem "path/to/images/*" | ForEach-Object { 
    & $magick $_.FullName -resize 427x240 "path/to/output/thumb_$($_.Name)"
}
```

**Bash (Linux/macOS)：**
```bash
# Resize a single image
magick input.jpg -resize 427x240 output.jpg

# Batch resize images
for img in path/to/images/*; do
    filename=$(basename "$img")
    magick "$img" -resize 427x240 "path/to/output/thumb_$filename"
done
```

### 示例3：获取详细图像信息

**PowerShell（Windows）：**
```powershell
# Get verbose information about an image
& $magick identify -verbose path/to/image.jpg
```

**Bash (Linux/macOS)：**
```bash
# Get verbose information about an image
magick identify -verbose path/to/image.jpg
```

### 示例4：根据尺寸处理图像

**PowerShell（Windows）：**
```powershell
Get-ChildItem "path/to/images/*" | ForEach-Object { 
    $dimensions = & $magick identify -format "%w,%h" $_.FullName
    if ($dimensions) {
        $width,$height = $dimensions -split ','
        if ([int]$width -eq 2560 -or [int]$height -eq 1440) {
            Write-Host "Processing $($_.Name)"
            & $magick $_.FullName -resize 427x240 "path/to/output/thumb_$($_.Name)"
        }
    }
}
```

**Bash (Linux/macOS)：**
```bash
for img in path/to/images/*; do
    dimensions=$(magick identify -format "%w,%h" "$img")
    if [[ -n "$dimensions" ]]; then
        width=$(echo "$dimensions" | cut -d',' -f1)
        height=$(echo "$dimensions" | cut -d',' -f2)
        if [[ "$width" -eq 2560 || "$height" -eq 1440 ]]; then
            filename=$(basename "$img")
            echo "Processing $filename"
            magick "$img" -resize 427x240 "path/to/output/thumb_$filename"
        fi
    fi
done
```

## 指南

1. **始终引用文件路径** - 在可能包含空格的文件路径周围使用引号
2. **使用 `&` 运算符 (PowerShell)** - 在 PowerShell 中使用 `&` 调用 magick 可执行文件
3. **将路径存储在变量中 (PowerShell)** - 将 ImageMagick 路径分配给 `$magick` 以获得更清晰的代码
4. **换行循环** - 处理多个文件时，使用 `ForEach-Object` (PowerShell) 或 `for` 循环 (Bash)
5. **先验证尺寸** - 在处理前检查图像尺寸，以避免不必要的操作
6. **使用适当的调整大小标志** - 考虑使用 `!` 强制精确尺寸或使用 `^` 最小尺寸

## 常见模式

### PowerShell 模式

#### 模式：存储ImageMagick路径

```powershell
$magick = (Get-Command magick).Source
```

#### 模式：获取尺寸作为变量

```powershell
$dimensions = & $magick identify -format "%w,%h" $_.FullName
$width,$height = $dimensions -split ','
```

#### 模式：条件处理

```powershell
if ([int]$width -gt 1920) {
    & $magick $_.FullName -resize 1920x1080 $outputPath
}
```

#### 模式：创建缩略图

```powershell
& $magick $_.FullName -resize 427x240 "thumbnails/thumb_$($_.Name)"
```

### 重击模式

#### 模式：检查 ImageMagick 安装

```bash
command -v magick &> /dev/null || { echo "ImageMagick required"; exit 1; }
```

#### 模式：获取尺寸作为变量

```bash
dimensions=$(magick identify -format "%w,%h" "$img")
width=$(echo "$dimensions" | cut -d',' -f1)
height=$(echo "$dimensions" | cut -d',' -f2)
```

#### 模式：条件处理

```bash
if [[ "$width" -gt 1920 ]]; then
    magick "$img" -resize 1920x1080 "$outputPath"
fi
```

#### 模式：创建缩略图

```bash
filename=$(basename "$img")
magick "$img" -resize 427x240 "thumbnails/thumb_$filename"
```

## 局限性

- 大批量操作可能会占用大量内存
- 一些复杂的操作可能需要额外的 ImageMagick 委托
- 在较旧的 Linux 系统上，使用 `convert` 而不是 `magick`（ImageMagick 6.x 与 7.x）
