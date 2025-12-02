# Story 002 – FR/BR Intake to Tasks

**Status:** IN PROGRESS  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Created:** 2025-12-02  
**Last updated:** 2025-12-02 (v0.4.2.3+1 – Task 3 complete: Create FR/BR intake templates and forms)
**Version:** v0.4.2.3+1
**Code:** E4S02

---

## Overview

Design and implement a clear, actionable flow for converting incoming Feature Requests (FRs) and Bug Reports (BRs) into Kanban Tasks. This story ensures that all work entering the dev-kit is properly structured, tracked, and aligned with the Kanban → Versioning → Release Workflow system.

---

## Goal

Make it easy and systematic to go from an incoming Feature Request or Bug Report to:
- Task(s) under a Story
- Story under an Epic (creating them when missing)
- Proper versioning alignment (`RC.EPIC.STORY.TASK+BUILD`)

This story operationalizes the FR/BR → Task → Story → Epic rule defined in the Kanban governance policy.

---

## Task Checklist

- [x] **E4:S02:T001 – Analyze current FR/BR intake process and requirements** ✅ COMPLETE
- [x] **E4:S02:T002 – Design FR/BR → Task → Story → Epic decision flow** ✅ COMPLETE
- [x] **E4:S02:T003 – Create FR/BR intake templates and forms** ✅ COMPLETE
- [ ] **E4:S02:T004 – Document the intake process with examples**
- [ ] **E4:S02:T005 – Create intake workflow guide for agents/users**

---

## Tasks

### E4:S02:T001 – Analyze current FR/BR intake process and requirements ✅ COMPLETE

**Input:** Current Kanban governance policy, existing FR/BR examples (if any)  
**Deliverable:** Analysis report documenting current state and requirements ✅ **DELIVERED**  
**Dependencies:** None  
**Blocker:** None

**Status:** ✅ **COMPLETE** - Comprehensive analysis report created

**Approach:**
1. ✅ Reviewed Kanban governance policy FR/BR rules
2. ✅ Identified current gaps in the intake process
3. ✅ Documented requirements for an effective intake flow
4. ✅ Identified stakeholders and use cases

**Key Findings:**
- ✅ Policy exists: FR/BR → Task → Story → Epic flow is defined
- ❌ Process gap: No systematic intake process or templates exist
- ❌ Documentation gap: No step-by-step guide for converting FRs/BRs to Tasks
- ❌ Tooling gap: No templates or forms for FR/BR intake

**Files Created:**
- ✅ `KB/PM_and_Portfolio/kanban/epics/Epic-4/stories/Story-002-fr-br-intake-to-tasks/T001-intake-analysis-report.md` (comprehensive analysis)

**Deliverable:** See [`T001-intake-analysis-report.md`](T001-intake-analysis-report.md) for complete analysis, requirements, use cases, and recommendations.

---

### E4:S02:T002 – Design FR/BR → Task → Story → Epic decision flow ✅ COMPLETE

**Input:** Analysis report from T001  
**Deliverable:** Decision flow diagram and process documentation ✅ **DELIVERED**  
**Dependencies:** E4:S02:T001  
**Blocker:** None

**Status:** ✅ **COMPLETE** - Comprehensive decision flow design created

**Approach:**
1. ✅ Designed decision tree/flowchart for FR/BR intake
2. ✅ Defined criteria for Story matching (scope, Epic alignment, status)
3. ✅ Defined criteria for Epic matching/creation (domain, status, conceptual fit)
4. ✅ Documented edge cases and exceptions (complex FR, ambiguous scope, duplicates, etc.)

**Key Deliverables:**
- ✅ Text-based decision flow diagram (high-level and detailed)
- ✅ Story matching criteria (primary and secondary)
- ✅ Epic matching criteria (primary and secondary)
- ✅ Epic creation guidelines (broad, abstract, examples)
- ✅ Edge case handling (complex FR, ambiguous scope, BR affecting multiple components, etc.)
- ✅ Versioning integration rules
- ✅ Kanban board integration rules
- ✅ Visual decision flow diagram (text-based flowchart)
- ✅ Decision criteria summary table
- ✅ Worked examples (4 scenarios)

**Files Created:**
- ✅ `KB/PM_and_Portfolio/kanban/epics/Epic-4/stories/Story-002-fr-br-intake-to-tasks/T002-decision-flow-design.md` (comprehensive design)

**Deliverable:** See [`T002-decision-flow-design.md`](T002-decision-flow-design.md) for complete decision flow, criteria, edge cases, and examples.

---

### E4:S02:T003 – Create FR/BR intake templates and forms ✅ COMPLETE

