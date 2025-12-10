---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-04T12:01:36Z
expires_at: null
housekeeping_policy: keep
---

# Dev Kit Versioning Policy

**Status:** Active  
**Owner:** AI Dev Kit / Book Project Lead  
**Last Updated:** 2025-12-02  
**Related Work:** Epic 1 (AI Dev Kit Core)

---

## 1. Purpose

This policy defines how the **AI Dev Kit** repository uses the `RC.EPIC.STORY.TASK+BUILD` versioning schema.

Goals:

- Apply the **full versioning schema and strategy** from the Numbering & Versioning framework to this repo.
- Ensure all substantive work is **Task-driven** and that versions reflect **Tasks**.
- Keep `ai-dev-kit` logically separate from any external project (e.g., Confidentia, fynd.deals) while reusing the same principles.

---

## 2. Schema (Adopted)

This repo fully adopts the RC.EPIC.STORY.TASK+BUILD schema:

- **Format:** `RC.EPIC.STORY.TASK+BUILD`
- **Components:**
  - **RC:** Release Candidate (0 = development, 1+ = release candidate)
  - **EPIC:** Dev-kit Epic number (1, 2, 3, 4, …)
  - **STORY:** Story number within Epic
  - **TASK:** Task number within Story
  - **BUILD:** Build number (increments per release within a Task)

Examples (dev-kit context):

- `0.1.1.1+1` – Dev snapshot for **Epic 1**, Story 1, Task 1, first build  
- `0.2.3.2+4` – Dev snapshot for **Epic 2**, Story 3, Task 2, 4th build  
- `1.4.1.1+1` – Release Candidate 1 for **Epic 4**, Story 1, Task 1, first build

> **Note:** Any references to versions like `0.9.21.3+1` in framework docs are **examples from other projects**, not dev-kit releases.

---

## 3. Epic Ranges for AI Dev Kit

Unlike the legacy/new split in the original policy, this repo starts **clean**:

- **Epic 1+:** All dev-kit epics use the full `RC.EPIC.STORY.TASK+BUILD` schema.
- There is **no legacy range** (1–9) in this repo – we start from first principles.

Initial epics:

- **Epic 1 – AI Dev Kit Core**
- **Epic 2 – Workflow Management Framework**
- **Epic 3 – Numbering & Versioning Framework**
- **Epic 4 – Kanban Framework**

Future epics (5+) can be introduced as needed (for example, “Book Manuscript”, “Examples & Templates”, etc.).

---

## 4. Mapping Kanban to Version Components

This repo’s Kanban is defined under:

- `KB/PM_and_Portfolio/kanban/_index.md`
- `KB/PM_and_Portfolio/kanban/epics/Epic-X/stories/Story-XXX-*.md`

Mapping rules:

- **Every Story** belongs to exactly one Epic (1–4 to start with).
- **Every Task**:
  - Lives under a Story.
  - Will eventually get a numeric **Task ID** that matches the `TASK` component in the version.
- **Every substantive change** that goes through Release Workflow (RW):
  - Targets **one active Task**.
  - Uses a version where `EPIC`, `STORY`, and `TASK` match that Task’s E/S/T coordinates.
  - Increments `BUILD` for successive releases of the same Task.

FR/BR rule (summarised):

- FRs and BRs **must** create Tasks, which are anchored under Stories, which are anchored under Epics.

See: `KB/PM_and_Portfolio/rituals/policy/kanban-governance-policy.md`.

---

## 5. Version File for This Repo

Dev-kit version information lives in:

- `src/fynd_deals/version.py` (legacy path from fynd.deals; acceptable for now, may be renamed to `src/vibe_dev_kit/version.py` in future)

The file should expose:

```python
VERSION_RC = <int>        # Release candidate
VERSION_EPIC = <int>      # Dev-kit Epic number
VERSION_STORY = <int>     # Story number within epic
VERSION_TASK = <int>      # Task number within story
VERSION_BUILD = <int>     # Build number

VERSION_STRING = f"{VERSION_RC}.{VERSION_EPIC}.{VERSION_STORY}.{VERSION_TASK}+{VERSION_BUILD}"
```

