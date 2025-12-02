# Story 001 – Dev Kit Alignment with Versioning Framework

**Status:** TODO
**Priority:** HIGH
**Estimated Effort:** [TBD]
**Created:** 2025-12-02
**Last updated:** 2025-12-02 (v0.3.1.3+1 – Task 3 complete: Dev-kit versioning policy enhanced with all missing sections)
**Version:** v0.3.1.3+1
**Code:** E3S01

---

## Overview

Ensure the dev kit's own versioning policy, version file, and docs align cleanly with the generic versioning framework. This story ensures that `vibe-dev-kit` serves as the **single point of truth (SoT)** for versioning policies and strategies, which other projects can copy and adapt.

---

## Goal

Make sure the dev kit's versioning implementation demonstrates best practices and serves as the canonical reference for how to adopt the `RC.EPIC.STORY.TASK+BUILD` schema in new projects.

---

## Task Checklist

- [x] **E3:S01:T001 – Review dev-kit versioning policy vs framework policy** ✅ COMPLETE (v0.3.1.1+2)
- [x] **E3:S01:T002 – Ingest versioning findings from fynd.deals Epic 15 work** ✅ COMPLETE (v0.3.1.2+1)
- [x] **E3:S01:T003 – Update dev-kit versioning policy as canonical SoT** ✅ COMPLETE (v0.3.1.3+1)
- [ ] **E3:S01:T004 – Align dev-kit version.py and CHANGELOG with framework**
- [ ] **E3:S01:T005 – Document consumption pattern for other projects**
- [ ] **E3:S01:T006 – Make .cursorrules abstract (remove hardcoded version numbers)**

---

## Tasks

### E3:S01:T001 – Review dev-kit versioning policy vs framework policy ✅ COMPLETE

**Input:** Current dev-kit and framework versioning files  
**Deliverable:** Gap analysis report ✅ **DELIVERED**  
**Dependencies:** None  
**Blocker:** None

**Status:** ✅ **COMPLETE** - Gap analysis documented in `T001-gap-analysis-report.md`

**Approach:**
1. ✅ Reviewed `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md`
2. ✅ Reviewed `packages/frameworks/numbering & versioning/versioning-policy.md`
3. ✅ Reviewed `packages/frameworks/numbering & versioning/versioning-strategy.md`
4. ✅ Compared dev-kit policy with framework policy
5. ✅ Documented gaps and inconsistencies

**Key Findings:**
- ✅ Schema definition matches perfectly
- ✅ Progression rules are correct
- ❌ Missing 6 critical sections: CHANGELOG format, canonical ordering, two-layer timestamps, traceability grid, immutability rules, validation
- ⚠️ Version file location uses legacy path (`src/fynd_deals/version.py`)
- ✅ Dev-kit correctly avoids legacy complexity (clean Epic 1+ start)

**Deliverable:** See [`T001-gap-analysis-report.md`](T001-gap-analysis-report.md) for complete gap analysis.

---

### E3:S01:T002 – Ingest versioning findings from fynd.deals Epic 15 work ✅ COMPLETE

**Input:** fynd.deals Epic 15 versioning documentation  
**Deliverable:** Summary of reusable patterns and findings ✅ **DELIVERED**  
**Dependencies:** E3:S01:T001  
**Blocker:** None

**Status:** ✅ **COMPLETE** - Findings documented in `T002-fynd-deals-epic15-findings.md`

**Approach:**
1. ✅ Reviewed framework package versioning files (already contain fynd.deals Epic 15 findings)
2. ✅ Analyzed versioning patterns from `packages/frameworks/numbering & versioning/`
3. ✅ Extracted reusable patterns (12 key patterns identified)
4. ✅ Documented findings and recommendations
5. ✅ Created findings document: `T002-fynd-deals-epic15-findings.md`

**Key Finding:** The framework package (`packages/frameworks/numbering & versioning/`) **already contains** the fynd.deals Epic 15 findings, as documented in `PACKAGE_UPDATE_SUMMARY.md`.

