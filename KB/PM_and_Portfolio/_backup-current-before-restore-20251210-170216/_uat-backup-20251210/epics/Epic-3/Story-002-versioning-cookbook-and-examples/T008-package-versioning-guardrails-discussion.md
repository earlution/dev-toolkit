# Package Versioning Guardrails: Discussion & Proposal

**Task:** E3:S02:T08 – Audit dual-versioning application across packages and propose strategy  
**Date:** 2025-12-08  
**Status:** DISCUSSION  
**Related:** T008-dual-versioning-package-audit-report.md

---

## Executive Summary

This document discusses guardrails, checks, and balances needed to ensure:
1. **Packages are versioned correctly** - Version format, location, and consistency
2. **Justifications for MAJOR/MINOR/PATCH bumps are fully defined and documented** - Clear criteria and examples
3. **Processes for bumping are sound** - Validation, review, and automation

**Key Areas:**
- **Validation Mechanisms** - Automated checks and validation scripts
- **Version Bump Criteria** - Clear definitions for MAJOR/MINOR/PATCH
- **Process Requirements** - When, how, and who can bump versions
- **Documentation Requirements** - Changelog, justification, and metadata
- **Review & Approval** - Quality gates and review processes

---

## 1. Current State Analysis

### 1.1 Existing Validation

**Current Validation Scripts:**
- `validate_branch_context.py` - Validates project version matches branch/epic
- `validate_changelog_format.py` - Validates changelog format
- `validate_version_bump.py` - Validates version bump logic

**Gaps for Package Versioning:**
- ❌ No validation for package version format (SemVer)
- ❌ No validation for package version location consistency
- ❌ No validation for package version bump justification
- ❌ No validation for package changelog requirements
- ❌ No validation for package version vs. project version alignment

### 1.2 Current Package Versioning Process

**Current Approach:**
- Manual updates in README files
- No formal process or validation
- No changelog requirements for packages
- No justification documentation
- No review process

**Issues:**
- Inconsistent version locations (some in README, some in YAML frontmatter)
- No clear criteria for when to bump versions
- No documentation of why versions were bumped
- No validation that versions follow SemVer rules
- No checks that version increments are appropriate

---

## 2. Guardrails & Validation Mechanisms

### 2.1 Version Format Validation

**Requirement:** Ensure all package versions follow SemVer format (`MAJOR.MINOR.PATCH`)

**Validation Checks:**
1. **Format Validation:**
   - Must match regex: `^\d+\.\d+\.\d+$`
   - No pre-release identifiers (e.g., `-alpha`, `-beta`) for stable packages
   - No build metadata (e.g., `+build`) for package versions

2. **Version Increment Validation:**
   - New version must be greater than previous version
   - Only one component can increment at a time (MAJOR, MINOR, or PATCH)
   - Cannot skip versions (e.g., 1.0.0 → 1.2.0 without 1.1.0)

3. **Version Location Consistency:**
   - All packages must have version in consistent location
   - README.md: `**Version:** X.Y.Z` (standardized format)
   - Package manifest files (if published): Must match README version

**Proposed Script:** `validate_package_version.py`
```python
#!/usr/bin/env python3
"""
Validate package version format and consistency.

Checks:
- SemVer format (MAJOR.MINOR.PATCH)
- Version increment is valid
- Version location consistency
- Version matches across all locations
"""

def validate_semver_format(version: str) -> bool:
    """Validate SemVer format."""
    import re
    pattern = r'^\d+\.\d+\.\d+$'
    return bool(re.match(pattern, version))

def validate_version_increment(old_version: str, new_version: str) -> bool:
    """Validate version increment is valid."""
    old_parts = [int(x) for x in old_version.split('.')]
    new_parts = [int(x) for x in new_version.split('.')]
    
    # Check if new version is greater
    if new_parts <= old_parts:
        return False
    
    # Check only one component incremented
    increments = sum(1 for i in range(3) if new_parts[i] > old_parts[i])
    if increments != 1:
        return False
    
    # Check no skipping (e.g., 1.0.0 -> 1.2.0 without 1.1.0)
    if new_parts[0] > old_parts[0]:  # MAJOR bump
        return new_parts[1] == 0 and new_parts[2] == 0
    elif new_parts[1] > old_parts[1]:  # MINOR bump
        return new_parts[2] == 0
    else:  # PATCH bump
        return True
```