Current values are **temporary placeholders** until we assign real Epics/Stories/Tasks for dev-kit work.

---

## 6. Progression Rules (Dev Kit)

For a given Epic, Story, Task:

- Working on **Epic 1, Story 1, Task 1**:
  - `0.1.1.1+1` – First dev build
  - `0.1.1.1+2` – Second dev build

- Moving to **Task 2** within the same Story:
  - `0.1.1.2+1` – First dev build for Task 2

Rules:

1. **TASK is stable per Task** – once you start `Task 1`, all its releases share `TASK = 1`.
2. **BUILD increments** for each release on the same Task.
3. **Moving to a new Task**:
   - `TASK` changes.
   - `BUILD` resets to `1`.
4. **RC increments**:
   - When promoting a dev snapshot to a release candidate for a given Task.

### 6.1 Task Transitions

**CRITICAL:** When moving to a new Task, the version file (`src/fynd_deals/version.py`) MUST be updated:

1. **Update `VERSION_TASK`:**
   - Set `VERSION_TASK` to match the new Task number
   - Example: Moving from Task 1 to Task 2 → `VERSION_TASK = 2`

2. **Reset `VERSION_BUILD`:**
   - Set `VERSION_BUILD = 1` (new Task always starts at BUILD 1)
   - Example: Moving from Task 1 to Task 2 → `VERSION_BUILD = 1`

3. **When to Update:**
   - **Option 1:** Update `version.py` when creating the new Task (recommended)
   - **Option 2:** Update `version.py` during Release Workflow Step 2 (automatic detection)
   - **CRITICAL:** Must be updated before running Release Workflow for the new Task

4. **Validation:**
   - Release Workflow Step 1 validates that `VERSION_TASK` matches the active Task number
   - If mismatch detected, workflow stops with error message
   - Release Workflow Step 2 automatically detects Task transitions and updates `VERSION_TASK` if needed

**Example Task Transition:**

**Before (Completing Task 1):**
```python
VERSION_EPIC = 4
VERSION_STORY = 3
VERSION_TASK = 1
VERSION_BUILD = 2
# Version: 0.4.3.1+2
```

**After (Starting Task 2):**
```python
VERSION_EPIC = 4
VERSION_STORY = 3
VERSION_TASK = 2  # ← Updated to match new Task
VERSION_BUILD = 1  # ← Reset to 1 for new Task
# Version: 0.4.3.2+1
```

**Common Mistakes to Avoid:**

- ❌ **DON'T:** Keep `VERSION_TASK = 1` and increment `VERSION_BUILD` when moving to Task 2
  - Wrong: `0.4.3.1+3` for Task 2
  - Correct: `0.4.3.2+1` for Task 2

- ❌ **DON'T:** Forget to reset `VERSION_BUILD` when moving to a new Task
  - Wrong: `0.4.3.2+3` for first release of Task 2
  - Correct: `0.4.3.2+1` for first release of Task 2

---

## 7. CHANGELOG Format

This repo uses a **two-layer changelog system** aligned with the framework pattern:

### Main Summary Changelog (`CHANGELOG.md`)

**Format:**
```markdown
## [0.3.1.1+2] - 02-12-25

📚 Documentation: Task 1 complete - Gap analysis comparing dev-kit versioning policy with framework

### Added
- Created gap analysis report...

### Notes
- See `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.3.1.1+2.md` for full details
```

**Key Characteristics:**
- Version: `[RC.EPIC.STORY.TASK+BUILD]`
- Date: `DD-MM-YY` (short date format for merge-to-main)
- Link to detailed changelog archive
- Can be updated if merge date changes

### Detailed Changelog Archive (`KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v{version}.md`)

**Format:**
```markdown
# Release v0.3.1.1+2

**Release Date:** 2025-12-02 00:00:00 UTC

**Epic / Story / Task:** Epic 3, Story 1, Task 1
**Type:** 📚 Documentation

## Summary
...

## Changes
...

## Related Work
- Epic: 3
- Story: 1
- Task: 1
```

