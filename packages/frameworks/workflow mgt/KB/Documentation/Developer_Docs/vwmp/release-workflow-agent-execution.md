# Release Workflow: Agent Execution Guide

**Version:** 1.0.0
**Last Updated:** 2025-12-02
**Related:** [Example: Confidentia - Epic 4 - User Workflows & Use Case Modeling, Release Workflow] | [Example: vibe-dev-kit - Epic 2 - Workflow Management Framework, Release Workflow]

---

## 📖 Overview

This document provides a **step-by-step agent execution guide** for the Release Workflow. The Release Workflow serves as the **canonical example** of intelligent agent-driven workflow execution.

**This guide shows exactly how an AI agent should analyze, determine, execute, validate, and proceed through each of the 13 Release Workflow steps (Steps 1-11 are required, Steps 12-13 are optional but recommended for PDCA CHECK and ACT phases).**

> **Note on Examples:** This document includes examples from multiple projects:
> - **[Example: Confidentia/fynd.deals]** - Examples from the original source project
> - **[Example: vibe-dev-kit]** - Examples from the dev-kit project
> 
> When adopting this workflow in your own project, replace all examples with your project-specific paths, versions, and structures.

---

## 🎯 Execution Context

### Workflow Definition

**Workflow:** Release Workflow
**Type:** `release`
**Steps:** 13 steps organized into 3 phases (Steps 1-11: required, Steps 12-13: optional CHECK and ACT phases)
**Canonical Example:** Yes - this workflow demonstrates the agent-driven execution pattern

### Agent Execution Pattern

For each step, the agent follows this pattern:
1. **ANALYZE** - Understand step requirements and context
2. **DETERMINE** - Decide what actions to take
3. **EXECUTE** - Perform the actions
4. **VALIDATE** - Verify execution succeeded
5. **PROCEED** - Document and move to next step

### 🚨 MANDATORY: Progress Tracking with Cursor TODOs

**REQUIRED:** Agents **MUST** use `todo_write` to create and maintain a TODO list tracking all 11 Release Workflow steps. This is **NOT OPTIONAL** - it is a mandatory requirement for Release Workflow execution.

**Why TODOs are Required:**
- ✅ **User Visibility:** User can see real-time progress through all 11 steps
- ✅ **Agent Organization:** Helps agent stay organized across 11 sequential steps
- ✅ **Error Recovery:** Clear visibility into where execution stopped if interrupted
- ✅ **User Transparency:** User can verify all steps completed successfully
- ✅ **Status Management:** Automatic status updates provide clear execution state
- ✅ **Accountability:** Provides audit trail of workflow execution

**Required Implementation Pattern:**

1. **At Workflow Start (MANDATORY):** Create TODO list with all 13 steps as `pending`
   ```python
   todo_write(merge=False, todos=[
       {'id': 'rw-step-1', 'status': 'pending', 'content': 'Step 1: Branch Safety Check - Analyze work and ensure it aligns with current branch'},
       {'id': 'rw-step-2', 'status': 'pending', 'content': 'Step 2: Bump Version - Analyze current version and determine next version'},
       {'id': 'rw-step-3', 'status': 'pending', 'content': 'Step 3: Create Detailed Changelog - Generate CHANGELOG with full timestamp'},
       {'id': 'rw-step-4', 'status': 'pending', 'content': 'Step 4: Update Main Changelog - Add summary entry'},
       {'id': 'rw-step-5', 'status': 'pending', 'content': 'Step 5: Update README - Update version badge and latest release'},
       {'id': 'rw-step-6', 'status': 'pending', 'content': 'Step 6: Auto-update Kanban Docs - Update Epic/Story docs with version markers'},
       {'id': 'rw-step-7', 'status': 'pending', 'content': 'Step 7: Stage Files - Stage all modified files'},
       {'id': 'rw-step-8', 'status': 'pending', 'content': 'Step 8: Run Validators - Execute branch context and changelog format validators'},
       {'id': 'rw-step-9', 'status': 'pending', 'content': 'Step 9: Commit Changes - Create git commit with versioned message'},
       {'id': 'rw-step-10', 'status': 'pending', 'content': 'Step 10: Create Git Tag - Create annotated tag'},
       {'id': 'rw-step-11', 'status': 'pending', 'content': 'Step 11: Push to Remote - Push branch and tags'},
       {'id': 'rw-step-12', 'status': 'pending', 'content': 'Step 12: Post-Commit Verification & Reflection - Verify changes and reflect on results (optional but recommended)'},
       {'id': 'rw-step-13', 'status': 'pending', 'content': 'Step 13: Act on Verification Results - Update changelog, create follow-ups, document improvements (optional but recommended)'},
   ])
   ```

2. **Before Each Step (MANDATORY):** Mark step as `in_progress`
   ```python
   todo_write(merge=True, todos=[{'id': 'rw-step-1', 'status': 'in_progress'}])
   ```

3. **After Each Step (MANDATORY):** Mark step as `completed` and mark next step as `in_progress`
   ```python
   todo_write(merge=True, todos=[
       {'id': 'rw-step-1', 'status': 'completed'},
       {'id': 'rw-step-2', 'status': 'in_progress'}
   ])
   ```

4. **On Completion (MANDATORY):** All steps marked as `completed`
   ```python
   todo_write(merge=True, todos=[{'id': 'rw-step-11', 'status': 'completed'}])
   ```

**Enforcement:**
- ❌ **DO NOT** execute Release Workflow without creating TODO list first
- ❌ **DO NOT** skip TODO updates between steps
- ✅ **MUST** create TODO list before Step 1 execution
- ✅ **MUST** update TODO status before and after each step
- ✅ **MUST** mark all steps as completed on successful completion

**Note:** The markdown checklist below (lines 480-512) serves as a reference, but Cursor TODOs are the **REQUIRED** mechanism for real-time progress tracking and user visibility.

---

## 🔒 Critical Requirement: Fix Verification

**CRITICAL:** Before marking any bug fix as "Fixed" in changelogs, the fix MUST be verified through testing.

### Verification Requirements

**For Bug Fixes:**
- **Verified Fixes:** Must have evidence of successful testing:
  - Test suite execution (automated tests pass)
  - Manual testing (documented test results)
- **Unverified Fixes:** Must be logged as "Attempted Fix (Pending Verification)" until verification is complete
- **DO NOT** claim a fix is "Fixed" until verification evidence exists

### Verification Methods

1. **Test Suite Execution:**
   - Automated test suite must pass
   - Test results must be documented
   - Evidence: Test output, CI/CD results, test logs

2. **Manual Testing:**
   - Manual test steps must be documented
   - Test results must be recorded
   - Evidence: Test documentation, screenshots, test logs

### Changelog Format for Fixes

**Verified Fixes:**
```markdown
### Fixed
- Fixed issue description
  - **Verification Status:** Verified
  - **Verification Method:** Test Suite / Manual Testing
  - **Verification Evidence:** [Link to test results or documentation]
```

**Unverified Fixes:**
```markdown
### Attempted Fixes (Pending Verification)
- Attempted fix for issue description
  - **Verification Status:** Attempted Fix (Pending Verification)
  - **Verification Method:** [To be determined]
  - **Next Steps:** Run test suite / Perform manual testing
```

