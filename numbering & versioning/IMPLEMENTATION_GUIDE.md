# Implementation Guide: Numbering & Versioning Strategies

**Purpose:** This guide explains how to implement Confidentia's numbering and versioning strategies in a different project.

**Target Audience:** Project maintainers, engineering leads, and developers setting up versioning and numbering systems.

---

## Overview

This guide walks you through implementing:
1. **Versioning Schema** (`RC.EPIC.STORY.TASK+BUILD`)
2. **Forensic Traceability System**
3. **Numbering Policies** (for work items and domain objects)
4. **Integration with Release Workflow**

---

## Step 1: Understand the Core Concepts

### Versioning Schema: `RC.EPIC.STORY.TASK+BUILD`

**Format:** `RC.EPIC.STORY.TASK+BUILD`

- **RC (Release Candidate):** `0` = development, `1+` = release candidate
- **EPIC:** Epic/workstream number (e.g., `20`)
- **STORY:** Story number within epic (e.g., `11`)
- **TASK:** Task number within story (e.g., `15`)
- **BUILD:** Build number (increments per release within task)

**Example:** `0.20.11.3+1` = Development, Epic 20, Story 11, Task 3, Build 1

### Key Principles

1. **Version numbers are canonical** - They determine ordering, not timestamps
2. **Parallel development support** - Each epic maintains its own version stream
3. **Forensic traceability** - Complete accountability through version ↔ work items ↔ changelogs
4. **Immutability** - Historical metadata is preserved as-is

---

## Step 2: Customize for Your Project

### 2.1 Adapt the Schema

**If you don't use Epic/Story/Task structure:**

You can adapt the schema to match your work item hierarchy:

