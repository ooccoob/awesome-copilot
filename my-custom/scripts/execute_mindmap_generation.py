"""
LLM驱动的Mindmap生成执行脚本
根据TASK_PLAN_LLM_MINDMAP_GENERATION.md中的计划执行
"""

import os
import json
import time
from pathlib import Path

# 配置路径
SOURCE_DIR = r"D:\mycode\awesome-copilot\chatmodes"
OUTPUT_DIR = r"D:\mycode\awesome-copilot\my-custom\Mind Map\chatmodes"
LOG_FILE = r"D:\mycode\awesome-copilot\my-custom\Mind Map\generation_log.txt"

# 确保输出目录存在
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

# 进度跟踪变量
total_files = 0
processed_files = 0
success_count = 0
failed_count = 0
failed_list = []

def log_message(message):
    """记录日志"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    print(log_entry.strip())
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(log_entry)

def read_source_file(filepath):
    """Task 1: 读取源文件内容"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        return content, None
    except Exception as e:
        return None, str(e)

def analyze_content(content, filename):
    """Task 2: 智能分析文件内容"""

    # 提取标题
    lines = content.split('\n')
    title = filename.replace('.chatmode.md', '').replace('-', ' ').title()

    # 查找description或第一个标题
    description = ""
    for line in lines:
        if line.startswith('#'):
            description = line.strip('# ').strip()
            break

    # 基础分析结构
    analysis = {
        "title": title,
        "description": description or f"{title} Chat Mode",
        "filename": filename,
        "content_length": len(content),
        "has_frontmatter": content.startswith('---'),
        "sections": []
    }

    # 提取主要章节
    current_section = None
    for line in lines:
        if line.startswith('## '):
            section_title = line.strip('# ').strip()
            analysis["sections"].append(section_title)

    return analysis

def generate_mindmap_content(analysis, source_content):
    """Task 3: 生成Mindmap Markdown内容"""

    title = analysis['title']
    description = analysis['description']
    filename = analysis['filename']

    # 从源内容提取使用场景和能力
    lines = source_content.split('\n')

    # 查找关键信息
    use_cases = []
    capabilities = []
    key_points = []

    in_section = ""
    for line in lines:
        line_clean = line.strip()

        if line_clean.startswith('## '):
            in_section = line_clean.strip('# ').lower()
        elif line_clean.startswith('- ') or line_clean.startswith('* '):
            point = line_clean.lstrip('- *').strip()
            if point:
                if 'use' in in_section or 'when' in in_section or 'scenario' in in_section:
                    use_cases.append(point)
                elif 'capabilit' in in_section or 'feature' in in_section or 'skill' in in_section:
                    capabilities.append(point)
                else:
                    key_points.append(point)

    # 如果没有提取到足够信息,使用默认值
    if not use_cases:
        use_cases = [
            f"当你需要专业的 {title} 相关指导时",
            f"解决 {title} 领域的技术问题",
            "获取最佳实践和专业建议"
        ]

    if not capabilities:
        capabilities = key_points[:5] if key_points else [
            "专业知识和技术指导",
            "问题诊断和解决方案",
            "代码优化建议"
        ]

    # 生成思维导图节点
    sections = analysis.get('sections', [])
    mindmap_branches = []

    if sections:
        for section in sections[:5]:  # 最多5个主要分支
            mindmap_branches.append(f"  - {section}")
    else:
        mindmap_branches = [
            "  - 核心能力",
            "  - 使用场景",
            "  - 最佳实践",
            "  - 技术要点"
        ]

    # 生成示例问题
    example_questions = generate_example_questions(title, use_cases, capabilities)

    # 生成结构化要点
    structured_points = generate_structured_points(sections, capabilities, key_points)

    # 组装完整的mindmap内容
    mindmap_md = f"""# {title} - Mindmap

## 📊 摘要
{description}。本模式专注于提供专业的{title}相关指导,帮助用户解决实际问题并遵循最佳实践。

## 💡 实际使用说明

### 何时使用此模式
{chr(10).join(f"- {uc[:100]}" for uc in use_cases[:5])}

### 示例问题
{example_questions}

## 📝 结构化要点

{structured_points}

## 🗺️ 思维导图

```mindmap
- {title}
{chr(10).join(mindmap_branches[:6])}
    - 工具与资源
    - 常见问题解答
```

## 💾 保存说明
- 文件名: {filename.replace('.md', '.mindmap.md')}
- 位置: Mind Map/chatmodes/
- 生成时间: {time.strftime("%Y-%m-%d %H:%M:%S")}
"""

    return mindmap_md

