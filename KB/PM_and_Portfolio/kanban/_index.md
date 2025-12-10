---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-04T12:02:50Z
expires_at: null
housekeeping_policy: keep
---

# AI Dev Kit – Kanban Board (Quick View)

**Last Updated:** 2025-12-06  
**Version:** v0.5.2.2+1

**Note:** Epics 1-4 are COMPLETE ✅. Epics 5-9 are IN PROGRESS or TODO.

---

## Overview

Quick reference board for all Kanban work. For detailed views, see [`kanban-board.md`](kanban-board.md).

**Structure:** All Kanban docs live under `KB/PM_and_Portfolio/kanban/`:
- Epic overviews: `epics/Epic-X/Epic-X.md`
- Story documents: `epics/Epic-X/Story-XXX-*.md`
- Board views: This file (quick) and `kanban-board.md` (detailed)

---

## Epics Summary

| Epic | Title                              | Status         | Stories | Progress |
|------|------------------------------------|----------------|---------|----------|
| 1    | AI Dev Kit Core                 | COMPLETE ✅     | 3       | 3/3      |
| 2    | Workflow Management Framework      | COMPLETE ✅     | 4       | 4/4      |
| 3    | Numbering & Versioning Framework   | COMPLETE ✅     | 3       | 3/3      |
| 4    | Kanban Framework                   | COMPLETE ✅     | 4       | 4/4      |
| 5    | Documentation Management          | IN PROGRESS    | 3       | 1/3      |
| 6    | Framework Management               | COMPLETE ✅     | 3       | 3/3      |
| 7    | Examples and Adoption              | TODO           | 3       | 0/3      |
| 8    | Tooling and Automation             | TODO           | 3       | 0/3      |
| 9    | Book Content Development          | IN PROGRESS    | 3       | 0/3      |

**Epic Docs:** 
- [`epics/Epic-1/Epic-1.md`](epics/Epic-1/Epic-1.md)
- [`epics/Epic-2/Epic-2.md`](epics/Epic-2/Epic-2.md)
- [`epics/Epic-3/Epic-3.md`](epics/Epic-3/Epic-3.md)
- [`epics/Epic-4/Epic-4.md`](epics/Epic-4/Epic-4.md)
- [`epics/Epic-5/Epic-5.md`](epics/Epic-5/Epic-5.md)
- [`epics/Epic-6/Epic-6.md`](epics/Epic-6/Epic-6.md)
- [`epics/Epic-7/Epic-7.md`](epics/Epic-7/Epic-7.md)
- [`epics/Epic-8/Epic-8.md`](epics/Epic-8/Epic-8.md)
- [`epics/Epic-9/Epic-9.md`](epics/Epic-9/Epic-9.md)

---

## How to Add Work

1. **Create Epic** (if needed):
   - Create `epics/Epic-X/` directory
   - Add `epics/Epic-X/Epic-X.md` (Epic overview)
   - Update this board (`_index.md`) and `kanban-board.md`

2. **Create Story**:
   - Add `epics/Epic-X/Story-XXX-short-slug.md`
   - Update Epic doc (`epics/Epic-X/Epic-X.md`) with Story reference
   - Update this board (`_index.md`) and `kanban-board.md`

3. **Track Progress**:
   - Update Story status in Story doc
   - Update Epic doc with version markers as work completes
   - Update board views as needed

See [`README.md`](README.md) for full structure details and `KB/PM_and_Portfolio/rituals/policy/kanban-governance-policy.md` for governance.


