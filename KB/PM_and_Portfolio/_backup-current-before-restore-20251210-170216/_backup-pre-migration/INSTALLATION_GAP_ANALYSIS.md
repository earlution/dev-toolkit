---
lifecycle: evergreen
ttl_days: null
created_at: 2025-01-27T00:00:00Z
expires_at: null
housekeeping_policy: keep
---

# Installation Gap Analysis - Pre-Existing Kanban Structures

**Date:** 2025-01-27  
**Issue:** ai-dev-kit Kanban framework lacks support for pre-existing Kanban structures  
**Status:** GAP DOCUMENTED

---

## Executive Summary

The ai-dev-kit Kanban framework installation process **assumes a fresh install** with no existing Kanban structure. When a project has pre-existing Kanban (or Sprint/Agile) systems, the framework:

1. ❌ **Cannot detect** existing structures
2. ❌ **Cannot migrate** from existing systems
3. ❌ **Cannot preserve** existing work items
4. ❌ **Cannot distinguish** between project epics and framework examples
5. ❌ **Risk of overwriting** existing work if installed naively

**Impact:** Projects with existing Kanban systems cannot safely adopt the framework without manual migration work.

---

## Use Case: dev-toolkit Migration

### Current State

**Pre-Existing Structure:**
- Epic 1: Tool Management and Registry System (dev-toolkit project epic)
  - Story 1: Tool Management System (COMPLETE)
  - Story 2: Tool Distribution Strategy (COMPLETE)
- Epic 2-9: Framework examples (ai-dev-kit documentation)

**Framework Files:**
- Already present in `packages/frameworks/kanban/`
- Templates available
- Canonical epics documented (now includes all 21 epics)

### Desired State

**After Framework Installation:**
- Epic 1: Tool Management and Registry System (preserved, migrated to canonical structure)
- Epic 2-8: Core framework epics (installed from templates)
- Epic 9-21: Ancillary epics (available for selection)
- Framework examples separated from project epics

### Migration Challenges

1. **Structure Mismatch:** Existing Epic 1 doesn't follow canonical template exactly
2. **Mixed Content:** Framework examples (Epic 2-9) mixed with project epic (Epic 1)
3. **No Migration Path:** Framework provides no utilities to migrate existing work
4. **Risk of Data Loss:** Naive installation would overwrite existing Epic 1

---

## Framework Installation Process Analysis

### Current Installation Steps (from README)

```yaml
step_1:
  action: "Copy package files"
  assumption: "Fresh project, no existing Kanban"
  
step_2:
  action: "Customize file paths"
  assumption: "No existing structure to preserve"
  
step_3:
  action: "Create first Epic"
  assumption: "Starting from scratch"
  
step_4:
  action: "Create first Story"
  assumption: "No existing stories to migrate"
```

### Missing Steps

```yaml
missing_step_0:
  action: "Detect existing Kanban structure"
  purpose: "Identify pre-existing epics/stories/tasks"
  current: "NOT IMPLEMENTED"
  
missing_step_0.5:
  action: "Analyze existing structure"
  purpose: "Map existing work items to E/S/T structure"
  current: "NOT IMPLEMENTED"
  
missing_step_1.5:
  action: "Preserve existing work"
  purpose: "Backup existing structure before installation"
  current: "NOT IMPLEMENTED"
  
missing_step_2.5:
  action: "Migrate existing work"
  purpose: "Convert existing items to canonical structure"
  current: "NOT IMPLEMENTED"
```

---

## Gap Categories

### Gap 1: Detection

**Missing:** Framework cannot detect existing Kanban structures  
**Impact:** Cannot determine if installation is safe  
**Required:** Detection utilities to scan for existing epics/stories

### Gap 2: Analysis

**Missing:** Framework cannot analyze existing structure  
**Impact:** Cannot understand what needs to be preserved  
**Required:** Analysis tools to map existing work to E/S/T structure

### Gap 3: Preservation

**Missing:** Framework cannot preserve existing work  
**Impact:** Risk of data loss during installation  
**Required:** Backup and preservation mechanisms

### Gap 4: Migration

**Missing:** Framework cannot migrate existing work  
**Impact:** Manual migration required, error-prone  
**Required:** Migration utilities to convert existing items to canonical structure

