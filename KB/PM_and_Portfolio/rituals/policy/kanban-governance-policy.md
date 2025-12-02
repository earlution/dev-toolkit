# Vibe Dev Kit – Kanban Governance Policy

**Owner:** Vibe Dev Kit / Book Project Lead  
**Last Updated:** 2025-12-02  
**Applies To:** All work tracked in the `vibe-dev-kit` repo  
**Based On:** `packages/frameworks/kanban/policies/kanban-governance-policy.md` (project-agnostic framework)

---

## 1. Purpose

This policy defines **how the Vibe Dev Kit repo runs Kanban** for:

- Work on the **Vibe Dev Kit** frameworks themselves (workflow mgt, numbering & versioning, kanban, etc.)
- Work on the **Vibe Coding For Dummies** book project that lives in this repo

This policy adopts the **full versioning schema and strategy** from the Numbering & Versioning package:

- **Version schema:** `RC.EPIC.STORY.TASK+BUILD`
- **All substantive work is Task-driven** (Feature Requests and Bug Reports become Tasks)

The implementation in this repo starts simple:

- Uses **Stories and Tasks** as the primary work items (Epics will be added as the work grows)
- Uses a **simple board view** in `KB/PM_and_Portfolio/kanban/_index.md`
- Can be evolved later to add Epics, swimlanes, WIP limits, etc.

---

## 2. Board Structure (This Repo)

### 2.1 Location

**Single Kanban Directory:** All Kanban documentation lives under `KB/PM_and_Portfolio/kanban/`:

- **Board files:**
  - `KB/PM_and_Portfolio/kanban/_index.md` (quick board view)
  - `KB/PM_and_Portfolio/kanban/kanban-board.md` (detailed board view)
  - `KB/PM_and_Portfolio/kanban/README.md` (structure overview)

- **Epic files:**
  - `KB/PM_and_Portfolio/kanban/epics/Epic-X.md` (Epic overview document)

- **Story files:**
  - `KB/PM_and_Portfolio/kanban/epics/Epic-X/stories/Story-XXX-*.md` (Story documents and associated files)

### 2.2 Columns (Conceptual)

The current board is implemented as a **table**, but conceptually it follows three columns:

1. **Backlog** – Defined stories not yet started  
2. **In Progress** – Stories currently being worked on  
3. **Done** – Completed stories (implemented, documented, and—if relevant—released)

You can represent these as:

- A column in the board table (e.g., `Status` = `Backlog` / `In Progress` / `Done`), and/or
- Separate sections in `_index.md` if the board grows more complex.

---

## 3. Work Items (This Repo)

### 3.1 Epics

Epics represent broad, conceptual areas of work (for example, “Kanban Framework”, “Workflow Framework”, “Book Manuscript”).

- **Location:** `KB/PM_and_Portfolio/kanban/epics/Epic-X.md` (Epic overview document)
- **Directory:** `KB/PM_and_Portfolio/kanban/epics/Epic-X/` (contains Stories subdirectory)
- **Template:** Use `packages/frameworks/kanban/templates/EPIC_TEMPLATE.md` as starting point

**Structure:**
```
kanban/epics/
├── Epic-1.md              # Epic 1 overview
├── Epic-1/                # Epic 1 directory
│   └── stories/           # Stories for Epic 1
│       ├── Story-001-*.md
│       └── [other story files]
├── Epic-2.md
└── Epic-2/
    └── stories/
        └── Story-XXX-*.md
```

**Every Story must belong to an Epic.** When creating a new Story, ensure its Epic exists (create Epic doc and directory if needed).

### 3.2 Stories

Stories are the **primary unit of planning** in this repo.

- **Location:** `KB/PM_and_Portfolio/kanban/epics/Epic-X/stories/Story-XXX-short-slug.md`
- **ID:** `XXX` (numeric string, e.g. `001`, `002`)
- **Directory:** Each Story lives in its Epic's `stories/` subdirectory, allowing for associated files (diagrams, notes, etc.)
- **Examples:**
  - `KB/PM_and_Portfolio/kanban/epics/Epic-1/stories/Story-001-vibe-dev-kit-kanban-and-versioning.md`

**Each Story file should include:**

- Status (`TODO` / `In Progress` / `Done`)
- Owner
- Repo (usually `vibe-dev-kit`)
- A brief overview of the goal
- A task checklist

### 3.3 Tasks

