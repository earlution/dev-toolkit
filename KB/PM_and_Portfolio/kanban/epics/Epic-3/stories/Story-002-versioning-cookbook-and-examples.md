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
**Last updated:** 2025-12-04 (v0.3.2.5+2 – E3:S02:T05 complete: RW Step 2 logic updated for out-of-order completion)  
**Version:** v0.3.2.5+2  
**Code:** E3S02

---

## Task Checklist

- [x] **E3:S02:T01 – Define core versioning scenarios for the cookbook** ✅ COMPLETE (v0.3.2.1+1)
- [x] **E3:S02:T02 – Create versioning cookbook document with worked examples** ✅ COMPLETE (v0.3.2.2+1)
- [x] **E3:S02:T03 – Add cross-framework examples (Kanban + Versioning + RW)** ✅ COMPLETE (v0.3.2.3+1)
- [x] **E3:S02:T04 – Document edge cases and anti-patterns** ✅ COMPLETE (v0.3.2.4+1)
- [x] **E3:S02:T05 – Create quick reference summary for users and agents** ✅ COMPLETE (v0.3.2.5+1)
- [x] **E3:S02:T06 – Investigate and harden changelog ordering process** ✅ COMPLETE (v0.3.2.6+1)

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

### E3:S02:T01 – Define core versioning scenarios for the cookbook

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

### E3:S02:T02 – Create versioning cookbook document with worked examples

**Input:**  
- Scenario list from T01  
- Existing dev-kit version history (CHANGELOG + archive)  

**Deliverable:**  
- `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-cookbook.md` (or similar)

**Approach:**
1. For each scenario from T01, create:
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

### E3:S02:T03 – Add cross-framework examples (Kanban + Versioning + RW)

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

### E3:S02:T04 – Document edge cases and anti-patterns ✅ COMPLETE

**Input:**  
- Findings from Epic 3 Story 1  
- Findings from Epic 4 Story 3 (integration validation)  

**Deliverable:**  
- Edge cases & anti-patterns section in the cookbook ✅ **DELIVERED**

**Status:** ✅ **COMPLETE** - Comprehensive edge cases and anti-patterns section added to versioning cookbook

**Approach:**
1. ✅ Listed known edge cases:
   - Task renumbering
   - Story re-parenting between epics
   - Version conflicts when branches diverge
   - Incorrect TASK mapping
   - Standalone task references
   - BUILD number overflow
   - Missing version in changelog
   - Version mismatch between commit and tag
   - Parallel epic development ordering
2. ✅ For each, documented:
   - Symptom
   - Root cause
   - Corrective pattern
   - Preventive guidance

**Key Deliverables:**
- ✅ Section 10 added to versioning cookbook with 10 edge cases and anti-patterns
- ✅ Each entry includes symptom, root cause, corrective pattern, and preventive guidance
- ✅ References to related documentation (error reference guide, root cause analysis)
- ✅ Table of contents updated to include new section
- ✅ Examples and real dev-kit scenarios included

**Acceptance Criteria:**
- [x] Edge cases identified and documented ✅
- [x] Anti-patterns clearly described ✅
- [x] Preventive guidance provided ✅

---

### E3:S02:T05 – Create quick reference summary for users and agents

**Input:**  
- Cookbook content from T02–T04  

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
- [x] Quick reference created ✅
- [x] Covers common scenarios and rules ✅
- [x] Linked from cookbook, dev-kit versioning policy, and relevant READMEs ✅

---

### E3:S02:T06 – Investigate and harden changelog ordering process

**Input:**  
- Issue: Changelog entries appeared in incorrect order (v0.3.2.4+1 before v0.2.4.9+3)
- Canonical ordering principle: Versions must be ordered by version number (RC.EPIC.STORY.TASK+BUILD)
- Policy: `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md` Section 8

**Deliverable:**  
- Root cause analysis of how changelog ordering violation occurred
- Process improvements to prevent future violations
- Validation/automation recommendations

**Approach:**
1. **Root Cause Analysis:**
   - Investigate how RW Step 4 (Update Main Changelog) handles version ordering
   - Check if RW Step 4 reads existing changelog entries before inserting new entry
   - Verify if RW Step 4 compares version numbers to determine insertion point
   - Document the exact sequence that led to incorrect ordering

2. **Process Gap Analysis:**
   - Identify missing validation steps in RW workflow
   - Check if changelog ordering is validated in RW Step 8 (Run Validators)
   - Determine if manual process is required or if automation is possible

3. **Prevention Strategy:**
   - Update RW Step 4 to explicitly validate version ordering
   - Add changelog ordering validation to RW Step 8
   - Create automated validation script if needed
   - Update RW documentation with ordering requirements

4. **Documentation Updates:**
   - Update RW Step 4 instructions to include ordering validation
   - Add changelog ordering to validation checklist
   - Document canonical ordering requirements clearly

**Acceptance Criteria:**
- [x] Root cause analysis completed and documented ✅
- [x] Process gaps identified ✅
- [x] Prevention strategy defined ✅
- [x] RW Step 4 updated with ordering validation ✅
- [x] Validation added to RW Step 8 ✅
- [x] Documentation updated with ordering requirements ✅
- [x] Prevention measures implemented ✅

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


