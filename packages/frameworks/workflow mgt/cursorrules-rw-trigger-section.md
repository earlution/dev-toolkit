---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-04T12:02:13Z
expires_at: null
housekeeping_policy: keep
---

# Cursor Rules: RW Trigger Section

**Purpose:** This section should be added to your project's `.cursorrules` file to enable the "RW" trigger for Release Workflow execution.

**Location in `.cursorrules`:** Add this section in the "Version Control and Release Process" section (or equivalent).

**Last Updated:** 2025-12-02  
**Source Project:** Originally fynd.deals (Epic 15, Story 1), now maintained in vibe-dev-kit as canonical SoT  
**Version:** 2.2.0 (abstracted version numbers and file paths, added schema calculation examples)

---

### 🚀 RELEASE WORKFLOW (RW) TRIGGER

**When the user types "RW" or "rw" (case-insensitive), execute the Release Workflow as an intelligent agent:**

1. **DO NOT** run the deterministic script `scripts/release_workflow.py`
2. **DO** execute the Release Workflow using the **intelligent agent-driven execution pattern**
3. **LOAD CONFIG FIRST (MANDATORY):** Before Step 1, load `rw-config.yaml` from project root if it exists. This is the **single source of truth** for all project-specific paths. If config exists, use its values. If not, use placeholders/examples (backward compatibility).
4. **Follow** the step-by-step guide below
5. **Start with Step 1: Branch Safety Check** - Analyze work and ensure it aligns with current branch before proceeding
6. **Execute all 11 steps** using the ANALYZE → DETERMINE → EXECUTE → VALIDATE → PROCEED pattern
7. **Document** each step's analysis, actions, and results
8. **MUST USE Cursor TODOs:** Create and maintain a TODO list tracking all 11 steps (see below)

**🔧 Config-Driven Approach (Preferred):**

If `rw-config.yaml` exists in project root, **MUST** load it and use its values for all paths:
- `version_file` → Use for version file path
- `main_changelog` → Use for main changelog path
- `changelog_dir` → Use for changelog archive directory
- `scripts_path` → Use for validation scripts path
- `readme_file` → Use for README path
- `kanban_root` → Use for Kanban root (if `use_kanban: true`)
- `epic_doc_pattern` → Use for epic document pattern (if Kanban enabled)
- `story_doc_pattern` → Use for story document pattern (if Kanban enabled)

**Loading Config Pattern:**
```python
# Load rw-config.yaml if it exists
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

# Use config values or fallback to defaults
version_file = config['version_file'] if config and 'version_file' in config else 'src/{project}/version.py'
main_changelog = config['main_changelog'] if config and 'main_changelog' in config else 'CHANGELOG.md'
changelog_dir = config['changelog_dir'] if config and 'changelog_dir' in config else 'docs/changelogs'
scripts_path = config['scripts_path'] if config and 'scripts_path' in config else 'scripts/validation'
readme_file = config['readme_file'] if config and 'readme_file' in config else 'README.md'
kanban_root = config.get('kanban_root', 'KB/PM_and_Portfolio/kanban') if config and config.get('use_kanban') else None
```

**Backward Compatibility:**
- If `rw-config.yaml` doesn't exist, use placeholder patterns (`{project}`, `{kanban_path}`, etc.)
- This ensures RW works in projects that haven't run the installer yet

**🚨 MANDATORY: Progress Tracking with Cursor TODOs**

**REQUIRED:** Agents **MUST** use `todo_write` to create and maintain a TODO list for all 11 Release Workflow steps:

1. **At Workflow Start:** Create TODO list with all 11 steps as `pending`
   ```python
   todo_write(merge=False, todos=[
       {'id': 'rw-step-1', 'status': 'pending', 'content': 'Step 1: Branch Safety Check - Analyze work and ensure it aligns with current branch'},
       {'id': 'rw-step-2', 'status': 'pending', 'content': 'Step 2: Bump Version - Read Story file, identify completed task number, compare to current VERSION_TASK, determine if new task or same task, update version file, validate'},
       {'id': 'rw-step-3', 'status': 'pending', 'content': 'Step 3: Create Detailed Changelog - Generate CHANGELOG with full timestamp'},
       {'id': 'rw-step-4', 'status': 'pending', 'content': 'Step 4: Update Main Changelog - Add summary entry'},
       {'id': 'rw-step-5', 'status': 'pending', 'content': 'Step 5: Update README - Update version badge and latest release'},
       {'id': 'rw-step-6', 'status': 'pending', 'content': 'Step 6: Auto-update Kanban Docs - Update Epic/Story docs with version markers'},
       {'id': 'rw-step-7', 'status': 'pending', 'content': 'Step 7: Stage Files - Stage all modified files'},
       {'id': 'rw-step-8', 'status': 'pending', 'content': 'Step 8: Run Validators - Execute branch context and changelog format validators'},
       {'id': 'rw-step-9', 'status': 'pending', 'content': 'Step 9: Commit Changes - Create git commit with versioned message'},
       {'id': 'rw-step-10', 'status': 'pending', 'content': 'Step 10: Create Git Tag - Create annotated tag'},
       {'id': 'rw-step-11', 'status': 'pending', 'content': 'Step 11: Push to Remote - Push branch and tags (with network permissions)'},
   ])
   ```

2. **Before Each Step:** Mark step as `in_progress`
   ```python
   todo_write(merge=True, todos=[{'id': 'rw-step-1', 'status': 'in_progress'}])
   ```

3. **After Each Step:** Mark step as `completed` and mark next step as `in_progress`
   ```python
   todo_write(merge=True, todos=[
       {'id': 'rw-step-1', 'status': 'completed'},
       {'id': 'rw-step-2', 'status': 'in_progress'}
   ])
   ```

4. **On Completion:** All steps marked as `completed`

5. **Atomicity & Blocking Behaviour (Accessibility-Critical):**

   - When the user types **`RW`**, the agent MUST either:
     - Run **all 11 steps (1–11)** to completion for the target version, OR
     - Stop at a **specific step** and clearly state:
       - The **step number and name** (e.g. "Step 1: Branch Safety Check" or "Step 8: Run Validators")
       - The **reason** it is blocked (e.g. wrong branch, missing tool, sandbox limitation)
       - The **exact action/commands** the user must run to unblock it
       - That **RW is NOT complete** until those actions are taken and the agent resumes

   - The agent MUST NOT:
     - Silently stop mid‑workflow after modifying files
     - Start a new RW while a previous RW's TODO items are still `pending` or `in_progress`

   - If RW is abandoned or cannot be completed, the agent MUST:
     - Mark remaining `rw-step-*` TODOs as `cancelled`
     - Output a short **"RW ABORTED"** summary with current state and next steps

**Agent Execution Pattern:**

For each step, follow this pattern:
1. **ANALYZE** - Understand step requirements and context
2. **DETERMINE** - Decide what actions to take
3. **EXECUTE** - Perform the actions
4. **VALIDATE** - Verify execution succeeded
5. **PROCEED** - Document and move to next step

**The 11 Steps:**

