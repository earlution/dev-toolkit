# Epic 4: Kanban Framework

**Status:** TODO  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Created:** 2025-12-02  
**Last updated:** 2025-12-02 (v0.4.3.6+1 – Task 6 complete: Document integration examples and edge cases)  
**Branch:** `epic/4-kanban-framework`  
**Version Schema:** `0.4.S.T+B`  
**Production URL:** [N/A for this repo]

---

## Story Checklist

- [x] **E4:S01 – Dev Kit Kanban Implementation** - COMPLETE ✅ (v0.4.1.1+6)  
- [x] **E4:S02 – FR/BR Intake to Tasks** - COMPLETE ✅ (v0.4.2.5+1)
  - Story: [`epics/Epic-4/stories/Story-002-fr-br-intake-to-tasks.md`](epics/Epic-4/stories/Story-002-fr-br-intake-to-tasks.md)  
- [ ] **E4:S03 – Kanban + Versioning + RW Integration** - IN PROGRESS (v0.4.3.6+1)
  - Tasks: T001 ✅ (v0.4.3.1+1), T002 ✅ (v0.4.3.2+2), T003 ✅ (v0.4.3.3+1), T004 ✅ (v0.4.3.4+1), T005 ✅ (v0.4.3.5+1), T006 ✅ (v0.4.3.6+1), T007 ✅ (v0.4.3.7+1)
  - Story: [`epics/Epic-4/stories/Story-003-kanban-versioning-rw-integration.md`](epics/Epic-4/stories/Story-003-kanban-versioning-rw-integration.md)  

---

## Overview

Epic 4 owns the **Kanban framework** (`packages/frameworks/kanban/`) and its concrete application inside this repo:

- Kanban board under `KB/PM_and_Portfolio/kanban/_index.md`
- Story files under `KB/PM_and_Portfolio/kanban/epics/Epic-4/stories/`
- Kanban governance policy for this repo

It ensures that:

- All substantive work is **Task/FR-driven**.
- Kanban, versioning, and RW form a coherent system.

---

## Goals

1. **Implement dev-kit Kanban using the framework**  
   - Align local Kanban policy with the framework policy.
   - Adopt the FR/BR → Task → Story → Epic rule in practice.

2. **Design FR/BR intake flow**  
   - Make it easy to go from an incoming Feature Request or Bug Report to:
     - Task(s) under a Story
     - Story under an Epic (creating them when missing)

3. **Clarify Kanban + Versioning + RW integration**  
   - Show how Tasks map to `TASK` in versions.
   - Show how RW updates Kanban docs and forensic markers.

---

## Stories (Initial)

### Story 1: Dev Kit Kanban Implementation

**Status:** COMPLETE  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Last updated:** 2025-12-02 (v0.4.3.6+1 – Task 6 complete: Document integration examples and edge cases)  

**Goal:**  
Fully align the dev-kit Kanban board, stories, and governance policy with the Kanban framework package. Establish `vibe-dev-kit` as the canonical SoT for Kanban policies, templates, and governance.

**Tasks:**
- [x] E4:S01:T001 – Review existing dev-kit Kanban policies and templates ✅ COMPLETE (v0.4.1.1+2)
- [x] E4:S01:T002 – Ingest findings from fynd.deals Epic 15 Kanban work into dev-kit ✅ COMPLETE (v0.4.1.1+3)
- [x] E4:S01:T003 – Update dev-kit Kanban governance policy as canonical SoT ✅ COMPLETE (v0.4.1.1+4)
- [x] E4:S01:T004 – Align dev-kit Kanban templates with updated governance ✅ COMPLETE (v0.4.1.1+5)
- [x] E4:S01:T005 – Document consumption pattern for other projects ✅ COMPLETE (v0.4.1.1+6)

> Full story: [`epics/Epic-4/stories/Story-001-dev-kit-kanban-implementation.md`](epics/Epic-4/stories/Story-001-dev-kit-kanban-implementation.md)  

---

### Story 2: FR/BR Intake to Tasks

**Status:** COMPLETE  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Last updated:** 2025-12-02 (v0.4.2.5+1 – Task 5 complete: Create intake workflow guide for agents/users - Story 2 COMPLETE)

**Goal:**  
Design and implement a clear, actionable flow for converting incoming Feature Requests (FRs) and Bug Reports (BRs) into Kanban Tasks. This story ensures that all work entering the dev-kit is properly structured, tracked, and aligned with the Kanban → Versioning → Release Workflow system.

**Tasks:**
- [x] E4:S02:T001 – Analyze current FR/BR intake process and requirements ✅ COMPLETE (v0.4.2.1+1)
- [x] E4:S02:T002 – Design FR/BR → Task → Story → Epic decision flow ✅ COMPLETE (v0.4.2.2+1)
- [x] E4:S02:T003 – Create FR/BR intake templates and forms ✅ COMPLETE (v0.4.2.3+1)
- [x] E4:S02:T004 – Document the intake process with examples ✅ COMPLETE (v0.4.2.4+1)
- [x] E4:S02:T005 – Create intake workflow guide for agents/users ✅ COMPLETE (v0.4.2.5+1)

> Full story: [`epics/Epic-4/stories/Story-002-fr-br-intake-to-tasks.md`](epics/Epic-4/stories/Story-002-fr-br-intake-to-tasks.md)  

---

### Story 3: Kanban + Versioning + RW Integration

**Status:** IN PROGRESS  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Last updated:** 2025-12-02 (v0.4.3.6+1 – Task 6 complete: Document integration examples and edge cases)

**Goal:**  
Ensure seamless integration between Kanban, Versioning, and Release Workflow (RW) systems within the dev-kit. This story validates that the three frameworks work together cohesively, providing end-to-end traceability from Feature Requests/Bug Reports through Kanban Tasks to versioned releases.

**Tasks:**
- [x] E4:S03:T001 – Review existing integration documentation ✅ COMPLETE (v0.4.3.1+1)
- [x] E4:S03:T002 – Validate Kanban → Versioning integration in dev-kit ✅ COMPLETE (v0.4.3.2+2)
- [x] E4:S03:T003 – Validate Versioning → RW integration in dev-kit ✅ COMPLETE (v0.4.3.3+1)
- [x] E4:S03:T004 – Validate RW → Kanban integration in dev-kit ✅ COMPLETE (v0.4.3.4+1)
- [x] E4:S03:T007 – Address RW → Kanban integration gaps identified in T004 ✅ COMPLETE (v0.4.3.7+1)
- [x] E4:S03:T005 – Create dev-kit integration guide ✅ COMPLETE (v0.4.3.5+1)
- [x] E4:S03:T006 – Document integration examples and edge cases ✅ COMPLETE (v0.4.3.6+1)

> Full story: [`epics/Epic-4/stories/Story-003-kanban-versioning-rw-integration.md`](epics/Epic-4/stories/Story-003-kanban-versioning-rw-integration.md)  

---

## Dependencies

**Blocks:**
- Clear, reusable Kanban implementation for dev-kit work.

**Blocked By:**
- Epic 1 and Epic 3 for some versioning and core-policy decisions.

**Coordinates With:**
- Epic 1: Vibe Dev Kit Core  
- Epic 2: Workflow Management Framework  
- Epic 3: Numbering & Versioning Framework  

---

## References

- `packages/frameworks/kanban/README.md`  
- `packages/frameworks/kanban/policies/kanban-governance-policy.md`  
- `KB/PM_and_Portfolio/rituals/policy/kanban-governance-policy.md`  
- `KB/PM_and_Portfolio/kanban/_index.md`  


