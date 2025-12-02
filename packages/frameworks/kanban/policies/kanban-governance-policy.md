# Kanban Governance Policy

**Owner:** Product Ops / Project Leadership  
**Last Updated:** 2025-11-26  
**Applies To:** All work streams that adopt this Kanban system (project-agnostic)  
**Source Example:** Confidentia project (original implementation)

---

## Purpose

A single, authoritative policy describing how to run Kanban with:

- Work-item types (Epic → Story → Task) and how they map to Git artifacts  
- Documentation, numbering, and versioning requirements  
- Rituals (board usage, stand-ups, release workflow) linked to the knowledge base

This document originated in the **Confidentia** project but is written so it can be **ported to any project** by:

- Updating **file paths** to your own KB structure  
- Updating **terminology** (e.g., Epic/Story/Task vs Theme/Epic/Story)  
- Integrating with your own **versioning policy** and **workflow rules**

**Foundation:** In the original project, this policy is underpinned by Cursor rules (`.cursorrules`). For your project, treat `.cursorrules` (or equivalent automation/config) as the **enforcement layer** for this policy.

---

## The Harmonious Cycle

Work flows in perfect harmony:

```
Task (Kanban)
  → defines what to do
    → Version (RC.EPIC.STORY.TASK+BUILD)
      → tracks the work
        → Release Workflow
          → implements both policies
            → Kanban Update
              → records the version (forensic marker)
                → Repeat
```

**Principle:** All substantive work MUST be task-driven.
If work doesn't map to a task, the Kanban needs updating.

**FR/BR Source of Truth:**  
- Every **Feature Request (FR)** and **Bug Report (BR)** MUST result in at least one **Kanban Task**.  
- Tasks must always live **under a Story**, which must always live **under an Epic** (once epics are in use for the project).

**FR/BR → Task → Story → Epic flow (canonical rule):**

1. **FR/BR arrives** (issue tracker, support channel, notes, etc.).
2. **Check for existing Story** that matches the FR/BR scope:
   - If found → create a **new Task** under that Story.
3. **If no Story exists** for this area:
   - Create a new Story under the **appropriate Epic**.
4. **If no Epic exists** for this problem domain:
   - Create a new, conceptually broad **Epic** to host the new Story.
   - Then create the Story under that Epic, and the Task under that Story.

No FR/BR should exist without a corresponding **Task** anchored to a Story (and, once epics are in use, an Epic). This keeps Kanban, versioning, and release workflow aligned.

---

## Board Structure

Five columns, left to right:

1. **Backlog** – Groomed but unscheduled
2. **Ready** – Fully specified, awaiting prioritisation
3. **In Progress** – Active work with branch
4. **Verify** – Done, awaiting validation
5. **Done** – Released, tagged, validated

**Rules:**
- Move strictly left → right (no skipping)
- WIP limits per swimlane
- Every card links to KB doc and branch/tag

---

## Work Items

### Epics

Governing artifact for a feature set or maintenance theme.

- **Location (example):** `KB/PM_and_Portfolio/epics/overview/Epic XX/Epic-XX.md`  
  - Replace with your KB path for epic overview docs.
- **Branch (example convention):** `epic/<number>-<slug>`  
  - Adjust to your branching strategy if different.
- **Version (when using RC.EPIC.STORY.TASK+BUILD):** `RC.EPIC.STORY.TASK+BUILD` (where EPIC = epic number)
- **Template (example):** `KB/PM_and_Portfolio/epics/templates/EPIC_TEMPLATE.md`

### Stories

Decompose epic scope into releasable slices.

- **Location (example):** `KB/PM_and_Portfolio/stories/overview/Epic XX/Story-N-Title.md`
- **Numbering (example):** `E<epic>S<story>` (e.g., `E20S7`)
- **Template (example):** `KB/PM_and_Portfolio/stories/templates/STORY_TEMPLATE.md`

### Tasks

Atomic units inside a story.

- **Numbering (example):** `Exx:Sxx:Txxx` (Epic, Story, Task with zero padding)
- **Example:** `E20:S07:T010` = Epic 20, Story 7, Task 10
- **Documented:** Input / Deliverable / Dependencies / Blocker / Parallel Development Candidacy
- **Tracked:** Git commits reference task ID (or equivalent in your VCS)

---

## Versioning

### Schema

**Format:** `RC.EPIC.STORY.TASK+BUILD`

- **RC:** Release Candidate (0 = development, 1+ = release candidate)
- **EPIC:** Epic number
- **STORY:** Story number within epic
- **TASK:** Task number within story
- **BUILD:** Build number (increments per release within task)

**Example:** `0.20.11.15+1` = Development, Epic 20, Story 11, Task 15, Build 1

**Related Documentation (examples):**
- **Versioning Policy (Schema)** – Complete schema definition (e.g., `KB/Architecture/Standards_and_ADRs/versioning-policy.md`)
- **Versioning Strategy** – Forensic traceability and canonical ordering principles (e.g., `KB/Architecture/Standards_and_ADRs/versioning-strategy.md`)

### Task-Level Requirements

**CRITICAL:** All substantive work MUST be task-driven.

**Version TASK number must match active task.**

**Requirements:**
1. Version TASK reflects the active task
   - Working on `E20:S11:T016` → version `0.20.11.16+B`
   - TASK component aligns with Kanban task

2. Task transitions use `--task` parameter
   - New task: `--task N` in release workflow
   - Resets BUILD to 1, sets TASK to N

3. BUILD resets to 1 with new task
   - BUILD increments within same task
   - BUILD does NOT carry over between tasks