### 2.2 Version Bump Justification Validation

**Requirement:** Every version bump must have documented justification

**Validation Checks:**
1. **Changelog Entry Required:**
   - Must have changelog entry for version bump
   - Changelog must list changes that justify the bump
   - Changes must align with SemVer rules (MAJOR/MINOR/PATCH)

2. **Justification Documentation:**
   - Must document why MAJOR/MINOR/PATCH was chosen
   - Must reference specific changes that justify the bump
   - Must follow version bump criteria (see Section 3)

3. **Change Detection:**
   - Validate that actual changes exist that justify the bump
   - Compare file changes against version bump type
   - Flag suspicious bumps (e.g., MAJOR bump with only documentation changes)

**Proposed Script:** `validate_package_version_bump.py`
```python
#!/usr/bin/env python3
"""
Validate package version bump justification.

Checks:
- Changelog entry exists
- Justification documented
- Changes align with bump type
- No suspicious bumps
"""

def validate_bump_justification(
    old_version: str,
    new_version: str,
    changelog_entry: str,
    changed_files: List[str]
) -> Tuple[bool, List[str]]:
    """Validate version bump justification."""
    errors = []
    
    # Determine bump type
    bump_type = determine_bump_type(old_version, new_version)
    
    # Check changelog entry exists
    if not changelog_entry:
        errors.append("Changelog entry required for version bump")
    
    # Check justification aligns with bump type
    if not validate_bump_type_justification(bump_type, changelog_entry, changed_files):
        errors.append(f"Changes do not justify {bump_type} bump")
    
    return len(errors) == 0, errors
```

### 2.3 Package Version Location Consistency

**Requirement:** All packages must have version in consistent, discoverable location

**Standardized Locations:**
1. **README.md** (Primary):
   ```markdown
   **Version:** X.Y.Z
   **Last Updated:** YYYY-MM-DD
   ```

2. **Package Manifest** (If published):
   - `package.json`: `"version": "X.Y.Z"`
   - `pubspec.yaml`: `version: X.Y.Z`
   - `pyproject.toml`: `version = "X.Y.Z"`
   - `Cargo.toml`: `version = "X.Y.Z"`

3. **VERSION File** (Optional, for automation):
   ```
   X.Y.Z
   ```

**Validation:**
- All locations must have same version
- README version is source of truth
- Package manifest versions must match README

**Proposed Script:** `validate_package_version_consistency.py`
```python
#!/usr/bin/env python3
"""
Validate package version consistency across all locations.

Checks:
- Version exists in README
- Version matches in all locations
- README is source of truth
"""

def validate_version_consistency(package_path: Path) -> Tuple[bool, List[str]]:
    """Validate version consistency across all locations."""
    errors = []
    
    # Read version from README (source of truth)
    readme_version = extract_version_from_readme(package_path / "README.md")
    
    # Check package manifest files
    for manifest_file in find_manifest_files(package_path):
        manifest_version = extract_version_from_manifest(manifest_file)
        if manifest_version != readme_version:
            errors.append(
                f"Version mismatch: README={readme_version}, "
                f"{manifest_file.name}={manifest_version}"
            )
    
    return len(errors) == 0, errors
```

---

## 3. Version Bump Criteria

### 3.1 MAJOR Version Bump (X.0.0)

**Definition:** Breaking changes that require consumers to modify their code or configuration

**Criteria for Documentation Packages:**
- ✅ **Breaking Structure Changes:**
  - Removing or renaming core files/directories
  - Changing required file locations or names
  - Removing templates or core components
  - Changing package directory structure significantly

- ✅ **Breaking Policy Changes:**
  - Changing core policy rules that break existing implementations
  - Removing policy options or requirements
  - Changing mandatory vs. optional requirements
  - Changing integration patterns that break existing setups

