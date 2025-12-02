# Release Workflow: Agent Execution Guide

**Version:** 1.0.0
**Last Updated:** 2025-12-01
**Related:** Epic 4 - User Workflows & Use Case Modeling, Release Workflow

---

## 📖 Overview

This document provides a **step-by-step agent execution guide** for the Release Workflow. The Release Workflow serves as the **canonical example** of intelligent agent-driven workflow execution.

**This guide shows exactly how an AI agent should analyze, determine, execute, validate, and proceed through each of the 10 Release Workflow steps.**

---

## 🎯 Execution Context

### Workflow Definition

**Workflow:** Release Workflow
**Type:** `release`
**Steps:** 10 steps organized into 2 phases
**Canonical Example:** Yes - this workflow demonstrates the agent-driven execution pattern

### Agent Execution Pattern

For each step, the agent follows this pattern:
1. **ANALYZE** - Understand step requirements and context
2. **DETERMINE** - Decide what actions to take
3. **EXECUTE** - Perform the actions
4. **VALIDATE** - Verify execution succeeded
5. **PROCEED** - Document and move to next step

### 🚨 MANDATORY: Progress Tracking with Cursor TODOs

**REQUIRED:** Agents **MUST** use `todo_write` to create and maintain a TODO list tracking all 10 Release Workflow steps. This is **NOT OPTIONAL** - it is a mandatory requirement for Release Workflow execution.

**Why TODOs are Required:**
- ✅ **User Visibility:** User can see real-time progress through all 10 steps
- ✅ **Agent Organization:** Helps agent stay organized across 10 sequential steps
- ✅ **Error Recovery:** Clear visibility into where execution stopped if interrupted
- ✅ **User Transparency:** User can verify all steps completed successfully
- ✅ **Status Management:** Automatic status updates provide clear execution state
- ✅ **Accountability:** Provides audit trail of workflow execution

**Required Implementation Pattern:**

1. **At Workflow Start (MANDATORY):** Create TODO list with all 10 steps as `pending`
   ```python
   todo_write(merge=False, todos=[
       {'id': 'rw-step-1', 'status': 'pending', 'content': 'Step 1: Bump Version - Analyze current version and determine next version'},
       {'id': 'rw-step-2', 'status': 'pending', 'content': 'Step 2: Create Detailed Changelog - Generate CHANGELOG with full timestamp'},
       {'id': 'rw-step-3', 'status': 'pending', 'content': 'Step 3: Update Main Changelog - Add summary entry'},
       {'id': 'rw-step-4', 'status': 'pending', 'content': 'Step 4: Update README - Update version badge and latest release'},
       {'id': 'rw-step-5', 'status': 'pending', 'content': 'Step 5: Auto-update Kanban Docs - Update Epic/Story docs with version markers'},
       {'id': 'rw-step-6', 'status': 'pending', 'content': 'Step 6: Stage Files - Stage all modified files'},
       {'id': 'rw-step-7', 'status': 'pending', 'content': 'Step 7: Run Validators - Execute branch context and changelog format validators'},
       {'id': 'rw-step-8', 'status': 'pending', 'content': 'Step 8: Commit Changes - Create git commit with versioned message'},
       {'id': 'rw-step-9', 'status': 'pending', 'content': 'Step 9: Create Git Tag - Create annotated tag'},
       {'id': 'rw-step-10', 'status': 'pending', 'content': 'Step 10: Push to Remote - Push branch and tags'},
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
   todo_write(merge=True, todos=[{'id': 'rw-step-10', 'status': 'completed'}])
   ```

**Enforcement:**
- ❌ **DO NOT** execute Release Workflow without creating TODO list first
- ❌ **DO NOT** skip TODO updates between steps
- ✅ **MUST** create TODO list before Step 1 execution
- ✅ **MUST** update TODO status before and after each step
- ✅ **MUST** mark all steps as completed on successful completion

**Note:** The markdown checklist below (lines 480-512) serves as a reference, but Cursor TODOs are the **REQUIRED** mechanism for real-time progress tracking and user visibility.

