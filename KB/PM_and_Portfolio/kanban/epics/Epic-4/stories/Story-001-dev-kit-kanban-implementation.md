# Story 001 – Dev Kit Kanban Implementation

**Status:** TODO  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Created:** 2025-12-02  
**Last updated:** 2025-12-02 (v0.4.1.1+2 – Task 1 complete: Gap analysis of dev-kit Kanban policies and templates)
**Version:** v0.4.1.1+2  
**Code:** E4S01

---

## Overview

Fully align the dev-kit Kanban board, stories, and governance policy with the Kanban framework package. This story ensures that `vibe-dev-kit` serves as the **single point of truth (SoT)** for Kanban policies, templates, and governance, which other projects (like `fynd.deals`) can copy and adapt.

---

## Goal

Establish `vibe-dev-kit` as the canonical source for Kanban framework policies, templates, and governance. Ensure that findings from real-world implementations (e.g., `fynd.deals` Epic 15) are captured and refined into reusable framework components.

---

## Task Checklist

- [x] **E4:S01:T001 – Review existing dev-kit Kanban policies and templates** ✅ COMPLETE
- [ ] **E4:S01:T002 – Ingest findings from fynd.deals Epic 15 Kanban work into dev-kit**
- [ ] **E4:S01:T003 – Update dev-kit Kanban governance policy as canonical SoT**
- [ ] **E4:S01:T004 – Align dev-kit Kanban templates with updated governance**
- [ ] **E4:S01:T005 – Document consumption pattern for other projects**

---

## Tasks

### E4:S01:T001 – Review existing dev-kit Kanban policies and templates ✅ COMPLETE

**Input:** Current dev-kit Kanban framework files  
**Deliverable:** Gap analysis report ✅ **DELIVERED**  
**Dependencies:** None  
**Blocker:** None

**Status:** ✅ **COMPLETE** - Gap analysis documented in `T001-gap-analysis-report.md`

**Approach:**
1. ✅ Reviewed `packages/frameworks/kanban/policies/kanban-governance-policy.md`
2. ✅ Reviewed `KB/PM_and_Portfolio/rituals/policy/kanban-governance-policy.md`
3. ✅ Reviewed `packages/frameworks/kanban/templates/EPIC_TEMPLATE.md`
4. ✅ Reviewed `packages/frameworks/kanban/templates/STORY_TEMPLATE.md`
5. ✅ Reviewed `packages/frameworks/kanban/README.md`
6. ✅ Compared framework policy with dev-kit policy
7. ✅ Compared framework templates with dev-kit usage
8. ✅ Documented gaps and inconsistencies

**Key Findings:**
- **7 critical gaps identified:** Atomic RW behaviour, "ALL sections" update requirement, accessibility constraints, forensic marker format standardization, consistency requirements, review schedules, escalation procedures
- **Template gaps:** Missing "ALL sections" update requirement notes, forensic marker format standardization notes, consistency check reminders
- **Dev-kit policy gaps:** Missing framework principles (Harmonious Cycle, detailed FR/BR flow, Task-Level Requirements, Release Workflow documentation)

**Deliverable:** See [`T001-gap-analysis-report.md`](T001-gap-analysis-report.md) for complete gap analysis report.

**Files Reviewed:**
- ✅ `packages/frameworks/kanban/policies/kanban-governance-policy.md`
- ✅ `KB/PM_and_Portfolio/rituals/policy/kanban-governance-policy.md`
- ✅ `packages/frameworks/kanban/templates/EPIC_TEMPLATE.md`
- ✅ `packages/frameworks/kanban/templates/STORY_TEMPLATE.md`
- ✅ `packages/frameworks/kanban/README.md`

---

### E4:S01:T002 – Ingest findings from fynd.deals Epic 15 Kanban work into dev-kit

**Input:** fynd.deals Epic 15 Kanban documentation  
**Deliverable:** Summary of reusable patterns and findings  
**Dependencies:** E4:S01:T001  
**Blocker:** None

**Approach:**
1. Review `fynd.deals/docs/fynd_deals/_design/documentation/KANBAN-WORKFLOW.md`
2. Review `fynd.deals/docs/fynd_deals/_design/documentation/KANBAN-TEMPLATES.md`
3. Review `fynd.deals/docs/fynd_deals/_design/documentation/KANBAN-GOVERNANCE.md`
4. Extract reusable patterns, especially:
   - Atomic RW + "ALL sections" update rules
   - Accessibility constraints and blocked/aborted RW behaviour
   - Forensic marker requirements and consistency checks
   - Review schedules and maintenance responsibilities
5. Document findings and recommendations

**Source Files (from fynd.deals):**
- `docs/fynd_deals/_design/documentation/KANBAN-WORKFLOW.md`
- `docs/fynd_deals/_design/documentation/KANBAN-TEMPLATES.md`
- `docs/fynd_deals/_design/documentation/KANBAN-GOVERNANCE.md`
- `docs/fynd_deals/_design/documentation/KANBAN-EPIC-AUDIT-REPORT.md`

**Key Patterns to Capture:**
- Atomic RW behaviour: RW must complete all 10 steps or stop with explicit BLOCKED message
- "ALL sections" rule: Epic docs must update header, Story Checklist, AND detailed story sections
- Accessibility constraints: No partial updates, no silent failures, clear actionable messages
- Forensic marker format: `✅ COMPLETE (vRC.E.S.T+B)` canonical format
- Consistency requirements: Kanban Board ↔ Epic ↔ Story must all align

