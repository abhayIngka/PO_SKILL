# Customer Order Tracking - Product Backlog

**Updated:** 2026-11-17

## Ordering Rationale

Stories are ordered by **dependencies first**, then **risk**, then **business value**:
1. **Story 1.1** comes first as the thin tracer bullet: it has no story dependencies, proves the riskiest integration path (live read from the order system within 5 minutes and strict per-customer authorization), and unblocks both 1.2 and 1.3.
2. **Story 1.2** comes second: it builds on 1.1 to expose the full "My Orders" list so customers can discover their orders without needing a direct link.
3. **Story 1.3** comes third: it adds proactive email notifications on status change using the order-system status feed proven in 1.1.

## Backlog Table

| Rank | Story | Epic | Value | Risk | Depends on | Points | Bucket | Status | Assignee |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [1.1 View Single Order Live Status (Tracer Bullet)](./epics.md#story-11-view-single-order-live-status-tracer-bullet) | 1 | High | Medium | none | 3 | Now | In Progress | Priya |
| 2 | [1.2 View My Orders List with Current Status](./epics.md#story-12-view-my-orders-list-with-current-status) | 1 | High | Low | 1.1 | Needs estimate | Next | Backlog | Unassigned |
| 3 | [1.3 Send Email Notification on Order Status Change](./epics.md#story-13-send-email-notification-on-order-status-change) | 1 | High | Medium | 1.1 | Needs estimate | Next | Backlog | Unassigned |

## Refinement & Status Log

- **2026-11-17:** Story 1.1 estimated at 3 points; UX, test environment access, and team readiness confirmed. Passed DoR (`Backlog → Ready`), committed to [Sprint 01](./sprints/sprint-01.md), and moved `Ready → In Progress` assigned to Priya.
- **2026-11-17:** Stories 1.2 and 1.3 remain in `Backlog` pending team point estimates and DoR sign-off.
