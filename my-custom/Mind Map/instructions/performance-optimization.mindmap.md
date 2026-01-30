## What/When/Why/How
- What: Cross-stack performance optimization playbook (frontend, backend, DB, cloud)
- When: Slow UX, high latency/cost, timeouts, CPU/memory spikes, QoS/SLA risks
- Why: Improve UX and business KPIs while reducing infra cost and risk
- How: Measure → find bottlenecks → apply targeted fixes → verify → automate regression checks

## Key Points (Essentials)
- Measure-first: profiling, tracing, budgets, CWV/Lighthouse/APM, SLO/SLA
- Hot paths: reduce algorithmic complexity, batch/stream, avoid sync/blocking I/O
- Caching: choose scope (in-proc/Redis/CDN), TTL/keys/invalidations, stampede control
- Frontend: bundle split, lazy load, image/font optimize, avoid re-renders, web workers
- Backend: async I/O, pools, idempotency, backpressure, circuit breaker, retries with jitter
- Database: star schema, proper indexes, avoid N+1/SELECT *, analyze plans, partitioning
- Network: compress (Brotli/gzip), pagination, minimal payloads, HTTP/2/3/gRPC
- Observability: structured logs, metrics, traces, slow-log, alerts; only log once per error
- Security & cost: cheap crypto where safe, protect from abuse (rate limit), monitor cost as KPI

## Compact Map
- Inputs: prod metrics, traces, slow query log, flame graphs, heap/GC stats, CWV
- Decisions: fix vs. redesign; cache vs. compute; batch vs. stream; scale up vs. out
- Tactics:
  - FE: code-split, prefetch/preload, virtualize lists, debounce/throttle, CSS animations
  - BE: async, worker/threads, queue, bulk ops, lock minimization, data locality
  - DB: covering indexes, parameterized queries, read replicas, archiving, sharding
  - Cloud: autoscale, warm paths, quotas, timeouts, budgets; pick right instance/storage class
- Verification: A/B or canary, perf tests (k6/Gatling/Locust), budgets in CI, alarms

## Example Questions (dev-focused)
1) What are our current perf budgets (TTI/LCP/API p95) and which fail most?
2) Which endpoints dominate tail latency (p95/p99) per trace spans last 24h?
3) Can we merge N round-trips into a single bulk call or server-side join?
4) Which queries lack effective indexes per EXPLAIN/pg_stat_statements?
5) Where do we block the main thread (FE) or event loop (BE) today?
6) What cache keys/TTLs and invalidation rules eliminate recomputation safely?
7) Can we paginate/stream large responses instead of building them in memory?
8) Which bundles exceed budget and how to split/treeshake to < desired KB?
9) Are retries exponential-with-jitter and capped to prevent storms?
10) What auto-scaling thresholds and alarms prevent saturation/overprovision?
11) How do we prove no regression (perf tests in CI + SLO alerts)?

Source: d:\mycode\awesome-copilot\instructions\performance-optimization.instructions.md | Generated: 2025-10-17
