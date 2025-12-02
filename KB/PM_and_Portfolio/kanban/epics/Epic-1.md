# Epic 1: Vibe Dev Kit Core

**Status:** IN PROGRESS  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Created:** 2025-12-02  
**Last updated:** 2025-12-02 (v0.1.2.5+1 – Task 5 complete: Package READMEs updated with modularity information)  
**Branch:** `epic/1-vibe-dev-kit-core`  
**Version Schema:** `0.1.S.T+B` (dev-kit RC.EPIC.STORY.TASK+BUILD)  
**Production URL:** [N/A for this repo]

---

## Story Checklist

- [x] **E1:S01 – Dev Kit Versioning & RW Behaviour** - COMPLETE ✅ (v0.1.1.1+1, E2:S01:T002, E2:S01:T003)  
- [x] **E1:S02 – Package & Repo Architecture** - COMPLETE ✅ (v0.1.2.5+1)
  - Tasks: T001 ✅ (v0.1.2.1+1), T002 ✅ (v0.1.2.2+1), T003 ✅ (v0.1.2.3+1), T004 ✅ (v0.1.2.4+1), T005 ✅ (v0.1.2.5+1)
  - Story: [`epics/Epic-1/stories/Story-002-package-and-repo-architecture.md`](epics/Epic-1/stories/Story-002-package-and-repo-architecture.md)  
- [ ] **E1:S03 – Core KB Structure for Dev Kit** - TODO  

---

## Overview

Epic 1 establishes the **core infrastructure and conventions** for the Vibe Dev Kit repository.  
It defines how the repo is structured, how versioning works for the dev kit itself, and how Release Workflow (RW) should behave when run *inside this repo* rather than inside an application project.

---

## Goals

1. **Define dev-kit versioning policy**  
   - Document how `RC.EPIC.STORY.TASK+BUILD` applies to dev-kit Epics, Stories, and Tasks.  
   - Ensure `version.py`, CHANGELOG, and RW docs all reflect this policy.

2. **Clarify modular architecture**  
   - Make it easy for users to consume **individual frameworks** (workflow mgt, versioning, kanban) without pulling in the whole repo.  

3. **Provide a solid KB foundation**  
   - Establish core KB locations for architecture, PM & portfolio, and dev-kit governance.

---

## Stories

### Story 1: Dev Kit Versioning & RW Behaviour

**Status:** COMPLETE  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Last updated:** 2025-12-02 (v0.1.1.1+2 – Documentation restructured to industry-standard templates)  

**Goal:**  
Define and implement how the dev kit uses `RC.EPIC.STORY.TASK+BUILD`, and how RW interprets versions and tasks when run in this repo.

**Tasks:**
- [x] E1:S01:T001 – Create `dev-kit-versioning-policy.md` ✅ COMPLETE (v0.1.1.1+1)  
- [x] E1:S01:T002 – Align `version.py` and CHANGELOG with dev-kit policy ✅ COMPLETE (v0.1.1.1+1)  
- [x] E1:S01:T003 – Update RW docs to distinguish dev-kit vs external examples ✅ COMPLETE (completed in E2:S01:T002 and E2:S01:T003)  

**Acceptance Criteria:**
- [x] Dev-kit versioning policy exists and is referenced by other docs ✅  
- [x] `version.py` encodes a real dev-kit Epic/Story/Task, not legacy external IDs ✅  
- [x] RW docs clarify dev-kit vs Confidentia/fynd.deals examples ✅

> Full story: `KB/PM_and_Portfolio/kanban/epics/Epic-1/stories/Story-001-vibe-dev-kit-kanban-and-versioning.md`

---

### Story 2: Package & Repo Architecture

**Status:** IN PROGRESS  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Last updated:** 2025-12-02 (v0.1.2.5+1 – Task 5 complete: Package READMEs updated with modularity information)

**Goal:**  
Clarify the modular architecture of the `vibe-dev-kit` repository, ensuring that users can easily consume individual frameworks (workflow mgt, versioning, kanban) without pulling in the entire repository.

**Tasks:**
- [x] E1:S02:T001 – Analyze current package structure and dependencies ✅ COMPLETE (v0.1.2.1+1)
- [x] E1:S02:T002 – Document modularity principles and boundaries ✅ COMPLETE (v0.1.2.2+1)
- [x] E1:S02:T003 – Create package dependency matrix ✅ COMPLETE (v0.1.2.3+1)
- [x] E1:S02:T004 – Document consumption patterns for each framework ✅ COMPLETE (v0.1.2.4+1)
- [ ] E1:S02:T005 – Update package READMEs with modularity information

> Full story: [`epics/Epic-1/stories/Story-002-package-and-repo-architecture.md`](epics/Epic-1/stories/Story-002-package-and-repo-architecture.md)

---

## Dependencies

**Blocks:**
- Clear versioning for future epics (2–4 and beyond)  
- Accurate forensic markers in dev-kit-specific examples  

**Blocked By:**
- None at initial creation.

**Coordinates With:**
- Epic 2: Workflow Management Framework  
- Epic 3: Numbering & Versioning Framework  
- Epic 4: Kanban Framework  

---

## Risks & Mitigations

- Risk: Confusion between dev-kit versions and external-project versions.  
  - Mitigation: Always label external examples as such; centralise dev-kit policy.

- Risk: Over-complexity for early adopters of the dev kit.  
  - Mitigation: Provide clear, minimal “start here” examples and keep advanced details in separate docs.

---

## References

- `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md`  
- `packages/frameworks/workflow mgt/README.md`  
- `packages/frameworks/numbering & versioning/README.md`  
- `packages/frameworks/kanban/README.md`  
- `KB/PM_and_Portfolio/kanban/README.md` (Kanban structure)  

---

## Maintenance Cadence

- **Quarterly:** Review dev-kit versioning policy and RW behaviour.  
- **As Needed:** Update epic stories and tasks as new core capabilities are added.