### Enforcement

- **Step 3 (Create Detailed Changelog):** Must check verification status before creating changelog
- **Step 4 (Update Main Changelog):** Must check verification status before updating main changelog
- **Validation:** If any fix is marked as "Fixed" without verification evidence, workflow MUST STOP

---

## 📋 Step-by-Step Agent Execution

### Step 1: Branch Safety Check

**Step Definition:**
```yaml
- id: step-1
  name: Branch Safety Check
  handler: release.branch_safety_check
  dependencies: []
  config:
    check_modified_files: true
    check_version_alignment: true
    check_changelog_alignment: true
```

**Agent Execution:**

1. **ANALYZE:**
   - Get current Git branch name (e.g., `epic/4` [Example: Confidentia], `epic/2` [Example: vibe-dev-kit], `main`)
   - Check if branch matches expected pattern (e.g., `epic/{n}` for epic branches)
   - Analyze modified files in working directory (`git status`, `git diff`)
   - Check if version file exists and read current version (if file is modified)
   - Check if changelog entries exist (if CHANGELOG.md is modified)
   - Extract expected epic number from branch name (e.g., `epic/4` → Epic 4 [Example: Confidentia], `epic/2` → Epic 2 [Example: vibe-dev-kit])
   - Check modified file paths for epic-specific patterns (e.g., `Epic-4/` [Example: Confidentia], `Epic-2/` [Example: vibe-dev-kit], `epic/4/` [Example: Confidentia])

2. **DETERMINE:**
   - Determine if work aligns with current branch:
     - If on `epic/4` [Example: Confidentia] or `epic/2` [Example: vibe-dev-kit], modified files should relate to that Epic
     - If version file modified, version epic should match branch epic
     - If changelog modified, changelog entries should match branch epic
     - Modified file paths should align with branch context
   - Identify any mismatches or cross-epic contamination
   - Determine if RW should proceed or stop

3. **EXECUTE:**
   - Run branch context analysis:
     - Check `git status` for modified files
     - Check `git diff` for changes to version file
     - Check `git diff` for changes to CHANGELOG.md
     - Analyze file paths for epic alignment
   - Compare branch epic with work epic (from files/version/changelog)

4. **VALIDATE:**
   - Verify branch and work alignment:
     - ✅ **PASS**: Work aligns with branch (e.g., on `epic/4` [Example: Confidentia] or `epic/2` [Example: vibe-dev-kit], all work is related to that Epic)
     - ❌ **FAIL**: Work does not align with branch (e.g., on `epic/4` [Example: Confidentia], but work references Epic 5 [Example: Confidentia])
   - If mismatch detected, workflow must stop immediately

5. **PROCEED:**
   - **If aligned**: Document "Branch safety check passed - work aligns with current branch", move to Step 2
   - **If misaligned**: 
     - Document: "🚨 RW BLOCKED: Branch Safety Check Failed"
     - Output clear warning message:
       ```
       🚨 RELEASE WORKFLOW BLOCKED
       
       Step 1: Branch Safety Check - FAILED
       
       Reason: Current branch '{branch}' does not align with the work being released.
       
       Details:
       - Current branch: {branch}
       - Expected epic: {expected_epic}
       - Detected issues: {list_of_issues}
       
       Action Required:
       1. Switch to the correct branch: git checkout epic/{correct_epic}
       2. Or review your changes to ensure they align with the current branch
       3. Then run RW again
       
       RW is NOT complete. Workflow stopped at Step 1.
       ```
     - Mark Step 1 TODO as `cancelled`
     - Mark all remaining steps as `cancelled`
     - **DO NOT PROCEED** to Step 2

**Example Alignment Checks:**

- **On `epic/4` branch [Example: Confidentia]:**
  - ✅ Version file shows `0.4.x.x+x` → PASS
  - ✅ Modified files in `Epic-4/` directory → PASS
  - ✅ Changelog entry references Epic 4 [Example: Confidentia] → PASS
  - ❌ Version file shows `0.5.x.x+x` → FAIL (mismatch)
  - ❌ Modified files in `Epic-5/` directory → FAIL (mismatch)

- **On `epic/2` branch [Example: vibe-dev-kit]:**
  - ✅ Version file shows `0.2.x.x+x` → PASS
  - ✅ Modified files in `Epic-2/` directory → PASS
  - ✅ Changelog entry references Epic 2 → PASS
  - ❌ Version file shows `0.3.x.x+x` → FAIL (mismatch)
  - ❌ Modified files in `Epic-3/` directory → FAIL (mismatch)

- **On `main` branch:**
  - ✅ Any epic number allowed (main can have any epic)
  - ⚠️ Warning: Consider if RW should run on main (usually run on epic branch first)

**CRITICAL: Task/Version Alignment Check**

**MANDATORY:** Before proceeding, verify that `VERSION_TASK` in the version file matches the active Task number from the Story document.

**Process:**
1. **Identify Active Task:**
   - Read the Story document to identify which Task is being completed
   - Extract Task number (e.g., `E4:S03:T002` → Task 2)
   - Note: This is the Task that was just completed and is being released

2. **Check Version File:**
   - Read `VERSION_TASK` from version file
   - Compare with active Task number from Story document

3. **Validation:**
   - ✅ If `VERSION_TASK` matches active Task number → PASS
   - ❌ If `VERSION_TASK` does NOT match active Task number → FAIL

**If Validation Fails:**
```
❌ TASK/VERSION MISMATCH DETECTED

Current VERSION_TASK: {current_task}
Active Task from Story: {active_task}

Action Required:
1. Update version.py: Set VERSION_TASK = {active_task}
2. If this is a new Task, also reset VERSION_BUILD = 1
3. Then run RW again

RW is NOT complete. Workflow stopped at Step 1.
```
- Mark Step 1 TODO as `cancelled`
- Mark all remaining steps as `cancelled`
- **DO NOT PROCEED** to Step 2

**Example Task Alignment Checks:**

- **Completing Task 2 in Story 3:**
  - ✅ `VERSION_TASK = 2` → PASS
  - ❌ `VERSION_TASK = 1` → FAIL (should be 2)
  - ❌ `VERSION_TASK = 3` → FAIL (should be 2)

- **Completing Task 1 in Story 1:**
  - ✅ `VERSION_TASK = 1` → PASS
  - ❌ `VERSION_TASK = 2` → FAIL (should be 1)

WARNING: This step prevents accidental cross-epic contamination and ensures version numbers match branch context. If this check fails, DO NOT proceed with the workflow. Fix the branch alignment first.

---

### Step 2: Bump Version

**Step Definition:**
```yaml
- id: step-2
  name: Bump Version
  handler: release.version_bump
  dependencies: [step-1]
  config:
    version_file: src/confidentia/version.py  # [Example: Confidentia] Use {version_file_path} template placeholder
    # [Example: vibe-dev-kit] version_file: src/fynd_deals/version.py
    increment_type: patch
```

**Agent Execution:**

