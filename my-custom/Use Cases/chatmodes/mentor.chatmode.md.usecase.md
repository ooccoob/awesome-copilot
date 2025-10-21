---
post_title: "mentor.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "mentor-chatmode-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: ["use-cases","chatmode","mentorship"]
tags: ["use-cases","mentor","guidance"]
ai_note: "Generated with AI assistance from chatmodes/mentor.chatmode.md"
summary: "Use cases for Mentor mode: guiding engineers with Socratic questioning, code review prompts, and stepwise problem decomposition." 
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- A coaching/mentor chatmode that helps engineers think critically, challenge assumptions, and explore alternate solutions using guided questions and suggestions.

## When

- When an engineer is designing a new feature, refactoring complex code, or needs to reason about trade-offs and long-term maintainability.

## Why

- To improve engineering judgment, reduce risky shortcuts, and increase the quality of design decisions through a guided mentorship approach.

## How

- Use Socratic questioning, the 5 Whys, and pointed guidance rather than making direct code edits. Use repository search to ground advice in context.
- Provide concise, actionable hints; encourage small experiments and tests; call out unsafe practices and their long-term costs.

## Key points (英文+中文对照)

- Socratic questioning to surface assumptions（苏格拉底式提问以揭示假设）
- Short, focused guidance—avoid excessive verbosity（简短、聚焦的引导——避免冗长）
- Use repository context to ground suggestions（利用仓库上下文定位建议）

## 使用场景

### 1. 方案设计评审

- 用户故事：作为工程师，我希望在实现前得到针对设计缺陷与风险点的系统性反馈。
- 例 1："[评审] 请逐步质疑以下设计决策并指出潜在风险： <paste design summary>。"
- 例 2："[权衡] 帮我列出采用方案 A 与方案 B 的优缺点并给出建议的试验步骤。"
- 例 3："[角色角度] 从安全/性能/可维护性角度分别评估此方案并提出改进。"
- 例 4："[减小隔离] 给出可以减小变更影响域的分阶段实施计划。"
- 例 5："[决策记录] 帮我写一段会议记录，包含关键决策与未决问题。"

### 2. 调试与问题定位

- 用户故事：作为开发者，我在现场遇到一个棘手的 bug，想要有人引导我逐步定位问题。
- 例 1："[定位] 给我一个调试步骤清单来复现并定位这个错误。"
- 例 2："[日志分析] 指导我如何从日志中提取有价值的信息并构建假设。"
- 例 3："[断点策略] 建议在哪些函数/模块设置断点以快速缩小问题范围。"
- 例 4："[回滚策略] 当修复失败时，如何快速打造安全回滚步骤？"
- 例 5："[问答] 用 5 个关键问题来挑战当前故障假设。"

### 3. 能力提升与培训

- 用户故事：作为主管，我需要为团队新人准备练习题与评估方案以跟踪成长。
- 例 1："[练习] 请为新人生成一组 10 道练习题（含参考答案）来评估其对代码可维护性的理解。"
- 例 2："[反馈] 给出一段代码并要求 mentor 模式给出 3 点改进建议。"
- 例 3："[学习路径] 为后端工程师设计为期 6 周的学习与实践计划。"
- 例 4："[面试题] 生成一道面试题并给出评分标准与参考答案。"
- 例 5："[复盘] 指导如何写一次正确的事后复盘以汲取教训。"

### 4. 决策记录与沟通

- 用户故事：作为团队负责人，我希望将复杂技术讨论转化为清晰的决策记录与任务项。
- 例 1："[记录] 将下面的讨论要点转为会议纪要并列出后续任务。"
- 例 2："[沟通] 帮我写给利益相关者的简短说明，解释为何采取该技术路径。"
- 例 3："[优先级] 请按风险与价值对当前待办事项排序并说明理由。"
- 例 4："[透明度] 生成一段可公开的变更摘要以供非技术利益相关者阅读。"
- 例 5："[会议议程] 为下次评审准备一份结构化议程与关键问题清单。"

## 原始文件

