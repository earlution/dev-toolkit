---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-04T12:01:50Z
expires_at: null
housekeeping_policy: keep
---

# Story 002 – Versioning Cookbook & Examples

**Status:** IN PROGRESS  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Created:** 2025-12-03  
**Last updated:** 2025-12-08 (v0.3.2.10+1 – T10 created: Integrate PVW into Release Workflow agent execution guide)  
**Version:** v0.3.2.10+1  
**Code:** E3S02

---

## Task Checklist

- [x] **E3:S02:T01 – Define core versioning scenarios for the cookbook** ✅ COMPLETE (v0.3.2.1+1)
- [x] **E3:S02:T02 – Create versioning cookbook document with worked examples** ✅ COMPLETE (v0.3.2.2+1)
- [x] **E3:S02:T03 – Add cross-framework examples (Kanban + Versioning + RW)** ✅ COMPLETE (v0.3.2.3+1)
- [x] **E3:S02:T04 – Document edge cases and anti-patterns** ✅ COMPLETE (v0.3.2.4+1)
- [x] **E3:S02:T05 – Create quick reference summary for users and agents** ✅ COMPLETE (v0.3.2.5+1)
- [x] **E3:S02:T06 – Investigate and harden changelog ordering process** 🔄 PERPETUAL (v0.3.2.6+1)
- [x] **E3:S02:T07 – Create dual-versioning guide for package manager compatibility** ✅ COMPLETE (v0.3.2.7+1)
- [x] **E3:S02:T08 – Audit dual-versioning application across packages and propose strategy** ✅ COMPLETE (v0.3.2.8+1)
- [x] **E3:S02:T09 – Implement Package Version Workflow (PVW) with agentic execution** ✅ COMPLETE (v0.3.2.9+1)
- [ ] **E3:S02:T10 – Integrate PVW into Release Workflow agent execution guide** - TODO

---

## Overview

This story produces a **practical versioning cookbook** for the RC.EPIC.STORY.TASK+BUILD schema, turning the dev-kit versioning policy and framework docs into **concrete, copyable examples** for other projects.

It focuses on:

- Realistic scenarios (new epic, new story, new task, bugfix, hotfix, parallel work)
- Clear mapping between **Kanban → Versioning → RW**
- Guidance that is **safe to copy** into external projects

---

## Goal

Provide a **versioning cookbook** with worked examples that shows:

- How to select the right version components for common scenarios
- How to handle parallel epics/stories safely
- How to represent bugfixes and hotfixes
- How to keep Kanban, versioning, and RW aligned

---

## Tasks

### E3:S02:T01 – Define core versioning scenarios for the cookbook

**Input:**  
- `packages/frameworks/numbering & versioning/versioning-policy.md`  
- `packages/frameworks/numbering & versioning/versioning-strategy.md`  
- `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md`  

**Deliverable:**  
- Scenario list + brief description for each scenario

**Approach:**
1. Identify core scenarios:
   - New epic
   - New story under existing epic
   - New task under existing story
   - Bugfix / hotfix on an existing task
   - Parallel epics and stories
2. For each scenario:
   - Describe context
   - Describe expected version behaviour
   - Note any Kanban/RW interactions
3. Validate against framework policy and dev-kit policy.

**Acceptance Criteria:**
- [ ] Core scenarios identified and documented
- [ ] Each scenario has clear description and expected version behaviour
- [ ] Scenarios aligned with both framework and dev-kit policies

---

### E3:S02:T02 – Create versioning cookbook document with worked examples

**Input:**  
- Scenario list from T01  
- Existing dev-kit version history (CHANGELOG + archive)  

**Deliverable:**  
- `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-cookbook.md` (or similar)

**Approach:**
1. For each scenario from T01, create:
   - Before/after version examples
   - Kanban context (Epic/Story/Task)
   - RW perspective (how RW interprets the version)
2. Use real dev-kit examples where possible; create synthetic ones where not.
3. Structure cookbook by scenario, with clear headings and cross-links.

