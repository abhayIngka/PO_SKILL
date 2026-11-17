---
status: approved
version: 1.0
owner: Product Owner
updated: 2026-11-17
---

# Customer Order Tracking - Product Requirements Document

## 1. Business Goals

- **Problem:** Customers call support to ask where their order is. This is about 2,000 calls a month.
- **Goal:** Customers see live order status online and get an email when it changes, so they do not need to call.
- **Why now:** Open question Q1.

## 2. Users and Stakeholders

| Who | Needs | Role (user / decider / veto) |
|---|---|---|
| Online customer | See where my order is, and be told when it changes | user |
| Customer support | Fewer "where is my order" calls | stakeholder |
| Decider / sign-off | Open question Q2 | decider |

## 3. User Requirements

### Functional Requirements

- **FR1:** A signed-in customer can view a list of their orders, each with its current status.
- **FR2:** A customer can open one order and see its current status and the time of the last status change.
- **FR3:** The order status shown online matches the order system's status (live, not manually updated).
- **FR4:** When an order's status changes, the customer receives an email naming the order and the new status.
- **FR5:** A customer sees only their own orders.

### Non-Functional Requirements

- **NFR1:** A status change appears online within 5 minutes of the change in the order system.
- **NFR2:** A status-change email is sent within 10 minutes of the change.
- **NFR3:** The order status page loads in under 2s at p95.

### Additional Requirements (constraints, integrations, compliance)

- Status data comes from the existing order system and, where needed, existing carrier data. No carrier-side changes.
- Customer email is personal data; handling follows company privacy policy (Q6).

## 4. Scope

### In Scope

- Online order status view for customers (list and detail).
- Email notification on each order status change.

### Out of Scope

- Returns (reason: not part of "where is my order").
- Refunds (reason: not part of "where is my order").
- SMS notifications (reason: email only for this release).
- Carrier-side changes (reason: we use the data we already receive).

## 5. Success Metrics

| Metric | Baseline | Target | How measured | When |
|---|---|---|---|---|
| Order-status support calls per month | about 2,000 (confirm exact figure, Q3) | 40% drop, to 1,200 or fewer | Support call log, calls tagged "order status" | Within 3 months of release |

## 6. Assumptions, Risks, Dependencies

- **Assumptions:**
  - Customers already have an account and can sign in. (Q5)
  - The order system holds a status that can be read in near real time. (Q5)
  - Customers have an email address on file.
- **Risks:**
  - Statuses are too coarse to answer "where is it" → agree the status list with support before building.
  - Customers do not find the page → link it from order confirmation emails and the account menu.
  - Calls are not tagged consistently, so the metric cannot be measured → agree the tagging with support before release.
- **Dependencies:** Order system (status data), email service, support team (call tagging and baseline).

## 7. Open Questions

- **Q1:** Why now (deadline, cost, complaints)? (owner: you)
- **Q2:** Who approves this PRD, and who can veto? (owner: you)
- **Q3:** Is about 2,000/month all order-status calls, and is there a tag to measure them? (owner: Support)
- **Q4:** Confirm NFR1 to NFR3 targets. (owner: you with engineering)
- **Q5:** Do accounts and a readable order status already exist? Do guest orders exist? (owner: engineering)
- **Q6:** Any privacy or email consent rules that apply? Can customers opt out of these emails? (owner: you)
- **Q7:** Which statuses are shown to the customer (for example placed, packed, shipped, delivered)? (owner: you with Support)

## 8. Decisions

- 2026-11-17: One epic for this PRD. (you)
- 2026-11-17: Out of scope: returns, refunds, SMS, carrier-side changes. (you)
- 2026-11-17: Success metric: order-status support calls down 40% within 3 months of release. (you)
- 2026-11-17: Proceed to stories using proposed NFR1-NFR3 targets and existing PRD content without additional pre-story gates. (you)