- ../../../../chatmodes/mentor.chatmode.md
---
post_title: 'mentor — Use Cases'
post_slug: 'mentor-use-cases'
tags: ['chatmode','mentor','usecase']
ai_note: 'Generated from chatmodes/mentor.chatmode.md'
summary: 'Use cases for the Mentor chatmode: coaching, feedback, learning plans, and code walkthroughs.'
post_date: '2025-10-20'
---

<!-- markdownlint-disable MD041 -->

What
====
A chatmode designed to act as a technical or career mentor—providing feedback, study plans, code walkthroughs, and interview prep.

When
====
When individuals seek structured mentorship: career advice, skill gap analysis, mock interviews, or regular feedback.

Why
===
To provide consistent, actionable guidance that helps mentees progress and prepares them for real-world engineering challenges.

How
===
Provide profile, goals, and current artifacts (code samples, resumes). Ask for a learning plan, milestone checks, and exercises.

Key Points (EN)
- Personalized learning plans
- Actionable feedback and exercises
- Mock interview and code review workflows

要点 (ZH)
- 个性化学习计划
- 可执行的反馈与练习
- 模拟面试与代码审查流程

Scenarios
---------

1) New-grad career plan
- Prompt: "Create a 6-month learning plan for a new grad backend engineer." 
- Expected output: topics, weekly cadence, and milestones.

2) Code walkthrough
- Prompt: "Walk me through this PR and highlight maintainability issues." 
- Expected output: critique, suggested refactorings, and code examples.

3) Mock interview
- Prompt: "Conduct a 45-minute system design mock interview and score me." 
- Expected output: questions, evaluation rubric, and feedback.

4) Continuous learning check-ins
- Prompt: "Design a monthly check-in template to assess progress against goals." 
- Expected output: checklist, measurements, and follow-ups.

5) Resume tailoring
- Prompt: "Tailor my resume for a backend engineer role at a mid-size SaaS company." 
- Expected output: bullet suggestions, impact framing, and keywords.

Original chatmode: ../../../../chatmodes/mentor.chatmode.md
---
post_title: 'mentor — Use Cases'
post_slug: 'mentor-use-cases'
tags: ['chatmode','mentor','coaching','usecase']
ai_note: 'Generated from chatmodes/mentor.chatmode.md'
summary: 'Use cases for Mentor chatmode: career coaching, code mentoring, learning plans, and feedback cycles for engineers.'
post_date: '2025-10-20'
---

<!-- markdownlint-disable MD041 -->

What
====
A chatmode that acts as a mentor to provide learning paths, code review feedback, career advice, and scaffolded challenges for skill development.

When
====
When an engineer requests structured mentoring: career advice, study plans, feedback on code, or starter projects with progressive difficulty.

Why
===
To provide consistent, actionable mentorship to engineers at various levels and help them progress with measurable outcomes.

How
===
Share goals, current level, time budget, and artifacts (code snippets or CV). Ask for a tailored roadmap, checkpoints, and resources.

Key Points (EN)
- Personalized learning roadmaps
- Actionable feedback and small experiments
- Measurable progress checkpoints

要点 (ZH)
- 个性化学习路线图
- 可执行的反馈与小实验
- 可衡量的进步检查点

Scenarios
---------

1) New grad onboarding plan
- Prompt: "Design a 12-week onboarding learning plan for a new backend engineer with Java experience but unfamiliar with our stack." 
- Expected output: week-by-week topics, exercises, and min-viable deliverables.

2) Career development coaching
- Prompt: "Advise on moving from senior engineer to tech lead in 12 months. Provide milestones and skill focus." 
- Expected output: leadership skills plan, architecture exposure tasks, and mentorship pairings.

3) Code feedback loop
- Prompt: "Provide constructive code review comments for this PR and suggested small refactors." 
- Expected output: prioritized list of improvements, small refactor patches, and test suggestions.

4) Interview prep
- Prompt: "Create a study plan and mock interview questions for system design interviews focusing on scaling and reliability." 
- Expected output: study topics, practice prompts, and grading rubric.

5) Learning-by-doing project
- Prompt: "Suggest a progressive project to learn microservices including CI/CD, monitoring, and testing." 
- Expected output: project milestones, required tech stack suggestions, and acceptance criteria.

Original chatmode: ../../../../chatmodes/mentor.chatmode.md

