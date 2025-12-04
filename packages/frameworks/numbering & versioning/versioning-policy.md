---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-04T12:02:07Z
expires_at: null
housekeeping_policy: keep
---

# Versioning Policy

**Status:** Active  
**Owner:** Engineering  
**Last Updated:** 2025-12-01  
**Related Work:** Epic 9, Story 21

---

## Purpose

Defines semantic versioning schema using the `RC.EPIC.STORY.TASK+BUILD` format for fynd.deals.

**Key Capabilities:**
- Enables parallel epic/workstream development
- Maintains clear version tracking at task level
- Provides build-level granularity
- Supports forensic traceability

---

## Schema

**Format:** `RC.EPIC.STORY.TASK+BUILD`

**Structure:**
- **RC:** Release Candidate (0 = development, 1+ = release candidate)
- **EPIC:** Epic number (e.g., 9)
- **STORY:** Story number within epic (e.g., 21)
- **TASK:** Task number within story (e.g., 3)
- **BUILD:** Build number (increments per release within task)

**Examples:**
- `0.9.21.3+1` - Development, Epic 9, Story 21, Task 3, Build 1
- `0.9.21.3+2` - Development, Epic 9, Story 21, Task 3, Build 2
- `0.9.21.4+1` - Development, Epic 9, Story 21, Task 4, Build 1
- `1.9.21.3+1` - Release Candidate 1, Epic 9, Story 21, Task 3, Build 1

---

## Rules

### RC (Release Candidate)
- **0:** Development phase (default)
- **1+:** Release candidate phase
- Increment when entering release candidate phase

### EPIC
- Epic number from Kanban board
- Set when starting new epic
- Constant for all work within that epic

### STORY
- Story number within epic
- Set when starting new story
- Constant for all work within that story

### TASK
- Task number within story
- Set when starting new task
- Constant for all releases within that task
- Format: `E{epic}:S{story}:T{task}` (e.g., `E9:S21:T03`) - Task numbers are 2-digit (01-99)

### BUILD
- Build number (increments per release within task)
- Starts at 1 for first release of task
- Increments with each subsequent release
- Resets to 1 when moving to new task

---

## Progression

**Working on Epic 9, Story 21, Task 3:**
- `0.9.21.3+1` - First release
- `0.9.21.3+2` - Second release
- `0.9.21.3+3` - Third release

**Moving to Task 4:**
- `0.9.21.4+1` - First release
- `0.9.21.4+2` - Second release

---

## Parallel Development

**Branch Strategy:**

Each epic works in parallel on its own version stream:

**Legacy Epics (1-9):**
- Epic 1: `0.1.S.P` (old format, complete)
- Epic 4: `0.4.S.P` (old format, complete)
- Epic 9: `0.9.S.P` (old format, in progress - will complete with old format)

**New Epics (10+):**
- Epic 10: `0.10.S.T+B` (new format)
- Epic 11: `0.11.S.T+B` (new format)
- Epic 12+: `0.{epic}.S.T+B` (new format)

Where:
- S = Story number
- T = Task number (Epic 10+)
- P = Patch number (Epic 1-9, legacy)
- B = Build number (Epic 10+)

**Merging Strategy:**

When merging epics:
1. Maintain epic numbers in merged code
2. Document epic mapping in CHANGELOG
3. Each epic maintains its own version stream
4. Version ordering is canonical (by version number, not timestamp)

---

## Version File

**Location:** `src/fynd_deals/version.py`

**Format:**
```python
VERSION_STRING = "0.9.21.3+1"
```

**Note:** The `+` character is part of the version string and must be preserved.

**Components:**
```python
VERSION_RC = 0         # Release candidate
VERSION_EPIC = 9      # Epic number
VERSION_STORY = 21    # Story number
VERSION_TASK = 3      # Task number
VERSION_BUILD = 1     # Build number
```

---

## CHANGELOG Format

### Main Changelog (`CHANGELOG.md`)

Each version entry:

```markdown
### [0.9.21.3+1] - 01-12-25
🚀 Feature: Brief description
- Detailed change description
- Additional changes
- See [CHANGELOG_v0.9.21.3+1.md](CHANGELOG_ARCHIVE/CHANGELOG_v0.9.21.3+1.md)
```

**Format:**
- Version: `[RC.EPIC.STORY.TASK+BUILD]`
- Date: `DD-MM-YY` (short date for merge-to-main)
- Link to detailed changelog

### Detailed Changelog (`CHANGELOG_ARCHIVE/CHANGELOG_v{version}.md`)

```markdown
# Changelog v0.9.21.3+1

**Release Date:** 2025-12-01 16:51:30 UTC
**Epic:** Epic 9 - Debug Test Failures & System Issues
**Story:** Story 21 - Versioning and Release Automation
**Task:** Task 3 - Task-level versioning validation
**Type:** 🚀 Feature

## Summary
🚀 Feature: Brief description of changes

## Changes
- Detailed change 1
- Detailed change 2

## Related Tasks
- E9:S21:T03 – Task description

## Technical Details
[Implementation notes, files changed, etc.]
```

**Format:**
- Full timestamp: `YYYY-MM-DD HH:MM:SS UTC` (immutable)
- Epic/Story/Task information
- Detailed change descriptions

---

## Migration from Old Schema

### Old Schema: `RC.EPIC.STORY.PATCH`

**Example:** `0.9.21.19`

### New Schema: `RC.EPIC.STORY.TASK+BUILD`

**Migration Mapping:**
- Old PATCH → New TASK (same number)
- BUILD starts at 1

**Example:** `0.9.21.19` → `0.9.21.19+1`

### Epic Renumbering Strategy

**Problem:** Epic 9 has both old format (100 versions) and new format (1 version), creating confusion.

**Solution:** Complete Epic 9 with old format, then start Epic 10+ with new format exclusively.

**Epic Ranges:**
- **Epic 1-9:** Legacy format (`RC.EPIC.STORY.PATCH`) - Grandfathered, immutable
- **Epic 10+:** New format (`RC.EPIC.STORY.TASK+BUILD`) - Fresh start, clean version space

**Migration Timeline:**
1. Complete Epic 9 work using old format (`0.9.x.x`)
2. Mark Epic 9 as complete
3. Start Epic 10 with new format (`0.10.1.1+1`)
4. All Epic 10+ work uses new format exclusively

**Benefits:**
- Clean separation between legacy and new formats
- No version collisions
- Fresh start for Epic 10+
- Clear branch strategy (`epic/10-*`, `epic/11-*`, etc.)

See [Version Renumbering Strategy](VERSION-RENUMBERING-STRATEGY.md) for complete details.

### Grandfathering

**Existing versions (Epic 1-9):**
- Format: `RC.EPIC.STORY.PATCH`
- Status: Grandfathered, preserved as-is
- Validation: Pass (warnings only)
- Scope: All versions before Epic 10

**New versions (Epic 10+):**
- Format: `RC.EPIC.STORY.TASK+BUILD`
- Status: Full validation required
- Validation: Strict enforcement
- Scope: All versions from Epic 10 onwards

---

## Related Documentation

**Core Policy Documents:**
- **[Versioning Strategy](versioning-strategy.md)** - Complete versioning strategy with forensic traceability
- **[Kanban Governance Policy](../../../knowledge/fynd_deals/Kanban/Kanban Board.md)** - Work item structure

**Implementation:**
- **Version File:** `src/fynd_deals/version.py`
- **Main Changelog:** `CHANGELOG.md`
- **Changelog Archive:** `CHANGELOG_ARCHIVE/`
- **Branch Context Validator:** `scripts/validation/validate_branch_context.py`
- **Changelog Format Validator:** `scripts/validation/validate_changelog_format.py`

---

## Revision History

| Date | Version | Changes |
| --- | --- | --- |
| 2025-12-01 | 1.0 | Initial versioning policy with RC.EPIC.STORY.TASK+BUILD schema |

---

_Last updated: 2025-12-01_