### Gap 5: Separation

**Missing:** Framework cannot distinguish project epics from framework examples  
**Impact:** Confusion about what belongs to project vs framework  
**Required:** Clear separation and identification mechanisms

---

## Required Framework Enhancements

### Enhancement 1: Pre-Installation Detection

**Feature:** Detect existing Kanban structures before installation  
**Components:**
- Scan for existing epic directories
- Detect epic documents
- Identify story documents
- Map existing structure

**Output:** Report of existing structure found

### Enhancement 2: Migration Utilities

**Feature:** Migrate existing work items to canonical structure  
**Components:**
- Epic migration (preserve content, update structure)
- Story migration (map to canonical format)
- Task migration (preserve work, update format)
- Version marker migration (preserve forensic markers)

**Output:** Migrated structure following canonical format

### Enhancement 3: Installation Modes

**Feature:** Support different installation modes  
**Modes:**
- **Fresh Install:** No existing structure (current behavior)
- **Migration Install:** Existing structure detected, migrate it
- **Update Install:** Framework already installed, update templates
- **Hybrid Install:** Preserve project epics, install framework epics

**Output:** Appropriate installation path selected

### Enhancement 4: Conflict Resolution

**Feature:** Handle conflicts during installation  
**Scenarios:**
- Epic numbering conflicts
- Story numbering conflicts
- File path conflicts
- Content conflicts

**Output:** Resolved conflicts with user input

---

## Migration Scenarios to Support

### Scenario 1: Simple Kanban Migration

**Existing:** Basic Kanban board with epics/stories  
**Challenge:** Map to E/S/T structure  
**Required:** Epic/Story mapping utilities

### Scenario 2: Sprint-Based Migration

**Existing:** Sprint-based agile system  
**Challenge:** Convert sprints to epics/stories  
**Required:** Sprint-to-Epic conversion utilities

### Scenario 3: Issue Tracker Migration

**Existing:** GitHub Issues, Jira, etc.  
**Challenge:** Convert issues to E/S/T structure  
**Required:** Issue-to-Task conversion utilities

### Scenario 4: Mixed Structure Migration

**Existing:** Mix of Kanban, Sprints, Issues  
**Challenge:** Unified migration to E/S/T  
**Required:** Multi-source migration utilities

### Scenario 5: Framework Update Migration

**Existing:** Older framework version  
**Challenge:** Update to new structure  
**Required:** Version-to-version migration utilities

---

## Implementation Recommendations

### Phase 1: Detection (Critical)

1. Create `detect_existing_structure.py`
   - Scan for epic directories
   - Detect epic documents
   - Identify story documents
   - Report findings

### Phase 2: Analysis (Critical)

2. Create `analyze_structure.py`
   - Map existing items to E/S/T
   - Identify conflicts
   - Generate migration plan

### Phase 3: Migration (High Priority)

3. Create `migrate_structure.py`
   - Backup existing structure
   - Migrate epics to canonical format
   - Migrate stories to canonical format
   - Migrate tasks to canonical format
   - Preserve forensic markers

### Phase 4: Installation Modes (High Priority)

4. Update installation process
   - Add mode selection
   - Implement migration mode
   - Implement update mode
   - Implement hybrid mode

### Phase 5: Conflict Resolution (Medium Priority)

5. Create conflict resolution utilities
   - Detect conflicts
   - Propose resolutions
   - Interactive resolution

---

## Success Criteria

**Framework should support:**
- ✅ Detection of existing Kanban structures
- ✅ Analysis of existing work items
- ✅ Preservation of existing work
- ✅ Migration to canonical structure
- ✅ Safe installation without data loss
- ✅ Clear separation of project vs framework epics

---

## References

- Framework README: `packages/frameworks/kanban/README.md`
- Epic Template: `packages/frameworks/kanban/templates/EPIC_TEMPLATE.md`
- Current Structure: `KB/PM_and_Portfolio/kanban/epics/`
- Backup: `KB/PM_and_Portfolio/kanban/_backup-pre-migration/`

---

**Last Updated:** 2025-01-27  
**Status:** GAP DOCUMENTED - Ready for BR/FR/UXR Creation

