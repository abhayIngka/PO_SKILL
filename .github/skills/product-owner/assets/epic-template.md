---
status: draft
stepsCompleted: []
inputDocuments: []
---

# {{project_name}} - Epic Breakdown

## Overview

This document provides the complete epic and story breakdown for {{project_name}}, decomposing the requirements from the PRD, UX Design if it exists, and Architecture requirements into implementable stories.

## Requirements Inventory

### Functional Requirements

{{fr_list}}

### NonFunctional Requirements

{{nfr_list}}

### Additional Requirements

{{additional_requirements}}

### UX Design Requirements

{{ux_design_requirements}}

### FR Coverage Map

{{requirements_coverage_map}}

## Epic List

{{epics_list}}

<!-- Repeat for each epic in epics_list (N = 1, 2, 3...) -->

## Epic {{N}}: {{epic_title_N}}

{{epic_goal_N}}

**Dependencies:** {{epic_dependencies_N}}
**Priority:** {{epic_priority_N}}
**Tracker ID:** {{epic_tracker_id_N}}

### Definition of Done

The epic is done only when all of the following hold:

- [ ] All stories in the epic are complete and accepted
- [ ] Every acceptance criterion has been verified
- [ ] Automated tests pass and no known regressions remain
- [ ] Code is reviewed and merged
- [ ] Documentation is updated
- [ ] Applicable NFRs are met
- [ ] The product owner has accepted the epic (demo or sign-off)
- [ ] No open critical or high-severity defects
{{epic_specific_dod_N}}

<!-- Repeat for each story (M = 1, 2, 3...) within epic N -->

### Story {{N}}.{{M}}: {{story_title_N_M}}

As a {{user_type}},
I want {{capability}},
So that {{value_benefit}}.

**Covers:** {{requirement_ids}}
**Depends on:** {{story_dependencies}}
**Estimate:** {{story_points}}
**Priority:** {{priority}}
**Status:** Backlog
**Tracker ID:** {{tracker_id}}

**Acceptance Criteria:**

<!-- for each AC on this story -->

**Given** {{precondition}}
**When** {{action}}
**Then** {{expected_outcome}}
**And** {{additional_criteria}}

<!-- End story repeat -->
