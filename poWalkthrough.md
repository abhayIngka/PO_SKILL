# Product Owner Skill — Complete Guide (14 Steps, Tracker & Templates)

This single document explains everything in the Product Owner (`PO_SKILL`) repository in plain language:
1. **All 14 steps** — what each step does, what input it takes, what it produces, and its completion criteria.
2. **How the tracker & story statuses are maintained** — with exact file paths and line numbers across both the skill rules and the live `order-tracking/` example.
3. **How the templates were created** — what frameworks, industry standards, and reference files each template in `.github/skills/product-owner/assets/` is built from.

---

## Part 1: All 14 Steps Explained (Input, Action, Output)

The overall flow is defined in [product-owner.agent.md](./.github/agents/product-owner.agent.md) (lines 12–30) and [SKILL.md](./.github/skills/product-owner/SKILL.md) (lines 10–33):

`PRD → Epic → Stories → Story Definition → Backlog → Refinement → Sprint Planning → Development → Tracker → Validation → Release Prep → Stakeholder Updates → Production → Post-Release`

---

### Step 1: PRD Writing
- **Reference File:** [01-prd.md](./.github/skills/product-owner/references/01-prd.md) (lines 1–31)
- **Template Used:** [prd-template.md](./.github/skills/product-owner/assets/prd-template.md)
- **Input:** Raw idea, brief, notes, transcript, or stakeholder request (e.g., [idea-2026-11-17.md](./order-tracking/sources/idea-2026-11-17.md)).
- **What It Does Exactly:**
  1. Saves the raw input untouched in `sources/` (line 9).
  2. Fills out Business Goals (problem, goal, why now), User Requirements with testable IDs (`FR1`, `FR2`, `NFR1` with measurable numbers), Scope (explicitly naming what is *In Scope* and *Out of Scope* with reasons), and Success Metrics (baseline, target, how measured, when) (lines 10–15).
  3. Lists assumptions, risks, dependencies, and open questions without guessing (line 16).
  4. Shows the draft to the user and logs their decisions in the `Decisions` section (line 17).
- **Output:** `<product>/prd.md` (e.g., [order-tracking/prd.md](./order-tracking/prd.md)).

---

### Step 2: Epic Creation
- **Reference File:** [02-epic.md](./.github/skills/product-owner/references/02-epic.md) (lines 1–30)
- **Template Used:** [epic-template.md](./.github/skills/product-owner/assets/epic-template.md) (lines 1–59)
- **Input:** The approved `prd.md`.
- **What It Does Exactly:**
  1. Copies all Functional (`FR`), Non-Functional (`NFR`), Additional (`AR`), and UX requirements from the PRD into the `Requirements Inventory` section (line 9).
  2. Groups requirements into outcome-based Epics (each delivering a user/business outcome, not a technical layer like "database" or "API") (lines 10–13).
  3. Builds the **FR Coverage Map** ensuring every PRD requirement maps to an epic with zero gaps (line 14).
  4. Adds an Epic **Definition of Done (DoD)** checklist and orders epics so the riskiest path is proven first (lines 15–17).
- **Output:** `<product>/epics.md` initialized with epics, coverage map, and epic DoD (e.g., [order-tracking/epics.md](./order-tracking/epics.md), lines 1–75).

---

### Step 3: Epic → Story Breakdown
- **Reference File:** [03-story-breakdown.md](./.github/skills/product-owner/references/03-story-breakdown.md) (lines 1–31)
- **Template Used:** Story section inside [epic-template.md](./.github/skills/product-owner/assets/epic-template.md) (lines 60–86)
- **Input:** Approved epics inside `epics.md`.
- **What It Does Exactly:**
  1. Splits each epic **vertically** into end-to-end user stories (`Story N.M: title`) using the format: *As a {user}, I want {capability}, So that {value}* (lines 9–12).
  2. Ensures each story fits in one sprint and is independently testable (line 13).
  3. Maps `Covers:` to specific `FR`/`NFR` IDs from the PRD so every epic requirement is covered (line 14).
  4. Maps `Depends on:` between stories and external systems, checking for zero dependency cycles and placing the "tracer bullet" (riskiest path) first (lines 15–17).
- **Output:** Stories added into `<product>/epics.md` (e.g., Stories 1.1, 1.2, and 1.3 in [order-tracking/epics.md](./order-tracking/epics.md), lines 77–228).

