# Changelog

All notable changes to this project will be documented in this file.

The format is inspired by **Keep a Changelog** ([`https://github.com/olivierlacan/keep-a-changelog`](https://github.com/olivierlacan/keep-a-changelog))  
and this project adheres to the **`RC.EPIC.STORY.TASK+BUILD`** versioning scheme described in the dev-kit versioning policy.

---

## [Unreleased]

### Planned

- Additional framework packages (architecture, testing, documentation)  
- More examples and templates for adopting the dev kit in real projects  
- Further integration between Kanban, Versioning, and Workflow frameworks

---

## [0.4.1.1+5] - 02-12-25

📚 Documentation: Task 4 complete - Align dev-kit Kanban templates with updated governance

### Added

- Enhanced **EPIC_TEMPLATE.md** with governance alignment notes:
  - "ALL sections" update requirement reminders
  - Forensic marker format notes (`✅ COMPLETE (vRC.E.S.T+B)`)
  - Consistency check reminders
  - Story Checklist as SINGLE SOURCE OF TRUTH emphasis
- Enhanced **STORY_TEMPLATE.md** with governance alignment notes:
  - "ALL sections" update requirement reminders
  - Forensic marker format notes
  - Consistency check reminders

### Notes

- Templates: `packages/frameworks/kanban/templates/EPIC_TEMPLATE.md` and `STORY_TEMPLATE.md`
- See `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.4.1.1+5.md` for full details

---

## [0.4.1.1+4] - 02-12-25

📚 Documentation: Task 3 complete - Update dev-kit Kanban governance policy as canonical SoT

### Added

- Added **9 Operational Principles sections** to framework Kanban governance policy:
  - Atomic Release Workflow Behaviour
  - "ALL Sections" Update Requirement
  - Accessibility Constraints
  - Forensic Marker Standardization
  - Consistency Requirements
  - Review Schedules
  - Maintenance Responsibilities
  - Escalation Procedures
  - Mandatory TODO Tracking
- Enhanced dev-kit local policy to explicitly reference framework as canonical SoT

### Notes

- Framework policy: `packages/frameworks/kanban/policies/kanban-governance-policy.md` (now comprehensive canonical SoT)
- See `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.4.1.1+4.md` for full details

---

## [0.4.1.1+3] - 02-12-25

📚 Documentation: Task 2 complete - Ingest findings from fynd.deals Epic 15 Kanban work

### Added

- Created **findings document** extracting 7 reusable Kanban patterns from framework packages
- Identified patterns already in framework vs. missing from policy
- Provided 9 high-priority recommendations for updating Kanban governance policy

### Notes

- Findings document: `KB/PM_and_Portfolio/kanban/epics/Epic-4/stories/Story-001-dev-kit-kanban-implementation/T002-fynd-deals-epic15-kanban-findings.md`
- See `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.4.1.1+3.md` for full details

---

## [0.4.1.1+2] - 02-12-25

📚 Documentation: Task 1 complete - Gap analysis of dev-kit Kanban policies and templates

### Added

- Created **gap analysis report** comparing dev-kit Kanban policies and templates with framework
- Identified 7 critical gaps (atomic RW behaviour, "ALL sections" requirement, accessibility constraints, etc.)
- Identified template gaps and dev-kit policy gaps

### Notes

- Gap analysis: `KB/PM_and_Portfolio/kanban/epics/Epic-4/stories/Story-001-dev-kit-kanban-implementation/T001-gap-analysis-report.md`
- See `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.4.1.1+2.md` for full details

---

## [0.3.1.6+1] - 02-12-25

📚 Documentation: Task 6 complete - Cursorrules abstracted (removed hardcoded version numbers)

### Changed

- Abstracted **cursorrules-rw-trigger-section.md** to use template placeholders instead of hardcoded paths and versions
- Replaced hardcoded version examples with generic schema calculation examples
- Replaced project-specific paths with template placeholders (`{project}`, `{kanban_path}`, `{scripts_path}`)
- Added version calculation examples and customization instructions

### Notes

- Cursorrules template is now fully abstract and reusable across projects
- All examples teach the pattern rather than listing stale instances
- References canonical policy documents instead of duplicating schema details
- See `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.3.1.6+1.md` for full details

---

## [0.3.1.5+1] - 02-12-25

📚 Documentation: Task 5 complete - Consumption pattern documented for other projects

### Added

- Added **consumption pattern documentation** to README and IMPLEMENTATION_GUIDE
- Documented copy vs reference pattern (CRITICAL: copy, don't reference)
- Explained customization boundaries and update process
- Added example setup workflows

### Changed

- Enhanced README with comprehensive consumption section
- Enhanced IMPLEMENTATION_GUIDE with consumption pattern section
- Clarified framework as single source of truth

### Notes

- Projects MUST copy framework files (not reference them) for independence and customization
- Framework remains canonical SoT while projects adapt for their context
- See `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.3.1.5+1.md` for full details

---

## [0.3.1.4+1] - 02-12-25

📚 Documentation: Task 4 complete - Version file and CHANGELOG aligned with framework

### Changed

- Enhanced **version file** (`src/fynd_deals/version.py`) with comprehensive documentation and validation notes
- Verified **CHANGELOG.md** format alignment with framework conventions
- Updated dev-kit versioning policy with version file location note

### Notes

- Version file now includes docstring explaining schema and dev-kit versioning approach
- CHANGELOG format verified to match framework (DD-MM-YY date format, archive structure)
- See `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.3.1.4+1.md` for full details

---

## [0.3.1.3+1] - 02-12-25

📚 Documentation: Task 3 complete - Dev-kit versioning policy enhanced with all missing sections

### Added

- Added **6 critical sections** to dev-kit versioning policy:
  - CHANGELOG Format (two-layer system)
  - Canonical Ordering Principle
  - Two-Layer Timestamp System
  - Forensic Traceability Grid (5 dimensions)
  - Immutability Rules (3 rules)
  - Version Validation

### Changed

- Enhanced dev-kit versioning policy with comprehensive documentation
- Updated policy status from "Draft" to "Active"
- Added Status and Maintenance section
- Added comprehensive References section

### Notes

- All 6 critical gaps from gap analysis (T001) have been addressed
- Policy now fully aligned with framework while maintaining dev-kit-specific context
- See `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.3.1.3+1.md` for full details

---

## [0.3.1.1+2] - 02-12-25

📚 Documentation: Task 1 complete - Gap analysis comparing dev-kit versioning policy with framework

### Added

- Created **gap analysis report** comparing dev-kit versioning policy with framework policies
- Identified 6 critical gaps (missing sections) and provided prioritized recommendations
- Documented alignment strengths and areas for improvement

### Changed

- Updated Story 001 to mark Task 1 as complete with gap analysis reference

### Notes

- Gap analysis: `KB/PM_and_Portfolio/kanban/epics/Epic-3/stories/Story-001-dev-kit-alignment-with-versioning-framework/T001-gap-analysis-report.md`
- See `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.3.1.1+2.md` for full details

---

## [0.3.1.2+1] - 02-12-25

📚 Documentation: Task 2 complete - Ingested versioning findings from fynd.deals Epic 15 work

### Added

- Created **findings document** analyzing 12 reusable versioning patterns from fynd.deals Epic 15 work
- Documented versioning patterns: schema, validation, CHANGELOG structure, traceability, immutability rules
- Identified that framework package already contains fynd.deals Epic 15 findings

### Changed

- Updated Story 001 to mark Task 2 as complete with findings reference

### Notes

- Findings document: `KB/PM_and_Portfolio/kanban/epics/Epic-3/stories/Story-001-dev-kit-alignment-with-versioning-framework/T002-fynd-deals-epic15-findings.md`
- See `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.3.1.2+1.md` for full details

---

## [0.4.1.1+1] - 02-12-25

📚 Documentation: Epic 4 structure and Story 1 definition for Kanban Framework

### Added

- Created **Epic 4: Kanban Framework** (`KB/PM_and_Portfolio/kanban/epics/Epic-4.md`)
- Created **Story 1: Dev Kit Kanban Implementation** with 5 initial tasks
- Updated Kanban board views with Epic 4 Story 1 references

### Notes

- Epic 4 owns the `packages/frameworks/kanban/` package
- Story 1 tasks focus on establishing dev-kit as canonical SoT for Kanban policies and templates
- See `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.4.1.1+1.md` for full details

---

## [0.3.1.1+1] - 02-12-25

📚 Documentation: Epic 3 structure and Story 1 definition for Numbering & Versioning Framework

### Added

- Created **Epic 3: Numbering & Versioning Framework** (`KB/PM_and_Portfolio/kanban/epics/Epic-3.md`)
- Created **Story 1: Dev Kit Alignment with Versioning Framework** with 5 initial tasks
- Updated Kanban board views with Epic 3 Story 1 references

### Notes

- Epic 3 owns the `packages/frameworks/numbering & versioning/` package
- Story 1 tasks focus on establishing dev-kit as canonical SoT for versioning policies
- See `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.3.1.1+1.md` for full details

---

## [0.1.1.1+2] - 02-12-25

📚 Documentation: Restructured CHANGELOG and README to follow industry-standard templates

### Changed

- **CHANGELOG.md** restructured to follow [Keep a Changelog](https://github.com/olivierlacan/keep-a-changelog) format with proper sections and organization
- **README.md** restructured using [Best-README-Template](https://github.com/othneildrew/Best-README-Template) layout with [Shields.io](https://shields.io/) badges
- Added **Roadmap** section to README summarizing Epics 1-4 with links to Kanban board

### Notes

- All existing content preserved; only structure and presentation improved
- See `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.1.1.1+2.md` for full details

---

## [0.1.1.1+1] - 02-12-25

🏗️ Foundation: First proper release with Epic 1–4 structure, dev-kit versioning policy, and Kanban FR/BR → Task flow

### Added

- Created **Epic 1–4 docs** (Core, Workflow, Numbering & Versioning, Kanban) to structure dev-kit work
- Introduced **dev-kit versioning policy** using `RC.EPIC.STORY.TASK+BUILD` starting at Epic 1
- Updated **Kanban framework policy** with explicit **FR/BR → Task → Story → Epic** flow
- Updated **dev-kit Kanban policy** to adopt full versioning strategy and task-driven work

### Notes

- See `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.1.1.1+1.md` for full details.

---

## [0.9.21.3+2] - 02-12-25

📚 Documentation: Branch safety Step 1 and modularity docs for workflow & numbering packages

### Changed

- Added **Branch Safety Check** as Step 1 in the Release Workflow agent guide  
- Updated RW and `.cursorrules` docs for an 11-step workflow with branch safety  
- Clarified modularity and package dependencies in workflow and numbering/versioning packages

### Notes

- This version referenced **Confidentia Epic 9** and predates dev-kit-specific epics.  
- Starting with `v0.1.1.1+1`, all releases use **dev-kit-specific Epic numbers**.
- See `KB/Changelog_and_Release_Notes/Changelog_Archive/CHANGELOG_v0.9.21.3+2.md` for full details.

