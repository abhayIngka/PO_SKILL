# Sprint 01 Plan

**Dates:** 2026-11-17 → TBD (open: confirm sprint end date)
**Sprint goal:** Prove the end-to-end live order status read by allowing a signed-in customer to view a single order's live status and last status-change timestamp from the order system.

## Capacity

| Person | Days available | Notes |
|---|---|---|
| Priya | Confirmed available | Assigned Story 1.1 |

**Team capacity:** 8 points (confirmed by user on 2026-11-17)

## Committed Stories

| Order | Story | Points | Depends on | Owner | Status |
|---|---|---|---|---|---|
| 1 | [1.1 View Single Order Live Status (Tracer Bullet)](../epics.md#story-11-view-single-order-live-status-tracer-bullet) | 3 | none | Priya | In Progress |

**Total committed:** 3 / 8 points

## Stretch (only if committed work finishes)

- None currently Ready (Stories 1.2 and 1.3 require team estimates and DoR check before entering a sprint).

## Risks and Blockers

- **Order-system read latency or timeout (Medium):** Mitigated by AC5 timeout handling (< 2s p95) and verified test environment access (owner: Priya).

## DoR Check

- [x] Every committed story meets the Definition of Ready (Story 1.1 verified 10/10 on 2026-11-17)
- [x] Dependencies are resolved or scheduled earlier in the sprint (Story 1.1 has no story dependencies; order system access confirmed)
- [x] Team agrees the commitment fits capacity (3 / 8 points)