**Key Characteristics:**
- Full timestamp: `YYYY-MM-DD HH:MM:SS UTC` (immutable)
- Epic/Story/Task information
- Detailed change descriptions
- **IMMUTABLE** once written (never edit `**Release Date:**`)

> **Reference:** See `packages/frameworks/numbering & versioning/versioning-strategy.md` for complete two-layer timestamp system documentation.

---

## 8. Canonical Ordering Principle

**Version numbers (`RC.EPIC.STORY.TASK+BUILD`) are the canonical ordering metric for all releases and changelog entries.**

This means:

- **Version ordering is independent of wall-clock time**
  - If `0.3.1.2+1` was committed on 2025-12-02 at 10:00:00 UTC
  - And `0.3.1.1+2` was committed on 2025-12-02 at 15:30:00 UTC
  - The changelog still orders them as: `0.3.1.1+2` first, then `0.3.1.2+1`
  - **The version number determines order, not the actual commit timestamp**

- **Parallel epic development is fully supported**
  - Epic 1 work (`0.1.x.x+x`) can be committed after Epic 4 work (`0.4.x.x+x`)
  - Epic 4 work can be committed before Epic 1 work
  - **The changelog orders by version number, not by Git commit time**

- **This enables true parallel development**
  - Multiple epics can work simultaneously
  - Each epic maintains its own version stream
  - When merged, versions are ordered correctly by their semantic structure

**The version number encodes the work hierarchy (Epic → Story → Task → Build), and that hierarchy is what matters for ordering, not when the code was actually committed.**

> **Reference:** See `packages/frameworks/numbering & versioning/versioning-strategy.md` (Section: Core Principle: Version Numbers Are Canonical) for complete documentation.

---

## 9. Two-Layer Timestamp System

The versioning strategy uses **two distinct timestamp layers** with **different purposes**:

### Layer 1: Main Summary Changelog (`CHANGELOG.md`)

**Format:** Short date in `DD-MM-YY` format  
**Example:** `## [0.3.1.1+2] - 02-12-25`

**Purpose:**
- Shows **when this version was merged into `main`**
- Provides a quick reference for "when did this hit production"
- Uses short format for readability in the summary view

**Key Characteristics:**
- **Not used for ordering** (version number is canonical)
- **Reflects merge-to-main date**, not commit date
- **Can be updated** if a version is merged on a different day than initially recorded
- **Format:** `DD-MM-YY` (e.g., `02-12-25` for December 2, 2025)

### Layer 2: Detailed Changelog Archive (`KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v{version}.md`)

**Format:** Full timestamp in `YYYY-MM-DD HH:MM:SS UTC` format  
**Example:** `**Release Date:** 2025-12-02 00:00:00 UTC`

**Purpose:**
- Captures **when this detailed changelog entry was authored/recorded**
- Provides forensic-level precision for accountability
- Enables exact traceability to the moment of release documentation

**Key Characteristics:**
- **IMMUTABLE once written** - **NEVER edit this timestamp retroactively**
- **Reflects the actual time the changelog was created**, not when code was committed
- **Full precision** (date + time + timezone) for complete accountability
- **Format:** `YYYY-MM-DD HH:MM:SS UTC` (e.g., `2025-12-02 00:00:00 UTC`)

### Why Two Layers?

1. **Different purposes:**
   - Main changelog: Quick reference for "when did this merge to main"
   - Detailed changelog: Forensic record of "when was this release documented"

2. **Different audiences:**
   - Main changelog: Developers scanning recent releases
   - Detailed changelog: Forensic analysis, audit trails, accountability

3. **Different update rules:**
   - Main changelog: Can be updated if merge date changes
   - Detailed changelog: **IMMUTABLE** - historical record must be preserved

4. **Enables parallel development:**
   - Versions are ordered by number, not by timestamp
   - Timestamps provide context, not ordering

> **Reference:** See `packages/frameworks/numbering & versioning/versioning-strategy.md` (Section: Two-Layer Timestamp System) for complete documentation.

---

## 10. Forensic Traceability Grid

The versioning strategy provides **complete traceability** through a multi-dimensional grid:

### Dimension 1: Version ↔ Epic/Story/Task

**Encoding:** The version number itself (`RC.EPIC.STORY.TASK+BUILD`)