Tasks are **checklist items** inside a Story and are the **atomic unit of work**.

- All substantive work MUST be represented as a **Task**.
- Each Task should be small enough to complete in **1–3 days**.
- Over time, Tasks can adopt the full `Exx:Sxx:Txxx` numbering from the Kanban templates, and the active Task should map to the `TASK` component in the version number (`RC.EPIC.STORY.TASK+BUILD`).

**FR/BR rule (this repo):**

- Every **Feature Request (FR)** and **Bug Report (BR)** MUST:
  1. Create at least one **Task** under an existing Story, OR
  2. If no suitable Story exists, create a new Story (see below), then create the Task.
  3. If no suitable Epic conceptually exists yet for that Story, create or identify a broad, abstract Epic to host it once the epic structure is formalised.

This ensures that all work flowing into the dev kit is **Task / FR-driven** and anchored in the Kanban system.

---

## 4. Board Usage Rules

1. **Single Source of Truth:**  
   - The board at `KB/PM_and_Portfolio/kanban/_index.md` is the **canonical quick view** of active stories for this repo.
   - The detailed board at `KB/PM_and_Portfolio/kanban/kanban-board.md` provides full context.
   - Each row in the board must map to exactly one Story file in `kanban/epics/Epic-X/stories/`.

2. **Status Field:**  
   - Use `TODO`, `In Progress`, or `Done` in the board’s `Status` column.
   - Keep the Story file’s internal `Status` field in sync with the board.

3. **Story Creation Flow:**
   1. **Ensure Epic exists:**
      - If Epic doesn't exist, create `KB/PM_and_Portfolio/kanban/epics/Epic-X.md` and `Epic-X/` directory
      - Create `Epic-X/stories/` subdirectory
   2. **Create Story file:**
      - `KB/PM_and_Portfolio/kanban/epics/Epic-X/stories/Story-XXX-short-slug.md`
      - Story directory allows for associated files (diagrams, notes, etc.) as needed
   3. **Update Epic doc:**
      - Add Story reference to Epic's Story Checklist
   4. **Update board views:**
      - Add row to `_index.md` (quick view)
      - Update `kanban-board.md` (detailed view) with Story details

4. **Updates:**
   - When you change a Story’s status or owner, update **both**:
     - The Story file, and
     - The board row in `_index.md`.

---

## 5. Relationship to the Kanban Framework Package

This repo **intends to use the full Kanban + Versioning + Workflow stack**, but is rolling it out in stages:

- We **do use now**:
  - Story + Task checklists as the primary work items
  - A canonical board in `KB/PM_and_Portfolio/kanban/_index.md`
  - The principle that all substantive work is Task/FR-driven

- We **will add next**:
  - Epics for major areas of the dev kit
  - `E{epic}S{story}T{task}` numbering for Tasks
  - Full `RC.EPIC.STORY.TASK+BUILD` alignment between Kanban and versioning

The underlying framework details are defined in:

- `packages/frameworks/kanban/policies/kanban-governance-policy.md`
- `packages/frameworks/kanban/integration/numbering-versioning-integration.md`

---

## 6. Versioning (This Repo)

This repo adopts the **RC.EPIC.STORY.TASK+BUILD** schema from the Numbering & Versioning framework, but with a dev-kit–specific interpretation to be finalised in `dev-kit-versioning-policy.md`:

- All releases are expressed as `RC.EPIC.STORY.TASK+BUILD`.
- Over time, each Task in Kanban will map to the `TASK` component of the version.
- Feature Requests and Bug Reports feed into Tasks, which then feed into versions (via Release Workflow) and documentation (via Kanban + RW integration).

Story 001 (“Set Up Kanban and Versioning for Vibe Dev Kit”) owns the work of:

- Defining the dev-kit epic/story/task ranges.
- Documenting the mapping between Kanban items and version components.
- Updating this policy once that mapping is locked in.

---

## 7. Next Steps

1. Finish **Story 001 – Set Up Kanban and Versioning for Vibe Dev Kit**:
   - Decide on a dev-kit versioning schema.
   - Document it under `KB/Architecture/Standards_and_ADRs/`.
   - Update this policy to align with that schema.

2. As work grows:
   - Consider introducing Epics for major areas (e.g., “Kanban Framework”, “Workflow Framework”, “Book Manuscript”).
   - Use the templates in `packages/frameworks/kanban/templates/` as starting points.


