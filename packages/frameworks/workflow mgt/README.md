# Release Workflow (RW) Implementation Package

**Version:** 2.0.0  
**Last Updated:** 2025-12-02  
**Purpose:** Complete package for implementing the Release Workflow (RW) trigger and agent-driven workflow execution pattern in your project  
**Source Project:** fynd.deals (Epic 15, Story 1)  
**Key Enhancements:** "ALL sections" requirement, atomicity, blocked protocol, epic branch workflow

---

## 📋 What's Included

This package contains all essential files needed to implement the Release Workflow (RW) trigger in your project. The RW trigger enables AI assistants to execute a complete 13-step release process (version bump, changelog generation, Git operations, PDCA verification and action) using intelligent agent-driven execution.

### Core Methodology Documents
- `KB/Documentation/Developer_Docs/vwmp/agent-driven-workflow-execution.md` - General methodology for agent-driven workflow execution
- `KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md` - Step-by-step guide for executing the 13-step Release Workflow
- `KB/Documentation/Developer_Docs/vwmp/release-workflow-reference.md` - Complete workflow reference
- `KB/Documentation/Developer_Docs/vwmp/portable-workflow-implementation-guide.md` - Detailed implementation guide

### Versioning Policy Documents
- `KB/Architecture/Standards_and_ADRs/versioning-policy.md` - Version schema definition (RC.EPIC.STORY.TASK+BUILD)
- `KB/Architecture/Standards_and_ADRs/versioning-strategy.md` - Complete versioning strategy with forensic traceability

### Workflow Definition
- `workflows/release-workflow.yaml` - YAML definition of the Release Workflow structure

### Validation Scripts
- `scripts/validation/validate_branch_context.py` - Validates branch/version/epic alignment (supports multi-digit epics)
- `scripts/validation/validate_changelog_format.py` - Validates changelog format (supports both old and new format)

### Cursor Rules Section
- `cursorrules-rw-trigger-section.md` - Section to add to your `.cursorrules` file (includes "ALL sections" requirement, atomicity, blocked protocol)

---

## 🧩 Modularity & Dependencies

This package is designed to be **fully modular** with maximum flexibility. You can use it standalone or combine it with other packages based on your needs.

### Standalone Usage

✅ **This package can be used completely independently** without requiring any other `vibe-dev-kit` packages.

**What you get standalone:**
- Complete Release Workflow (RW) trigger and execution methodology
- Agent-driven workflow execution patterns
- Workflow validation scripts
- Cursor rules integration
- Versioning policy documents (included for RW to work)

**Hard dependencies (required):**
- Git (for version control)
- Python 3 (for validation scripts)
- AI Assistant (for agent-driven execution)

**Independence score:** 9/10 — Can be used standalone with minimal external dependencies.

### Combined Usage

**With Numbering & Versioning Package:**
- RW uses the version schema from Numbering & Versioning
- Optional: Can swap in your own versioning policy if preferred
- Integration: RW reads version file and follows versioning schema

**With Kanban Package:**
- RW automatically updates Kanban documentation (Step 4)
- Integration: RW adds forensic markers to Kanban Story Checklist
- Optional: Can use RW without Kanban (skip Step 4)

**With Both Packages:**
- Complete three-way integration (Kanban ↔ Versioning ↔ RW)
- Automated Kanban updates with version markers
- Full forensic traceability

### Dependency Matrix

| Dependency Type | Package | Required? | Purpose |
|----------------|---------|-----------|---------|
| Hard | Git | ✅ Yes | Version control operations |
| Hard | Python 3 | ✅ Yes | Validation scripts |
| Hard | AI Assistant | ✅ Yes | Agent-driven execution |
| Soft | Numbering & Versioning | ❌ No | Version schema (can swap) |
| Soft | Kanban | ❌ No | Documentation updates (optional) |

### Copy vs Reference Pattern

**⚠️ CRITICAL: Copy, Don't Reference**

Projects must **copy** this package into their repository, not link to it.

**Why copy?**
- Projects need to customize file paths, project names, and terminology
- Projects evolve independently and may need project-specific adaptations
- Copying ensures projects have full control over their workflow implementation
- Prevents breaking changes in `vibe-dev-kit` from affecting consuming projects

