# Dual-Versioning Package Audit Report

**Task:** E3:S02:T08 – Audit dual-versioning application across packages and propose strategy  
**Date:** 2025-12-08  
**Status:** ✅ COMPLETE  
**Version:** 0.3.2.8+1

---

## Executive Summary

This report audits the current state of package versioning across all packages in the `ai-dev-kit` repository, analyzes the applicability of the dual-versioning strategy for package management, and proposes a comprehensive solution for consistent and reliable package versioning.

**Key Findings:**
- ✅ Three framework packages have version numbers documented in README files (Workflow Management: 2.0.0, Numbering & Versioning: 2.0.0, Kanban: 1.0.0)
- ❌ **No package manifest files found** (no `package.json`, `pubspec.yaml`, `setup.py`, `pyproject.toml`, `Cargo.toml`)
- ⚠️ **Dual-versioning strategy may not be applicable** - Packages are documentation-only, not published to package managers
- ⚠️ **SemVer continuity concern validated** - Generated SemVers from `RC.EPIC.STORY.TASK+BUILD` would not follow-on numerically
- ✅ **Current approach is appropriate** - Package versions are independent SemVer for documentation purposes

**Recommendation:**
- **For documentation packages:** Continue using independent SemVer (current approach)
- **For future published packages:** Implement independent SemVer tracking separate from project version
- **For adopting projects:** Provide guidance on when to use dual-versioning vs. independent SemVer

---

## 1. Package Inventory

### 1.1 Framework Packages

#### 1.1.1 Workflow Management (`packages/frameworks/workflow mgt/`)

**Current Version:** 2.0.0  
**Version Location:** `README.md` (line 11)  
**Version History:** 
- Version 1.0.0 → 1.1.0 → 1.2.0 → 2.0.0 (mentioned in `release-workflow-agent-execution.md`)
- User mentioned versions 1.0, 1.1, 1.2 pattern (likely referring to this history)

**Package Manifest Files:** ❌ None found
- No `package.json` (npm)
- No `pubspec.yaml` (pub.dev)
- No `setup.py` or `pyproject.toml` (PyPI)
- No `Cargo.toml` (crates.io)

**Package Type:** Documentation + Scripts (Python validation scripts)  
**Publishing Status:** Not published to any package manager  
**Versioning Approach:** Independent SemVer in README (not derived from project version)

**Files Containing Version References:**
- `README.md`: `**Version:** 2.0.0`
- `workflows/release-workflow.yaml`: `version: 2.0.0`
- `cursorrules-rw-trigger-section.md`: `**Version:** 2.2.0`
- `KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md`: Version history (1.0.0, 1.1.0, 1.2.0)

---

#### 1.1.2 Numbering & Versioning (`packages/frameworks/numbering & versioning/`)

**Current Version:** 2.0.0  
**Version Location:** `README.md` (line 15), `PACKAGE_OVERVIEW.md` (line 11)  
**Version History:** 
- Version 1.0 → 2.0.0 (mentioned in `versioning-policy.md`)

**Package Manifest Files:** ❌ None found
- No `package.json` (npm)
- No `pubspec.yaml` (pub.dev)
- No `setup.py` or `pyproject.toml` (PyPI)
- No `Cargo.toml` (crates.io)

**Package Type:** Documentation only (pure policy package)  
**Publishing Status:** Not published to any package manager  
**Versioning Approach:** Independent SemVer in README (not derived from project version)

**Files Containing Version References:**
- `README.md`: `**Version:** 2.0.0`
- `PACKAGE_OVERVIEW.md`: `**Version:** 2.0.0`
- `KB/Architecture/Standards_and_ADRs/versioning-policy.md`: Version history table

---

#### 1.1.3 Kanban (`packages/frameworks/kanban/`)

**Current Version:** 1.0.0  
**Version Location:** `README.md` (line 14, YAML format)  
**Version History:** 
- Version 1.0.0 (initial release, mentioned in version history section)

**Package Manifest Files:** ❌ None found
- No `package.json` (npm)
- No `pubspec.yaml` (pub.dev)
- No `setup.py` or `pyproject.toml` (PyPI)
- No `Cargo.toml` (crates.io)

**Package Type:** Documentation + Templates  
**Publishing Status:** Not published to any package manager  
**Versioning Approach:** Independent SemVer in README (not derived from project version)

**Files Containing Version References:**
- `README.md`: `version: "1.0.0"` (YAML format)
- `README.md`: Version history section (v1.0.0)

---

#### 1.1.4 Debug Path (`packages/frameworks/debug-path/`)

**Current Version:** ❌ Not found  
**Version Location:** N/A  
**Package Manifest Files:** ❌ None found  
**Package Type:** Documentation + Templates  
**Publishing Status:** Not published  
**Versioning Approach:** No version tracking

---

#### 1.1.5 Doc Lifecycle (`packages/frameworks/doc-lifecycle/`)

**Current Version:** ❌ Not found  
**Version Location:** N/A  
**Package Manifest Files:** ❌ None found  
**Package Type:** Documentation + Policies  
**Publishing Status:** Not published  
**Versioning Approach:** No version tracking

