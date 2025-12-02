# Epic 3: Numbering & Versioning Framework

**Status:** TODO  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Created:** 2025-12-02  
**Last updated:** 2025-12-02 (v0.3.1.1+1 – initial epic definition)  
**Branch:** `epic/3-numbering-and-versioning-framework`  
**Version Schema:** `0.3.S.T+B`  
**Production URL:** [N/A for this repo]

---

## Story Checklist

- [ ] **E3:S01 – Dev Kit Alignment with Versioning Framework** - TODO  
- [ ] **E3:S02 – Versioning Cookbook & Examples** - TODO  
- [ ] **E3:S03 – Versioning Integration with Kanban & RW** - TODO  

---

## Overview

Epic 3 owns the **Numbering & Versioning framework** living under `packages/frameworks/numbering & versioning/`.

It ensures the dev kit:

- Uses the RC.EPIC.STORY.TASK+BUILD schema consistently.
- Provides clear guidance on how to adopt the schema in new projects.
- Integrates versioning with Kanban and workflows.

---

## Goals

1. **Align dev kit with the framework policy**  
   - Ensure `dev-kit-versioning-policy.md` is coherent with the generic `versioning-policy.md` and `versioning-strategy.md`.

2. **Provide a versioning cookbook**  
   - Show worked examples for:
     - New Epic
     - New Story
     - New Task
     - Bugfix / hotfix
     - Parallel epics

3. **Clarify integration points**  
   - Describe how Kanban Tasks and RW steps map to version components.

---

## Stories (Initial)

### Story 1: Dev Kit Alignment with Versioning Framework

**Status:** TODO  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Last updated:** [YYYY-MM-DD] (v0.3.1.1+1 – [summary])  

**Goal:**  
Make sure the dev kit’s own versioning policy, version file, and docs align cleanly with the generic versioning framework.

**Tasks (examples):**
- [ ] E3:S01:T001 – Review `dev-kit-versioning-policy.md` vs `versioning-policy.md`  
- [ ] E3:S01:T002 – Adjust examples to avoid legacy/conflicting epics  
- [ ] E3:S01:T003 – Document “dev-kit as framework consumer” pattern  

---

## Dependencies

**Blocks:**
- Clear dev-kit story for how to use versioning framework in other projects.

**Blocked By:**
- Epic 1 Story 1 (dev-kit versioning & RW behaviour).

**Coordinates With:**
- Epic 2: Workflow Management Framework  
- Epic 4: Kanban Framework  

---

## References

- `packages/frameworks/numbering & versioning/README.md`  
- `packages/frameworks/numbering & versioning/versioning-policy.md`  
- `packages/frameworks/numbering & versioning/versioning-strategy.md`  
- `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md`  