**What to copy:**
1. All files in `packages/frameworks/workflow mgt/`
2. Maintain directory structure
3. Customize all file paths in documentation
4. Update `.cursorrules` section with your project paths

**Customization boundaries:**
- ✅ **CAN customize:** File paths, project names, branch naming conventions, version file location
- ❌ **MUST keep:** Workflow steps (1-13), validation logic, agent execution pattern, atomicity requirements, PDCA integration

### Usage Scenarios

**Scenario 1: Standalone Workflow Management**
- Copy only this package
- Use RW for automated releases
- Swap in your own versioning policy if needed
- Skip Kanban integration (manual updates)

**Scenario 2: Workflow + Versioning**
- Copy this package and Numbering & Versioning package
- RW uses versioning schema automatically
- Full versioning integration

**Scenario 3: Complete Integration**
- Copy all three packages (Workflow, Versioning, Kanban)
- Full three-way integration
- Automated Kanban updates with version markers

See `KB/PM_and_Portfolio/kanban/epics/Epic-1/stories/Story-002-package-and-repo-architecture/T004-consumption-patterns.md` for detailed step-by-step guides for each scenario.

---

## 🚀 Quick Start

### Step 1: Copy Files to Your Project

Copy all files maintaining the directory structure:

```bash
# Copy to your project root
cp -r temp/workflow\ mgt/* /path/to/your/project/
```

Or manually copy:
- `KB/` → Your documentation directory
- `workflows/` → Your workflows directory (or create it)
- `scripts/validation/` → Your scripts directory (or create it)

### Step 2: Customize File Paths

**Critical:** You must update file paths in all documents to match your project structure.

**Search and Replace:**
1. **Version File:**
   - Search: `src/fynd_deals/version.py`
   - Replace: `src/yourproject/version.py` (or your actual path)

2. **Changelog Directory:**
   - Search: `CHANGELOG_ARCHIVE/`
   - Replace: Your changelog archive directory path

3. **Main Changelog:**
   - Search: `CHANGELOG.md`
   - Replace: Your main changelog file path

4. **Kanban Documentation:**
   - Search: `knowledge/fynd_deals/Kanban/`
   - Replace: Your Kanban doc structure (if using Kanban)

5. **Documentation References:**
   - Update all `KB/Documentation/Developer_Docs/vwmp/` references to match your doc structure

**Files to Update:**
- All `.md` files in `KB/Documentation/Developer_Docs/vwmp/`
- `workflows/release-workflow.yaml`
- `scripts/validation/validate_branch_context.py`
- `scripts/validation/validate_changelog_format.py`
- `cursorrules-rw-trigger-section.md` (before adding to `.cursorrules`)

### Step 3: Add RW Trigger to `.cursorrules`

1. Open `cursorrules-rw-trigger-section.md`
2. Copy the entire section (from `### 🚀 RELEASE WORKFLOW (RW) TRIGGER` to the end)
3. Paste into your `.cursorrules` file in an appropriate location (e.g., "Version Control and Release Process" section)
4. Update all file path references in the section to match your project

### Step 4: Customize Version Schema (if needed)

The default schema is `RC.EPIC.STORY.TASK+BUILD` (e.g., `0.15.1.4+2`). If you need a different schema:

1. Update `KB/Architecture/Standards_and_ADRs/versioning-policy.md` with your schema
2. Update `scripts/validation/validate_branch_context.py` to parse your schema
3. Update `KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md` Step 1 to handle your schema
4. Update the version schema section in your `.cursorrules`

### Step 5: Customize Branch Mapping (if needed)

If using different branch naming conventions:

1. Update `scripts/validation/validate_branch_context.py` to parse your branch pattern (currently uses regex `epic/(\d+)`)
2. Update branch mapping section in your `.cursorrules`
3. Update any documentation that references branch patterns

**Current Implementation:**
- Supports multi-digit epic numbers (e.g., `epic/10-fastapi-migration`, `epic/15-documentation`)
- Uses regex pattern `epic/(\d+)` to extract epic number from branch name
- Validates that version epic matches branch epic

### Step 6: Test the Workflow

