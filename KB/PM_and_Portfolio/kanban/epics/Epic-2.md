# Epic 2: Workflow Management Framework

**Status:** TODO  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Created:** 2025-12-02  
**Last updated:** 2025-12-02 (v0.2.1.1+1 – initial epic definition)  
**Branch:** `epic/2-workflow-management-framework`  
**Version Schema:** `0.2.S.T+B`  
**Production URL:** [N/A for this repo]

---

## Story Checklist

- [ ] **E2:S01 – RW Agent Execution & Docs** - TODO  
  - Story: [`epics/Epic-2/stories/Story-001-rw-agent-execution-and-docs.md`](epics/Epic-2/stories/Story-001-rw-agent-execution-and-docs.md)  
- [ ] **E2:S02 – Additional Workflows & Examples** - TODO  
- [ ] **E2:S03 – RW Behaviour When Used as a Template** - TODO  

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

**Status:** TODO  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Last updated:** [YYYY-MM-DD] (v0.2.1.1+1 – [summary])  

**Goal:**  
Make RW agent execution documentation fully portable, clearly distinguishing dev-kit behaviour from external examples.

**Tasks:**
- [ ] E2:S01:T001 – Audit `release-workflow-agent-execution.md` for project-specific assumptions  
- [ ] E2:S01:T002 – Tag Confidentia/fynd.deals examples and add dev-kit examples  
- [ ] E2:S01:T003 – Align `.cursorrules` RW trigger section with dev-kit policy
- [ ] E2:S01:T004 – Update RW changelog step to require verification before marking fixes as "fixed"

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


