"""
批量生成思维导图文件
从 chatmodes 文件夹读取所有 .md 件,并生成对应的 .mindmap.md 文件
根据每个文件的实际内容生成个性化的摘要和问题
"""

import os
import re
from pathlib import Path

def parse_markdown_structure(content):
    """解析 Markdown 文件的完整结构,包括标题和内容"""
    lines = content.split('\n')
    structure = []
    current_section = None

    for i, line in enumerate(lines):
        stripped = line.strip()

        # 检测标题
        if stripped.startswith('####'):
            title = stripped.replace('####', '').strip()
            structure.append({
                'level': 4,
                'title': title,
                'content': [],
                'line_num': i
            })
            current_section = structure[-1]
        elif stripped.startswith('###'):
            title = stripped.replace('###', '').strip()
            structure.append({
                'level': 3,
                'title': title,
                'content': [],
                'line_num': i
            })
            current_section = structure[-1]
        elif stripped.startswith('##'):
            title = stripped.replace('##', '').strip()
            structure.append({
                'level': 2,
                'title': title,
                'content': [],
                'line_num': i
            })
            current_section = structure[-1]
        elif stripped and current_section and not stripped.startswith('#'):
            # 收集每个标题下的内容
            if not stripped.startswith('```'):
                current_section['content'].append(stripped)

    return structure

def extract_key_points(structure):
    """从结构中提取关键要点"""
    points = []
    for section in structure:
        # 提取列表项
        for content_line in section['content']:
            if content_line.startswith('- **') or content_line.startswith('* **'):
                # 提取加粗的关键词
                match = re.search(r'\*\*([^*]+)\*\*:?\s*(.+)?', content_line)
                if match:
                    points.append({
                        'section': section['title'],
                        'keyword': match.group(1),
                        'description': match.group(2) if match.group(2) else ''
                    })
            elif content_line.startswith('- ') or content_line.startswith('* '):
                # 普通列表项
                text = content_line.lstrip('- *').strip()
                if text and len(text) < 100:  # 避免太长的内容
                    points.append({
                        'section': section['title'],
                        'keyword': text,
                        'description': ''
                    })
    return points

def extract_front_matter(content):
    """提取 front matter"""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[1].strip(), parts[2].strip()
    return None, content

def analyze_content_themes(structure, key_points):
    """分析内容主题,生成个性化的问题类别"""
    themes = {
        'performance': [],
        'error_handling': [],
        'architecture': [],
        'integration': [],
        'best_practices': []
    }

    # 关键词匹配
    keywords_map = {
        'performance': ['performance', 'optimization', 'cost', 'efficient', 'speed', 'throughput', 'scalability'],
        'error_handling': ['error', 'exception', 'retry', 'fault', 'resilience', 'handling', 'debugging', 'troubleshoot'],
        'architecture': ['architecture', 'design', 'pattern', 'structure', 'scaling', 'deployment', 'component'],
        'integration': ['integration', 'api', 'connector', 'hybrid', 'connectivity', 'service', 'communication'],
        'best_practices': ['best practice', 'guideline', 'standard', 'convention', 'approach', 'methodology']
    }

    # 分析每个要点
    for point in key_points:
        text = (point['keyword'] + ' ' + point['description']).lower()
        for theme, keywords in keywords_map.items():
            if any(kw in text for kw in keywords):
                themes[theme].append(point)

    return themes

