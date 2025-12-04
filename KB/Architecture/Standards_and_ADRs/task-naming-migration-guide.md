---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-04T12:01:47Z
expires_at: null
housekeeping_policy: keep
---

# Task Naming Migration Guide

**Date:** 2025-12-03  
**Change:** Task naming format changed from Txxx (3-digit) to Txx (2-digit)  
**Policy:** `packages/frameworks/kanban/policies/kanban-governance-policy.md`

---

## Summary

The Kanban Task naming policy has been updated from 3-digit format (`Txxx`) to 2-digit format (`Txx`) to standardize with Story numbering format (`Sxx`) and simplify the naming convention.

---

## Format Change

**Old Format:**
- `Exx:Sxx:Txxx` (Epic, Story, Task with 3-digit zero padding)
- Example: `E20:S07:T010` = Epic 20, Story 7, Task 10

**New Format:**
- `Exx:Sxx:Txx` (Epic, Story, Task with 2-digit zero padding)
- Example: `E20:S07:T10` = Epic 20, Story 7, Task 10

---

## Migration Strategy

### Backward Compatibility

**Existing Tasks:**
- Existing tasks can keep their current format (backward compatible)
- No requirement to rename existing task files
- No requirement to update existing task references in completed work

**New Tasks:**
- All new tasks MUST use Txx format (2-digit)
- Task files should be named `T01-*.md`, `T02-*.md`, etc.
- Task IDs in commits and references should use Txx format

### Transition Period

**During Transition:**
- Both formats are acceptable for existing tasks
- New tasks should use Txx format
- Documentation should be updated to show Txx format
- Examples should use Txx format

**After Transition:**
- All new work uses Txx format
- Documentation consistently uses Txx format
- Examples use Txx format

---

## What Was Updated

### Policy Documents
- ✅ `packages/frameworks/kanban/policies/kanban-governance-policy.md`
- ✅ `packages/frameworks/numbering & versioning/kanban-governance-policy.md`
- ✅ `KB/PM_and_Portfolio/rituals/policy/kanban-governance-policy.md`

### Templates
- ✅ `packages/frameworks/kanban/templates/STORY_TEMPLATE.md`
- ✅ `packages/frameworks/kanban/templates/EPIC_TEMPLATE.md`

### Examples
- ✅ `packages/frameworks/kanban/examples/Story-33-Example.md`
- ✅ `packages/frameworks/kanban/examples/Epic-4-Example.md`
- ✅ `packages/frameworks/kanban/integration/numbering-versioning-integration.md`
- ✅ `packages/frameworks/kanban/README.md`
- ✅ `packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md`
- ✅ `packages/frameworks/workflow mgt/KB/Documentation/Templates/action-workflow-template.md`
- ✅ `packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-reference.md`
- ✅ `packages/frameworks/workflow mgt/KB/Architecture/Standards_and_ADRs/versioning-strategy.md`
- ✅ `packages/frameworks/kanban/guides/portfolio-kanban-alignment-playbook.md`
- ✅ `packages/frameworks/kanban/FR_BR_INTAKE_AGENT_GUIDE.md`
- ✅ `packages/frameworks/kanban/FR_BR_INTAKE_GUIDE.md`

### Code/Scripts
- ✅ No scripts found that parse Task IDs with Txxx format
- ✅ No validators found that check Task format specifically

---

## Examples

### Task Checklist Format

**Old:**
```markdown
- [x] **E2:S02:T001 – Add CHECK Phase** ✅ COMPLETE (v0.2.2.1+1)
- [ ] **E2:S02:T002 – Add ACT Phase**
```

**New:**
```markdown
- [x] **E2:S02:T01 – Add CHECK Phase** ✅ COMPLETE (v0.2.2.1+1)
- [ ] **E2:S02:T02 – Add ACT Phase**
```

### Task File Naming

**Old:**
```
T001-add-check-phase.md
T002-add-act-phase.md
T010-some-task.md
```

**New:**
```
T01-add-check-phase.md
T02-add-act-phase.md
T10-some-task.md
```

### Commit Message References

**Old:**
```
Release v0.2.2.1+1: E2:S02:T001: Add CHECK Phase
```

**New:**
```
Release v0.2.2.1+1: E2:S02:T01: Add CHECK Phase
```

---

## Impact on Version Numbers

**No Impact:**
- Version numbers use numeric Task component: `RC.EPIC.STORY.TASK+BUILD`
- Task component in version is numeric (e.g., `0.2.2.1+1` = Task 1)
- Task naming format (Txx vs Txxx) does not affect version numbers
- Version numbers remain unchanged

**Example:**
- Task T01 (new format) = Version `0.2.2.1+1` (Task component = 1)
- Task T001 (old format) = Version `0.2.2.1+1` (Task component = 1)
- Both refer to the same Task number, just different display format

---

## Best Practices

1. **Use Txx Format for New Tasks:**
   - All new tasks should use 2-digit format
   - Task files: `T01-*.md`, `T02-*.md`, etc.
   - Task IDs: `E2:S02:T01`, `E2:S02:T02`, etc.

2. **Maintain Existing Tasks:**
   - Existing tasks can keep their format
   - No need to rename existing files
   - No need to update historical references

3. **Update Documentation:**
   - New documentation should use Txx format
   - Examples should use Txx format
   - Templates should use Txx format

4. **Consistency:**
   - Use consistent format within a story
   - Use consistent format in documentation
   - Use consistent format in examples

---

## References

- **Kanban Policy:** `packages/frameworks/kanban/policies/kanban-governance-policy.md`
- **Versioning Policy:** `packages/frameworks/numbering & versioning/kanban-governance-policy.md`
- **Dev-Kit Policy:** `KB/PM_and_Portfolio/rituals/policy/kanban-governance-policy.md`
- **Task T07:** `KB/PM_and_Portfolio/kanban/epics/Epic-2/stories/Story-002-pdca-integration-into-release-workflow/T07-implement-task-naming-change.md`
- **Task T08:** `KB/PM_and_Portfolio/kanban/epics/Epic-2/stories/Story-002-pdca-integration-into-release-workflow/T08-update-kanban-docs-to-txx-standard.md`

---

## Questions?

If you have questions about the migration or need clarification, refer to:
- Task T07: Implementation details
- Task T08: Documentation updates
- Kanban policy documents: Current standards