1. **Branch Safety Check** - Analyze work done and ensure it aligns with current branch. Check modified files, version alignment, and changelog alignment. If work does not align with branch (e.g., on `epic/4` but work references Epic 5), STOP workflow with clear warning. This prevents cross-epic contamination before any modifications.
2. **Bump Version** - **MANDATORY STEP-BY-STEP PROCESS (DO NOT SKIP ANY STEP):**

   **A. READ CURRENT VERSION:**
   - **Load config first:** If `rw-config.yaml` exists, read `version_file` from config. Otherwise, use `src/{project}/version.py` as fallback.
   - Read the version file (from config or fallback) to get current `VERSION_EPIC`, `VERSION_STORY`, `VERSION_TASK`, `VERSION_BUILD`
   - Document current version: `RC.EPIC.STORY.TASK+BUILD`
   - [Example: vibe-dev-kit] Read `src/fynd_deals/version.py` (or from `rw-config.yaml` if present)

   **B. IDENTIFY COMPLETED TASK (MANDATORY):**
   - **Load config first:** If `rw-config.yaml` exists and `use_kanban: true`, read `kanban_root` and `story_doc_pattern` from config. Otherwise, use `{kanban_path}/epics/Epic-{epic}/stories/Story-{story}-*.md` as fallback.
   - Read the Story file using config values or fallback pattern
   - [Example: vibe-dev-kit] `KB/PM_and_Portfolio/kanban/epics/Epic-{epic}/stories/Story-{story}-*.md` (or from `rw-config.yaml` if present)
   - Find the MOST RECENTLY COMPLETED task in the Task Checklist (marked `✅ COMPLETE`)
   - Extract the task number from the task identifier: `E{epic}:S{story}:T{task}` (e.g., `E2:S02:T008` → task number is `8`)
   - **CRITICAL:** If no task is marked complete, or you cannot identify which task was just completed, **STOP** and ask the user which task was completed

   **C. DETERMINE VERSION BUMP (MANDATORY LOGIC):**
   - Compare completed task number to current `VERSION_TASK`:
     - **IF completed task number > current VERSION_TASK:** This is a NEW TASK
       - Set `VERSION_TASK` = completed task number
       - Set `VERSION_BUILD` = 1 (reset to 1 for new task)
       - Example: Current `0.2.2.3+5`, completed T008 → New version: `0.2.2.8+1`
     - **IF completed task number == current VERSION_TASK:** This is SAME TASK, new build
       - Keep `VERSION_TASK` unchanged
       - Increment `VERSION_BUILD` by 1
       - Example: Current `0.2.2.3+1`, completed T003 → New version: `0.2.2.3+2`
     - **IF completed task number < current VERSION_TASK:** This is an ERROR
       - **STOP** and report error: "Completed task number ({completed}) is less than current VERSION_TASK ({current}). This indicates a versioning error. Please verify which task was actually completed."

   **D. VALIDATE BEFORE UPDATING:**
   - Verify: New `VERSION_TASK` matches completed task number
   - Verify: If new task, `VERSION_BUILD` = 1; if same task, `VERSION_BUILD` = current + 1
   - Document decision: "Task {completed_task} completed. Current TASK={current_task}, BUILD={current_build}. Decision: {new_task/new_build} → TASK={new_task}, BUILD={new_build}"

   **E. UPDATE VERSION FILE:**
   - **Use config path:** Update `VERSION_TASK` and `VERSION_BUILD` in the version file path from config (or `src/{project}/version.py` as fallback)
   - Update `VERSION_STRING` to reflect new version
   - Update `VERSION_INFO["description"]` if present
   - [Example: vibe-dev-kit] Update `src/fynd_deals/version.py` (or from `rw-config.yaml` if present)

   **F. VALIDATE AFTER UPDATING:**
   - Re-read `version.py` and verify the new version matches your decision
   - Confirm: `VERSION_TASK` = completed task number
   - Confirm: `VERSION_BUILD` = 1 (if new task) or current+1 (if same task)

   **Use format:** `RC.EPIC.STORY.TASK+BUILD`

   **🚨 CRITICAL: Step 2 Version Bump Requirements:**
   - **MUST** read Story file to identify completed task number
   - **MUST** compare completed task number to current VERSION_TASK
   - **MUST** validate TASK number matches completed task before updating
   - **MUST** validate TASK number matches completed task after updating
   - **MUST** document decision: "Task {N} completed. Current TASK={X}, BUILD={Y}. Decision: {new_task/new_build} → TASK={Z}, BUILD={W}"
   - See `KB/Architecture/Standards_and_ADRs/versioning-error-reference-guide.md` for error prevention reference
   - See `packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md` Step 2 for complete procedure
