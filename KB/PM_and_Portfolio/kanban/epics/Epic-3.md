# Epic 3: Numbering & Versioning Framework

**Status:** TODO
**Priority:** HIGH
**Estimated Effort:** [TBD]
**Created:** 2025-12-02
**Last updated:** 2025-12-02 (v0.3.1.2+1 – added T006: Make .cursorrules abstract)
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
**Last updated:** 2025-12-02 (v0.3.1.2+1 – added T006: Make .cursorrules abstract)

**Goal:**
Make sure the dev kit's own versioning policy, version file, and docs align cleanly with the generic versioning framework. Establish `vibe-dev-kit` as the canonical SoT for versioning policies and strategies.

**Tasks:**
- [ ] E3:S01:T001 – Review dev-kit versioning policy vs framework policy
- [ ] E3:S01:T002 – Ingest versioning findings from fynd.deals Epic 15 work
- [ ] E3:S01:T003 – Update dev-kit versioning policy as canonical SoT
- [ ] E3:S01:T004 – Align dev-kit version.py and CHANGELOG with framework
- [ ] E3:S01:T005 – Document consumption pattern for other projects
- [ ] E3:S01:T006 – Make .cursorrules abstract (remove hardcoded version numbers)

> Full story: [`epics/Epic-3/stories/Story-001-dev-kit-alignment-with-versioning-framework.md`](epics/Epic-3/stories/Story-001-dev-kit-alignment-with-versioning-framework.md)

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