---

### Step 4: Story Definition
- **Reference File:** [04-story-definition.md](./.github/skills/product-owner/references/04-story-definition.md) (lines 1–43) & [definitions.md](./.github/skills/product-owner/references/definitions.md) (lines 3–30)
- **Template Used:** Story Acceptance Criteria block inside [epic-template.md](./.github/skills/product-owner/assets/epic-template.md) (lines 74–86)
- **Input:** Broken-down stories in `epics.md`.
- **What It Does Exactly:**
  1. Writes **Given / When / Then** Acceptance Criteria (AC) for each story — covering the happy path plus at least one failure, refusal, or empty state, using concrete numbers (max 7 ACs per story) (lines 10–21).
  2. Runs the 10-point **Definition of Ready (DoR)** checklist from [definitions.md](./.github/skills/product-owner/references/definitions.md) (lines 12–28) and flags any gaps with an owner (line 25).
  3. Requests **story point estimates from the team** (the PO never guesses or estimates on behalf of developers; stories > 8 points must be split back in Step 3) (lines 29–32).
- **Output:** Fully defined stories with ACs, DoR checklists, and team estimates in `<product>/epics.md` (e.g., Story 1.1 AC & DoR in [order-tracking/epics.md](./order-tracking/epics.md), lines 91–137).

---

### Step 5: Backlog Creation and Prioritization
- **Reference File:** [05-backlog.md](./.github/skills/product-owner/references/05-backlog.md) (lines 1–41)
- **Template Used:** Backlog table format defined directly in [05-backlog.md](./.github/skills/product-owner/references/05-backlog.md) (lines 22–26)
- **Input:** Defined stories from `epics.md` (plus any bugs, spikes, or tech debt items).
- **What It Does Exactly:**
  1. Lists every item once in a single ranked table, starting in `Backlog` status (line 8).
  2. Orders stories by **Dependencies first** (a story cannot rank above its prerequisite), then **Risk** (pulling high-risk / high-learning items early), then **Business Value** (impact on PRD metrics) (lines 9–13). Supports optional RICE or WSJF scoring if real numbers exist (lines 14–16).
  3. Assigns each item to a bucket: **Now** (next 1–2 sprints, must be Ready), **Next**, or **Later** (line 17).
- **Output:** `<product>/backlog.md` (e.g., [order-tracking/backlog.md](./order-tracking/backlog.md), lines 1–24).

---

