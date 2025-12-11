---
lifecycle: evergreen
ttl_days: null
created_at: 2025-01-27T00:00:00Z
expires_at: null
housekeeping_policy: keep
---

# Migration Approach - Understanding the Structure

**Date:** 2025-01-27  
**Status:** APPROACH DEFINED

---

## Key Understanding

### What Are Epic 2-9?

**Epic 2-9 in dev-toolkit are:**
- ai-dev-kit's own project epics (not templates)
- Framework documentation examples
- NOT dev-toolkit project epics
- Should NOT be in dev-toolkit's Kanban structure

**Epic 1 in dev-toolkit is:**
- dev-toolkit project epic (Tool Management)
- Valid project work
- Must be preserved

### What Does "Installing Framework" Mean?

**Framework provides:**
- Templates (`EPIC_TEMPLATE.md`, `STORY_TEMPLATE.md`)
- Canonical definitions (`CANONICAL_EPICS.md`)
- Governance policies
- Examples

**Framework does NOT:**
- Create project epics automatically
- Install default epic structure
- Require matching canonical epic numbers

**Our Epic 1 ≠ Framework Epic 1:**
- Framework Epic 1: "Project Core" (template for new projects)
- Our Epic 1: "Tool Management" (specific project work)
- Both are valid - ours is project-specific

---

## Migration Strategy

### Step 1: Remove Framework Epics ✅

**Action:** Remove Epic 2-9 (they're ai-dev-kit's epics, not ours)  
**Rationale:** These are framework examples/documentation, not dev-toolkit work  
**Risk:** None - they're not our project epics

### Step 2: Preserve Project Epic 1 ✅

**Action:** Keep Epic 1 as-is  
**Rationale:** Valid project work, follows structure correctly  
**Note:** Doesn't need to match framework Epic 1 template

### Step 3: Framework Available ✅

**Action:** Framework templates already available  
**Status:** No installation needed - framework is in `packages/frameworks/kanban/`  
**Use:** Templates available for creating NEW epics in future

### Step 4: Document Gaps ✅

**Action:** Create BR/FR/UXR for missing migration support  
**Focus:** Framework needs to handle pre-existing structures

---

## Revised Plan

1. ✅ Backup complete
2. ⏳ Remove Epic 2-9 (framework examples)
3. ✅ Keep Epic 1 (project work)
4. ✅ Framework templates available
5. ⏳ Document gaps and create BR/FR/UXR

---

**Last Updated:** 2025-01-27  
**Status:** APPROACH DEFINED

