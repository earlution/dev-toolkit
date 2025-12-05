---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-04T12:02:13Z
expires_at: null
housekeeping_policy: keep
---

# Release Workflow: Agent Execution Guide

**Version:** 1.0.0
**Last Updated:** 2025-12-02
**Related:** [Example: Confidentia - Epic 4 - User Workflows & Use Case Modeling, Release Workflow] | [Example: vibe-dev-kit - Epic 2 - Workflow Management Framework, Release Workflow]

---

## 📖 Overview

This document provides a **step-by-step agent execution guide** for the Release Workflow. The Release Workflow serves as the **canonical example** of intelligent agent-driven workflow execution.

**This guide shows exactly how an AI agent should analyze, determine, execute, validate, and proceed through each of the 14 Release Workflow steps (Steps 1-12 are required, Steps 13-14 are optional but recommended for PDCA CHECK and ACT phases).**

> **Note on Examples:** This document includes examples from multiple projects:
> - **[Example: Confidentia/fynd.deals]** - Examples from the original source project
> - **[Example: vibe-dev-kit]** - Examples from the dev-kit project
> 
> When adopting this workflow in your own project, replace all examples with your project-specific paths, versions, and structures.

---

## 🔒 RW Hardening Principles (Summary)

This Release Workflow follows the shared *Workflow Hardening Guide for Agent‑Driven Release Processes* (`KB/Architecture/Standards_and_ADRs/workflow-hardening-guide.md`). In practice, this means:

- **Atomic RW per invocation:** One RW run attempts all steps for a single version or clearly stops in a `RW BLOCKED at Step X` state.
- **Minimal, predictable tools:** RW uses a small, stable set of tools (file read/write, git/validators, TODO tracking) and avoids experimental or irrelevant tools during execution.
- **Single sources of truth per step:** For each step, there is one authoritative artifact (version file, changelog entry, story file, etc.), and related files are normalized to it.
- **TODOs as a state machine:** RW step TODOs (`rw-step-1` … `rw-step-N`) move monotonically from `pending` → `in_progress` → `completed` (or `cancelled`), with at most one step `in_progress` at a time.
- **Honest blocked states:** When RW cannot proceed (missing user input, branch policy, no network for push), it reports a clear `RW BLOCKED` status with exact follow‑up actions, instead of silently stalling.

These principles are part of the RW contract for agents and humans in this project and should be preserved when this workflow is copied into other repos.

---

## 🎯 Execution Context

### Workflow Definition

**Workflow:** Release Workflow
**Type:** `release`
**Steps:** 14 steps organized into 3 phases (Steps 1-12: required, Steps 13-14: optional CHECK and ACT phases)
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
- ✅ **User Visibility:** User can see real-time progress through all 13 steps
- ✅ **Agent Organization:** Helps agent stay organized across 11 sequential steps
- ✅ **Error Recovery:** Clear visibility into where execution stopped if interrupted
- ✅ **User Transparency:** User can verify all steps completed successfully
- ✅ **Status Management:** Automatic status updates provide clear execution state
- ✅ **Accountability:** Provides audit trail of workflow execution

**Required Implementation Pattern:**

1. **At Workflow Start (MANDATORY):** Create TODO list with all 14 steps as `pending`
   ```python
   todo_write(merge=False, todos=[
       {'id': 'rw-step-1', 'status': 'pending', 'content': 'Step 1: Branch Safety Check - Analyze work and ensure it aligns with current branch'},
       {'id': 'rw-step-2', 'status': 'pending', 'content': 'Step 2: Bump Version - Analyze current version and determine next version'},
       {'id': 'rw-step-3', 'status': 'pending', 'content': 'Step 3: Create Detailed Changelog - Generate CHANGELOG with full timestamp'},
       {'id': 'rw-step-4', 'status': 'pending', 'content': 'Step 4: Update Main Changelog - Add summary entry'},
       {'id': 'rw-step-5', 'status': 'pending', 'content': 'Step 5: Update README - Update version badge and latest release'},
       {'id': 'rw-step-6', 'status': 'pending', 'content': 'Step 6: Update BR/FR Docs - Document flaws and fix attempts in Bug Reports and Feature Requests'},
       {'id': 'rw-step-7', 'status': 'pending', 'content': 'Step 7: Auto-update Kanban Docs - Update Epic/Story docs with version markers'},
       {'id': 'rw-step-8', 'status': 'pending', 'content': 'Step 8: Stage Files - Stage all modified files'},
       {'id': 'rw-step-9', 'status': 'pending', 'content': 'Step 9: Run Validators - Execute branch context and changelog format validators'},
       {'id': 'rw-step-10', 'status': 'pending', 'content': 'Step 10: Commit Changes - Create git commit with versioned message'},
       {'id': 'rw-step-11', 'status': 'pending', 'content': 'Step 11: Create Git Tag - Create annotated tag'},
       {'id': 'rw-step-12', 'status': 'pending', 'content': 'Step 12: Push to Remote - Push branch and tags'},
       {'id': 'rw-step-13', 'status': 'pending', 'content': 'Step 13: Post-Commit Verification & Reflection - Verify changes and reflect on results (optional but recommended)'},
       {'id': 'rw-step-14', 'status': 'pending', 'content': 'Step 14: Act on Verification Results - Update changelog, create follow-ups, document improvements (optional but recommended)'},
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

### 🔧 Config Loading (Before Step 1)

**MANDATORY:** Before executing any RW steps, load `rw-config.yaml` from project root if it exists. This is the **single source of truth** for all project-specific paths.

**Config Loading Pattern:**
```python
from pathlib import Path
import yaml