### Step 6: Backlog Refinement (Grooming)
- **Reference File:** [06-refinement.md](./.github/skills/product-owner/references/06-refinement.md) (lines 1–38)
- **Template Used:** Refinement output table in [06-refinement.md](./.github/skills/product-owner/references/06-refinement.md) (lines 18–23)
- **Input:** `backlog.md` and `epics.md` (specifically *Now* and *Next* stories that haven't passed DoR).
- **What It Does Exactly:**
  1. Walks through upcoming stories with the team to clarify requirements and record answers directly on the story (lines 7–8).
  2. Updates story point estimates with the team and splits any story that grew above 8 points (line 9).
  3. Reviews and tightens Acceptance Criteria (line 10).
  4. Enforces the **Gate In (Definition of Ready)**: stories that pass all 10 DoR checks and are confirmed by the team move from `Backlog → Ready` (line 11).
- **Output:** Stories promoted to `Ready` status in `epics.md`, `backlog.md`, and the external tracker (aiming for 1.5× next sprint's capacity).

---

### Step 7: Sprint Planning
- **Reference File:** [07-sprint-planning.md](./.github/skills/product-owner/references/07-sprint-planning.md) (lines 1–28)
- **Template Used:** [sprint-plan-template.md](./.github/skills/product-owner/assets/sprint-plan-template.md) (lines 1–36)
- **Input:** Ordered `backlog.md` (only stories in `Ready` status), team availability, and historical velocity.
- **What It Does Exactly:**
  1. Records team capacity in points based on availability and velocity (asked from the team, never assumed) (line 8).
  2. Proposes a one-sentence **Sprint Goal** tied to the top backlog outcome (line 9).
  3. Selects **only `Ready` stories** from the top of the backlog respecting dependency order, never exceeding capacity (lines 10–12).
  4. Gets team commitment, lists stretch stories separately, logs risks/blockers, and transitions committed work as the sprint starts (lines 13–15).
- **Output:** `<product>/sprints/sprint-<nn>.md` (e.g., [order-tracking/sprints/sprint-01.md](./order-tracking/sprints/sprint-01.md)).

---

### Step 8: Development Execution
- **Reference File:** [08-development.md](./.github/skills/product-owner/references/08-development.md) (lines 1–37)
- **Input:** Committed sprint stories (`sprints/sprint-<nn>.md` and `epics.md`).
- **What It Does Exactly:**
  1. Moves stories through the active build statuses: `Ready → In Progress → In Review → Built → Testing` (lines 7–18).
  2. Tracks side states (`Blocked` with blocker + owner, or `Dropped` with reason) (line 20).
  3. Defines PO sprint duties: answer requirement questions same-day, log answers in the story, protect sprint scope (new requests go to backlog unless explicitly swapped), and test `Built` stories early rather than waiting for the last day of the sprint (lines 24–28).
  4. Fails stories back to `In Progress` immediately if an AC fails during early verification (line 27).
- **Output:** Stories progressed to `Built` / `Testing`, with synchronized statuses in `epics.md`, `backlog.md`, `sprint-<nn>.md`, and the external tracker.

---

### Step 9: Tracker Integration (Azure DevOps / Jira)
- **Reference File:** [09-tracker.md](./.github/skills/product-owner/references/09-tracker.md) (lines 1–49)
- **Input:** Local markdown artifacts (`prd.md`, `epics.md`, `backlog.md`, `sprints/sprint-<nn>.md`) and explicit user permission to push.
- **What It Does Exactly:**
  1. Maps local work items and statuses to **Azure DevOps** or **Jira** (lines 7–31).
  2. Creates/updates Epics and Stories in the external tool with parent-child links, story points, AC, and PRD requirement IDs, and writes the returned `Tracker ID` back into `epics.md` (line 35).
  3. Keeps status transitions, dependency links (`Predecessor/Successor` or `blocks/is blocked by`), and sprint membership synced (lines 36–38).
  4. Runs a **Drift Check** between the tracker and local files (`epics.md` / `backlog.md`) so they never contradict each other (line 39).
- **Output:** Updated Azure DevOps / Jira board, populated `Tracker ID` fields in `epics.md`, and sprint/epic/release metrics for reporting.

---

### Step 10: Validation and Closure
- **Reference File:** [10-validation.md](./.github/skills/product-owner/references/10-validation.md) (lines 1–46) & [definitions.md](./.github/skills/product-owner/references/definitions.md) (lines 30–59)
- **Input:** Stories in `Testing` status and completed Epics.
- **What It Does Exactly:**
  1. **Story Acceptance:** Verifies every Given/When/Then AC via a runnable check (demo, test run, query), checks the 7-point Story DoD, attaches concrete **evidence** (PR number, CI run, test report), and marks the story `Done` (only the PO can move a story to `Done`) (lines 8–12). If any AC fails, moves the story back to `In Progress` naming the failed criterion (line 11).
  2. **Epic Closure:** Runs the Epic DoD checklist in `epics.md`, attaches proof to every checkbox (`- [x] ... — evidence: PR #41`), obtains stakeholder demo/sign-off, logs `Decision: accepted`, and marks the epic `Done` (lines 16–28).
- **Output:** Accepted `Done` stories and closed epics in `epics.md`, `backlog.md`, and the tracker, with evidence recorded inline.

---

### Step 11: Release Preparation
- **Reference File:** [11-release-prep.md](./.github/skills/product-owner/references/11-release-prep.md) (lines 1–29)
- **Template Used:** [release-notes-template.md](./.github/skills/product-owner/assets/release-notes-template.md) (lines 1–46)
- **Input:** Accepted (`Done`) stories/epics, deferred stories, known defects, and ops/deployment details.
- **What It Does Exactly:**
  1. Defines release scope: lists what is shipping (`Done`) and what was planned but deferred (with reasons) (line 8).
  2. Drafts user-facing release notes (plain language, no internal jargon) including fixes, known issues, and workarounds (line 9).
  3. Plans deployment steps, owners, timing, feature flags, migrations, and a tested rollback plan (line 10).
  4. Runs the 8-point **Go-Live Readiness** checklist and records the formal **Go / No-Go** decision (lines 11–16).
- **Output:** `<product>/releases/release-<version>-notes.md` and a recorded Go/No-Go decision.

---

### Step 12: Release Stakeholder Updates
- **Reference File:** [12-stakeholder-updates.md](./.github/skills/product-owner/references/12-stakeholder-updates.md) (lines 1–33)
- **Template Used:** [stakeholder-update-template.md](./.github/skills/product-owner/assets/stakeholder-update-template.md) (lines 1–39)
- **Input:** Tracker metrics, sprint/epic progress, milestone dates, and active risks.
- **What It Does Exactly:**
  1. Leads with overall health (`🟢 On track / 🟡 At risk / 🔴 Off track`) and any decisions needed from stakeholders (lines 8–14, 24).
  2. Reports exact story/epic completion counts and sprint points pulled from the tracker (never from memory) (line 25).
  3. Explicitly calls out what slipped or did *not* ship alongside what did, plus risks with owners and mitigations (lines 26–27).
- **Output:** `<product>/reports/stakeholder-update-<date>.md`.

---

### Step 13: Production Release
- **Reference File:** [13-production-release.md](./.github/skills/product-owner/references/13-production-release.md) (lines 1–28)
- **Input:** Approved Go decision from Step 11, deployment plan, and explicit user approval to release.
- **What It Does Exactly:**
  1. Confirms the Go decision still holds (no last-minute critical defects) (line 8).
  2. Executes deployment with the delivery/ops team and smoke-tests key user journeys and feature flags in production (lines 9–10).
  3. Monitors errors, latency, business metrics, and support channels during the agreed window (e.g., 24–72 hours), triggering fix-forward or rollback if needed (lines 11–12).
  4. Updates released stories/epics with version and release date, ticks the production DoD evidence line, publishes release notes, and sends the stakeholder "released" update (lines 13–16).
- **Output:** Verified production release, updated tracker/epic DoD evidence, and published release notes.

---

### Step 14: Post-Release Tracking
- **Reference File:** [14-post-release.md](./.github/skills/product-owner/references/14-post-release.md) (lines 1–29)
- **Template Used:** [post-release-review-template.md](./.github/skills/product-owner/assets/post-release-review-template.md) (lines 1–39)
- **Input:** Live production metrics, PRD success targets (from Step 1), post-launch defects/incidents, and user/support feedback.
- **What It Does Exactly:**
  1. Compares actual post-launch metrics against the PRD baseline and target, marking each `Met`, `Missed`, or `Too early` (with a scheduled follow-up date) (line 8).
  2. Logs post-release defects/incidents with severity and tracker IDs (line 9).
  3. Captures user, support, and stakeholder feedback and turns actionable items into newly ranked backlog items (returns to Step 5) or a new PRD (Step 1) (lines 10–15).
- **Output:** `<product>/reports/post-release-<version>.md` and an updated `backlog.md`.

---

## Part 2: How the Tracker & Story Status Are Maintained (Files & Exact Lines)

This workflow maintains state using a **dual-layer tracking model**:
1. **Local Markdown Tracker (Always active in Git):** Stored across `epics.md`, `backlog.md`, and `sprints/sprint-<nn>.md`.
2. **External Tool Tracker (Azure DevOps / Jira):** Synced via Step 9 ([09-tracker.md](./.github/skills/product-owner/references/09-tracker.md)) and linked back to the markdown files via `Tracker ID`.

### 1. The 7-Stage Story Status Flow & Ownership Rules
Defined in [definitions.md](./.github/skills/product-owner/references/definitions.md) (lines 61–77) and [08-development.md](./.github/skills/product-owner/references/08-development.md) (lines 7–20):

| Status | Meaning | Who Can Move It | Gate Required |
|---|---|---|---|
| `Backlog` | Captured, not yet ready | Product Owner | None |
| `Ready` | Clear, estimated, testable | Product Owner | **Gate In:** Definition of Ready (DoR) — 10 checks in [definitions.md](./.github/skills/product-owner/references/definitions.md) (lines 12–28) |
| `In Progress` | Developer is actively building | Developer | Selected in Sprint Planning |
| `In Review` | Code complete, PR open | Developer | PR opened |
| `Built` | Reviewed, merged, deployed to test env | Developer | Code review passed & merged |
| `Testing` | QA / PO verifying Acceptance Criteria | QA / PO | Deployed in test environment |
| `Done` | AC verified + DoD met + PO accepted | **Product Owner ONLY** | **Gate Out:** Definition of Done (DoD) with evidence — [definitions.md](./.github/skills/product-owner/references/definitions.md) (lines 30–59) |

*Side states:* `Blocked` (must name blocker + owner) and `Dropped` (must name reason) — [definitions.md](./.github/skills/product-owner/references/definitions.md) (line 77).

### 2. Exact Files and Lines Where Status & Tracker State Live

In a real project folder (such as `order-tracking/`), story and epic status is tracked in **four exact places**:

#### A. Document-Level Workflow Progress (`epics.md` YAML Frontmatter)
- **Template definition:** [epic-template.md](./.github/skills/product-owner/assets/epic-template.md) (lines 1–5)
- **Live example:** [order-tracking/epics.md](./order-tracking/epics.md) (lines 1–5):
  ```yaml
  ---
  status: approved
  stepsCompleted: [epics, story-breakdown, story-definition, backlog, refinement, sprint-planning, development]
  inputDocuments: [prd.md]
  ---
  ```
  *How it works:* As each workflow step completes, its name is appended to `stepsCompleted` on line 3 so the agent always knows which of the 14 steps are finished and what comes next.

#### B. Per-Epic & Per-Story Metadata Block (`epics.md`)
- **Template definition:**
  - Epic tracker ID: [epic-template.md](./.github/skills/product-owner/assets/epic-template.md) (line 43: `**Tracker ID:** {{epic_tracker_id_N}}`)
  - Epic DoD checkboxes: [epic-template.md](./.github/skills/product-owner/assets/epic-template.md) (lines 49–58)
  - Story status & tracker ID: [epic-template.md](./.github/skills/product-owner/assets/epic-template.md) (lines 68–72: `**Estimate:**`, `**Priority:**`, `**Status:** Backlog`, `**Tracker ID:** {{tracker_id}}`)
- **Live example in [order-tracking/epics.md](./order-tracking/epics.md):**
  - **Epic 1 Metadata:** lines 55–58 (`Covers`, `Dependencies`, `Priority: 1`, `Tracker ID: TBD`) and Epic DoD checkboxes on lines 68–75.
  - **Story 1.1 (`In Progress`):** lines 83–90 hold `Covers`, `Depends on`, `Estimate: 3`, `Priority: 1`, `Risk: Medium`, `Status: In Progress` (line 88), `Assignee: Priya` (line 89), and `Tracker ID: TBD` (line 90). Its 10-item DoR gate is checked off `[x]` on lines 127–137.
  - **Story 1.2 (`Backlog`):** lines 145–151 hold `Estimate: Needs team estimate` (line 147), `Status: Backlog` (line 150), `Tracker ID: TBD` (line 151), and its partial DoR checklist (`[x]` vs `[ ]` with open owners) on lines 183–193.
  - **Story 1.3 (`Backlog`):** lines 201–207 hold `Status: Backlog` (line 206), `Tracker ID: TBD` (line 207), and its DoR checklist on lines 239–249.

#### C. Master Ordered Backlog & Audit Log (`backlog.md`)
- **Rule definition:** [05-backlog.md](./.github/skills/product-owner/references/05-backlog.md) (lines 22–26)
- **Live example in [order-tracking/backlog.md](./order-tracking/backlog.md):**
  - **Backlog Table (lines 13–17):** Mirrors every story's `Rank`, `Story` (markdown link to `epics.md`), `Epic`, `Value`, `Risk`, `Depends on`, `Points`, `Bucket` (`Now`/`Next`/`Later`), `Status` (`In Progress` / `Backlog`), and `Assignee`.
  - **Refinement & Status Log (lines 19–22):** Chronological audit trail recording *when* and *why* a story changed status (e.g., line 21 logs Story 1.1 moving `Backlog → Ready` after passing DoR, committing to Sprint 01, and moving `Ready → In Progress` under Priya).

#### D. Active Sprint Board (`sprints/sprint-<nn>.md`)
- **Template definition:** [sprint-plan-template.md](./.github/skills/product-owner/assets/sprint-plan-template.md) (lines 14–20)
- **Live example in [order-tracking/sprints/sprint-01.md](./order-tracking/sprints/sprint-01.md):**
  - **Committed Stories Table (lines 14–16):** Tracks sprint-level execution (`Order`, `Story`, `Points`, `Depends on`, `Owner`, `Status: In Progress`).
  - **DoR Gate Check (lines 26–30):** Confirms all 3 sprint readiness gates before work begins.

#### E. External Tracker Mapping (Azure DevOps & Jira)
- **Rule definition:** [09-tracker.md](./.github/skills/product-owner/references/09-tracker.md) (lines 7–49)
- **Status mapping table (lines 21–31):**
  - `Backlog` ↔ ADO `New` / Jira `Backlog`
  - `Ready` ↔ ADO `Approved / Ready` / Jira `Ready for Dev`
  - `In Progress` ↔ ADO `Active` / Jira `In Progress`
  - `In Review` ↔ ADO `Active (tag: in-review)` / Jira `In Review`
  - `Built` ↔ ADO `Resolved` / Jira `Built / Ready for QA`
  - `Testing` ↔ ADO `Testing (or Resolved + tag)` / Jira `In Testing`
  - `Done` ↔ ADO `Closed` / Jira `Done`
- **Sync & Drift Check (lines 35–39):** Whenever an item is created in ADO/Jira, its ID replaces `TBD` in `**Tracker ID:**` inside `epics.md`. Step 9 requires comparing the external tracker against `epics.md` and `backlog.md` ("Drift check", line 39) so local markdown and external boards always match.

---

## Part 3: How the Templates Were Created & What References They Use

All 6 templates in [.github/skills/product-owner/assets/](./.github/skills/product-owner/assets/) were designed by directly translating the rules in `.github/skills/product-owner/references/` and established Agile / Product Management frameworks into fill-in-the-blank `{{variable}}` structures.

Here is the exact origin and reference design behind each template:

### 1. `prd-template.md`
- **File:** [prd-template.md](./.github/skills/product-owner/assets/prd-template.md) (lines 1–64)
- **Paired Reference:** [01-prd.md](./.github/skills/product-owner/references/01-prd.md)
- **Frameworks & References Used to Design It:**
  - **Standard Lean PRD & Marty Cagan / SVPG Opportunity Assessment:** Sections 1 (`Problem`, `Goal`, `Why now`) and 5 (`Baseline`, `Target`, `How measured`, `When`) enforce outcome-oriented product management rather than feature lists.
  - **IEEE 830 / BABOK Requirements Traceability:** Section 3 separates Functional (`FR1`, `FR2`), Non-Functional (`NFR1` with hard p95/latency numbers), and Additional constraints so every requirement has a unique ID that later links to Epics and Stories.
  - **Explicit Scope Guardrails:** Section 4 requires an explicit `Out of Scope` list with a `(reason: {{reason}})` to prevent scope creep.
  - **RAPID / DACI Decision Governance:** Section 2 (`user / decider / veto` roles) and Section 8 (`Decisions` log) ensure the agent never guesses stakeholder sign-off.

### 2. `epic-template.md`
- **File:** [epic-template.md](./.github/skills/product-owner/assets/epic-template.md) (lines 1–86)
- **Paired References:** [02-epic.md](./.github/skills/product-owner/references/02-epic.md), [03-story-breakdown.md](./.github/skills/product-owner/references/03-story-breakdown.md), [04-story-definition.md](./.github/skills/product-owner/references/04-story-definition.md), and [definitions.md](./.github/skills/product-owner/references/definitions.md)
- **Frameworks & References Used to Design It:**
  - **BMAD-Method / AI-Agent Frontmatter State Pattern:** Lines 1–5 (`status`, `stepsCompleted: []`, `inputDocuments: []`) use structured YAML frontmatter so an AI agent can resume multi-step epic/story decomposition across chat turns without losing state.
  - **Requirements Traceability Matrix (RTM):** Lines 13–31 (`Requirements Inventory` + `FR Coverage Map`) force a 1-to-1 check between `prd.md` and `epics.md` before any story is written.
  - **Mike Cohn / Connextra User Story Format:** Lines 62–64 use the classic Connextra template (*"As a `{{user_type}}`, I want `{{capability}}`, So that `{{value_benefit}}`"*).
  - **Dan North / Cucumber BDD (Behavior-Driven Development):** Lines 74–83 use Gherkin syntax (`Given` / `When` / `Then` / `And`) so every Acceptance Criterion is directly executable as a test scenario.
  - **Scrum Guide Definition of Done:** Lines 45–58 embed the 8-point Epic DoD from [definitions.md](./.github/skills/product-owner/references/definitions.md) (lines 43–55) directly into every epic.

### 3. `sprint-plan-template.md`
- **File:** [sprint-plan-template.md](./.github/skills/product-owner/assets/sprint-plan-template.md) (lines 1–36)
- **Paired References:** [07-sprint-planning.md](./.github/skills/product-owner/references/07-sprint-planning.md) and [definitions.md](./.github/skills/product-owner/references/definitions.md)
- **Frameworks & References Used to Design It:**
  - **Scrum Guide Sprint Planning (Topic One, Two, Three):** Captures the *Why* (`Sprint goal`, line 4), the *How Much* (`Capacity` table + historical velocity on lines 6–12), and the *What* (`Committed Stories` vs `Stretch` on lines 14–24).
  - **INVEST & Scrum "Gate In" (Definition of Ready):** Lines 30–35 embed a mandatory `DoR Check` block so no story can be added to the sprint table unless it passed all 10 readiness checks in Step 6.

### 4. `release-notes-template.md`
- **File:** [release-notes-template.md](./.github/skills/product-owner/assets/release-notes-template.md) (lines 1–46)
- **Paired Reference:** [11-release-prep.md](./.github/skills/product-owner/references/11-release-prep.md)
- **Frameworks & References Used to Design It:**
  - **Keep a Changelog & User-Centric Release Notes:** Sections `Highlights`, `What's New` (focusing on `What changed for the user` rather than git commits), `Fixes`, and `Known Issues` with workarounds (lines 6–24).
  - **Scope Transparency:** Section `Not Included (planned but deferred)` (lines 26–28) prevents silent scope drops by naming deferred stories and where they moved.
  - **ITIL / SRE Release Readiness & Go/No-Go Checklists:** Sections `Deployment Plan` (with `Rollback plan` and `Feature flags`, lines 30–37) and `Go-Live Readiness` (lines 39–46) enforce operational safety before Step 13 production deployment.

### 5. `stakeholder-update-template.md`
- **File:** [stakeholder-update-template.md](./.github/skills/product-owner/assets/stakeholder-update-template.md) (lines 1–39)
- **Paired Reference:** [12-stakeholder-updates.md](./.github/skills/product-owner/references/12-stakeholder-updates.md)
- **Frameworks & References Used to Design It:**
  - **Executive RAG (Red / Amber / Green) Status Reporting & BLUF (Bottom Line Up Front):** Line 3 puts health (`🟢 On track / 🟡 At risk / 🔴 Off track`) at the very top, followed by a 2–3 sentence `Summary` (lines 6–8).
  - **RAID Log (Risks, Assumptions, Issues, Dependencies) & Decision-Driven Reporting:** Sections `Progress`, `Milestones`, `Risks and Issues` (with `Impact`, `Mitigation`, `Owner`), and `Decisions or Help Needed` (lines 10–35) ensure stakeholders immediately see what changed and what action is needed from them.

### 6. `post-release-review-template.md`
- **File:** [post-release-review-template.md](./.github/skills/product-owner/assets/post-release-review-template.md) (lines 1–39)
- **Paired Reference:** [14-post-release.md](./.github/skills/product-owner/references/14-post-release.md)
- **Frameworks & References Used to Design It:**
  - **Build-Measure-Learn Feedback Loop (Lean Startup / Continuous Discovery):** Section `Metrics vs PRD Targets` (lines 6–10) directly closes the loop opened in Step 1 (`prd-template.md` Section 5) by comparing `Target` vs `Actual` with a strict verdict (`Met / Missed / Too early`).
  - **Agile Retrospective & Post-Implementation Review (PIR):** Combines production incident tracking (`Issues Since Release`), voice-of-the-customer triage (`Feedback`), team reflection (`What Went Well / What to Improve`), and a `Backlog Updates` checklist (lines 12–39) so learnings immediately feed the next cycle of Step 1 or Step 5.


## current limitations

Status and gates are only described, so nothing enforces them. A story can be marked Ready without a DoR check.
Tracking lives in markdown, so there is no way to list or query what is blocked.
Its references are generic (for example, Azure DevOps / Jira are named but no integration exists in the folder).