1. **ANALYZE:**
   - Read current version from version file:
     - [Example: Confidentia] `src/confidentia/version.py`
     - [Example: vibe-dev-kit] `src/fynd_deals/version.py`
   - Understand version schema: `RC.EPIC.STORY.TASK+BUILD`
   - Check current Git branch to determine Epic number (already validated in Step 1)
   - **CRITICAL:** Identify the active Task being completed:
     - Read Story document to find the Task that was just completed
     - Extract Task number (e.g., `E4:S03:T002` → Task 2)
   - Understand increment type: `patch` means increment BUILD number (for same Task)
   - Verify version matches branch schema (already checked in Step 1, but double-check)
   - **CRITICAL:** Check if this is a Task transition:
     - Compare `VERSION_TASK` in version file with active Task number from Story
     - If different → This is a Task transition (new Task)
     - If same → This is a BUILD increment (same Task)

2. **DETERMINE:**
   - **If Task Transition (New Task):**
     - **CRITICAL:** Update `VERSION_TASK` to match active Task number
     - **CRITICAL:** Reset `VERSION_BUILD` to 1 (new Task always starts at BUILD 1)
     - Calculate next version:
       - [Example: vibe-dev-kit] If completing Task 2, and `VERSION_TASK = 1`:
         - Update: `VERSION_TASK = 2`, `VERSION_BUILD = 1`
         - Next version: `0.4.3.2+1` (Task 2, Build 1)
   - **If Same Task (BUILD Increment):**
     - Keep `VERSION_TASK` unchanged
     - Increment `VERSION_BUILD` by 1
     - Calculate next version:
       - [Example: Confidentia] If current is `0.4.3.2+8`, next is `0.4.3.2+9`
       - [Example: vibe-dev-kit] If current is `0.2.1.1+2`, next is `0.2.1.1+3`
   - Validate version matches branch:
     - [Example: Confidentia] Epic 4 = `0.4.x.x+x`
     - [Example: vibe-dev-kit] Epic 2 = `0.2.x.x+x`

3. **EXECUTE:**
   - **If Task Transition:**
     - Update `VERSION_TASK` to match active Task number
     - Update `VERSION_BUILD` to 1
     - Update version file:
       - [Example: vibe-dev-kit] `src/fynd_deals/version.py`
       - Use `search_replace` tool to update both `VERSION_TASK` and `VERSION_BUILD`
   - **If Same Task:**
     - Update `VERSION_BUILD` only (increment by 1)
     - Update version file:
       - [Example: Confidentia] `src/confidentia/version.py`
       - [Example: vibe-dev-kit] `src/fynd_deals/version.py`
       - Use `search_replace` tool to update `VERSION_BUILD`
   - Update version string comment if needed

4. **VALIDATE:**
   - Read version file to confirm update
   - Verify version format is valid
   - Check version matches branch schema
   - **CRITICAL:** Verify `VERSION_TASK` matches active Task number from Story
   - **CRITICAL:** If Task transition, verify `VERSION_BUILD = 1`
   - **CRITICAL:** If same Task, verify `VERSION_BUILD` incremented correctly

5. **PROCEED:**
   - Document version bump:
     - **If Task Transition:**
       - [Example: vibe-dev-kit] "Version bumped: Task transition detected. Updated VERSION_TASK: 1 → 2, VERSION_BUILD reset to 1. New version: 0.4.3.2+1"
     - **If Same Task:**
       - [Example: Confidentia] "Version bumped: 0.4.3.2+8 → 0.4.3.2+9"
       - [Example: vibe-dev-kit] "Version bumped: 0.2.1.1+2 → 0.2.1.1+3"
   - Pass `new_version` to Step 3
   - Move to Step 3

---

### Step 3: Create Detailed Changelog

**Step Definition:**
```yaml
- id: step-3
  name: Create Detailed Changelog
  handler: release.changelog_create
  dependencies: [step-2]
  config:
    changelog_dir: KB/Changelog_and_Release_Notes/Changelog_Archive
    format: full_timestamp
```

**Agent Execution:**

1. **ANALYZE:**
   - Get `new_version` from Step 2 output:
     - [Example: Confidentia] `"0.4.3.2+9"`
     - [Example: vibe-dev-kit] `"0.2.1.1+3"`
   - Get release summary from workflow parameters
   - Get change type from workflow parameters
   - Extract Epic/Story from Git branch name:
     - [Example: Confidentia] `epic/4` → Epic 4
     - [Example: vibe-dev-kit] `epic/2` → Epic 2
   - Understand timestamp format: `YYYY-MM-DD HH:MM:SS UTC`
   - Check changelog directory exists

2. **DETERMINE:**
   - Generate full timestamp: `date -u +"%Y-%m-%d %H:%M:%S UTC"`
   - Determine Epic number from branch:
     - [Example: Confidentia] `epic/4` → Epic 4
     - [Example: vibe-dev-kit] `epic/2` → Epic 2
   - Determine Story number from version:
     - [Example: Confidentia] `0.4.3.2+9` → Story 3
     - [Example: vibe-dev-kit] `0.2.1.1+3` → Story 1
   - Create changelog file path:
     - [Example: Confidentia] `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.4.3.2+9.md`
     - [Example: vibe-dev-kit] `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.2.1.1+3.md`
   - Review previous changelog format for consistency

3. **EXECUTE:**
   - Generate timestamp using system command
   - **PLAN Phase - Create PLAN Section:**
     - **Objectives:** Document what this release aims to achieve
       - List specific objectives for this release
       - Be clear and measurable
       - Example: "Add Step 12 to Release Workflow", "Fix changelog verification issue"
     - **Expected Outcomes:** Document what success looks like
       - Describe what should be achieved
       - Define success criteria
       - Example: "Step 12 added and documented", "Changelog verification working"
     - **Verification Plan:** Document how success will be verified
       - Define verification methods (test suite, manual testing, observation)
       - Specify what evidence will be collected
       - Link to Step 12 (CHECK phase) verification
       - Example: "Run test suite", "Manual testing of Step 12", "Review documentation"
   - **CRITICAL - Verification Check for Fixes:**
     - If this release includes bug fixes, check verification status:
       - **Verified fixes:** Must have evidence of testing (test suite pass or documented manual test results)
       - **Unverified fixes:** Must be logged as "Attempted Fix (Pending Verification)" until verified
     - **DO NOT** mark fixes as "Fixed" in changelog until verification is complete
   - Create changelog file with proper format:
     - Release Date (full timestamp)
     - Epic and Story information
     - Type (with emoji)
     - Summary
     - **PLAN Phase section (NEW):**
       - Objectives
       - Expected Outcomes
       - Verification Plan
     - Changes section:
       - **Fixed** section: Only verified fixes (with verification evidence)
       - **Attempted Fixes** section: Unverified fixes (pending verification)
       - Verification Status field for each fix entry
     - Related Tasks section

4. **VALIDATE:**
   - Verify file was created
   - Check timestamp format is correct (`YYYY-MM-DD HH:MM:SS UTC`)
   - Verify all required fields are present
   - **CRITICAL - Verification Validation:**
     - If changelog contains "Fixed" entries, verify each has:
       - Verification status: `Verified` or `Attempted Fix (Pending Verification)`
       - Verification method: `Test Suite` or `Manual Testing`
       - Verification evidence: Test results or manual test documentation
     - If any fix is marked as "Fixed" without verification evidence, **STOP** and require verification
   - Check file is readable

