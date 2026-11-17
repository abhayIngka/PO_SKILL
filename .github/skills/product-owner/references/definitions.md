# Key Definitions

## Acceptance Criteria (AC)

Conditions that must be met for **one story** to be accepted. Written per story, in Given / When / Then form.

- Testable: a stranger can check pass or fail.
- Specific: no "fast", "easy", "works correctly". Use numbers.
- Cover the happy path **and** at least one failure or empty state.
- Keep to 7 or fewer per story. More means the story is too big.

## Definition of Ready (DoR)

Gate **in**. The story is clear, estimated, prioritized, and testable **before** it enters a sprint.

- [ ] Story statement written (As a / I want / So that)
- [ ] Linked to an epic and a PRD requirement (FR/NFR id)
- [ ] Acceptance criteria written and agreed
- [ ] Estimated by the team, within the max size (default 8 points)
- [ ] Prioritized in the backlog
- [ ] Dependencies identified and none blocking
- [ ] Design / UX available (if user-facing)
- [ ] Access, test data, environments available
- [ ] No open `Unknown` or placeholder (TBD, TODO)
- [ ] Team confirms they can start without coming back to the PO

## Definition of Done (DoD)

Gate **out**. Development complete, code reviewed, tested, documented, and accepted.

**Story**

- [ ] All acceptance criteria verified (evidence attached)
- [ ] Code reviewed and merged
- [ ] Automated tests pass; no known regressions
- [ ] Documentation updated
- [ ] Applicable NFRs met
- [ ] No open critical or high-severity defects
- [ ] Product Owner accepted

**Epic** (copied into every epic from `assets/epic-template.md`)

- [ ] All stories complete and accepted
- [ ] Every acceptance criterion verified
- [ ] Automated tests pass; no known regressions
- [ ] Code reviewed and merged
- [ ] Documentation updated
- [ ] Applicable NFRs met
- [ ] Product owner accepted the epic (demo or sign-off)
- [ ] No open critical or high-severity defects
- [ ] Epic-specific lines (e.g. deployed to production and verified)

**Evidence rule:** a tick without proof is a claim. Write the proof on the line: a PR, CI run, test report, screenshot, or file path.
Example: `- [x] Code reviewed and merged — evidence: PR #41 merged to main`

## Story status flow

`Backlog → Ready → In Progress → In Review → Built → Testing → Done`

| Status | Meaning | Moved by | Gate |
|---|---|---|---|
| Backlog | Captured, not yet ready | PO | n/a |
| Ready | Meets DoR, can be pulled into a sprint | PO | DoR |
| In Progress | Developer is building it | Developer | Selected in sprint |
| In Review | Code review / PR open | Developer | Code complete |
| Built | Review passed, merged, deployed to test env | Developer | Review done |
| Testing | QA / PO verifying acceptance criteria | QA / PO | Build in test env |
| Done | AC verified, DoD met, PO accepted | PO only | DoD |

- Backwards moves are allowed (Testing → In Progress when a criterion fails). Record why.
- Side states: **Blocked** (name the blocker and owner), **Dropped** (name the reason).

## Estimation

- Story points, set by the **team**. The PO never estimates for them.
- Stories larger than the max (default 8) are split before they are Ready.
- Use the same scale throughout (e.g. 1, 2, 3, 5, 8).

## Priority

Order by **business value**, **risk**, and **dependencies**. See [05-backlog.md](05-backlog.md).
