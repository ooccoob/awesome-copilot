---
summary: Prompts localization batching plan (zh-cn)
created: 2025-08-12
source: plan/prompts-translation-inventory.md
batch_size_min: 5
batch_size_max: 15
---
# Prompts Localization Batching Plan

## Strategy

- Order = inventory listing order (stable, deterministic)
- Batch size target: 5 initially (ramp up after process confidence > 95%)
- Selection rule: next N pending (⏳) excluding already localized (✅)
- QA per batch: structural parity, disclaimer, diff line count tolerance = 0 (strict)
- Progress update artifacts: per-batch report + cumulative-progress.md

## Batch Definitions

| Batch | Files (count) | File Names | Status |
|-------|---------------|------------|--------|
| 1 | 5 | voidbeast-gpt41enhanced.chatmode.md; wg-code-alchemist.chatmode.md; wg-code-sentinel.chatmode.md; update-oo-component-documentation.prompt.md; update-specification.prompt.md | ✅ Completed |
| 2 | 5 | ai-prompt-engineering-safety-review.prompt.md; architecture-blueprint-generator.prompt.md; aspnet-minimal-api-openapi.prompt.md; az-cost-optimize.prompt.md; azure-resource-health-diagnose.prompt.md | ⏳ Pending |

## Next Actions

- Translate Batch 2
- Generate batch 2 QA report
- Update cumulative progress
- Assess if batch size can increase (criteria: 2 consecutive zero-issue QA batches)

## Criteria for Increasing Batch Size

- No structural mismatches in last 2 batches
- Translation accuracy spot-check pass (>98% segments)
- Time per file under threshold (TBD)