- ✅ **Breaking API Changes (for script packages):**
  - Removing command-line arguments or options
  - Changing script behavior in incompatible ways
  - Removing functions or classes from public API
  - Changing return types or signatures

**Examples:**
- **MAJOR:** Removing `EPIC_TEMPLATE.md` (breaking - consumers depend on it)
- **MAJOR:** Changing `version_file` location requirement (breaking - breaks existing configs)
- **MAJOR:** Removing support for old version format (breaking - breaks existing projects)

**NOT MAJOR:**
- ❌ Adding new templates (MINOR)
- ❌ Adding new optional features (MINOR)
- ❌ Clarifying documentation (PATCH)
- ❌ Fixing typos (PATCH)

### 3.2 MINOR Version Bump (x.Y.0)

**Definition:** New features, enhancements, or additions that are backward compatible

**Criteria for Documentation Packages:**
- ✅ **New Features:**
  - Adding new templates or guides
  - Adding new integration patterns
  - Adding new optional features or capabilities
  - Adding new examples or use cases

- ✅ **Enhancements:**
  - Expanding existing templates with new sections
  - Adding new policy options (non-breaking)
  - Adding new configuration options
  - Adding new validation rules (non-breaking)

- ✅ **New Documentation:**
  - Adding new guides or tutorials
  - Adding new examples or case studies
  - Adding new integration documentation
  - Adding new troubleshooting guides

**Examples:**
- **MINOR:** Adding new `MIGRATION_GUIDE.md` (new feature)
- **MINOR:** Adding new template variant (new feature)
- **MINOR:** Adding new integration pattern (new feature)
- **MINOR:** Expanding existing guide with new sections (enhancement)

**NOT MINOR:**
- ❌ Fixing broken links (PATCH)
- ❌ Correcting typos (PATCH)
- ❌ Clarifying ambiguous text (PATCH)
- ❌ Removing features (MAJOR)

### 3.3 PATCH Version Bump (x.y.Z)

**Definition:** Bug fixes, corrections, clarifications, or minor improvements that don't add functionality

**Criteria for Documentation Packages:**
- ✅ **Bug Fixes:**
  - Fixing broken links or references
  - Correcting incorrect examples or code snippets
  - Fixing formatting or rendering issues
  - Fixing validation script bugs

- ✅ **Corrections:**
  - Correcting typos or grammatical errors
  - Correcting factual errors
  - Correcting version numbers or dates
  - Correcting file paths or references

- ✅ **Clarifications:**
  - Clarifying ambiguous language
  - Adding missing context or explanations
  - Improving readability without changing meaning
  - Adding cross-references or links

- ✅ **Minor Improvements:**
  - Improving formatting or structure
  - Updating outdated information (non-breaking)
  - Improving code examples (non-breaking)
  - Minor refactoring of documentation structure

**Examples:**
- **PATCH:** Fixing broken link to external resource
- **PATCH:** Correcting typo in template
- **PATCH:** Clarifying ambiguous policy statement
- **PATCH:** Fixing code example syntax error

**NOT PATCH:**
- ❌ Adding new template (MINOR)
- ❌ Removing feature (MAJOR)
- ❌ Changing structure (MAJOR)

### 3.4 Version Bump Decision Matrix

| Change Type | MAJOR | MINOR | PATCH |
|------------|-------|-------|-------|
| **Breaking Changes** | ✅ | ❌ | ❌ |
| **New Features** | ❌ | ✅ | ❌ |
| **Enhancements** | ❌ | ✅ | ❌ |
| **Bug Fixes** | ❌ | ❌ | ✅ |
| **Corrections** | ❌ | ❌ | ✅ |
| **Clarifications** | ❌ | ❌ | ✅ |
| **Minor Improvements** | ❌ | ❌ | ✅ |

---

## 4. Process Requirements

### 4.1 Version Bump Process

**Step 1: Determine Bump Type**
1. Review changes made to package
2. Classify changes using criteria (Section 3)
3. Determine appropriate bump type (MAJOR/MINOR/PATCH)
4. Document decision and justification