config = None
config_path = Path("rw-config.yaml")
if config_path.exists():
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
    except Exception:
        pass  # Fall back to placeholders

# Extract paths from config or use fallbacks
version_file = config['version_file'] if config and 'version_file' in config else 'src/{project}/version.py'
main_changelog = config['main_changelog'] if config and 'main_changelog' in config else 'CHANGELOG.md'
changelog_dir = config['changelog_dir'] if config and 'changelog_dir' in config else 'docs/changelogs'
scripts_path = config['scripts_path'] if config and 'scripts_path' in config else 'scripts/validation'
readme_file = config['readme_file'] if config and 'readme_file' in config else 'README.md'
kanban_root = config.get('kanban_root') if config and config.get('use_kanban') else None
epic_doc_pattern = config.get('epic_doc_pattern') if config and config.get('use_kanban') else None
story_doc_pattern = config.get('story_doc_pattern') if config and config.get('use_kanban') else None
```

**Philosophy:**
- **Config-driven (preferred):** If `rw-config.yaml` exists, use its values as the single source of truth
- **Backward compatible:** If config doesn't exist, use placeholder patterns (ensures RW works in projects that haven't run the installer)
- **Consistent:** All steps use the same config values loaded at the start

**Note:** Validation scripts (`validate_branch_context.py`, `validate_changelog_format.py`) automatically load `rw-config.yaml` if available, so they will use the same paths.

---

### Step 1: Branch Safety Check

**🚨 MANDATORY BLOCKING STEP - DO NOT BYPASS**

**Step Definition:**
```yaml
- id: step-1
  name: Branch Safety Check
  handler: release.branch_safety_check
  dependencies: []
  mandatory: true  # MANDATORY: Cannot be skipped
  blocking: true   # BLOCKING: Stops workflow on failure
  config:
    check_modified_files: true
    check_version_alignment: true
    check_changelog_alignment: true
    use_validator: true  # MANDATORY: Must use validate_branch_context.py
    strict_mode: true     # MANDATORY: Validator must run in strict mode