5. **PROCEED:**
   - Document changelog creation:
     - [Example: Confidentia] "Created detailed changelog: CHANGELOG_v0.4.3.2+9.md"
     - [Example: vibe-dev-kit] "Created detailed changelog: CHANGELOG_v0.2.1.1+3.md"
   - Pass `changelog_file` path to Step 4
   - Move to Step 4

---

### Step 4: Update Main Changelog

**Step Definition:**
```yaml
- id: step-4
  name: Update Main Changelog
  handler: release.changelog_update
  dependencies: [step-3]
  config:
    main_changelog: CHANGELOG.md
    date_format: DD-MM-YY
```

**Agent Execution:**

1. **ANALYZE:**
   - Get `new_version` from Step 2:
     - [Example: Confidentia] `"0.4.3.2+9"`
     - [Example: vibe-dev-kit] `"0.2.1.1+3"`
   - Get summary and change type from parameters
   - Read current `CHANGELOG.md` to find "## Recent Releases" section
   - Understand date format: `DD-MM-YY` (e.g., `01-12-25`)

2. **DETERMINE:**
   - Generate summary date: Current date in `DD-MM-YY` format
   - Determine entry format: `### [version] - date`
   - Find insertion point: After "## Recent Releases" header, before first existing entry
   - Create summary entry with link to detailed changelog

3. **EXECUTE:**
   - Insert new entry at top of Recent Releases section
   - Format examples:
     - [Example: Confidentia] `### [0.4.3.2+9] - 01-12-25`
     - [Example: vibe-dev-kit] `### [0.2.1.1+3] - 02-12-25`
   - Include summary with emoji
   - **CRITICAL - Verification Check for Fixes:**
     - If this release includes bug fixes, check verification status from detailed changelog:
       - **Verified fixes:** Include in "Fixed" subsection
       - **Unverified fixes:** Include in "Attempted Fixes" subsection (not in "Fixed")
     - **DO NOT** list unverified fixes under "Fixed" section
   - Add link to detailed changelog file

4. **VALIDATE:**
   - Verify entry was inserted correctly
   - Check date format is `DD-MM-YY`
   - Verify link to detailed changelog is correct
   - Ensure entry is at top of Recent Releases
   - **CRITICAL - Verification Validation:**
     - If entry includes "Fixed" subsection, verify all listed fixes have verification evidence in detailed changelog
     - If any fix in "Fixed" section lacks verification evidence, **STOP** and require verification
     - Verify "Attempted Fixes" section exists if there are unverified fixes

5. **PROCEED:**
   - Document: "Updated main changelog with summary entry"
   - Move to Step 5 (can run in parallel with Steps 5-6)

---

### Step 5: Update README

**Step Definition:**
```yaml
- id: step-5
  name: Update README
  handler: release.readme_update
  dependencies: [step-2]
  config:
    readme_file: README.md
    update_badge: true
    update_latest_release: true
```

**Agent Execution:**

1. **ANALYZE:**
   - Get `new_version` from Step 2:
     - [Example: Confidentia] `"0.4.3.2+9"`
     - [Example: vibe-dev-kit] `"0.2.1.1+3"`
   - Get summary and change type from parameters
   - Read `README.md` to find version badge and latest release callout
   - Understand badge format: `[![Version](...badge/version-{version}-blue)...]`
   - Understand latest release format: `**🎉 Latest Release: v{version}** - {summary}`

2. **DETERMINE:**
   - Update version badge: Replace version in badge URL
   - Update latest release: Replace version and summary
   - Find exact patterns in README to replace

3. **EXECUTE:**
   - Update version badge using `search_replace`
   - Update latest release callout using `search_replace`

4. **VALIDATE:**
   - Verify badge URL contains new version
   - Verify latest release callout has new version and summary
   - Check README is still valid Markdown

5. **PROCEED:**
   - Document: "Updated README version badge and latest release"
   - Move to Step 6 (can run in parallel with Steps 4-6)

---

### Step 6: Auto-update Kanban Docs

**Step Definition:**
```yaml
- id: step-6
  name: Auto-update Kanban Docs
  handler: confidentia.kanban_update  # [Example: Confidentia] Use {project}.kanban_update or kanban.update
  # [Example: vibe-dev-kit] handler: vibe-dev-kit.kanban_update (if implemented)
  dependencies: [step-2]
  config:
    epic_doc_pattern: KB/PM_and_Portfolio/epics/overview/Epic {epic}/Epic-{epic}.md  # [Example: Confidentia]
    # [Example: vibe-dev-kit] epic_doc_pattern: KB/PM_and_Portfolio/kanban/epics/Epic-{epic}.md
    kanban_board: KB/PM_and_Portfolio/epics/overview/_index.md  # [Example: Confidentia]
    # [Example: vibe-dev-kit] kanban_board: KB/PM_and_Portfolio/kanban/kanban-board.md
```

**Agent Execution:**

1. **ANALYZE:**
   - Get `new_version` from Step 2:
     - [Example: Confidentia] `"0.4.3.2+9"`
     - [Example: vibe-dev-kit] `"0.2.1.1+3"`
   - Extract Epic number from branch:
     - [Example: Confidentia] `epic/4` → Epic 4 (already validated in Step 1)
     - [Example: vibe-dev-kit] `epic/2` → Epic 2 (already validated in Step 1)
   - Extract Story number from version:
     - [Example: Confidentia] `0.4.3.2+9` → Story 3
     - [Example: vibe-dev-kit] `0.2.1.1+3` → Story 1
   - Find Epic doc:
     - [Example: Confidentia] `KB/PM_and_Portfolio/epics/overview/Epic 4/Epic-4.md`
     - [Example: vibe-dev-kit] `KB/PM_and_Portfolio/kanban/epics/Epic-2.md`
   - Find Story doc:
     - [Example: Confidentia] `KB/PM_and_Portfolio/kanban/Epic 4/Story-3-*.md`
     - [Example: vibe-dev-kit] `KB/PM_and_Portfolio/kanban/epics/Epic-2/stories/Story-001-*.md`
   - Understand "Last updated" field format

2. **DETERMINE:**
   - **CRITICAL: "ALL Sections" Requirement** - Must update ALL sections referencing the story/task:
     - Epic doc header "Last updated" field
     - Epic doc Story Checklist (status and version marker)
     - Epic doc detailed Story sections (Status, Last updated, Task checkboxes with forensic markers)
     - Story doc header "Last updated" and "Version" fields
     - Story doc Task Checklist (with forensic markers)
     - Story doc detailed Task sections (Status, version markers)
     - Any other references to the story/task
   - Format for "Last updated": `**Last updated:** YYYY-MM-DD (v{version} – {summary})`
   - Format for forensic markers: `✅ COMPLETE (v{version})` (canonical format)
   - Determine if tasks should be marked complete (if applicable)
   - **Systematic Process:**
     1. Read the FULL Epic document file
     2. Read the authoritative Story document file to get correct state
     3. Use grep/search to find ALL sections referencing the story/task
     4. Update ALL of them to match the Story file's state

