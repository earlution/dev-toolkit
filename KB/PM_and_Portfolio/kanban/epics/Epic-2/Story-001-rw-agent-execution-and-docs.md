---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-04T12:01:50Z
expires_at: null
housekeeping_policy: keep
---

# Story 001 – RW Agent Execution & Docs

**Status:** IN PROGRESS  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Created:** 2025-12-02  
**Last updated:** 2025-12-05 (v0.2.1.1+5 – New task T05 added: Harden RW branch safety checks)  
**Version:** v0.2.1.1+5  
**Code:** E2S01

---

## Overview

Make RW agent execution documentation fully portable, clearly distinguishing dev-kit behaviour from external examples. This story ensures that the Release Workflow documentation is template-ready and can be easily adopted by other projects.

---

## Goal

Make RW agent execution documentation fully portable, clearly distinguishing dev-kit behaviour from external examples. Ensure that the Release Workflow accurately reflects verification requirements for fixes and other changes.

---

## Task Checklist

- [x] **E2:S01:T01 – Audit `release-workflow-agent-execution.md` for project-specific assumptions** ✅ COMPLETE (v0.2.1.1+3)
- [x] **E2:S01:T02 – Tag Confidentia/fynd.deals examples and add dev-kit examples** ✅ COMPLETE (v0.2.1.1+4)
- [x] **E2:S01:T03 – Align `.cursorrules` RW trigger section with dev-kit policy** ✅ COMPLETE (v0.2.1.1+5)
- [x] **E2:S01:T04 – Update RW changelog step to require verification before marking fixes as "fixed"** ✅ COMPLETE (v0.2.1.1+2)
- [ ] **E2:S01:T05 – Harden RW branch safety checks to stop execution on wrong branch** - TODO

---

## Tasks

### E2:S01:T01 – Audit `release-workflow-agent-execution.md` for project-specific assumptions ✅ COMPLETE

**Input:** Current `release-workflow-agent-execution.md` file  
**Deliverable:** Audit report identifying project-specific assumptions ✅ **DELIVERED**  
**Dependencies:** None  
**Blocker:** None

**Status:** ✅ **COMPLETE** - Comprehensive audit report created

**Approach:**
1. ✅ Reviewed `packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md`
2. ✅ Identified 15 project-specific assumptions across 4 categories:
   - Hardcoded File Paths (7 instances)
   - Handler Names (2 instances)
   - Project References (3 instances)
   - Version/Branch Examples (3 instances)
3. ✅ Documented findings and recommendations in audit report

**Key Findings:**
- **15 project-specific assumptions** identified
- **7 hardcoded file paths** need template placeholders
- **2 handler names** need abstraction
- **3 project references** need tagging or removal
- **3 version/branch examples** need generic patterns

**Recommendations:**
- Replace hardcoded paths with template placeholders (`{version_file_path}`, `{kanban_path}`, etc.)
- Replace handler names with generic or templated versions
- Tag all examples clearly or use generic patterns
- Add configuration section listing all template placeholders

**Files Created:**
- ✅ `KB/PM_and_Portfolio/kanban/Story-001-rw-agent-execution-and-docs/T001-audit-report.md` (comprehensive audit report)

**Deliverable:** See [`T001-audit-report.md`](T001-audit-report.md) for complete audit findings and recommendations.

---

### E2:S01:T02 – Tag Confidentia/fynd.deals examples and add dev-kit examples ✅ COMPLETE

**Input:** Audit report from T001  
**Deliverable:** Updated documentation with clearly tagged examples ✅ **DELIVERED**  
**Dependencies:** E2:S01:T01  
**Blocker:** None

**Status:** ✅ **COMPLETE** - All examples tagged and dev-kit examples added

**Approach:**
1. ✅ Tagged all Confidentia/fynd.deals examples with `[Example: Confidentia]` or `[Example: Confidentia/fynd.deals]` labels
2. ✅ Added dev-kit-specific examples with `[Example: vibe-dev-kit]` labels throughout the document
3. ✅ Added overview note explaining example tagging system
4. ✅ Ensured examples are clearly distinguished in all 11 steps