**Traceability Path:**
- `0.3.1.1+2` → Epic 3, Story 1, Task 1, Build 2
- Direct mapping from version to work hierarchy
- No lookup required - the version number IS the identifier

### Dimension 2: Version ↔ Detailed Changelog

**Mapping:** One detailed changelog file per version

**File Location:** `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v{version}.md`

**Traceability Path:**
- Version number → File path (deterministic)
- File contains: Full timestamp, epic/story/task info, detailed changes
- **Full timestamp provides forensic-level accountability**

### Dimension 3: Version ↔ Main Summary Changelog

**Mapping:** One summary entry per version in `CHANGELOG.md`

**Traceability Path:**
- Version number → Summary entry (ordered by version, not time)
- Entry contains: Short date (merge-to-main), summary, link to detailed changelog
- **Short date shows when version merged to main**

### Dimension 4: Version ↔ Kanban Forensic Markers

**Mapping:** Epic/Story documents and Kanban rituals include explicit version references

**Traceability Path:**
- Version number → Epic/Story/Task documents
- Documents contain: Version references, commit hashes, workflow run IDs
- **Kanban markers provide work context and decision history**

**Example:**
- Version: `0.3.1.1+2`
- Epic 3 document: `KB/PM_and_Portfolio/kanban/epics/Epic-3/Epic-3.md`
- Story 1 markers: Version references, commit hashes, workflow runs

### Dimension 5: Version ↔ Git History

**Mapping:** Version number in commit messages and tags

**Traceability Path:**
- Version number → Git commits (via commit messages)
- Git commits → Commit hashes, author, timestamp
- **Git history provides code-level traceability**

**Example:**
- Version: `0.3.1.1+2`
- Commit message: "Release v0.3.1.1+2: Task 1 complete..."
- Git commit: Contains code changes, author, commit timestamp

**This grid provides complete accountability and efficient traceability.**

> **Reference:** See `packages/frameworks/numbering & versioning/versioning-strategy.md` (Section: Forensic Traceability Grid) for complete documentation.

---

## 11. Immutability Rules

### Rule 1: Detailed Changelog Timestamps Are Immutable

**Once a detailed changelog file is created with a `**Release Date:**` timestamp, that timestamp MUST NEVER be edited.**

**Rationale:**
- The timestamp captures **when the changelog entry was authored**
- Editing it would corrupt the forensic record
- Historical accuracy requires preserving original timestamps

**What This Means:**
- ❌ **NEVER** edit `**Release Date:**` in existing changelog files
- ❌ **NEVER** "fix" old timestamps to satisfy new validation rules
- ❌ **NEVER** update timestamps for cosmetic reasons
- ✅ **ONLY** create new changelog files with correct timestamps going forward

### Rule 2: Version Ordering Is Immutable

**Once a version is assigned and documented, its position in the changelog ordering is fixed by the version number.**

**Rationale:**
- Version numbers encode the work hierarchy
- Ordering by version number ensures consistent, logical progression
- Changing order would break traceability

**What This Means:**
- Versions are ordered by `RC.EPIC.STORY.TASK+BUILD` structure
- `0.3.1.1+2` always comes before `0.3.1.2+1` in changelogs
- Even if `0.3.1.2+1` was committed first

### Rule 3: Historical Files Are Preserved As-Is

**Changelog files created before the full-timestamp policy are preserved exactly as they were created.**

**Rationale:**
- Historical files are artifacts of their time
- They reflect the practices and tools available when they were created
- Preserving them maintains the complete historical record

> **Reference:** See `packages/frameworks/numbering & versioning/versioning-strategy.md` (Section: Immutability Rules) for complete documentation.

---

## 12. Version Validation

### Validation Scripts

The dev-kit uses validation scripts from the workflow management framework:

- **`packages/frameworks/workflow mgt/scripts/validation/validate_branch_context.py`**
  - Validates version matches branch/epic
  - Checks version format (old vs new)
  - Validates CHANGELOG entries match branch

