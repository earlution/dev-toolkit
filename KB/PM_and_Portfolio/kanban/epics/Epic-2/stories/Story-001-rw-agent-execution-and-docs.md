# Story 001 – RW Agent Execution & Docs

**Status:** TODO  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Created:** 2025-12-02  
**Last updated:** 2025-12-02 (v0.2.1.1+2 – Task 4 complete: Update RW changelog step to require verification)
**Version:** v0.2.1.1+2  
**Code:** E2S01

---

## Overview

Make RW agent execution documentation fully portable, clearly distinguishing dev-kit behaviour from external examples. This story ensures that the Release Workflow documentation is template-ready and can be easily adopted by other projects.

---

## Goal

Make RW agent execution documentation fully portable, clearly distinguishing dev-kit behaviour from external examples. Ensure that the Release Workflow accurately reflects verification requirements for fixes and other changes.

---

## Task Checklist

- [ ] **E2:S01:T001 – Audit `release-workflow-agent-execution.md` for project-specific assumptions**
- [ ] **E2:S01:T002 – Tag Confidentia/fynd.deals examples and add dev-kit examples**
- [ ] **E2:S01:T003 – Align `.cursorrules` RW trigger section with dev-kit policy**
- [x] **E2:S01:T004 – Update RW changelog step to require verification before marking fixes as "fixed"** ✅ COMPLETE (v0.2.1.1+2)

---

## Tasks

### E2:S01:T001 – Audit `release-workflow-agent-execution.md` for project-specific assumptions

**Input:** Current `release-workflow-agent-execution.md` file  
**Deliverable:** Audit report identifying project-specific assumptions  
**Dependencies:** None  
**Blocker:** None

**Approach:**
1. Review `packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md`
2. Identify project-specific paths, examples, and assumptions
3. Document findings and recommendations for making it template-ready

**Files to Review:**
- `packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md`

---

### E2:S01:T002 – Tag Confidentia/fynd.deals examples and add dev-kit examples

**Input:** Audit report from T001  
**Deliverable:** Updated documentation with clearly tagged examples  
**Dependencies:** E2:S01:T001  
**Blocker:** None

**Approach:**
1. Tag all Confidentia/fynd.deals examples with clear labels
2. Add dev-kit-specific examples where appropriate
3. Ensure examples are clearly distinguished

**Files to Update:**
- `packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md`

---

### E2:S01:T003 – Align `.cursorrules` RW trigger section with dev-kit policy

**Input:** Updated RW documentation from T002  
**Deliverable:** Updated `.cursorrules` RW trigger section  
**Dependencies:** E2:S01:T002  
**Blocker:** None

**Approach:**
1. Review `packages/frameworks/workflow mgt/cursorrules-rw-trigger-section.md`
2. Ensure alignment with dev-kit versioning and Kanban policies
3. Update any inconsistencies

**Files to Update:**
- `packages/frameworks/workflow mgt/cursorrules-rw-trigger-section.md`

---

### E2:S01:T004 – Update RW changelog step to require verification before marking fixes as "fixed"

**Input:** Current RW changelog documentation  
**Deliverable:** Updated RW documentation requiring verification for fixes  
**Dependencies:** None  
**Blocker:** None

**Approach:**
1. Review Step 3 (Create Detailed Changelog) and Step 4 (Update Main Changelog) in `release-workflow-agent-execution.md`
2. Update documentation to specify that fixes cannot be claimed as "Fixed" until verified through testing
3. Add requirement that unverified fixes should be logged as "Attempted fix" until verification
4. Specify verification methods: test suite execution or manual testing
5. Update changelog format guidelines to include verification status
6. Add validation step to ensure fixes are not marked as "Fixed" without verification evidence

**Problem Solved:**
- Prevents claiming fixes are complete before they're actually verified
- Ensures changelogs accurately reflect the state of fixes
- Maintains integrity of release documentation

**Files to Update:**
- `packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md`
- Update Step 3 (Create Detailed Changelog) to include verification requirements
- Update Step 4 (Update Main Changelog) to include verification requirements
- Add validation checks for verification status

**Key Changes:**
- Add verification requirement to changelog creation process
- Specify that fixes must be logged as "Attempted fix" until verified
- Add verification status field to changelog format
- Update agent execution pattern to include verification check
- Add validation step to ensure verification before marking as "Fixed"

**Verification Methods:**
- Test suite execution (automated tests pass)
- Manual testing (documented test results)
- Both methods acceptable, but verification must be documented

**Changelog Format Updates:**
- Add "Verification Status" field: `Verified` / `Attempted Fix (Pending Verification)`
- Update "Fixed" section to only include verified fixes
- Add "Attempted Fixes" section for unverified fixes
- Include verification method and evidence in changelog entry

---

## Acceptance Criteria

- [ ] RW documentation is fully portable and template-ready
- [ ] Examples are clearly tagged as dev-kit vs external
- [x] Changelog step requires verification before marking fixes as "Fixed" ✅
- [x] Unverified fixes are logged as "Attempted fix" until verified ✅
- [x] Verification methods (test suite, manual testing) are documented ✅
- [x] Validation checks enforce verification requirements ✅

---

## Dependencies

**Coordinates With:**
- Epic 3: Numbering & Versioning Framework (for versioning integration)
- Epic 4: Kanban Framework (for Kanban integration)

---

## References

- `packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md`
- `packages/frameworks/workflow mgt/cursorrules-rw-trigger-section.md`
- `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md`

---

_Last updated: 2025-12-02 (v0.2.1.1+2 – Task 4 complete: Update RW changelog step to require verification)_

