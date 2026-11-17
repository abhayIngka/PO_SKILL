# 10. Validation and Closure

**Goal:** accept only what is proven. Gate out of development.
**Rules:** [definitions.md](definitions.md) (AC, DoD, evidence).

## Story acceptance

1. Take a story in `Testing`.
2. **Verify each acceptance criterion** by running it (demo, test run, query). Record the evidence next to the criterion.
3. **Check the story DoD:** code reviewed and merged, tests pass, docs updated, NFRs met, no open critical/high defects.
4. All pass → set `Done`, with evidence. Any fail → move back to `In Progress`, name the failing criterion, and record why.
5. Update the tracker.

## Epic closure

1. Run the epic's **Definition of Done** from `epics.md`:
   - All stories complete and accepted
   - Every acceptance criterion verified
   - Automated tests pass, no regressions
   - Code reviewed and merged
   - Documentation updated
   - Applicable NFRs met
   - No open critical/high defects
   - Epic-specific lines
2. Tick each line **with evidence** (PR, CI run, report, file path). A tick without proof stays unticked.
3. Get **stakeholder acceptance**: demo or sign-off. Record the date and name as a `Decision: accepted`.
4. Mark the epic `Done`.

## Exceptions

- **Waiver:** a DoD line that does not apply is ticked as `evidence: waived, <reason>` with a recorded decision. Frequent waivers mean the DoD is wrong; raise it with the team.
- **Accepted with follow-up:** accept, and create the follow-up as its own backlog item. Never widen an accepted story afterwards.
- **Dropped stories:** need a reason; their requirements are delivered elsewhere or parked with a reason.

## Done when

- [ ] Every story and epic in scope is Done with evidence, or consciously deferred
- [ ] Stakeholder acceptance recorded
- [ ] Tracker matches

**Next:** [11-release-prep.md](11-release-prep.md)
