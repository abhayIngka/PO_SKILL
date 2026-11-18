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

## Push rules (Jira and Confluence)

These rules apply to every push, create, or update in Jira (epics, stories, tasks, bugs, sub-tasks) and Confluence (pages and child pages).

1. **Explicit yes:** push only after the user asks for that exact item. A yes approves only what was shown.
2. **Labels:** never add labels on your own. Add a label only when the user explicitly asks for it.
3. **Provenance label `ai_assisted` is mandatory:** every item or page you create or update must carry the label `ai_assisted`, even if the user did not ask. It is the only label you may add unprompted. The user may remove it later; you must not remove it.
4. **Keep existing labels:** when updating, preserve the current labels. Never replace the full label set.
5. **Check for duplicates first:** before creating, search the space or project by title, including trashed items. If a match exists, ask the user which to update. Do not create a second copy silently.
6. **Mandatory push procedure (no exceptions):**
   1. Load the product-owner skill before pushing.
   2. Create or update the item.
   3. Add the `ai_assisted` label in the same push, plus any labels the user asked for. A push without the label is a failed push.
   4. Read the labels back. If `ai_assisted` is missing, add it and read again.
   5. Report the item ID or key and the labels confirmed. Do not report the push as done until step 4 passes.

### Confluence API calls

- Create: `POST {CONFLUENCE_URL}/rest/api/content` with `type`, `title`, `space.key`, and `body.storage`.
- Add label: `POST {CONFLUENCE_URL}/rest/api/content/{id}/label` with body `[{"prefix":"global","name":"ai_assisted"}]`.
- Verify: `GET {CONFLUENCE_URL}/rest/api/content/{id}/label` and confirm `ai_assisted` is in `results`.

## Reporting

- Sprint: committed vs done points, burndown, carry-over.
- Epic: stories done / total, blocked items, remaining dependencies.
- Release: scope done vs planned, open defects.
- Feed these into [12-stakeholder-updates.md](12-stakeholder-updates.md).

If no tracker tool is available, say so and give the user the exact field values to enter instead of guessing.
