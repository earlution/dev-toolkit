# Vibe Dev Kit – Kanban Board (Quick View)

**Last Updated:** 2025-12-02  
**Version:** v0.1.1.1+2

---

## Overview

Quick reference board for all Kanban work. For detailed views, see [`kanban-board.md`](kanban-board.md).

**Structure:** All Kanban docs live under `KB/PM_and_Portfolio/kanban/`:
- Epic overviews: `epics/Epic-X.md`
- Story documents: `epics/Epic-X/stories/Story-XXX-*.md`
- Board views: This file (quick) and `kanban-board.md` (detailed)

---

## Active Stories

| Epic | Story ID | Title                                      | Status      | Owner | Notes                           |
|------|---------:|--------------------------------------------|-------------|-------|---------------------------------|
| 1    | 001      | Set up Kanban + versioning for dev kit     | In Progress | RMS   | Epic 1, Story 1                |
| 2    | 001      | RW Agent Execution & Docs                   | TODO        | RMS   | Epic 2, Story 1                |
| 3    | 001      | Dev Kit Alignment with Versioning Framework | TODO        | RMS   | Epic 3, Story 1                |
| 4    | 001      | Dev Kit Kanban Implementation               | TODO        | RMS   | Epic 4, Story 1                |

**Story Locations:**
- Epic 1: [`epics/Epic-1/stories/Story-001-vibe-dev-kit-kanban-and-versioning.md`](epics/Epic-1/stories/Story-001-vibe-dev-kit-kanban-and-versioning.md)
- Epic 2: [`epics/Epic-2/stories/Story-001-rw-agent-execution-and-docs.md`](epics/Epic-2/stories/Story-001-rw-agent-execution-and-docs.md)
- Epic 3: [`epics/Epic-3/stories/Story-001-dev-kit-alignment-with-versioning-framework.md`](epics/Epic-3/stories/Story-001-dev-kit-alignment-with-versioning-framework.md)
- Epic 4: [`epics/Epic-4/stories/Story-001-dev-kit-kanban-implementation.md`](epics/Epic-4/stories/Story-001-dev-kit-kanban-implementation.md)

---

## Epics Summary

| Epic | Title                              | Status      | Stories |
|------|------------------------------------|-------------|---------|
| 1    | Vibe Dev Kit Core                 | IN PROGRESS | 1       |
| 2    | Workflow Management Framework      | TODO        | 1       |
| 3    | Numbering & Versioning Framework   | TODO        | 1       |
| 4    | Kanban Framework                   | TODO        | 1       |

**Epic Docs:** [`epics/Epic-1.md`](epics/Epic-1.md), [`epics/Epic-2.md`](epics/Epic-2.md), [`epics/Epic-3.md`](epics/Epic-3.md), [`epics/Epic-4.md`](epics/Epic-4.md)

---

## How to Add Work

1. **Create Epic** (if needed):
   - Add `epics/Epic-X.md` (Epic overview)
   - Create `epics/Epic-X/` directory
   - Create `epics/Epic-X/stories/` subdirectory

2. **Create Story**:
   - Add `epics/Epic-X/stories/Story-XXX-short-slug.md`
   - Update Epic doc (`epics/Epic-X.md`) with Story reference
   - Update this board (`_index.md`) and `kanban-board.md`

3. **Track Progress**:
   - Update Story status in Story doc
   - Update Epic doc with version markers as work completes
   - Update board views as needed

See [`README.md`](README.md) for full structure details and `KB/PM_and_Portfolio/rituals/policy/kanban-governance-policy.md` for governance.


