# 8. Development Execution

**Goal:** the team builds; the PO keeps status true, answers questions fast, and unblocks.

## Status flow

`Backlog → Ready → In Progress → In Review → Built → Testing → Done`

| Status | Moved by | When |
|---|---|---|
| Backlog | PO | Captured, not ready |
| Ready | PO | DoR met and confirmed |
| In Progress | Developer | Work started (sprint-selected) |
| In Review | Developer | PR open |
| Built | Developer | Review passed, merged, in test environment |
| Testing | QA / PO | Verifying acceptance criteria |
| Done | **PO only** | AC verified and DoD met ([10-validation.md](10-validation.md)) |

Side states: **Blocked** (blocker and owner named), **Dropped** (reason named).

## PO responsibilities during the sprint

1. Be available to answer requirement questions the same day. Record answers in the story.
2. Check status daily (board or tracker); chase blocked items.
3. Handle scope changes: any new request is a new backlog item unless the user explicitly swaps it for committed work. Record the decision.
4. Verify built stories early (don't wait for the last day); fail fast on missed criteria by moving back to `In Progress` with the failing criterion named.
5. Never set `Done` from the developer's word alone.

## Done when (for the sprint)

- [ ] Every committed story is Done or consciously carried over with a reason
- [ ] Carry-overs returned to the backlog and re-ranked

**Next:** [09-tracker.md](09-tracker.md) (continuous) and [10-validation.md](10-validation.md)
