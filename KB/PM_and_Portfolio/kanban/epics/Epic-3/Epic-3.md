---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-04T12:01:47Z
expires_at: null
housekeeping_policy: keep
---

# Epic 3: Numbering & Versioning Framework

**Status:** IN PROGRESS
**Priority:** HIGH
**Estimated Effort:** [TBD]
**Created:** 2025-12-02
**Last updated:** 2025-12-07 (v0.3.2.7+1 – Story 2 T07 added: Dual-versioning package manager documentation)
**Branch:** `epic/3-numbering-and-versioning-framework`
**Version Schema:** `0.3.S.T+B`
**Production URL:** [N/A for this repo]

---

## Story Checklist

- [x] **E3:S01 – Dev Kit Alignment with Versioning Framework** - COMPLETE ✅ (v0.3.1.6+1)
- [ ] **E3:S02 – Versioning Cookbook & Examples** - IN PROGRESS (v0.3.2.7+1 – T07 added: Dual-versioning package manager documentation)
- [x] **E3:S03 – Versioning Integration with Kanban & RW** - COMPLETE ✅ (v0.3.3.6+2 – All tasks complete: Epic 3 marked COMPLETE)
  - Story: [`Story-003-versioning-integration-with-kanban-and-rw.md`](Story-003-versioning-integration-with-kanban-and-rw.md)

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

**Status:** COMPLETE
**Priority:** HIGH
**Estimated Effort:** [TBD]
**Last updated:** 2025-12-02 (v0.3.1.6+1 – Task 6 complete: Cursorrules abstracted (removed hardcoded version numbers))

**Goal:**
Make sure the dev kit's own versioning policy, version file, and docs align cleanly with the generic versioning framework. Establish `ai-dev-kit` as the canonical SoT for versioning policies and strategies.

**Tasks:**
- [x] E3:S01:T01 – Review dev-kit versioning policy vs framework policy ✅ COMPLETE (v0.3.1.1+2)
- [x] E3:S01:T02 – Ingest versioning findings from fynd.deals Epic 15 work ✅ COMPLETE (v0.3.1.2+1)
- [x] E3:S01:T03 – Update dev-kit versioning policy as canonical SoT ✅ COMPLETE (v0.3.1.3+1)
- [x] E3:S01:T04 – Align dev-kit version.py and CHANGELOG with framework ✅ COMPLETE (v0.3.1.4+1)
- [x] E3:S01:T05 – Document consumption pattern for other projects ✅ COMPLETE (v0.3.1.5+1)
- [x] E3:S01:T06 – Make .cursorrules abstract (remove hardcoded version numbers) ✅ COMPLETE (v0.3.1.6+1)

> Full story: [`Story-001-dev-kit-alignment-with-versioning-framework.md`](Story-001-dev-kit-alignment-with-versioning-framework.md)

---

### Story 2: Versioning Cookbook & Examples

**Status:** IN PROGRESS  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Last updated:** 2025-12-07 (v0.3.2.7+1 – T07 added: Dual-versioning package manager documentation)

**Goal:**  
Provide a practical versioning cookbook with worked examples for RC.EPIC.STORY.TASK+BUILD, making it easy for other projects to adopt the dev-kit versioning strategy safely and correctly.

**Tasks:**
- [x] E3:S02:T01 – Define core versioning scenarios for the cookbook ✅ COMPLETE (v0.3.2.1+1)
- [x] E3:S02:T02 – Create versioning cookbook document with worked examples ✅ COMPLETE (v0.3.2.2+1)
- [x] E3:S02:T03 – Add cross-framework examples (Kanban + Versioning + RW) ✅ COMPLETE (v0.3.2.3+1)
- [x] E3:S02:T04 – Document edge cases and anti-patterns ✅ COMPLETE (v0.3.2.4+1)
- [x] E3:S02:T05 – Create quick reference summary for users and agents ✅ COMPLETE (v0.3.2.5+1)
- [x] E3:S02:T06 – Investigate and harden changelog ordering process 🔄 PERPETUAL (v0.3.2.6+1)
- [x] E3:S02:T07 – Create dual-versioning guide for package manager compatibility ✅ COMPLETE (v0.3.2.7+1)
- [x] E3:S02:T08 – Audit dual-versioning application across packages and propose strategy ✅ COMPLETE (v0.3.2.8+1)
- [x] E3:S02:T09 – Implement Package Version Workflow (PVW) with agentic execution ✅ COMPLETE (v0.3.2.9+1)
- [ ] E3:S02:T10 – Integrate PVW into Release Workflow agent execution guide - TODO

> Full story: [`Story-002-versioning-cookbook-and-examples.md`](Story-002-versioning-cookbook-and-examples.md)

---

### Story 3: Versioning Integration with Kanban & RW

**Status:** COMPLETE ✅  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Last updated:** 2025-12-05 (v0.3.3.6+1 – All tasks complete: Story 3 complete with RW Step 6 for BR/FR fix attempt history)

**Goal:**  
Create comprehensive, framework-level integration documentation that explains how the Numbering & Versioning framework integrates with the Kanban and Workflow Management frameworks. Unlike E4:S03 (which validated dev-kit implementation), this story focuses on **portable, template-ready documentation** that external projects can use to integrate all three frameworks.

**Tasks:**
- [x] E3:S03:T01 – Review existing framework-level integration documentation ✅ COMPLETE (v0.3.3.1+1)
- [x] E3:S03:T02 – Create comprehensive framework-level integration guide ✅ COMPLETE (v0.3.3.2+1)
- [x] E3:S03:T03 – Document integration patterns and best practices ✅ COMPLETE (v0.3.3.3+1)
- [x] E3:S03:T04 – Create integration examples for external projects ✅ COMPLETE (v0.3.3.4+1)
- [x] E3:S03:T05 – Document integration troubleshooting and common issues ✅ COMPLETE (v0.3.3.5+1)
- [x] E3:S03:T06 – Add RW Step 6: Update BR/FR Docs with fix attempt history ✅ COMPLETE (v0.3.3.6+1)

> Full story: [`Story-003-versioning-integration-with-kanban-and-rw.md`](Story-003-versioning-integration-with-kanban-and-rw.md)

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
