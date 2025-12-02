# Cursor Rules: RW Trigger Section

**Purpose:** This section should be added to your project's `.cursorrules` file to enable the "RW" trigger for Release Workflow execution.

**Location in `.cursorrules`:** Add this section in the "Version Control and Release Process" section (or equivalent).

**Last Updated:** 2025-12-02  
**Source Project:** fynd.deals (Epic 15, Story 1)  
**Version:** 2.0.0 (includes "ALL sections" requirement, atomicity, blocked protocol)

---

### 🚀 RELEASE WORKFLOW (RW) TRIGGER

**When the user types "RW" or "rw" (case-insensitive), execute the Release Workflow as an intelligent agent:**

1. **DO NOT** run the deterministic script `scripts/release_workflow.py`
2. **DO** execute the Release Workflow using the **intelligent agent-driven execution pattern**
3. **Follow** the step-by-step guide below
4. **Execute all 10 steps** using the ANALYZE → DETERMINE → EXECUTE → VALIDATE → PROCEED pattern
5. **Document** each step's analysis, actions, and results
6. **MUST USE Cursor TODOs:** Create and maintain a TODO list tracking all 10 steps (see below)

**🚨 MANDATORY: Progress Tracking with Cursor TODOs**

**REQUIRED:** Agents **MUST** use `todo_write` to create and maintain a TODO list for all 10 Release Workflow steps:

1. **At Workflow Start:** Create TODO list with all 10 steps as `pending`
   ```python
   todo_write(merge=False, todos=[
       {'id': 'rw-step-1', 'status': 'pending', 'content': 'Step 1: Bump Version - Analyze current version and determine next version'},
       {'id': 'rw-step-2', 'status': 'pending', 'content': 'Step 2: Update CHANGELOG - Add new release entry'},
       {'id': 'rw-step-3', 'status': 'pending', 'content': 'Step 3: Update Kanban Board - Add release note'},
       {'id': 'rw-step-4', 'status': 'pending', 'content': 'Step 4: Update KB Epic Docs - Update epic documentation with version'},
       {'id': 'rw-step-5', 'status': 'pending', 'content': 'Step 5: Update README - Update version references if present'},
       {'id': 'rw-step-6', 'status': 'pending', 'content': 'Step 6: Stage Files - Stage all modified files'},
       {'id': 'rw-step-7', 'status': 'pending', 'content': 'Step 7: Run Validators - Execute branch context and changelog format validators'},
       {'id': 'rw-step-8', 'status': 'pending', 'content': 'Step 8: Commit Changes - Create git commit with versioned message'},
       {'id': 'rw-step-9', 'status': 'pending', 'content': 'Step 9: Create Git Tag - Create annotated tag'},
       {'id': 'rw-step-10', 'status': 'pending', 'content': 'Step 10: Push to Remote - Push branch and tags'},
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
     - Run **all 10 steps (1–10)** to completion for the target version, OR
     - Stop at a **specific step** and clearly state:
       - The **step number and name** (e.g. "Step 7: Run Validators")
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

**The 10 Steps:**

1. **Bump Version** - Read `src/fynd_deals/version.py`, determine next version (increment BUILD for same task, or set new TASK+BUILD=1), update file. Use new format: `RC.EPIC.STORY.TASK+BUILD`
2. **Update CHANGELOG** - Add new entry at top: `## [version] - DD-MM-YY` (new format) or `## [version] - YYYY-MM-DD` (old format) with release description. For new format, also create detailed changelog in `CHANGELOG_ARCHIVE/CHANGELOG_v{version}.md` with full timestamp.
3. **Update Kanban Board** - Add release note to `knowledge/fynd_deals/Kanban/Kanban Board.md`
4. **Update KB Epic Docs** - Update epic documentation at `knowledge/fynd_deals/Kanban/Epic-{epic}/Epic-{epic}.md` with version marker. **CRITICAL: "ALL" means ALL sections:**
   - Header metadata (Last updated, Version)
   - Story Checklist at top (status, task counts, version)
   - **Detailed Story sections** (Status, Last updated, task checkboxes with forensic markers)
   - Any other references to the story/task being released
   - **Systematic Process:**
     1. Read the FULL Epic-{epic}.md file
     2. Read the authoritative Story-{N}-{Name}.md file to get correct state
     3. Find ALL sections referencing the story/task (grep/search the file)
     4. Update ALL of them to match the Story file's state
     5. Validate consistency: header, checklist, and detailed sections must all match
5. **Update README** - Update version references if present (optional)
6. **Stage Files** - Run `git add -A` to stage all modified files
7. **Run Validators** - Execute `scripts/validation/validate_branch_context.py --strict` and `scripts/validation/validate_changelog_format.py --strict`
   - **IMPORTANT:** Validators should confirm you're on an epic branch, not `main`
   - If on `main`, warn user and suggest switching to epic branch
8. **Commit Changes** - Create commit with message: `Release {version}`
9. **Create Git Tag** - Create annotated tag: `v{version}` with message: `Release {version}`
10. **Push to Remote** - Push epic branch and tag to origin (DO NOT push to main unless ready to deploy)

**Key Principles:**
- ✅ **Intelligent Analysis:** Understand each step's requirements before executing
- ✅ **Context-Aware:** Use branch context, version schema, and project state to make decisions
- ✅ **Validation:** Verify each step succeeded before proceeding
- ✅ **Documentation:** Document decisions and actions at each step
- ✅ **Progress Tracking:** MUST use Cursor TODOs to track all 10 steps
- ❌ **Never Blind Execution:** Don't just run scripts without understanding what they do
- ❌ **Never Leave RW Ambiguous:** Always end in either **RW COMPLETE** or **RW ABORTED (with reason)** state

**File Paths:**
- Version file: `src/fynd_deals/version.py`
- Changelog: `CHANGELOG.md`
- Kanban Board: `knowledge/fynd_deals/Kanban/Kanban Board.md`
- Epic Docs: `knowledge/fynd_deals/Kanban/Epic-{epic}/Epic-{epic}.md`
- Validators: `scripts/validation/validate_branch_context.py`, `scripts/validation/validate_changelog_format.py`

**Version Schema:**
- Format: `RC.EPIC.STORY.TASK+BUILD` (e.g., `0.15.1.4+2`)
- Default increment: BUILD (for same task) or TASK+BUILD=1 (for new task)
- Epic number should match current branch (if on `epic/15`, version should be `0.15.x.x.x+x`)

**Branch Mapping:**
- `main` - **PRODUCTION BRANCH** - Only merge when ready to deploy. Auto-deploys trigger on every push!
- `epic/{n}` - **DEVELOPMENT BRANCH** - All epic work should be done here. Should have version `0.{n}.x.x+x`
- Other branches - Validate against known patterns

**🚨 CRITICAL: Epic Branch Workflow**
- **ALWAYS work on epic branches** (`epic/10-fastapi-migration`, `epic/15-documentation`, etc.)
- **NEVER commit directly to `main`** during epic development
- **ONLY merge to `main`** when ready to deploy (triggers auto-deployment)
- **Release Workflow (RW)** should be run on epic branch, then merge to main
- This prevents unnecessary deployments during development

---

**Note:** After copying this section to your `.cursorrules`, update all file path references to match your project structure.