```

**CRITICAL REQUIREMENTS:**
- ✅ **MANDATORY:** This step MUST run before ANY file modifications
- ✅ **BLOCKING:** If this step fails, the workflow MUST STOP immediately
- ✅ **NON-OPTIONAL:** This step cannot be skipped, bypassed, or ignored
- ✅ **VALIDATOR REQUIRED:** Must run `validate_branch_context.py` with `--strict` flag
- ✅ **EXIT CODE CHECK:** Must check validator exit code and stop on non-zero
- ❌ **DO NOT PROCEED:** If Step 1 fails, DO NOT proceed to Step 2 or any subsequent step

**Agent Execution:**

1. **ANALYZE:**
   - **Load config first:** Load `rw-config.yaml` if it exists (see Config Loading section above)
   - Get current Git branch name (e.g., `epic/4` [Example: Confidentia], `epic/2` [Example: vibe-dev-kit], `main`)
   - **MANDATORY:** Determine validator script path:
     - From config: `scripts_path` + `/validate_branch_context.py`
     - Fallback: `packages/frameworks/workflow mgt/scripts/validation/validate_branch_context.py` [Example: vibe-dev-kit]
     - Or: `scripts/validation/validate_branch_context.py` [Example: Confidentia]
   - Verify validator script exists (if not found, this is a critical error - workflow must stop)

2. **DETERMINE:**
   - **MANDATORY ACTION:** Run `validate_branch_context.py` with `--strict` flag
   - **Command:** `python {validator_path} --strict`
   - **Expected Behavior:**
     - Exit code 0 = PASS (branch and work align)
     - Exit code 1 = FAIL (branch and work do not align)
   - **CRITICAL:** If validator script is missing or cannot be executed, workflow MUST STOP

3. **EXECUTE:**
   - **MANDATORY:** Execute validator script:
     ```bash
     python {validator_path} --strict
     ```
   - **Capture exit code:** Store the exit code from validator execution
   - **Capture output:** Store validator output for error messages
   - **DO NOT MODIFY FILES:** This step runs BEFORE any file modifications

4. **VALIDATE:**
   - **Check exit code:**
     - ✅ **PASS (exit code 0):** Branch and work align correctly
     - ❌ **FAIL (exit code 1 or non-zero):** Branch and work do not align
   - **CRITICAL RULE:** If exit code is non-zero, workflow MUST STOP immediately
   - **NO EXCEPTIONS:** Do not proceed to Step 2 if validation fails

5. **PROCEED:**
   - **If PASS (exit code 0):**
     - Document: "✅ Branch safety check passed - work aligns with current branch"
     - Mark Step 1 TODO as `completed`
     - Move to Step 2
   
   - **If FAIL (exit code 1 or non-zero):**
     - **MANDATORY ACTIONS:**
       1. Document: "🚨 RW BLOCKED: Branch Safety Check Failed"
       2. Output clear error message using validator output:
          ```
          🚨 RELEASE WORKFLOW BLOCKED
          
          Step 1: Branch Safety Check - FAILED
          
          Reason: Current branch '{branch}' does not align with the work being released.
          
          Details:
          - Current branch: {branch}
          - Expected branch: epic/{expected_epic}
          - Version file shows: {version}
          - Detected epic from work: {detected_epic}
          
          Validator Output:
          {validator_output}
          
          Action Required:
          1. Switch to the correct branch: git checkout epic/{correct_epic}
          2. Verify your changes align with the branch: git status
          3. Then run RW again
          
          RW is NOT complete. Workflow stopped at Step 1.
          All subsequent steps have been cancelled.
          ```
       3. Mark Step 1 TODO as `cancelled`
       4. Mark ALL remaining steps (2-14) as `cancelled`:
          ```python
          todo_write(merge=True, todos=[
              {'id': 'rw-step-1', 'status': 'cancelled'},
              {'id': 'rw-step-2', 'status': 'cancelled'},
              {'id': 'rw-step-3', 'status': 'cancelled'},
              # ... mark all remaining steps as cancelled
          ])
          ```
       5. **STOP WORKFLOW:** Do not execute any further steps
       6. **DO NOT PROCEED:** Do not attempt Step 2 or any subsequent step
       7. **DO NOT MODIFY FILES:** No file modifications should occur after Step 1 failure

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
   - Extract Task number (e.g., `E4:S03:T02` → Task 2)
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

**🚨 MANDATORY: Follow this 6-step procedure (A-F) exactly. Do not skip any step.**

**A. READ CURRENT VERSION:**
1. **ANALYZE:**
   - **Use config path:** Read current version from version file (from config `version_file` or fallback):
     - [Example: Confidentia] `src/confidentia/version.py` (or from `rw-config.yaml` if present)
     - [Example: vibe-dev-kit] `src/fynd_deals/version.py` (or from `rw-config.yaml` if present)
   - Extract current `VERSION_EPIC`, `VERSION_STORY`, `VERSION_TASK`, `VERSION_BUILD`
   - Document current version: `RC.EPIC.STORY.TASK+BUILD`
   - Understand version schema: `RC.EPIC.STORY.TASK+BUILD`
   - Check current Git branch to determine Epic number (already validated in Step 1)
   - Verify version matches branch schema (already checked in Step 1, but double-check)

**B. IDENTIFY COMPLETED TASK (MANDATORY):**
2. **ANALYZE (continued):**
   - **MANDATORY:** Read the Story file to identify completed task. **Use config paths:** If `rw-config.yaml` exists and `use_kanban: true`, use `kanban_root` and `story_doc_pattern` from config. Otherwise, use fallback patterns:
     - [Example: Confidentia] `KB/PM_and_Portfolio/epics/overview/Epic {epic}/Story-{story}-*.md` (or from `rw-config.yaml` if present)
     - [Example: vibe-dev-kit] `KB/PM_and_Portfolio/kanban/epics/Epic-{epic}/Story-{story}-*.md` (or from `rw-config.yaml` if present)
   - Find the MOST RECENTLY COMPLETED task in the Task Checklist (marked `✅ COMPLETE`)
   - Extract the task number from the task identifier: `E{epic}:S{story}:T{task}` (e.g., `E2:S02:T08` → task number is `8`)
   - **CRITICAL:** If no task is marked complete, or you cannot identify which task was just completed, **STOP** and ask the user which task was completed
   - **CRITICAL:** Document the completed task number for comparison

**C. DETERMINE VERSION BUMP (MANDATORY LOGIC):**
3. **DETERMINE:**
   - **MANDATORY:** Compare completed task number to current `VERSION_TASK`:
     - **IF completed task number > current VERSION_TASK:** This is a NEW TASK (forward progression)
       - Set `VERSION_TASK` = completed task number
       - Set `VERSION_BUILD` = 1 (reset to 1 for new task)
       - Example: Current `0.2.2.3+5`, completed T008 → New version: `0.2.2.8+1`
       - [Example: vibe-dev-kit] If completing Task 2, and `VERSION_TASK = 1`:
         - Update: `VERSION_TASK = 2`, `VERSION_BUILD = 1`
         - Next version: `0.4.3.2+1` (Task 2, Build 1)
     - **IF completed task number == current VERSION_TASK:** This is SAME TASK, new build
       - Keep `VERSION_TASK` unchanged
       - Increment `VERSION_BUILD` by 1
       - Example: Current `0.2.2.3+1`, completed T003 → New version: `0.2.2.3+2`
       - [Example: Confidentia] If current is `0.4.3.2+8`, next is `0.4.3.2+9`
       - [Example: vibe-dev-kit] If current is `0.2.1.1+2`, next is `0.2.1.1+3`
     - **IF completed task number < current VERSION_TASK:** This is OUT-OF-ORDER TASK COMPLETION
       - **This is VALID** - Tasks can be completed out of sequential order
       - Set `VERSION_TASK` = completed task number (use completed task, not current)
       - Set `VERSION_BUILD` = 1 (reset to 1 for the completed task)
       - Example: Current `0.3.2.6+1`, completed T005 → New version: `0.3.2.5+1`
       - **CRITICAL:** Version reflects completed task, not current VERSION_TASK
       - **CRITICAL:** Changelog entry will appear before higher task numbers (canonical ordering)
       - **Note:** This enables parallel task work and out-of-order completion
   - Validate version matches branch:
     - [Example: Confidentia] Epic 4 = `0.4.x.x+x`
     - [Example: vibe-dev-kit] Epic 2 = `0.2.x.x+x`

**D. VALIDATE BEFORE UPDATING:**
4. **VALIDATE (before update):**
   - Verify: New `VERSION_TASK` matches completed task number (always use completed task, not current)
   - Verify: If new task or out-of-order task, `VERSION_BUILD` = 1; if same task, `VERSION_BUILD` = current + 1
   - Document decision: "Task {completed_task} completed. Current TASK={current_task}, BUILD={current_build}. Decision: {new_task/out_of_order/same_task} → TASK={new_task}, BUILD={new_build}"

**E. UPDATE VERSION FILE:**
5. **EXECUTE:**
   - **If Task Transition (New Task or Out-of-Order Task):**
     - Update `VERSION_TASK` to match completed Task number (always use completed task, not current)
     - Update `VERSION_BUILD` to 1
     - **Use config path:** Update version file (from config `version_file` or fallback):
       - [Example: Confidentia] `src/confidentia/version.py` (or from `rw-config.yaml` if present)
       - [Example: vibe-dev-kit] `src/fynd_deals/version.py` (or from `rw-config.yaml` if present)
       - Use `search_replace` tool to update both `VERSION_TASK` and `VERSION_BUILD`
   - **If Same Task (BUILD Increment):**
     - Update `VERSION_BUILD` only (increment by 1)
     - **Use config path:** Update version file (from config `version_file` or fallback):
       - [Example: Confidentia] `src/confidentia/version.py` (or from `rw-config.yaml` if present)
       - [Example: vibe-dev-kit] `src/fynd_deals/version.py` (or from `rw-config.yaml` if present)
       - Use `search_replace` tool to update `VERSION_BUILD`
   - Update `VERSION_STRING` to reflect new version
   - Update `VERSION_INFO["description"]` if present

**F. VALIDATE AFTER UPDATING:**
6. **VALIDATE (after update):**
   - Re-read version file to confirm update
   - Verify version format is valid: `RC.EPIC.STORY.TASK+BUILD`
   - Check version matches branch schema
   - **CRITICAL:** Verify `VERSION_TASK` matches completed task number from Story (always use completed task)
   - **CRITICAL:** If Task transition (new or out-of-order), verify `VERSION_BUILD = 1`
   - **CRITICAL:** If same Task, verify `VERSION_BUILD` incremented correctly (current + 1)

7. **PROCEED:**
   - Document version bump with decision rationale:
     - **If Task Transition:**
       - [Example: vibe-dev-kit] "Version bumped: Task transition detected. Task E2:S02:T08 completed. Current TASK=3, BUILD=5. Decision: new_task → TASK=8, BUILD=1. New version: 0.2.2.8+1"
     - **If Same Task:**
       - [Example: Confidentia] "Version bumped: Task E4:S03:T02 completed. Current TASK=2, BUILD=8. Decision: new_build → TASK=2, BUILD=9. New version: 0.4.3.2+9"
       - [Example: vibe-dev-kit] "Version bumped: Task E2:S01:T01 completed. Current TASK=1, BUILD=2. Decision: new_build → TASK=1, BUILD=3. New version: 0.2.1.1+3"
   - Pass `new_version` to Step 3
   - Move to Step 3

**🚨 CRITICAL REMINDERS:**
- **NEVER skip reading the Story file** - It's the source of truth for completed tasks
- **NEVER assume same task** - Always compare completed task number to current VERSION_TASK
- **ALWAYS validate before and after** - Catch errors before they propagate
- **ALWAYS document your decision** - Show your work for traceability
- See `KB/Architecture/Standards_and_ADRs/versioning-error-reference-guide.md` for error prevention reference

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
   - **Use config path:** Create changelog file path (from config `changelog_dir` or fallback):
     - [Example: Confidentia] `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.4.3.2+9.md` (or from `rw-config.yaml` if present)
     - [Example: vibe-dev-kit] `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.2.1.1+3.md` (or from `rw-config.yaml` if present)
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
   - **Use config path:** Read main changelog (from config `main_changelog` or fallback `CHANGELOG.md`) to find "## Recent Releases" section
   - **CRITICAL - Canonical Ordering:** Read ALL existing changelog entries and extract version numbers
   - Parse existing version numbers: Extract `## [version]` headers and parse `RC.EPIC.STORY.TASK+BUILD` format
   - Understand canonical ordering: Versions must be ordered by version number (RC → EPIC → STORY → TASK → BUILD), NOT by insertion time
   - Understand date format: `DD-MM-YY` (e.g., `01-12-25`)

