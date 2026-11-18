---
status: approved
stepsCompleted: [epics, story-breakdown, story-definition, backlog, refinement, sprint-planning, development]
inputDocuments: [prd.md]
---

# Customer Order Tracking - Epic Breakdown

## Overview

This document provides the epic breakdown for Customer Order Tracking, decomposing the requirements from [prd.md](./prd.md). Stories are added in the story breakdown step.

## Requirements Inventory

### Functional Requirements

- **FR1:** A signed-in customer can view a list of their orders, each with its current status.
- **FR2:** A customer can open one order and see its current status and the time of the last status change.
- **FR3:** The order status shown online matches the order system's status (live, not manually updated).
- **FR4:** When an order's status changes, the customer receives an email naming the order and the new status.
- **FR5:** A customer sees only their own orders.

### NonFunctional Requirements

- **NFR1:** A status change appears online within 5 minutes of the change in the order system.
- **NFR2:** A status-change email is sent within 10 minutes of the change.
- **NFR3:** The order status page loads in under 2s at p95.

### Additional Requirements

- **AR1:** Status data comes from the existing order system and, where needed, existing carrier data. No carrier-side changes.
- **AR2:** Customer email is personal data; handling follows company privacy policy.

### UX Design Requirements

None in the PRD.

### FR Coverage Map

| Requirement | Epic |
|---|---|
| FR1, FR2, FR3, FR4, FR5 | Epic 1: Order Status View |
| NFR1, NFR2, NFR3 | Epic 1: Order Status View |
| AR1, AR2 | Epic 1: Order Status View |

## Epic List

1. Epic 1: Order Status View

## Epic 1: Order Status View

Online customers can view a live list of their orders, inspect any order's current status and last status-change timestamp, and receive an email notification whenever an order's status changes, reducing order-status support calls by 40% (from ~2,000/month to 1,200 or fewer) within 3 months of release.

**Covers:** FR1, FR2, FR3, FR4, FR5, NFR1, NFR2, NFR3, AR1, AR2
**Dependencies:** Order system (status data), email service, support team (call tagging and baseline)
**Priority:** 1
**Tracker ID:** TBD

### Scope & Constraints (from PRD)

- **In Scope:** Online order status view for signed-in customers (order list and order detail with last status-change time); email notification on each order status change.
- **Out of Scope:** Returns, refunds, SMS notifications, carrier-side changes.

### Definition of Done

The epic is done only when all of the following hold:

- [ ] All stories in the epic are complete and accepted
- [ ] Every acceptance criterion has been verified
- [ ] Automated tests pass and no known regressions remain
- [ ] Code is reviewed and merged
- [ ] Documentation is updated
- [ ] Applicable NFRs are met (NFR1: online status within 5 min; NFR2: email sent within 10 min; NFR3: page load p95 < 2s)
- [ ] The product owner has accepted the epic (demo or sign-off)
- [ ] No open critical or high-severity defects

### Story 1.1: View Single Order Live Status (Tracer Bullet)

As a signed-in customer,
I want to open one of my orders and see its live status and last status-change time directly from the order system,
So that I can immediately verify where my order is and when it last updated.

**Covers:** FR2, FR3, FR5, NFR1, NFR3, AR1
**Depends on:** None (external: order system read access)
**Estimate:** 3
**Priority:** 1
**Risk:** Medium
**Status:** Done (code reviewed; 7/7 tests passing. Code: `order-tracking/app/`; tests: `order-tracking/app/tests/`.
**Waiver (PO sign-off, 2026-11-18):** Accepted without (a) merge to git, (b) recorded demo, (c) NFR3 p95 page-load measurement. These carry forward: merge and demo before the epic is closed; NFR3 measured in a follow-up.)
**Assignee:** Priya
**Tracker ID:** TBD
**Runnable Done Check:** Sign in as Customer A, open order `#1001`, verify the page renders the exact status and timestamp from the order system in < 2s (p95) and updates within 5 minutes of an order-system status change; then request Customer B's order `#1002` or unknown order `#9999` and verify access is denied (HTTP 403/404); then simulate an order-system read timeout/error and verify a retry message renders without exposing raw errors.

**Acceptance Criteria:**

**AC1 — Happy path (live status and timestamp):**
**Given** a signed-in customer who owns order `#1001` with status `Shipped` and last status change `2026-11-17T10:00:00Z` in the order system
**When** the customer opens the detail page for order `#1001`
**Then** the page displays order `#1001`, current status `Shipped`, and last status-change timestamp `2026-11-17T10:00:00Z` matching the order system (FR2, FR3, AR1)
**And** the page loads in under 2 seconds at p95 (NFR3)

