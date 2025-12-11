---
lifecycle: evergreen
ttl_days: null
created_at: 2025-01-27T00:00:00Z
expires_at: null
housekeeping_policy: keep
---

# Kanban Migration Analysis - Pre-Existing Structure

**Date:** 2025-01-27  
**Issue:** ai-dev-kit Kanban framework assumes fresh install, but dev-toolkit has pre-existing Kanban structure  
**Status:** ANALYSIS IN PROGRESS

---

## Problem Statement

The ai-dev-kit Kanban framework installation process assumes:
- ✅ Fresh project with no existing Kanban structure
- ✅ Clean slate for Epic/Story/Task setup
- ✅ No migration needed from existing systems

**Reality for dev-toolkit:**
- ❌ Pre-existing Kanban structure (Epic 1 with 2 complete stories)
- ❌ Framework examples mixed with project epics (Epic-2 through Epic-9 are framework examples)
- ❌ No migration path from existing structure to new framework structure
- ❌ Framework would overwrite existing work if installed naively

---

## Current State Analysis

### Existing Structure

**Dev-Toolkit Epic:**
- Epic 1: Tool Management and Registry System
  - Story 1: Tool Management System (COMPLETE v0.1.1.1+1)
  - Story 2: Tool Distribution Strategy (COMPLETE v0.1.2.1+1)
  - Location: `KB/PM_and_Portfolio/kanban/epics/Epic-1/`

**Framework Examples (Mixed In):**
- Epic 2-9: ai-dev-kit framework examples
- Location: `KB/PM_and_Portfolio/kanban/epics/Epic-2/` through `Epic-9/`
- These are documentation examples, not dev-toolkit project epics

### Framework Files

**Framework Location:** `packages/frameworks/kanban/`
- Templates: `templates/EPIC_TEMPLATE.md`, `STORY_TEMPLATE.md`
- Canonical Epics: `templates/CANONICAL_EPICS.md` (now updated with all 21 epics)
- Policies: `policies/kanban-governance-policy.md`
- Examples: `examples/Epic-4-Example.md`, etc.

**Framework Installation Process:**
- Manual copy-paste (no automated installer)
- Assumes fresh `KB/PM_and_Portfolio/kanban/` directory
- No detection of existing Kanban structures
- No migration utilities

---

## Gap Analysis

### Gap 1: No Pre-Existing Structure Detection

**Expected:** Framework should detect existing Kanban structure  
**Current:** Framework assumes clean slate  
**Impact:** Risk of overwriting existing work

### Gap 2: No Migration Path

**Expected:** Framework should provide migration from existing Kanban to E/S/T structure  
**Current:** No migration utilities or guides  
**Impact:** Manual migration required, error-prone

### Gap 3: No Uninstall Process

**Expected:** Framework should support uninstalling/reinstalling  
**Current:** No uninstall process defined  
**Impact:** Cannot safely reinstall framework

### Gap 4: Mixed Structure Handling

**Expected:** Framework should handle mixed structures (project epics + framework examples)  
**Current:** No distinction between project epics and framework examples  
**Impact:** Confusion about what belongs to project vs framework

---

## Migration Strategy

### Phase 1: Backup ✅ COMPLETE

- Current structure backed up to `_backup-pre-migration/`
- 91 files preserved
- Complete directory structure maintained

### Phase 2: Framework Installation

**Question:** Do we need to uninstall first?

**Analysis:**
- Framework files are in `packages/frameworks/kanban/` (already present)
- Project Kanban structure is in `KB/PM_and_Portfolio/kanban/`
- These are separate - framework doesn't need "uninstalling"
- But we need to ensure fresh install doesn't overwrite existing structure

**Decision:** 
- Framework files already present (no uninstall needed)
- Need to install fresh Kanban structure WITHOUT overwriting existing Epic 1
- Use separate location or careful installation

### Phase 3: Task Migration

**Current Tasks to Migrate:**
- Epic 1, Story 1, Task 1: Tool Management System (COMPLETE)
- Epic 1, Story 2, Tasks 1-3: Tool Distribution Strategy (COMPLETE)

**Migration Mapping:**
- Existing Epic 1 → New Epic 1 (same epic, but using canonical template structure)
- Existing Stories → Map to new Story structure
- Existing Tasks → Map to new Task structure

### Phase 4: Documentation

**Deliverables:**
- BR: Bug report for missing migration support
- FR: Feature request for migration utilities
- UXR: User experience research on migration scenarios

---

## Next Steps

1. ✅ Backup complete
2. ⏳ Analyze framework installation process
3. ⏳ Install fresh Kanban structure (preserving Epic 1)
4. ⏳ Migrate existing tasks to new structure
5. ⏳ Document gaps and create BR/FR/UXR

---

**Last Updated:** 2025-01-27  
**Status:** ANALYSIS IN PROGRESS