2. **DETERMINE:**
   - Generate summary date: Current date in `DD-MM-YY` format
   - Determine entry format: `### [version] - date`
   - **CRITICAL - Find Correct Insertion Point:**
     - Parse new version: `RC.EPIC.STORY.TASK+BUILD` → (RC, EPIC, STORY, TASK, BUILD)
     - For each existing entry:
       - Parse existing version: `RC.EPIC.STORY.TASK+BUILD` → (RC, EPIC, STORY, TASK, BUILD)
       - Compare versions using canonical ordering:
         - Compare RC first (if equal, continue)
         - Compare EPIC second (if equal, continue)
         - Compare STORY third (if equal, continue)
         - Compare TASK fourth (if equal, continue)
         - Compare BUILD last
       - If new version < existing version: Insert before this entry
       - If new version > existing version: Continue to next entry
     - If no existing entry is greater: Insert at end
   - **NEVER assume "top" or "newest"** - Always use version number comparison
   - Create summary entry with link to detailed changelog

3. **EXECUTE:**
   - Insert new entry at correct position based on canonical ordering (NOT at top)
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
   - **CRITICAL - Canonical Ordering Validation:**
     - Verify entry is in correct canonical order (by version number, NOT by insertion time)
     - Re-read changelog entries and verify all versions are in canonical order
     - Check that new version appears after all smaller versions and before all larger versions
     - If ordering violation detected: **STOP** and report error
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
   - **Use config path:** Read README file (from config `readme_file` or fallback `README.md`) to find version badge and latest release callout
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

