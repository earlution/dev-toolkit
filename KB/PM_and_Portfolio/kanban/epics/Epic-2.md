# Epic 2: Workflow Management Framework

**Status:** IN PROGRESS  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Created:** 2025-12-02  
**Last updated:** 2025-12-03 (v0.2.3.6+1 – Stories 1–3 complete, Story 4 TODO)  
**Branch:** `epic/2-workflow-management-framework`  
**Version Schema:** `0.2.S.T+B`  
**Production URL:** [N/A for this repo]

---

## Story Checklist

- [x] **E2:S01 – RW Agent Execution & Docs** - COMPLETE ✅ (v0.2.1.1+5)  
  - Story: [`epics/Epic-2/stories/Story-001-rw-agent-execution-and-docs.md`](epics/Epic-2/stories/Story-001-rw-agent-execution-and-docs.md)  
- [x] **E2:S02 – PDCA Integration into Release Workflow** - COMPLETE ✅ (v0.2.2.8+1 – All tasks complete)  
  - Story: [`epics/Epic-2/stories/Story-002-pdca-integration-into-release-workflow.md`](epics/Epic-2/stories/Story-002-pdca-integration-into-release-workflow.md)
- [x] **E2:S03 – Additional Workflows & Examples** - COMPLETE ✅ (v0.2.3.6+1 – All tasks complete)  
- [ ] **E2:S04 – RW Installer & Plug-and-Play Adoption** - IN PROGRESS (v0.2.4.5+2 – T05 build 2: RW config-driven philosophy aligned)  
  - Story: [`epics/Epic-2/stories/Story-004-rw-installer-and-plug-and-play-adoption.md`](epics/Epic-2/stories/Story-004-rw-installer-and-plug-and-play-adoption.md)  

---

## Overview

Epic 2 owns the **Workflow Management framework** living under `packages/frameworks/workflow mgt/`.

It defines how Release Workflow (RW) and other workflows are:

- Documented (agent execution guides, references)
- Integrated with `.cursorrules` and Cursor behaviour
- Used as **portable templates** in other projects

---

## Goals

1. **Document RW agent execution clearly and portably**  
   - Make `release-workflow-agent-execution.md` fully template-ready.  
   - Ensure examples are clearly labelled as dev-kit vs external.

2. **Add non-release workflow examples**  
   - Provide additional workflows (e.g., refactor, migration) that follow the same ANALYZE → DETERMINE → EXECUTE → VALIDATE → PROCEED pattern.

3. **Clarify RW-as-template behaviour**  
   - Document how RW should be customised when imported into a new project.

---

## Stories (Initial)

### Story 1: RW Agent Execution & Docs

**Status:** COMPLETE ✅  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Last updated:** 2025-12-02 (v0.2.1.1+5 – All tasks complete)  

**Goal:**  
Make RW agent execution documentation fully portable, clearly distinguishing dev-kit behaviour from external examples.

**Tasks:**
- [x] E2:S01:T001 – Audit `release-workflow-agent-execution.md` for project-specific assumptions ✅ COMPLETE (v0.2.1.1+3)
- [x] E2:S01:T002 – Tag Confidentia/fynd.deals examples and add dev-kit examples ✅ COMPLETE (v0.2.1.1+4)
- [x] E2:S01:T003 – Align `.cursorrules` RW trigger section with dev-kit policy ✅ COMPLETE (v0.2.1.1+5)
- [x] E2:S01:T004 – Update RW changelog step to require verification before marking fixes as "fixed" ✅ COMPLETE (v0.2.1.1+2)

> Full story: [`epics/Epic-2/stories/Story-001-rw-agent-execution-and-docs.md`](epics/Epic-2/stories/Story-001-rw-agent-execution-and-docs.md)  

---

## Dependencies

**Blocks:**
- Clear documentation for users who import the workflow mgt package into their projects.

**Blocked By:**
- Epic 1 Story 1 (dev-kit versioning & RW behaviour) for some cross-references.

**Coordinates With:**
- Epic 3: Numbering & Versioning Framework  
- Epic 4: Kanban Framework  

---

## Risks & Mitigations

- Risk: RW docs feel tied to a single project.  
  - Mitigation: Aggressive labelling and separation of project-specific vs framework-level content.

---

## References

- `packages/frameworks/workflow mgt/README.md`  
- `packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md`  
- `.cursorrules` RW trigger section (when added to this repo)  


