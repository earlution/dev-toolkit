# Story 001 – Set Up Kanban and Versioning for Vibe Dev Kit

**Status:** In Progress  
**Owner:** RMS  
**Repo:** `vibe-dev-kit`  
**Version:** (TBD – dev-kit schema to be defined for this repo)  

---

## 1. Story Overview

This story creates a **local Kanban structure** and **versioning entry point** for the `vibe-dev-kit` repo itself, separate from any application project (like fynd.deals or Confidentia).

Goals:

- Provide a simple, repo-local Kanban structure under `KB/PM_and_Portfolio/kanban/`.
- Avoid importing external Kanban structures (e.g., `knowledge/fynd_deals/Kanban`).
- Prepare ground for a **dev-kit-specific versioning strategy** that does not claim to be working on any external Epic (such as Epic 9).

---

## 2. Kanban Structure for This Repo

**Target structure:**

```text
KB/
  PM_and_Portfolio/
    kanban/
      _index.md                  # Kanban board for this repo
      stories/
        Story-001-vibe-dev-kit-kanban-and-versioning.md
        Story-XXX-...            # Future stories
```

This structure is:

- **Local:** It belongs only to `vibe-dev-kit`.
- **Story-first:** Stories live in `kanban/stories/` with simple numeric IDs.
- **Flexible:** You can introduce epics or other groupings later without changing the base layout.

---

## 3. Tasks

### Task 1 – Create Kanban Board File

- [x] Create `KB/PM_and_Portfolio/kanban/_index.md` with:
  - A short description of the board.
  - A minimal stories table.
  - A reference to this story file.

### Task 2 – Create Story 001 File

- [x] Create `KB/PM_and_Portfolio/kanban/stories/Story-001-vibe-dev-kit-kanban-and-versioning.md` (this file).
- [x] Include:
  - Status, Owner, Repo, and placeholder Version.
  - Overview of the Kanban and versioning goals.
  - Task list (this section).

### Task 3 – Decide Versioning Approach for This Repo

- [ ] Decide whether this repo:
  - Uses the same `RC.EPIC.STORY.TASK+BUILD` schema as the Numbering & Versioning package, **but with its own epic range**, or
  - Uses a simplified schema (e.g., `0.MAJOR.MINOR+BUILD`) dedicated to the dev kit itself.
- [ ] Document the decision in a local versioning policy under:
  - `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md` (or similar).
- [ ] Align `src/fynd_deals/version.py` (or a renamed version file) with the chosen schema.

### Task 4 – Align RW with Dev-Kit Versioning

- [ ] Update `release-workflow-agent-execution.md` to:
  - Clarify that examples using `0.9.21.3+2` are **Confidentia/fynd.deals examples**, not dev-kit releases.
  - Add a short note about how RW should be interpreted when running directly in the `vibe-dev-kit` repo.
- [ ] Ensure `.cursorrules` (when added for this repo) uses the correct dev-kit version schema.

---

## 4. Notes & Open Questions

- **Epic mapping:**  
  For this repo, we haven’t yet defined any canonical **Epic IDs**. Until that’s done, we should avoid publishing tags that encode an Epic number (e.g., `0.9.21.3+2`) as if it were authoritative for this repo.

- **Scope separation:**  
  This repo models **portable frameworks** (workflow mgt, numbering & versioning, etc.). Its versioning should reflect **framework/package evolution**, not application-level epics from other projects.

When these questions are resolved and the tasks above are completed, this story can be marked as **Done** and new stories can reference the resulting policies and structures.


