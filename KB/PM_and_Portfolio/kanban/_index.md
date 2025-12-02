# Vibe Dev Kit – Kanban Board

This directory contains the **Kanban view** for work on the `vibe-dev-kit` repo and the **Vibe Coding For Dummies** book project.

The structure is intentionally simple and modular:

- This Kanban is **local to this repo** (not shared with any other project).
- Stories live under `KB/PM_and_Portfolio/kanban/stories/`.
- You can add epics, swimlanes, or additional metadata later without breaking the structure.

---

## Board (Stories)

| Story ID | Title                                      | Status  | Owner | Notes                           |
|---------:|--------------------------------------------|---------|-------|---------------------------------|
| 001      | Set up Kanban + versioning for dev kit     | In Progress | RMS   | Local Kanban + version schema  |

Each row in this table should map to a corresponding Story file in `stories/`, for example:

- `stories/Story-001-vibe-dev-kit-kanban-and-versioning.md`

You can extend this board with additional columns (e.g., Epic, Priority, Target Release) as the project grows.

---

## How to Add a New Story

1. **Create a story file** under `KB/PM_and_Portfolio/kanban/stories/`, following the naming pattern:
   - `Story-XXX-short-slug.md` (e.g., `Story-002-vibe-dev-kit-testing.md`)
2. **Update this board** (`_index.md`) with a new row pointing to that story.
3. **Keep everything local** to this repo unless you explicitly decide to link to external projects.


