# 5. Backlog Creation and Prioritization

**Goal:** one ordered list of all stories. The top is ready and most valuable.
**Output:** `backlog.md` (and the same order in the tracker).

## Steps

1. List every story (and bug, spike, tech debt item) once. All start as `Backlog`.
2. Prioritize using three inputs:
   - **Business value:** impact on PRD goals and success metrics.
   - **Risk:** unknowns, technical or integration risk. Do risky work early to learn early.
   - **Dependencies:** a story cannot come before what it depends on.
3. Order: dependencies first, then highest value, with risky items pulled forward.
4. Optional scoring (use only inputs you have; never invent them):
   - **RICE** = (Reach × Impact × Confidence) / Effort
   - **WSJF** = Cost of Delay / Job Size
5. Bucket the list: **Now** (next 1-2 sprints, must be ready), **Next**, **Later** (rough only).
6. The user confirms the order. Record the reason for any non-obvious placement.

## Backlog table

| Rank | Story | Epic | Value | Risk | Depends on | Points | Bucket | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | 1.1 {{title}} | 1 | High | High | none | 3 | Now | Ready |

## Maintain it

- New items (bugs, feedback, change requests) are added and ranked, not squeezed in silently.
- Remove or merge duplicates; close stale items with a reason.
- Re-rank after every release and whenever scope changes.

## Done when

- [ ] Every story appears once with a rank
- [ ] No story ranks above its dependency
- [ ] Now / Next / Later assigned
- [ ] User approved the order

**Next:** [06-refinement.md](06-refinement.md)