3. **EXECUTE:**
   - Update Epic doc header "Last updated" field
   - Update Epic doc Story Checklist with version marker (format: `- [ ] **E4:S03 – Story Name** - IN PROGRESS (v{version})`)
   - Update Epic doc detailed Story sections (Status, Last updated, Task checkboxes with forensic markers)
   - Update Story doc header "Last updated" and "Version" fields
   - Update Story doc Task Checklist with forensic markers (format: `✅ COMPLETE (v{version})`)
   - Update Story doc detailed Task sections with forensic markers
   - Search for and update any other references to the story/task

4. **VALIDATE:**
   - Verify Epic doc header was updated
   - Verify Epic doc Story Checklist was updated with version marker
   - Verify Epic doc detailed Story sections were updated
   - Verify Story doc header was updated
   - Verify Story doc Task Checklist was updated with forensic markers
   - Verify Story doc detailed Task sections were updated
   - Check date format is correct
   - Verify version numbers are correct
   - Verify forensic marker format is canonical: `✅ COMPLETE (v{version})`
   - **Consistency Check:** Verify Epic header matches Story Checklist, Story Checklist matches detailed sections

5. **PROCEED:**
   - Document: "Updated Kanban docs with version markers"
   - Move to Step 7 (waits for Steps 2-6 to complete)

---

### Step 7: Stage Files

**Step Definition:**
```yaml
- id: step-7
  name: Stage Files
  handler: git.stage_all
  dependencies: [step-2, step-3, step-4, step-5, step-6]
  config:
    paths: ["*"]
```

**Agent Execution:**

1. **ANALYZE:**
   - Understand all files modified in Steps 2-6:
     - Version file
     - Detailed changelog (new file)
     - Main changelog
     - README
     - Kanban docs
   - Check current Git status
   - Understand `git add -A` stages all changes

2. **DETERMINE:**
   - Stage all modified files
   - Use `git add -A` to stage everything

3. **EXECUTE:**
   - Run `git add -A`
   - Verify files are staged

4. **VALIDATE:**
   - Check `git status --short` to verify files are staged
   - Ensure all expected files are in staging area

5. **PROCEED:**
   - Document: "Staged all modified files"
   - Move to Step 8

---

### Step 8: Run Validators

**Step Definition:**
```yaml
- id: step-8
  name: Run Validators
  handler: confidentia.run_validators  # [Example: Confidentia] Use {project}.run_validators or validation.run_validators
  # [Example: vibe-dev-kit] handler: vibe-dev-kit.run_validators (if implemented)
  dependencies: [step-7]
  config:
    validators:
      - scripts/validation/validate_branch_context.py  # Use {validation_scripts_path}/validate_branch_context.py
      - scripts/validation/validate_changelog_format.py  # Use {validation_scripts_path}/validate_changelog_format.py
    strict_mode: true
```

**Agent Execution:**

1. **ANALYZE:**
   - Understand validators to run:
     - `validate_branch_context.py` - Checks branch/version/epic alignment
     - `validate_changelog_format.py` - Checks changelog format
   - Understand strict mode: Failures block workflow
   - Check validators exist and are executable

2. **DETERMINE:**
   - Run each validator with `--strict` flag
   - Collect output from each validator
   - Determine if validators passed or failed

3. **EXECUTE:**
   - Run `python scripts/validation/validate_branch_context.py --strict`
   - Run `python scripts/validation/validate_changelog_format.py --strict`
   - Capture exit codes and output

4. **VALIDATE:**
   - Check exit codes: 0 = success, non-zero = failure
   - If any validator fails in strict mode, workflow must abort
   - Analyze error messages if validators fail

5. **PROCEED:**
   - If validators pass: Document "Validators passed", move to Step 9
   - If validators fail: Abort workflow, report errors, do not proceed

---

### Step 9: Commit Changes

**Step Definition:**
```yaml
- id: step-9
  name: Commit Changes
  handler: git.commit
  dependencies: [step-8]
  config:
    message_template: "{version} - {summary}"
```

**Agent Execution:**

1. **ANALYZE:**
   - Get `new_version` from Step 2:
     - [Example: Confidentia] `"0.4.3.2+9"`
     - [Example: vibe-dev-kit] `"0.2.2.4+1"`
   - Get summary from parameters
   - Read detailed changelog from Step 3 to understand:
     - What was actually done (DO phase)
     - Verification status (if fixes included)
     - PLAN phase objectives (if included)
   - Understand commit message template: `"{version} - {summary}"`
   - Verify files are still staged
   - **CRITICAL - Language Alignment:**
     - Check changelog for verification status
     - If changelog contains "Attempted Fixes", commit message MUST use unverified language
     - If changelog contains "Fixed" (verified), commit message can use verified language
     - Commit message language MUST match changelog verification status

2. **DETERMINE:**
   - Build commit message:
     - [Example: Confidentia] `"0.4.3.2+9 - 📚 Documentation: Tighten Epic 4 [Example: Confidentia] Kanban docs..."`
     - [Example: vibe-dev-kit] `"0.2.2.4+1 - 🧰 Tooling: Task 4 complete - Enhanced DO Phase..."`
   - **Language Pattern Selection:**
     - **If verified fixes:** Use verified language ("Fixed", "Resolved", "Corrected")
     - **If unverified fixes:** Use unverified language ("Attempted fix", "Addressed", "Modified")
     - **If documentation/feature:** Use appropriate language ("Added", "Updated", "Created")
   - Ensure message follows project conventions
   - Ensure message accurately reflects what was done (DO phase)
   - Ensure message aligns with changelog intent (PLAN phase)

3. **EXECUTE:**
   - Run `git commit -m "{message}"`
   - Capture commit hash if available
   - **Document Execution:**
     - Record what was actually done
     - Note any deviations from PLAN phase
     - Document execution details if needed

4. **VALIDATE:**
   - Verify commit was created (check exit code)
   - Verify commit message is correct
   - **CRITICAL - Language Validation:**
     - Verify commit message language matches changelog verification status
     - If changelog says "Attempted Fix", commit message MUST NOT say "Fixed"
     - If changelog says "Fixed" (verified), commit message can say "Fixed"
     - Verify commit message accurately reflects what was done
   - Check commit hash if available

5. **PROCEED:**
   - Document: "Created commit {hash} with message: {message}"
   - Document execution details (what was actually done)
   - Pass commit hash to Step 10 (if needed)
   - Move to Step 10

**Key Points:**
- This step implements the **DO phase** of PDCA cycle
- Commit message MUST match changelog verification status
- Commit message MUST accurately reflect what was done
- Commit message MUST align with changelog intent (PLAN phase)
- Language patterns must match verification status

**Language Pattern Guidelines:**

**Verified Fixes (use these words):**
- "Fixed", "Resolved", "Corrected", "Repaired"
- Only use if verification evidence exists in changelog

**Unverified Fixes (use these words):**
- "Attempted fix", "Addressed", "Modified", "Updated", "Changed"
- Use when changelog shows "Attempted Fix (Pending Verification)"

**Documentation/Features (use these words):**
- "Added", "Created", "Updated", "Enhanced", "Improved"
- Use for documentation, features, tooling changes

**DO NOT:**
- ❌ Say "Fixed" if changelog says "Attempted Fix"
- ❌ Use overly confident language for unverified changes
- ❌ Misrepresent what was actually done
- ❌ Deviate from changelog intent without documenting why

