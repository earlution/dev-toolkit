---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-08T23:55:00Z
expires_at: null
housekeeping_policy: keep
---

# Canonical Epics for Kanban Framework

**Purpose:** This document lists the canonical set of epics that are part of the Kanban framework package. These epics represent the standard organizational structure for projects using the Kanban framework.

**Usage:** When adopting the Kanban framework, these canonical epics provide the foundation for organizing work. Projects can add additional epics as needed, but these represent the core framework structure.

---

## Canonical Epics

### Epic 1: AI Dev Kit Core

**Purpose:** Core foundational work for the AI Dev Kit project.  
**Scope:** Fundamental infrastructure, core functionality, and foundational frameworks.  
**Status:** Canonical (part of framework structure)

**Description:**
This epic encompasses the core foundational work for the AI Dev Kit project, including fundamental infrastructure, core functionality, and foundational frameworks that other epics build upon.

**Key Characteristics:**
- Foundational infrastructure
- Core functionality
- Base frameworks
- Project fundamentals

---

### Epic 2: Workflow Management Framework

**Purpose:** Workflow management and automation framework.  
**Scope:** Workflow definitions, execution patterns, automation, and workflow-related tooling.  
**Status:** Canonical (part of framework structure)

**Description:**
This epic covers workflow management and automation, including workflow definitions, execution patterns, agent-driven workflows, and workflow-related tooling and infrastructure.

**Key Characteristics:**
- Workflow definitions
- Execution patterns
- Automation tooling
- Agent-driven workflows

---

### Epic 3: Numbering & Versioning Framework

**Purpose:** Versioning and numbering schema framework.  
**Scope:** Versioning policies, numbering schemas, version management, and version-related tooling.  
**Status:** Canonical (part of framework structure)

**Description:**
This epic encompasses versioning and numbering schema frameworks, including versioning policies, numbering schemas (e.g., RC.EPIC.STORY.TASK+BUILD), version management, and version-related tooling.

**Key Characteristics:**
- Versioning policies
- Numbering schemas
- Version management
- Version tooling

---

### Epic 4: Kanban Framework

**Purpose:** Kanban system implementation and governance.  
**Scope:** Kanban policies, templates, intake processes, and Kanban-related tooling.  
**Status:** Canonical (part of framework structure)

**Description:**
This epic covers the Kanban system implementation, including Kanban governance policies, templates, FR/BR intake processes, and Kanban-related tooling and infrastructure.

**Key Characteristics:**
- Kanban governance
- Templates and patterns
- Intake processes
- Kanban tooling

---

### Epic 5: FR Implementation

**Purpose:** Feature Request implementation and management.  
**Scope:** Feature Request intake, processing, implementation workflows, and FR-related tooling.  
**Status:** Canonical (part of framework structure)

**Description:**
This epic encompasses Feature Request (FR) implementation and management, including FR intake processes, FR processing workflows, FR implementation patterns, and FR-related tooling.

**Key Characteristics:**
- FR intake processes
- FR processing workflows
- FR implementation patterns
- FR tooling

---

### Epic 6: BR Implementation

**Purpose:** Bug Report implementation and management.  
**Scope:** Bug Report intake, processing, bug fix workflows, and BR-related tooling.  
**Status:** Canonical (part of framework structure)

**Description:**
This epic covers Bug Report (BR) implementation and management, including BR intake processes, BR processing workflows, bug fix patterns, and BR-related tooling.

**Key Characteristics:**
- BR intake processes
- BR processing workflows
- Bug fix patterns
- BR tooling

---

## Epic Ordering Rationale

The canonical epics are ordered logically:

1. **Epic 1: AI Dev Kit Core** - Foundational epic that establishes the base
2. **Epic 2: Workflow Management Framework** - Operational framework for workflows
3. **Epic 3: Numbering & Versioning Framework** - Operational framework for versioning
4. **Epic 4: Kanban Framework** - Operational framework for Kanban
5. **Epic 5: FR Implementation** - Implementation epic that supports Kanban (FRs come first)
6. **Epic 6: BR Implementation** - Implementation epic that supports Kanban (BRs follow FRs)

**Ordering Principles:**
- Foundational epics come first (Epic 1)
- Operational frameworks follow (Epics 2-4)
- Implementation epics that support frameworks come last (Epics 5-6)
- FR Implementation (Epic 5) comes before BR Implementation (Epic 6) because Feature Requests typically precede Bug Reports in the intake flow

---

## How to Use Canonical Epics

1. **Adopt Structure:** Use these canonical epics as the foundation for your project
2. **Customize:** Adapt epic names and descriptions to your project's specific context
3. **Extend:** Add additional epics as needed for your project's specific domains
4. **Maintain Order:** When adding new epics, continue numbering from Epic 6 (or your highest epic number)

---

## Adding New Canonical Epics

When an epic pattern proves reusable across multiple projects, it should be added to this document:

1. **Identify Pattern:** Epic appears in multiple projects or represents a common organizational need
2. **Document Pattern:** Create entry in this document with:
   - Epic number (following canonical order)
   - Purpose
   - Scope
   - Key characteristics
   - Ordering rationale
3. **Update Framework:** Add to Kanban framework documentation
4. **Update References:** Update all references to canonical epics in intake guides and other documentation

---

**Last Updated:** 2025-12-08  
**Version:** 1.0  
**Maintained By:** Kanban Framework Team