**Patterns Extracted:**
- ✅ Version schema: `RC.EPIC.STORY.TASK+BUILD` format
- ✅ Epic renumbering strategy (project-specific, but pattern documented)
- ✅ Version validation: Branch context checks, changelog format validation
- ✅ CHANGELOG structure: Two-layer system (main + archive)
- ✅ Date formats: New format uses `DD-MM-YY`, old format uses `YYYY-MM-DD`
- ✅ Canonical ordering: Version numbers, not timestamps
- ✅ Forensic traceability: Multi-dimensional grid
- ✅ Immutability rules: Historical metadata preservation

**Deliverable:** See [`T002-fynd-deals-epic15-findings.md`](T002-fynd-deals-epic15-findings.md) for complete findings document.

---

### E3:S01:T003 – Update dev-kit versioning policy as canonical SoT ✅ COMPLETE

**Input:** Findings from T001 and T002  
**Deliverable:** Updated canonical versioning policy ✅ **DELIVERED**  
**Dependencies:** E3:S01:T001, E3:S01:T002  
**Blocker:** None

**Status:** ✅ **COMPLETE** - Dev-kit versioning policy updated with all missing sections

**Approach:**
1. ✅ Enhanced `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md` with:
   - CHANGELOG Format section (two-layer system)
   - Canonical Ordering Principle section
   - Two-Layer Timestamp System section
   - Forensic Traceability Grid section (5 dimensions)
   - Immutability Rules section (3 rules)
   - Version Validation section
   - Enhanced Relationship to Framework Policies section
   - Status and Maintenance section
   - Comprehensive References section

2. ✅ Documented relationship between framework policy (SoT) and dev-kit adaptations
3. ✅ Updated policy status from "Draft" to "Active"

**Key Sections Added:**
- ✅ CHANGELOG Format (Section 7) - Two-layer system documented
- ✅ Canonical Ordering Principle (Section 8) - Version numbers are canonical
- ✅ Two-Layer Timestamp System (Section 9) - Main vs detailed changelog timestamps
- ✅ Forensic Traceability Grid (Section 10) - 5 dimensions documented
- ✅ Immutability Rules (Section 11) - 3 rules documented
- ✅ Version Validation (Section 12) - Validation scripts and behavior documented

**Files Updated:**
- ✅ `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md` - Enhanced with all missing sections
- ✅ Policy status updated to "Active"

**Note:** Framework policies (`packages/frameworks/numbering & versioning/`) remain the canonical SoT. Dev-kit policy now comprehensively documents how the framework is applied in dev-kit context, referencing framework for detailed explanations.

---

### E3:S01:T004 – Align dev-kit version.py and CHANGELOG with framework

**Input:** Updated versioning policy from T003
**Deliverable:** Updated dev-kit version file and CHANGELOG
**Dependencies:** E3:S01:T003
**Blocker:** None

**Approach:**
1. Update `src/fynd_deals/version.py` to:
   - Use dev-kit Epic/Story/Task numbers (not external project numbers)
   - Follow `RC.EPIC.STORY.TASK+BUILD` schema
   - Include validation logic
   - Document dev-kit versioning approach
2. Ensure `CHANGELOG.md` follows framework format:
   - New format: `## [version] - DD-MM-YY`
   - Archive entries in `CHANGELOG_ARCHIVE/CHANGELOG_v{version}.md`
   - Consistent structure and metadata
3. Align with framework validation scripts

**Files to Update:**
- `src/fynd_deals/version.py` (or rename to `src/vibe_dev_kit/version.py` if appropriate)
- `CHANGELOG.md`
- `CHANGELOG_ARCHIVE/` structure

**Key Alignments:**
- Version schema matches framework
- Validation logic matches framework scripts
- CHANGELOG format matches framework conventions
- Date format uses new format (`DD-MM-YY`)

---

### E3:S01:T005 – Document consumption pattern for other projects

**Input:** Updated policies and version file from T003-T004
**Deliverable:** Consumption documentation
**Dependencies:** E3:S01:T003, E3:S01:T004
**Blocker:** None

**Approach:**
1. Update `packages/frameworks/numbering & versioning/README.md` to document:
   - Projects MUST **copy** versioning policies from `vibe-dev-kit`
   - They then customize Epic/Story/Task ranges, but keep the **schema and validation rules** intact
   - `vibe-dev-kit` remains the single point of truth for future updates
2. Create/update implementation guides showing:
   - How to copy versioning framework into a new project
   - How to set up `version.py` with project-specific Epic/Story/Task ranges
   - How to configure validation scripts
   - How to stay aligned with framework updates