**Acceptance Criteria:**
- [ ] Cookbook document created
- [ ] At least one worked example per scenario
- [ ] Examples are copyable and safe for other projects
- [ ] Links to relevant policies and guides added

---

### E3:S02:T03 – Add cross-framework examples (Kanban + Versioning + RW)

**Input:**  
- Integration docs:
  - `KB/Architecture/Standards_and_ADRs/dev-kit-kanban-versioning-rw-integration.md`
  - `KB/PM_and_Portfolio/kanban/Story-003-kanban-versioning-rw-integration.md`

**Deliverable:**  
- Section in the cookbook with end-to-end cross-framework examples

**Approach:**
1. Select 2–3 representative flows:
   - FR → Task → Version → RW → Kanban update
   - Bugfix with verification requirement
   - Parallel epic/story work
2. For each flow, show:
   - Kanban state
   - Version change
   - RW steps and checks
   - Resulting documentation (changelogs, Kanban markers)

**Acceptance Criteria:**
- [ ] At least 2 cross-framework examples documented
- [ ] Each example ties together Kanban, versioning, and RW
- [ ] Examples align with existing integration docs

---

### E3:S02:T04 – Document edge cases and anti-patterns ✅ COMPLETE

**Input:**  
- Findings from Epic 3 Story 1  
- Findings from Epic 4 Story 3 (integration validation)  

**Deliverable:**  
- Edge cases & anti-patterns section in the cookbook ✅ **DELIVERED**

**Status:** ✅ **COMPLETE** - Comprehensive edge cases and anti-patterns section added to versioning cookbook

**Approach:**
1. ✅ Listed known edge cases:
   - Task renumbering
   - Story re-parenting between epics
   - Version conflicts when branches diverge
   - Incorrect TASK mapping
   - Standalone task references
   - BUILD number overflow
   - Missing version in changelog
   - Version mismatch between commit and tag
   - Parallel epic development ordering
2. ✅ For each, documented:
   - Symptom
   - Root cause
   - Corrective pattern
   - Preventive guidance

**Key Deliverables:**
- ✅ Section 10 added to versioning cookbook with 10 edge cases and anti-patterns
- ✅ Each entry includes symptom, root cause, corrective pattern, and preventive guidance
- ✅ References to related documentation (error reference guide, root cause analysis)
- ✅ Table of contents updated to include new section
- ✅ Examples and real dev-kit scenarios included

**Acceptance Criteria:**
- [x] Edge cases identified and documented ✅
- [x] Anti-patterns clearly described ✅
- [x] Preventive guidance provided ✅

---

### E3:S02:T05 – Create quick reference summary for users and agents

**Input:**  
- Cookbook content from T02–T04  

**Deliverable:**  
- Short quick reference (1–2 pages) for humans and agents

**Approach:**
1. Extract the most commonly needed rules and patterns.
2. Present them as:
   - Tables
   - Mini decision flows
   - \"If this, then version like that\" rules
3. Ensure language is agent-friendly and human-friendly.

**Acceptance Criteria:**
- [x] Quick reference created ✅
- [x] Covers common scenarios and rules ✅
- [x] Linked from cookbook, dev-kit versioning policy, and relevant READMEs ✅

---

### E3:S02:T06 – Investigate and harden changelog ordering process

**Status:** 🔄 PERPETUAL  
**Note:** This task is marked as PERPETUAL because changelog ordering is an ongoing maintenance concern. While the initial investigation and hardening work was completed in v0.3.2.6+1, the changelog must be continuously maintained to ensure canonical ordering is preserved. This task remains active to track any future ordering violations and ensure the process continues to work correctly.

**Input:**  
- Issue: Changelog entries appeared in incorrect order (v0.3.2.4+1 before v0.2.4.9+3)
- Canonical ordering principle: Versions must be ordered by version number (RC.EPIC.STORY.TASK+BUILD)
- Policy: `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md` Section 8

**Deliverable:**  
- Root cause analysis of how changelog ordering violation occurred
- Process improvements to prevent future violations
- Validation/automation recommendations
- Ongoing maintenance of changelog canonical ordering

