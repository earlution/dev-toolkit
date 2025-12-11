---
lifecycle: evergreen
ttl_days: null
created_at: 2025-01-27T00:00:00Z
expires_at: null
housekeeping_policy: keep
---

# Bug Report: Kanban Framework Epic Structure Gap (UAT Finding)

**Type:** Bug Report (BR)  
**Submitted:** 2025-01-27  
**Submitted By:** AI Agent (Cursor) acting as user/client  
**Priority:** HIGH  
**Severity:** HIGH  
**Status:** ✅ FIXED - BR #1 addressed in ai-dev-kit (2025-12-10)

---

## Summary

The Kanban framework's `CANONICAL_EPICS.md` only documents Epics 1-7, but the expected structure includes Epics 1-21, where Epics 1-8 are CORE (always installed) and Epics 9-21 are ANCILLARY (users pick and choose). This gap prevents users from getting the expected epic structure during framework installation.

---

## Description

### What is the Bug?

The Kanban framework documentation (`packages/frameworks/kanban/templates/CANONICAL_EPICS.md`) is incomplete. It only documents 7 canonical epics (Epics 1-7), but the framework is expected to provide 21 epics total:
- **Core Epics (1-8):** Always installed
- **Ancillary Epics (9-21):** Users pick and choose

Additionally, Epic 7 (UXR) is missing entirely, and Epic 7 (Codebase Maintenance) should be Epic 8.

### What Should Happen vs. What Actually Happens?

**Expected Behavior:**
1. User requests Kanban structure setup: "I want you to setup our Kanban structure, using the [updated] Kanban pack from ai-dev-kit"
2. Framework provides complete epic structure:
   - Core epics (1-8) automatically installed
   - Ancillary epics (9-21) available for selection
   - All epics properly numbered and documented
3. Installation process creates epic templates from canonical definitions
4. User gets expected 21-epic structure with proper numbering

**Actual Behavior:**
1. User requests Kanban structure setup
2. Agent reads `CANONICAL_EPICS.md` and finds only Epics 1-7
3. Agent creates incorrect Epic 1 for dev-toolkit (should use canonical Epic 1 template)
4. User discovers structure doesn't match expectations
5. User identifies gap: Missing Epic 7 (UXR), Epic 8 misnumbered, Epics 9-21 missing

### When Does It Occur?

This bug occurs whenever:
- A user tries to set up Kanban structure using the framework
- An agent tries to install Kanban epics from canonical templates
- A user expects the full 21-epic structure (core + ancillary)
- Installation process references `CANONICAL_EPICS.md`

### Who is Affected?

**Primary Affected:**
- Users installing Kanban framework in new projects
- AI agents automating Kanban structure setup
- Projects expecting the full epic structure

**Secondary Affected:**
- Framework maintainers (incomplete documentation)
- Framework users (confusion about epic structure)
- Future framework adopters (incorrect expectations)

---

## Affected Component

**Primary Component:** Kanban Framework - Epic Structure Documentation  
**Affected Areas:**
- [x] Documentation
- [x] Framework Templates
- [x] Installation Process
- [ ] Backend/API
- [ ] Frontend/UI
- [ ] Database/Schema
- [ ] Integration/External Service

**Root Cause:**
The `CANONICAL_EPICS.md` file was never updated to include all 21 epics. The framework documentation only covers Epics 1-7, missing Epic 7 (UXR) and all ancillary epics (9-21). Additionally, Epic 7 (Codebase Maintenance) is misnumbered and should be Epic 8.

---

## Steps to Reproduce

### UAT Scenario: Setting Up Kanban Structure

**Context:** AI Agent (Cursor) acting as user/client for dev-toolkit project

1. **User Request:** User types: "I want you to setup our Kanban structure, using the [updated] Kanban pack from ai-dev-kit"

2. **Agent Action:** Agent reads Kanban framework documentation:
   - Reads `packages/frameworks/kanban/templates/CANONICAL_EPICS.md`
   - Finds only Epics 1-7 documented
   - No mention of Epic 7 (UXR)
   - No mention of Epics 9-21

3. **Agent Assumption:** Agent assumes framework only has 7 epics

4. **Agent Creates Structure:** Agent creates new Epic 1 for dev-toolkit:
   - Creates `KB/PM_and_Portfolio/kanban/epics/Epic-1/Epic-1.md`
   - Creates Story 1 and Story 2 under Epic 1
   - Does NOT use canonical Epic 1 template

5. **User Discovery:** User reviews created structure and identifies gap:
   - User expects Epics 1-21 (core + ancillary)
   - User finds only Epic 1 created
   - User identifies missing Epic 7 (UXR)
   - User identifies Epic 8 misnumbered (should be Epic 8, currently Epic 7)
   - User identifies missing Epics 9-21