---

## 2. Dual-Versioning Strategy Analysis

### 2.1 Current State Assessment

**Finding:** The dual-versioning strategy documented in `KB/Architecture/Standards_and_ADRs/dual-versioning-package-managers.md` is **not currently applied** to any packages in the repository.

**Evidence:**
1. No package manifest files exist that would require SemVer
2. Package versions are tracked independently in README files
3. Package versions are not derived from project version (`RC.EPIC.STORY.TASK+BUILD`)
4. No sync scripts or automation exists to maintain dual versions

### 2.2 Applicability Analysis

#### 2.2.1 For Current Packages (Documentation-Only)

**Conclusion:** Dual-versioning is **NOT applicable** for current packages.

**Reasoning:**
- Packages are documentation-only, not published to package managers
- No package manifest files require SemVer format
- Independent SemVer in README is sufficient for documentation versioning
- No need to synchronize with project version

**Current Approach (Appropriate):**
- Package versions are independent SemVer (e.g., 1.0.0, 2.0.0)
- Versions are manually updated in README files when package content changes significantly
- No automation or sync scripts needed

#### 2.2.2 For Future Published Packages

**Conclusion:** Dual-versioning **MAY be applicable** if packages are published to package managers.

**Considerations:**
- If packages are published to npm, pub.dev, PyPI, etc., SemVer will be required
- However, **independent SemVer tracking is recommended** over derived SemVer

**Reasoning:**
- Package versions should reflect package-specific changes, not project-wide changes
- A package may not change even if the project version changes
- Package version history should be continuous and meaningful to package consumers
- Derived SemVer from `RC.EPIC.STORY.TASK+BUILD` would create non-continuous version sequences

### 2.3 SemVer Continuity Problem

**User Concern Validated:** ✅

**Problem Statement:**
If SemVer is derived from `RC.EPIC.STORY.TASK+BUILD` using mapping strategies, the resulting SemVer versions will **not follow-on numerically**, breaking package version history continuity.

**Example Problem:**

**Project Version Sequence:**
```
0.3.2.1+1  →  SemVer: 0.3.201 (Strategy 4: MINOR = EPIC*100+STORY, PATCH = TASK*100+BUILD)
0.3.2.2+1  →  SemVer: 0.3.202
0.3.2.3+1  →  SemVer: 0.3.203
0.7.4.1+1  →  SemVer: 0.7.401  ← Jumps from 0.3.203 to 0.7.401
0.7.4.2+1  →  SemVer: 0.7.402
0.2.5.1+1  →  SemVer: 0.2.501  ← Goes backwards from 0.7.402 to 0.2.501
```

**Issues:**
1. **Non-continuous sequence:** Versions jump around (0.3.203 → 0.7.401 → 0.2.501)
2. **Backwards progression:** Later project versions can produce earlier SemVer (0.7.402 → 0.2.501)
3. **Package manager confusion:** Package managers expect monotonically increasing versions
4. **Consumer confusion:** Package consumers see version history that doesn't make sense

**Impact:**
- Package managers may reject non-monotonic versions
- Dependency resolution may fail
- Consumers cannot understand version progression
- Breaking changes may not be properly signaled

---

## 3. Proposed Solution

### 3.1 Strategy: Independent SemVer for Packages

**Recommendation:** Use **independent SemVer tracking** for packages, separate from project version.

**Approach:**
1. **Package versions are independent** - Tracked separately from project version
2. **SemVer follows standard rules** - MAJOR.MINOR.PATCH with semantic meaning
3. **Package version increments** only when package content changes
4. **Project version and package version** are tracked separately but can be cross-referenced

### 3.2 Implementation Pattern

#### 3.2.1 For Documentation Packages (Current)

**Status:** ✅ Already implemented correctly