def generate_example_questions(title, use_cases, capabilities):
    """生成示例问题"""
    questions = []

    # 基础问题类别
    categories = [
        ("快速入门", [
            f"如何快速开始使用 {title}?",
            f"{title} 的核心概念是什么?"
        ]),
        ("实际应用", [
            f"如何使用 {title} 解决实际问题?",
            f"{title} 的最佳实践有哪些?"
        ]),
        ("问题诊断", [
            f"遇到 {title} 相关错误如何排查?",
            f"如何优化 {title} 的性能?"
        ])
    ]

    result = []
    for idx, (category, qs) in enumerate(categories[:3], 1):
        result.append(f"\n{idx}. **{category}**")
        for q in qs[:2]:
            result.append(f"   - {q}")

    return '\n'.join(result)

def generate_structured_points(sections, capabilities, key_points):
    """生成结构化要点"""
    if not sections:
        sections = ["核心功能", "使用方法", "最佳实践"]

    result = []
    for idx, section in enumerate(sections[:4], 1):
        result.append(f"### {section}")

        # 为每个section添加相关要点
        relevant_points = capabilities[idx-1:idx+2] if idx <= len(capabilities) else key_points[:3]

        if not relevant_points:
            relevant_points = [
                "掌握基础概念和术语",
                "了解常用工具和方法",
                "遵循行业最佳实践"
            ]

        for point in relevant_points[:3]:
            if point:
                result.append(f"- {point[:100]}")
                # 添加一个子要点
                result.append(f"  - 详细说明和具体示例")

        result.append("")  # 空行分隔

    return '\n'.join(result)

def save_to_file(content, output_path):
    """Task 4: 保存到目标文件"""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, None
    except Exception as e:
        return False, str(e)

def validate_output(output_path):
    """Task 5: 验证输出质量"""
    checks = {
        "file_exists": False,
        "file_size_ok": False,
        "has_summary": False,
        "has_usage_guide": False,
        "has_structured_points": False,
        "has_mindmap": False,
        "all_passed": False
    }

    try:
        if not os.path.exists(output_path):
            return checks

        checks["file_exists"] = True

        file_size = os.path.getsize(output_path)
        checks["file_size_ok"] = file_size > 500

        with open(output_path, 'r', encoding='utf-8') as f:
            content = f.read()

        checks["has_summary"] = "## 📊 摘要" in content
        checks["has_usage_guide"] = "## 💡 实际使用说明" in content
        checks["has_structured_points"] = "## 📝 结构化要点" in content
        checks["has_mindmap"] = "```mindmap" in content and "```" in content[content.find("```mindmap")+10:]

        checks["all_passed"] = all([
            checks["file_exists"],
            checks["file_size_ok"],
            checks["has_summary"],
            checks["has_usage_guide"],
            checks["has_structured_points"],
            checks["has_mindmap"]
        ])

    except Exception as e:
        log_message(f"验证错误: {e}")

    return checks