6. **User Confirmation:** User confirms expectation:
   - "My understanding is the ai-dev-kit should install the following E/S/T struct:"
   - Lists all 21 expected epics
   - Confirms Epics 1-8 are core, 9-21 are ancillary

**Expected Result:**
- Framework provides all 21 epics
- Core epics (1-8) automatically installed
- Ancillary epics (9-21) available for selection
- Proper epic numbering (Epic 7 = UXR, Epic 8 = Codebase Maintenance)

**Actual Result:**
- Framework only provides 7 epics
- Epic 7 (UXR) missing entirely
- Epic 7 (Codebase Maintenance) should be Epic 8
- Epics 9-21 not documented
- Agent creates incorrect structure

---

## Environment

**Environment:** Development (Framework Installation)  
**Version:** Kanban Framework v1.3.0 (as of 2025-12-09)  
**Repository:** earlution/dev-toolkit (consuming ai-dev-kit framework)  
**Framework Source:** earlution/ai-dev-kit  
**Framework Path:** `packages/frameworks/kanban/`  
**Affected File:** `packages/frameworks/kanban/templates/CANONICAL_EPICS.md`

---

## Impact

### User Impact

**Severity:** HIGH

**Impact Description:**
- **Critical:** Users cannot get expected epic structure during installation
- **High:** Installation creates incorrect epic numbering
- **High:** Missing Epic 7 (UXR) entirely - users cannot use UXR epic
- **Medium:** No way to select ancillary epics (9-21) during setup
- **Medium:** Confusion about epic structure and numbering

**User Experience:**
- Users expect 21-epic structure but only get 7 epics
- Users must manually create missing epics
- Users cannot leverage ancillary epics (9-21) from framework
- Installation process doesn't match user expectations

### Business Impact

**Framework Adoption:**
- Users may abandon framework if structure doesn't match expectations
- Framework appears incomplete compared to user expectations
- Framework credibility affected by documentation gaps

**Framework Maintenance:**
- Incomplete documentation creates maintenance burden
- Users create workarounds instead of using framework
- Framework evolution blocked by incomplete structure

### Workaround

**Current Workaround:**
1. Manually create missing epics (Epic 7: UXR, Epics 9-21)
2. Manually renumber Epic 7 (Codebase Maintenance) → Epic 8
3. Manually create epic templates from scratch
4. Manually update framework documentation

**Workaround Limitations:**
- Time-consuming and error-prone
- Doesn't leverage framework templates
- Creates inconsistency across projects
- Doesn't solve root cause

---

## Acceptance Criteria (Fix Requirements)

### Fix 1: Update `CANONICAL_EPICS.md`

- [ ] **Criterion 1:** Epic 7 (UXR) added to `CANONICAL_EPICS.md` with complete description
- [ ] **Criterion 2:** Epic 7 (Codebase Maintenance) renumbered to Epic 8 in `CANONICAL_EPICS.md`
- [ ] **Criterion 3:** Epics 9-21 added to `CANONICAL_EPICS.md` with complete descriptions:
  - Epic 9: User Management
  - Epic 10: Data Management
  - Epic 11: API & Backend
  - Epic 12: Frontend & UI
  - Epic 13: Testing & QA
  - Epic 14: Deployment & DevOps
  - Epic 15: Security
  - Epic 16: Performance
  - Epic 17: Integration
  - Epic 18: Documentation
  - Epic 19: Analytics
  - Epic 20: Mobile
  - Epic 21: Internationalization
- [ ] **Criterion 4:** Documentation clearly distinguishes core epics (1-8) vs ancillary epics (9-21)
- [ ] **Criterion 5:** All epic descriptions include purpose, scope, key characteristics, typical stories, and integration points

### Fix 2: Create Epic Template Files

- [ ] **Criterion 6:** Epic template files created for all 21 epics in `templates/epics/` directory
- [ ] **Criterion 7:** Template files follow naming convention: `Epic-{NN}-{Name}.md`
- [ ] **Criterion 8:** Template files include all required sections per `EPIC_TEMPLATE.md`
- [ ] **Criterion 9:** Template files are properly formatted and ready for use

### Fix 3: Create Installation Script/Guide

- [ ] **Criterion 10:** Installation script/guide created that installs core epics (1-8) automatically
- [ ] **Criterion 11:** Installation script/guide provides selection interface for ancillary epics (9-21)
- [ ] **Criterion 12:** Installation script/guide copies selected epic templates to project KB structure
- [ ] **Criterion 13:** Installation script/guide validates epic structure after installation

### Fix 4: Update Framework Documentation

