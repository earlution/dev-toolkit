# Dev-Kit: Kanban + Versioning + Release Workflow Integration Guide

**Status:** Active  
**Version:** 1.0.0  
**Last Updated:** 2025-12-02  
**Related:** Epic 4, Story 3, Task 5

---

## Overview

This guide documents how the three core frameworks—**Kanban**, **Versioning**, and **Release Workflow (RW)**—integrate within the `vibe-dev-kit` repository. It provides dev-kit specific examples, end-to-end flows, troubleshooting, and validation results.

**Integration Type:** Three-way complementary integration
- **Kanban** tracks work items (Epics, Stories, Tasks)
- **Versioning** tracks code releases (`RC.EPIC.STORY.TASK+BUILD`)
- **Release Workflow** automates versioning and Kanban updates

---

## Prerequisites

```yaml
required:
  - Kanban System package installed (`packages/frameworks/kanban/`)
  - Numbering & Versioning package installed (`packages/frameworks/numbering & versioning/`)
  - Workflow Management package installed (`packages/frameworks/workflow mgt/`)
  - .cursorrules configured with RW trigger
  - Epic and Story documents following templates
  - Version file: `src/fynd_deals/version.py`
  - Kanban structure: `KB/PM_and_Portfolio/kanban/`
```

---

## Integration Architecture

### Three-Way Relationship

```yaml
kanban:
  tracks: "Work items (Epics, Stories, Tasks)"
  provides: "Work item structure and traceability"
  location: "KB/PM_and_Portfolio/kanban/"

versioning:
  tracks: "Code releases (versions)"
  provides: "Forensic traceability via RC.EPIC.STORY.TASK+BUILD schema"
  location: "src/fynd_deals/version.py"

release_workflow:
  automates: "Version bumping and Kanban documentation updates"
  provides: "Intelligent agent-driven workflow execution"
  location: "packages/frameworks/workflow mgt/"
```

### Integration Flow

```yaml
end_to_end_flow:
  1: "Developer completes Task (code changes)"
  2: "Developer types 'RW' in AI assistant"
  3: "RW Step 1: Branch Safety Check"
  4: "RW Step 2: Bump Version (reads from version.py, updates TASK/BUILD)"
  5: "RW Step 3: Create Detailed Changelog"
  6: "RW Step 4: Update Main Changelog"
  7: "RW Step 5: Update README (optional)"
  8: "RW Step 6: Auto-update Kanban Docs (adds forensic markers)"
  9: "RW Step 7: Stage Files"
  10: "RW Step 8: Run Validators"
  11: "RW Step 9: Commit Changes"
  12: "RW Step 10: Create Git Tag"
  13: "RW Step 11: Push to Remote"
```

---

## Integration Points

### 1. Kanban → Versioning Integration

**How They Connect:**
- Kanban Tasks map to version `TASK` component
- Kanban Stories map to version `STORY` component
- Kanban Epics map to version `EPIC` component
- Forensic markers link completed work items to versions

**Dev-Kit Example:**
```yaml
kanban_task: "E4:S03:T001"
version: "0.4.3.1+1"
forensic_marker: "✅ COMPLETE (v0.4.3.1+1)"
```

**Validation Status:** ✅ **VALIDATED** (E4:S03:T002)
- Epic/Story mapping: ✅ PASS
- Task mapping: ✅ PASS (fixed in E4:S03:T002)
- Version assignment: ✅ PASS

**Reference:** `KB/PM_and_Portfolio/kanban/epics/Epic-4/stories/Story-003-kanban-versioning-rw-integration/T002-kanban-versioning-validation.md`

---

### 2. Versioning → Release Workflow Integration

**How They Connect:**
- RW Step 2 reads version from `src/fynd_deals/version.py`
- RW Step 2 updates `VERSION_TASK` and `VERSION_BUILD` based on active Task
- RW Step 2 detects Task transitions and resets BUILD to 1
- Validation scripts verify version format and branch alignment

**Dev-Kit Example:**
```python
# src/fynd_deals/version.py
VERSION_RC = 0
VERSION_EPIC = 4      # Epic 4: Kanban Framework
VERSION_STORY = 3     # Story 3: Kanban + Versioning + RW Integration
VERSION_TASK = 7      # Task 7: Address RW → Kanban integration gaps
VERSION_BUILD = 1     # Build 1 (increments per release within task)
VERSION_STRING = f"{VERSION_RC}.{VERSION_EPIC}.{VERSION_STORY}.{VERSION_TASK}+{VERSION_BUILD}"
# Result: "0.4.3.7+1"
```