**Examples:**

**Example 1: Verified Fix (Good)**
- Changelog: "Fixed changelog verification issue" (with verification evidence)
- Commit: "Release v0.2.2.4+1: Fixed changelog verification issue"
- ✅ Language matches verification status

**Example 2: Unverified Fix (Good)**
- Changelog: "Attempted fix for changelog verification issue" (pending verification)
- Commit: "Release v0.2.2.4+1: Attempted fix for changelog verification issue"
- ✅ Language matches verification status

**Example 3: Unverified Fix (Bad)**
- Changelog: "Attempted fix for changelog verification issue" (pending verification)
- Commit: "Release v0.2.2.4+1: Fixed changelog verification issue"
- ❌ Language doesn't match - too confident for unverified fix

**Example 4: Documentation (Good)**
- Changelog: "Added execution documentation template"
- Commit: "Release v0.2.2.4+1: Added execution documentation template"
- ✅ Appropriate language for documentation

**See Also:**
- **Commit Message Language Guidelines:** `packages/frameworks/workflow mgt/KB/Documentation/Templates/commit-message-language-guidelines.md`
- **Execution Documentation Template:** `packages/frameworks/workflow mgt/KB/Documentation/Templates/execution-documentation-template.md`
- **Changelog Language Analysis:** `KB/Architecture/Standards_and_ADRs/rw-changelog-commit-language-analysis.md`

---

### Step 10: Create Git Tag

**Step Definition:**
```yaml
- id: step-10
  name: Create Git Tag
  handler: git.create_tag
  dependencies: [step-9]
  config:
    tag_template: v{version}
    message_template: "Release {tag}: {summary}"
    annotated: true
```

**Agent Execution:**

1. **ANALYZE:**
   - Get `new_version` from Step 2:
     - [Example: Confidentia] `"0.4.3.2+9"`
     - [Example: vibe-dev-kit] `"0.2.1.1+3"`
   - Get summary from parameters
   - Understand tag template: `v{version}`:
     - [Example: Confidentia] → `v0.4.3.2+9`
     - [Example: vibe-dev-kit] → `v0.2.1.1+3`
   - Understand message template: `"Release {tag}: {summary}"`
   - Understand annotated tag: Includes metadata

2. **DETERMINE:**
   - Build tag name:
     - [Example: Confidentia] `v0.4.3.2+9`
     - [Example: vibe-dev-kit] `v0.2.1.1+3`
   - Build tag message:
     - [Example: Confidentia] `"Release v0.4.3.2+9: 📚 Documentation: Tighten Epic 4 [Example: Confidentia] Kanban docs..."`
     - [Example: vibe-dev-kit] `"Release v0.2.1.1+3: Task 1 complete - Audit RW documentation..."`
   - Check if tag already exists (should not)

3. **EXECUTE:**
   - Run `git tag -a -m "{message}" v{version}`
   - Verify tag was created

4. **VALIDATE:**
   - Verify tag exists:
     - [Example: Confidentia] `git tag -l "v0.4.3.2+9"`
     - [Example: vibe-dev-kit] `git tag -l "v0.2.1.1+3"`
   - Check tag message is correct
   - Verify tag is annotated

5. **PROCEED:**
   - Document tag creation:
     - [Example: Confidentia] "Created annotated tag v0.4.3.2+9"
     - [Example: vibe-dev-kit] "Created annotated tag v0.2.1.1+3"
   - Move to Step 11 (waits for Step 9 to complete)

---

### Step 11: Push to Remote

**Step Definition:**
```yaml
- id: step-11
  name: Push to Remote
  handler: git.push
  dependencies: [step-9, step-10]
  config:
    push_tags: true
    remote: origin
```

**Agent Execution:**

1. **ANALYZE:**
   - Get current branch name:
     - [Example: Confidentia] `epic/4` (already validated in Step 1)
     - [Example: vibe-dev-kit] `epic/2` or `main` (already validated in Step 1)
   - Get tag name from Step 10:
     - [Example: Confidentia] `v0.4.3.2+9`
     - [Example: vibe-dev-kit] `v0.2.1.1+3`
   - Understand remote: `origin`
   - Check network access and Git credentials

2. **DETERMINE:**
   - Push branch:
     - [Example: Confidentia] `git push origin epic/4`
     - [Example: vibe-dev-kit] `git push origin main` (or `epic/2`)
   - Push tag:
     - [Example: Confidentia] `git push origin v0.4.3.2+9`
     - [Example: vibe-dev-kit] `git push origin v0.2.1.1+3`
   - Determine if network access is available

3. **EXECUTE:**
   - Push branch to remote
   - Push tag to remote
   - Capture output

4. **VALIDATE:**
   - Verify branch push succeeded
   - Verify tag push succeeded
   - Check for any errors or warnings

5. **PROCEED:**
   - Document: "Pushed branch and tag to origin"
   - Move to Step 12 (if enabled)

---

### Step 12: Post-Commit Verification & Reflection

**Step Definition:**
```yaml
- id: step-12
  name: Post-Commit Verification & Reflection
  handler: release.verification_reflection
  dependencies: [step-11]
  config:
    verification_prompt: true
    reflection_questions: true
    changelog_update: true
```

**Agent Execution:**

1. **ANALYZE:**
   - Get `new_version` from Step 2:
     - [Example: Confidentia] `"0.4.3.2+9"`
     - [Example: vibe-dev-kit] `"0.2.2.1+1"`
   - Read detailed changelog from Step 3:
     - [Example: Confidentia] `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.4.3.2+9.md`
     - [Example: vibe-dev-kit] `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.2.2.1+1.md`
   - Understand this is the **CHECK phase** of PDCA cycle
   - Check if release includes bug fixes or changes requiring verification
   - Review changelog for "Attempted Fixes" entries

2. **DETERMINE:**
   - **If release includes fixes or changes:**
     - Prompt for verification status: "Has this change been verified?"
     - Options: Verified / Unverified / Deferred
     - If verified: Collect verification evidence
     - If unverified: Document as "Attempted Fix (Pending Verification)"
     - If deferred: Document verification plan
   - **If release is documentation/feature (no fixes):**
     - Prompt for reflection: "Does this change work as expected?"
     - Document reflection results
   - Determine verification method:
     - Test suite execution (automated)
     - Manual testing (documented)
     - Observation period (for behavior changes)
     - Defer verification (explicit decision)

3. **EXECUTE:**
   - **Verification Prompt:**
     ```
     🔍 POST-COMMIT VERIFICATION (CHECK Phase)
     
     Release: v{version}
     Changes: {summary}
     
     Has this change been verified?
     - [ ] Verified (with evidence)
     - [ ] Unverified (pending verification)
     - [ ] Deferred (verification planned)
     
     If verified, provide:
     - Verification method: [Test Suite / Manual Testing / Observation]
     - Verification evidence: [Link or description]
     - Verification date: [YYYY-MM-DD HH:MM:SS UTC]
     ```
   
   - **Reflection Questions:**
     ```
     📝 REFLECTION QUESTIONS
     
     1. Did the change work as expected?
        - [ ] Yes
        - [ ] Partially
        - [ ] No
        - [ ] Unknown (needs verification)
     
     2. Did it solve the problem?
        - [ ] Yes
        - [ ] Partially
        - [ ] No
        - [ ] Unknown (needs verification)
     
     3. Are there any side effects?
        - [ ] None observed
        - [ ] Minor side effects (document)
        - [ ] Significant side effects (document)
        - [ ] Unknown (needs observation)
     
     4. What did we learn?
        - [Document lessons learned]
     ```
   
   - **Document Verification Results:**
     - If verified: Update changelog with verification status
     - If unverified: Ensure changelog shows "Attempted Fix (Pending Verification)"
     - If deferred: Document verification plan
     - Create verification documentation file if needed