- [ ] **Criterion 14:** `README.md` updated to mention 21-epic structure
- [ ] **Criterion 15:** Installation guide updated to explain core vs ancillary epics
- [ ] **Criterion 16:** Intake guides updated to reference all 21 epics
- [ ] **Criterion 17:** All framework documentation consistent with 21-epic structure

**Verification Method:**
- [x] Test suite execution (if applicable)
- [x] Manual testing (UAT scenario reproduction)
- [x] Documentation review
- [x] Framework installation test

**Fix Verification Status:**
- [ ] Verified (test suite passed / manual test passed)
- [ ] Attempted Fix (pending verification)

---

## Fix Attempt History

**Purpose:** This section documents all fix attempts for this bug, ensuring that if a bug isn't squashed, the next build can be informed by previous attempts.

### Fix Attempts

_No fix attempts yet. This is the initial bug report._

---

## Dependencies

**Blocks:**
- Proper Kanban structure installation in new projects
- Framework adoption with expected epic structure
- UXR epic usage in projects
- Ancillary epic selection during setup

**Blocked By:**
- None

**Related Work:**
- Framework: `packages/frameworks/kanban/templates/CANONICAL_EPICS.md`
- Gap Analysis: `KB/Architecture/Standards_and_ADRs/kanban-epic-structure-gap-analysis.md` (dev-toolkit)
- Epic 4: Kanban Framework (ai-dev-kit)
- Story 2: FR/BR Intake to Tasks (ai-dev-kit)

---

## Intake Decision

**Intake Status:** PENDING  
**Intake Date:** [TBD]  
**Intake By:** [TBD]

**Decision Flow Results:**
- [ ] Story Match Found: [Epic X, Story Y] → Task [T]
- [ ] New Story Created: [Epic X, Story Y] → Task 1
- [ ] New Epic Created: [Epic X, Story 1, Task 1]

**Assigned To:**
- Epic: [TBD]
- Story: [TBD]
- Task: [TBD]
- Version: `[TBD]`

**Kanban Links:**
- Epic: [TBD]
- Story: [TBD]
- Task: [TBD]

---

## Notes

### UAT Context

This bug report is the result of **User Acceptance Testing (UAT)** performed by an AI agent (Cursor) acting as a user/client for the dev-toolkit project. The UAT scenario involved:

1. **User Role:** AI Agent (Cursor) acting as framework consumer
2. **User Action:** Requested Kanban structure setup using ai-dev-kit framework
3. **Expected Outcome:** Complete 21-epic structure (core + ancillary)
4. **Actual Outcome:** Only 7 epics available, missing Epic 7 (UXR) and Epics 9-21
5. **User Feedback:** Identified gap and provided expected epic structure

### Rationale

**Why This Matters:**
- Framework documentation should match user expectations
- Incomplete documentation creates confusion and adoption barriers
- Users expect full epic structure based on framework claims
- Missing epics prevent users from leveraging framework capabilities

**Why This Should Be Fixed:**
- Framework credibility depends on complete documentation
- Users cannot use framework as intended without complete epic structure
- Installation process should match user expectations
- Framework evolution requires complete epic structure

### Expected Epic Structure (Per User Requirements)

**Core Epics (1-8) - Always Installed:**
- Epic 1: Project Core
- Epic 2: Workflow Management
- Epic 3: Versioning
- Epic 4: Kanban Framework
- Epic 5: FR Implementation
- Epic 6: BR Implementation
- Epic 7: UXR (MISSING)
- Epic 8: Codebase Maintenance (currently misnumbered as Epic 7)

**Ancillary Epics (9-21) - Users Pick and Choose:**
- Epic 9: User Management
- Epic 10: Data Management
- Epic 11: API & Backend
- Epic 12: Frontend & UI
- Epic 13: Testing & QA
- Epic 14: Deployment & DevOps
- Epic 15: Security
- Epic 16: Performance
- Epic 17: Integration
- Epic 18: Documentation
- Epic 19: Analytics
- Epic 20: Mobile
- Epic 21: Internationalization

---

## References

- **Framework Documentation:** `packages/frameworks/kanban/templates/CANONICAL_EPICS.md`
- **Gap Analysis:** `KB/Architecture/Standards_and_ADRs/kanban-epic-structure-gap-analysis.md` (dev-toolkit)
- **Epic Template:** `packages/frameworks/kanban/templates/EPIC_TEMPLATE.md`
- **Kanban Framework README:** `packages/frameworks/kanban/README.md`
- **User Expectation:** Based on UAT conversation 2025-01-27

---

**Template Usage:**
- This BR follows the Kanban Framework BR template
- UAT findings documented as bug report
- Comprehensive gap analysis included
- Clear acceptance criteria provided
- Fix requirements specified

---

_This bug report is part of the Kanban Framework. See `packages/frameworks/kanban/` for complete framework documentation._