**Validation Status:** ✅ **VALIDATED** (E4:S03:T003)
- Version file reading: ✅ PASS
- BUILD increment: ✅ PASS
- Task transition handling: ✅ PASS
- EPIC/STORY progression: ⚠️ PARTIAL (not explicitly documented)

**Reference:** `KB/PM_and_Portfolio/kanban/epics/Epic-4/stories/Story-003-kanban-versioning-rw-integration/T003-versioning-rw-validation.md`

---

### 3. Release Workflow → Kanban Integration

**How They Connect:**
- RW Step 6 automatically updates Kanban documentation
- RW Step 6 adds forensic markers to Task/Story checklists
- RW Step 6 updates Epic header with version and summary
- RW Step 6 updates ALL sections (header, checklist, detailed sections)

**Dev-Kit Example:**
```markdown
# Epic-4.md
**Last updated:** 2025-12-02 (v0.4.3.7+1 – Task 7 complete: Address RW → Kanban integration gaps)

## Story Checklist
- [ ] **E4:S03 – Kanban + Versioning + RW Integration** - IN PROGRESS (v0.4.3.7+1)
  - Tasks: T001 ✅ (v0.4.3.1+1), T002 ✅ (v0.4.3.2+2), T003 ✅ (v0.4.3.3+1), T004 ✅ (v0.4.3.4+1), T007 ✅ (v0.4.3.7+1)
```

**Validation Status:** ✅ **VALIDATED** (E4:S03:T004, gaps fixed in E4:S03:T007)
- Epic document updates: ✅ PASS (after fixes)
- Story document updates: ✅ PASS
- "ALL sections" requirement: ✅ PASS (after fixes)
- Forensic marker format: ✅ PASS (after fixes)

**Reference:** 
- `KB/PM_and_Portfolio/kanban/epics/Epic-4/stories/Story-003-kanban-versioning-rw-integration/T004-rw-kanban-validation.md`
- `KB/PM_and_Portfolio/kanban/epics/Epic-4/stories/Story-003-kanban-versioning-rw-integration/T007-gap-resolution-summary.md`

---

## End-to-End Integration Flow

### Complete Workflow Example

**Scenario:** Complete Task E4:S03:T005 (Create dev-kit integration guide)

**Step 1: Work Completion**
- Developer completes Task 5 work (creates integration guide)
- Files modified: `KB/Architecture/Standards_and_ADRs/dev-kit-kanban-versioning-rw-integration.md`

**Step 2: Trigger Release Workflow**
- Developer types `RW` in AI assistant
- AI agent starts Release Workflow execution

**Step 3: RW Step 1 - Branch Safety Check**
- Validates work aligns with current branch (`main`)
- Validates `VERSION_TASK` matches active Task (Task 5)
- ✅ PASS: On `main`, Task 5 is active

**Step 4: RW Step 2 - Bump Version**
- Reads current version: `0.4.3.7+1` (Task 7, Build 1)
- Detects Task transition: Task 7 → Task 5
- Updates `VERSION_TASK` to 5
- Resets `VERSION_BUILD` to 1
- New version: `0.4.3.5+1`

**Step 5: RW Step 3 - Create Detailed Changelog**
- Creates `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.4.3.5+1.md`
- Includes full timestamp, Epic/Story/Task info, summary, changes

**Step 6: RW Step 4 - Update Main Changelog**
- Adds summary entry to `CHANGELOG.md`
- Format: `## [0.4.3.5+1] - 02-12-25`
- Includes link to detailed changelog

**Step 7: RW Step 5 - Update README**
- Updates version badge (if present)
- Updates latest release callout (if present)

**Step 8: RW Step 6 - Auto-update Kanban Docs**
- Updates Epic-4.md header: `**Last updated:** 2025-12-02 (v0.4.3.5+1 – Task 5 complete: Create dev-kit integration guide)`
- Updates Epic-4.md Story Checklist: `- [ ] **E4:S03 – ...** - IN PROGRESS (v0.4.3.5+1)`
- Updates Epic-4.md detailed Story section: Task 5 marked complete
- Updates Story-003.md header: `**Last updated:** ...`, `**Version:** v0.4.3.5+1`
- Updates Story-003.md Task Checklist: `- [x] **E4:S03:T005 – ...** ✅ COMPLETE (v0.4.3.5+1)`
- Updates Story-003.md detailed Task section: `**Status:** ✅ **COMPLETE** (v0.4.3.5+1) - ...`
- Updates Story-003.md footer: `_Last updated: ..._`

