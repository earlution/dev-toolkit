# Document Lifecycle Metadata Specification

**Version:** 1.0.0  
**Last Updated:** 2025-12-04  
**Status:** Draft  
**Related:** [Document Lifecycle Policy](./doc-lifecycle-policy.md) | [KB Structure Overview](./kb-structure-overview.md)

---

## 📋 Overview

This specification defines the **metadata fields** that control document lifecycle management in the Knowledge Base (KB). Documents can be marked as **evergreen** (persistent), **timeboxed** (archive after period), or **transient** (delete after period), enabling automated housekeeping to prevent documentation bloat.

**Key Concepts:**
- **Lifecycle classification:** Documents are classified by their intended persistence
- **TTL-based expiration:** Time-to-live (TTL) determines when documents become eligible for housekeeping
- **Reference-aware cleanup:** Documents referenced from evergreen sources are protected from deletion
- **Agent-driven management:** AI agents create and maintain lifecycle metadata automatically

---

## 🎯 Goals

1. **Prevent documentation bloat** by identifying and managing temporary documents
2. **Preserve evergreen content** while allowing cleanup of obsolete planning/implementation docs
3. **Enable automated housekeeping** through clear, machine-readable metadata
4. **Maintain audit trails** by archiving (not deleting) historically significant temporary docs
5. **Support agent-driven workflows** with explicit lifecycle rules and defaults

---

## 📐 Metadata Schema

### Required Fields

All KB documents **MUST** include the following front-matter fields:

```yaml
---
lifecycle: evergreen | timeboxed | transient
ttl_days: <integer> | null
created_at: <ISO 8601 datetime>
expires_at: <ISO 8601 datetime> | null
housekeeping_policy: keep | archive | delete
---
```

### Field Definitions

#### `lifecycle` (required, enum)

**Purpose:** Classifies the document's intended persistence.

**Values:**
- **`evergreen`** – Permanent, canonical documentation (standards, ADRs, core how-tos, Kanban Epics/Stories)
- **`timeboxed`** – Temporarily useful, archive after period (design spikes, exploratory analysis, refactoring plans)
- **`transient`** – Operational scratch, delete after period (implementation plans, renumbering sequences, one-time scripts)

**Default:** `evergreen` (if omitted, assume permanent)

**Agent Rule:** Agents **MUST** set `lifecycle` when creating KB documents. If uncertain, default to `evergreen` and let user override.

---

#### `ttl_days` (required, integer | null)

**Purpose:** Time-to-live in days from `created_at` until `expires_at`.

**Values:**
- **Integer** (1-3650) – Number of days until expiration (only meaningful for `timeboxed` or `transient`)
- **`null`** – No expiration (required for `lifecycle: evergreen`)

**Default by Lifecycle:**
- `evergreen` → `null`
- `timeboxed` → `90` (3 months)
- `transient` → `14` (2 weeks) or `30` (1 month) depending on doc type

**Agent Rule:** Agents **MUST** set `ttl_days` based on lifecycle. For `evergreen`, set to `null`. For `timeboxed`/`transient`, use defaults unless explicitly overridden.

---

#### `created_at` (required, ISO 8601 datetime)

**Purpose:** Timestamp when document was created.

**Format:** `YYYY-MM-DDTHH:MM:SSZ` (e.g., `2025-12-04T11:30:00Z`)

**Agent Rule:** Agents **MUST** set `created_at` to current UTC time when creating documents.

---

#### `expires_at` (required, ISO 8601 datetime | null)

**Purpose:** Calculated expiration timestamp (`created_at + ttl_days`).

**Format:** `YYYY-MM-DDTHH:MM:SSZ` (e.g., `2025-12-18T11:30:00Z`) or `null`

**Calculation:**
- If `ttl_days` is `null` → `expires_at = null`
- If `ttl_days` is integer → `expires_at = created_at + ttl_days days`

**Agent Rule:** Agents **MUST** calculate `expires_at` from `created_at + ttl_days` when creating documents.

---

#### `housekeeping_policy` (required, enum)

**Purpose:** Determines action when document expires.

**Values:**
- **`keep`** – Never delete or archive (required for `lifecycle: evergreen`)
- **`archive`** – Move to `KB/Archive/` when expired (typical for `timeboxed`)
- **`delete`** – Remove from KB when expired (typical for `transient`)

**Default by Lifecycle:**
- `evergreen` → `keep`
- `timeboxed` → `archive`
- `transient` → `delete`

**Agent Rule:** Agents **MUST** set `housekeeping_policy` based on lifecycle defaults unless explicitly overridden.

---

## 📊 Document Type → Lifecycle Mapping

### Default Classifications