**Approach:**
1. **Root Cause Analysis:**
   - Investigate how RW Step 4 (Update Main Changelog) handles version ordering
   - Check if RW Step 4 reads existing changelog entries before inserting new entry
   - Verify if RW Step 4 compares version numbers to determine insertion point
   - Document the exact sequence that led to incorrect ordering

2. **Process Gap Analysis:**
   - Identify missing validation steps in RW workflow
   - Check if changelog ordering is validated in RW Step 8 (Run Validators)
   - Determine if manual process is required or if automation is possible

3. **Prevention Strategy:**
   - Update RW Step 4 to explicitly validate version ordering
   - Add changelog ordering validation to RW Step 8
   - Create automated validation script if needed
   - Update RW documentation with ordering requirements

4. **Documentation Updates:**
   - Update RW Step 4 instructions to include ordering validation
   - Add changelog ordering to validation checklist
   - Document canonical ordering requirements clearly

**Acceptance Criteria:**
- [x] Root cause analysis completed and documented ✅
- [x] Process gaps identified ✅
- [x] Prevention strategy defined ✅
- [x] RW Step 4 updated with ordering validation ✅
- [x] Validation added to RW Step 8 ✅
- [x] Documentation updated with ordering requirements ✅
- [x] Prevention measures implemented ✅

---

### E3:S02:T07 – Create dual-versioning guide for package manager compatibility

**Input:**  
- User requirement: Projects using `RC.EPIC.STORY.TASK+BUILD` schema need SemVer (`MAJOR.MINOR.PATCH`) for package managers (npm, pub.dev, PyPI, etc.)
- Issue identified: `been-there` project agent created sync script, indicating need for canonical guidance
- Framework documentation: `packages/frameworks/numbering & versioning/IMPLEMENTATION_GUIDE.md`

**Deliverable:**  
- `KB/Architecture/Standards_and_ADRs/dual-versioning-package-managers.md` - Comprehensive guide for managing dual versioning
- Updated `IMPLEMENTATION_GUIDE.md` with package manager compatibility warning
- Updated framework README with dual-versioning reference

**Approach:**
1. **Document the Problem:**
   - Explain incompatibility between `RC.EPIC.STORY.TASK+BUILD` and SemVer requirements
   - Provide examples of package manager requirements (npm, pub.dev, PyPI, Maven)
   - Show real-world scenario (been-there project)

2. **Define Mapping Strategies:**
   - Strategy 1: Direct Mapping (MAJOR=RC, MINOR=EPIC, PATCH=STORY*100+TASK)
   - Strategy 2: Compact Mapping (includes BUILD in PATCH)
   - Strategy 3: Independent SemVer (for public releases)
   - Strategy 4: BUILD-Preserving Mapping (Recommended) - `MINOR = EPIC * 100 + STORY`, `PATCH = TASK * 100 + BUILD`
   - Strategy 5: Hybrid Approach (combines strategies)

3. **Implementation Patterns:**
   - Pattern 1: Single Source of Truth (Python example)
   - Pattern 2: Sync Script (any language)
   - Pattern 3: Build-Time Generation (CI/CD)

4. **Code Examples:**
   - Python implementation (Strategy 4)
   - Dart/Flutter implementation (pubspec.yaml)
   - Sync script examples
   - Validation scripts

5. **Best Practices:**
   - Single source of truth principle
   - Automation recommendations
   - Validation requirements
   - Integration with Release Workflow

6. **Update Framework Documentation:**
   - Add warning to `IMPLEMENTATION_GUIDE.md` about package manager compatibility
   - Update framework README with dual-versioning reference
   - Update dev-kit versioning policy with dual-versioning reference

**Key Requirements:**
- Use mathematical formula `EPIC * 100 + STORY` (not string concatenation) to avoid ambiguity
- Preserve BUILD number in SemVer when possible (Strategy 4)
- Provide clear, copyable examples for different languages
- Document all mapping strategies with pros/cons

