# Document Lifecycle Management Package - Proposal

**Status:** Proposal  
**Date:** 2025-12-04  
**Related:** [Document Lifecycle Metadata Spec](../../../KB/Architecture/Standards_and_ADRs/doc-lifecycle-metadata-spec.md) | [Document Lifecycle Policy](../../../KB/Architecture/Standards_and_ADRs/doc-lifecycle-policy.md)

---

## 📋 Package Overview

**Proposed Package Name:** `packages/frameworks/doc-lifecycle/`  
**Purpose:** Standalone package for managing Knowledge Base (KB) document lifecycle with TTL-based expiration and automated housekeeping.

**Core Value:**
- Prevents documentation bloat through lifecycle classification
- Enables automated housekeeping of temporary documents
- Preserves evergreen content while cleaning up obsolete docs
- Agent-driven lifecycle management with clear rules

---

## 🧩 Modularity & Dependencies

### Standalone Usage

✅ **This package can be used completely independently** without requiring any other `ai-dev-kit` packages.

**What you get standalone:**
- Complete document lifecycle metadata specification
- Document lifecycle policy and governance rules
- Lifecycle classification rules (evergreen/timeboxed/transient)
- TTL-based expiration system
- Housekeeping process documentation
- Agent requirements and rules

**Hard dependencies (required):**
- None — this is a pure documentation/policy package

**Independence score:** 10/10 — Pure documentation/policy, no runtime dependencies.

---

### Combined Usage

**With Kanban Package:**
- Lifecycle metadata can be applied to Kanban Epics/Stories
- Integration: Kanban docs can have lifecycle metadata for housekeeping
- Optional: Kanban can work without lifecycle management

**With Workflow Management Package:**
- Doc Housekeeping Workflow can automate lifecycle management
- Integration: RW can set lifecycle metadata when creating docs
- Optional: Workflow mgt can work without lifecycle management

**With Both Packages:**
- Complete integration: RW sets lifecycle → Housekeeping Workflow manages expiration
- Automated lifecycle management for all KB documents

---

## 📦 Proposed Package Structure

```
packages/frameworks/doc-lifecycle/
├── README.md                          # Package overview and quick reference
├── PACKAGE_OVERVIEW.md                # Package structure and usage
├── IMPLEMENTATION_GUIDE.md            # Step-by-step implementation guide
│
├── policies/
│   ├── doc-lifecycle-metadata-spec.md # Metadata schema (copy from KB)
│   └── doc-lifecycle-policy.md         # Policy and governance (copy from KB)
│
├── workflows/
│   └── doc-housekeeping-workflow.yaml # Automated housekeeping workflow (future)
│
├── scripts/
│   ├── validate_lifecycle_metadata.py # Validator for lifecycle metadata
│   └── housekeeping_scanner.py         # Scanner for expired documents (future)
│
├── templates/
│   ├── DOCUMENT_TEMPLATE.md           # Template with lifecycle metadata
│   └── LIFECYCLE_EXAMPLES.md          # Examples for each lifecycle type
│
└── integration/
    ├── kanban-integration.md          # How to integrate with Kanban
    └── workflow-mgt-integration.md    # How to integrate with Workflow Mgt
```

---

## 🔗 Integration Points

### With Kanban Package

**Integration:** Kanban Epics/Stories can include lifecycle metadata

**Example:**
```yaml
---
lifecycle: evergreen  # Kanban docs are typically evergreen
ttl_days: null
created_at: 2025-12-04T11:30:00Z
expires_at: null
housekeeping_policy: keep
---
# Epic 2: Workflow Management Framework
...
```

**Optional:** Kanban can work without lifecycle management (manual cleanup).

---

### With Workflow Management Package

**Integration:** RW and other workflows can set lifecycle metadata when creating docs

**Example:** When RW creates a renumbering plan:
```yaml
---
lifecycle: transient  # One-time operational doc
ttl_days: 14
created_at: 2025-12-04T11:30:00Z
expires_at: 2025-12-18T11:30:00Z
housekeeping_policy: delete
---
# E2:S04:T05 – Renumbering Plan
...
```

**Future:** Doc Housekeeping Workflow automates cleanup based on lifecycle metadata.

---

## 📚 Package Contents

### Core Documents

1. **`README.md`** — Package overview, modularity, quick reference
2. **`PACKAGE_OVERVIEW.md`** — Package structure, usage patterns, dependencies
3. **`IMPLEMENTATION_GUIDE.md`** — Step-by-step guide for adopting in other projects

### Policies

4. **`policies/doc-lifecycle-metadata-spec.md`** — Complete metadata schema
5. **`policies/doc-lifecycle-policy.md`** — Governance and enforcement rules

### Workflows (Future)

6. **`workflows/doc-housekeeping-workflow.yaml`** — Automated housekeeping workflow

### Scripts (Future)

7. **`scripts/validate_lifecycle_metadata.py`** — Validator for lifecycle metadata
8. **`scripts/housekeeping_scanner.py`** — Scanner for expired documents

### Templates

9. **`templates/DOCUMENT_TEMPLATE.md`** — Template with lifecycle metadata
10. **`templates/LIFECYCLE_EXAMPLES.md`** — Examples for each lifecycle type

### Integration Guides

11. **`integration/kanban-integration.md`** — How to integrate with Kanban
12. **`integration/workflow-mgt-integration.md`** — How to integrate with Workflow Mgt

---

## 🎯 Adoption Pattern

### Copy Pattern (Same as Other Packages)

**⚠️ CRITICAL: Copy, Don't Reference**

Projects must **copy** this package into their repository, not link to it.

**Why copy?**
- Projects need to customize lifecycle defaults and housekeeping policies
- Projects evolve independently and may need project-specific adaptations
- Copying ensures projects have full control over their lifecycle management
- Prevents breaking changes in `ai-dev-kit` from affecting consuming projects

**What to copy:**
1. All files in `packages/frameworks/doc-lifecycle/`
2. Maintain directory structure
3. Customize lifecycle defaults if needed
4. Update examples with project-specific paths

**Customization boundaries:**
- ✅ **CAN customize:** Lifecycle defaults, TTL values, housekeeping policies, KB paths
- ❌ **MUST keep:** Metadata schema (5 required fields), lifecycle enum values, protection rules

---

## 🚀 Next Steps

1. **Create package structure** — Set up `packages/frameworks/doc-lifecycle/` directory
2. **Copy core documents** — Copy spec and policy from KB to package
3. **Create README** — Package overview following pattern from other packages
4. **Create templates** — Document template with lifecycle metadata
5. **Create integration guides** — How to integrate with Kanban and Workflow Mgt
6. **Future:** Implement Doc Housekeeping Workflow (YAML + agent execution guide)
7. **Future:** Implement validation scripts

---

## 📊 Comparison with Other Packages

| Package | Type | Dependencies | Integration Points |
|---------|------|--------------|-------------------|
| **Kanban** | Policy + Templates | Git, Markdown | Versioning, Workflow Mgt |
| **Numbering & Versioning** | Policy | None | Kanban, Workflow Mgt |
| **Workflow Management** | Policy + Scripts + Workflows | Versioning (soft) | Kanban, Versioning |
| **Doc Lifecycle** | Policy + Scripts + Workflows (future) | None | Kanban, Workflow Mgt |

**Doc Lifecycle** follows the same modular pattern:
- ✅ Standalone capability
- ✅ Copy pattern (not reference)
- ✅ Integration points with other packages
- ✅ Clear customization boundaries

---

**Last Updated:** 2025-12-04  
**Status:** Proposal — Awaiting approval and implementation