1. Ensure you have a version file (e.g., `src/yourproject/version.py` with `VERSION_STRING = "0.1.1.1+1"`)
2. Create an epic branch (e.g., `git checkout -b epic/1-first-epic`)
3. Type "RW" in your AI assistant (Cursor)
4. Verify all 13 steps execute correctly:
   - Step 1: Branch Safety Check
   - Step 2: Version bumped
   - Step 3: CHANGELOG + archive updated
   - Step 4: Main CHANGELOG updated
   - Step 5: README updated (if applicable)
   - Step 6: Kanban docs auto-updated
   - Step 7: Files staged
   - Step 8: Validators run
   - Step 9: Commit created
   - Step 10: Tag created
   - Step 11: Branch and tag pushed (or manual instructions provided)
   - Step 12: Post-Commit Verification & Reflection (optional but recommended)
   - Step 13: Act on Verification Results (optional but recommended)

---

## 📖 How It Works

### The RW Trigger

When a user types "RW" or "rw" (case-insensitive) in their AI assistant:

1. **AI Assistant Recognizes Trigger:** The `.cursorrules` file instructs the AI to execute the Release Workflow
2. **Intelligent Execution:** The AI follows the step-by-step guide, analyzing each step before executing
3. **Progress Tracking:** The AI creates and maintains a TODO list tracking all 13 steps
4. **Validation:** Each step is validated before proceeding to the next
5. **Documentation:** All actions are documented with analysis and results
6. **Atomicity:** The workflow either completes all 13 steps or stops with a clear "RW BLOCKED" message

### The 13 Steps

**Phase 1: Version & Documentation Updates (Steps 1-6)**
1. **Branch Safety Check** - Verify work aligns with branch context
2. **Bump Version** - Increment version number based on schema (BUILD for same task, or TASK+BUILD=1 for new task)
3. **Create Detailed Changelog** - Create detailed changelog archive with full timestamp and PLAN section
4. **Update Main Changelog** - Add summary entry with short date (DD-MM-YY)
5. **Update README** - Update version references if present (optional)
6. **Auto-update Kanban Docs** - Update **ALL sections** (header, checklist, detailed story sections) to match authoritative Story file

**Phase 2: Git Operations & Validation (Steps 7-11)**
7. **Stage Files** - Stage all modified files
8. **Run Validators** - Execute branch context and changelog format validators (must be on epic branch, not main)
9. **Commit Changes** - Create git commit with versioned message
10. **Create Git Tag** - Create annotated tag
11. **Push to Remote** - Push epic branch and tags to remote repository (DO NOT push to main unless ready to deploy)

**Phase 3: PDCA CHECK & ACT (Steps 12-13, optional but recommended)**
12. **Post-Commit Verification & Reflection** - Verify changes worked as expected, evaluate against objectives, reflect on results
13. **Act on Verification Results** - Update changelog based on verification, standardize practices, create follow-up tasks if needed

### Agent-Driven Execution

Unlike deterministic scripts, the AI agent:
- **Analyzes** each step's requirements before executing
- **Determines** appropriate actions based on context
- **Executes** the actions intelligently
- **Validates** results before proceeding
- **Documents** all decisions and actions

This ensures the workflow adapts to your project's specific context and handles edge cases intelligently.

### Key Enhancements (v2.0.0)

**"ALL Sections" Requirement:**
- Step 4 now explicitly requires updating ALL sections of epic documentation:
  - Header metadata
  - Story Checklist
  - Detailed Story sections
  - Any other references
- Includes systematic process: read full file → find all references → update all → validate consistency

**Atomicity & Blocked Protocol:**
- RW must complete all 10 steps OR stop with clear "RW BLOCKED" message
- Cannot silently stop mid-workflow
- Cannot start new RW while previous RW TODOs are pending/in_progress
- If aborted, must mark remaining TODOs as cancelled and output "RW ABORTED" summary

**Epic Branch Workflow:**
- ALWAYS work on epic branches (`epic/{n}-...`)
- NEVER commit directly to `main` during development
- ONLY merge to `main` when ready to deploy
- Prevents unnecessary auto-deployments during development

---

## 🔧 Customization Guide

### File Paths