**AC2 — Near-real-time status update:**
**Given** order `#1001` changes status from `Packed` to `Shipped` at `2026-11-17T10:05:00Z` in the order system
**When** 5 minutes or less have elapsed and the customer loads or refreshes the order `#1001` detail page
**Then** the page displays the updated status `Shipped` and timestamp `2026-11-17T10:05:00Z` (FR2, FR3, NFR1)

**AC3 — Authorization refusal (other customer's order):**
**Given** a signed-in customer who does not own order `#1002`
**When** the customer requests the detail page for order `#1002`
**Then** the system does not expose any data for order `#1002` and returns a 404/403 "Order not found" state (FR5)

**AC4 — Empty / non-existent order state:**
**Given** a signed-in customer
**When** the customer requests an order ID `#9999` that does not exist in the order system
**Then** the page displays a clear "Order not found" message with a link back to the customer's account/orders within 2 seconds at p95 (FR2, NFR3)

**AC5 — Failure state (order system unavailable or timed out):**
**Given** a signed-in customer who owns order `#1001` and the order system fails to respond within 2 seconds or returns an error
**When** the customer opens the detail page for order `#1001`
**Then** the page displays "Live order status is temporarily unavailable. Please try again in a few minutes." instead of a stale/fabricated status or raw error stack trace (FR3, NFR3)

**Definition of Ready (DoR) Check:**
- [x] Story statement written (As a / I want / So that)
- [x] Linked to an epic (Epic 1) and PRD requirements (FR2, FR3, FR5, NFR1, NFR3, AR1)
- [x] Acceptance criteria written and agreed (5 ACs: happy path, live freshness, auth refusal, non-existent order, order-system failure)
- [x] Estimated by the team, within the max size (default 8 points) — 3 points (confirmed 2026-11-17)
- [x] Prioritized in the backlog (Priority 1, Risk: Medium)
- [x] Dependencies identified and none blocking (first story; external: order system read access)
- [x] Design / UX available (if user-facing) — confirmed 2026-11-17
- [x] Access, test data, environments available — confirmed 2026-11-17
- [x] No open `Unknown` or placeholder in requirements/AC
- [x] Team confirms they can start without coming back to the PO — confirmed 2026-11-17

### Story 1.2: View My Orders List with Current Status

As a signed-in customer,
I want to view a list of all my orders with each order's current live status and open any order's detail view,
So that I can check all my purchases in one place without needing an order link or calling support.

**Covers:** FR1, FR3, FR5, NFR1, NFR3, AR1
**Depends on:** Story 1.1
**Estimate:** Needs team estimate
**Priority:** 2
**Risk:** Low
**Status:** Backlog
**Tracker ID:** TBD
**Runnable Done Check:** Sign in as a customer with 2 orders and verify only those 2 orders and their live statuses render in < 2s (p95) and link to the Story 1.1 detail view; sign in as a customer with 0 orders and verify the empty-state message renders; simulate an order-system error and verify a retry message renders.

**Acceptance Criteria:**

**AC1 — Happy path (order list with live statuses):**
**Given** a signed-in customer who owns orders `#1001` (`Shipped`) and `#1003` (`Packed`) in the order system, while another customer owns order `#1002`
**When** the customer opens the "My Orders" page
**Then** only orders `#1001` (`Shipped`) and `#1003` (`Packed`) are listed with statuses matching the order system, and `#1002` is not shown (FR1, FR3, FR5, AR1)
**And** the page loads in under 2 seconds at p95 (NFR3)

**AC2 — Near-real-time status update on list:**
**Given** order `#1003` changes status from `Packed` to `Shipped` in the order system
**When** 5 minutes or less have elapsed and the customer refreshes the "My Orders" page
**Then** order `#1003` is shown with status `Shipped` in the list (FR1, FR3, NFR1)

**AC3 — Navigate from list to order detail:**
**Given** a signed-in customer viewing the "My Orders" list
**When** the customer selects order `#1001`
**Then** the Story 1.1 order detail page opens for `#1001` showing its current status and last status-change timestamp (FR1, FR2)

**AC4 — Empty state (customer has zero orders):**
**Given** a signed-in customer who has 0 orders in the order system
**When** the customer opens the "My Orders" page
**Then** the page displays "You have no orders yet" and renders no order rows in under 2 seconds at p95 (FR1, FR5, NFR3)

**AC5 — Failure state (order system unavailable):**
**Given** a signed-in customer and the order system fails to respond within 2 seconds or returns an error
**When** the customer opens the "My Orders" page
**Then** the page displays "Your orders cannot be loaded right now. Please try again in a few minutes." without exposing raw error details (FR3, NFR3)

**Definition of Ready (DoR) Check:**
- [x] Story statement written (As a / I want / So that)
- [x] Linked to an epic (Epic 1) and PRD requirements (FR1, FR3, FR5, NFR1, NFR3, AR1)
- [x] Acceptance criteria written and agreed (5 ACs: happy path, live freshness, navigation to detail, zero-orders empty state, order-system failure)
- [ ] Estimated by the team, within the max size (default 8 points) — *open: needs team estimate (owner: dev team)*
- [x] Prioritized in the backlog (Priority 2, Risk: Low)
- [x] Dependencies identified (Depends on Story 1.1)
- [ ] Design / UX available (if user-facing) — *open: confirm whether existing account UI styles suffice (owner: you/UX)*
- [ ] Access, test data, environments available — *open: confirm test accounts with 0 and 2+ orders (owner: dev team)*
- [x] No open `Unknown` or placeholder in requirements/AC
- [ ] Team confirms they can start without coming back to the PO — *pending team estimate & environment check*

### Story 1.3: Send Email Notification on Order Status Change

As an online customer,
I want to receive an email naming my order and its new status whenever my order's status changes,
So that I know my order progressed without having to visit the website or call support.

**Covers:** FR4, NFR2, AR1, AR2
**Depends on:** Story 1.1 (uses the order-system status feed; external: email service)
**Estimate:** Needs team estimate
**Priority:** 3
**Risk:** Medium
**Status:** Backlog
**Tracker ID:** TBD
**Runnable Done Check:** Trigger a status change on a test order in the order system from `Packed` to `Shipped` and verify within 10 minutes that 1 email arrives at the owner's address containing the order ID, `Shipped`, and a link to the order detail page; re-send the identical status and verify no duplicate email is sent; simulate an email service failure or missing email address and verify the failure is logged without crashing online status views.

**Acceptance Criteria:**

**AC1 — Happy path (email sent on status change within 10 minutes):**
**Given** order `#1001` owned by a customer with a valid email address on file changes status from `Packed` to `Shipped` in the order system
**When** the status change is detected
**Then** exactly 1 email is sent to that customer's email address within 10 minutes naming order `#1001`, the new status `Shipped`, and a link to view the order online (FR4, NFR2, AR1, AR2)

**AC2 — Idempotency (no duplicate email when status is unchanged):**
**Given** an email for order `#1001` changing to `Shipped` has already been sent
**When** a subsequent check or duplicate event reports order `#1001` is still `Shipped`
**Then** no additional email is sent to the customer (FR4)

**AC3 — Privacy and scoping (recipient receives only their own order):**
**Given** order `#1001` belongs to Customer A
**When** the status-change email for `#1001` is generated and sent
**Then** the email is addressed only to Customer A's email on file and contains no other customer's order data or personal data beyond what privacy policy permits (FR5, AR2)

**AC4 — Empty / missing email state:**
**Given** an order changes status in the order system but the customer record has no valid email address on file
**When** the notification step runs
**Then** no email send is attempted, a warning is logged with the order ID, and processing continues for other orders without error (FR4, AR2)

**AC5 — Failure state (email service unavailable or transient error):**
**Given** order `#1001` changes status to `Shipped` and the email service returns an error or times out
**When** the send attempt fails
**Then** the failure is logged with order ID `#1001` and status `Shipped` for retry/alerting, and the failure does not block or degrade online order status reads (FR3, FR4, NFR2)

**Definition of Ready (DoR) Check:**
- [x] Story statement written (As a / I want / So that)
- [x] Linked to an epic (Epic 1) and PRD requirements (FR4, NFR2, AR1, AR2)
- [x] Acceptance criteria written and agreed (5 ACs: happy path ≤ 10 min, idempotency, privacy scoping, missing email empty state, email service failure)
- [ ] Estimated by the team, within the max size (default 8 points) — *open: needs team estimate (owner: dev team)*
- [x] Prioritized in the backlog (Priority 3, Risk: Medium)
- [x] Dependencies identified (Depends on Story 1.1; external: email service)
- [ ] Design / UX available (if user-facing) — *open: confirm plain/transactional email template copy (owner: you)*
- [ ] Access, test data, environments available — *open: confirm sandbox email service credentials (owner: dev team)*
- [x] No open `Unknown` or placeholder in requirements/AC
- [ ] Team confirms they can start without coming back to the PO — *pending team estimate & environment check*
