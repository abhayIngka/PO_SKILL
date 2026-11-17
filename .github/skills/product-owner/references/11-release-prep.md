# 11. Release Preparation

**Goal:** everyone knows what ships, how, and whether we are ready to go live.
**Template:** `assets/release-notes-template.md` → `releases/release-<version>-notes.md`.

## Steps

1. **Define the release scope:** list the Done stories and fixes going out; list what was planned but is not included, with reasons.
2. **Write release notes** in user terms (what changed for them), not internal jargon. Include known issues and workarounds.
3. **Plan the deployment** with the delivery or ops team: steps, owners, timing, feature flags, data migrations, rollback plan, communication to users.
4. **Check go-live readiness** (checklist in the template):
   - All release stories Done (DoD met), no open critical or high defects
   - Regression and smoke tests pass in staging
   - NFRs verified (performance, security)
   - Monitoring and alerts ready; rollback tested
   - Support and stakeholders informed
5. **Go / No-Go:** present the evidence and a recommendation; the user (and release owner) decide. Record the decision, who, and when.

## Done when

- [ ] Release notes written and reviewed
- [ ] Deployment and rollback plan agreed
- [ ] Readiness checklist complete
- [ ] Go decision recorded

**Next:** [12-stakeholder-updates.md](12-stakeholder-updates.md)
