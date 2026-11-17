# 3. Epic → Story Breakdown

**Goal:** split each epic into stories small enough to build and accept in one sprint, and find what depends on what.
**Template:** story block inside `assets/epic-template.md`.
**Input:** the approved epics.

## Steps

1. For each epic, write stories as `Story N.M: title` with the statement:
   *As a {user}, I want {capability}, So that {value}.*
2. Split **vertically**: each story gives the user something usable end to end. Avoid splitting by layer ("build the API", "build the UI").
3. Good split patterns: by workflow step, by rule or variation, by user type, by happy path vs error path, by data or platform.
4. Each story: one outcome, fits in a sprint, independently testable. If it carries "and" over several requirements, split it.
5. Set `Covers:` to the FR/NFR ids it proves. Every epic requirement must be covered by some story.
6. Identify **dependencies** per story: `Depends on: 1.2`. Also note external ones (another team, access, data, environment).
   - Dependencies must not form a cycle.
   - The first story of the first epic proves the riskiest path.
7. Never shrink scope to fit ("for now", "simplified", "wire later"). That is a second story.

## Done when

- [ ] Every epic has stories; every epic requirement is covered
- [ ] Each story has statement, `Covers`, and `Depends on`
- [ ] No story is clearly larger than one sprint
- [ ] No dependency cycles
- [ ] User approved the breakdown

**Next:** [04-story-definition.md](04-story-definition.md)