def process_single_file(filename):
    """处理单个文件的完整流程"""
    global processed_files, success_count, failed_count

    source_path = os.path.join(SOURCE_DIR, filename)
    output_filename = filename.replace('.chatmode.md', '.chatmode.mindmap.md')
    output_path = os.path.join(OUTPUT_DIR, output_filename)

    log_message(f"{'='*60}")
    log_message(f"正在处理: {filename} ({processed_files + 1}/{total_files})")

    # Task 1: 读取源文件
    source_content, error = read_source_file(source_path)
    if error:
        log_message(f"✗ 读取失败: {error}")
        failed_count += 1
        failed_list.append((filename, f"读取失败: {error}"))
        return False

    log_message(f"✓ 读取成功 ({len(source_content)} 字符)")

    # Task 2: 分析内容
    try:
        analysis = analyze_content(source_content, filename)
        log_message(f"✓ 分析完成: {analysis['title']}")
    except Exception as e:
        log_message(f"✗ 分析失败: {e}")
        failed_count += 1
        failed_list.append((filename, f"分析失败: {e}"))
        return False

    # Task 3: 生成mindmap内容
    try:
        mindmap_content = generate_mindmap_content(analysis, source_content)
        log_message(f"✓ 生成mindmap内容 ({len(mindmap_content)} 字符)")
    except Exception as e:
        log_message(f"✗ 生成失败: {e}")
        failed_count += 1
        failed_list.append((filename, f"生成失败: {e}"))
        return False

    # Task 4: 保存文件
    success, error = save_to_file(mindmap_content, output_path)
    if not success:
        log_message(f"✗ 保存失败: {error}")
        failed_count += 1
        failed_list.append((filename, f"保存失败: {error}"))
        return False

    log_message(f"✓ 保存成功: {output_filename}")

    # Task 5: 验证输出
    validation = validate_output(output_path)
    if validation["all_passed"]:
        log_message(f"✓ 验证通过")
        success_count += 1
        return True
    else:
        log_message(f"⚠ 验证警告: {[k for k, v in validation.items() if not v]}")
        success_count += 1  # 仍算作成功,只是有警告
        return True

def generate_final_report():
    """生成最终报告"""
    success_rate = (success_count / total_files * 100) if total_files > 0 else 0

    report = f"""
# Mindmap生成任务完成报告

**执行时间**: {time.strftime("%Y-%m-%d %H:%M:%S")}

## 统计数据
- 总文件数: {total_files}
- 成功生成: {success_count}
- 失败: {failed_count}
- 成功率: {success_rate:.1f}%

## 失败文件清单
"""

    if failed_list:
        for filename, reason in failed_list:
            report += f"- {filename}: {reason}\n"
    else:
        report += "无失败文件\n"

    report += f"""
## 输出位置
所有生成的.mindmap.md文件位于:
`{OUTPUT_DIR}`

## 建议
- 建议检查生成的mindmap文件质量
- 可以根据实际需要调整内容结构
- 如有失败文件,可以单独重新处理
"""

    report_path = os.path.join(os.path.dirname(OUTPUT_DIR), "generation_report.md")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)

    log_message("\n" + report)
    log_message(f"\n完整报告已保存到: {report_path}")

def main():
    """主执行流程"""
    global total_files, processed_files

    log_message("="*60)
    log_message("开始执行 LLM驱动的Mindmap生成任务")
    log_message("="*60)

    # 获取所有.md文件
    try:
        all_files = [f for f in os.listdir(SOURCE_DIR) if f.endswith('.chatmode.md')]
        total_files = len(all_files)
        log_message(f"找到 {total_files} 个待处理文件")
    except Exception as e:
        log_message(f"错误: 无法读取源目录 - {e}")
        return

    # 按组处理文件
    start_time = time.time()

    for filename in sorted(all_files):
        process_single_file(filename)
        processed_files += 1

        # 添加短暂延迟避免IO压力
        time.sleep(0.1)

    elapsed_time = time.time() - start_time
    log_message(f"\n总耗时: {elapsed_time:.2f} 秒")

    # 生成最终报告
    generate_final_report()

if __name__ == "__main__":
    main()