**Step 2: Update Version**
1. Update version in README.md
2. Update version in package manifest files (if published)
3. Update VERSION file (if exists)
4. Ensure all locations are consistent

**Step 3: Create Changelog Entry**
1. Create changelog entry in package CHANGELOG.md
2. Document all changes that justify the bump
3. Include justification for bump type chosen
4. Reference project version (if applicable)

**Step 4: Document Justification**
1. Document why MAJOR/MINOR/PATCH was chosen
2. List specific changes that justify the bump
3. Reference version bump criteria used
4. Include any relevant context or notes

**Step 5: Validate**
1. Run validation scripts:
   - `validate_package_version.py` - Format validation
   - `validate_package_version_bump.py` - Justification validation
   - `validate_package_version_consistency.py` - Consistency validation
2. Fix any validation errors
3. Re-run validation until all checks pass

**Step 6: Review (If Required)**
1. Submit for review (if MAJOR bump or policy requires)
2. Address review feedback
3. Get approval before merging

**Step 7: Commit & Tag**
1. Commit changes with versioned message
2. Create git tag for package version
3. Push changes and tags

### 4.2 Automation Opportunities

**Pre-Commit Hook:**
- Validate version format before commit
- Check version consistency
- Validate version increment

**CI/CD Pipeline:**
- Run validation scripts on PR
- Check changelog entry exists
- Validate version bump justification
- Check version consistency

**Release Workflow Integration:**
- Add package version bump step to RW
- Validate package versions during RW
- Update package changelogs automatically
- Create package version tags

### 4.3 Review Requirements

**MAJOR Bumps:**
- ✅ **Mandatory Review:** All MAJOR bumps require review
- ✅ **Review Criteria:** Breaking changes, impact assessment, migration path
- ✅ **Approval Required:** Must be approved before merging

**MINOR Bumps:**
- ⚠️ **Optional Review:** MINOR bumps may require review (configurable)
- ⚠️ **Review Criteria:** Feature completeness, documentation quality
- ⚠️ **Approval:** May be auto-approved if criteria met

**PATCH Bumps:**
- ❌ **No Review Required:** PATCH bumps can be auto-merged
- ❌ **Auto-Approval:** If validation passes, auto-approve

---

## 5. Documentation Requirements

### 5.1 Changelog Requirements

**Required Format:**
```markdown
## [X.Y.Z] - YYYY-MM-DD

**Package Version:** X.Y.Z
**Project Version:** RC.EPIC.STORY.TASK+BUILD (if applicable)
**Bump Type:** MAJOR | MINOR | PATCH

### Justification
[Explanation of why this bump type was chosen]

### Added
- [New features or additions]

### Changed
- [Changes to existing features]

### Fixed
- [Bug fixes]

### Removed
- [Removed features] (MAJOR only)
```

**Required Sections:**
- **Version Header:** Package version and date
- **Justification:** Why this bump type was chosen
- **Change Categories:** Added/Changed/Fixed/Removed
- **Project Version Reference:** Link to project version (if applicable)

### 5.2 Justification Documentation

**Required Information:**
1. **Bump Type:** MAJOR/MINOR/PATCH
2. **Reason:** Why this bump type was chosen
3. **Changes:** List of specific changes that justify the bump
4. **Criteria Reference:** Which criteria from Section 3 were used
5. **Impact Assessment:** Impact on consumers (for MAJOR bumps)

**Example:**
```markdown
### Justification

**Bump Type:** MINOR

**Reason:** Added new integration guide for Workflow Management package.

**Changes:**
- Added `integration/workflow-management-integration.md`
- Added new integration pattern examples
- Expanded integration documentation section

**Criteria Reference:** Section 3.2 - MINOR Version Bump
- ✅ New feature: New integration guide
- ✅ Enhancement: Expanded documentation

**Impact Assessment:** None - backward compatible addition
```

### 5.3 Package Metadata

**Required Metadata:**
- **Version:** Current package version
- **Last Updated:** Date of last version bump
- **Version History:** Link to changelog or version history
- **Bump Policy:** Link to versioning policy document