**Most Important:** Update these paths in ALL files:
- Version file location
- Changelog directory
- Main changelog file
- Kanban documentation paths (if using)
- Documentation directory structure

**Quick Find/Replace:**
```bash
# Find all occurrences (customize these paths for your project)
grep -r "src/{project}/version.py" .  # Replace {project} with your project name
grep -r "{changelog_archive_path}" .  # Replace with your changelog archive path
grep -r "{kanban_path}" .              # Replace with your Kanban documentation path
grep -r "{scripts_path}" .            # Replace with your scripts directory path
```

**Note:** The `cursorrules-rw-trigger-section.md` file has been abstracted to use template placeholders (`{project}`, `{changelog_archive_path}`, etc.) instead of hardcoded paths. Update these placeholders when copying to your project.

### Version Schema

The default schema `RC.EPIC.STORY.TASK+BUILD` is designed to be universal, but you can customize:

**Example:** `0.{epic}.{story}.{task}+{build}` (e.g., `0.3.1.5+1`)
- `0` = Release Candidate (0 = development, 1+ = release candidate)
- `{epic}` = Epic number (e.g., 3)
- `{story}` = Story number within epic (e.g., 1)
- `{task}` = Task number within story (e.g., 5)
- `{build}` = Build number (increments per release within task, e.g., 1)

**Schema Calculation:**
- Epic N, Story S, Task T → Version: `0.N.S.T+1` (first build)
- Same Task: Increment BUILD → `0.N.S.T+{B+1}`
- New Task: Reset BUILD → `0.N.S.{T+1}+1`
- New Story: Reset TASK and BUILD → `0.N.{S+1}.1+1`
- New Epic: Reset STORY, TASK, BUILD → `0.{N+1}.1.1+1`

**To Customize:**
1. Update `versioning-policy.md` with your schema
2. Update validation scripts to parse your schema
3. Update workflow execution guide Step 1

### Branch Mapping

If using different branch naming (e.g., `feature/epic-{n}` instead of `epic/{n}`):

1. Update `validate_branch_context.py`:
   ```python
   def parse_branch_epic(branch: str) -> Optional[int]:
       # Match your pattern (e.g., feature/epic-4 -> 4)
       # Current default pattern: epic/{n} or epic/{n}-{description}
       match = re.match(r"^epic/(\d+)", branch)  # Default pattern
       # Or customize: match = re.match(r"^feature/epic-(\d+)", branch)
       if match:
           return int(match.group(1))
       return None
   ```

2. Update `.cursorrules` branch mapping section to reflect your naming convention
3. Update branch examples in documentation to use generic patterns

### Optional Steps

Steps 4 (Update README) and 5 (Update KB Epic Docs) can be adapted:
- If you don't have a README with version badge, skip Step 5
- If you don't use Kanban structure, skip Step 4 (but note: Step 4 is critical for Kanban-based projects)

---

## ✅ Verification Checklist

After implementation, verify:

- [ ] All file paths updated in all documents
- [ ] RW trigger section added to `.cursorrules`
- [ ] Version file exists and is accessible
- [ ] Changelog directory exists
- [ ] Validation scripts are executable
- [ ] RW trigger responds to "RW" or "rw" in AI assistant
- [ ] All 13 steps execute in correct order
- [ ] Version file updates correctly
- [ ] Changelogs created with full timestamps
- [ ] Epic docs updated in ALL sections (header, checklist, detailed story sections)
- [ ] Validators run and pass
- [ ] Git commit includes version number
- [ ] Git tag created with correct format
- [ ] Branch and tag pushed to remote (or manual instructions provided)
- [ ] TODO list tracks all 13 steps (visible in AI assistant)
- [ ] RW completes atomically or stops with clear "RW BLOCKED" message
- [ ] PDCA CHECK and ACT phases executed (Steps 12-13)

---

## 📚 Documentation Structure

The included documentation follows this structure:

```
KB/
├── Documentation/
│   └── Developer_Docs/
│       └── vwmp/
│           ├── agent-driven-workflow-execution.md
│           ├── release-workflow-agent-execution.md
│           ├── release-workflow-reference.md
│           └── portable-workflow-implementation-guide.md
└── Architecture/
    └── Standards_and_ADRs/
        ├── versioning-policy.md
        └── versioning-strategy.md
```

