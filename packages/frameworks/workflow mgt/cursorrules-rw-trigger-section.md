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
3. **Follow** the step-by-step guide below
4. **Start with Step 1: Branch Safety Check** - Analyze work and ensure it aligns with current branch before proceeding
5. **Execute all 11 steps** using the ANALYZE → DETERMINE → EXECUTE → VALIDATE → PROCEED pattern
6. **Document** each step's analysis, actions, and results
7. **MUST USE Cursor TODOs:** Create and maintain a TODO list tracking all 11 steps (see below)

**🚨 MANDATORY: Progress Tracking with Cursor TODOs**

**REQUIRED:** Agents **MUST** use `todo_write` to create and maintain a TODO list for all 11 Release Workflow steps:

1. **At Workflow Start:** Create TODO list with all 11 steps as `pending`
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
2. **Bump Version** - Read version file (typically `src/{project}/version.py`), determine next version using schema calculation:
   - **Same Task:** Increment BUILD (e.g., `0.E.S.T+B` → `0.E.S.T+{B+1}`)
   - **New Task:** Set new TASK and BUILD=1 (e.g., `0.E.S.T+B` → `0.E.S.{T+1}+1`)
   - **New Story:** Set new STORY, TASK=1, BUILD=1 (e.g., `0.E.S.T+B` → `0.E.{S+1}.1+1`)
   - **New Epic:** Set new EPIC, STORY=1, TASK=1, BUILD=1 (e.g., `0.E.S.T+B` → `0.{E+1}.1.1+1`)
   - Use format: `RC.EPIC.STORY.TASK+BUILD`
3. **Create Detailed Changelog** - Create detailed changelog in changelog archive directory (typically `{changelog_archive_path}/CHANGELOG_v{version}.md`) with full timestamp (`YYYY-MM-DD HH:MM:SS UTC`)
4. **Update Main Changelog** - Add new entry at top: `## [version] - DD-MM-YY` (new format) with release description and link to detailed changelog. Follow [Keep a Changelog](https://github.com/olivierlacan/keep-a-changelog) format.
5. **Update README** - Update version badge and latest release callout if present (optional)
6. **Auto-update Kanban Docs** - Update epic documentation at `{kanban_path}/epics/Epic-{epic}.md` and story documentation at `{kanban_path}/epics/Epic-{epic}/stories/Story-{story}-*.md` with version markers. **CRITICAL: "ALL" means ALL sections:**
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
8. **Run Validators** - Execute validation scripts (typically `{scripts_path}/validation/validate_branch_context.py` and `{scripts_path}/validation/validate_changelog_format.py`)
   - **IMPORTANT:** Validators should confirm you're on an epic branch, not `main`
   - If on `main`, warn user and suggest switching to epic branch
   - Validators check version format, branch context alignment, and changelog format
9. **Commit Changes** - Create commit with message: `Release v{version}: {summary}\n\nEpic: {epic} | Story: {story} | Task: {task}`
10. **Create Git Tag** - Create annotated tag: `v{version}` with message: `Release v{version}: {summary}\n\nEpic: {epic} | Story: {story} | Task: {task}`
11. **Push to Remote** - Push epic branch and tag to origin (DO NOT push to main unless ready to deploy)

**Key Principles:**
- ✅ **Intelligent Analysis:** Understand each step's requirements before executing
- ✅ **Context-Aware:** Use branch context, version schema, and project state to make decisions
- ✅ **Validation:** Verify each step succeeded before proceeding
- ✅ **Documentation:** Document decisions and actions at each step
- ✅ **Progress Tracking:** MUST use Cursor TODOs to track all 11 steps
- ✅ **Branch Safety First:** Step 1 validates branch alignment before any modifications
- ❌ **Never Blind Execution:** Don't just run scripts without understanding what they do
- ❌ **Never Leave RW Ambiguous:** Always end in either **RW COMPLETE** or **RW ABORTED (with reason)** state

**File Paths (Customize for Your Project):**
- Version file: `src/{project}/version.py` (e.g., `src/myproject/version.py`)
- Changelog: `CHANGELOG.md`
- Changelog Archive: `{changelog_archive_path}/CHANGELOG_v{version}.md` (e.g., `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v{version}.md`)
- Kanban Board: `{kanban_path}/kanban-board.md` or `{kanban_path}/_index.md` (customize path)
- Epic Docs: `{kanban_path}/epics/Epic-{epic}.md` (customize path)
- Story Docs: `{kanban_path}/epics/Epic-{epic}/stories/Story-{story}-*.md` (customize path)
- Validators: `{scripts_path}/validation/validate_branch_context.py`, `{scripts_path}/validation/validate_changelog_format.py`

**Version Schema:**
- Format: `RC.EPIC.STORY.TASK+BUILD` (e.g., `0.{epic}.{story}.{task}+{build}`)
- **Schema Calculation:** Epic N, Story S, Task T → Version: `0.N.S.T+1` (first build)
- **Build Increment:** Same Epic/Story/Task → Increment BUILD (e.g., `0.N.S.T+1` → `0.N.S.T+2`)
- **New Task:** Different Task → Reset BUILD to 1 (e.g., `0.N.S.T+5` → `0.N.S.{T+1}+1`)
- **Epic Alignment:** Epic number should match current branch (if on `epic/{n}`, version should be `0.{n}.S.T+B`)
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
- Moving to Task 2 in same Story: `0.1.1.2+1` (new task, BUILD resets to 1)
- Moving to Story 2 in same Epic: `0.1.2.1+1` (new story, TASK and BUILD reset)
- Moving to Epic 2: `0.2.1.1+1` (new epic, STORY, TASK, and BUILD reset)

**Reference Documentation:**
- Versioning Policy: `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md` (or your project's equivalent)
- Versioning Strategy: `packages/frameworks/numbering & versioning/versioning-strategy.md` (framework reference)
- Release Workflow Guide: `packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md`

---

**⚠️ IMPORTANT: Customization Required**

After copying this section to your `.cursorrules`, you MUST:
1. **Update all file paths** to match your project structure
2. **Update version file location** (currently shows `src/{project}/version.py` as template)
3. **Update Kanban paths** (currently shows `{kanban_path}/...` as templates)
4. **Update validator script paths** (currently shows `{scripts_path}/...` as templates)
5. **Reference your project's versioning policy** instead of dev-kit policy
6. **Customize branch naming** if your project uses different conventions (e.g., `feature/epic-{n}` instead of `epic/{n}`)
