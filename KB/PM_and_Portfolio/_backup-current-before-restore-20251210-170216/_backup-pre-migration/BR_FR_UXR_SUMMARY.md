---
lifecycle: evergreen
ttl_days: null
created_at: 2025-01-27T00:00:00Z
expires_at: null
housekeeping_policy: keep
---

# BR/FR/UXR Summary - Pre-Existing Kanban Migration Support

**Date:** 2025-01-27  
**Status:** READY FOR SUBMISSION  
**Target:** ai-dev-kit repository

---

## Overview

This document summarizes the BR/FR/UXR that need to be filed with ai-dev-kit to address the gap in handling pre-existing Kanban structures during framework installation.

---

## BR: Missing Migration Support

**Type:** Bug Report  
**Priority:** HIGH  
**Severity:** HIGH

**Summary:** Framework installation process assumes fresh install with no existing Kanban structure. When projects have pre-existing Kanban (or Sprint/Agile) systems, the framework cannot detect, analyze, preserve, or migrate existing work items.

**Impact:**
- Risk of overwriting existing work
- No migration path from existing systems
- Manual migration required (error-prone)
- Framework adoption barriers for projects with existing Kanban

**Acceptance Criteria:**
- Framework can detect existing Kanban structures
- Framework can analyze existing work items
- Framework can preserve existing work during installation
- Framework can migrate existing items to canonical structure
- Framework supports multiple installation modes (fresh, migration, update)

---

## FR: Migration Utilities and Installation Modes

**Type:** Feature Request  
**Priority:** HIGH

**Summary:** Add migration utilities and installation modes to support projects with pre-existing Kanban structures.

**Features:**
1. **Detection Utilities:**
   - `detect_existing_structure.py` - Scan for existing epics/stories
   - Report existing structure found

2. **Analysis Utilities:**
   - `analyze_structure.py` - Map existing items to E/S/T
   - Identify conflicts and generate migration plan

3. **Migration Utilities:**
   - `migrate_structure.py` - Migrate existing work to canonical format
   - Preserve forensic markers and work history

4. **Installation Modes:**
   - Fresh Install (current behavior)
   - Migration Install (detect and migrate)
   - Update Install (update existing framework)
   - Hybrid Install (preserve project epics, install framework epics)

**Use Cases:**
- Projects migrating from Sprint-based systems
- Projects migrating from issue trackers (GitHub Issues, Jira)
- Projects updating from older framework versions
- Projects with mixed Kanban structures

---

## UXR: Migration User Experience Research

**Type:** User Experience Research  
**Priority:** MEDIUM

**Summary:** Research user experience of migrating from existing Kanban/Sprint systems to ai-dev-kit Kanban framework.

**Research Objectives:**
1. Understand common existing Kanban/Sprint structures
2. Identify migration pain points
3. Document user workflows for migration
4. Validate migration utility designs

**Key Findings (from dev-toolkit migration):**
- Existing structures vary widely (Kanban, Sprints, Issues)
- Framework examples can be confused with project epics
- No clear separation between project work and framework examples
- Manual migration is error-prone and time-consuming

**Recommendations:**
- Provide clear detection and analysis tools
- Support multiple migration scenarios
- Clear separation of project epics vs framework examples
- Interactive migration process with user confirmation

---

## Interdependencies

**BR → FR:** BR identifies the gap, FR provides the solution  
**FR → UXR:** FR designs migration utilities, UXR validates user experience  
**UXR → FR:** UXR findings inform FR implementation

**All three should reference each other** to provide comprehensive coverage of the migration gap.

---

## Submission Plan

1. **BR:** File first (identifies the problem)
2. **FR:** File second (proposes solution, references BR)
3. **UXR:** File third (validates approach, references BR and FR)

**Cross-References:**
- BR references FR and UXR
- FR references BR and UXR
- UXR references BR and FR

---

**Last Updated:** 2025-01-27  
**Status:** READY FOR CREATION

