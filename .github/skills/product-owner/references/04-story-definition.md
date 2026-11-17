# 4. Story Definition

**Goal:** make each story clear enough to build and test without coming back to the PO.
**Template:** story block in `assets/epic-template.md`. Rules: [definitions.md](definitions.md).

## Steps

### 1. Acceptance Criteria

Write Given / When / Then criteria per story:

```
**Given** a signed-in customer with an empty cart
**When** they add an item priced 20.00
**Then** the cart total shows 20.00
**And** the cart count shows 1
```

- Cover the happy path and at least one failure, refusal, or empty state.
- Use numbers, not adjectives. Max 7 per story.

### 2. Definition of Ready

Run the DoR checklist in [definitions.md](definitions.md). Anything unmet is either fixed or listed as an open question with an owner.

### 3. Estimation

- **The team estimates, not the PO.** Ask for story points; do not propose them.
- A story over the max size (default 8) goes back to [03-story-breakdown.md](03-story-breakdown.md) to be split.
- Record the estimate on the story.

## Done when

- [ ] Every story has Given/When/Then criteria
- [ ] DoR checklist run; gaps listed with owners
- [ ] Team estimate recorded (or flagged "needs estimate")

**Next:** [05-backlog.md](05-backlog.md)
