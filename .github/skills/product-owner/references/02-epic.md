# 2. Epic Creation

**Goal:** group the PRD requirements into high-level features or initiatives, each delivering a user outcome.
**Template:** `assets/epic-template.md` → save as `epics.md`.
**Input:** the approved PRD.

## Steps

1. Fill the template's **Requirements Inventory** from the PRD (FR, NFR, additional, UX).
2. Group requirements into epics. Each epic:
   - delivers one clear user or business outcome (not a technical layer),
   - has a title and a goal in one or two sentences,
   - lists the FR/NFR ids it covers.
3. Build the **FR Coverage Map**: every FR maps to exactly one epic. An uncovered FR is a gap.
4. Add each epic's **Definition of Done** (standard lines from the template plus epic-specific lines, e.g. "deployed to production and verified").
5. Note epic dependencies and order epics so the one that proves the riskiest path comes first.
6. Show the epic list. The user confirms scope and order.

## Done when

- [ ] Every PRD requirement is covered by an epic (or parked with a reason)
- [ ] Each epic has a goal, covered requirements, and a DoD
- [ ] Epic dependencies are listed
- [ ] User approved the epic list

**Next:** [03-story-breakdown.md](03-story-breakdown.md)