**Key Changes:**
- **Document Header:** Tagged "Related" field with example labels
- **Step 1 (Branch Safety Check):** Tagged branch examples, added dev-kit branch examples
- **Step 2 (Bump Version):** Tagged version file paths, version numbers, added dev-kit equivalents
- **Step 3 (Create Detailed Changelog):** Tagged version examples, branch examples, file paths, added dev-kit equivalents
- **Step 4 (Update Main Changelog):** Tagged version examples, added dev-kit equivalents
- **Step 5 (Update README):** Tagged version examples, added dev-kit equivalents
- **Step 6 (Auto-update Kanban Docs):** Tagged handler names, Kanban paths, version examples, added dev-kit equivalents
- **Step 8 (Run Validators):** Tagged handler names, script paths, added template placeholder notes
- **Step 9 (Commit Changes):** Tagged version examples, commit messages, added dev-kit equivalents
- **Step 10 (Create Git Tag):** Tagged version examples, tag names/messages, added dev-kit equivalents
- **Step 11 (Push to Remote):** Tagged branch examples, tag examples, added dev-kit equivalents

**Files Updated:**
- ✅ `packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md` (comprehensive tagging and dev-kit examples added)

**Deliverable:** Documentation now clearly distinguishes between Confidentia/fynd.deals examples and dev-kit examples, making it easier for users to understand which examples apply to their project.

---

### E2:S01:T03 – Align `.cursorrules` RW trigger section with dev-kit policy ✅ COMPLETE

**Input:** Updated RW documentation from T002  
**Deliverable:** Updated `.cursorrules` RW trigger section ✅ **DELIVERED**  
**Dependencies:** E2:S01:T02  
**Blocker:** None

**Status:** ✅ **COMPLETE** - Cursorrules RW trigger section aligned with dev-kit policy

**Approach:**
1. ✅ Reviewed `packages/frameworks/workflow mgt/cursorrules-rw-trigger-section.md`
2. ✅ Reviewed `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md`
3. ✅ Added dev-kit-specific examples throughout the section
4. ✅ Enhanced version schema section with new story/epic progression rules
5. ✅ Added dev-kit file path examples
6. ✅ Added dev-kit epic ranges information
7. ✅ Added canonical ordering, forensic traceability, and immutability principles
8. ✅ Added "For vibe-dev-kit Usage" section with dev-kit-specific paths
9. ✅ Enhanced changelog format notes with immutability requirements

**Key Changes:**
- **File Paths Section:** Added dev-kit examples for all paths (version file, changelog, Kanban, validators)
- **Version Schema Section:** 
  - Added new story/epic progression rules
  - Added dev-kit epic ranges (Epic 1-4+)
  - Clarified no legacy range in dev-kit
- **Version Calculation Examples:** Added dev-kit-specific examples for all progression scenarios
- **Key Principles:** Added canonical ordering, forensic traceability, and immutability principles
- **Changelog Steps:** Enhanced with immutability notes (detailed changelog timestamps are immutable)
- **Reference Documentation:** Added Kanban governance policy reference
- **Customization Section:** Added "For vibe-dev-kit Usage" subsection with dev-kit-specific paths and policy references

**Files Updated:**
- ✅ `packages/frameworks/workflow mgt/cursorrules-rw-trigger-section.md` (aligned with dev-kit policy)

**Deliverable:** Cursorrules RW trigger section now includes dev-kit-specific examples and aligns with dev-kit versioning policy, making it clear how to use the template in the dev-kit repository itself.

---

### E2:S01:T04 – Update RW changelog step to require verification before marking fixes as "fixed"

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

### E2:S01:T05 – Harden RW branch safety checks to stop execution on wrong branch

