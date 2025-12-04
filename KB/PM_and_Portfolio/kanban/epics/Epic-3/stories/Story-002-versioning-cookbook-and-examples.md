---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-04T12:01:50Z
expires_at: null
housekeeping_policy: keep
---

# Story 002 – Versioning Cookbook & Examples

**Status:** IN PROGRESS  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Created:** 2025-12-03  
**Last updated:** 2025-12-03  
**Version:** v0.3.2.1+1 (planned)  
**Code:** E3S02

---

## Task Checklist

- [x] **E3:S02:T001 – Define core versioning scenarios for the cookbook** ✅ COMPLETE (v0.3.2.1+1)
- [x] **E3:S02:T002 – Create versioning cookbook document with worked examples** ✅ COMPLETE (v0.3.2.2+1)
- [x] **E3:S02:T003 – Add cross-framework examples (Kanban + Versioning + RW)** ✅ COMPLETE (v0.3.2.3+1)
- [ ] **E3:S02:T004 – Document edge cases and anti-patterns**
- [ ] **E3:S02:T005 – Create quick reference summary for users and agents**

---

## Overview

This story produces a **practical versioning cookbook** for the RC.EPIC.STORY.TASK+BUILD schema, turning the dev-kit versioning policy and framework docs into **concrete, copyable examples** for other projects.

It focuses on:

- Realistic scenarios (new epic, new story, new task, bugfix, hotfix, parallel work)
- Clear mapping between **Kanban → Versioning → RW**
- Guidance that is **safe to copy** into external projects

---

## Goal

Provide a **versioning cookbook** with worked examples that shows:

- How to select the right version components for common scenarios
- How to handle parallel epics/stories safely
- How to represent bugfixes and hotfixes
- How to keep Kanban, versioning, and RW aligned

---

## Tasks

### E3:S02:T001 – Define core versioning scenarios for the cookbook

**Input:**  
- `packages/frameworks/numbering & versioning/versioning-policy.md`  
- `packages/frameworks/numbering & versioning/versioning-strategy.md`  
- `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md`  

**Deliverable:**  
- Scenario list + brief description for each scenario

**Approach:**
1. Identify core scenarios:
   - New epic
   - New story under existing epic
   - New task under existing story
   - Bugfix / hotfix on an existing task
   - Parallel epics and stories
2. For each scenario:
   - Describe context
   - Describe expected version behaviour
   - Note any Kanban/RW interactions
3. Validate against framework policy and dev-kit policy.

**Acceptance Criteria:**
- [ ] Core scenarios identified and documented
- [ ] Each scenario has clear description and expected version behaviour
- [ ] Scenarios aligned with both framework and dev-kit policies

---

### E3:S02:T002 – Create versioning cookbook document with worked examples

**Input:**  
- Scenario list from T001  
- Existing dev-kit version history (CHANGELOG + archive)  

**Deliverable:**  
- `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-cookbook.md` (or similar)

**Approach:**
1. For each scenario from T001, create:
   - Before/after version examples
   - Kanban context (Epic/Story/Task)
   - RW perspective (how RW interprets the version)
2. Use real dev-kit examples where possible; create synthetic ones where not.
3. Structure cookbook by scenario, with clear headings and cross-links.

**Acceptance Criteria:**
- [ ] Cookbook document created
- [ ] At least one worked example per scenario
- [ ] Examples are copyable and safe for other projects
- [ ] Links to relevant policies and guides added

---

### E3:S02:T003 – Add cross-framework examples (Kanban + Versioning + RW)

**Input:**  
- Integration docs:
  - `KB/Architecture/Standards_and_ADRs/dev-kit-kanban-versioning-rw-integration.md`
  - `KB/PM_and_Portfolio/kanban/epics/Epic-4/stories/Story-003-kanban-versioning-rw-integration.md`

**Deliverable:**  
- Section in the cookbook with end-to-end cross-framework examples

**Approach:**
1. Select 2–3 representative flows:
   - FR → Task → Version → RW → Kanban update
   - Bugfix with verification requirement
   - Parallel epic/story work
2. For each flow, show:
   - Kanban state
   - Version change
   - RW steps and checks
   - Resulting documentation (changelogs, Kanban markers)

**Acceptance Criteria:**
- [ ] At least 2 cross-framework examples documented
- [ ] Each example ties together Kanban, versioning, and RW
- [ ] Examples align with existing integration docs

---

### E3:S02:T004 – Document edge cases and anti-patterns

**Input:**  
- Findings from Epic 3 Story 1  
- Findings from Epic 4 Story 3 (integration validation)  

**Deliverable:**  
- Edge cases & anti-patterns section in the cookbook

**Approach:**
1. List known edge cases:
   - Task renumbering
   - Story re-parenting between epics
   - Version conflicts when branches diverge
   - Incorrect TASK mapping
2. For each, document:
   - Symptom
   - Root cause
   - Corrective pattern
   - Preventive guidance

**Acceptance Criteria:**
- [ ] Edge cases identified and documented
- [ ] Anti-patterns clearly described
- [ ] Preventive guidance provided

---

### E3:S02:T005 – Create quick reference summary for users and agents

**Input:**  
- Cookbook content from T002–T004  

**Deliverable:**  
- Short quick reference (1–2 pages) for humans and agents

**Approach:**
1. Extract the most commonly needed rules and patterns.
2. Present them as:
   - Tables
   - Mini decision flows
   - \"If this, then version like that\" rules
3. Ensure language is agent-friendly and human-friendly.

**Acceptance Criteria:**
- [ ] Quick reference created
- [ ] Covers common scenarios and rules
- [ ] Linked from cookbook, dev-kit versioning policy, and relevant READMEs

---

## Acceptance Criteria (Story)

- [ ] Versioning cookbook document created with worked examples
- [ ] Core scenarios documented and validated
- [ ] Cross-framework examples (Kanban + Versioning + RW) included
- [ ] Edge cases and anti-patterns documented
- [ ] Quick reference summary created
- [ ] Links added from dev-kit versioning policy and framework READMEs to the cookbook

---

## References

- `packages/frameworks/numbering & versioning/versioning-policy.md`  
- `packages/frameworks/numbering & versioning/versioning-strategy.md`  
- `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md`  
- `KB/Architecture/Standards_and_ADRs/dev-kit-kanban-versioning-rw-integration.md`  
- `KB/PM_and_Portfolio/kanban/epics/Epic-4/stories/Story-003-kanban-versioning-rw-integration.md`  

---

_Last updated: 2025-12-03 (initial story definition)_  