def generate_contextual_questions(structure, key_points, themes):
    """根据实际内容生成个性化的问题"""
    questions = []
    question_num = 1

    # 根据主题生成问题
    if themes['performance']:
        keywords = ', '.join([p['keyword'] for p in themes['performance'][:3]])
        questions.append(f"""#### {question_num}. 性能优化与效率提升类问题

关注如何提升系统性能、降低成本和优化资源使用。
> **问题示例:**
> 在处理 {keywords} 相关场景时,如何进行性能优化和效率提升?""")
        question_num += 1

    if themes['error_handling']:
        keywords = ', '.join([p['keyword'] for p in themes['error_handling'][:3]])
        questions.append(f"""#### {question_num}. 错误处理与容错设计类问题

关注如何构建健壮的系统,优雅处理异常和故障。
> **问题示例:**
> 在实现 {keywords} 时,如何设计有效的错误处理和容错机制?""")
        question_num += 1

    if themes['architecture']:
        keywords = ', '.join([p['keyword'] for p in themes['architecture'][:3]])
        questions.append(f"""#### {question_num}. 架构设计与模式应用类问题

聚焦系统架构、设计模式和可扩展性。
> **问题示例:**
> 在设计涉及 {keywords} 的系统时,应该采用什么样的架构模式和设计方法?""")
        question_num += 1

    if themes['integration']:
        keywords = ', '.join([p['keyword'] for p in themes['integration'][:3]])
        questions.append(f"""#### {question_num}. 集成与连接性类问题

关注系统间集成、API 设计和混合连接。
> **问题示例:**
> 如何实现与 {keywords} 相关的系统集成,确保安全性和可靠性?""")
        question_num += 1

    if themes['best_practices']:
        keywords = ', '.join([p['keyword'] for p in themes['best_practices'][:3]])
        questions.append(f"""#### {question_num}. 最佳实践与标准规范类问题

聚焦行业标准、开发规范和团队协作。
> **问题示例:**
> 在 {keywords} 方面,有哪些被广泛认可的最佳实践和开发标准?""")
        question_num += 1

    # 如果某些主题为空,使用通用问题
    if len(questions) < 3:
        questions.append(f"""#### {question_num}. 代码质量与可维护性类问题

关注代码质量、可读性和长期维护。
> **问题示例:**
> 如何确保代码符合该领域的质量标准,便于团队协作和长期维护?""")

    return "\n\n".join(questions)

def generate_summary(filename, front_matter, content, structure, key_points):
    """根据文件实际内容生成个性化摘要"""
    # 从 front matter 提取描述
    description = ""
    if front_matter:
        desc_match = re.search(r"description:\s*['\"](.+?)['\"]", front_matter, re.DOTALL)
        if desc_match:
            description = desc_match.group(1)

    # 提取文件主标题
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else filename.replace('.chatmode.md', '')

    # 分析内容主题
    themes = analyze_content_themes(structure, key_points)

    # 提取适用场景 - 从实际内容中找
    scenarios = []
    for section in structure:
        if any(keyword in section['title'].lower() for keyword in ['scenario', 'use case', 'when to', 'application', 'approach']):
            scenarios.extend([c for c in section['content'] if c.startswith('- ') or c.startswith('* ')])

    if not scenarios:
        # 从其他部分提取有用的场景信息
        for section in structure[:5]:  # 查看前几个部分
            for content_line in section['content']:
                if content_line.startswith('- ') or content_line.startswith('* '):
                    scenarios.append(content_line)
                    if len(scenarios) >= 5:
                        break
            if len(scenarios) >= 5:
                break

    if not scenarios:
        scenarios = [
            "- 需要专业领域指导的开发任务",
            "- 代码审查和最佳实践建议",
            "- 架构设计和技术决策"
        ]

    # 提取主要用途 - 从核心专长或关键领域中总结
    purposes = []
    for section in structure:
        if any(keyword in section['title'].lower() for keyword in ['core', 'expertise', 'focus', 'key', 'knowledge']):
            for content_line in section['content'][:3]:
                if content_line.startswith('- ') or content_line.startswith('* '):
                    purposes.append(content_line)
                elif '**' in content_line:  # 包含加粗的关键内容
                    purposes.append(content_line)

    purpose_text = "通过专业的提示词模板,为特定技术领域或开发场景提供专家级的指导和建议。"
    if purposes:
        purpose_text = "\n".join(purposes[:3])

    # 生成个性化的问题示例
    questions = generate_contextual_questions(structure, key_points, themes)

    return f"""## 摘要

**功能**: {title}

**描述**: {description if description else '此聊天模式用于特定的开发场景'}

**适用场景**:
{chr(10).join(scenarios[:5])}

**主要用途**:
{purpose_text}

### 实际使用说明示例问题(最佳实践)

> **说明:**
> 以下问题根据该文档的实际内容和关键词自动生成,涵盖文档的核心主题、典型场景和最佳实践。

{questions}
"""