### Step 6: Update BR/FR Docs

**Step Definition:**
```yaml
- id: step-6
  name: Update BR/FR Docs
  handler: release.br_fr_update
  dependencies: [step-2]
  config:
    fr_br_root: KB/PM_and_Portfolio/kanban/fr-br  # Default location for FR/BR files
    br_pattern: BR-*.md
    fr_pattern: FR-*.md
```

**Agent Execution:**

1. **ANALYZE:**
   - Get `new_version` from Step 2:
     - [Example: vibe-dev-kit] `"0.2.1.1+3"`
   - Get completed task identifier from Step 2:
     - [Example: vibe-dev-kit] `E2:S01:T01`
   - Get release summary from workflow parameters
   - Extract Epic/Story/Task from completed task identifier
   - **Use config paths:** Find FR/BR root directory (from config `fr_br_root` or fallback):
     - [Example: vibe-dev-kit] `KB/PM_and_Portfolio/kanban/fr-br` (or from `rw-config.yaml` if present)
   - Understand BR/FR linking pattern:
     - BRs/FRs are linked to Tasks via "Intake Decision" section
     - Search for BR/FR files that reference the completed task
   - Understand fix attempt documentation requirements:
     - Document flaw description
     - Document attempted fix
     - Document verification status
     - Document lessons learned (if fix failed)

2. **DETERMINE:**
   - **Search for linked BR/FR files:**
     - Search Story file for references to BR/FR files
     - Search Epic file for references to BR/FR files
     - Search task description for BR/FR links
     - Search "Intake Decision" sections in BR/FR files for task references
   - **For Bug Reports (BR):**
     - If BR is linked to completed task:
       - Add new entry to "Fix Attempt History" section
       - Document flaw description (from BR or task description)
       - Document attempted fix (from changelog or task description)
       - Document verification status (from Step 3 changelog or task)
       - Document lessons learned if fix failed
   - **For Feature Requests (FR):**
     - If FR is linked to completed task:
       - Update "Intake Decision" section with implementation status
       - Document implementation details (from changelog or task description)
       - Document verification status (from Step 3 changelog or task)
   - **If no BR/FR linked:**
     - Skip this step (no BR/FR to update)
     - Document: "No BR/FR linked to this task"

