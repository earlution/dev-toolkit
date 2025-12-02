# Dev Kit Versioning Policy

**Status:** Draft (initial adoption)  
**Owner:** Vibe Dev Kit / Book Project Lead  
**Last Updated:** 2025-12-02  
**Related Work:** Epic 1 (Vibe Dev Kit Core)

---

## 1. Purpose

This policy defines how the **Vibe Dev Kit** repository uses the `RC.EPIC.STORY.TASK+BUILD` versioning schema.

Goals:

- Apply the **full versioning schema and strategy** from the Numbering & Versioning framework to this repo.
- Ensure all substantive work is **Task-driven** and that versions reflect **Tasks**.
- Keep `vibe-dev-kit` logically separate from any external project (e.g., Confidentia, fynd.deals) while reusing the same principles.

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

## 3. Epic Ranges for Vibe Dev Kit

Unlike the legacy/new split in the original policy, this repo starts **clean**:

- **Epic 1+:** All dev-kit epics use the full `RC.EPIC.STORY.TASK+BUILD` schema.
- There is **no legacy range** (1–9) in this repo – we start from first principles.

Initial epics:

- **Epic 1 – Vibe Dev Kit Core**
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

- `src/fynd_deals/version.py` (temporary path; may be renamed to a dev-kit–specific module later)

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

---

## 7. Relationship to Framework Policies

This policy is a **specialisation** of the general framework policies:

- Base schema & strategy:
  - `packages/frameworks/numbering & versioning/versioning-policy.md`
  - `packages/frameworks/numbering & versioning/versioning-strategy.md`
- Kanban integration:
  - `packages/frameworks/kanban/policies/kanban-governance-policy.md`
  - `packages/frameworks/kanban/integration/numbering-versioning-integration.md`

The dev-kit policy:

- Fixes the EPIC space (1–4+) for this repo.
- Clarifies that **all work in this repo** using the version file is speaking about dev-kit Epics/Stories/Tasks, not any external project.

---

## 8. Next Steps

1. **Align `version.py`** with a real dev-kit Epic/Story/Task:
   - Pick an initial Epic/Story/Task for the work we just did (e.g., Epic 1, Story 1, Task 1).
   - Set `VERSION_EPIC`, `VERSION_STORY`, `VERSION_TASK`, `VERSION_BUILD` accordingly.

2. **Introduce Epic docs**:
   - Create Epic 1–4 docs under `KB/PM_and_Portfolio/kanban/epics/Epic-{n}.md`.

3. **Update RW docs** to:
   - Clarify that dev-kit RW runs use **dev-kit epics** (1–4+).
   - Explicitly note that other version examples (e.g., `0.9.21.3+1`) are external project samples.