**Acceptance Criteria:**
- [ ] Dual-versioning guide created with comprehensive mapping strategies
- [ ] Strategy 4 (BUILD-Preserving Mapping) documented as recommended approach
- [ ] Mathematical formula `EPIC * 100 + STORY` used (not string concatenation)
- [ ] Implementation patterns provided (Python, Dart/Flutter, sync scripts)
- [ ] Code examples included for all patterns
- [ ] Best practices and validation documented
- [ ] Framework documentation updated with references
- [ ] Guide linked from Implementation Guide and framework README

---

### E3:S02:T08 – Audit dual-versioning application across packages and propose strategy

**Status:** ✅ COMPLETE (v0.3.2.8+1)  

**Input:**  
- Dual-versioning guide (`dual-versioning-package-managers.md`)  
- Current package version metadata (if any) in each package  
- Release history and SemVer expectations for package managers  

**Deliverable:**  
- ✅ **Audit Report:** `T008-dual-versioning-package-audit-report.md` - Comprehensive audit covering:
  - All packages inventoried (Workflow Management: 2.0.0, Numbering & Versioning: 2.0.0, Kanban: 1.0.0, Debug Path: 1.0.0, Doc Lifecycle: 1.0.0)
  - No package manifest files found (no `package.json`, `pubspec.yaml`, `setup.py`, `pyproject.toml`)
  - Dual-versioning strategy analysis: NOT applicable for current documentation-only packages
  - SemVer continuity problem validated: Derived SemVer from RC.EPIC.STORY.TASK+BUILD would create non-continuous sequences
  - Proposed solution: Independent SemVer for packages (current approach is correct)
  - Recommendations for current packages and future published packages
  - Guidance for adopting projects on when to use dual-versioning vs. independent SemVer

**Key Findings:**
- ✅ Current packages use independent SemVer in README (appropriate for documentation packages)
- ❌ No package manifest files exist (not needed for documentation-only packages)
- ⚠️ Dual-versioning is NOT necessary for documentation-only packages
- ✅ Independent SemVer is recommended for published packages (avoids continuity issues)
- ✅ SemVer continuity concern validated - derived SemVer would create non-continuous sequences

**Recommendations:**
- Continue current approach for documentation packages (independent SemVer in README)
- Use independent SemVer for future published packages (separate from project version)
- Update dual-versioning guide to clarify when to use dual-versioning vs. independent SemVer

**Dependencies:** None (uses existing policy and guide)  
**Blocker:** None  
**Parallel Development Candidacy:** Safe  

**Approach:**  
1. ✅ Inventoried all packages and located any existing SemVer fields (none found - no package manifest files)
2. ✅ Recorded current SemVer values in README files (Workflow Management: 2.0.0, Numbering & Versioning: 2.0.0, Kanban: 1.0.0, Debug Path: 1.0.0, Doc Lifecycle: 1.0.0)
3. ✅ Evaluated applicability of dual-versioning mapping strategies:
   - Assessed that derived SemVer would disrupt version continuity (validated user concern)
   - Determined that independent SemVer track is appropriate for current packages
4. ✅ Proposed package-specific strategy:
   - Current packages: Continue independent SemVer in README (no changes needed)
   - Future published packages: Use independent SemVer with project version reference in metadata
   - Guidance provided on when to use dual-versioning vs. independent SemVer
5. ✅ Summarized findings and recommendations in comprehensive audit report  

---

### E3:S02:T09 – Implement Package Version Workflow (PVW) with agentic execution

**Status:** ✅ COMPLETE (v0.3.2.9+1)  

**Input:**  
- Audit report (`T008-dual-versioning-package-audit-report.md`)
- Agentic approach proposal (`T008-package-versioning-agentic-approach.md`)
- Release Workflow agent execution pattern
- Agent-driven execution methodology

