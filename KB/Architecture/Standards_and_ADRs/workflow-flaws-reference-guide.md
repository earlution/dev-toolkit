---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-04T21:00:00Z
expires_at: null
housekeeping_policy: keep
---

# Release Workflow Flaws Reference Guide

**Status:** ACTIVE REFERENCE  
**Owner:** Engineering  
**Last Updated:** 2025-12-04  
**Related Work:** Epic 3, Story 3 (Versioning Integration with Kanban & RW)

---

## Purpose

This document serves as a **comprehensive reference** for all discovered flaws, anti-patterns, and workflow issues in the Release Workflow (RW). Each flaw is documented with symptoms, root causes, solutions, and pointers to where fixes are implemented.

**Use this document when:**
- A workflow flaw is discovered
- Reviewing workflow procedures
- Onboarding new team members
- Debugging workflow issues
- Strengthening RW procedures

**This document references:**
- Root cause analysis for each flaw
- Step-by-step solutions
- Policy documents
- Fix implementations

---

## Quick Reference: All Known Flaws

| Flaw ID | Step | Symptom | Status | Solution Location |
|---------|------|---------|--------|-------------------|
| [WF-001](#wf-001-story-file-not-updated-first) | Step 6 | Story file lacks forensic markers, Epic matches incomplete state | ✅ FIXED | [Solution](#wf-001-story-file-not-updated-first) |
| [WF-002](#wf-002-version-bump-logic-error) | Step 2 | BUILD incremented instead of TASK for new tasks | ✅ FIXED | [Solution](#wf-002-version-bump-logic-error) |

---

## WF-001: Story File Not Updated First (Step 6)

**Status:** ✅ FIXED  
**Date Discovered:** 2025-12-04  
**Date Fixed:** 2025-12-04  
**Related Work:** Epic 3, Story 3, Task 5

### Quick Reference: The Flaw

**Anti-Pattern:** Story file (authoritative source) wasn't being updated with forensic markers before Epic file was updated to match it.

**Symptom:**
- Story file task checklist lacks forensic markers
- Epic file matches Story file (correct behavior)
- But Epic file also lacks forensic markers (because Story file lacked them)
- Result: Both files in incomplete state

**Example:**
- ❌ **Wrong:** Epic file updated to match Story file, but Story file never updated with `✅ COMPLETE (v0.11.5.2+1)`
- ✅ **Correct:** Story file updated FIRST with forensic markers, then Epic file updated to match

**Impact:** Forensic markers missing from both Story and Epic documents, breaking traceability.

### Root Cause Analysis

**Primary Root Cause:**
- **Location:** RW Step 6 (Auto-update Kanban Docs) instructions
- **Problem:** Step 6 treated Story file as authoritative source but didn't update it
- **Workflow Gap:** One-way sync where Epic matched Story, but Story wasn't updated during RW

**What Happened:**
1. Step 6 read Story file to get "correct state"
2. Step 6 updated Epic file to match Story file
3. But Step 6 never updated Story file with forensic markers
4. Result: Story file (authoritative) lacked markers, Epic matched that incomplete state

**Why It Happened:**
- Step 6 documentation said "read Story file to get correct state" and "update Epic to match Story"
- But it didn't say "update Story file FIRST, then update Epic to match"
- The order of operations wasn't explicit
- Story file was treated as read-only authoritative source, not as something to update

### The Fix

**Solution:** Explicit order requirement in RW Step 6:

1. **FIRST:** Update Story file (`Story-{N}-{Name}.md`) task checklist with forensic markers
2. **THEN:** Update Epic-{epic}.md to match the updated Story file

**Implementation:**
- Updated `release-workflow-agent-execution.md` Step 6 EXECUTE phase
- Updated `cursorrules-rw-trigger-section.md` Step 6 instructions
- Made order explicit: Story file FIRST, then Epic file

**See:**
- `packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md` Step 6
- `packages/frameworks/workflow mgt/cursorrules-rw-trigger-section.md` Step 6

### Prevention

**How to Prevent:**
- Always update Story file FIRST with forensic markers
- Then update Epic file to match the updated Story file
- Follow explicit order: Story → Epic
- Validate both files have forensic markers after update

**Key Principle:**
- Story file is authoritative source, but it must be updated during RW
- Epic file matches Story file, so Story must be updated first

---

## WF-002: Version Bump Logic Error (Step 2)

**Status:** ✅ FIXED  
**Date Discovered:** 2025-12-03  
**Date Fixed:** 2025-12-03  
**Related Work:** Epic 2, Story 2 (PDCA Integration)

### Quick Reference: The Flaw

**Anti-Pattern:** BUILD was incremented instead of TASK when completing new tasks.

**Symptom:**
- Version shows wrong TASK component (e.g., `0.1.1.1+2` for Task 2)
- BUILD increments when it should reset (e.g., `0.1.1.1+3` for Task 3)
- Version doesn't match completed task number

**Example:**
- ❌ **Wrong:** T003 completed → `0.11.1.1+2` (BUILD incremented, TASK unchanged)
- ✅ **Correct:** T003 completed → `0.11.1.3+1` (TASK incremented to 3, BUILD reset to 1)

**Impact:** Multiple tasks can be released with TASK=1, only BUILD incremented (1-9), breaking version traceability.

### Root Cause Analysis

**Primary Root Cause:**
- **Location:** RW Step 2 (Bump Version) instructions
- **Problem:** Vague instruction didn't specify how to determine if task is new or same
- **Missing:** No mandatory Story file read, no task number extraction, no validation

**Why It Happened:**
- Instruction said "increment BUILD for same task, or set new TASK+BUILD=1"
- But didn't specify HOW to determine which case
- No source of truth specified (where to find completed task)
- Agent defaulted to "increment BUILD" without checking

### The Fix

**Solution:** Explicit, mandatory step-by-step procedure in RW Step 2:

1. **MUST** read Story file to identify completed task
2. **MUST** extract task number from task identifier
3. **MUST** compare task number to current VERSION_TASK
4. **MUST** validate before and after updating

**See:**
- `packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md` Step 2
- `packages/frameworks/workflow mgt/cursorrules-rw-trigger-section.md` Step 2
- `KB/Architecture/Standards_and_ADRs/versioning-error-reference-guide.md` (detailed analysis)

### Prevention

**How to Prevent:**
- Always read Story file first (source of truth)
- Always extract task number from task identifier
- Always compare completed task vs. current VERSION_TASK
- Always validate before and after updating

---

## How to Use This Document

### When a New Flaw is Discovered

**Step 1: Document the Flaw**
- Add new entry to "Quick Reference: All Known Flaws" table
- Create detailed section following the template:
  - Quick Reference (symptom, example, impact)
  - Root Cause Analysis
  - The Fix (solution, implementation, pointers)
  - Prevention

**Step 2: Implement the Fix**
- Update relevant workflow documentation
- Update `.cursorrules` if needed
- Update agent execution guides if needed

**Step 3: Update This Document**
- Mark flaw as FIXED
- Add date fixed
- Add pointers to fix implementation
- Update prevention section

### When Reviewing Workflow Procedures

**Checklist:**
- [ ] Review all known flaws in this document
- [ ] Verify fixes are still in place
- [ ] Check if any new flaws have emerged
- [ ] Update prevention strategies if needed

### When Onboarding New Team Members

**Process:**
1. Share this document as context
2. Explain each flaw and why it matters
3. Walk through the fixes
4. Show examples of correct vs. incorrect behavior
5. Emphasize prevention strategies

---

## Related Documentation

### Core Workflow Documents
- **[Release Workflow Agent Execution](../../../packages/frameworks/workflow%20mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md)** - Complete step-by-step guide
- **[Cursor Rules RW Trigger Section](../../../packages/frameworks/workflow%20mgt/cursorrules-rw-trigger-section.md)** - RW trigger instructions
- **[Workflow Hardening Guide](workflow-hardening-guide.md)** - Core principles for workflow design

### Versioning Documents
- **[Versioning Error Reference Guide](versioning-error-reference-guide.md)** - Versioning-specific errors (WF-002 detailed here)
- **[Versioning Policy](dev-kit-versioning-policy.md)** - Versioning schema definition

### Integration Documents
- **[Integration Troubleshooting Guide](../../../packages/frameworks/numbering%20%26%20versioning/integration/integration-troubleshooting-guide.md)** - Integration issues and solutions

---

## Key Takeaways

### Common Patterns in Flaws

1. **Missing Explicit Order:** Steps don't specify order of operations
2. **Missing Mandatory Checks:** Steps don't require reading source of truth
3. **Missing Validation:** Steps don't validate before/after state
4. **Vague Instructions:** Steps use ambiguous language instead of explicit procedures

### How Flaws Are Fixed

1. **Make Order Explicit:** Specify FIRST/THEN order of operations
2. **Add Mandatory Checks:** Require reading source of truth
3. **Add Validation:** Require before/after validation
4. **Clarify Instructions:** Replace vague language with explicit step-by-step procedures

### How to Prevent Future Flaws

1. **Follow Explicit Procedures:** Don't skip steps, follow order
2. **Read Source of Truth First:** Always read authoritative sources
3. **Validate Everything:** Check before and after state
4. **Document Decisions:** Show your work, explain choices

---

## Version History

| Date | Version | Changes |
| --- | --- | --- |
| 2025-12-04 | 1.0 | Initial document created with WF-001 (Story file not updated first) and WF-002 (Version bump logic error) |

---

## Contact and Escalation

**If a new flaw is discovered:**
1. Document it in this guide following the template
2. Implement the fix
3. Update this document with fix details
4. Update related documentation
5. Escalate if fix needs further refinement

**Questions or issues:**
- Review related documentation (see "Related Documentation" section)
- Check workflow execution guides for current procedures
- Verify fixes are still in place

---

_Last updated: 2025-12-04_  
_This document should be updated whenever a new workflow flaw is discovered or fixed._

