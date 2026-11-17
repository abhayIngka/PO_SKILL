# Product Owner Agent

A Product Owner persona and skill covering the full delivery workflow, from PRD to post-release review.

```
.github/
  agents/product-owner.agent.md          # the persona
  skills/product-owner/
    SKILL.md                             # workflow overview and rules
    references/                          # 14 steps + definitions.md
    assets/                              # templates
```

**Flow:** PRD → Epic → Stories → Refinement → Prioritization → Sprint Planning → Development → Tracking → Validation → Release → Stakeholder Updates → Production → Post-Release Review

**Story status:** Backlog → Ready → In Progress → In Review → Built → Testing → Done

Copy `.github/` into the project that will use it, then invoke the `product-owner` agent in Copilot Chat.
