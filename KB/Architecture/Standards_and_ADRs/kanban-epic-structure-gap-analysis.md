---
lifecycle: evergreen
ttl_days: null
created_at: 2025-01-27T00:00:00Z
expires_at: null
housekeeping_policy: keep
---

# Kanban Epic Structure Gap Analysis

**Issue:** The Kanban framework's `CANONICAL_EPICS.md` only documents Epics 1-7, but the expected structure includes Epics 1-21, where Epics 1-8 are CORE (always installed) and Epics 9-21 are ANCILLARY (users pick and choose).

**Date:** 2025-01-27  
**Status:** ✅ FIXED - BR #1 addressed in ai-dev-kit (2025-12-10)  
**Update:** Framework updated with all 21 epics (Core 1-8, Ancillary 9-21)

---

## Expected Epic Structure (Per User Requirements)

### Core Epics (1-8) - Always Installed

✅ **Epic 1:** Project Core - Found in all projects  
✅ **Epic 2:** Workflow Management - Found in vibe-dev-kit, been-there, fynd.deals  
✅ **Epic 3:** Versioning - Found in vibe-dev-kit, been-there, fynd.deals  
✅ **Epic 4:** Kanban Framework - Found in all projects  
✅ **Epic 5:** FR Implementation - Found in vibe-dev-kit, starborn_legacy  
✅ **Epic 6:** BR Implementation - Found in vibe-dev-kit, starborn_legacy  
✅ **Epic 7:** UXR - Found in vibe-dev-kit  
✅ **Epic 8:** Codebase Maintenance - Found in vibe-dev-kit, dev-toolkit  

### Ancillary Epics (9-21) - Users Pick and Choose

✅ **Epic 9:** User Management - Found in confidentia, fynd.deals  
✅ **Epic 10:** Data Management - Found in fynd.deals, confidentia  
✅ **Epic 11:** API & Backend - Found in fynd.deals, confidentia  
✅ **Epic 12:** Frontend & UI - Found in been-there, starborn_legacy  
✅ **Epic 13:** Testing & QA - Found in confidentia, fynd.deals  
✅ **Epic 14:** Deployment & DevOps - Found in fynd.deals  
✅ **Epic 15:** Security - Found in confidentia  
✅ **Epic 16:** Performance - Found in starborn_legacy (Backlog)  
✅ **Epic 17:** Integration - Found in confidentia, starborn_legacy  
✅ **Epic 18:** Documentation - Found in fynd.deals (Epic 15, Epic 16)  
✅ **Epic 19:** Analytics - Found in confidentia  
✅ **Epic 20:** Mobile - Found in been-there  
✅ **Epic 21:** Internationalization - Found in vibe-dev-kit  

---

## Current Framework State

### What's Documented in `CANONICAL_EPICS.md`:

1. ✅ Epic 1: AI Dev Kit Core (matches expected Epic 1)
2. ✅ Epic 2: Workflow Management Framework (matches expected Epic 2)
3. ✅ Epic 3: Numbering & Versioning Framework (matches expected Epic 3)
4. ✅ Epic 4: Kanban Framework (matches expected Epic 4)
5. ✅ Epic 5: FR Implementation (matches expected Epic 5)
6. ✅ Epic 6: BR Implementation (matches expected Epic 6)
7. ❌ Epic 7: Codebase Maintenance and Review (should be Epic 8)
8. ❌ **MISSING:** Epic 7: UXR (not documented)
9. ❌ **MISSING:** Epics 9-21: Ancillary epics (not documented)

---

## Gaps Identified

### Gap 1: Epic 7 Missing (UXR)
- **Expected:** Epic 7: UXR
- **Current:** Epic 7 is Codebase Maintenance (should be Epic 8)
- **Impact:** UXR epic not available as canonical template

### Gap 2: Epic 8 Misnumbered
- **Expected:** Epic 8: Codebase Maintenance
- **Current:** Epic 7: Codebase Maintenance and Review
- **Impact:** Epic numbering mismatch

### Gap 3: Ancillary Epics Missing (9-21)
- **Expected:** 13 ancillary epics (9-21) available as templates
- **Current:** Only 7 epics documented, no ancillary epics
- **Impact:** Users cannot pick and choose from ancillary epics during setup

---

## Root Cause Analysis

1. **Framework Documentation Incomplete:** `CANONICAL_EPICS.md` only documents Epics 1-7, missing Epic 7 (UXR) and all ancillary epics (9-21)

2. **Installation Process Missing:** No installation script or guide that:
   - Installs core epics (1-8) automatically
   - Provides selection interface for ancillary epics (9-21)
   - Creates epic templates from canonical definitions

3. **Epic Template Files Missing:** Framework should include:
   - Epic template files for all 21 epics
   - Story templates for canonical stories
   - Installation script to set up selected epics

---

## Required Fixes

### Fix 1: Update `CANONICAL_EPICS.md`
- [ ] Add Epic 7: UXR (User Experience Research)
- [ ] Renumber Epic 7 (Codebase Maintenance) → Epic 8
- [ ] Add Epics 9-21: All ancillary epics with descriptions

### Fix 2: Create Epic Template Files
- [ ] Create `templates/epics/Epic-01-Project-Core.md`
- [ ] Create `templates/epics/Epic-02-Workflow-Management.md`
- [ ] Create `templates/epics/Epic-03-Versioning.md`
- [ ] Create `templates/epics/Epic-04-Kanban-Framework.md`
- [ ] Create `templates/epics/Epic-05-FR-Implementation.md`
- [ ] Create `templates/epics/Epic-06-BR-Implementation.md`
- [ ] Create `templates/epics/Epic-07-UXR.md` (NEW)
- [ ] Create `templates/epics/Epic-08-Codebase-Maintenance.md` (renumbered)
- [ ] Create `templates/epics/Epic-09-User-Management.md` through `Epic-21-Internationalization.md`

### Fix 3: Create Installation Script/Guide
- [ ] Create `install_kanban_structure.py` or installation guide
- [ ] Install core epics (1-8) automatically
- [ ] Provide selection interface for ancillary epics (9-21)
- [ ] Copy selected epic templates to project KB structure

### Fix 4: Update Framework Documentation
- [ ] Update `README.md` to mention 21-epic structure
- [ ] Update installation guide to explain core vs ancillary
- [ ] Update intake guides to reference all 21 epics

---

## Impact Assessment

**Current State:**
- Users cannot get the expected 21-epic structure
- Installation creates incorrect epic numbering
- Missing UXR epic entirely
- No way to select ancillary epics during setup

**After Fix:**
- Users get core epics (1-8) automatically
- Users can select ancillary epics (9-21) during setup
- All epics properly numbered and documented
- Installation process matches user expectations

---

## Next Steps

1. **Immediate:** Document this gap (this file)
2. **Short-term:** Update `CANONICAL_EPICS.md` with all 21 epics
3. **Short-term:** Create epic template files for all 21 epics
4. **Medium-term:** Create installation script/guide for epic setup
5. **Long-term:** Update all framework documentation to reference 21-epic structure

---

## References

- Framework: `packages/frameworks/kanban/templates/CANONICAL_EPICS.md`
- User Expectation: Based on conversation 2025-01-27
- Current Implementation: `KB/PM_and_Portfolio/kanban/epics/Epic-1/Epic-1.md` (incorrect - created new Epic 1 instead of using canonical)

---

**Last Updated:** 2025-01-27  
**Status:** GAP DOCUMENTED - Awaiting Framework Update

