# Release Workflow: Agent Execution Guide

**Version:** 1.0.0
**Last Updated:** 2025-12-01
**Related:** Epic 4 - User Workflows & Use Case Modeling, Release Workflow

---

## 📖 Overview

This document provides a **step-by-step agent execution guide** for the Release Workflow. The Release Workflow serves as the **canonical example** of intelligent agent-driven workflow execution.

**This guide shows exactly how an AI agent should analyze, determine, execute, validate, and proceed through each of the 11 Release Workflow steps.**

---

## 🎯 Execution Context

### Workflow Definition

**Workflow:** Release Workflow
**Type:** `release`
**Steps:** 11 steps organized into 2 phases
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

1. **At Workflow Start (MANDATORY):** Create TODO list with all 11 steps as `pending`
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
   - Get current Git branch name (e.g., `epic/4`, `main`)
   - Check if branch matches expected pattern (e.g., `epic/{n}` for epic branches)
   - Analyze modified files in working directory (`git status`, `git diff`)
   - Check if version file exists and read current version (if file is modified)
   - Check if changelog entries exist (if CHANGELOG.md is modified)
   - Extract expected epic number from branch name (e.g., `epic/4` → Epic 4)
   - Check modified file paths for epic-specific patterns (e.g., `Epic-4/`, `epic/4/`)

2. **DETERMINE:**
   - Determine if work aligns with current branch:
     - If on `epic/4`, modified files should relate to Epic 4
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
     - ✅ **PASS**: Work aligns with branch (e.g., on `epic/4`, all work is Epic 4 related)
     - ❌ **FAIL**: Work does not align with branch (e.g., on `epic/4`, but work references Epic 5)
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

- **On `epic/4` branch:**
  - ✅ Version file shows `0.4.x.x+x` → PASS
  - ✅ Modified files in `Epic-4/` directory → PASS
  - ✅ Changelog entry references Epic 4 → PASS
  - ❌ Version file shows `0.5.x.x+x` → FAIL (mismatch)
  - ❌ Modified files in `Epic-5/` directory → FAIL (mismatch)

- **On `main` branch:**
  - ✅ Any epic number allowed (main can have any epic)
  - ⚠️ Warning: Consider if RW should run on main (usually run on epic branch first)

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
    version_file: src/confidentia/version.py
    increment_type: patch
```

**Agent Execution:**

1. **ANALYZE:**
   - Read current version from `src/confidentia/version.py`
   - Understand version schema: `RC.EPIC.STORY.TASK+BUILD`
   - Check current Git branch to determine Epic number (already validated in Step 1)
   - Understand increment type: `patch` means increment BUILD number
   - Verify version matches branch schema (already checked in Step 1, but double-check)

2. **DETERMINE:**
   - Calculate next version: If current is `0.4.3.2+8`, next is `0.4.3.2+9`
   - Validate version matches branch (Epic 4 = `0.4.x.x+x`)
   - Determine if this is a task transition (would reset BUILD to 1)

3. **EXECUTE:**
   - Update `src/confidentia/version.py` with new version
   - Use `search_replace` tool to update version string

4. **VALIDATE:**
   - Read version file to confirm update
   - Verify version format is valid
   - Check version matches branch schema

5. **PROCEED:**
   - Document: "Version bumped: 0.4.3.2+8 → 0.4.3.2+9"
   - Pass `new_version: "0.4.3.2+9"` to Step 3
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
   - Get `new_version` from Step 2 output: `"0.4.3.2+9"`
   - Get release summary from workflow parameters
   - Get change type from workflow parameters
   - Extract Epic/Story from Git branch name (e.g., `epic/4` → Epic 4)
   - Understand timestamp format: `YYYY-MM-DD HH:MM:SS UTC`
   - Check changelog directory exists

2. **DETERMINE:**
   - Generate full timestamp: `date -u +"%Y-%m-%d %H:%M:%S UTC"`
   - Determine Epic number from branch (e.g., `epic/4` → Epic 4)
   - Determine Story number from version (e.g., `0.4.3.2+9` → Story 3)
   - Create changelog file path: `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.4.3.2+9.md`
   - Review previous changelog format for consistency

3. **EXECUTE:**
   - Generate timestamp using system command
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
   - Document: "Created detailed changelog: CHANGELOG_v0.4.3.2+9.md"
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
   - Get `new_version` from Step 2: `"0.4.3.2+9"`
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
   - Format: `### [0.4.3.2+9] - 01-12-25`
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
   - Get `new_version` from Step 2: `"0.4.3.2+9"`
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
  handler: confidentia.kanban_update
  dependencies: [step-2]
  config:
    epic_doc_pattern: KB/PM_and_Portfolio/epics/overview/Epic {epic}/Epic-{epic}.md
    kanban_board: KB/PM_and_Portfolio/epics/overview/_index.md