3. **EXECUTE:**
   - **For Bug Reports:**
     - Read BR file
     - Add new entry to "Fix Attempt History" section:
       ```markdown
       #### Attempt N: [Version] - [Date]
       
       **Fix Description:**
       [Describe what was attempted to fix this bug]
       
       **Changes Made:**
       - [List specific changes from changelog or task description]
       
       **Verification Status:**
       - [ ] Verified (test suite passed / manual test passed)
       - [ ] Attempted Fix (pending verification)
       - [ ] Fix Failed (bug still present)
       
       **Verification Method:**
       - [ ] Test suite execution
       - [ ] Manual testing
       - [ ] Both
       
       **Verification Evidence:**
       [Link to test results, CI/CD output, or documentation]
       
       **Result:**
       - [ ] Bug Fixed
       - [ ] Bug Partially Fixed (describe partial fix)
       - [ ] Bug Not Fixed (describe why fix didn't work)
       
       **Lessons Learned:**
       [What was learned from this attempt? What should be tried differently next time?]
       
       **Next Steps:**
       [What should be attempted in the next fix attempt?]
       ```
     - Update BR file with fix attempt entry
   - **For Feature Requests:**
     - Read FR file
     - Update "Intake Decision" section:
       - Add implementation status: `**Implementation Status:** IMPLEMENTED (v{version})`
       - Add implementation date: `**Implementation Date:** {date}`
       - Add verification status: `**Verification Status:** {Verified/Attempted Fix (pending verification)}`
     - Update FR file with implementation status

4. **VALIDATE:**
   - Verify BR file was updated with fix attempt entry (if BR linked)
   - Verify FR file was updated with implementation status (if FR linked)
   - Verify fix attempt entry includes all required fields:
     - Fix Description
     - Changes Made
     - Verification Status
     - Result
   - Verify version number is correct in fix attempt entry
   - Verify date is correct in fix attempt entry
   - Check that lessons learned are documented (if fix failed)

5. **PROCEED:**
   - Document: "Updated BR/FR docs with fix attempt information"
   - Move to Step 7 (can run in parallel with Steps 4-7)

---

### Step 7: Auto-update Kanban Docs

**Step Definition:**
```yaml
- id: step-7
  name: Auto-update Kanban Docs
  handler: confidentia.kanban_update  # [Example: Confidentia] Use {project}.kanban_update or kanban.update
  # [Example: vibe-dev-kit] handler: vibe-dev-kit.kanban_update (if implemented)
  dependencies: [step-2]
  config:
    epic_doc_pattern: KB/PM_and_Portfolio/epics/overview/Epic {epic}/Epic-{epic}.md  # [Example: Confidentia]
    # [Example: vibe-dev-kit] epic_doc_pattern: KB/PM_and_Portfolio/kanban/epics/Epic-{epic}/Epic-{epic}.md
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
   - **Use config paths:** Find Epic doc (from config `kanban_root` and `epic_doc_pattern` if `use_kanban: true`, or fallback):
     - [Example: Confidentia] `KB/PM_and_Portfolio/epics/overview/Epic 4/Epic-4.md` (or from `rw-config.yaml` if present)
     - [Example: vibe-dev-kit] `KB/PM_and_Portfolio/kanban/epics/Epic-2/Epic-2.md` (or from `rw-config.yaml` if present)
   - **Use config paths:** Find Story doc (from config `kanban_root` and `story_doc_pattern` if `use_kanban: true`, or fallback):
     - [Example: Confidentia] `KB/PM_and_Portfolio/kanban/Epic 4/Story-3-*.md` (or from `rw-config.yaml` if present)
     - [Example: vibe-dev-kit] `KB/PM_and_Portfolio/kanban/epics/Epic-2/Story-001-*.md` (or from `rw-config.yaml` if present)
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
     4. **CRITICAL: Update Story file FIRST, then Epic file to match**
     5. Update ALL sections to match the updated Story file's state

3. **EXECUTE:**
   - **CRITICAL: Update Story file FIRST, then Epic file to match:**
   - **FIRST: Update the Story file (`Story-{N}-{Name}.md`) task checklist:**
     - Add forensic marker `(v{version})` to the completed task in the Task Checklist
     - Example: `✅ COMPLETE (v0.11.5.2+1)`
     - Update Story doc header "Last updated" and "Version" fields
     - Update Story doc detailed Task sections with forensic markers
   - **THEN: Update Epic-{epic}/Epic-{epic}.md to match the updated Story file:**
     - Update Epic doc header "Last updated" field
     - Update Epic doc Story Checklist with version marker (format: `- [ ] **E4:S03 – Story Name** - IN PROGRESS (v{version})`)
     - Update Epic doc detailed Story sections (Status, Last updated, Task checkboxes with forensic markers)
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
   - Move to Step 8 (waits for Steps 2-7 to complete)

---

### Step 8: Stage Files

**Step Definition:**
```yaml
- id: step-8
  name: Stage Files
  handler: git.stage_all
  dependencies: [step-2, step-3, step-4, step-5, step-6, step-7]
  config:
    paths: ["*"]
