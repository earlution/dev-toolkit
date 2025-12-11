---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-04T12:02:50Z
expires_at: null
housekeeping_policy: keep
---

# Dev Toolkit – Kanban Board (Quick View)

**Last Updated:** 2025-01-27  
**Version:** v0.1.2.1+1

**Note:** This board tracks work on the `dev-toolkit` repository. The ai-dev-kit epics (Epic-1 through Epic-9) visible in the `epics/` directory are framework documentation examples from the Kanban framework package, not dev-toolkit project epics.

---

## Overview

Quick reference board for all dev-toolkit Kanban work. For detailed views, see [`kanban-board.md`](kanban-board.md).

**Structure:** All Kanban docs live under `KB/PM_and_Portfolio/kanban/`:
- Epic overviews: `epics/Epic-X/Epic-X.md`
- Story documents: `epics/Epic-X/Story-XXX-*.md`
- Board views: This file (quick) and `kanban-board.md` (detailed)

---

## Dev-Toolkit Epics Summary

| Epic | Title                              | Status         | Stories | Progress |
|------|------------------------------------|----------------|---------|----------|
| 1    | Tool Management and Registry System | IN PROGRESS    | 2       | 2/2      |

**Dev-Toolkit Epic Docs:** 
- [`epics/Epic-1/Epic-1.md`](epics/Epic-1/Epic-1.md) - **Dev-Toolkit Epic 1**

**Note:** Epics 1-9 in the `epics/` directory are ai-dev-kit framework examples (from `packages/frameworks/kanban/`). Dev-toolkit epics start fresh from Epic 1.

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


