---
lifecycle: evergreen
ttl_days: null
created_at: 2025-01-27T00:00:00Z
expires_at: null
housekeeping_policy: keep
---

# Kanban Migration Plan - dev-toolkit

**Date:** 2025-01-27  
**Status:** PLANNING  
**Goal:** Migrate existing Kanban structure to updated ai-dev-kit framework while preserving all work

---

## Current State

### Existing Project Epic

**Epic 1: Tool Management and Registry System**
- Status: IN PROGRESS
- Stories: 2/2 COMPLETE
- Location: `KB/PM_and_Portfolio/kanban/epics/Epic-1/`
- Content: Valid project work, must be preserved

### Framework Examples (To Remove)

**Epic 2-9:** ai-dev-kit framework examples
- Status: Documentation examples only
- Location: `KB/PM_and_Portfolio/kanban/epics/Epic-2/` through `Epic-9/`
- Content: Framework documentation, not project work
- Action: Can be removed (they're just examples)

---

## Migration Strategy

### Phase 1: Backup ✅ COMPLETE

- All existing structure backed up to `_backup-pre-migration/`
- 91 files preserved
- Complete directory structure maintained

### Phase 2: Clean Framework Examples

**Action:** Remove framework examples (Epic 2-9)  
**Rationale:** These are documentation examples, not project epics  
**Risk:** Low - they're examples, not project work

### Phase 3: Preserve Project Epic 1

**Action:** Keep Epic 1 as-is (it's valid project work)  
**Rationale:** Our Epic 1 is project-specific, not framework Epic 1  
**Note:** Framework Epic 1 is "Project Core" (generic template)  
**Our Epic 1:** "Tool Management" (specific project work)

### Phase 4: Framework Structure

**Action:** Framework files already present in `packages/frameworks/kanban/`  
**Status:** No installation needed - framework is already there  
**Note:** Framework provides templates, not installed epics

### Phase 5: Task Migration

**Action:** Migrate existing tasks to ensure they follow canonical structure  
**Current Tasks:**
- E1:S01:T01 - Tool Management System (COMPLETE)
- E1:S02:T01-T03 - Tool Distribution Strategy (COMPLETE)

**Migration:** Ensure tasks follow canonical format (already do)

---

## Key Insight

**Framework Installation ≠ Creating Epics**

The framework provides:
- ✅ Templates for creating epics
- ✅ Canonical epic definitions
- ✅ Governance policies
- ✅ Examples

The framework does NOT:
- ❌ Create project epics automatically
- ❌ Install a default epic structure
- ❌ Overwrite existing epics

**Our Epic 1 is valid project work** - it doesn't need to match framework Epic 1 (Project Core). Framework Epic 1 is a template for NEW projects, not a requirement.

---

## Revised Migration Plan

### Step 1: Clean Up Framework Examples ✅

Remove Epic 2-9 (framework examples, not project work)

### Step 2: Verify Epic 1 Structure ✅

Ensure Epic 1 follows canonical template format (it mostly does)

### Step 3: Document Gaps ✅

Create BR/FR/UXR for missing migration support

### Step 4: Framework Available ✅

Framework templates available for future epic creation

---

## Conclusion

**No "installation" needed** - framework is already present.  
**No "migration" needed** - our Epic 1 is valid project work.  
**Action needed:** Remove framework examples, document gaps.

---

**Last Updated:** 2025-01-27  
**Status:** PLAN REVISED

