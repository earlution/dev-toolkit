# Story 001 – Dev Kit Alignment with Versioning Framework

**Status:** TODO  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Created:** 2025-12-02  
**Last updated:** 2025-12-02 (v0.3.1.1+1 – initial story definition)  
**Version:** v0.3.1.1+1  
**Code:** E3S01

---

## Overview

Ensure the dev kit's own versioning policy, version file, and docs align cleanly with the generic versioning framework. This story ensures that `vibe-dev-kit` serves as the **single point of truth (SoT)** for versioning policies and strategies, which other projects can copy and adapt.

---

## Goal

Make sure the dev kit's versioning implementation demonstrates best practices and serves as the canonical reference for how to adopt the `RC.EPIC.STORY.TASK+BUILD` schema in new projects.

---

## Task Checklist

- [ ] **E3:S01:T001 – Review dev-kit versioning policy vs framework policy**
- [ ] **E3:S01:T002 – Ingest versioning findings from fynd.deals Epic 15 work**
- [ ] **E3:S01:T003 – Update dev-kit versioning policy as canonical SoT**
- [ ] **E3:S01:T004 – Align dev-kit version.py and CHANGELOG with framework**
- [ ] **E3:S01:T005 – Document consumption pattern for other projects**

---

## Tasks

### E3:S01:T001 – Review dev-kit versioning policy vs framework policy

**Input:** Current dev-kit and framework versioning files  
**Deliverable:** Gap analysis report  
**Dependencies:** None  
**Blocker:** None

**Approach:**
1. Review `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md`
2. Review `packages/frameworks/numbering & versioning/versioning-policy.md`
3. Review `packages/frameworks/numbering & versioning/versioning-strategy.md`
4. Compare dev-kit policy with framework policy
5. Document gaps and inconsistencies

**Files to Review:**
- `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md`
- `packages/frameworks/numbering & versioning/versioning-policy.md`
- `packages/frameworks/numbering & versioning/versioning-strategy.md`
- `packages/frameworks/numbering & versioning/README.md`
- `src/fynd_deals/version.py` (dev-kit version file)

---

### E3:S01:T002 – Ingest versioning findings from fynd.deals Epic 15 work

**Input:** fynd.deals Epic 15 versioning documentation  
**Deliverable:** Summary of reusable patterns and findings  
**Dependencies:** E3:S01:T001  
**Blocker:** None

**Approach:**
1. Review `fynd.deals/docs/fynd_deals/_design/versioning/versioning-policy.md`
2. Review `fynd.deals/docs/fynd_deals/_design/versioning/versioning-strategy.md`
3. Review `fynd.deals/src/fynd_deals/version.py` (implementation)
4. Extract reusable patterns, especially:
   - Version schema format: `RC.EPIC.STORY.TASK+BUILD`
   - Epic renumbering strategy (Epic 1-9 legacy, Epic 10+ new format)
   - Version validation and branch context checks
   - CHANGELOG format and archive structure
5. Document findings and recommendations

**Source Files (from fynd.deals):**
- `docs/fynd_deals/_design/versioning/versioning-policy.md`
- `docs/fynd_deals/_design/versioning/versioning-strategy.md`
- `docs/fynd_deals/_design/versioning/VERSION-RENUMBERING-STRATEGY.md`
- `src/fynd_deals/version.py`
- `CHANGELOG.md` and `CHANGELOG_ARCHIVE/` structure

**Key Patterns to Capture:**
- Version schema: `RC.EPIC.STORY.TASK+BUILD` format
- Legacy vs new format: Epic 1-9 grandfathered, Epic 10+ uses new format
- Version validation: Branch context checks, changelog format validation
- CHANGELOG structure: Main changelog + archive with detailed entries
- Date formats: New format uses `DD-MM-YY`, old format uses `YYYY-MM-DD`

---

### E3:S01:T003 – Update dev-kit versioning policy as canonical SoT

**Input:** Findings from T001 and T002  
**Deliverable:** Updated canonical versioning policy  
**Dependencies:** E3:S01:T001, E3:S01:T002  
**Blocker:** None

**Approach:**
1. Refine `packages/frameworks/numbering & versioning/versioning-policy.md` to embed:
   - Complete `RC.EPIC.STORY.TASK+BUILD` schema definition
   - Epic renumbering strategy (legacy vs new format)
   - Version validation requirements
   - CHANGELOG format and archive structure
   - Branch context validation
2. Ensure `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md` aligns with framework policy
3. Document the relationship between framework policy (SoT) and project-specific adaptations

**Files to Update:**
- `packages/frameworks/numbering & versioning/versioning-policy.md` (primary SoT)
- `packages/frameworks/numbering & versioning/versioning-strategy.md` (comprehensive strategy)
- `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md` (dev-kit local policy, references framework)

**Key Sections to Add/Enhance:**
- Version schema definition (`RC.EPIC.STORY.TASK+BUILD`)
- Epic renumbering strategy (legacy Epic 1-9, new Epic 10+)
- Version validation (branch context, changelog format)
- CHANGELOG structure (main + archive)
- Date format conventions (new vs old format)

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
- Source: `fynd.deals/docs/fynd_deals/_design/versioning/versioning-*.md`

---

_Last updated: 2025-12-02 (to be released as v0.3.1.1+1)_

