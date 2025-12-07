---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-07T23:50:00Z
expires_at: null
housekeeping_policy: keep
---

# Story 004 – Bug Reports

**Status:** IN PROGRESS  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Created:** 2025-12-07  
**Last updated:** 2025-12-07 (v0.6.4.2+1 – T02 complete: Canonical stories documentation created)  
**Version:** v0.6.4.2+1  
**Code:** E6S04

---

## Task Checklist

- [x] **E6:S04:T01 – Fix RW installer template path bug** ✅ COMPLETE (v0.6.4.1+1) - Fixed incorrect path to cursorrules template file
- [x] **E6:S04:T02 – Document canonical stories for Kanban framework** ✅ COMPLETE (v0.6.4.2+1) - Created CANONICAL_STORIES.md documenting Bug Reports and Feature Requests patterns

---

## Overview

This story tracks all bug reports and bug fixes related to framework management, installation, updates, and maintenance. Bugs are converted into tasks following the FR/BR → Task → Story → Epic flow defined in the Kanban governance policy.

---

## Goal

Systematically track, prioritize, and resolve bugs in framework packages, installation tools, update mechanisms, and related framework management processes.

---

## Tasks

### E6:S04:T01 – Fix RW installer template path bug

**Input:** User feedback from `been-there` project indicating installer script couldn't find template file  
**Deliverable:** Fixed installer script with correct template path  
**Dependencies:** None  
**Blocker:** None

**Problem Statement:**
The RW installer script (`install_release_workflow.py`) was looking for the `cursorrules-rw-trigger-section.md` template file in the wrong location. It was using `PACKAGE_ROOT` (which points to `packages/frameworks/`) instead of the framework root directory (`packages/frameworks/workflow mgt/`), causing a `FileNotFoundError` when users tried to run the installer.

**Root Cause:**
- Script calculated: `PACKAGE_ROOT = SCRIPT_DIR.parent.parent` = `packages/frameworks/`
- Template file is actually at: `packages/frameworks/workflow mgt/cursorrules-rw-trigger-section.md`
- Script was looking for: `packages/frameworks/cursorrules-rw-trigger-section.md` (wrong path)

**Solution:**
- Added `FRAMEWORK_ROOT = SCRIPT_DIR.parent` to correctly point to `packages/frameworks/workflow mgt/`
- Updated `CURSORRULES_TEMPLATE` to use `FRAMEWORK_ROOT` instead of `PACKAGE_ROOT`
- Updated `SCHEMA_DOC` to use `FRAMEWORK_ROOT` for consistency

**Changes Made:**
- `packages/frameworks/workflow mgt/scripts/install_release_workflow.py`:
  - Added `FRAMEWORK_ROOT = SCRIPT_DIR.parent`
  - Changed `CURSORRULES_TEMPLATE = PACKAGE_ROOT / "cursorrules-rw-trigger-section.md"` to `FRAMEWORK_ROOT / "cursorrules-rw-trigger-section.md"`
  - Changed `SCHEMA_DOC = PACKAGE_ROOT / "config" / "rw-config-schema.md"` to `FRAMEWORK_ROOT / "config" / "rw-config-schema.md"`

**Verification:**
- ✅ Template file exists at: `packages/frameworks/workflow mgt/cursorrules-rw-trigger-section.md`
- ✅ Schema file exists at: `packages/frameworks/workflow mgt/config/rw-config-schema.md`
- ✅ Path calculation now correctly resolves to framework root directory

**Impact:**
- **Before:** Installer failed with `FileNotFoundError` when trying to load template
- **After:** Installer successfully finds and loads template file
- **User Impact:** Users can now run the installer without needing to manually work around the path bug

**Related Work:**
- E05:S04:T08 - Document `.cursorrules` setup for RW trigger (documentation that references the installer)
- E2:S04 - RW Installer & Plug-and-Play Adoption (original installer implementation)

---

## Dependencies

**Blocks:**
- None

**Blocked By:**
- None

**Coordinates With:**
- Epic 5 (Documentation Management) - Bug fixes may require documentation updates
- Epic 2 (Workflow Management Framework) - Bugs in workflow framework tools

---

## References

- `KB/PM_and_Portfolio/kanban/epics/Epic-6/Epic-6.md`
- `KB/PM_and_Portfolio/rituals/policy/kanban-governance-policy.md` - FR/BR → Task → Story → Epic flow