---

### E4:S01:T003 – Update dev-kit Kanban governance policy as canonical SoT

**Input:** Findings from T001 and T002  
**Deliverable:** Updated canonical Kanban governance policy  
**Dependencies:** E4:S01:T001, E4:S01:T002  
**Blocker:** None

**Approach:**
1. Refine `packages/frameworks/kanban/policies/kanban-governance-policy.md` to embed:
   - Atomic RW behaviour and no-partial-updates rule
   - Accessibility/agent-behaviour requirements
   - Epic/Story/Task + forensic marker integration
   - Review schedules and maintenance responsibilities
   - Escalation procedures
2. Ensure `KB/PM_and_Portfolio/rituals/policy/kanban-governance-policy.md` clearly points at the framework policy as the SoT
3. Document the relationship between framework policy (SoT) and project-specific adaptations

**Files to Update:**
- `packages/frameworks/kanban/policies/kanban-governance-policy.md` (primary SoT)
- `KB/PM_and_Portfolio/rituals/policy/kanban-governance-policy.md` (dev-kit local policy, references framework)

**Key Sections to Add/Enhance:**
- Governance principles (single source of truth, forensic traceability, atomic updates, consistency first)
- Atomic RW behaviour (complete all steps or explicit BLOCKED state)
- "ALL sections" update requirement (header, checklist, detailed sections)
- Accessibility constraints (no partial updates, clear actionable messages)
- Review schedules (weekly, monthly, quarterly)
- Escalation procedures (Level 1-3)

---

### E4:S01:T004 – Align dev-kit Kanban templates with updated governance

**Input:** Updated governance policy from T003  
**Deliverable:** Updated Kanban templates  
**Dependencies:** E4:S01:T003  
**Blocker:** None

**Approach:**
1. Update `packages/frameworks/kanban/templates/EPIC_TEMPLATE.md` to encode:
   - Required metadata (status, priority, dates, version, branch)
   - Story Checklist with version markers
   - Explicit "ALL sections" update requirements for RW
   - Forensic marker format requirements
2. Update `packages/frameworks/kanban/templates/STORY_TEMPLATE.md` to encode:
   - Required metadata (status, priority, dates, version, code)
   - Task Checklist with forensic markers
   - Explicit forensic marker format: `✅ COMPLETE (vRC.E.S.T+B)`
   - "ALL sections" update requirements
3. Ensure templates align with governance principles

**Files to Update:**
- `packages/frameworks/kanban/templates/EPIC_TEMPLATE.md`
- `packages/frameworks/kanban/templates/STORY_TEMPLATE.md`

**Template Enhancements:**
- Explicit forensic marker format in task checklists
- Notes about "ALL sections" update requirements
- Version metadata requirements
- Consistency check reminders

---

### E4:S01:T005 – Document consumption pattern for other projects

**Input:** Updated policies and templates from T003-T004  
**Deliverable:** Consumption documentation  
**Dependencies:** E4:S01:T003, E4:S01:T004  
**Blocker:** None

**Approach:**
1. Update `packages/frameworks/kanban/README.md` to document:
   - Projects MUST **copy** policies/templates from `vibe-dev-kit`
   - They then customize paths/names, but keep the **governance + atomicity rules** intact
   - `vibe-dev-kit` remains the single point of truth for future updates
2. Create/update integration guides showing:
   - How to copy Kanban framework into a new project
   - What can be customized vs what must remain unchanged
   - How to stay aligned with framework updates
3. Document the relationship between framework (SoT) and project implementations

**Files to Update/Create:**
- `packages/frameworks/kanban/README.md` (add consumption section)
- `packages/frameworks/kanban/guides/` (create consumption guide if needed)

**Key Documentation Points:**
- Copy, don't reference: Projects must copy files, not link to `vibe-dev-kit`
- Customization boundaries: What can be customized (paths, names) vs what must stay (governance rules, atomicity)
- Update process: How to pull framework updates into projects
- SoT relationship: `vibe-dev-kit` is the canonical source

---

## Acceptance Criteria

- [ ] Dev-kit Kanban governance policy is the canonical SoT
- [ ] Policies capture atomic RW behaviour and accessibility constraints
- [ ] Templates encode forensic markers and "ALL sections" requirements
- [ ] Consumption pattern is clearly documented
- [ ] Framework and project implementations are clearly distinguished

---

## Dependencies

**Coordinates With:**
- Epic 3: Numbering & Versioning Framework (for versioning integration)
- Epic 2: Workflow Management Framework (for RW integration)

---

## References

- `packages/frameworks/kanban/README.md`
- `packages/frameworks/kanban/policies/kanban-governance-policy.md`
- `packages/frameworks/kanban/templates/EPIC_TEMPLATE.md`
- `packages/frameworks/kanban/templates/STORY_TEMPLATE.md`
- `KB/PM_and_Portfolio/rituals/policy/kanban-governance-policy.md`
- Source: `fynd.deals/docs/fynd_deals/_design/documentation/KANBAN-*.md`

---

_Last updated: 2025-12-02 (v0.4.1.1+2 – Task 1 complete)_

