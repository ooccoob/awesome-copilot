import os

# 设置路径
source_dir = r"D:\mycode\awesome-copilot\chatmodes"
target_dir = r"D:\mycode\awesome-copilot\my-custom\localization\zh-cn-new\chatmodes"

# 获取所有源文件
source_files = set(f for f in os.listdir(source_dir) if f.endswith('.chatmode.md'))

# 获取已翻译文件
translated_files = set(f for f in os.listdir(target_dir) if f.endswith('.chatmode.md'))

# 找出需要翻译的文件
remaining_files = source_files - translated_files

print(f"总文件数: {len(source_files)}")
print(f"已翻译: {len(translated_files)}")
print(f"剩余需要翻译: {len(remaining_files)}")
print("\n剩余需要翻译的文件列表:")

for i, filename in enumerate(sorted(remaining_files), 1):
    print(f"{i:2d}. {filename}")

# 保存文件列表到文件
with open(os.path.join(target_dir, "remaining_files.txt"), "w", encoding="utf-8") as f:
    for filename in sorted(remaining_files):
        f.write(f"{filename}\n")

print(f"\n文件列表已保存到: {os.path.join(target_dir, 'remaining_files.txt')}")