```

**Agent Execution:**

1. **ANALYZE:**
   - Get `new_version` from Step 2: `"0.4.3.2+9"`
   - Extract Epic number from branch: `epic/4` → Epic 4 (already validated in Step 1)
   - Extract Story number from version: `0.4.3.2+9` → Story 3
   - Find Epic doc: `KB/PM_and_Portfolio/epics/overview/Epic 4/Epic-4.md`
   - Find Story doc: `KB/PM_and_Portfolio/kanban/Epic 4/Story-3-*.md`
   - Understand "Last updated" field format

2. **DETERMINE:**
   - Update Epic doc "Last updated" field with version and summary
   - Update Story doc "Last updated" field with version and summary
   - Format: `**Last updated:** YYYY-MM-DD (v{version} – {summary})`
   - Determine if tasks should be marked complete (if applicable)

3. **EXECUTE:**
   - Update Epic doc "Last updated" field
   - Update Story doc "Last updated" field
   - If tasks completed, mark them with version numbers

4. **VALIDATE:**
   - Verify Epic doc was updated
   - Verify Story doc was updated
   - Check date format is correct
   - Verify version numbers are correct

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
  handler: confidentia.run_validators
  dependencies: [step-7]
  config:
    validators:
      - scripts/validation/validate_branch_context.py
      - scripts/validation/validate_changelog_format.py
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
   - Get `new_version` from Step 2: `"0.4.3.2+9"`
   - Get summary from parameters
   - Understand commit message template: `"{version} - {summary}"`
   - Verify files are still staged

2. **DETERMINE:**
   - Build commit message: `"0.4.3.2+9 - 📚 Documentation: Tighten Epic 4 Kanban docs..."`
   - Ensure message follows project conventions

3. **EXECUTE:**
   - Run `git commit -m "{message}"`
   - Capture commit hash if available

4. **VALIDATE:**
   - Verify commit was created (check exit code)
   - Verify commit message is correct
   - Check commit hash if available

5. **PROCEED:**
   - Document: "Created commit {hash} with message: {message}"
   - Pass commit hash to Step 10 (if needed)
   - Move to Step 10

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
   - Get `new_version` from Step 2: `"0.4.3.2+9"`
   - Get summary from parameters
   - Understand tag template: `v{version}` → `v0.4.3.2+9`
   - Understand message template: `"Release {tag}: {summary}"`
   - Understand annotated tag: Includes metadata

2. **DETERMINE:**
   - Build tag name: `v0.4.3.2+9`
   - Build tag message: `"Release v0.4.3.2+9: 📚 Documentation: Tighten Epic 4 Kanban docs..."`
   - Check if tag already exists (should not)

3. **EXECUTE:**
   - Run `git tag -a -m "{message}" v{version}`
   - Verify tag was created

4. **VALIDATE:**
   - Verify tag exists: `git tag -l "v0.4.3.2+9"`
   - Check tag message is correct
   - Verify tag is annotated

5. **PROCEED:**
   - Document: "Created annotated tag v0.4.3.2+9"
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
   - Get current branch name: `epic/4` (already validated in Step 1)
   - Get tag name from Step 10: `v0.4.3.2+9`
   - Understand remote: `origin`
   - Check network access and Git credentials

2. **DETERMINE:**
   - Push branch: `git push origin epic/4`
   - Push tag: `git push origin v0.4.3.2+9`
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
   - **Workflow Complete!**

---

## ✅ Agent Execution Checklist

**Note:** This markdown checklist serves as a reference. **Agents MUST use Cursor TODOs** (see "🚨 MANDATORY: Progress Tracking with Cursor TODOs" section above) for real-time progress tracking. TODOs are **REQUIRED**, not optional.

When executing Release Workflow as an agent, ensure:

### Pre-Execution
- [ ] **MANDATORY:** Created TODO list with all 11 steps (using `todo_write`)
- [ ] Loaded workflow definition from YAML
- [ ] Parsed all 11 steps and dependencies
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
