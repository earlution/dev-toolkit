# Numbering & Versioning Policies

**Portable Package:** This directory contains all policy documents relating to numbering and versioning strategies. These documents can be adapted for use in other projects.

**Source:** Originally developed for the Confidentia project, refined and enhanced in fynd.deals (Epic 15, Story 1).  
**Last Updated:** 2025-12-02  
**Version:** 2.0.0 (includes Epic renumbering strategy, epic branch workflow)

---

This directory contains all policy documents relating to numbering and versioning strategies.

## Package Structure

This package is designed to be **portable and customizable** for use in other projects. All documents include:
- Portable package headers
- Customization notes
- Relative cross-references
- Example paths marked for customization

**Start Here:** Read `PACKAGE_OVERVIEW.md` for complete package structure and usage scenarios.

## Contents

### Versioning Policies

1. **`versioning-policy.md`**
   - Defines the semantic versioning schema: `RC.EPIC.STORY.TASK+BUILD`
   - Explains version progression rules
   - Documents parallel development support
   - Defines version file location and CHANGELOG format
   - Includes Epic renumbering strategy (Epic 1-9 legacy, Epic 10+ new format)

2. **`versioning-strategy.md`**
   - Complete versioning strategy with forensic traceability
   - Canonical ordering principles (version numbers, not timestamps)
   - Two-layer timestamp system (short dates vs. full timestamps)
   - Immutability rules for historical metadata
   - Handling of legacy/pre-policy releases

### Numbering Policies

3. **`learning-outcome-numbering-policy.md`**
   - Policy governing numbering for learning outcomes
   - Defines how learning outcomes are numbered and structured
   - *(Domain-specific, adaptable to other numbering systems)*

4. **`set2-numbering-schema.md`**
   - Numbering schema decisions for SET2 learning outcomes
   - Specific implementation details for SET2 system
   - *(Reference example, adaptable)*

### Related Governance

5. **`kanban-governance-policy.md`**
   - Kanban governance policy that includes versioning requirements
   - Defines work-item types (Epic → Story → Task) and how they map to version schema
   - Links versioning to Kanban workflow and release process

### Templates

6. **`EPIC_TEMPLATE.md`**
   - Template for creating epic documents
   - Includes version schema fields (`RC.X.S.T+B`)
   - Includes task numbering format (`EXX:SYY:T001`)
   - Ready to customize for your project

7. **`STORY_TEMPLATE.md`**
   - Template for creating story documents
   - Includes version fields and task checklists
   - Includes version markers for completed tasks
   - Ready to customize for your project

### Implementation Guide

8. **`IMPLEMENTATION_GUIDE.md`**
   - Step-by-step guide for implementing these strategies in a different project
   - Customization instructions
   - Testing and validation strategies
   - CI/CD integration patterns

## Core Versioning Schema

**Format:** `RC.EPIC.STORY.TASK+BUILD`

- **RC:** Release Candidate (0 = development, 1+ = release candidate)
- **EPIC:** Epic number (e.g., 15)
- **STORY:** Story number within epic (e.g., 1)
- **TASK:** Task number within story (e.g., 4)
- **BUILD:** Build number (increments per release within task)

**Example:** `0.15.1.4+2` = Development, Epic 15, Story 1, Task 4, Build 2

## Epic Renumbering Strategy

**Problem:** Having both old (`RC.EPIC.STORY.PATCH`) and new (`RC.EPIC.STORY.TASK+BUILD`) version formats within the same epic creates confusion and version collisions.

**Solution:** Complete legacy epics with old format, then start new epics with new format exclusively.

**Epic Ranges:**
- **Epic 1-9:** Legacy format (`RC.EPIC.STORY.PATCH`) - Grandfathered, immutable
- **Epic 10+:** New format (`RC.EPIC.STORY.TASK+BUILD`) - Fresh start, clean version space

**Benefits:**
- Clean separation between legacy and new formats
- No version collisions
- Fresh start for new epics
- Clear branch strategy (`epic/10-*`, `epic/11-*`, etc.)

## Key Principles

1. **Version numbers are canonical** - They determine ordering, not timestamps
2. **Parallel epic development** - Each epic maintains its own version stream
3. **Forensic traceability** - Complete accountability through version ↔ epic/story/task ↔ changelogs ↔ kanban markers
4. **Immutability** - Historical metadata is preserved as-is
5. **Epic branch workflow** - Always work on epic branches (`epic/{n}-...`), never directly on `main`

## Related Documentation

These policies are part of a larger system of interconnected documents:
- **Cursor Rules** (`.cursorrules`) - Fundamental system rules that enforce versioning requirements *(Project-specific)*
- **Release Workflow Reference** - Automated implementation of versioning schema *(see workflow mgt package)*
- **Release Workflow Agent Execution Guide** - Step-by-step agent execution patterns *(see workflow mgt package)*

**Note:** Some references point to project-specific files. When implementing in other projects, see `IMPLEMENTATION_GUIDE.md` for customization instructions.

## Usage

These documents should be referenced when:
- Creating new epics, stories, or tasks
- Determining version numbers for releases
- Understanding version progression rules
- Implementing versioning in other projects
- Setting up numbering systems for learning outcomes or other domain objects
- Planning epic renumbering strategies

---

**Last Updated:** 2025-12-02  
**Source Location:** `docs/fynd_deals/_design/versioning/` (fynd.deals)  
**Package Version:** 2.0.0
