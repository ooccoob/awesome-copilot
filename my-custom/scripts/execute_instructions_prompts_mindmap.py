"""
LLM驱动的Instructions和Prompts Mindmap生成执行脚本
根据TASK_PLAN_INSTRUCTIONS_PROMPTS_MINDMAP.md中的计划执行
处理两个目录: instructions/ 和 prompts/
"""

import os
import json
import time
from pathlib import Path

# 配置路径
BASE_DIR = r"D:\mycode\awesome-copilot"
INSTRUCTIONS_SOURCE_DIR = os.path.join(BASE_DIR, "instructions")
PROMPTS_SOURCE_DIR = os.path.join(BASE_DIR, "prompts")
INSTRUCTIONS_OUTPUT_DIR = os.path.join(BASE_DIR, r"my-custom\Mind Map\instructions")
PROMPTS_OUTPUT_DIR = os.path.join(BASE_DIR, r"my-custom\Mind Map\prompts")
LOG_FILE = os.path.join(BASE_DIR, r"my-custom\Mind Map\instructions_prompts_generation_log.txt")

# 确保输出目录存在
Path(INSTRUCTIONS_OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(PROMPTS_OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

# 进度跟踪变量
instructions_total = 0
instructions_processed = 0
instructions_success = 0
instructions_failed = 0

prompts_total = 0
prompts_processed = 0
prompts_success = 0
prompts_failed = 0

total_files = 0
total_processed = 0
total_success = 0
total_failed = 0

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

def extract_frontmatter(content):
    """提取Front Matter元数据"""
    frontmatter = {}
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm_text = parts[1].strip()
            for line in fm_text.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    frontmatter[key.strip()] = value.strip().strip('"\'')
    return frontmatter

def analyze_instructions_content(content, filename):
    """Task 2.1: 分析Instructions文件内容"""
    lines = content.split('\n')
    frontmatter = extract_frontmatter(content)

    # 提取标题
    title = frontmatter.get('description', filename.replace('.instructions.md', '').replace('-', ' ').title())

    analysis = {
        "title": title,
        "description": frontmatter.get('description', ''),
        "file_type": "instructions",
        "applies_to": frontmatter.get('applyTo', '**/*'),
        "filename": filename,
        "core_themes": [],
        "key_rules": [],
        "technologies": [],
        "sections": [],
        "key_terms": []
    }

    # 提取章节标题
    current_section = None
    for line in lines:
        if line.startswith('## '):
            section_title = line.strip('# ').strip()
            analysis["sections"].append(section_title)
            analysis["core_themes"].append(section_title)
        elif line.startswith('### '):
            subsection = line.strip('# ').strip()
            analysis["key_rules"].append(subsection)

    return analysis

def analyze_prompts_content(content, filename):
    """Task 2.2: 分析Prompts文件内容"""
    lines = content.split('\n')
    frontmatter = extract_frontmatter(content)

    # 提取标题
    title = frontmatter.get('description', filename.replace('.prompt.md', '').replace('-', ' ').title())

    analysis = {
        "title": title,
        "description": frontmatter.get('description', ''),
        "file_type": "prompts",
        "filename": filename,
        "task_goal": "",
        "workflow_steps": [],
        "required_inputs": [],
        "output_format": "",
        "tools_involved": frontmatter.get('tools', '').split(',') if frontmatter.get('tools') else [],
        "key_features": [],
        "use_scenarios": [],
        "sections": []
    }

    # 提取章节和步骤
    for line in lines:
        if line.startswith('## '):
            section_title = line.strip('# ').strip()
            analysis["sections"].append(section_title)
        elif line.startswith('### '):
            subsection = line.strip('# ').strip()
            analysis["workflow_steps"].append(subsection)
        elif line.strip().startswith(('1.', '2.', '3.', '4.', '5.')):
            step = line.strip().lstrip('0123456789.').strip()
            if step and step not in analysis["workflow_steps"]:
                analysis["workflow_steps"].append(step)

    return analysis

def generate_instructions_mindmap(analysis, source_content):
    """Task 3.1: 生成Instructions类型的Mindmap"""
    title = analysis['title']
    description = analysis['description']
    applies_to = analysis['applies_to']
    filename = analysis['filename']
    sections = analysis['sections']

    # 提取技术栈信息
    tech_keywords = ['TypeScript', 'JavaScript', 'Python', 'Java', 'C#', '.NET', 'Azure',
                     'Docker', 'Kubernetes', 'React', 'Vue', 'Angular', 'Spring', 'Quarkus']
    technologies = [tech for tech in tech_keywords if tech.lower() in source_content.lower()]

    # 提取核心规则
    rules = []
    lines = source_content.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('- ') or line.startswith('* '):
            rule = line.strip('- *').strip()
            if rule and len(rule) > 10 and len(rule) < 200:
                rules.append(rule)

    # 生成思维导图分支
    mindmap_branches = []
    mindmap_branches.append("  - 适用范围")
    mindmap_branches.append(f"    - 文件类型: {applies_to}")
    if technologies:
        mindmap_branches.append(f"    - 技术栈: {', '.join(technologies[:5])}")

    if sections:
        mindmap_branches.append("  - 核心规则")
        for section in sections[:5]:
            mindmap_branches.append(f"    - {section}")

    mindmap_branches.append("  - 最佳实践")
    mindmap_branches.append("    - 代码质量")
    mindmap_branches.append("    - 性能优化")
    mindmap_branches.append("    - 安全考虑")

    mindmap_md = f"""# {title} - Instructions Mindmap

## 📊 摘要
{description if description else f'{title}的开发指南和最佳实践'}

本指令提供了关于{title}的核心规范和最佳实践,帮助开发者编写高质量、可维护的代码。

## 🎯 适用范围
- **文件类型**: `{applies_to}`
- **技术栈**: {', '.join(technologies[:5]) if technologies else '见文档详情'}
- **场景**: 开发和维护{title}相关项目时使用

## 💡 核心规则与最佳实践

### 主要规范
{chr(10).join(f"- {rule[:150]}" for rule in rules[:8])}

### 代码质量标准
- 遵循行业标准编码规范
- 保持代码简洁可读
- 添加适当的注释和文档
- 进行充分的测试覆盖

## 📝 关键技术要点

### 项目配置
- 正确设置开发环境
- 配置必要的工具和依赖
- 遵循项目结构规范

### 实现标准
- 使用推荐的设计模式
- 遵循命名规范
- 注意性能和安全考虑

## 🗺️ 思维导图

```mindmap
- {title}
{chr(10).join(mindmap_branches)}
```

## 💾 保存说明
- 文件名: {filename.replace('.md', '.mindmap.md')}
- 位置: Mind Map/instructions/
- 生成时间: {time.strftime("%Y-%m-%d %H:%M:%S")}
- 文件类型: Instructions (编程规范/最佳实践)
"""

    return mindmap_md

def generate_prompts_mindmap(analysis, source_content):
    """Task 3.2: 生成Prompts类型的Mindmap"""
    title = analysis['title']
    description = analysis['description']
    filename = analysis['filename']
    tools = analysis['tools_involved']
    sections = analysis['sections']
    workflow_steps = analysis['workflow_steps']

    # 提取输入输出信息
    inputs = []
    outputs = []
    lines = source_content.split('\n')
    in_input_section = False
    in_output_section = False

    for line in lines:
        line_lower = line.lower()
        if 'input' in line_lower and line.startswith('#'):
            in_input_section = True
            in_output_section = False
        elif 'output' in line_lower and line.startswith('#'):
            in_output_section = True
            in_input_section = False
        elif line.startswith('#'):
            in_input_section = False
            in_output_section = False
        elif line.startswith('- ') or line.startswith('* '):
            item = line.strip('- *').strip()
            if in_input_section and item:
                inputs.append(item)
            elif in_output_section and item:
                outputs.append(item)

    # 生成思维导图分支
    mindmap_branches = []

    if inputs or outputs:
        mindmap_branches.append("  - 输入输出")
        if inputs:
            mindmap_branches.append("    - 输入要求")
            for inp in inputs[:3]:
                mindmap_branches.append(f"      - {inp[:50]}")
        if outputs:
            mindmap_branches.append("    - 输出内容")
            for out in outputs[:3]:
                mindmap_branches.append(f"      - {out[:50]}")

    if workflow_steps:
        mindmap_branches.append("  - 处理流程")
        for step in workflow_steps[:5]:
            mindmap_branches.append(f"    - {step[:50]}")

    if tools:
        mindmap_branches.append("  - 工具技术")
        for tool in tools[:5]:
            if tool.strip():
                mindmap_branches.append(f"    - {tool.strip()}")

    mindmap_md = f"""# {title} - Prompt Mindmap

## 📊 摘要
{description if description else f'{title}的任务提示词'}

本提示词定义了{title}的具体执行流程,包括输入要求、处理步骤和输出格式。

## 🚀 使用场景
- **主要用途**: {title}
- **适用时机**: 需要{title}时使用
- **预期效果**: 自动化完成{title}相关任务
{f"- **推荐工具**: {', '.join(tools[:3])}" if tools else ""}

## 💡 工作流程

### 输入准备
{chr(10).join(f"- {inp[:150]}" for inp in inputs[:5]) if inputs else "- 根据具体任务准备必要的输入信息"}

### 执行步骤
{chr(10).join(f"{i+1}. {step[:150]}" for i, step in enumerate(workflow_steps[:8])) if workflow_steps else "1. 分析任务需求\n2. 执行核心处理\n3. 生成输出结果"}

### 输出内容
{chr(10).join(f"- {out[:150]}" for out in outputs[:5]) if outputs else "- 生成符合要求的输出"}

## 📝 关键特性

### 自动化能力
- 减少手动操作
- 提高处理效率
- 确保输出一致性

### 质量控制
- 遵循最佳实践
- 进行格式验证
- 提供错误处理

## 🔧 工具与技术

{chr(10).join(f"- **{tool.strip()}**" for tool in tools if tool.strip()) if tools else "- 根据任务需要使用相应工具"}

## 🗺️ 思维导图

```mindmap
- {title}
  - 使用场景
    - 主要用途
    - 适用时机
{chr(10).join(mindmap_branches)}
```

## 💾 保存说明
- 文件名: {filename.replace('.md', '.mindmap.md')}
- 位置: Mind Map/prompts/
- 生成时间: {time.strftime("%Y-%m-%d %H:%M:%S")}
- 文件类型: Prompts (AI任务提示词)
"""

    return mindmap_md

def save_to_file(content, output_path):
    """Task 4: 保存到目标文件"""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, None
    except Exception as e:
        return False, str(e)

def validate_output(output_path, file_type):
    """Task 5: 验证输出质量"""
    checks = {
        "file_exists": False,
        "file_size_ok": False,
        "has_summary": False,
        "has_usage_or_scope": False,
        "has_key_content": False,
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

        if file_type == "instructions":
            checks["has_usage_or_scope"] = "## 🎯 适用范围" in content
            checks["has_key_content"] = "## 💡 核心规则与最佳实践" in content
        else:  # prompts
            checks["has_usage_or_scope"] = "## 🚀 使用场景" in content
            checks["has_key_content"] = "## 💡 工作流程" in content

        checks["has_mindmap"] = "```mindmap" in content and "```" in content[content.find("```mindmap")+10:]

        checks["all_passed"] = all([
            checks["file_exists"],
            checks["file_size_ok"],
            checks["has_summary"],
            checks["has_usage_or_scope"],
            checks["has_key_content"],
            checks["has_mindmap"]
        ])

    except Exception as e:
        log_message(f"验证错误: {e}")

    return checks

def process_instructions_file(filename):
    """处理单个Instructions文件"""
    global instructions_processed, instructions_success, instructions_failed
    global total_processed, total_success, total_failed

    source_path = os.path.join(INSTRUCTIONS_SOURCE_DIR, filename)
    output_filename = filename.replace('.instructions.md', '.instructions.mindmap.md')
    output_path = os.path.join(INSTRUCTIONS_OUTPUT_DIR, output_filename)

    log_message(f"{'='*80}")
    log_message(f"[Instructions] 正在处理: {filename} ({instructions_processed + 1}/{instructions_total})")

    # Task 1: 读取源文件
    source_content, error = read_source_file(source_path)
    if error:
        log_message(f"✗ 读取失败: {error}")
        instructions_failed += 1
        total_failed += 1
        failed_list.append((filename, f"[Instructions] 读取失败: {error}"))
        return False

    log_message(f"✓ 读取成功 ({len(source_content)} 字符)")

    # Task 2: 分析内容
    try:
        analysis = analyze_instructions_content(source_content, filename)
        log_message(f"✓ 分析完成: {analysis['title']}")
    except Exception as e:
        log_message(f"✗ 分析失败: {e}")
        instructions_failed += 1
        total_failed += 1
        failed_list.append((filename, f"[Instructions] 分析失败: {e}"))
        return False

    # Task 3: 生成mindmap内容
    try:
        mindmap_content = generate_instructions_mindmap(analysis, source_content)
        log_message(f"✓ 生成mindmap内容 ({len(mindmap_content)} 字符)")
    except Exception as e:
        log_message(f"✗ 生成失败: {e}")
        instructions_failed += 1
        total_failed += 1
        failed_list.append((filename, f"[Instructions] 生成失败: {e}"))
        return False

    # Task 4: 保存文件
    success, error = save_to_file(mindmap_content, output_path)
    if not success:
        log_message(f"✗ 保存失败: {error}")
        instructions_failed += 1
        total_failed += 1
        failed_list.append((filename, f"[Instructions] 保存失败: {error}"))
        return False

    log_message(f"✓ 保存成功: {output_filename}")

    # Task 5: 验证输出
    validation = validate_output(output_path, "instructions")
    if validation["all_passed"]:
        log_message(f"✓ 验证通过")
        instructions_success += 1
        total_success += 1
        return True
    else:
        log_message(f"⚠ 验证警告: {[k for k, v in validation.items() if not v]}")
        instructions_success += 1
        total_success += 1
        return True

def process_prompts_file(filename):
    """处理单个Prompts文件"""
    global prompts_processed, prompts_success, prompts_failed
    global total_processed, total_success, total_failed

    source_path = os.path.join(PROMPTS_SOURCE_DIR, filename)
    output_filename = filename.replace('.prompt.md', '.prompt.mindmap.md')
    output_path = os.path.join(PROMPTS_OUTPUT_DIR, output_filename)

    log_message(f"{'='*80}")
    log_message(f"[Prompts] 正在处理: {filename} ({prompts_processed + 1}/{prompts_total})")

    # Task 1: 读取源文件
    source_content, error = read_source_file(source_path)
    if error:
        log_message(f"✗ 读取失败: {error}")
        prompts_failed += 1
        total_failed += 1
        failed_list.append((filename, f"[Prompts] 读取失败: {error}"))
        return False

    log_message(f"✓ 读取成功 ({len(source_content)} 字符)")

    # Task 2: 分析内容
    try:
        analysis = analyze_prompts_content(source_content, filename)
        log_message(f"✓ 分析完成: {analysis['title']}")
    except Exception as e:
        log_message(f"✗ 分析失败: {e}")
        prompts_failed += 1
        total_failed += 1
        failed_list.append((filename, f"[Prompts] 分析失败: {e}"))
        return False

    # Task 3: 生成mindmap内容
    try:
        mindmap_content = generate_prompts_mindmap(analysis, source_content)
        log_message(f"✓ 生成mindmap内容 ({len(mindmap_content)} 字符)")
    except Exception as e:
        log_message(f"✗ 生成失败: {e}")
        prompts_failed += 1
        total_failed += 1
        failed_list.append((filename, f"[Prompts] 生成失败: {e}"))
        return False

    # Task 4: 保存文件
    success, error = save_to_file(mindmap_content, output_path)
    if not success:
        log_message(f"✗ 保存失败: {error}")
        prompts_failed += 1
        total_failed += 1
        failed_list.append((filename, f"[Prompts] 保存失败: {e}"))
        return False

    log_message(f"✓ 保存成功: {output_filename}")

    # Task 5: 验证输出
    validation = validate_output(output_path, "prompts")
    if validation["all_passed"]:
        log_message(f"✓ 验证通过")
        prompts_success += 1
        total_success += 1
        return True
    else:
        log_message(f"⚠ 验证警告: {[k for k, v in validation.items() if not v]}")
        prompts_success += 1
        total_success += 1
        return True

def generate_final_report():
    """生成最终报告"""
    instructions_rate = (instructions_success / instructions_total * 100) if instructions_total > 0 else 0
    prompts_rate = (prompts_success / prompts_total * 100) if prompts_total > 0 else 0
    total_rate = (total_success / total_files * 100) if total_files > 0 else 0

    report = f"""
# Instructions和Prompts Mindmap生成任务完成报告

**执行时间**: {time.strftime("%Y-%m-%d %H:%M:%S")}

## 统计数据

### Instructions处理结果
- 总文件数: {instructions_total}
- 成功生成: {instructions_success}
- 失败: {instructions_failed}
- 成功率: {instructions_rate:.1f}%

### Prompts处理结果
- 总文件数: {prompts_total}
- 成功生成: {prompts_success}
- 失败: {prompts_failed}
- 成功率: {prompts_rate:.1f}%

### 总计
- 总文件数: {total_files}
- 总成功数: {total_success}
- 总失败数: {total_failed}
- 总成功率: {total_rate:.1f}%

## 失败文件清单
"""

    if failed_list:
        instructions_failures = [f for f in failed_list if f[1].startswith('[Instructions]')]
        prompts_failures = [f for f in failed_list if f[1].startswith('[Prompts]')]

        if instructions_failures:
            report += "\n### Instructions失败文件\n"
            for filename, reason in instructions_failures:
                report += f"- {filename}: {reason}\n"

        if prompts_failures:
            report += "\n### Prompts失败文件\n"
            for filename, reason in prompts_failures:
                report += f"- {filename}: {reason}\n"
    else:
        report += "无失败文件\n"

    report += f"""
## 输出位置
- Instructions Mindmaps: `{INSTRUCTIONS_OUTPUT_DIR}`
- Prompts Mindmaps: `{PROMPTS_OUTPUT_DIR}`

## 质量分析
所有生成的mindmap文件已按照Instructions和Prompts的不同特点进行结构化处理:
- Instructions: 突出规范性和最佳实践
- Prompts: 突出工作流程和可执行性

## 建议
- 建议检查生成的mindmap文件质量
- 可以根据实际需要调整内容结构
- Instructions mindmap适合开发规范参考
- Prompts mindmap适合任务执行指导
"""

    report_path = os.path.join(BASE_DIR, r"my-custom\Mind Map\instructions_prompts_generation_report.md")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)

    log_message("\n" + report)
    log_message(f"\n完整报告已保存到: {report_path}")

def main():
    """主执行流程"""
    global instructions_total, instructions_processed
    global prompts_total, prompts_processed
    global total_files, total_processed

    log_message("="*80)
    log_message("开始执行 Instructions和Prompts Mindmap生成任务")
    log_message("="*80)

    # 获取Instructions文件列表
    try:
        instructions_files = [f for f in os.listdir(INSTRUCTIONS_SOURCE_DIR) if f.endswith('.instructions.md')]
        instructions_total = len(instructions_files)
        log_message(f"找到 {instructions_total} 个Instructions文件")
    except Exception as e:
        log_message(f"错误: 无法读取Instructions目录 - {e}")
        instructions_files = []
        instructions_total = 0

    # 获取Prompts文件列表
    try:
        prompts_files = [f for f in os.listdir(PROMPTS_SOURCE_DIR) if f.endswith('.prompt.md')]
        prompts_total = len(prompts_files)
        log_message(f"找到 {prompts_total} 个Prompts文件")
    except Exception as e:
        log_message(f"错误: 无法读取Prompts目录 - {e}")
        prompts_files = []
        prompts_total = 0

    total_files = instructions_total + prompts_total
    log_message(f"总计 {total_files} 个待处理文件\n")

    if total_files == 0:
        log_message("没有找到待处理文件,退出执行")
        return

    start_time = time.time()

    # 策略A: 先处理所有Instructions,再处理所有Prompts
    log_message("\n" + "="*80)
    log_message("阶段1: 处理Instructions文件")
    log_message("="*80 + "\n")

    for filename in sorted(instructions_files):
        process_instructions_file(filename)
        instructions_processed += 1
        total_processed += 1
        time.sleep(0.1)  # 短暂延迟

    log_message("\n" + "="*80)
    log_message("阶段2: 处理Prompts文件")
    log_message("="*80 + "\n")

    for filename in sorted(prompts_files):
        process_prompts_file(filename)
        prompts_processed += 1
        total_processed += 1
        time.sleep(0.1)  # 短暂延迟

    elapsed_time = time.time() - start_time
    log_message(f"\n{'='*80}")
    log_message(f"总耗时: {elapsed_time:.2f} 秒 ({elapsed_time/60:.2f} 分钟)")
    log_message(f"{'='*80}\n")

    # 生成最终报告
    generate_final_report()

if __name__ == "__main__":
    main()
