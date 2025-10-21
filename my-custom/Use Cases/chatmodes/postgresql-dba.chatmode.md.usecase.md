---
post_title: 'postgresql-dba — Use Cases'
post_slug: 'postgresql-dba-use-cases'
tags: ['chatmode','postgresql','dba','usecase']
ai_note: 'Generated from chatmodes/postgresql-dba.chatmode.md'
summary: 'Use cases for PostgreSQL DBA chatmode: tuning, backups, replication, schema changes, and performance troubleshooting.'
post_date: '2025-10-20'
---

<!-- markdownlint-disable MD041 -->

What
====
A specialized chatmode for PostgreSQL DBAs to receive diagnostics, tuning recommendations, safe migration steps, and backup/replication guidance.

When
====
When you need to plan schema migrations, analyze slow queries, configure replication, or design backup/restore strategies.

Why
===
To minimize downtime, reduce risk during migrations, and ensure PostgreSQL instances are configured for their workload profiles.

How
===
Provide pg_stat_activity, EXPLAIN ANALYZE output, configuration snippets, or workload descriptions. Ask for concrete tuned settings, migration checklist, and query rewrites.

Key Points (EN)
- Safe schema migration patterns
- Index strategies and query tuning
- Replication and backup best practices

要点 (ZH)
- 安全的模式迁移模式
- 索引策略与查询调优
- 复制和备份最佳实践

Scenarios
---------

1) Slow query optimization
- Prompt: "Optimize this slow query: EXPLAIN ANALYZE attached." 
- Expected output: rewritten query suggestions, index recommendations, and expected cost improvements.

2) Zero-downtime schema migration
- Prompt: "Plan a zero-downtime column rename and backfill for a 1TB table." 
- Expected output: phased migration steps, triggers/dual-write plan, and backfill performance tuning.

3) Configure streaming replication
- Prompt: "Set up streaming replication between primary and hot standby across regions with minimal lag." 
- Expected output: configuration snippets, network recommendations, and monitoring checks.

4) Disaster recovery plan
- Prompt: "Design a DR runbook for regional failure including failover testing steps." 
- Expected output: RTO/RPO guidance, failover steps, and validation tests.

5) Backup verification
- Prompt: "Provide steps to verify backups and restore a subset of rows from a point-in-time recovery." 
- Expected output: recovery commands, verification steps, and sample restore queries.

Original chatmode: ../../../../chatmodes/postgresql-dba.chatmode.md