**Input:** Current RW Step 1 implementation, `validate_branch_context.py` script  
**Deliverable:** Hardened RW with mandatory branch safety enforcement  
**Dependencies:** None  
**Blocker:** None

**Problem Statement:**
The Release Workflow (RW) currently has Step 1: Branch Safety Check documented, but it is not being enforced. The RW continues execution even when on the wrong branch (e.g., on `epic/9` but committing Epic 5 work). This allows cross-epic contamination and violates branch isolation principles. The RW must STOP immediately if branch safety checks fail and provide clear guidance to the user.

**Approach:**
1. **Audit current implementation:**
   - Review Step 1 execution in `release-workflow-agent-execution.md`
   - Review `validate_branch_context.py` script behavior
   - Identify gaps where RW continues despite branch mismatches
   - Document all failure modes where branch safety is bypassed

2. **Design mandatory branch safety enforcement:**
   - Define branch safety check as **MANDATORY BLOCKING STEP**
   - Ensure Step 1 runs BEFORE any file modifications
   - Design clear failure states and error messages
   - Create user guidance for branch mismatch scenarios

3. **Implement branch safety hardening:**
   - Update RW Step 1 to call `validate_branch_context.py` and parse exit code
   - If validator returns non-zero exit code, STOP workflow immediately
   - Mark all remaining steps as `cancelled`
   - Output clear error message with actionable guidance

4. **Update RW documentation:**
   - Update `release-workflow-agent-execution.md` Step 1 to emphasize MANDATORY nature
   - Add explicit "DO NOT PROCEED" language
   - Document exact error message format
   - Add examples of branch mismatch scenarios and resolutions

5. **Update agent guidance:**
   - Update `.cursorrules` RW trigger section to emphasize branch safety
   - Add explicit instruction: "If Step 1 fails, DO NOT proceed to Step 2"
   - Create agent rules that prevent bypassing branch checks
   - Document anti-pattern: "Never skip or ignore branch safety checks"

6. **Create validation integration:**
   - Ensure `validate_branch_context.py` returns proper exit codes
   - Integrate validator into RW Step 1 execution flow
   - Add validation result parsing and error handling
   - Create test scenarios for branch mismatch detection

**Deliverables:**
- Hardened RW Step 1 that stops on branch mismatch
- Updated `release-workflow-agent-execution.md` with mandatory enforcement
- Updated `.cursorrules` RW trigger section with branch safety emphasis
- Integration of `validate_branch_context.py` into RW execution
- Clear error messages and user guidance for branch mismatches
- Agent rules preventing branch safety bypass

**Success Criteria:**
- RW stops immediately if branch safety check fails
- No file modifications occur when on wrong branch
- Clear error messages guide user to correct branch
- All remaining steps marked as `cancelled` on failure
- Agent cannot bypass branch safety checks
- Validator integration is mandatory and non-optional

**Error Message Format:**
```
🚨 RELEASE WORKFLOW BLOCKED

Step 1: Branch Safety Check - FAILED

Reason: Current branch '{branch}' does not align with the work being released.

Details:
- Current branch: {branch}
- Expected branch: epic/{expected_epic}
- Version file shows: {version}
- Detected epic from work: {detected_epic}

Action Required:
1. Switch to the correct branch: git checkout epic/{correct_epic}
2. Verify your changes align with the branch: git status
3. Then run RW again

RW is NOT complete. Workflow stopped at Step 1.
All subsequent steps have been cancelled.
```

**Files to Update:**
- `packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md` (Step 1 hardening)
- `packages/frameworks/workflow mgt/cursorrules-rw-trigger-section.md` (branch safety emphasis)
- Agent execution patterns (mandatory validation)

---

## Acceptance Criteria

- [x] RW documentation is fully portable and template-ready ✅
- [x] Examples are clearly tagged as dev-kit vs external ✅
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

_Last updated: 2025-12-02 (v0.2.1.1+5 – Task 3 complete: Align .cursorrules RW trigger section with dev-kit policy)_