**Example:**
```markdown
**Version:** 2.0.0
**Last Updated:** 2025-12-08
**Version History:** [CHANGELOG.md](CHANGELOG.md)
**Bump Policy:** [Package Versioning Policy](../../KB/Architecture/Standards_and_ADRs/package-versioning-policy.md)
```

---

## 6. Proposed Implementation

### 6.1 Phase 1: Define Criteria & Process

**Deliverables:**
- ✅ Version bump criteria document (this document)
- ✅ Process documentation
- ✅ Examples and decision matrix

**Timeline:** Immediate

### 6.2 Phase 2: Create Validation Scripts

**Deliverables:**
- `validate_package_version.py` - Format validation
- `validate_package_version_bump.py` - Justification validation
- `validate_package_version_consistency.py` - Consistency validation

**Timeline:** 1-2 weeks

### 6.3 Phase 3: Standardize Package Structure

**Deliverables:**
- Standardized README format
- Package CHANGELOG.md templates
- VERSION file format (if needed)

**Timeline:** 1 week

### 6.4 Phase 4: Integrate with Release Workflow

**Deliverables:**
- RW step for package version validation
- Automated package changelog generation
- Package version tagging

**Timeline:** 2-3 weeks

### 6.5 Phase 5: CI/CD Integration

**Deliverables:**
- Pre-commit hooks
- CI validation checks
- Automated review/approval

**Timeline:** 1-2 weeks

---

## 7. Open Questions & Discussion Points

### 7.1 Version Bump Authority

**Question:** Who can bump package versions?

**Options:**
- **A:** Package maintainers only
- **B:** Anyone with write access
- **C:** Requires approval for MAJOR, auto-approve for MINOR/PATCH

**Recommendation:** Option C - Requires approval for MAJOR, auto-approve for MINOR/PATCH if validation passes

### 7.2 Changelog Location

**Question:** Where should package changelogs live?

**Options:**
- **A:** `packages/frameworks/{package}/CHANGELOG.md`
- **B:** Centralized `KB/Changelog_and_Release_Notes/Packages/`
- **C:** Both (package-level + centralized)

**Recommendation:** Option A - Package-level changelogs for discoverability

### 7.3 Version Bump Frequency

**Question:** How often should packages be versioned?

**Options:**
- **A:** Every change requires version bump
- **B:** Version only on significant changes
- **C:** Version on releases/milestones

**Recommendation:** Option A - Every change requires version bump (ensures traceability)

### 7.4 Project Version Reference

**Question:** Should package versions reference project version?

**Options:**
- **A:** Always include project version reference
- **B:** Optional project version reference
- **C:** No project version reference

**Recommendation:** Option B - Optional reference for traceability, not required

---

## 8. Next Steps

### 8.1 Immediate Actions

1. **Review & Approve Criteria:**
   - Review version bump criteria (Section 3)
   - Approve decision matrix
   - Finalize examples

2. **Create Validation Scripts:**
   - Implement `validate_package_version.py`
   - Implement `validate_package_version_bump.py`
   - Implement `validate_package_version_consistency.py`

3. **Standardize Package Structure:**
   - Update README templates
   - Create CHANGELOG.md templates
   - Document version location requirements

### 8.2 Future Enhancements

1. **Release Workflow Integration:**
   - Add package version validation to RW
   - Automate package changelog generation
   - Add package version tagging

2. **CI/CD Integration:**
   - Pre-commit hooks
   - CI validation checks
   - Automated review/approval

3. **Documentation:**
   - Package versioning policy document
   - Version bump guide for maintainers
   - Examples and case studies

---

## 9. References

- **Audit Report:** `T008-dual-versioning-package-audit-report.md`
- **Dual-Versioning Guide:** `KB/Architecture/Standards_and_ADRs/dual-versioning-package-managers.md`
- **Versioning Policy:** `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md`
- **SemVer Specification:** https://semver.org/

---

**Status:** DISCUSSION  
**Next Review:** After discussion and approval of criteria and process

