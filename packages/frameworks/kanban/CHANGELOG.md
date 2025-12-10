# Changelog

All notable changes to the Kanban System Implementation Package will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.4.0] - 2025-12-09

**Package Version:** 1.4.0
**Project Version:** 0.4.6.0+1
**Bump Type:** MINOR

### Added
- **Comprehensive Canonical E/S/T Structure:** Complete template system for canonical epics, stories, and tasks
  - `packages/frameworks/kanban/templates/COMPREHENSIVE_CANONICAL_EST_STRUCTURE.md` - Complete canonical structure (Epics 1-21+)
  - Epic 7: User Experience Research (UXR) added as canonical epic
  - ~50+ stories and ~300+ tasks defined
  - Scalability guidance (tiny → ambitious projects)
  - Contextualization system with placeholders
- **Design Documentation:** Comprehensive canonical structure design document
  - `KB/Documentation/Engineering_and_Platform/comprehensive-canonical-est-structure-design.md`
  - Rationale for Epic 7 (UXR) as canonical
  - Epic ordering rationale
  - Implementation requirements

### Changed
- Epic 7 changed from "Codebase Maintenance" to "User Experience Research (UXR)"
- Codebase Maintenance moved to Epic 8 (project-specific canonical pattern)
- All project-specific epics renumbered (8→9, 9→10, etc.)

---

## [1.3.0] - 2025-12-09

**Package Version:** 1.3.0
**Project Version:** 0.4.2.6+1
**Bump Type:** MINOR

### Added
- **GitHub Issue Templates:** Bug Report, Feature Request, and UXR templates for GitHub Issues
  - `.github/ISSUE_TEMPLATE/bug_report.yml` - Structured bug report form
  - `.github/ISSUE_TEMPLATE/feature_request.yml` - Structured feature request form
  - `.github/ISSUE_TEMPLATE/ux_research.yml` - Structured UX research form
- **GitHub Action:** Automatic conversion from GitHub Issues to FR/BR/UXR documents
  - `.github/workflows/fr-br-intake.yml` - Converts Issues to Kanban documents
  - Automatic document creation and linking
  - Bidirectional linking between GitHub Issues and Kanban documents
- **UXR Template:** User Experience Research template
  - `packages/frameworks/kanban/templates/UXR_TEMPLATE.md` - Complete UXR template
- **GitHub Submission Guide:** Comprehensive guide for external contributors
  - `packages/frameworks/kanban/FR_BR_UXR_GITHUB_SUBMISSION_GUIDE.md` - Complete submission guide

### Changed
- Updated README to include new templates and guides

**Criteria Reference:** MINOR Version Bump
- ✅ New feature: GitHub Issue integration for FR/BR/UXR submissions
- ✅ New feature: UXR template and support
- ✅ Enhancement: External contributor accessibility
- ✅ Backward compatible: No breaking changes

---

## [1.2.0] - 2025-12-09

### Added
- **Epic 7: Codebase Maintenance and Review** - New canonical epic for codebase maintenance and review work
  - Story 1: Codebase Maintenance Tasks with perpetual task for IDE-flagged issues
  - Example Epic 7 document demonstrating structure and content
  - Integration with Epic 4 (Kanban Framework) and Epic 6 (BR Implementation)

### Changed
- Updated canonical epic count from 1-6 to 1-7
- Updated intake guides to reference Epic 7 (new project-specific epics now start at Epic 8)
- Updated README to include Epic 7 in canonical epic definitions

### Documentation
- Added Epic 7 example document: `examples/Epic-7-Codebase-Maintenance-Example.md`
- Updated `CANONICAL_EPICS.md` with Epic 7 definition and ordering rationale
- Updated all intake guides (`FR_BR_INTAKE_GUIDE.md`, `FR_BR_INTAKE_AGENT_GUIDE.md`, `FR_BR_INTAKE_USER_GUIDE.md`)

## [1.1.0] - 2025-12-09

### Added
- Canonical Epics 5 and 6 (FR Implementation, BR Implementation)
- Example Epic 5 and Epic 6 documents
- Canonical stories template for FR/BR Implementation epics

### Changed
- Updated canonical epic count from 1-4 to 1-6
- Updated intake guides to reference new canonical epics

## [1.0.0] - 2025-12-04

### Added
- Initial release of Kanban System Implementation Package
- Complete Kanban governance policy
- Epic and Story templates
- FR/BR intake processes
- Canonical Epics 1-4 (Core, Workflow, Versioning, Kanban)