4. **VALIDATE:**
   - Verify verification status is documented
   - Verify reflection questions are answered (if applicable)
   - Verify changelog accurately reflects verification status
   - **CRITICAL:** If fix is marked as "Fixed" without verification evidence, **STOP** and require verification
   - Verify verification evidence exists (if verified)

5. **PROCEED:**
   - Document verification and reflection results
   - Pass verification status to Step 13 (if enabled)
   - If verification deferred: Create reminder task or schedule verification
   - Move to Step 13 (if enabled) or mark workflow complete

**Key Points:**
- This step implements the **CHECK phase** of PDCA cycle
- Enables explicit verification after commit
- Prevents "Attempted Fixes" from remaining unverified indefinitely
- Creates learning loop through reflection questions
- Integrates with existing fix verification requirements

**Integration with Fix Verification:**
- If changelog contains "Attempted Fixes", this step prompts for verification
- If verification succeeds, changelog can be updated to "Fixed" (in Step 13)
- If verification fails, document what didn't work (in Step 13)
- If verification deferred, document plan and schedule

**Examples:**

**Example 1: Verified Fix**
- Release: `v0.2.2.1+1` (bugfix)
- Changelog contains: "Attempted fix for changelog verification requirement"
- Step 12 prompts: "Has this change been verified?"
- Response: Verified
- Verification method: Test suite execution
- Verification evidence: All tests pass (15/15)
- Result: Verification documented, ready for Step 13 to update changelog

**Example 2: Unverified Fix**
- Release: `v0.2.2.1+1` (bugfix)
- Changelog contains: "Attempted fix for changelog verification requirement"
- Step 12 prompts: "Has this change been verified?"
- Response: Unverified
- Verification plan: Run test suite after deployment
- Result: Remains in "Attempted Fixes" section, verification plan documented

**Example 3: Deferred Verification**
- Release: `v0.2.2.1+1` (bugfix)
- Changelog contains: "Attempted fix for changelog verification requirement"
- Step 12 prompts: "Has this change been verified?"
- Response: Deferred
- Reason: Requires production deployment
- Verification plan: Verify after next deployment (scheduled 2025-12-05)
- Result: Verification deferred, plan documented, reminder created

**Example 4: Documentation Release (No Fixes)**
- Release: `v0.2.2.1+1` (documentation)
- Changelog contains: "Added Step 12 execution guide"
- Step 12 prompts: "Does this change work as expected?"
- Reflection: Documentation complete, examples added, templates created
- Result: Reflection documented, no verification needed

---

### Step 13: Act on Verification Results

**Step Definition:**
```yaml
- id: step-13
  name: Act on Verification Results
  handler: release.act_on_results
  dependencies: [step-12]
  config:
    changelog_update: true
    follow_up_tasks: true
    process_improvement: true
```

**Agent Execution:**

1. **ANALYZE:**
   - Get verification status from Step 12:
     - Verified / Unverified / Deferred
     - Verification evidence (if verified)
     - Reflection results (if available)
   - Get `new_version` from Step 2:
     - [Example: Confidentia] `"0.4.3.2+9"`
     - [Example: vibe-dev-kit] `"0.2.2.2+1"`
   - Read detailed changelog from Step 3:
     - [Example: Confidentia] `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.4.3.2+9.md`
     - [Example: vibe-dev-kit] `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.2.2.2+1.md`
   - Understand this is the **ACT phase** of PDCA cycle
   - Check if Step 12 was executed (optional step)
   - Review changelog for "Attempted Fixes" entries

2. **DETERMINE:**
   - **If verification status is Verified:**
     - Determine action: Update changelog to move from "Attempted Fixes" to "Fixed"
     - Standardize successful practices
     - Document verification evidence
     - Create new release if needed (or update existing changelog)
   - **If verification status is Failed:**
     - Determine action: Document what didn't work
     - Identify root causes
     - Create follow-up task
     - Plan next iteration
   - **If verification status is Deferred:**
     - Determine action: Document verification plan
     - Schedule verification
     - Create reminder task
   - **If no verification needed (documentation/feature):**
     - Determine action: Document process improvements
     - Capture lessons learned
     - Update RW documentation if needed

3. **EXECUTE:**
   - **If Verified Fix:**
     - Update detailed changelog: Move entry from "Attempted Fixes" to "Fixed" section
     - Add verification evidence to changelog entry
     - Update main changelog: Move entry from "Attempted Fixes" to "Fixed" subsection
     - Document successful practices
     - **Option A:** Create new release with updated changelog (recommended)
     - **Option B:** Update existing changelog file (requires manual edit)
   
   - **If Failed Fix:**
     - Document what didn't work in changelog
     - Add "Failed Fixes" section if needed
     - Identify root causes
     - Create follow-up task in Kanban
     - Plan next iteration
   
   - **If Deferred Verification:**
     - Document verification plan in changelog
     - Add "Deferred Verification" section if needed
     - Schedule verification (create reminder task)
     - Document next steps
   
   - **Process Improvement:**
     - Reflect on RW process itself
     - Identify improvements
     - Document lessons learned
     - Update RW documentation if needed
     - Create process improvement task if needed

4. **VALIDATE:**
   - Verify changelog updates are accurate
   - Verify verification evidence is documented (if verified)
   - Verify follow-up tasks are created (if needed)
   - Verify process improvements are documented (if any)
   - **CRITICAL:** If creating new release, verify version is incremented correctly

5. **PROCEED:**
   - Document actions taken
   - If new release created: Pass to next RW cycle
   - If changelog updated: Document update
   - If follow-up tasks created: Document tasks
   - **Workflow Complete!** (or ready for next iteration)

**Key Points:**
- This step implements the **ACT phase** of PDCA cycle
- Enables acting on verification results from Step 12
- Updates changelogs based on verification status
- Creates follow-up tasks when needed
- Captures process improvements
- Completes the Document-Commit-Reflect pattern

**Integration with Step 12:**
- Step 13 depends on Step 12 (CHECK phase)
- Uses verification status from Step 12
- Acts on reflection results from Step 12
- Completes the PDCA cycle

**Changelog Update Options:**

**Option A: Create New Release (Recommended)**
- Increment BUILD number
- Create new changelog entry
- Move "Attempted Fix" to "Fixed" section
- Include verification evidence
- Full traceability maintained

**Option B: Update Existing Release**
- Update existing changelog file
- Move "Attempted Fix" to "Fixed" section
- Add verification evidence
- Note: Requires manual file edit (not automated)

**Examples:**

