# Epic 4: Kanban Framework

**Status:** TODO  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Created:** 2025-12-02  
**Last updated:** 2025-12-02 (v0.4.1.1+1 – initial epic definition)  
**Branch:** `epic/4-kanban-framework`  
**Version Schema:** `0.4.S.T+B`  
**Production URL:** [N/A for this repo]

---

## Story Checklist

- [ ] **E4:S01 – Dev Kit Kanban Implementation** - TODO  
- [ ] **E4:S02 – FR/BR Intake to Tasks** - TODO  
- [ ] **E4:S03 – Kanban + Versioning + RW Integration** - TODO  

---

## Overview

Epic 4 owns the **Kanban framework** (`packages/frameworks/kanban/`) and its concrete application inside this repo:

- Kanban board under `KB/PM_and_Portfolio/kanban/_index.md`
- Story files under `KB/PM_and_Portfolio/kanban/stories/`
- Kanban governance policy for this repo

It ensures that:

- All substantive work is **Task/FR-driven**.
- Kanban, versioning, and RW form a coherent system.

---

## Goals

1. **Implement dev-kit Kanban using the framework**  
   - Align local Kanban policy with the framework policy.
   - Adopt the FR/BR → Task → Story → Epic rule in practice.

2. **Design FR/BR intake flow**  
   - Make it easy to go from an incoming Feature Request or Bug Report to:
     - Task(s) under a Story
     - Story under an Epic (creating them when missing)

3. **Clarify Kanban + Versioning + RW integration**  
   - Show how Tasks map to `TASK` in versions.
   - Show how RW updates Kanban docs and forensic markers.

---

## Stories (Initial)

### Story 1: Dev Kit Kanban Implementation

**Status:** TODO  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Last updated:** [YYYY-MM-DD] (v0.4.1.1+1 – [summary])  

**Goal:**  
Fully align the dev-kit Kanban board, stories, and governance policy with the Kanban framework package.

**Tasks (examples):**
- [ ] E4:S01:T001 – Review dev-kit Kanban policy vs framework policy  
- [ ] E4:S01:T002 – Introduce E/S/T numbering for Tasks where appropriate  
- [ ] E4:S01:T003 – Document how to add new dev-kit Stories and Tasks consistently  

---

## Dependencies

**Blocks:**
- Clear, reusable Kanban implementation for dev-kit work.

**Blocked By:**
- Epic 1 and Epic 3 for some versioning and core-policy decisions.

**Coordinates With:**
- Epic 1: Vibe Dev Kit Core  
- Epic 2: Workflow Management Framework  
- Epic 3: Numbering & Versioning Framework  

---

## References

- `packages/frameworks/kanban/README.md`  
- `packages/frameworks/kanban/policies/kanban-governance-policy.md`  
- `KB/PM_and_Portfolio/rituals/policy/kanban-governance-policy.md`  
- `KB/PM_and_Portfolio/kanban/_index.md`  