| Document Type | Lifecycle | TTL (days) | Housekeeping Policy | Notes |
|---------------|-----------|------------|---------------------|-------|
| **Standards & ADRs** | `evergreen` | `null` | `keep` | Canonical technical standards |
| **Kanban Epics/Stories** | `evergreen` | `null` | `keep` | Project management artifacts |
| **Core How-Tos** | `evergreen` | `null` | `keep` | User-facing guides |
| **Design Spikes** | `timeboxed` | `90` | `archive` | Exploratory analysis |
| **Refactoring Plans** | `timeboxed` | `90` | `archive` | Implementation planning |
| **Renumbering Plans** | `transient` | `14` | `delete` | One-time operational docs |
| **Implementation Sequences** | `transient` | `30` | `delete` | Step-by-step execution plans |
| **Analysis Documents** | `timeboxed` | `90` | `archive` | Research, impact analysis |

### Agent Decision Tree

When creating a KB document, agents should:

1. **Identify document type** from context (task description, file path, content)
2. **Map to lifecycle** using table above
3. **Apply defaults** for `ttl_days` and `housekeeping_policy`
4. **Calculate** `expires_at` from `created_at + ttl_days`
5. **Set all fields** in front-matter

**Example:**
```yaml
---
lifecycle: transient
ttl_days: 14
created_at: 2025-12-04T11:30:00Z
expires_at: 2025-12-18T11:30:00Z
housekeeping_policy: delete
---
```

---

## 🔄 Lifecycle Transitions

### Promotion (Upgrade Lifecycle)

Documents can be **promoted** to longer lifecycle:

- **`transient → timeboxed`** – If document turns out more useful than expected
- **`timeboxed → evergreen`** – If document becomes canonical reference

**Process:**
1. Update `lifecycle` field
2. Update `ttl_days` (set to `null` if promoting to `evergreen`)
3. Update `expires_at` (recalculate or set to `null`)
4. Update `housekeeping_policy` (if needed)
5. **Log promotion** in changelog or Story task notes

**Agent Rule:** Agents **MUST NOT** silently promote documents. Promotion should be explicit and logged.

---

### Demotion (Downgrade Lifecycle)

Documents can be **demoted** to shorter lifecycle (rare):

- **`evergreen → timeboxed`** – If document becomes obsolete but historically valuable
- **`timeboxed → transient`** – If document is less useful than expected

**Process:**
1. Update `lifecycle` field
2. Set appropriate `ttl_days`
3. Recalculate `expires_at`
4. Update `housekeeping_policy`
5. **Log demotion** with reason

**Agent Rule:** Demotion should be **explicit and rare**. Consider archiving instead of demoting evergreen docs.

---

## 🛡️ Protection Rules

### Reference-Based Protection

Documents **MUST NOT** be deleted if they are:

1. **Referenced from evergreen docs** – Links from `lifecycle: evergreen` documents
2. **Referenced in changelogs** – Mentioned in released changelog entries
3. **Referenced in git history** – Committed in git (always preserved via git)

**Housekeeping Workflow Rule:** Before deleting, scan for references. If found, **auto-upgrade** to `archive` instead of `delete`.

---

### Immutable Evidence Protection

Documents that serve as **audit trail evidence** **MUST NOT** be deleted:

- Documents referenced from released changelogs
- Documents that document completed work (even if transient)
- Documents that contain unique historical context

**Action:** Set `housekeeping_policy: archive` even for `transient` docs if they serve as evidence.

---

## 📝 Examples

### Example 1: Evergreen Standard

```yaml
---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-04T11:30:00Z
expires_at: null
housekeeping_policy: keep
---
# Document Lifecycle Metadata Specification

This document defines the metadata fields...
```

---

### Example 2: Timeboxed Analysis

```yaml
---
lifecycle: timeboxed
ttl_days: 90
created_at: 2025-12-04T11:30:00Z
expires_at: 2025-03-04T11:30:00Z
housekeeping_policy: archive
---
# T01 – RW Adoption Friction Analysis

This analysis documents current friction points...
```

---

### Example 3: Transient Renumbering Plan

```yaml
---
lifecycle: transient
ttl_days: 14
created_at: 2025-12-04T11:30:00Z
expires_at: 2025-12-18T11:30:00Z
housekeeping_policy: delete
---
# E2:S04:T05 – Renumbering Plan

## Steps to Renumber Story IDs

1. Update Epic-2.md...
```

---

## 🔗 Related Documents

- **Policy:** [`doc-lifecycle-policy.md`](./doc-lifecycle-policy.md) – Governance and enforcement
- **Workflow:** `packages/frameworks/workflow mgt/workflows/doc-housekeeping-workflow.yaml` – Automated housekeeping
- **KB Structure:** [`kb-structure-overview.md`](./kb-structure-overview.md) – KB organization

---

## 📚 References

- **ISO 8601:** Date/time format standard
- **TTL Pattern:** Network protocol time-to-live concept
- **Document Lifecycle:** Information lifecycle management principles

---

**Last Updated:** 2025-12-04  
**Status:** Draft – Awaiting review and adoption