**Example 1: Verified Fix - Create New Release**
- Step 12 result: Verified (test suite pass)
- Step 13 action: Create new release `v0.2.2.2+1`
- Changelog update: Move "Attempted fix" to "Fixed" section
- Verification evidence: Added to changelog
- Result: Full traceability, verification documented

**Example 2: Failed Fix - Document and Create Follow-Up**
- Step 12 result: Failed (tests fail)
- Step 13 action: Document failure, create follow-up task
- Changelog update: Add "Failed Fixes" section
- Follow-up task: E2:S02:T007 – Fix Step 12 verification issue
- Result: Failure documented, next iteration planned

**Example 3: Deferred Verification - Document Plan**
- Step 12 result: Deferred (requires production deployment)
- Step 13 action: Document verification plan, schedule reminder
- Changelog update: Add "Deferred Verification" section
- Reminder task: Verify after deployment (2025-12-05)
- Result: Plan documented, verification scheduled

**Example 4: Process Improvement**
- Step 12 reflection: RW process could be improved
- Step 13 action: Document process improvement
- Documentation update: Update RW execution guide
- Process improvement: Add validation for Step 12
- Result: Process improved, documentation updated

---

## ✅ Agent Execution Checklist

**Note:** This markdown checklist serves as a reference. **Agents MUST use Cursor TODOs** (see "🚨 MANDATORY: Progress Tracking with Cursor TODOs" section above) for real-time progress tracking. TODOs are **REQUIRED**, not optional.

When executing Release Workflow as an agent, ensure:

### Pre-Execution
- [ ] **MANDATORY:** Created TODO list with all 13 steps (using `todo_write`) - Note: Steps 12-13 are optional but recommended
- [ ] Loaded workflow definition from YAML
- [ ] Parsed all 13 steps and dependencies
- [ ] Gathered workflow parameters (summary, change_type, etc.)
- [ ] Checked current Git branch
- [ ] Verified workspace context

### Step Execution
- [ ] **Step 1:** Analyzed work and branch alignment, validated branch safety
- [ ] **Step 2:** Analyzed version, determined next version, updated file, validated
- [ ] **Step 3:** Analyzed requirements, generated timestamp, created changelog, validated
- [ ] **Step 4:** Analyzed format, determined date, updated CHANGELOG.md, validated
- [ ] **Step 5:** Analyzed README, updated badge and callout, validated
- [ ] **Step 6:** Analyzed Kanban docs, updated Epic/Story docs, validated
- [ ] **Step 7:** Analyzed modified files, staged all files, validated
- [ ] **Step 8:** Analyzed validators, ran both validators, validated results
- [ ] **Step 9:** Analyzed template, built message, created commit, validated
- [ ] **Step 10:** Analyzed tag format, created annotated tag, validated
- [ ] **Step 11:** Analyzed remote, pushed branch and tag, validated
- [ ] **Step 12:** Analyzed changes, prompted for verification, documented reflection, validated (optional but recommended)
- [ ] **Step 13:** Analyzed verification results, acted on results, updated changelog, created follow-ups, validated (optional but recommended)

### Post-Execution
- [ ] **MANDATORY:** All steps marked as completed in TODO list
- [ ] All steps completed successfully
- [ ] Version file updated correctly
- [ ] Changelogs created/updated correctly
- [ ] README updated correctly
- [ ] Kanban docs updated correctly
- [ ] Files committed with correct message
- [ ] Tag created and pushed
- [ ] Branch pushed to remote
- [ ] Verification and reflection documented (if Step 12 executed)
- [ ] Actions taken and follow-ups created (if Step 13 executed)
- [ ] Execution documented

---

## 🚫 Common Agent Mistakes

### ❌ Don't: Blindly Run Scripts

**Bad:**
```python
# Agent just runs the script
run_terminal_cmd("python scripts/automation/release_workflow.py --auto-go")
```

**Good:**
```python
# Agent analyzes and executes each step intelligently
# Step 1: Analyze work and branch alignment, validate branch safety
# Step 2: Analyze version, determine next version, update file
# Step 3: Analyze changelog requirements, create file
# etc.
```

### ❌ Don't: Skip Analysis

**Bad:**
- Agent updates version without checking branch context
- Agent creates changelog without understanding format requirements
- Agent commits without validating

**Good:**
- Agent checks branch safety before any modifications (Step 1)
- Agent analyzes branch context before version bump
- Agent understands changelog format requirements
- Agent validates before committing

### ❌ Don't: Ignore Dependencies

**Bad:**
- Agent tries to create changelog before version is bumped
- Agent tries to commit before files are staged
- Agent tries to push before commit exists

**Good:**
- Agent completes Step 1 (branch safety) before any modifications
- Agent waits for Step 2 to complete before Step 3
- Agent waits for Step 7 to complete before Step 8
- Agent respects dependency order

---

## 📚 Related Documentation

**Workflow Documentation:**
- **[Agent-Driven Workflow Execution](agent-driven-workflow-execution.md)** - General agent execution methodology
- **[Release Workflow Reference](release-workflow-reference.md)** - Complete workflow reference
- **[Release Workflow Usage](release-workflow-usage.md)** - How to use the workflow

**Policy Documentation:**
- **[Kanban Governance Policy](../../PM_and_Portfolio/rituals/policy/kanban-governance-policy.md)** - Work item structure
- **[Versioning Strategy](../../Architecture/Standards_and_ADRs/versioning-strategy.md)** - Versioning requirements
- **[Versioning Policy](../../Architecture/Standards_and_ADRs/versioning-policy.md)** - Version schema

**Cursor Rules Integration:**

### RW Trigger Definition

The `.cursorrules` file defines a **case-insensitive "RW" trigger** that mandates intelligent agent-driven Release Workflow execution:

**Trigger:** User types "RW" or "rw" (case-insensitive)

**Required Behavior (from `.cursorrules`):**
1. **DO NOT** run `scripts/automation/release_workflow.py` (deterministic script)
2. **DO** execute Release Workflow using intelligent agent-driven execution
3. **Follow** this guide (`release-workflow-agent-execution.md`) step-by-step
4. **Start with Step 1: Branch Safety Check** - Analyze work and ensure it aligns with current branch before proceeding
5. **Use** ANALYZE → DETERMINE → EXECUTE → VALIDATE → PROCEED pattern for each step
6. **Document** analysis, actions, and results at each step

**Cursor Rules Enforcement:**
- ✅ **Explicit Pattern:** Rules mandate agent-driven execution for "RW" trigger
- ✅ **Documentation Links:** Rules reference this guide and agent execution methodology
- ✅ **Anti-Pattern Prevention:** Rules explicitly prohibit blind script execution
- ✅ **Integration:** Rules connect to versioning, changelog, and validation requirements

**How This Works:**
1. User types "RW" in chat
2. `.cursorrules` instructs AI assistant to use agent-driven execution
3. AI assistant loads this guide and executes each step intelligently
4. AI assistant follows `.cursorrules` guardrails (branch checks, validators, versioning)
5. AI assistant analyzes, determines, executes, validates, and documents at each step
6. Process is transparent, traceable, and intelligent

**See:** `.cursorrules` - "🚀 RELEASE WORKFLOW (RW) TRIGGER" section

---

**Last Updated:** 2025-01-02
**Document Version:** 1.1.0
