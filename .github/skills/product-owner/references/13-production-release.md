# 13. Production Release

**Goal:** ship safely and confirm it works in production.
**Rule:** the PO does not deploy alone. The release happens only after the Go decision ([11-release-prep.md](11-release-prep.md)) and an explicit yes from the user.

## Steps

1. **Confirm the Go decision** and that nothing changed since (no new defects, no scope changes).
2. **Deploy to production** following the deployment plan, with the delivery/ops team. Track each step.
3. **Verify in production:** smoke test the key user journeys from the release scope. Check feature flag states.
4. **Monitor the release:** watch errors, latency, key business metrics, and support channels for the agreed window (e.g. first 24-72 hours).
5. **If something breaks:** decide quickly between fix-forward and rollback, using the rollback plan. Tell stakeholders immediately.
6. **Close out:**
   - Mark released stories and epics with the version and date; tick the epic's production DoD line with evidence (deployment record, smoke test result).
   - Send the "released" update ([12-stakeholder-updates.md](12-stakeholder-updates.md)).
   - Publish the release notes.

## Done when

- [ ] Deployed and verified in production
- [ ] Monitoring window completed without unresolved critical issues
- [ ] Tracker updated (version, date, Done)
- [ ] Stakeholders told the outcome

**Next:** [14-post-release.md](14-post-release.md)