**Input:** Decision flow from T002  
**Deliverable:** Templates and forms for FR/BR intake ✅ **DELIVERED**  
**Dependencies:** E4:S02:T002  
**Blocker:** None

**Status:** ✅ **COMPLETE** - FR and BR templates created

**Approach:**
1. ✅ Created FR template/form (`FR_TEMPLATE.md`)
2. ✅ Created BR template/form (`BR_TEMPLATE.md`)
3. ✅ Aligned templates with Kanban templates (EPIC_TEMPLATE, STORY_TEMPLATE)
4. ✅ Included intake decision tracking section
5. ✅ Added versioning and Kanban integration fields

**Key Features:**

**FR Template:**
- Summary and description sections
- Requirements (functional and non-functional)
- Scope analysis (problem domain, affected areas, complexity)
- Use cases
- Acceptance criteria
- Dependencies and related work
- **Intake Decision section** (tracks FR → Task → Story → Epic conversion)
- Kanban links for traceability

**BR Template:**
- Summary and description sections
- Affected component identification
- Steps to reproduce
- Environment details
- Impact assessment (user and business)
- Workaround documentation
- Acceptance criteria (fix requirements)
- **Fix verification status** (aligned with RW verification requirements)
- **Intake Decision section** (tracks BR → Task → Story → Epic conversion)
- Kanban links for traceability

**Template Alignment:**
- Both templates align with EPIC_TEMPLATE and STORY_TEMPLATE structure
- Include intake decision tracking for FR/BR → Task → Story → Epic flow
- Support versioning integration (`RC.EPIC.STORY.TASK+BUILD`)
- Include Kanban links for traceability
- BR template includes fix verification status (aligned with RW requirements)

**Files Created:**
- ✅ `packages/frameworks/kanban/templates/FR_TEMPLATE.md` (Feature Request template)
- ✅ `packages/frameworks/kanban/templates/BR_TEMPLATE.md` (Bug Report template)

**Deliverable:** FR and BR templates are ready for use. Templates include all necessary fields for intake processing and align with the decision flow design from T002.

---

### E4:S02:T004 – Document the intake process with examples

**Input:** Templates from T003, decision flow from T002  
**Deliverable:** Complete intake process documentation with worked examples  
**Dependencies:** E4:S02:T003  
**Blocker:** None

**Approach:**
1. Write step-by-step intake process guide
2. Create worked examples for common scenarios:
   - FR that fits existing Story
   - FR that needs new Story (existing Epic)
   - FR that needs new Epic
   - BR that fits existing Story
   - BR that needs new Story
   - Complex FR requiring multiple Tasks
3. Document integration with versioning and RW

**Files to Create:**
- `packages/frameworks/kanban/FR_BR_INTAKE_GUIDE.md`
- Example scenarios documentation

---

### E4:S02:T005 – Create intake workflow guide for agents/users

**Input:** Process documentation from T004  
**Deliverable:** User-friendly guide for AI agents and human users  
**Dependencies:** E4:S02:T004  
**Blocker:** None

**Approach:**
1. Create agent-friendly guide (for AI assistants)
2. Create user-friendly guide (for human users)
3. Include quick reference/cheat sheet
4. Add troubleshooting section

**Files to Create:**
- `packages/frameworks/kanban/FR_BR_INTAKE_AGENT_GUIDE.md`
- `packages/frameworks/kanban/FR_BR_INTAKE_USER_GUIDE.md`
- Quick reference card

---

## Acceptance Criteria

- [ ] Clear decision flow exists for FR/BR → Task → Story → Epic
- [ ] Templates exist for FR, BR, Story creation, Epic creation
- [ ] Process is documented with worked examples
- [ ] Guides exist for both agents and users
- [ ] Process integrates with versioning (`RC.EPIC.STORY.TASK+BUILD`)
- [ ] Process integrates with Release Workflow

---

## Dependencies

**Coordinates With:**
- Epic 2: Workflow Management Framework (for RW integration)
- Epic 3: Numbering & Versioning Framework (for versioning alignment)
- Epic 1: Vibe Dev Kit Core (for core policies)

---

## References

- `packages/frameworks/kanban/policies/kanban-governance-policy.md` (FR/BR rules)
- `KB/PM_and_Portfolio/rituals/policy/kanban-governance-policy.md` (dev-kit implementation)
- `packages/frameworks/kanban/templates/EPIC_TEMPLATE.md`
- `packages/frameworks/kanban/templates/STORY_TEMPLATE.md`

---

_Last updated: 2025-12-02 (v0.4.2.3+1 – Task 3 complete: Create FR/BR intake templates and forms)_

