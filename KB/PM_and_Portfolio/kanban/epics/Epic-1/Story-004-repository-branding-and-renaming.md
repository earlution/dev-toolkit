---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-07T12:00:00Z
expires_at: null
housekeeping_policy: keep
---

# Story 004 – Repository Branding and Renaming

**Status:** TODO  
**Priority:** MEDIUM  
**Estimated Effort:** [TBD]  
**Created:** 2025-12-07  
**Last updated:** 2025-12-07 (v0.1.4.0+0 – Story created)  
**Version:** v0.1.4.0+0  
**Code:** E1S04

---

## Task Checklist

- [ ] **E1:S04:T01 – Plan repository rename from vibe-dev-kit to ai-dev-kit** - TODO
- [ ] **E1:S04:T02 – Plan repository rename from ai-dev-kit to head-first-ai-dev-kit (conditional on O'Reilly acceptance)** - TODO

---

## Overview

This story plans and executes the repository renaming strategy to align with the book branding. The repository will be renamed in stages:
1. **Phase 1:** `vibe-dev-kit` → `ai-dev-kit` (immediate alignment with book focus)
2. **Phase 2:** `ai-dev-kit` → `head-first-ai-dev-kit` (conditional on O'Reilly book acceptance)

This ensures the repository name aligns with "Head First AI-Assisted Development" book branding while maintaining continuity for existing users.

---

## Goal

Plan and execute repository renaming to align with book branding, ensuring minimal disruption to existing users and clear migration paths.

---

## Tasks

### E1:S04:T01 – Plan repository rename from vibe-dev-kit to ai-dev-kit

**Input:** Current repository structure, all references to `vibe-dev-kit`  
**Deliverable:** Comprehensive rename plan and impact analysis  
**Dependencies:** None  
**Blocker:** None

**Problem Statement:**
The repository is currently named `vibe-dev-kit`, but the book focus has shifted to "Head First AI-Assisted Development". To align branding, we need to rename to `ai-dev-kit` as an intermediate step. This requires identifying all references, planning the migration, and ensuring continuity.

**Approach:**

1. **Inventory All References:**
   - Search codebase for all occurrences of `vibe-dev-kit`
   - Identify file paths, URLs, documentation references
   - List external references (GitHub, documentation sites, etc.)
   - Catalog CLI tool names, package names, import paths
   - Document all configuration files referencing the name

2. **Impact Analysis:**
   - **Breaking Changes:** Identify what will break for existing users
   - **Migration Path:** Define how users migrate from old to new name
   - **Documentation Updates:** List all docs needing updates
   - **External Dependencies:** Check if other projects reference this repo
   - **GitHub Settings:** Repository name, URLs, webhooks, etc.

3. **Create Rename Plan:**
   - **Phase 1 Steps:** Detailed step-by-step rename procedure
   - **Rollback Plan:** How to revert if issues arise
   - **Communication Plan:** How to notify users of the change
   - **Timeline:** When to execute the rename
   - **Testing Plan:** How to verify rename was successful

4. **Document Migration Guide:**
   - Instructions for users updating their projects
   - Update commands for Git remotes
   - Update instructions for framework dependencies
   - CLI tool update procedures

**Deliverables:**
- `KB/Architecture/Standards_and_ADRs/repository-rename-plan-ai-dev-kit.md` - Comprehensive rename plan
- `KB/Architecture/Standards_and_ADRs/repository-rename-impact-analysis.md` - Impact analysis document
- `KB/Documentation/User_Docs/repository-rename-migration-guide.md` - User migration guide
- Inventory of all references to `vibe-dev-kit`

**Success Criteria:**
- All references to `vibe-dev-kit` identified and cataloged
- Impact analysis complete with breaking changes documented
- Rename plan includes all steps, rollback, and testing
- Migration guide provides clear instructions for users
- Plan ready for execution

**Related Work:**
- Epic 6 (Framework Management) - Framework dependency references
- Epic 5 (Documentation Management) - Documentation updates
- Epic 9 (Book Related Work) - Book branding alignment

---

### E1:S04:T02 – Plan repository rename from ai-dev-kit to head-first-ai-dev-kit (conditional on O'Reilly acceptance)

**Input:** Repository rename plan from T01, O'Reilly book acceptance confirmation  
**Deliverable:** Conditional rename plan for O'Reilly branding alignment  
**Dependencies:** E1:S04:T01, O'Reilly book acceptance  
**Blocker:** O'Reilly book acceptance

**Problem Statement:**
If the book is accepted by O'Reilly for the "Head First" series, the repository should be renamed to `head-first-ai-dev-kit` to align with Head First series naming conventions (following patterns like `head-first-csharp`, `head-first-git`, etc.). This requires planning the second rename phase.

**Approach:**

1. **Review Phase 1 Rename:**
   - Assess what worked well in Phase 1 rename
   - Identify any issues or improvements needed
   - Update rename procedures based on Phase 1 experience

2. **Plan Phase 2 Rename:**
   - Inventory all references to `ai-dev-kit`
   - Identify additional considerations for "Head First" branding
   - Plan GitHub template repository setup (if applicable)
   - Consider O'Reilly-specific requirements or guidelines

3. **Create Conditional Plan:**
   - Detailed rename procedure for Phase 2
   - Communication plan for O'Reilly announcement
   - Update book references and documentation
   - Plan for template repository setup (if readers should use as template)

4. **Document O'Reilly Alignment:**
   - How the rename aligns with Head First series conventions
   - Repository description and branding updates
   - Template repository configuration (if applicable)
   - Book-repo integration documentation

**Deliverables:**
- `KB/Architecture/Standards_and_ADRs/repository-rename-plan-head-first-ai-dev-kit.md` - Phase 2 rename plan
- `KB/Architecture/Standards_and_ADRs/oreilly-branding-alignment.md` - O'Reilly branding alignment guide
- Updated migration guide for Phase 2
- Template repository setup guide (if applicable)

**Success Criteria:**
- Phase 2 rename plan complete and ready for execution
- O'Reilly branding alignment documented
- Template repository setup planned (if applicable)
- All documentation updated for Head First branding
- Plan ready for execution upon O'Reilly acceptance

**Related Work:**
- E1:S04:T01 (Phase 1 rename) - Foundation for Phase 2
- Epic 9 (Book Related Work) - O'Reilly book acceptance
- Epic 5 (Documentation Management) - Documentation updates

**Note:** This task is conditional on O'Reilly book acceptance. Do not execute until confirmation.

---

## Dependencies

**Blocks:**
- None (planning task)

**Blocked By:**
- None

**Coordinates With:**
- Epic 6 (Framework Management) - Framework dependency references
- Epic 5 (Documentation Management) - Documentation updates
- Epic 9 (Book Related Work) - Book branding and O'Reilly acceptance

---

## References

- `KB/PM_and_Portfolio/kanban/epics/Epic-1/Epic-1.md`
- `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md`
- `KB/PM_and_Portfolio/rituals/policy/kanban-governance-policy.md`

---