4. Validation enforces alignment
   - Release workflow validates task exists
   - Validators check task/version alignment
   - Pre-commit hooks enforce alignment

See: **your own canonical story docs** that define guardrails and versioning rules.  
(*Original example:* `KB/PM_and_Portfolio/stories/overview/Epic 20/Story-11-GUARDRAILS-PLAN.md` in the Confidentia project.)

---

## Release Workflow

The process that implements both policies (Kanban Governance and Versioning Strategy).

**Reference (example):** `KB/Documentation/Developer_Docs/vwmp/release-workflow-reference.md`

**Documents (example set):**
1. Version File (e.g., `src/yourproject/version.py`)
2. Detailed Changelog (e.g., `CHANGELOG_vRC.EPIC.STORY.TASK+BUILD.md`)
3. Main Changelog (e.g., `CHANGELOG.md`)
4. README (e.g., `README.md`)
5. Epic Doc (auto-updated)
6. Story Docs (auto-updated)
7. Kanban Board (auto-updated)
8. Branch Context Validator
9. Changelog Format Validator
10. Kanban Update Module

**Process:**
1. Version Bump
   - `--task N` sets task (resets BUILD to 1)
   - `--story N` sets story (resets TASK and BUILD to 1)
   - Otherwise increments BUILD on current task
   - Validates task exists and version TASK matches

2. Changelog Creation
   - Detailed changelog with full timestamp
   - Main CHANGELOG.md with summary

3. Kanban Auto-Update
   - Updates epic/story docs with version and summary
   - Updates completed tasks with version numbers
   - Updates Kanban board entry
   - Validates forensic markers were added

4. Validation
   - Branch context (epic ↔ version ↔ changelog, task/version alignment)
   - Changelog format (timestamp)
   - Task exists in story doc
   - Version TASK matches provided task

5. Git Operations
   - Stage all files
   - Commit with version in message
   - Create annotated tag
   - Push to remote

---

## Documentation

**Epics** reference:
- Branch name, version schema, story checklist, dependencies, risks

**Stories** include:
- Task index aligning with E#S#T# numbering
- Goals and acceptance criteria
- Completion summary before release

**Tasks** capture:
- Cross-team impacts (Parallel Development Candidacy)
- Staging plan if spanning multiple PRs

**Templates:**
- New epic/story created from templates (e.g., those in the Kanban package)
- Deviations should be reviewed/approved by whoever owns process governance in your context

---

## Rules

1. **Traceability:** Every board card links to KB doc, branch/tag, changelog entry
2. **Single Source of Truth:** KB docs are canonical
3. **Gate Conditions:**
   - Ready → In Progress: Story doc complete, blockers resolved, branch created
   - In Progress → Verify: Tasks checked, summary drafted, dry-run done
   - Verify → Done: Release workflow executed, tag pushed, KB doc accepted
4. **Numbering Discipline:** No duplicate IDs; IDs never reused
5. **WIP & Ownership:** Each story has named DRI; pause >48h moves back to Ready

---

## Templates & References

**Templates:**
- Epic: `KB/PM_and_Portfolio/epics/templates/EPIC_TEMPLATE.md`
- Story: `KB/PM_and_Portfolio/stories/templates/STORY_TEMPLATE.md`

**Release Workflow:**
- Script: `scripts/automation/release_workflow.py`
- Module: `scripts/automation/update_kanban_docs.py`
- Makefile: `make release`, `make release-check`

**Validation:**
- Branch Context: `scripts/validation/validate_branch_context.py`
- Changelog Format: `scripts/validation/validate_changelog_format.py`

**Policy Documents (examples):**
- **Versioning Strategy** – Complete versioning strategy with forensic traceability system (e.g., `KB/Architecture/Standards_and_ADRs/versioning-strategy.md`)
- **Versioning Policy (Schema)** – Versioning schema definition (e.g., `KB/Architecture/Standards_and_ADRs/versioning-policy.md`)
- **Release Workflow Reference** – Release Workflow documentation (e.g., `KB/Documentation/Developer_Docs/vwmp/release-workflow-reference.md`)
- **Kanban Board Overview** – Board structure (e.g., `KB/PM_and_Portfolio/rituals/overview/kanban-board.md`)
- **System Architecture / Template Philosophy** – Supporting governance docs (paths will vary by project)

**Foundation:**
- **Automation / Rules Engine:** In Confidentia this was Cursor Rules (`.cursorrules`) ⭐. In your project, use the equivalent mechanism (Cursor rules, CI checks, or other automation) as the enforcement layer for this policy.

---

## Change History

- **2025-11-26:** Refined task-level versioning requirements (original Confidentia example: Epic 20, Story 11, Task 011)
- **2025-11-26:** Updated to reference RC.EPIC.STORY.TASK+BUILD schema, defined all Release Workflow documents (original Confidentia example: Epic 20, Story 11, Task 015)
- **2025-11-20:** Initial policy authored (original Confidentia example: Epic 20 Story 6/7 follow-up)

---

## Portability Notes

When adopting this policy in a new project:

- **Update paths** to match your KB layout (e.g., where Epics, Stories, and Kanban board files live).
- **Confirm versioning**:
  - If you use `RC.EPIC.STORY.TASK+BUILD`, link to your own Versioning Policy and Strategy.
  - Otherwise, adapt the “Versioning” section to your schema and update examples.
- **Align work item names** (Epic/Story/Task vs Theme/Epic/Story, etc.) and adjust templates accordingly.
- **Decide ownership:** Replace Product Ops / PMO labels with the actual roles in your organisation.