**Step 9: RW Step 7 - Stage Files**
- Runs `git add -A` to stage all modified files

**Step 10: RW Step 8 - Run Validators**
- Runs `validate_branch_context.py`: ✅ PASS
- Runs `validate_changelog_format.py`: ✅ PASS

**Step 11: RW Step 9 - Commit Changes**
- Creates commit: `Release v0.4.3.5+1: Task 5 complete: Create dev-kit integration guide\n\nEpic: 4 | Story: 3 | Task: 5`

**Step 12: RW Step 10 - Create Git Tag**
- Creates annotated tag: `v0.4.3.5+1`
- Tag message includes Epic/Story/Task info

**Step 13: RW Step 11 - Push to Remote**
- Pushes `main` branch to origin
- Pushes tag `v0.4.3.5+1` to origin

**Result:**
- Version `v0.4.3.5+1` released
- Task 5 marked complete with forensic marker
- All Kanban docs updated
- Full traceability: Version ↔ Epic/Story/Task ↔ Changelog ↔ Kanban ↔ Git

---

## Dev-Kit Specific Configuration

### File Locations

```yaml
version_file:
  path: "src/fynd_deals/version.py"
  schema: "RC.EPIC.STORY.TASK+BUILD"
  example: "0.4.3.7+1"

kanban_structure:
  root: "KB/PM_and_Portfolio/kanban/"
  epics: "KB/PM_and_Portfolio/kanban/epics/Epic-{epic}.md"
  stories: "KB/PM_and_Portfolio/kanban/epics/Epic-{epic}/stories/Story-{story}-*.md"
  board: "KB/PM_and_Portfolio/kanban/kanban-board.md"
  index: "KB/PM_and_Portfolio/kanban/_index.md"

changelog:
  main: "CHANGELOG.md"
  archive: "KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v{version}.md"

release_workflow:
  docs: "packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md"
  trigger: ".cursorrules RW trigger section"
```

### Version Schema

```yaml
schema: "RC.EPIC.STORY.TASK+BUILD"
components:
  RC: "0 (development) or 1+ (release candidate)"
  EPIC: "Dev-kit Epic number (1-4+)"
  STORY: "Story number within epic"
  TASK: "Task number within story"
  BUILD: "Build number (increments per release within task)"

dev_kit_epics:
  1: "Vibe Dev Kit Core"
  2: "Workflow Management Framework"
  3: "Numbering & Versioning Framework"
  4: "Kanban Framework"

examples:
  - version: "0.4.3.7+1"
    epic: "Epic 4 (Kanban Framework)"
    story: "Story 3 (Kanban + Versioning + RW Integration)"
    task: "Task 7 (Address RW → Kanban integration gaps)"
    build: "Build 1"
```

### Forensic Marker Format

```yaml
canonical_format: "✅ COMPLETE (vRC.E.S.T+B)"
examples:
  - task: "✅ COMPLETE (v0.4.3.7+1)"
  - story: "✅ COMPLETE (v0.4.3.7+1)"
  - epic: "✅ COMPLETE (v0.4.1.6+1)"

locations:
  - Story Task Checklist
  - Story detailed Task sections
  - Epic Story Checklist (with Task list)
  - Epic detailed Story sections
```

---

## Validation Results

### Integration Validation Summary

All three integration points have been validated in dev-kit:

**✅ Kanban → Versioning (E4:S03:T002)**
- Status: ✅ VALIDATED
- Epic/Story mapping: ✅ PASS
- Task mapping: ✅ PASS (fixed critical issue)
- Version assignment: ✅ PASS

**✅ Versioning → RW (E4:S03:T003)**
- Status: ✅ VALIDATED
- Version file reading: ✅ PASS
- BUILD increment: ✅ PASS
- Task transition handling: ✅ PASS
- EPIC/STORY progression: ⚠️ PARTIAL (not explicitly documented)

**✅ RW → Kanban (E4:S03:T004, E4:S03:T007)**
- Status: ✅ VALIDATED (gaps fixed)
- Epic document updates: ✅ PASS
- Story document updates: ✅ PASS
- "ALL sections" requirement: ✅ PASS
- Forensic marker format: ✅ PASS

