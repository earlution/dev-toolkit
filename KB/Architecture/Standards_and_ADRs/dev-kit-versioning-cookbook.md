---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-04T12:01:47Z
expires_at: null
housekeeping_policy: keep
---

# Versioning Cookbook

**Task:** E3:S02:T02 – Create versioning cookbook document with worked examples  
**Date:** 2025-12-03  
**Status:** ✅ COMPLETE  
**Version:** v0.3.2.3+1

---

## Executive Summary

This cookbook provides **practical, worked examples** for using the `RC.EPIC.STORY.TASK+BUILD` versioning schema. Each example shows:

- **Before/after version** transitions
- **Kanban context** (Epic/Story/Task)
- **RW perspective** (how Release Workflow interprets and handles the version)
- **Real dev-kit examples** where available

**Target Audience:**
- Developers adopting the versioning framework
- AI agents executing Release Workflow
- Project maintainers managing version progression

**Safe to Copy:** All examples are **project-agnostic** and safe to copy into other projects.

---

## Table of Contents

1. [New Epic](#1-new-epic)
2. [New Story Under Existing Epic](#2-new-story-under-existing-epic)
3. [New Task Under Existing Story](#3-new-task-under-existing-story)
4. [Bugfix/Hotfix on Existing Task](#4-bugfixhotfix-on-existing-task)
5. [Parallel Epics and Stories](#5-parallel-epics-and-stories)
6. [Task Transitions](#6-task-transitions)
7. [Story Completion](#7-story-completion)
8. [Epic Completion](#8-epic-completion)
9. [Cross-Framework Examples](#9-cross-framework-examples)
   - [Example 1: FR → Task → Version → RW → Kanban Update](#example-1-fr--task--version--rw--kanban-update)
   - [Example 2: Bugfix with Verification Requirement](#example-2-bugfix-with-verification-requirement)
   - [Example 3: Parallel Epic/Story Work](#example-3-parallel-epicstory-work)

---

## 1. New Epic

### Scenario

Starting a completely new epic that has no prior work in the repository.

**Example:** Creating Epic 5 for "Documentation Framework" when Epics 1-4 already exist.

### Worked Example

**Before:**
- Last version: `0.4.3.7+1` (Epic 4, Story 3, Task 7, Build 1)
- No Epic 5 exists yet

**After:**
- New version: `0.5.1.1+1` (Epic 5, Story 1, Task 1, Build 1)

### Version File Update

**Before (`version.py`):**
```python
VERSION_RC = 0
VERSION_EPIC = 4      # Previous epic
VERSION_STORY = 3
VERSION_TASK = 7
VERSION_BUILD = 1
```

**After (`version.py`):**
```python
VERSION_RC = 0
VERSION_EPIC = 5      # NEW: Increment to new epic
VERSION_STORY = 1      # NEW: Reset to first story
VERSION_TASK = 1       # NEW: Reset to first task
VERSION_BUILD = 1      # NEW: Reset to first build
```

### Kanban Context

**Epic Document:** `KB/PM_and_Portfolio/kanban/epics/Epic-5.md`
```markdown
# Epic 5: Documentation Framework

**Status:** IN PROGRESS
**Version Schema:** `0.5.S.T+B`

## Story Checklist
- [ ] **E5:S01 – Framework Documentation Structure** - TODO
```

**Story Document:** `KB/PM_and_Portfolio/kanban/epics/Epic-5/stories/Story-001-*.md`
```markdown
# Story 001 – Framework Documentation Structure

**Status:** IN PROGRESS
**Epic:** Epic 5
**Story:** Story 1

## Task Checklist
- [ ] **E5:S01:T01 – Define documentation structure** - TODO
```

### RW Perspective

**RW Step 1: Branch Safety Check**
- Validates branch: `epic/5-documentation-framework`
- Validates version matches: `0.5.1.1+1` matches Epic 5

**RW Step 2: Bump Version**
- Detects new epic (EPIC changed from 4 to 5)
- Confirms STORY=1, TASK=1, BUILD=1 (all reset)

**RW Step 3: Create Detailed Changelog**
- Creates: `CHANGELOG_v0.5.1.1+1.md`
- Includes Epic 5 context

**RW Step 6: Auto-update Kanban Docs**
- Updates Epic-5.md with version marker
- Updates Story-001-*.md with version marker

### Real Dev-Kit Example

**Epic 1 Start:**
- First version: `0.1.1.1+1` (Epic 1, Story 1, Task 1)
- See: `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.1.1.1+1.md`

---

## 2. New Story Under Existing Epic

### Scenario

Adding a new story to an existing epic that already has one or more stories.

**Example:** Adding Story 2 to Epic 3 when Story 1 already exists and is complete.

### Worked Example

**Before:**
- Last version: `0.3.1.6+1` (Epic 3, Story 1, Task 6, Build 1)
- Story 1 is COMPLETE

**After:**
- New version: `0.3.2.1+1` (Epic 3, Story 2, Task 1, Build 1)

### Version File Update

**Before (`version.py`):**
```python
VERSION_RC = 0
VERSION_EPIC = 3
VERSION_STORY = 1      # Previous story
VERSION_TASK = 6
VERSION_BUILD = 1
```

**After (`version.py`):**
```python
VERSION_RC = 0
VERSION_EPIC = 3       # Unchanged
VERSION_STORY = 2      # NEW: Increment to next story
VERSION_TASK = 1       # NEW: Reset to first task
VERSION_BUILD = 1      # NEW: Reset to first build
```

### Kanban Context

**Epic Document:** `KB/PM_and_Portfolio/kanban/epics/Epic-3.md`
```markdown
## Story Checklist
- [x] **E3:S01 – Dev Kit Alignment with Versioning Framework** - COMPLETE ✅ (v0.3.1.6+1)
- [ ] **E3:S02 – Versioning Cookbook & Examples** - IN PROGRESS
```

**Story Document:** `KB/PM_and_Portfolio/kanban/epics/Epic-3/stories/Story-002-*.md`
```markdown
# Story 002 – Versioning Cookbook & Examples

**Status:** IN PROGRESS
**Epic:** Epic 3
**Story:** Story 2

## Task Checklist
- [ ] **E3:S02:T01 – Define core versioning scenarios** - TODO
```

### RW Perspective

**RW Step 1: Branch Safety Check**
- Validates branch: `epic/3-numbering-and-versioning-framework`
- Validates version matches: `0.3.2.1+1` matches Epic 3

**RW Step 2: Bump Version**
- Detects story progression (STORY changed from 1 to 2)
- Confirms TASK=1, BUILD=1 (both reset)

**RW Step 3: Create Detailed Changelog**
- Creates: `CHANGELOG_v0.3.2.1+1.md`
- Includes Epic 3, Story 2 context

**RW Step 6: Auto-update Kanban Docs**
- Updates Epic-3.md with Story 2 reference
- Updates Story-002-*.md with version marker

### Real Dev-Kit Example

**Epic 1 Story Progression:**
- Story 1: `0.1.1.1+1` → `0.1.1.1+2`
- Story 2: `0.1.2.1+1` → `0.1.2.5+1`
- Story 3: `0.1.3.1+1` → `0.1.3.6+1`
- See: `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.1.2.1+1.md`

---

## 3. New Task Under Existing Story

### Scenario

Adding a new task to an existing story that already has one or more tasks.

**Example:** Completing Task 1 (`0.3.1.1+3`) and starting Task 2 (`0.3.1.2+1`).

### Worked Example

**Before:**
- Last version: `0.3.1.1+3` (Epic 3, Story 1, Task 1, Build 3)
- Task 1 is COMPLETE

**After:**
- New version: `0.3.1.2+1` (Epic 3, Story 1, Task 2, Build 1)

### Version File Update

**Before (`version.py`):**
```python
VERSION_RC = 0
VERSION_EPIC = 3
VERSION_STORY = 1
VERSION_TASK = 1       # Previous task
VERSION_BUILD = 3      # Previous build
```

**After (`version.py`):**
```python
VERSION_RC = 0
VERSION_EPIC = 3       # Unchanged
VERSION_STORY = 1      # Unchanged
VERSION_TASK = 2       # NEW: Increment to next task
VERSION_BUILD = 1      # NEW: Reset to 1 for new task
```

### Kanban Context

**Story Document:** `KB/PM_and_Portfolio/kanban/epics/Epic-3/stories/Story-001-*.md`
```markdown
## Task Checklist
- [x] **E3:S01:T01 – Review dev-kit versioning policy vs framework policy** ✅ COMPLETE (v0.3.1.1+2)
- [ ] **E3:S01:T02 – Ingest versioning findings from fynd.deals Epic 15 work** - TODO
```

### RW Perspective

**RW Step 1: Branch Safety Check**
- Validates branch: `epic/3-numbering-and-versioning-framework`
- Validates version matches: `0.3.1.2+1` matches Epic 3, Story 1

**RW Step 2: Bump Version**
- **CRITICAL:** Detects task transition
- Compares `VERSION_TASK` in `version.py` (currently 1) with active Task in Story document (Task 2)
- **Automatically updates** `VERSION_TASK` to 2
- **Automatically resets** `VERSION_BUILD` to 1
- This is the **automatic task transition handling**

**RW Step 3: Create Detailed Changelog**
- Creates: `CHANGELOG_v0.3.1.2+1.md`
- Includes Epic 3, Story 1, Task 2 context

**RW Step 6: Auto-update Kanban Docs**
- Updates Story document with Task 1 completion marker: `✅ COMPLETE (v0.3.1.1+3)`
- Updates Story document with Task 2 start marker

### Real Dev-Kit Example

**Epic 1 Story 2 Task Progression:**
- Task 1: `0.1.2.1+1`
- Task 2: `0.1.2.2+1`
- Task 3: `0.1.2.3+1`
- Task 4: `0.1.2.4+1`
- Task 5: `0.1.2.5+1`
- See: `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.1.2.2+1.md`

---

## 4. Bugfix/Hotfix on Existing Task

### Scenario

Fixing a bug or issue in a task that is either in progress or completed.

**Example:** Fixing a bug discovered in Task 3 after it was completed and released as `v0.3.1.3+1`.

### Worked Example: In-Progress Task Bugfix

**Before:**
- Current version: `0.3.1.3+1` (Epic 3, Story 1, Task 3, Build 1)
- Bug discovered while Task 3 is still in progress

**After:**
- Fixed version: `0.3.1.3+2` (Epic 3, Story 1, Task 3, Build 2)

### Version File Update

**Before (`version.py`):**
```python
VERSION_RC = 0
VERSION_EPIC = 3
VERSION_STORY = 1
VERSION_TASK = 3
VERSION_BUILD = 1      # Previous build
```

**After (`version.py`):**
```python
VERSION_RC = 0
VERSION_EPIC = 3       # Unchanged
VERSION_STORY = 1      # Unchanged
VERSION_TASK = 3       # Unchanged (same task)
VERSION_BUILD = 2      # Increment build number
```

### Worked Example: Completed Task Hotfix

**Before:**
- Completed version: `0.3.1.3+1` (Epic 3, Story 1, Task 3, Build 1)
- Task 3 marked COMPLETE
- Bug discovered later

**After:**
- Hotfix version: `0.3.1.3+2` (Epic 3, Story 1, Task 3, Build 2)

**Version File Update:** Same as in-progress bugfix (BUILD increments)

### Kanban Context

**Story Document:**
```markdown
## Task Checklist
- [x] **E3:S01:T03 – Update dev-kit versioning policy as canonical SoT** ✅ COMPLETE (v0.3.1.3+1)
  - Bugfix: Fixed policy reference issue ✅ COMPLETE (v0.3.1.3+2)
```

### RW Perspective

**RW Step 1: Branch Safety Check**
- Validates branch: `epic/3-numbering-and-versioning-framework`
- Validates version matches: `0.3.1.3+2` matches Epic 3, Story 1, Task 3

**RW Step 2: Bump Version**
- Detects same task (TASK unchanged)
- Increments BUILD from 1 to 2

**RW Step 3: Create Detailed Changelog**
- **CRITICAL:** RW Step 3 requires fix verification
- If fix is **verified** (tested):
  ```markdown
  ### Fixed
  - Fixed policy reference issue in versioning policy
  ```
- If fix is **unverified** (not yet tested):
  ```markdown
  ### Attempted Fixes
  - Attempted fix: Policy reference issue (verification pending)
  ```
- RW **stops** if unverified fixes are marked as "Fixed"

**RW Step 6: Auto-update Kanban Docs**
- Updates Story document with bugfix marker
- Includes verification status

### Real Dev-Kit Example

**Epic 4 Story 3 Task 2 Bugfix:**
- Original: `0.4.3.2+1` (Task 2 complete)
- Bugfix: `0.4.3.2+2` (Critical issue resolution)
- See: `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.4.3.2+2.md`

---

## 5. Parallel Epics and Stories

### Scenario

Working on multiple epics or stories simultaneously, where work happens in parallel branches and may be merged out of chronological order.

**Example:** 
- Epic 3 work on `epic/3-*` branch
- Epic 4 work on `epic/4-*` branch
- Both branches merged to `main` at different times

### Worked Example

**Epic 3 Branch:**
- Work: `0.3.1.1+1`, `0.3.1.2+1`, `0.3.2.1+1`
- Merged to `main` on 2025-12-03

**Epic 4 Branch:**
- Work: `0.4.1.1+1`, `0.4.2.1+1`, `0.4.3.1+1`
- Merged to `main` on 2025-12-02 (earlier than Epic 3)

### Version File Update

**On Epic 3 Branch (`epic/3-*`):**
```python
VERSION_RC = 0
VERSION_EPIC = 3       # Epic 3 context
VERSION_STORY = 2
VERSION_TASK = 1
VERSION_BUILD = 1
```

**On Epic 4 Branch (`epic/4-*`):**
```python
VERSION_RC = 0
VERSION_EPIC = 4       # Epic 4 context
VERSION_STORY = 3
VERSION_TASK = 1
VERSION_BUILD = 1
```

### Kanban Context

**Kanban Board:** Shows both epics in parallel
```markdown
### Epic 3: Numbering & Versioning Framework
**Status:** IN PROGRESS
- Story 1: COMPLETE ✅
- Story 2: IN PROGRESS

### Epic 4: Kanban Framework
**Status:** COMPLETE ✅
- Story 1: COMPLETE ✅
- Story 2: COMPLETE ✅
- Story 3: COMPLETE ✅
```

### RW Perspective

**RW Step 1: Branch Safety Check**
- Epic 3 branch: Validates `0.3.2.1+1` matches `epic/3-*` branch
- Epic 4 branch: Validates `0.4.3.1+1` matches `epic/4-*` branch
- **No conflicts** between parallel epic versions

**RW Step 3: Create Detailed Changelog**
- Each epic creates its own changelog entries
- Changelogs ordered **canonically by version number**, not by commit time

**Changelog Ordering (Canonical):**
```markdown
## [0.3.1.1+1] - 03-12-25    # Epic 3, Story 1, Task 1
## [0.3.1.2+1] - 03-12-25    # Epic 3, Story 1, Task 2
## [0.4.1.1+1] - 02-12-25    # Epic 4, Story 1, Task 1 (merged earlier, but ordered correctly)
## [0.4.2.1+1] - 02-12-25    # Epic 4, Story 2, Task 1
## [0.4.3.1+1] - 02-12-25    # Epic 4, Story 3, Task 1
## [0.3.2.1+1] - 03-12-25    # Epic 3, Story 2, Task 1 (merged later, but ordered correctly)
```

**Key Point:** Version numbers determine order, not timestamps.

### Real Dev-Kit Example

**Parallel Epic Development:**
- Epic 1: `0.1.1.1+1` → `0.1.3.6+1` (completed)
- Epic 2: `0.2.1.1+2` → `0.2.1.1+5` (completed)
- Epic 3: `0.3.1.1+1` → `0.3.2.1+1` (in progress)
- Epic 4: `0.4.1.1+1` → `0.4.3.7+1` (completed)
- See: `CHANGELOG.md` for canonical ordering

---

## 6. Task Transitions

### Scenario

Moving from one task to another within the same story, where the previous task is complete and a new task is starting.

**Example:** Completing Task 1 (`0.3.1.1+3`) and starting Task 2 (`0.3.1.2+1`).

### Worked Example

**Before:**
- Last version: `0.3.1.1+3` (Epic 3, Story 1, Task 1, Build 3)
- Task 1 marked COMPLETE

**After:**
- New version: `0.3.1.2+1` (Epic 3, Story 1, Task 2, Build 1)

### Version File Update

**Before (`version.py`):**
```python
VERSION_RC = 0
VERSION_EPIC = 3
VERSION_STORY = 1
VERSION_TASK = 1       # Previous task
VERSION_BUILD = 3      # Previous build
```

**After (`version.py`):**
```python
VERSION_RC = 0
VERSION_EPIC = 3       # Unchanged
VERSION_STORY = 1      # Unchanged
VERSION_TASK = 2       # Increment to next task
VERSION_BUILD = 1      # Reset to 1 for new task
```

### Kanban Context

**Story Document:**
```markdown
## Task Checklist
- [x] **E3:S01:T01 – Review dev-kit versioning policy vs framework policy** ✅ COMPLETE (v0.3.1.1+2)
- [ ] **E3:S01:T02 – Ingest versioning findings from fynd.deals Epic 15 work** - TODO
```

### RW Perspective

**RW Step 1: Branch Safety Check**
- Validates branch: `epic/3-numbering-and-versioning-framework`
- **CRITICAL:** Validates `VERSION_TASK` in `version.py` matches active Task in Story document
- If mismatch detected: RW stops with clear error message

**RW Step 2: Bump Version**
- **CRITICAL:** RW Step 2 detects task transition automatically
- Compares `VERSION_TASK` in `version.py` (currently 1) with active Task in Story document (Task 2)
- **Automatically updates** `VERSION_TASK` to 2
- **Automatically resets** `VERSION_BUILD` to 1
- This ensures correct version progression

**RW Step 3: Create Detailed Changelog**
- Creates: `CHANGELOG_v0.3.1.2+1.md`
- Includes Task 1 completion context
- Includes Task 2 start context

**RW Step 6: Auto-update Kanban Docs**
- Updates Story document with Task 1 completion marker: `✅ COMPLETE (v0.3.1.1+3)`
- Updates Story document with Task 2 start marker

### Common Mistakes to Avoid

❌ **Manually updating `VERSION_TASK` without RW detection**
- Let RW handle task transitions automatically

❌ **Forgetting to reset `VERSION_BUILD` to 1**
- RW automatically resets BUILD when TASK changes

❌ **Starting new task with same BUILD number**
- BUILD must reset to 1 for new task

### Real Dev-Kit Example

**Epic 1 Story 3 Task Transitions:**
- Task 1: `0.1.3.1+1`
- Task 2: `0.1.3.2+1`
- Task 3: `0.1.3.3+1`
- Task 4: `0.1.3.4+1`
- Task 5: `0.1.3.5+1`
- Task 6: `0.1.3.6+1`
- See: `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.1.3.2+1.md`

---

## 7. Story Completion

### Scenario

Completing all tasks in a story, marking the story as complete.

**Example:** Completing Story 1 in Epic 3 after Tasks 1-6 are all complete.

### Worked Example

**Before:**
- Last version: `0.3.1.6+1` (Epic 3, Story 1, Task 6, Build 1)
- All tasks in Story 1 are COMPLETE

**After:**
- Story 1 marked COMPLETE
- Next story (if exists): `0.3.2.1+1` (Epic 3, Story 2, Task 1, Build 1)

### Version File Update

**For Story Completion:**
- No version change needed (last task version remains: `0.3.1.6+1`)

**For Next Story:**
```python
VERSION_RC = 0
VERSION_EPIC = 3       # Unchanged
VERSION_STORY = 2      # Increment to next story
VERSION_TASK = 1       # Reset to first task
VERSION_BUILD = 1      # Reset to first build
```

### Kanban Context

**Epic Document:** `KB/PM_and_Portfolio/kanban/epics/Epic-3.md`
```markdown
## Story Checklist
- [x] **E3:S01 – Dev Kit Alignment with Versioning Framework** - COMPLETE ✅ (v0.3.1.6+1)
- [ ] **E3:S02 – Versioning Cookbook & Examples** - IN PROGRESS
```

**Story Document:** `KB/PM_and_Portfolio/kanban/epics/Epic-3/stories/Story-001-*.md`
```markdown
**Status:** COMPLETE ✅
**Completed:** 2025-12-02 (v0.3.1.6+1)

## Task Checklist
- [x] **E3:S01:T01** ✅ COMPLETE (v0.3.1.1+2)
- [x] **E3:S01:T02** ✅ COMPLETE (v0.3.1.2+1)
- [x] **E3:S01:T03** ✅ COMPLETE (v0.3.1.3+1)
- [x] **E3:S01:T04** ✅ COMPLETE (v0.3.1.4+1)
- [x] **E3:S01:T05** ✅ COMPLETE (v0.3.1.5+1)
- [x] **E3:S01:T06** ✅ COMPLETE (v0.3.1.6+1)
```

### RW Perspective

**RW Step 6: Auto-update Kanban Docs**
- Updates Story document with COMPLETE status
- Updates Epic document with story completion marker: `✅ COMPLETE (v0.3.1.6+1)`
- Updates Kanban board

**When Starting Next Story:**
- RW handles story transition (see Scenario 2)
- Version updates to `0.3.2.1+1`

### Real Dev-Kit Example

**Epic 1 Story Completion:**
- Story 1: Completed at `v0.1.1.1+2`
- Story 2: Completed at `v0.1.2.5+1`
- Story 3: Completed at `v0.1.3.6+1`
- See: `KB/PM_and_Portfolio/kanban/epics/Epic-1.md`

---

## 8. Epic Completion

### Scenario

Completing all stories in an epic, marking the epic as complete.

**Example:** Completing Epic 4 after Stories 1-3 are all complete.

### Worked Example

**Before:**
- Last version: `0.4.3.7+1` (Epic 4, Story 3, Task 7, Build 1)
- All stories in Epic 4 are COMPLETE

**After:**
- Epic 4 marked COMPLETE
- Next epic (if exists): `0.5.1.1+1` (Epic 5, Story 1, Task 1, Build 1)

### Version File Update

**For Epic Completion:**
- No version change needed (last story version remains: `0.4.3.7+1`)

**For Next Epic:**
```python
VERSION_RC = 0
VERSION_EPIC = 5      # Increment to next epic
VERSION_STORY = 1     # Reset to first story
VERSION_TASK = 1      # Reset to first task
VERSION_BUILD = 1     # Reset to first build
```

### Kanban Context

**Epic Document:** `KB/PM_and_Portfolio/kanban/epics/Epic-4.md`
```markdown
**Status:** COMPLETE ✅
**Completed:** 2025-12-02 (v0.4.3.7+1)

## Story Checklist
- [x] **E4:S01 – Dev Kit Kanban Implementation** - COMPLETE ✅ (v0.4.1.1+6)
- [x] **E4:S02 – FR/BR Intake to Tasks** - COMPLETE ✅ (v0.4.2.5+1)
- [x] **E4:S03 – Kanban + Versioning + RW Integration** - COMPLETE ✅ (v0.4.3.7+1)
```

**Kanban Board:**
```markdown
### Epic 4: Kanban Framework
**Status:** COMPLETE ✅
**Last Updated:** v0.4.3.7+1
```

### RW Perspective

**RW Step 6: Auto-update Kanban Docs**
- Updates Epic document with COMPLETE status
- Updates Kanban board with epic completion marker
- All stories remain marked COMPLETE

**When Starting Next Epic:**
- RW handles epic transition (see Scenario 1)
- Version updates to `0.5.1.1+1`

### Real Dev-Kit Example

**Epic 4 Completion:**
- Epic 4: Completed at `v0.4.3.7+1`
- All 3 stories completed
- See: `KB/PM_and_Portfolio/kanban/epics/Epic-4.md`

---

## 9. Cross-Framework Examples

This section demonstrates **end-to-end flows** that tie together Kanban, Versioning, and Release Workflow. These examples show how the three frameworks work together in practice.

---

### Example 1: FR → Task → Version → RW → Kanban Update

**Scenario:** A Feature Request arrives and flows through the complete system from intake to release.

#### Step 1: Receive Feature Request

**FR Document:** `KB/PM_and_Portfolio/kanban/fr-br/FR-001-add-validation-script.md`
```markdown
# Feature Request: Add Kanban Consistency Validation Script

**Summary:** Add validation script to check Kanban document consistency
**Priority:** HIGH
**Scope:** Epic 4 (Kanban Framework)
**Status:** Received
```

#### Step 2: Intake Decision (FR → Task)

**Process:**
1. Search Epic 4 stories for matching scope
2. Found: Story 3 (Kanban + Versioning + RW Integration) - matches scope
3. Decision: Create Task under Story 3

**Task Created:**
- Task: E4:S03:T08 – Add Kanban consistency validation script
- Added to `Story-003-kanban-versioning-rw-integration.md`
- Task status: TODO

#### Step 3: Assign Version Number

**Current Version:** `0.4.3.5+1` (Task 5)
**New Task:** Task 8

**Version File Update (`version.py`):**
```python
VERSION_RC = 0
VERSION_EPIC = 4       # Unchanged (Epic 4)
VERSION_STORY = 3      # Unchanged (Story 3)
VERSION_TASK = 8      # NEW: Task 8
VERSION_BUILD = 1     # Reset to 1 for new Task
```

**Expected Version:** `0.4.3.8+1`

#### Step 4: Complete Work

**Work Completed:**
- Created validation script: `scripts/validation/validate_kanban_consistency.py`
- Tested script
- Work ready for release

#### Step 5: Trigger Release Workflow

**Developer types:** `RW`

**RW Step 1: Branch Safety Check**
- ✅ Branch: `epic/4-kanban-framework`
- ✅ Version `0.4.3.8+1` matches Epic 4
- ✅ `VERSION_TASK` (8) matches active Task in Story document

**RW Step 2: Bump Version**
- ✅ Detects task transition (Task 5 → Task 8)
- ✅ Confirms `VERSION_TASK` updated to 8
- ✅ Confirms `VERSION_BUILD` reset to 1
- ✅ Version: `0.4.3.8+1`

**RW Step 3: Create Detailed Changelog**
- ✅ Creates: `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.4.3.8+1.md`
- ✅ Includes Epic 4, Story 3, Task 8 context
- ✅ Includes full timestamp: `2025-12-02 18:00:00 UTC`

**RW Step 4: Update Main Changelog**
- ✅ Adds entry: `## [0.4.3.8+1] - 02-12-25`
- ✅ Includes summary and link to detailed changelog

**RW Step 5: Update README**
- ✅ Updates version badge (if applicable)
- ✅ Updates latest release callout

**RW Step 6: Auto-update Kanban Docs**
- ✅ Updates `Epic-4.md`:
  - `**Last updated:** 2025-12-02 (v0.4.3.8+1 – Task 8 complete: Add Kanban consistency validation script)`
  - Story Checklist: `- [ ] **E4:S03 – ...** - IN PROGRESS (v0.4.3.8+1)`
- ✅ Updates `Story-003-kanban-versioning-rw-integration.md`:
  - `**Last updated:** 2025-12-02 (v0.4.3.8+1)`
  - `**Version:** v0.4.3.8+1`
  - Task Checklist: `- [x] **E4:S03:T08 – Add Kanban consistency validation script** ✅ COMPLETE (v0.4.3.8+1)`
  - Task section: `**Status:** ✅ **COMPLETE** (v0.4.3.8+1)`

**RW Steps 7-11: Git Operations**
- ✅ Stage files
- ✅ Run validators
- ✅ Commit: `Release v0.4.3.8+1: Task 8 complete - Add Kanban consistency validation script`
- ✅ Tag: `v0.4.3.8+1`
- ✅ Push to remote

#### Result

**Complete Traceability:**
- FR → Task (E4:S03:T08)
- Task → Version (`0.4.3.8+1`)
- Version → Changelog (`CHANGELOG_v0.4.3.8+1.md`)
- Version → Kanban markers (`✅ COMPLETE (v0.4.3.8+1)`)
- Version → Git tag (`v0.4.3.8+1`)

**All Systems Updated:**
- ✅ Kanban: Task marked complete with forensic marker
- ✅ Versioning: Version file updated, changelog created
- ✅ RW: All 11 steps executed successfully
- ✅ Git: Committed and tagged

---

### Example 2: Bugfix with Verification Requirement

**Scenario:** A bug is discovered in a completed task, requiring fix verification before marking as "Fixed".

#### Step 1: Discover Bug

**Bug Context:**
- Task: E4:S03:T02 – Validate Kanban → Versioning integration
- Completed version: `v0.4.3.2+1`
- Bug: `VERSION_TASK` not correctly updated during task transitions

#### Step 2: Create Bugfix Task

**Task Created:**
- Task: E4:S03:T02 (bugfix) – Fix Task → version TASK component mapping
- Same task number (bugfix on existing task)
- Version: `0.4.3.2+2` (BUILD increments)

#### Step 3: Implement Fix

**Fix Implemented:**
- Updated RW Step 2 to detect task transitions
- Updated RW Step 2 to automatically update `VERSION_TASK`
- Updated RW Step 2 to reset `VERSION_BUILD` to 1
- **Fix NOT yet verified** (no tests run yet)

#### Step 4: Trigger Release Workflow

**Developer types:** `RW`

**RW Step 1: Branch Safety Check**
- ✅ Branch: `epic/4-kanban-framework`
- ✅ Version `0.4.3.2+2` matches Epic 4, Story 3, Task 2

**RW Step 2: Bump Version**
- ✅ Same task (TASK=2 unchanged)
- ✅ Increments BUILD: `0.4.3.2+1` → `0.4.3.2+2`

**RW Step 3: Create Detailed Changelog**
- ✅ Creates: `CHANGELOG_v0.4.3.2+2.md`
- ✅ **CRITICAL:** RW Step 3 checks fix verification status
- ✅ Fix is **unverified** (no tests run)
- ✅ Changelog format:
  ```markdown
  ### Attempted Fixes
  - Attempted fix: Task → version TASK component mapping (verification pending)
  ```
- ✅ RW **does not** mark as "Fixed" (verification required)

**RW Step 4: Update Main Changelog**
- ✅ Adds entry with "Attempted Fixes" section
- ✅ Does not add to "Fixed" section

**RW Step 6: Auto-update Kanban Docs**
- ✅ Updates Story document with bugfix context
- ✅ Includes verification status: "verification pending"

#### Step 5: Verify Fix

**Verification Process:**
- Run test suite: ✅ PASS
- Manual verification: ✅ PASS
- Fix verified

#### Step 6: Update Changelog (Post-Verification)

**Option A: Create New Release**
- New version: `0.4.3.2+3`
- Changelog: `### Fixed` section with verified fix

**Option B: Update Existing Release**
- Update `CHANGELOG_v0.4.3.2+2.md`:
  - Move from "Attempted Fixes" to "Fixed"
  - Add verification timestamp
  - Note: This requires manual update (RW doesn't retroactively update)

#### Result

**Verification Workflow:**
- ✅ Unverified fixes logged as "Attempted Fixes"
- ✅ Verified fixes logged as "Fixed"
- ✅ Clear distinction between attempted and verified fixes
- ✅ Prevents false "Fixed" claims

**Real Dev-Kit Example:**
- See: `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.4.3.2+2.md`
- Bugfix: Task → version TASK component mapping
- Verification: Root cause analysis and documentation updates completed

---

### Example 3: Parallel Epic/Story Work

**Scenario:** Working on multiple epics simultaneously, with work merged out of chronological order.

#### Context

**Epic 3 Branch (`epic/3-*`):**
- Work: `0.3.1.1+1`, `0.3.1.2+1`, `0.3.2.1+1`
- Merged to `main` on 2025-12-03

**Epic 4 Branch (`epic/4-*`):**
- Work: `0.4.1.1+1`, `0.4.2.1+1`, `0.4.3.1+1`
- Merged to `main` on 2025-12-02 (earlier than Epic 3)

#### Kanban State

**Epic 3:**
- Story 1: IN PROGRESS (Tasks 1-2 complete)
- Story 2: IN PROGRESS (Task 1 complete)

**Epic 4:**
- Story 1: COMPLETE ✅
- Story 2: COMPLETE ✅
- Story 3: IN PROGRESS (Task 1 complete)

#### Version File States

**On Epic 3 Branch:**
```python
VERSION_RC = 0
VERSION_EPIC = 3
VERSION_STORY = 2
VERSION_TASK = 1
VERSION_BUILD = 1
```

**On Epic 4 Branch:**
```python
VERSION_RC = 0
VERSION_EPIC = 4
VERSION_STORY = 3
VERSION_TASK = 1
VERSION_BUILD = 1
```

#### RW Execution (Parallel)

**Epic 3 RW (on `epic/3-*` branch):**
- ✅ Step 1: Validates branch `epic/3-*` matches version `0.3.2.1+1`
- ✅ Step 2: Bumps version (if needed)
- ✅ Step 3: Creates `CHANGELOG_v0.3.2.1+1.md`
- ✅ Step 6: Updates Epic-3.md and Story-002-*.md

**Epic 4 RW (on `epic/4-*` branch):**
- ✅ Step 1: Validates branch `epic/4-*` matches version `0.4.3.1+1`
- ✅ Step 2: Bumps version (if needed)
- ✅ Step 3: Creates `CHANGELOG_v0.4.3.1+1.md`
- ✅ Step 6: Updates Epic-4.md and Story-003-*.md

**No Conflicts:** Each epic maintains independent version stream

#### Changelog Ordering (Canonical)

**Main Changelog (`CHANGELOG.md`):**
```markdown
## [0.3.1.1+1] - 03-12-25    # Epic 3, Story 1, Task 1
## [0.3.1.2+1] - 03-12-25    # Epic 3, Story 1, Task 2
## [0.4.1.1+1] - 02-12-25    # Epic 4, Story 1, Task 1 (merged earlier, but ordered correctly)
## [0.4.2.1+1] - 02-12-25    # Epic 4, Story 2, Task 1
## [0.4.3.1+1] - 02-12-25    # Epic 4, Story 3, Task 1
## [0.3.2.1+1] - 03-12-25    # Epic 3, Story 2, Task 1 (merged later, but ordered correctly)
```

**Key Point:** Versions ordered **canonically by version number**, not by commit timestamp.

#### Result

**Parallel Development Supported:**
- ✅ Each epic maintains independent version stream
- ✅ No version conflicts between epics
- ✅ Changelog ordering is canonical (by version number)
- ✅ Git history reflects actual commit order
- ✅ Kanban board shows all epics in parallel

**Real Dev-Kit Example:**
- Epic 1: `0.1.1.1+1` → `0.1.3.6+1` (completed)
- Epic 2: `0.2.1.1+2` → `0.2.1.1+5` (completed)
- Epic 3: `0.3.1.1+1` → `0.3.2.2+1` (in progress)
- Epic 4: `0.4.1.1+1` → `0.4.3.7+1` (completed)
- See: `CHANGELOG.md` for canonical ordering

---

## Quick Reference: Version Component Rules

| Component | When It Changes | When It Resets | Example |
|-----------|----------------|----------------|---------|
| **RC** | Entering RC phase | N/A | `0` → `1` |
| **EPIC** | Starting new epic | Never | `3` → `4` |
| **STORY** | Starting new story | When EPIC changes | `1` → `2` |
| **TASK** | Starting new task | When STORY changes | `1` → `2` |
| **BUILD** | Every release | When TASK changes | `1` → `2` → `3` |

---

## Quick Reference: Version Progression Patterns

| Scenario | EPIC | STORY | TASK | BUILD | Example |
|----------|------|-------|------|-------|---------|
| **New Epic** | Increment | 1 | 1 | 1 | `0.5.1.1+1` |
| **New Story** | Same | Increment | 1 | 1 | `0.3.2.1+1` |
| **New Task** | Same | Same | Increment | 1 | `0.3.1.2+1` |
| **Bugfix** | Same | Same | Same | Increment | `0.3.1.3+2` |
| **Task Transition** | Same | Same | Increment | 1 | `0.3.1.2+1` |

---

## References

- **Scenario Definitions:** `KB/PM_and_Portfolio/kanban/epics/Epic-3/stories/Story-002-versioning-cookbook-and-examples/T001-core-versioning-scenarios.md`
- **Versioning Policy:** `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md`
- **Framework Policy:** `packages/frameworks/numbering & versioning/versioning-policy.md`
- **Integration Guide:** `KB/Architecture/Standards_and_ADRs/dev-kit-kanban-versioning-rw-integration.md`
- **Integration Examples:** `KB/PM_and_Portfolio/kanban/epics/Epic-4/stories/Story-003-kanban-versioning-rw-integration/T006-integration-examples.md`
- **RW Execution Guide:** `packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md`

---

## Copying This Cookbook

**Safe to Copy:** This cookbook is **project-agnostic** and safe to copy into other projects.

**Customization:**
- Replace dev-kit examples with your project's examples
- Update file paths to match your project structure
- Adjust epic ranges if your project uses different ranges

**Maintain Links:** Keep references to framework policies and guides.

---

_End of Versioning Cookbook_