3. Document the relationship between framework (SoT) and project implementations

**Files to Update/Create:**
- `packages/frameworks/numbering & versioning/README.md` (add consumption section)
- `packages/frameworks/numbering & versioning/IMPLEMENTATION_GUIDE.md` (update or create)

**Key Documentation Points:**
- Copy, don't reference: Projects must copy files, not link to `vibe-dev-kit`
- Customization boundaries: What can be customized (Epic ranges, paths) vs what must stay (schema, validation)
- Update process: How to pull framework updates into projects
- SoT relationship: `vibe-dev-kit` is the canonical source

---

### E3:S01:T006 – Make .cursorrules abstract (remove hardcoded version numbers)

**Input:** Findings from T002 (versioning pattern analysis)
**Deliverable:** Updated `.cursorrules` template without hardcoded versions
**Dependencies:** E3:S01:T002
**Blocker:** None

**Approach:**
1. Analyze current `.cursorrules` implementations across projects (confidentia/12, fynd.deals)
2. Identify areas where specific version numbers are hardcoded (e.g., "Epic 12 = 0.4.7.x")
3. Replace hardcoded version examples with:
   - Generic schema explanations (`RC.EPIC.STORY.TASK+BUILD`)
   - Template-style examples (e.g., "Epic 12, Story 4, Task 1 → `0.12.4.1+1`")
   - References to canonical policy documents instead of duplicating schema details
4. Update branch mapping sections to explain the **pattern** rather than list specific branches
5. Ensure `.cursorrules` teaches the **schema** without listing stale/project-specific instances

**Problem Solved:**
- Hardcoded version numbers in `.cursorrules` become stale as work progresses
- Creates confusion when examples don't match current state
- Violates "single source of truth" principle (schema is already in KB docs)
- Increases maintenance burden (must update `.cursorrules` for each epic/story)

**Files to Review/Update:**
- `.cursorrules` (template for dev kit)
- Example `.cursorrules` from confidentia/12 project (reference implementation)
- `packages/frameworks/workflow mgt/cursorrules-rw-trigger-section.md` (if applicable)

**Key Changes:**
- Replace "BRANCH MAPPING" with "BRANCH NAMING AND VERSIONING" that explains schema
- Remove specific branch → version mappings
- Add generic examples showing schema calculation (Epic N → 0.N.x.x+x)
- Reference `KB/Architecture/Standards_and_ADRs/versioning-policy.md` as canonical source
- Update MANDATORY COMMIT CHECKLIST to use generic schema reference

**Validation:**
- `.cursorrules` should not contain any project-specific version numbers
- Examples should be generic and teach the pattern
- Schema explanations should match canonical policy documents
- File should remain useful without requiring updates as work progresses

**Source Reference:**
- Work completed in confidentia/12 project (2025-12-02)
- Changes made to lines 7, 35-46 of `.cursorrules`

---

## Acceptance Criteria

- [ ] Dev-kit versioning policy is the canonical SoT
- [ ] Policies capture complete version schema and validation rules
- [ ] Dev-kit version.py and CHANGELOG align with framework
- [ ] Consumption pattern is clearly documented
- [ ] Framework and project implementations are clearly distinguished

---

## Dependencies

**Coordinates With:**
- Epic 4: Kanban Framework (for Kanban + versioning integration)
- Epic 2: Workflow Management Framework (for RW + versioning integration)
- Epic 1: Vibe Dev Kit Core (for dev-kit versioning decisions)

---

## References

- `packages/frameworks/numbering & versioning/README.md`
- `packages/frameworks/numbering & versioning/versioning-policy.md`
- `packages/frameworks/numbering & versioning/versioning-strategy.md`
- `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md`
- **T001 Gap Analysis:** [`T001-gap-analysis-report.md`](T001-gap-analysis-report.md)
- **T002 Findings:** [`T002-fynd-deals-epic15-findings.md`](T002-fynd-deals-epic15-findings.md)
- Source: `fynd.deals/docs/fynd_deals/_design/versioning/versioning-*.md` (findings already ingested into framework package)

---

_Last updated: 2025-12-02 (v0.3.1.2+1 – Task 2 complete)_