**Reference Documents:**
- T002: `KB/PM_and_Portfolio/kanban/epics/Epic-4/stories/Story-003-kanban-versioning-rw-integration/T002-kanban-versioning-validation.md`
- T003: `KB/PM_and_Portfolio/kanban/epics/Epic-4/stories/Story-003-kanban-versioning-rw-integration/T003-versioning-rw-validation.md`
- T004: `KB/PM_and_Portfolio/kanban/epics/Epic-4/stories/Story-003-kanban-versioning-rw-integration/T004-rw-kanban-validation.md`
- T007: `KB/PM_and_Portfolio/kanban/epics/Epic-4/stories/Story-003-kanban-versioning-rw-integration/T007-gap-resolution-summary.md`

---

## Troubleshooting

### Common Issues

**Issue 1: Version TASK Component Not Updating**

**Symptoms:**
- All Tasks in a Story use `TASK=1`
- BUILD increments across Tasks instead of resetting

**Solution:**
- Ensure RW Step 2 detects Task transitions
- Verify `VERSION_TASK` in `version.py` matches active Task
- Check RW Step 1 validation passes

**Reference:** T002 validation report (critical issue fixed)

---

**Issue 2: Epic Story Checklist Not Updated**

**Symptoms:**
- Epic Story Checklist missing version markers
- Inconsistency between Story Checklist and detailed sections

**Solution:**
- Ensure RW Step 6 updates ALL sections
- Verify systematic process is followed (read full file, find all references, update all)
- Check forensic marker format is canonical: `✅ COMPLETE (v{version})`

**Reference:** T004 validation report, T007 gap resolution

---

**Issue 3: Forensic Marker Format Inconsistency**

**Symptoms:**
- Some sections use correct format, others missing version markers
- Inconsistent traceability

**Solution:**
- Use canonical format: `✅ COMPLETE (v{version})`
- Ensure all Task status fields include version markers
- Verify RW Step 6 validation checks format

**Reference:** T007 gap resolution

---

**Issue 4: Branch Context Validation Fails**

**Symptoms:**
- `validate_branch_context.py` fails
- Version doesn't match branch context

**Solution:**
- Verify branch name matches Epic number
- Check version EPIC component matches branch Epic
- Ensure version file is correctly formatted

**Reference:** RW Step 1 documentation

---

**Issue 5: Changelog Format Validation Fails**

**Symptoms:**
- `validate_changelog_format.py` fails
- Date format incorrect

**Solution:**
- Use date format: `DD-MM-YY` for main changelog
- Use full timestamp: `YYYY-MM-DD HH:MM:SS UTC` for detailed changelog
- Verify changelog follows Keep a Changelog format

**Reference:** RW Step 3, Step 4 documentation

---

## Best Practices

### 1. Always Use RW for Releases

**DO:**
- Type `RW` in AI assistant after completing work
- Let RW handle version bumping and Kanban updates
- Verify all steps complete successfully

**DON'T:**
- Manually update version file
- Manually update Kanban docs
- Skip validation steps

---

### 2. Maintain Consistency

**DO:**
- Ensure Epic header, Story Checklist, and detailed sections all match
- Use canonical forensic marker format
- Update ALL sections when releasing

**DON'T:**
- Update only some sections
- Use inconsistent forensic marker formats
- Leave sections out of sync

---

### 3. Validate Before Committing

**DO:**
- Run validators before committing
- Fix validation errors before proceeding
- Verify branch context alignment

**DON'T:**
- Skip validation steps
- Commit with validation errors
- Ignore branch context warnings

---

### 4. Document Work Properly

**DO:**
- Create detailed changelog entries
- Include Epic/Story/Task info in commit messages
- Link to related work items

**DON'T:**
- Use generic commit messages
- Skip changelog updates
- Forget to link related work

---

## Related Documentation

### Framework Integration Guides

- **Kanban + Versioning:** `packages/frameworks/kanban/integration/numbering-versioning-integration.md`
- **Kanban + Workflow Management:** `packages/frameworks/kanban/integration/workflow-management-integration.md`

### Dev-Kit Policies

- **Versioning Policy:** `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md`
- **Kanban Governance:** `KB/PM_and_Portfolio/rituals/policy/kanban-governance-policy.md`

### Release Workflow Documentation

- **RW Agent Execution:** `packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md`
- **RW Trigger Section:** `packages/frameworks/workflow mgt/cursorrules-rw-trigger-section.md`

### Validation Reports

- **T002:** Kanban → Versioning validation
- **T003:** Versioning → RW validation
- **T004:** RW → Kanban validation
- **T007:** Gap resolution summary

---

## Version History

- **v1.0.0** (2025-12-02): Initial version created (E4:S03:T005)

---

_End of Dev-Kit Integration Guide_