3. **Create Detailed Changelog** - Create detailed changelog in changelog archive directory. **Use config:** If `rw-config.yaml` exists, read `changelog_dir` from config. Otherwise, use `{changelog_archive_path}/CHANGELOG_v{version}.md` as fallback. Full timestamp (`YYYY-MM-DD HH:MM:SS UTC`). **CRITICAL:** Timestamp is IMMUTABLE once written - never edit the `**Release Date:**` field.
   - [Example: vibe-dev-kit] `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v{version}.md` (or from `rw-config.yaml` if present)
4. **Update Main Changelog** - Add new entry at top: `## [version] - DD-MM-YY` (short date format for merge-to-main) with release description and link to detailed changelog. **Use config:** If `rw-config.yaml` exists, read `main_changelog` from config. Otherwise, use `CHANGELOG.md` as fallback. Follow [Keep a Changelog](https://github.com/olivierlacan/keep-a-changelog) format. **Note:** Main changelog date can be updated if merge date changes, but detailed changelog timestamp is immutable.
5. **Update README** - Update version badge and latest release callout if present (optional). **Use config:** If `rw-config.yaml` exists, read `readme_file` from config. Otherwise, use `README.md` as fallback.
6. **Auto-update Kanban Docs** - Update epic documentation and story documentation with version markers. **Use config:** If `rw-config.yaml` exists and `use_kanban: true`, read `kanban_root`, `epic_doc_pattern`, and `story_doc_pattern` from config. Otherwise, use `{kanban_path}/epics/Epic-{epic}.md` and `{kanban_path}/epics/Epic-{epic}/stories/Story-{story}-*.md` as fallback. **CRITICAL: "ALL" means ALL sections:**
   - Header metadata (Last updated, Version)
   - Story Checklist at top (status, task counts, version)
   - **Detailed Story sections** (Status, Last updated, task checkboxes with forensic markers)
   - Any other references to the story/task being released
   - **Systematic Process:**
     1. Read the FULL Epic-{epic}.md file
     2. Read the authoritative Story-{story}-{name}.md file to get correct state
     3. Find ALL sections referencing the story/task (grep/search the file)
     4. Update ALL of them to match the Story file's state
     5. Validate consistency: header, checklist, and detailed sections must all match
7. **Stage Files** - Run `git add -A` to stage all modified files
8. **Run Validators** - Execute validation scripts. **Use config:** If `rw-config.yaml` exists, read `scripts_path` from config. Otherwise, use `{scripts_path}/validation/` as fallback. Run `validate_branch_context.py` and `validate_changelog_format.py` (both scripts automatically read from `rw-config.yaml` if available).
   - **IMPORTANT:** Validators should confirm you're on an epic branch, not `main`
   - If on `main`, warn user and suggest switching to epic branch
   - Validators check version format, branch context alignment, and changelog format
9. **Commit Changes** - Create commit with message: `Release v{version}: {summary}\n\nEpic: {epic} | Story: {story} | Task: {task}`
10. **Create Git Tag** - Create annotated tag: `v{version}` with message: `Release v{version}: {summary}\n\nEpic: {epic} | Story: {story} | Task: {task}`
11. **Push to Remote** - Push epic branch and tag to origin (DO NOT push to main unless ready to deploy)
    - **CRITICAL: Use `required_permissions: ['network']` for git push commands**
    - Example: `run_terminal_cmd(command="git push origin {branch} --tags", required_permissions=['network'])`
    - This enables network access in Cursor's sandbox environment
    - See: `KB/Architecture/Standards_and_ADRs/agent-network-access-and-git-push-limitations.md`

**Key Principles:**
- ✅ **Intelligent Analysis:** Understand each step's requirements before executing
- ✅ **Context-Aware:** Use branch context, version schema, and project state to make decisions
- ✅ **Validation:** Verify each step succeeded before proceeding
- ✅ **Documentation:** Document decisions and actions at each step
- ✅ **Progress Tracking:** MUST use Cursor TODOs to track all 11 steps
- ✅ **Branch Safety First:** Step 1 validates branch alignment before any modifications
- ✅ **Canonical Ordering:** Version numbers (not timestamps) determine changelog ordering - versions are the canonical ordering metric
- ✅ **Forensic Traceability:** Maintain complete traceability grid (version ↔ epic/story/task ↔ changelogs ↔ kanban ↔ git)
- ✅ **Immutability:** Detailed changelog timestamps are immutable once written - never edit `**Release Date:**` field
- ✅ **Mandatory Task Identification:** Step 2 MUST read Story file to identify completed task number
- ✅ **Version Validation:** Step 2 MUST validate TASK number matches completed task before and after updating
- ❌ **Never Blind Execution:** Don't just run scripts without understanding what they do
- ❌ **Never Leave RW Ambiguous:** Always end in either **RW COMPLETE** or **RW ABORTED (with reason)** state
- ❌ **Never Skip Task Identification:** Always read Story file to find completed task number
- ❌ **Never Assume Same Task:** Always compare completed task number to current VERSION_TASK

**File Paths (Customize for Your Project):**
- Version file: `src/{project}/version.py` (e.g., `src/myproject/version.py`)
  - [Example: vibe-dev-kit] `src/fynd_deals/version.py` (legacy path, acceptable for now)
- Changelog: `CHANGELOG.md`
- Changelog Archive: `{changelog_archive_path}/CHANGELOG_v{version}.md`
  - [Example: vibe-dev-kit] `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v{version}.md`
- Kanban Board: `{kanban_path}/kanban-board.md` or `{kanban_path}/_index.md` (customize path)
  - [Example: vibe-dev-kit] `KB/PM_and_Portfolio/kanban/_index.md` or `KB/PM_and_Portfolio/kanban/kanban-board.md`
- Epic Docs: `{kanban_path}/epics/Epic-{epic}.md` (customize path)
  - [Example: vibe-dev-kit] `KB/PM_and_Portfolio/kanban/epics/Epic-{epic}.md`
- Story Docs: `{kanban_path}/epics/Epic-{epic}/stories/Story-{story}-*.md` (customize path)
  - [Example: vibe-dev-kit] `KB/PM_and_Portfolio/kanban/epics/Epic-{epic}/stories/Story-{story}-*.md`
- Validators: `{scripts_path}/validation/validate_branch_context.py`, `{scripts_path}/validation/validate_changelog_format.py`
  - [Example: vibe-dev-kit] `packages/frameworks/workflow mgt/scripts/validation/validate_branch_context.py`, `packages/frameworks/workflow mgt/scripts/validation/validate_changelog_format.py`

**Version Schema:**
- Format: `RC.EPIC.STORY.TASK+BUILD` (e.g., `0.{epic}.{story}.{task}+{build}`)
- **Schema Calculation:** Epic N, Story S, Task T → Version: `0.N.S.T+1` (first build)
- **Build Increment:** Same Epic/Story/Task → Increment BUILD (e.g., `0.N.S.T+1` → `0.N.S.T+2`)
- **New Task:** Different Task → Reset BUILD to 1 (e.g., `0.N.S.T+5` → `0.N.S.{T+1}+1`)
- **New Story:** Different Story → Reset TASK to 1, BUILD to 1 (e.g., `0.N.S.T+B` → `0.N.{S+1}.1+1`)
- **New Epic:** Different Epic → Reset STORY to 1, TASK to 1, BUILD to 1 (e.g., `0.N.S.T+B` → `0.{N+1}.1.1+1`)
- **Epic Alignment:** Epic number should match current branch (if on `epic/{n}`, version should be `0.{n}.S.T+B`)
- **Epic Ranges:**
  - [Example: vibe-dev-kit] Epic 1-4+ (Epic 1: Vibe Dev Kit Core, Epic 2: Workflow Management Framework, Epic 3: Numbering & Versioning Framework, Epic 4: Kanban Framework)
  - No legacy range in dev-kit - starts from Epic 1 with full schema
- **Reference:** See `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md` (or your project's versioning policy) for complete schema definition

**Branch Mapping (Customize for Your Project):**
- `main` - **PRODUCTION BRANCH** - Only merge when ready to deploy. Auto-deploys trigger on every push!
- `epic/{n}` - **DEVELOPMENT BRANCH** - All epic work should be done here. Should have version `0.{n}.S.T+B`
- Other branches - Validate against known patterns

**🚨 CRITICAL: Epic Branch Workflow**
- **ALWAYS work on epic branches** (`epic/{n}-{description}`, e.g., `epic/1-core`, `epic/3-versioning`, etc.)
- **NEVER commit directly to `main`** during epic development
- **ONLY merge to `main`** when ready to deploy (triggers auto-deployment)
- **Release Workflow (RW)** should be run on epic branch, then merge to main
- This prevents unnecessary deployments during development

**Version Calculation Examples:**
- Working on Epic 1, Story 1, Task 1: `0.1.1.1+1` (first build) → `0.1.1.1+2` (second build)
  - [Example: vibe-dev-kit] Epic 1 (Vibe Dev Kit Core), Story 1, Task 1: `0.1.1.1+1` → `0.1.1.1+2`
- Moving to Task 2 in same Story: `0.1.1.2+1` (new task, BUILD resets to 1)
  - [Example: vibe-dev-kit] Epic 2 (Workflow Management Framework), Story 1, Task 2: `0.2.1.2+1`
- Moving to Story 2 in same Epic: `0.1.2.1+1` (new story, TASK and BUILD reset)
  - [Example: vibe-dev-kit] Epic 3 (Numbering & Versioning Framework), Story 2: `0.3.2.1+1`
- Moving to Epic 2: `0.2.1.1+1` (new epic, STORY, TASK, and BUILD reset)
  - [Example: vibe-dev-kit] Epic 4 (Kanban Framework), Story 1, Task 1: `0.4.1.1+1`

**Reference Documentation:**
- Versioning Policy: `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md` (or your project's equivalent)
  - [Example: vibe-dev-kit] `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md` (canonical SoT for dev-kit)
- Versioning Strategy: `packages/frameworks/numbering & versioning/versioning-strategy.md` (framework reference)
- Release Workflow Guide: `packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md`
- Kanban Governance: `KB/PM_and_Portfolio/rituals/policy/kanban-governance-policy.md` (or your project's equivalent)
  - [Example: vibe-dev-kit] `KB/PM_and_Portfolio/rituals/policy/kanban-governance-policy.md` (references framework as SoT)

---

**⚠️ IMPORTANT: Customization Required**

After copying this section to your `.cursorrules`, you MUST:
1. **Update all file paths** to match your project structure
2. **Update version file location** (currently shows `src/{project}/version.py` as template)
   - [Example: vibe-dev-kit] `src/fynd_deals/version.py` (legacy path, acceptable for now)
3. **Update Kanban paths** (currently shows `{kanban_path}/...` as templates)
   - [Example: vibe-dev-kit] `KB/PM_and_Portfolio/kanban/epics/Epic-{epic}.md`
4. **Update validator script paths** (currently shows `{scripts_path}/...` as templates)
   - [Example: vibe-dev-kit] `packages/frameworks/workflow mgt/scripts/validation/...`
5. **Reference your project's versioning policy** instead of dev-kit policy
   - [Example: vibe-dev-kit] Uses `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md` as canonical SoT
6. **Customize branch naming** if your project uses different conventions (e.g., `feature/epic-{n}` instead of `epic/{n}`)
7. **Customize epic ranges** if your project uses different epic numbering (e.g., legacy range 1-9, new range 10+)
   - [Example: vibe-dev-kit] Epic 1-4+ (no legacy range, starts from Epic 1 with full schema)

**For vibe-dev-kit Usage:**
When using this section in the vibe-dev-kit repository itself:
- Version file: `src/fynd_deals/version.py`
- Changelog Archive: `KB/Changelog_and_Release_Notes/Changelog_Archive/`
- Kanban: `KB/PM_and_Portfolio/kanban/`
- Validators: `packages/frameworks/workflow mgt/scripts/validation/`
- Versioning Policy: `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md` (canonical SoT)