**Deliverable:**  
- ✅ **PVW Workflow Definition:** `packages/frameworks/workflow mgt/workflows/package-version-workflow.yaml`
- ✅ **PVW Agent Execution Guide:** `packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/package-version-workflow-agent-execution.md`
- ✅ **Validation Scripts (Tools):** `packages/frameworks/workflow mgt/scripts/validation/package/`
- ✅ **RW Integration:** Updated `release-workflow.yaml` with PVW as Step 2.5
- ✅ **Cursor Rules Section:** Added PVW trigger section with comprehensive TODO tracking
- ✅ **Version Bump Criteria:** `KB/Architecture/Standards_and_ADRs/package-versioning-criteria.md`

**Package Version Updates:**
- **Workflow Management:** 2.0.0 → 2.1.0 (MINOR) - Added Package Version Workflow (PVW)

**Dependencies:** E3:S02:T08 (completed)  
**Blocker:** None  
**Parallel Development Candidacy:** Safe  

**Approach:**  
1. ✅ Created PVW workflow definition (YAML structure similar to RW)
2. ✅ Created PVW agent execution guide (step-by-step guide with examples)
3. ✅ Created validation scripts as tools (format, increment, consistency, change analysis)
4. ✅ Integrated with Release Workflow YAML (PVW as Step 2.5)
5. ✅ Created Cursor rules section (PVW trigger with TODO tracking)
6. ✅ Documented version bump criteria as guidance

---

### E3:S02:T10 – Integrate PVW into Release Workflow agent execution guide

**Status:** TODO  

**Input:**  
- PVW implementation (E3:S02:T09 - completed)
- Release Workflow agent execution guide (`release-workflow-agent-execution.md`)
- Release Workflow YAML definition (`release-workflow.yaml` - already has step-2.5)

**Deliverable:**  
- ✅ **Updated RW Agent Execution Guide:** `packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md`
  - Add step-2.5 (PVW) to TODO list (15 steps total, not 14)
  - Add step-2.5 execution documentation (ANALYZE → DETERMINE → EXECUTE → VALIDATE → PROCEED)
  - Reference PVW agent execution guide for detailed step-by-step instructions
  - Update Step 3 dependencies to include step-2.5
  - Update execution checklist to include step-2.5
  - Update version history to document PVW integration
- ✅ **Updated Step Dependencies:** Ensure Step 3 (Create Detailed Changelog) depends on both step-2 and step-2.5
- ✅ **Updated Workflow Count:** Update from 14 steps to 15 steps (with step-2.5)

**Key Requirements:**
- Step-2.5 executes after Step 2 (Bump Version) and before Step 3 (Create Detailed Changelog)
- Step-2.5 should reference the PVW agent execution guide for detailed instructions
- Step-2.5 should be optional (required: false) but enabled by default
- Step-2.5 should handle the case where no packages have changed (skip gracefully)

**Dependencies:** E3:S02:T09 (completed)  
**Blocker:** None  
**Parallel Development Candidacy:** Safe  

**Approach:**  
1. Update TODO list in RW guide to include `rw-step-2.5`
2. Add step-2.5 section to RW guide with execution instructions
3. Reference PVW agent execution guide for detailed step-by-step
4. Update Step 3 dependencies documentation
5. Update execution checklist
6. Update version history

---

## Acceptance Criteria (Story)

- [ ] Versioning cookbook document created with worked examples
- [ ] Core scenarios documented and validated
- [ ] Cross-framework examples (Kanban + Versioning + RW) included
- [ ] Edge cases and anti-patterns documented
- [ ] Quick reference summary created
- [ ] Links added from dev-kit versioning policy and framework READMEs to the cookbook

---

## References

- `packages/frameworks/numbering & versioning/versioning-policy.md`  
- `packages/frameworks/numbering & versioning/versioning-strategy.md`  
- `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md`  
- `KB/Architecture/Standards_and_ADRs/dev-kit-kanban-versioning-rw-integration.md`  
- `KB/PM_and_Portfolio/kanban/Story-003-kanban-versioning-rw-integration.md`  

---

_Last updated: 2025-12-03 (initial story definition)_  


