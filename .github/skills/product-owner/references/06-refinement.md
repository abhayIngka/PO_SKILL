# 6. Backlog Refinement (Grooming)

**Goal:** keep the next 1-2 sprints of stories Ready. Run it regularly (e.g. once per sprint) with the team.

## Steps

1. **Pick the scope:** all *Now* and *Next* stories that fail the DoR.
2. **Clarify requirements:** walk each story with the team. Capture questions and answers in the story. Anything unanswered becomes an open question with an owner.
3. **Update estimates:** team re-estimates stories whose understanding changed. Split any story over the max size.
4. **Review acceptance criteria:** are they testable, specific, covering failure paths? Fix weak wording.
5. **Enforce the DoR:** run the checklist in [definitions.md](definitions.md). Stories that pass and are confirmed by the team move to `Ready`.
6. **Housekeeping:** re-rank, merge duplicates, close stale items, add new items from feedback and bugs.
7. Record decisions and update the tracker ([09-tracker.md](09-tracker.md)).

## Output

| Story | Result | Action |
|---|---|---|
| 1.2 | Ready | none |
| 1.3 | Not ready | needs design, owner: UX, by {{date}} |

## Rules

- Only `Ready` stories are offered to sprint planning.
- A change after Ready (scope, AC, dependency) sends the story back to `Backlog` until re-checked.
- Starting before ready is an exception: name what is missing, get the user's agreement, record the decision.

## Done when

- [ ] Enough Ready stories for the next sprint (aim for 1.5× capacity)
- [ ] Estimates current; AC reviewed
- [ ] Open questions have owners and dates

**Next:** [07-sprint-planning.md](07-sprint-planning.md)