**You can adjust this structure** to match your project's documentation organization. Just update all cross-references in the files.

---

## 🆘 Troubleshooting

### RW Trigger Not Responding

1. **Check `.cursorrules`:** Ensure the RW trigger section is properly added
2. **Check File Paths:** Verify all file path references in `.cursorrules` are correct
3. **Check Documentation:** Ensure referenced documentation files exist at specified paths

### Validation Failures

1. **Branch Context:** Check that your branch name matches the version schema (e.g., `epic/15` for version `0.15.x.x.x+x`)
2. **Changelog Format:** Ensure changelog has correct format (new: `DD-MM-YY`, old: `YYYY-MM-DD`)
3. **Version Schema:** Verify version matches expected format (`RC.EPIC.STORY.TASK+BUILD`)

### Step Failures

1. **Check Dependencies:** Ensure previous steps completed successfully
2. **Check File Permissions:** Ensure files are writable
3. **Check Git State:** Ensure you're on a valid epic branch with no uncommitted conflicts

### "ALL Sections" Not Updated

1. **Check Step 4:** Ensure systematic process is followed:
   - Read FULL Epic-{epic}.md file
   - Read authoritative Story-{N}-{Name}.md file
   - Find ALL sections referencing story/task (use grep/search)
   - Update ALL of them
   - Validate consistency

---

## 🔗 Key Concepts

### Agent-Driven Execution

The workflow uses **intelligent agent-driven execution**, not deterministic scripts. This means:
- The AI analyzes each step before executing
- The AI makes context-aware decisions
- The AI validates results before proceeding
- The AI documents all actions

### Mandatory TODOs

**Cursor TODOs are MANDATORY** for the Release Workflow. The AI must:
- Create a TODO list with all 10 steps at workflow start
- Update TODO status before and after each step
- Mark all steps as completed on success
- Mark remaining steps as cancelled on abort

This provides:
- Real-time progress visibility
- Error recovery capability
- Execution transparency
- Accessibility support (critical for users with cognitive constraints)

### Version Schema

The `RC.EPIC.STORY.TASK+BUILD` schema provides:
- **Forensic Traceability:** Every version links to specific work items
- **Parallel Development:** Multiple epics can develop simultaneously
- **Task-Level Granularity:** Versions track work at the task level
- **Build Increments:** Multiple releases within a task are tracked

### Epic Branch Workflow

**Critical:** Always work on epic branches, never directly on `main`:
- Prevents unnecessary auto-deployments
- Maintains clean version streams per epic
- Enables parallel development
- Only merge to `main` when ready to deploy

---

## 📝 Next Steps

1. **Review Documentation:** Read through the included guides to understand the methodology
2. **Customize Paths:** Update all file paths to match your project
3. **Test Workflow:** Run a test release on a feature/epic branch
4. **Set Up Pre-commit Hooks:** Add validators to pre-commit hooks (optional but recommended)
5. **Train Your Team:** Share the documentation with your team

---

## 💡 Tips

1. **Start Small:** Test the workflow on a feature branch before using in production
2. **Version Schema:** The default schema is designed to be universal - only customize if necessary
3. **File Structure:** You don't need the exact `KB/` structure - adjust to match your project
4. **Validation:** The validators are the most project-specific - customize these carefully
5. **Documentation:** Keep documentation updated as you customize the workflow
6. **"ALL Sections":** Always follow the systematic process for Step 4 to prevent inconsistencies
7. **Atomicity:** Ensure RW always ends in "RW COMPLETE" or "RW BLOCKED" state - never ambiguous

---

## 📞 Support

For questions or issues:
1. Review `KB/Documentation/Developer_Docs/vwmp/portable-workflow-implementation-guide.md` for detailed customization instructions
2. Check the step-by-step execution guide for specific step issues
3. Review the versioning policy documents for schema questions
4. Check `.cursorrules` for the complete RW trigger section with all requirements

---

**Last Updated:** 2025-12-02  
**Package Version:** 2.0.0  
**Source Project:** fynd.deals (Epic 15, Story 1)  
**Key Features:** "ALL sections" requirement, atomicity, blocked protocol, epic branch workflow
