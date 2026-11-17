# 1. PRD Writing

**Goal:** one document that says what we build, for whom, and how we know it worked.
**Template:** `assets/prd-template.md` → save as `prd.md`.
**Input:** an idea, brief, notes, transcript, or stakeholder request.

## Steps

1. Save the raw input as received (e.g. `sources/`). Do not edit it.
2. Fill the PRD sections:
   - **Business goals:** problem, goal, why now.
   - **User requirements:** FR (what it does), NFR (how well, with numbers), additional constraints. Number them `FR1`, `NFR1`...
   - **Scope:** what is in, and what is explicitly out with a reason.
   - **Success metrics:** baseline, target, how measured, when.
3. List assumptions, risks, dependencies, and open questions. Do not guess; ask.
4. Show the draft. Record the user's decisions in the Decisions section.

## Done when

- [ ] Every requirement has an id and is testable (no "fast", "easy")
- [ ] At least one item is explicitly out of scope
- [ ] Every success metric has a target and a way to measure it
- [ ] Stakeholders are named (who decides, who can veto)
- [ ] No open placeholder or TBD that blocks epic creation
- [ ] User approved the PRD

**Next:** [02-epic.md](02-epic.md)