```

**Agent Execution:**

1. **ANALYZE:**
   - Understand all files modified in Steps 2-7:
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
   - Move to Step 9

---

### Step 9: Run Validators

**Step Definition:**
```yaml
- id: step-9
  name: Run Validators
  handler: confidentia.run_validators  # [Example: Confidentia] Use {project}.run_validators or validation.run_validators
  # [Example: vibe-dev-kit] handler: vibe-dev-kit.run_validators (if implemented)
  dependencies: [step-8]
  config:
    validators:
      - scripts/validation/validate_branch_context.py  # Use {validation_scripts_path}/validate_branch_context.py
      - scripts/validation/validate_changelog_format.py  # Use {validation_scripts_path}/validate_changelog_format.py
      - scripts/validation/validate_version_bump.py  # Use {validation_scripts_path}/validate_version_bump.py
    strict_mode: true
```

**Agent Execution:**

1. **ANALYZE:**
   - Understand validators to run:
     - `validate_branch_context.py` - Checks branch/version/epic alignment
     - `validate_changelog_format.py` - Checks changelog format (including canonical ordering)
     - `validate_version_bump.py` - Checks version bump logic (task transitions, out-of-order completion)
   - Understand strict mode: Failures block workflow
   - Check validators exist and are executable
   - **CRITICAL - Changelog Ordering:** `validate_changelog_format.py` now validates canonical ordering
   - **CRITICAL - Version Bump Logic:** `validate_version_bump.py` validates RW Step 2 logic is followed correctly

2. **DETERMINE:**
   - Run each validator with `--strict` flag
   - Collect output from each validator
   - Determine if validators passed or failed

3. **EXECUTE:**
   - **Use config path:** Run validators (from config `scripts_path` or fallback `scripts/validation/`):
     - `python {scripts_path}/validation/validate_branch_context.py --strict` (script automatically reads `rw-config.yaml` if available)
     - `python {scripts_path}/validation/validate_changelog_format.py --strict` (script automatically reads `rw-config.yaml` if available)
     - `python {scripts_path}/validation/validate_version_bump.py --strict` (script automatically reads `rw-config.yaml` if available)
   - Capture exit codes and output

4. **VALIDATE:**
   - Check exit codes: 0 = success, non-zero = failure
   - If any validator fails in strict mode, workflow must abort
   - Analyze error messages if validators fail
   - **CRITICAL:** `validate_version_bump.py` validates:
     - Completed task vs. current VERSION_TASK comparison
     - New task detection (VERSION_TASK = completed, BUILD = 1)
     - Same task detection (VERSION_TASK unchanged, BUILD incremented)
     - Out-of-order completion (VERSION_TASK = completed, BUILD = 1)

5. **PROCEED:**
   - If validators pass: Document "Validators passed: branch context ✓, changelog format ✓, changelog ordering ✓, version bump logic ✓", move to Step 9
   - If validators fail: Abort workflow, report errors, do not proceed

---

### Step 10: Commit Changes

**Step Definition:**
```yaml
- id: step-10
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

### Step 11: Create Git Tag

**Step Definition:**
```yaml
- id: step-11
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

### Step 12: Push to Remote

**Step Definition:**
```yaml
- id: step-12
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
   - Get tag name from Step 11:
     - [Example: Confidentia] `v0.4.3.2+9`
     - [Example: vibe-dev-kit] `v0.2.1.1+3`
   - Understand remote: `origin`
   - **CRITICAL:** Must use `required_permissions: ['network']` for git push commands
   - This enables network access in Cursor's sandbox environment
   - See: `KB/Architecture/Standards_and_ADRs/agent-network-access-and-git-push-limitations.md`