- **Option A:** Use your existing hierarchy (e.g., `RC.MILESTONE.FEATURE.TASK+BUILD`)
- **Option B:** Simplify (e.g., `RC.MAJOR.MINOR.PATCH+BUILD` for semantic versioning)
- **Option C:** Flatten (e.g., `RC.EPIC.STORY+BUILD` if you don't have tasks)

**Example Adaptation:**
```
Original: RC.EPIC.STORY.TASK+BUILD
Adapted:  RC.MILESTONE.FEATURE.TASK+BUILD
          RC.MAJOR.MINOR.PATCH+BUILD
          RC.EPIC.STORY+BUILD
```

### 2.2 Define Your Work Item Structure

**Map your work items to the version schema:**

| Your Structure | Maps To | Example |
|--------------|---------|---------|
| Project/Milestone | EPIC | `0.20.x.x+x` |
| Feature/User Story | STORY | `0.20.11.x+x` |
| Task/Sub-task | TASK | `0.20.11.3+x` |
| Release/Build | BUILD | `0.20.11.3+1` |

**Document this mapping** in your versioning policy document.

### 2.3 Set Version File Location

**Standard location:** `src/<project>/version.py`

**Customize:**
- Update path in `versioning-policy.md`
- Update any scripts that read the version file
- Update CI/CD pipelines that reference the version

**Example:**
```python
# src/myproject/version.py
__version__ = "0.20.11.3+1"
```

---

## Step 3: Set Up Version File

### 3.1 Create Version File

Create `src/<project>/version.py`:

```python
"""Version information for the project."""
__version__ = "0.1.0.0+1"  # Start with your first version
```

### 3.2 Make Version Accessible

**Option A: Import in `__init__.py`**
```python
# src/myproject/__init__.py
from .version import __version__
```

**Option B: Package-level access**
```python
# src/myproject/version.py
__version__ = "0.1.0.0+1"

# Usage: from myproject.version import __version__
```

### 3.3 Update Version in Release Workflow

Ensure your release workflow updates this file:
- Read current version
- Determine next version based on work items
- Update version file
- Commit with versioned message

---

## Step 4: Set Up Changelog System

### 4.1 Create Changelog Structure

**Main changelog:** `CHANGELOG.md` (summary entries)

**Detailed changelogs:** `CHANGELOG_ARCHIVE/CHANGELOG_v{version}.md`

**Directory structure:**
```
project-root/
├── CHANGELOG.md
└── CHANGELOG_ARCHIVE/
    ├── CHANGELOG_v0.1.0.0+1.md
    ├── CHANGELOG_v0.1.0.0+2.md
    └── ...
```

### 4.2 Define Changelog Format

**Main Changelog Entry:**
```markdown
### [0.20.11.3+1] - 01-12-25
🚀 Feature: Brief description
- See [CHANGELOG_v0.20.11.3+1.md](CHANGELOG_ARCHIVE/CHANGELOG_v0.20.11.3+1.md)
```

**Detailed Changelog Template:**
```markdown
# Changelog v0.20.11.3+1

**Release Date:** 2025-12-01 16:51:30 UTC
**Epic:** Epic 20 - Maintenance
**Story:** Story 11 - Versioning and Release Automation
**Task:** Task 3 - Task-level versioning validation
**Type:** 🚀 Feature

## Summary
🚀 Feature: Brief description of changes

## Changes
- Detailed change 1
- Detailed change 2

## Related Tasks
- E20:S11:T003 – Task description

## Technical Details
[Implementation notes, files changed, etc.]
```

### 4.3 Implement Two-Layer Timestamp System

**Layer 1: Main Changelog (`CHANGELOG.md`)**
- Format: `DD-MM-YY` (e.g., `01-12-25`)
- Purpose: Quick reference for merge-to-main date
- Can be updated if merge date changes

**Layer 2: Detailed Changelog (`CHANGELOG_vX.Y.Z.md`)**
- Format: `YYYY-MM-DD HH:MM:SS UTC` (e.g., `2025-12-01 16:51:30 UTC`)
- Purpose: Forensic-level precision
- **IMMUTABLE** - Never edit after creation

---

## Step 5: Create Validation Scripts

### 5.1 Branch Context Validator

**Purpose:** Ensure version matches branch/work item

**Key checks:**
- Version number matches current work item
- Branch name aligns with epic/workstream
- No cross-epic contamination

**Example structure:**
```python
# scripts/validation/validate_branch_context.py
def validate_branch_context():
    current_branch = get_current_branch()
    current_version = get_current_version()

    # Extract epic from branch name
    branch_epic = extract_epic_from_branch(current_branch)

    # Extract epic from version
    version_epic = extract_epic_from_version(current_version)

    if branch_epic != version_epic:
        raise ValidationError("Version epic doesn't match branch epic")

    # Additional validations...
```

### 5.2 Changelog Format Validator

**Purpose:** Ensure changelog format compliance

**Key checks:**
- Full timestamp format in detailed changelogs
- Proper version number format
- Required fields present
- Links are valid

**Example structure:**
```python
# scripts/validation/validate_changelog_format.py
def validate_changelog_format():
    changelog_file = get_latest_changelog()

    # Check timestamp format
    if not has_full_timestamp(changelog_file):
        raise ValidationError("Changelog must have full timestamp")

    # Check version format
    if not matches_version_schema(changelog_file):
        raise ValidationError("Version doesn't match schema")

    # Additional validations...
```

### 5.3 Integrate with Pre-commit Hooks

**Add to `.pre-commit-config.yaml`:**
```yaml
repos:
  - repo: local
    hooks:
      - id: validate-branch-context
        name: Validate Branch Context
        entry: python scripts/validation/validate_branch_context.py
        language: system
        pass_filenames: false

      - id: validate-changelog-format
        name: Validate Changelog Format
        entry: python scripts/validation/validate_changelog_format.py
        language: system
        pass_filenames: false
```

---

## Step 6: Integrate with Release Workflow

### 6.1 Define Release Workflow Steps

**Standard 10-step workflow:**
1. Bump Version
2. Create Detailed Changelog
3. Update Main Changelog
4. Update README
5. Update Documentation
6. Stage Files
7. Run Validators
8. Commit Changes
9. Create Git Tag
10. Push to Remote

**Customize for your project:**
- Add/remove steps as needed
- Integrate with your CI/CD pipeline
- Add project-specific validations

### 6.2 Version Bumping Logic

**Determine next version:**
```python
def determine_next_version(current_version, work_item):
    """
    Determine next version based on current version and work item.

    Args:
        current_version: Current version string (e.g., "0.20.11.3+1")
        work_item: Dict with epic, story, task info

    Returns:
        Next version string
    """
    rc, epic, story, task, build = parse_version(current_version)

    # If working on new task, reset build to 1
    if (epic != work_item['epic'] or
        story != work_item['story'] or
        task != work_item['task']):
        build = 1
    else:
        build += 1

    return f"{rc}.{work_item['epic']}.{work_item['story']}.{work_item['task']}+{build}"
```

### 6.3 Git Tagging

**Create annotated tags:**
```bash
git tag -a v0.20.11.3+1 -m "Release v0.20.11.3+1: Description"
```

**Tag format:** `v{version}` (e.g., `v0.20.11.3+1`)

**Note:** The `+` character in version numbers may need escaping in some contexts.

---

## Step 7: Set Up Numbering Policies

### 7.1 Work Item Numbering

**Format:** `E{epic}S{story}T{task}`

**Examples:**
- `E20S11T003` = Epic 20, Story 11, Task 3
- `E4S16T001` = Epic 4, Story 16, Task 1

**Rules:**
- Zero-pad task numbers (e.g., `T001`, `T010`, `T100`)
- Never reuse IDs
- IDs are immutable once assigned

### 7.2 Domain Object Numbering (if applicable)

**For learning outcomes or similar:**
- Define numbering schema (e.g., `J277-1.1`, `J277-1.2`)
- Document in `learning-outcome-numbering-policy.md` (or equivalent)
- Ensure uniqueness and traceability

**Customize for your domain:**
- Adapt schema to your object types
- Define numbering rules
- Document in policy file

---

## Step 8: Documentation Updates

### 8.1 Update Project README

**Add version badge:**
```markdown
[![Version](https://img.shields.io/badge/version-0.20.11.3+1-blue)](https://github.com/org/repo/releases)
```

**Add latest release callout:**
```markdown
**🎉 Latest Release: v0.20.11.3+1** - 🚀 Feature: Brief description
```

### 8.2 Create Policy Documents

**Copy and customize:**
1. `versioning-policy.md` - Update schema, examples, file paths
2. `versioning-strategy.md` - Update traceability grid, examples
3. `kanban-governance-policy.md` - Update work item structure

### 8.3 Copy and Customize Templates

**Copy templates to your project:**
1. Copy `EPIC_TEMPLATE.md` to your templates directory (e.g., `docs/templates/`)
2. Copy `STORY_TEMPLATE.md` to your templates directory
3. Update paths in templates (e.g., story references)
4. Customize terminology if your work items differ from Epic/Story/Task
5. Update version schema format if you've adapted it

**Update references:**
- File paths
- Project names
- Work item terminology
- CI/CD integration points

### 8.3 Document Integration Points

**Create integration guide:**
- How versioning integrates with your CI/CD
- How to update version in your release process
- How to query version programmatically
- How to generate changelogs automatically

---

## Step 9: Testing and Validation

### 9.1 Test Version Bumping

**Test scenarios:**
- New task in same story
- New story in same epic
- New epic
- Build increment within task

**Example test:**
```python
def test_version_bumping():
    # Test build increment
    assert next_version("0.20.11.3+1", {"epic": 20, "story": 11, "task": 3}) == "0.20.11.3+2"

    # Test new task
    assert next_version("0.20.11.3+5", {"epic": 20, "story": 11, "task": 4}) == "0.20.11.4+1"

    # Test new story
    assert next_version("0.20.11.3+2", {"epic": 20, "story": 12, "task": 1}) == "0.20.12.1+1"
```

### 9.2 Test Validators

**Test validation scripts:**
- Valid versions pass
- Invalid versions fail
- Branch context matches
- Changelog format correct

### 9.3 Test Release Workflow

**End-to-end test:**
1. Start with version `0.1.0.0+1`
2. Execute release workflow
3. Verify version bumped correctly
4. Verify changelogs created
5. Verify git tag created
6. Verify validators pass

---

## Step 10: Migration Strategy (if applicable)

### 10.1 Existing Projects

**If you have existing versions:**

**Option A: Grandfather existing versions**
- Keep existing version scheme
- Apply new scheme to new work
- Document mapping between old and new

**Option B: Migrate to new scheme**
- Map existing versions to new schema
- Update all references
- Create migration changelog entry

**Example migration:**
```
Old: v1.2.3
New: 0.1.2.3+1 (assuming Epic 1, Story 2, Task 3, Build 1)
```

### 10.2 Legacy Changelogs

**Preserve existing changelogs:**
- Don't modify historical entries
- Grandfather old format
- Apply new format going forward

---

## Step 11: CI/CD Integration

### 11.1 Version Validation in CI

**Add to CI pipeline:**
```yaml
# .github/workflows/ci.yml
- name: Validate Version
  run: python scripts/validation/validate_branch_context.py

- name: Validate Changelog
  run: python scripts/validation/validate_changelog_format.py
```

### 11.2 Automatic Version Tagging

**On release:**
```yaml
- name: Create Release Tag
  run: |
    VERSION=$(python -c "from myproject.version import __version__; print(__version__)")
    git tag -a "v${VERSION}" -m "Release ${VERSION}"
    git push origin "v${VERSION}"
```

### 11.3 Changelog Generation

**Optional: Auto-generate changelogs from commits:**
- Use conventional commits
- Parse commit messages
- Generate changelog entries
- Still require manual review/editing

---

## Step 12: Team Adoption

### 12.1 Training

**Educate team on:**
- Version schema and format
- When to bump version
- How to create changelogs
- How to use validators

### 12.2 Documentation

**Create quick reference:**
- Version format cheat sheet
- Common scenarios
- Troubleshooting guide
- FAQ

### 12.3 Tooling

**Provide tools:**
- Version bumping script
- Changelog template generator
- Validation scripts
- Release workflow automation

---

## Customization Checklist

Use this checklist to ensure you've customized everything for your project:

- [ ] Updated version schema to match your work item structure
- [ ] Updated version file location
- [ ] Updated changelog directory structure
- [ ] Updated file paths in policy documents
- [ ] Updated work item terminology
- [ ] Created validation scripts
- [ ] Integrated with pre-commit hooks
- [ ] Integrated with CI/CD pipeline
- [ ] Updated README with version badge
- [ ] Created project-specific documentation
- [ ] Tested version bumping logic
- [ ] Tested validators
- [ ] Tested release workflow end-to-end
- [ ] Trained team on new system
- [ ] Created quick reference guide

---

## Common Pitfalls and Solutions

### Pitfall 1: Version Format Mismatch

**Problem:** Version doesn't match schema

**Solution:** Use validation scripts, enforce in CI/CD

### Pitfall 2: Missing Changelog Timestamps

**Problem:** Changelog missing full timestamp

**Solution:** Use template, validate in pre-commit hook

### Pitfall 3: Version Not Updated

**Problem:** Code changes but version stays same

**Solution:** Make version bump mandatory in release workflow

### Pitfall 4: Cross-Epic Contamination

**Problem:** Work from one epic gets versioned under another

**Solution:** Branch context validation, clear branch naming

### Pitfall 5: Immutability Violations

**Problem:** Editing historical changelogs

**Solution:** Document immutability rules, use read-only permissions

---

## Support and Resources

### Key Documents

- `versioning-policy.md` - Schema definition
- `versioning-strategy.md` - Complete strategy
- `kanban-governance-policy.md` - Work item structure
- `learning-outcome-numbering-policy.md` - Domain numbering (if applicable)

### Related Systems

- Release Workflow - Automated implementation
- Kanban System - Work item tracking
- CI/CD Pipeline - Automated validation

---

## Next Steps

1. **Review** all policy documents
2. **Customize** schema and terminology for your project
3. **Implement** version file and changelog structure
4. **Create** validation scripts
5. **Integrate** with release workflow
6. **Test** end-to-end
7. **Train** team
8. **Document** project-specific details

---

**Last Updated:** 2025-12-01
**Based on:** Confidentia Project Versioning & Numbering Policies