**Pattern:**
- Package version in README (`**Version:** X.Y.Z`)
- Manual updates when package content changes significantly
- No automation needed (documentation packages don't change frequently)

**Example:**
```markdown
**Version:** 2.0.0  
**Last Updated:** 2025-12-06
```

**When to bump:**
- **MAJOR:** Breaking changes to package structure, removal of features
- **MINOR:** New features, new templates, new guides
- **PATCH:** Bug fixes, clarifications, minor updates

#### 3.2.2 For Future Published Packages

**Pattern:**
- Package manifest file (e.g., `package.json`, `pubspec.yaml`) contains SemVer
- Package version file (e.g., `packages/frameworks/workflow-mgt/VERSION`) tracks version
- Version increments independently based on package changes
- Cross-reference to project version in changelog or metadata

**Example Structure:**

**`packages/frameworks/workflow-mgt/package.json` (if published to npm):**
```json
{
  "name": "@ai-dev-kit/workflow-mgt",
  "version": "2.0.0",
  "description": "Release Workflow implementation package"
}
```

**`packages/frameworks/workflow-mgt/VERSION`:**
```
2.0.0
```

**Changelog Entry:**
```markdown
## [2.0.0] - 2025-12-06

**Package Version:** 2.0.0  
**Project Version:** 0.2.1.5+3 (Epic 2, Story 1, Task 5, Build 3)

### Added
- PDCA integration
- Config-driven workflow updates

### Changed
- Workflow YAML schema updated
```

### 3.3 Version Mapping Strategy (If Dual-Versioning Required)

**Note:** This strategy is **NOT recommended** for the reasons stated above, but documented here for completeness and for adopting projects that may have different requirements.

**If dual-versioning is absolutely required:**

**Strategy: Independent SemVer with Project Version Reference**

1. **Package version (SemVer)** is the primary version for package managers
2. **Project version (`RC.EPIC.STORY.TASK+BUILD`)** is tracked in package metadata
3. **Package version increments** independently based on package changes
4. **Project version** is included in package metadata for traceability

**Example:**

**`package.json`:**
```json
{
  "name": "@ai-dev-kit/workflow-mgt",
  "version": "2.0.0",
  "metadata": {
    "projectVersion": "0.2.1.5+3",
    "epic": 2,
    "story": 1,
    "task": 5,
    "build": 3
  }
}
```

**Benefits:**
- Package version is continuous and meaningful
- Project version is available for traceability
- No mapping complexity
- No version continuity issues

---

## 4. Recommendations

### 4.1 For ai-dev-kit Repository

#### 4.1.1 Current Packages (Documentation-Only)

**Action:** ✅ **No changes needed**

**Rationale:**
- Current approach (independent SemVer in README) is appropriate
- Packages are not published, so no package manifest files needed
- Manual version updates are sufficient for documentation packages

**Maintenance:**
- Continue updating package versions in README when content changes significantly
- Document version history in README or separate CHANGELOG if needed

#### 4.1.2 Future Published Packages

**Action:** Implement independent SemVer tracking

**Steps:**
1. Create package manifest files when publishing (e.g., `package.json`, `pubspec.yaml`)
2. Track package version separately from project version
3. Include project version reference in package metadata for traceability
4. Document versioning policy in package README

**Example Policy:**
```markdown
## Package Versioning

This package uses **independent Semantic Versioning** (SemVer) separate from the project version.

- **Package Version:** Tracks package-specific changes (MAJOR.MINOR.PATCH)
- **Project Version:** Available in package metadata for traceability (RC.EPIC.STORY.TASK+BUILD)

Package version increments when:
- **MAJOR:** Breaking changes to package API or structure
- **MINOR:** New features or capabilities added
- **PATCH:** Bug fixes or minor improvements
```

### 4.2 For Adopting Projects

#### 4.2.1 Guidance on Dual-Versioning vs. Independent SemVer

**Use Dual-Versioning When:**
- Package version must be derived from project version for compliance reasons
- Package version and project version must always be synchronized
- Project version changes always result in package version changes

**Use Independent SemVer When:**
- Package version should reflect package-specific changes (RECOMMENDED)
- Package may not change even if project version changes
- Package is published to package managers and needs continuous version history
- Package consumers need meaningful version progression

#### 4.2.2 Implementation Guidance

**For Documentation Packages:**
- Use independent SemVer in README
- Update manually when content changes significantly
- No automation needed

**For Published Packages:**
- Use independent SemVer in package manifest
- Track version in separate VERSION file or package manifest
- Include project version reference in metadata for traceability
- Document versioning policy clearly

---

## 5. Conclusion

### 5.1 Current State

- ✅ Package versions are tracked independently (appropriate for documentation packages)
- ✅ No package manifest files exist (not needed for documentation-only packages)
- ✅ Dual-versioning strategy is documented but not applied (correct, as it's not needed)
- ✅ Current approach is appropriate for the repository's needs

### 5.2 Key Insights

1. **Dual-versioning is NOT necessary** for documentation-only packages
2. **Independent SemVer is recommended** for published packages (avoids continuity issues)
3. **SemVer continuity concern is valid** - derived SemVer would create non-continuous sequences
4. **Current approach is correct** - packages use independent SemVer for documentation purposes

### 5.3 Recommendations

1. **Continue current approach** for documentation packages (independent SemVer in README)
2. **Use independent SemVer** for future published packages (separate from project version)
3. **Update dual-versioning guide** to clarify when to use dual-versioning vs. independent SemVer
4. **Document package versioning policy** for adopting projects

---

## 6. Next Steps

### 6.1 Immediate Actions

- [x] Complete audit report (this document)
- [ ] Update dual-versioning guide with guidance on when to use independent SemVer
- [ ] Document package versioning policy for adopting projects

### 6.2 Future Considerations

- [ ] If packages are published, implement independent SemVer tracking
- [ ] Create package manifest files when publishing
- [ ] Document versioning policy in each package README

---

## 7. References

- **Dual-Versioning Guide:** `KB/Architecture/Standards_and_ADRs/dual-versioning-package-managers.md`
- **Versioning Policy:** `KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md`
- **Package Structure Analysis:** `KB/PM_and_Portfolio/kanban/epics/Epic-1/Story-002-package-and-repo-architecture/T001-package-structure-analysis.md`

---

**Report Status:** ✅ COMPLETE  
**Next Review:** When packages are published or versioning approach changes

