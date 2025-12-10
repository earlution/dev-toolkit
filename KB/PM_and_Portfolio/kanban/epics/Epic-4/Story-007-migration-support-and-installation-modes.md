---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-10T14:00:00Z
expires_at: null
housekeeping_policy: keep
---

# Story 7: Migration Support and Installation Modes

**Status:** IN PROGRESS  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Last updated:** 2025-12-10 (v0.4.7.1+1 – Task 1 complete: Detection and analysis utilities implemented)  
**Version:** v0.4.7.1+1  
**Code:** E4S07

---

## Goal

Provide safe adoption paths for projects with pre-existing Kanban/Sprint/Issue structures by adding detection, analysis, migration utilities, and installation modes.

---

## Tasks

- [x] **E4:S07:T01 – BR-006: Detection/analysis utilities for existing structures** ✅ COMPLETE (v0.4.7.1+1)
  - Implemented detection utility (`detect_existing_structure.py`) - scans for epic directories, detects epic/story documents, identifies tasks, generates detection report
  - Implemented analysis utility (`analyze_structure.py`) - maps existing items to E/S/T format, identifies conflicts and gaps, generates migration plan
  - Created scripts README with usage documentation
  - Tested on current project structure (10 epics, 46 stories, 335 tasks detected)
  - **Linked BR:** `BR-006-missing-migration-support-pre-existing-kanban.md` (GitHub issue #2)  
  - **Acceptance:** ✅ Criteria 1-4 of BR-006 satisfied and documented.

- [ ] **E4:S07:T02 – FR-007: Migration utilities and installation modes**  
  - Implement migration utility (`migrate_structure.py`), backups, and installation modes (Fresh, Migration, Update, Hybrid) with documentation and examples.  
  - **Linked FR:** `FR-007-migration-utilities-and-installation-modes.md` (GitHub issue #3)  
  - **Acceptance:** AC-1..AC-8 of FR-007 satisfied and documented.

- [ ] **E4:S07:T03 – Documentation and guides update**  
  - Update `packages/frameworks/kanban/README.md` and user guides to cover detection, migration paths, and mode selection; add examples.  
  - **Linked BR/FR:** BR-006 / FR-007.  
  - **Acceptance:** BR-006 criteria 9-12 and FR-007 AC-6..AC-8 addressed in docs.

---

## References

- BR-006: `KB/PM_and_Portfolio/kanban/fr-br/BR-006-missing-migration-support-pre-existing-kanban.md`
- FR-007: `KB/PM_and_Portfolio/kanban/fr-br/FR-007-migration-utilities-and-installation-modes.md`
- UXR-001 (inputs): `KB/PM_and_Portfolio/kanban/fr-br/UXR-001-migration-user-experience-research.md`

---

**Template Usage:** Story follows Kanban framework story template; Tasks trace to BR/FR for forensic linkage.