- **`packages/frameworks/workflow mgt/scripts/validation/validate_changelog_format.py`**
  - Validates version format in CHANGELOG.md
  - Checks date format (old: `YYYY-MM-DD`, new: `DD-MM-YY`)
  - Validates build number >= 1
  - Grandfathers old format (warnings only)

### Validation Behavior

- **New files (TASK+BUILD format):** Require strict enforcement
- **Pre-commit hooks:** Enforce format before commit (when configured)
- **Release Workflow:** Validators run automatically before commit
- **CI/CD:** Can validate in continuous integration (when configured)

### Manual Review Checklist

**Before committing:**
1. Verify version number matches branch/epic/story/task
2. Verify detailed changelog has full timestamp (new format)
3. Verify main changelog has short date (`DD-MM-YY`)
4. Verify version in commit message
5. Verify Kanban markers updated

**After merging:**
1. Verify changelog ordering (by version, not time)
2. Verify traceability grid is complete
3. Verify historical files preserved

> **Reference:** See `packages/frameworks/workflow mgt/scripts/validation/` for validation script implementations.

---

## 13. Relationship to Framework Policies

This policy is a **specialisation** of the general framework policies:

- **Base schema & strategy:**
  - `packages/frameworks/numbering & versioning/versioning-policy.md` (primary SoT)
  - `packages/frameworks/numbering & versioning/versioning-strategy.md` (comprehensive strategy)
- **Kanban integration:**
  - `packages/frameworks/kanban/policies/kanban-governance-policy.md`
  - `KB/PM_and_Portfolio/rituals/policy/kanban-governance-policy.md` (dev-kit local)

The dev-kit policy:

- **Fixes the EPIC space (1–4+) for this repo**
- **Clarifies that all work in this repo** using the version file is speaking about dev-kit Epics/Stories/Tasks, not any external project
- **References framework policies** as the canonical source of truth for detailed patterns and strategies
- **Documents dev-kit-specific adaptations** while maintaining alignment with framework principles

**Key Principle:** The framework policies (`packages/frameworks/numbering & versioning/`) serve as the **canonical source of truth**. This dev-kit policy documents how the framework is applied in the dev-kit context, referencing the framework for detailed explanations.

---

## 14. Status and Maintenance

**Status:** Active  
**Owner:** AI Dev Kit Lead  
**Last Updated:** 2025-12-02  
**Related Work:** Epic 3, Story 1 (Dev Kit Alignment with Versioning Framework)

**Maintenance:**
- This policy should be reviewed when framework policies are updated
- Gaps identified in gap analysis (T001) have been addressed
- Policy aligns with framework patterns while maintaining dev-kit-specific context

---

## 15. References

**Framework Policies (Canonical SoT):**
- `packages/frameworks/numbering & versioning/versioning-policy.md`
- `packages/frameworks/numbering & versioning/versioning-strategy.md`
- `packages/frameworks/numbering & versioning/README.md`

**Dev-Kit Implementation:**
- `src/fynd_deals/version.py` (version file - to be renamed to dev-kit-specific path)
- `CHANGELOG.md` (main summary changelog)
- `KB/Changelog_and_Release_Notes/Changelog_Archive/` (detailed changelog archive)
- `KB/PM_and_Portfolio/kanban/` (Kanban board and Epic/Story docs)

**Validation Scripts:**
- `packages/frameworks/workflow mgt/scripts/validation/validate_branch_context.py`
- `packages/frameworks/workflow mgt/scripts/validation/validate_changelog_format.py`

**Related Documentation:**
- **[Versioning Quick Reference](versioning-quick-reference.md)** - 1-2 page summary for quick lookup ⚡
- **[Dual-Versioning Guide](dual-versioning-package-managers.md)** - Managing `RC.EPIC.STORY.TASK+BUILD` + SemVer for package managers ⚠️
- `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-cookbook.md` - Practical worked examples
- `KB/PM_and_Portfolio/kanban/epics/Epic-3/Story-001-dev-kit-alignment-with-versioning-framework/T001-gap-analysis-report.md` (gap analysis)
- `KB/PM_and_Portfolio/kanban/epics/Epic-3/Story-001-dev-kit-alignment-with-versioning-framework/T002-fynd-deals-epic15-findings.md` (findings)