---

## 📋 Step-by-Step Agent Execution

### Step 1: Bump Version

**Step Definition:**
```yaml
- id: step-1
  name: Bump Version
  handler: release.version_bump
  config:
    version_file: src/confidentia/version.py
    increment_type: patch
```

**Agent Execution:**

1. **ANALYZE:**
   - Read current version from `src/confidentia/version.py`
   - Understand version schema: `RC.EPIC.STORY.TASK+BUILD`
   - Check current Git branch to determine Epic number
   - Understand increment type: `patch` means increment BUILD number
   - Check if version matches branch schema (e.g., `epic/4` → `0.4.x.x+x`)

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
   - Pass `new_version: "0.4.3.2+9"` to Step 2
   - Move to Step 2

---

### Step 2: Create Detailed Changelog

**Step Definition:**
```yaml
- id: step-2
  name: Create Detailed Changelog
  handler: release.changelog_create
  dependencies: [step-1]
  config:
    changelog_dir: KB/Changelog_and_Release_Notes/Changelog_Archive
    format: full_timestamp
```

**Agent Execution:**

1. **ANALYZE:**
   - Get `new_version` from Step 1 output: `"0.4.3.2+9"`
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
   - Create changelog file with proper format:
     - Release Date (full timestamp)
     - Epic and Story information
     - Type (with emoji)
     - Summary
     - Changes section
     - Related Tasks section

4. **VALIDATE:**
   - Verify file was created
   - Check timestamp format is correct (`YYYY-MM-DD HH:MM:SS UTC`)
   - Verify all required fields are present
   - Check file is readable

5. **PROCEED:**
   - Document: "Created detailed changelog: CHANGELOG_v0.4.3.2+9.md"
   - Pass `changelog_file` path to Step 3
   - Move to Step 3

---

### Step 3: Update Main Changelog

**Step Definition:**
```yaml
- id: step-3
  name: Update Main Changelog
  handler: release.changelog_update
  dependencies: [step-2]
  config:
    main_changelog: CHANGELOG.md
    date_format: DD-MM-YY
```

**Agent Execution:**

1. **ANALYZE:**
   - Get `new_version` from Step 1: `"0.4.3.2+9"`
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
   - Add link to detailed changelog file

4. **VALIDATE:**
   - Verify entry was inserted correctly
   - Check date format is `DD-MM-YY`
   - Verify link to detailed changelog is correct
   - Ensure entry is at top of Recent Releases

5. **PROCEED:**
   - Document: "Updated main changelog with summary entry"
   - Move to Step 4 (can run in parallel with Steps 4-5)

---

### Step 4: Update README

**Step Definition:**
```yaml
- id: step-4
  name: Update README
  handler: release.readme_update
  dependencies: [step-1]
  config:
    readme_file: README.md
    update_badge: true
    update_latest_release: true
```

**Agent Execution:**

1. **ANALYZE:**
   - Get `new_version` from Step 1: `"0.4.3.2+9"`
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
   - Move to Step 5 (can run in parallel with Steps 3-5)

---

### Step 5: Auto-update Kanban Docs

**Step Definition:**
```yaml
- id: step-5
  name: Auto-update Kanban Docs
  handler: confidentia.kanban_update
  dependencies: [step-1]
  config:
    epic_doc_pattern: KB/PM_and_Portfolio/epics/overview/Epic {epic}/Epic-{epic}.md
    kanban_board: KB/PM_and_Portfolio/epics/overview/_index.md
```

**Agent Execution:**

1. **ANALYZE:**
   - Get `new_version` from Step 1: `"0.4.3.2+9"`
   - Extract Epic number from branch: `epic/4` → Epic 4
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
   - Move to Step 6 (waits for Steps 1-5 to complete)

---

### Step 6: Stage Files

**Step Definition:**
```yaml
- id: step-6
  name: Stage Files
  handler: git.stage_all
  dependencies: [step-1, step-2, step-3, step-4, step-5]
  config:
    paths: ["*"]
```

