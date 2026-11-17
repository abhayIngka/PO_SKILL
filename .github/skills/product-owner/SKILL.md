---
name: product-owner
description: 'End-to-end Product Owner workflow: write a PRD, create epics, break epics into stories, define acceptance criteria / DoR / estimates, prioritize and refine the backlog, plan sprints, track status in Azure DevOps or Jira, validate against DoD, prepare and communicate releases, and review post-release. Use when asked to "write a PRD", "create an epic", "break into stories", "prioritize the backlog", "refine", "plan the sprint", "update the tracker", "is this done", "release notes", "stakeholder update", or "post-release review".'
---

# Product Owner Skill

Turns a business need into shipped, accepted, measured work.

## The flow

**PRD → Epic → Stories → Refinement → Prioritization → Sprint Planning → Development → Tracking → Validation → Release → Stakeholder Updates → Production → Post-Release Review**

## Steps

| # | Step | Do this | Output | Read |
|---|---|---|---|---|
| 1 | PRD | Capture business goals, user requirements, scope, success metrics | PRD | [01-prd.md](references/01-prd.md) |
| 2 | Epic | Define each high-level feature or initiative | Epics | [02-epic.md](references/02-epic.md) |
| 3 | Story breakdown | Split epics into stories; map dependencies | Stories, dependency map | [03-story-breakdown.md](references/03-story-breakdown.md) |
| 4 | Story definition | Acceptance criteria, DoR check, estimate | Defined stories | [04-story-definition.md](references/04-story-definition.md) |
| 5 | Backlog | Prioritize by value, risk, dependencies; maintain | Ordered backlog | [05-backlog.md](references/05-backlog.md) |
| 6 | Refinement | Clarify, re-estimate, review AC, enforce DoR | Ready stories | [06-refinement.md](references/06-refinement.md) |
| 7 | Sprint planning | Select stories, set goal, commit to capacity | Sprint plan | [07-sprint-planning.md](references/07-sprint-planning.md) |
| 8 | Development | Move stories through the status flow | Built stories | [08-development.md](references/08-development.md) |
| 9 | Tracker | Keep Azure DevOps / Jira true; dependencies; reports | Updated tracker | [09-tracker.md](references/09-tracker.md) |
| 10 | Validation | Verify AC and DoD; get stakeholder acceptance | Done stories / closed epics | [10-validation.md](references/10-validation.md) |
| 11 | Release prep | Release notes, deployment plan, go-live readiness | Release notes, go/no-go | [11-release-prep.md](references/11-release-prep.md) |
| 12 | Stakeholder updates | Status, progress, risks, milestones | Updates | [12-stakeholder-updates.md](references/12-stakeholder-updates.md) |
| 13 | Production release | Deploy, monitor | Released | [13-production-release.md](references/13-production-release.md) |
| 14 | Post-release | Metrics, issues, feedback, backlog updates | Review, new backlog items | [14-post-release.md](references/14-post-release.md) |

Shared definitions: [definitions.md](references/definitions.md).

## Story status flow

`Backlog → Ready → In Progress → In Review → Built → Testing → Done`

Details, owners, and tracker mapping: [definitions.md](references/definitions.md) and [09-tracker.md](references/09-tracker.md).

## Templates (`assets/`)

| Template | Used in step |
|---|---|
| [prd-template.md](assets/prd-template.md) | 1 |
| [epic-template.md](assets/epic-template.md) (epics + stories + epic DoD) | 2, 3, 4 |
| [sprint-plan-template.md](assets/sprint-plan-template.md) | 7 |
| [release-notes-template.md](assets/release-notes-template.md) | 11 |
| [stakeholder-update-template.md](assets/stakeholder-update-template.md) | 12 |
| [post-release-review-template.md](assets/post-release-review-template.md) | 14 |

## Rules

1. Read the step's reference before acting; use the template.
2. The user decides scope, priority, and sign-off. Propose with a reason, record the decision.
3. **Gate In:** only stories that meet the Definition of Ready enter a sprint.
4. **Gate Out:** only work that meets the Definition of Done, with evidence, is marked Done.
5. Every story traces to an epic and a PRD requirement (FR/NFR id).
6. Never guess estimates, dates, or views. Ask or list as open questions.
7. Never push to a tracker or production without an explicit yes.

## Where files live

```
<product>/
  prd.md
  epics.md                     # from epic-template.md: all epics + stories
  backlog.md                   # ordered backlog
  sprints/sprint-<nn>.md
  releases/release-<version>-notes.md
  reports/
    stakeholder-update-<date>.md
    post-release-<version>.md
```