2. **DETERMINE:**
   - Push branch:
     - [Example: Confidentia] `git push origin epic/4`
     - [Example: vibe-dev-kit] `git push origin main` (or `epic/2`)
   - Push tag:
     - [Example: Confidentia] `git push origin v0.4.3.2+9`
     - [Example: vibe-dev-kit] `git push origin v0.2.1.1+3`
   - **Use network permissions:** Always use `required_permissions: ['network']` for git push
   - **Prepare fallback:** If push still fails (shouldn't happen), provide clear user instructions

3. **EXECUTE:**
   - **CRITICAL: Use `required_permissions: ['network']` for git push commands**
   - **Attempt push with network permissions:**
     ```python
     # ✅ CORRECT - With network permissions
     run_terminal_cmd(
         command=f"git push origin {branch_name} --tags",
         required_permissions=['network']  # Enable network access for git push
     )
     print("✅ Successfully pushed branch and tags to remote")
     ```
   - **If push fails (fallback):**
     ```python
     try:
         run_terminal_cmd(
             command=f"git push origin {branch_name} --tags",
             required_permissions=['network']
         )
     except Exception as e:
         # Handle push failures gracefully (should not happen with network permissions)
         print("⚠️  Push failed - see manual push instructions below")
         print("\n📋 Manual Push Required:")
         print(f"   git push origin {branch_name} --tags")
         # Don't fail the workflow - provide instructions instead
     ```
   - **If push fails:**
     - Provide clear user instructions
     - Show exact command to run
     - Link to network access limitations document
     - Mark workflow as "complete pending push"

4. **VALIDATE:**
   - **If push succeeds:**
     - ✅ Verify branch push succeeded
     - ✅ Verify tag push succeeded
     - ✅ Check for any errors or warnings
   - **If push fails:**
     - ✅ Verify user instructions were provided
     - ✅ Verify workflow marked as complete (pending push)
     - ✅ Don't fail the entire workflow

5. **PROCEED:**
   - **If push succeeded:**
     - Document: "Pushed branch and tag to origin"
     - Move to Step 12 (if enabled)
   - **If push failed:**
     - Document: "Push failed due to network restrictions - manual push required"
     - Provide user instructions:
       ```markdown
       📋 Manual Push Required:
       
       Due to sandbox environment network restrictions, please run:
       
       ```bash
       git push origin main --tags
       ```
       
       See: KB/Architecture/Standards_and_ADRs/agent-network-access-and-git-push-limitations.md
       ```
     - Mark workflow as "complete pending push"
     - Move to Step 12 (if enabled) - workflow is still considered successful

**Error Handling:**

**CRITICAL: Use Network Permissions:**
- **ALWAYS use `required_permissions: ['network']`** for git push commands
- This enables network access in Cursor's sandbox environment
- Without this, push will fail with "Could not resolve host" errors

**Example Implementation (Correct):**
```python
# ✅ CORRECT - Use required_permissions for network access
run_terminal_cmd(
    command=f"git push origin {branch_name} --tags",
    required_permissions=['network']  # Enable network access
)
print("✅ Successfully pushed to remote")
```

**Example Error Handling (Fallback - Should Not Be Needed):**
```python
try:
    run_terminal_cmd(
        command=f"git push origin {branch_name} --tags",
        required_permissions=['network']
    )
    print("✅ Successfully pushed to remote")
except Exception as e:
    # Fallback: Should not happen if network permissions are used correctly
    print("⚠️  Push failed unexpectedly")
    print("\n📋 Manual Push Required:")
    print(f"   git push origin {branch_name} --tags")
    print("\n   See: KB/Architecture/Standards_and_ADRs/agent-network-access-and-git-push-limitations.md")
    # Don't fail the workflow - mark as complete pending push
    return "complete_pending_push"
```

**Related Documentation:**
- **Network Access Limitations:** `KB/Architecture/Standards_and_ADRs/agent-network-access-and-git-push-limitations.md` - Complete guide on this issue and solutions

---

### Step 13: Post-Commit Verification & Reflection

**Step Definition:**
```yaml
- id: step-13
  name: Post-Commit Verification & Reflection
  handler: release.verification_reflection
  dependencies: [step-10]
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

### Step 14: Act on Verification Results

**Step Definition:**
```yaml
- id: step-14
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
   - Get verification status from Step 13:
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

**Integration with Step 13:**
- Step 14 depends on Step 13 (CHECK phase)
- Uses verification status from Step 13
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
- Follow-up task: E2:S02:T07 – Fix Step 12 verification issue
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
- [ ] **Step 6:** Analyzed BR/FR docs, updated fix attempt history, validated
- [ ] **Step 7:** Analyzed Kanban docs, updated Epic/Story docs, validated
- [ ] **Step 8:** Analyzed modified files, staged all files, validated
- [ ] **Step 9:** Analyzed validators, ran both validators, validated results
- [ ] **Step 10:** Analyzed template, built message, created commit, validated
- [ ] **Step 11:** Analyzed tag format, created annotated tag, validated
- [ ] **Step 12:** Analyzed remote, pushed branch and tag, validated
- [ ] **Step 13:** Analyzed changes, prompted for verification, documented reflection, validated (optional but recommended)
- [ ] **Step 14:** Analyzed verification results, acted on results, updated changelog, created follow-ups, validated (optional but recommended)

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
- Agent waits for Step 8 to complete before Step 9
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

**Reference Documentation:**
- **[Workflow Flaws Reference Guide](../../Architecture/Standards_and_ADRs/workflow-flaws-reference-guide.md)** - Comprehensive reference for all discovered RW flaws
- **[Versioning Error Reference Guide](../../Architecture/Standards_and_ADRs/versioning-error-reference-guide.md)** - Versioning-specific error reference (WF-002)

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