**Agent Execution:**

1. **ANALYZE:**
   - Understand all files modified in Steps 1-5:
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
   - Move to Step 7

---

### Step 7: Run Validators

**Step Definition:**
```yaml
- id: step-7
  name: Run Validators
  handler: confidentia.run_validators
  dependencies: [step-6]
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
   - If validators pass: Document "Validators passed", move to Step 8
   - If validators fail: Abort workflow, report errors, do not proceed

---

### Step 8: Commit Changes

**Step Definition:**
```yaml
- id: step-8
  name: Commit Changes
  handler: git.commit
  dependencies: [step-7]
  config:
    message_template: "{version} - {summary}"
```

**Agent Execution:**

1. **ANALYZE:**
   - Get `new_version` from Step 1: `"0.4.3.2+9"`
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
   - Pass commit hash to Step 9 (if needed)
   - Move to Step 9

---

### Step 9: Create Git Tag

**Step Definition:**
```yaml
- id: step-9
  name: Create Git Tag
  handler: git.create_tag
  dependencies: [step-8]
  config:
    tag_template: v{version}
    message_template: "Release {tag}: {summary}"
    annotated: true
```

**Agent Execution:**

1. **ANALYZE:**
   - Get `new_version` from Step 1: `"0.4.3.2+9"`
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
   - Move to Step 10 (waits for Step 8 to complete)

---

### Step 10: Push to Remote

**Step Definition:**
```yaml
- id: step-10
  name: Push to Remote
  handler: git.push
  dependencies: [step-8, step-9]
  config:
    push_tags: true
    remote: origin
```

**Agent Execution:**

1. **ANALYZE:**
   - Get current branch name: `epic/4`
   - Get tag name from Step 9: `v0.4.3.2+9`
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
- [ ] **MANDATORY:** Created TODO list with all 10 steps (using `todo_write`)
- [ ] Loaded workflow definition from YAML
- [ ] Parsed all 10 steps and dependencies
- [ ] Gathered workflow parameters (summary, change_type, etc.)
- [ ] Checked current Git branch
- [ ] Verified workspace context

### Step Execution
- [ ] **Step 1:** Analyzed version, determined next version, updated file, validated
- [ ] **Step 2:** Analyzed requirements, generated timestamp, created changelog, validated
- [ ] **Step 3:** Analyzed format, determined date, updated CHANGELOG.md, validated
- [ ] **Step 4:** Analyzed README, updated badge and callout, validated
- [ ] **Step 5:** Analyzed Kanban docs, updated Epic/Story docs, validated
- [ ] **Step 6:** Analyzed modified files, staged all files, validated
- [ ] **Step 7:** Analyzed validators, ran both validators, validated results
- [ ] **Step 8:** Analyzed template, built message, created commit, validated
- [ ] **Step 9:** Analyzed tag format, created annotated tag, validated
- [ ] **Step 10:** Analyzed remote, pushed branch and tag, validated

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
# Step 1: Analyze version, determine next version, update file
# Step 2: Analyze changelog requirements, create file
# etc.
```

### ❌ Don't: Skip Analysis

**Bad:**
- Agent updates version without checking branch context
- Agent creates changelog without understanding format requirements
- Agent commits without validating

**Good:**
- Agent analyzes branch context before version bump
- Agent understands changelog format requirements
- Agent validates before committing

### ❌ Don't: Ignore Dependencies

**Bad:**
- Agent tries to create changelog before version is bumped
- Agent tries to commit before files are staged
- Agent tries to push before commit exists

**Good:**
- Agent waits for Step 1 to complete before Step 2
- Agent waits for Step 6 to complete before Step 7
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
4. **Use** ANALYZE → DETERMINE → EXECUTE → VALIDATE → PROCEED pattern for each step
5. **Document** analysis, actions, and results at each step

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

**Last Updated:** 2025-12-01
**Document Version:** 1.0.0