def generate_structured_list(structure, key_points):
    """生成结构化要点列表(包含关键内容要点)"""
    if not structure:
        return "- 暂无结构化内容\n"

    output = []
    for section in structure:
        indent = "  " * (section['level'] - 2)

        # 添加标题
        output.append(f"{indent}- {section['title']}")

        # 添加该部分的关键要点
        section_points = [p for p in key_points if p['section'] == section['title']]
        for point in section_points[:5]:  # 限制每个部分最多5个要点
            sub_indent = indent + "  "
            if point['description']:
                output.append(f"{sub_indent}- {point['keyword']}: {point['description'][:80]}")
            else:
                output.append(f"{sub_indent}- {point['keyword']}")

    return '\n'.join(output)

def generate_mindmap(structure, key_points):
    """生成思维导图格式(中文,清晰的层级结构)"""
    if not structure:
        return "- 暂无内容\n"

    output = []

    for section in structure:
        level = section['level']
        title = section['title']

        if level == 2:
            output.append(f"- {title}")

            # 为 H2 添加其直接的关键要点
            section_points = [p for p in key_points if p['section'] == title]
            for point in section_points[:3]:
                output.append(f"  - {point['keyword']}")

        elif level == 3:
            output.append(f"  - {title}")

            # 为 H3 添加关键要点
            section_points = [p for p in key_points if p['section'] == title]
            for point in section_points[:3]:
                output.append(f"    - {point['keyword']}")

        elif level == 4:
            output.append(f"    - {title}")

    return '\n'.join(output)

def process_file(input_path, output_dir):
    """处理单个 Markdown 文件"""
    try:
        # 读取文件
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 提取 front matter
        front_matter, main_content = extract_front_matter(content)

        # 解析结构和关键要点
        structure = parse_markdown_structure(main_content)
        key_points = extract_key_points(structure)

        # 获取文件名信息
        filename = os.path.basename(input_path)
        parent_folder = os.path.basename(os.path.dirname(input_path))
        output_filename = filename.replace('.md', '.mindmap.md')

        # 生成输出内容
        summary = generate_summary(filename, front_matter, main_content, structure, key_points)
        structured_list = generate_structured_list(structure, key_points)
        mindmap = generate_mindmap(structure, key_points)

        # 组合完整输出
        output_content = f"""{summary}

## 结构化要点(嵌套 Markdown 列表 - 中英文对照)

{structured_list}

## 思维导图格式 Markdown

{mindmap}

## 保存说明

已将思维导图 Markdown 文件保存至:
{os.path.join(output_dir, parent_folder, output_filename)}

### 原始文件信息

- **原始文件**: {input_path}
- **父文件夹**: {parent_folder}
- **文件名**: {filename}
"""

        # 创建输出目录
        output_folder = os.path.join(output_dir, parent_folder)
        os.makedirs(output_folder, exist_ok=True)

        # 写入文件
        output_path = os.path.join(output_folder, output_filename)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(output_content)

        return True, output_path
    except Exception as e:
        return False, str(e)

def main():
    """主函数"""
    input_dir = r"D:\mycode\awesome-copilot\chatmodes"
    output_base_dir = r"D:\mycode\awesome-copilot\my-custom\Mind Map"

    # 获取所有 .md 文件
    md_files = list(Path(input_dir).glob('*.md'))

    print(f"找到 {len(md_files)} 个 Markdown 文件")
    print("开始处理...\n")

    success_count = 0
    failed_count = 0

    for md_file in md_files:
        print(f"处理: {md_file.name}...", end=' ')
        success, result = process_file(str(md_file), output_base_dir)

        if success:
            print("✓ 成功")
            success_count += 1
        else:
            print(f"✗ 失败: {result}")
            failed_count += 1

    print("\n处理完成!")
    print(f"成功: {success_count} 个")
    print(f"失败: {failed_count} 个")
    print(f"\n输出目录: {output_base_dir}")

if __name__ == "__main__":
    main()
