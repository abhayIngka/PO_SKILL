# 9. Tracker Integration (Azure DevOps / Jira)

**Goal:** the tracker always matches reality, and is the source for status, dependencies, and reporting.
**Rule:** push to a tracker only after an explicit yes. A yes approves only what was shown.

## Mapping

| This workflow | Azure DevOps | Jira |
|---|---|---|
| Initiative / PRD | Feature or Epic | Epic or Initiative |
| Epic | Epic | Epic |
| Story | User Story (or PBI) | Story |
| Bug | Bug | Bug |
| Spike | Task / Spike | Spike / Task |
| Story points | Story Points | Story Points |
| Acceptance criteria | Acceptance Criteria field | Description section or AC field |
| Sprint | Iteration | Sprint |
| Dependency | Predecessor / Successor link | "is blocked by" / "blocks" link |
| Epic-to-story | Parent / Child link | Epic Link / Parent |

## Status mapping

| Story status | Azure DevOps state | Jira status |
|---|---|---|
| Backlog | New | Backlog |
| Ready | Approved / Ready | Ready for Dev |
| In Progress | Active | In Progress |
| In Review | Active (tag: in-review) | In Review |
| Built | Resolved | Built / Ready for QA |
| Testing | Testing (or Resolved + tag) | In Testing |
| Done | Closed | Done |

Adjust to the project's actual workflow; confirm the mapping once and record it.

## Updates

1. **Create:** epics and stories with parent links, points, priority, AC, and the PRD requirement ids. Store the tracker id back in `epics.md` (`Tracker ID`).
2. **Status:** update on each transition. Add a comment when a story goes backwards or is blocked.
3. **Dependencies:** create links for every `Depends on`. Review blocked chains weekly.
4. **Sprint:** keep sprint membership in sync with the sprint plan.
5. **Drift check:** compare the tracker with `epics.md` and `backlog.md`; fix whichever is wrong and record the change.

## Reporting

- Sprint: committed vs done points, burndown, carry-over.
- Epic: stories done / total, blocked items, remaining dependencies.
- Release: scope done vs planned, open defects.
- Feed these into [12-stakeholder-updates.md](12-stakeholder-updates.md).

If no tracker tool is available, say so and give the user the exact field values to enter instead of guessing.
