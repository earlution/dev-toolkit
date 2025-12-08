# Changelog

All notable changes to the Workflow Management package will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.1.0] - 2025-12-08

**Package Version:** 2.1.0
**Project Version:** 0.3.2.9+1
**Bump Type:** MINOR

### Justification
Added Package Version Workflow (PVW) - a complete new workflow for intelligent agent-driven package versioning. This is a new feature that is backward compatible.

**Changes:**
- Added `workflows/package-version-workflow.yaml` - PVW workflow definition
- Added `KB/Documentation/Developer_Docs/vwmp/package-version-workflow-agent-execution.md` - Complete agent execution guide
- Added `scripts/validation/package/` - Validation scripts as tools (format, increment, consistency, change analysis)
- Updated `workflows/release-workflow.yaml` - Integrated PVW as Step 2.5
- Updated `cursorrules-rw-trigger-section.md` - Added PVW trigger section with comprehensive TODO tracking

**Criteria Reference:** MINOR Version Bump
- ✅ New feature: Complete new workflow (PVW)
- ✅ Enhancement: Integrated with Release Workflow
- ✅ Backward compatible: No breaking changes

**Impact Assessment:** None - backward compatible addition. Existing RW functionality unchanged.

### Added
- **Package Version Workflow (PVW):** Complete workflow for intelligent agent-driven package versioning
  - Workflow definition (`package-version-workflow.yaml`)
  - Agent execution guide (`package-version-workflow-agent-execution.md`)
  - Validation scripts as tools (`scripts/validation/package/`)
- **PVW Integration:** PVW executes as RW Step 2.5 (after project version bump, before changelog)
- **Cursor Rules:** PVW trigger section with comprehensive TODO tracking requirements
- **Version Bump Criteria:** Documentation of MAJOR/MINOR/PATCH criteria as guidance

---

## [2.0.0] - 2025-12-06

**Package Version:** 2.0.0
**Project Version:** 0.2.1.5+3

### Added
- "ALL sections" requirement for Kanban updates
- Atomicity and blocked protocol
- Epic branch workflow support

### Changed
- Workflow YAML schema updated
- Enhanced validation and error handling

---

