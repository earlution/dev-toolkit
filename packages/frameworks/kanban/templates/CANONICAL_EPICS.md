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

> **Note:** For the complete canonical structure including all epics (1-23+), stories, and tasks, see [`COMPREHENSIVE_CANONICAL_EST_STRUCTURE.md`](COMPREHENSIVE_CANONICAL_EST_STRUCTURE.md). This document focuses on the core framework epics (1-7).

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
This epic encompasses Feature Request (FR) implementation and management, including FR intake processes, FR processing workflows, FR implementation patterns, and FR-related tooling. This epic provides the organizational structure for all feature development work that originates from Feature Requests.

**Key Characteristics:**
- FR intake processes (converting FRs to Kanban tasks)
- FR processing workflows (prioritization, analysis, design)
- FR implementation patterns (development, testing, documentation)
- FR tooling (automation, tracking, reporting)

**Typical Stories:**
- Story 1: FR Intake and Processing Workflow
- Story 2: FR Prioritization and Planning
- Story 3: FR Implementation Patterns and Best Practices
- Story 4: FR Tracking and Reporting
- Story 5: FR Automation and Tooling

**Integration Points:**
- **Epic 4 (Kanban Framework):** Uses Kanban intake processes to convert FRs to tasks
- **Epic 2 (Workflow Management):** May use workflows for FR processing automation
- **Epic 3 (Versioning):** Tracks FR implementation with version markers

---

### Epic 6: BR Implementation

**Purpose:** Bug Report implementation and management.  
**Scope:** Bug Report intake, processing, bug fix workflows, and BR-related tooling.  
**Status:** Canonical (part of framework structure)

**Description:**
This epic covers Bug Report (BR) implementation and management, including BR intake processes, BR processing workflows, bug fix patterns, and BR-related tooling. This epic provides the organizational structure for all bug fix work that originates from Bug Reports.

**Key Characteristics:**
- BR intake processes (converting BRs to Kanban tasks)
- BR processing workflows (triage, prioritization, assignment)
- Bug fix patterns (reproduction, root cause analysis, testing)
- BR tooling (automation, tracking, reporting)

**Typical Stories:**
- Story 1: BR Intake and Triage Workflow
- Story 2: BR Prioritization and Assignment
- Story 3: Bug Fix Patterns and Best Practices
- Story 4: BR Tracking and Reporting
- Story 5: BR Automation and Tooling

**Integration Points:**
- **Epic 4 (Kanban Framework):** Uses Kanban intake processes to convert BRs to tasks
- **Epic 2 (Workflow Management):** May use workflows for BR processing automation
- **Epic 3 (Versioning):** Tracks bug fixes with version markers

---

### Epic 7: UXR (User Experience Research)

**Purpose:** User experience research, user feedback, and user-centered design.  
**Scope:** User research, usability testing, user feedback collection, persona development, user journey mapping, and UX insights.  
**Status:** Canonical (part of framework structure)

**Description:**
This epic encompasses user experience research activities, including user research, usability testing, user feedback collection, persona development, user journey mapping, and UX insights. This epic provides the organizational structure for understanding users and ensuring products meet user needs effectively.

**Key Characteristics:**
- User research and interviews
- Usability testing and user testing
- User feedback collection and analysis
- Persona development and user modeling
- User journey mapping
- UX insights and recommendations

**Typical Stories:**
- Story 1: User Research and Discovery
- Story 2: Usability Testing and Validation
- Story 3: User Feedback Collection and Analysis
- Story 4: User Journey Mapping and Experience Design
- Story 5: UX Insights and Recommendations

**Integration Points:**
- **Epic 4 (Kanban Framework):** Uses Kanban for tracking UXR tasks and research activities
- **Epic 5 (FR Implementation):** UXR insights inform Feature Requests
- **Epic 6 (BR Implementation):** UXR findings may identify usability issues tracked as Bug Reports
- **Epic 2 (Workflow Management):** May use workflows for UXR process automation

---

## Epic Ordering Rationale

The canonical epics are ordered logically:

1. **Epic 1: AI Dev Kit Core** - Foundational epic that establishes the base
2. **Epic 2: Workflow Management Framework** - Operational framework for workflows
3. **Epic 3: Numbering & Versioning Framework** - Operational framework for versioning
4. **Epic 4: Kanban Framework** - Operational framework for Kanban
5. **Epic 5: FR Implementation** - Implementation epic that supports Kanban (FRs come first)
6. **Epic 6: BR Implementation** - Implementation epic that supports Kanban (BRs follow FRs)
7. **Epic 7: UXR (User Experience Research)** - User research epic that bridges framework and project work

**Ordering Principles:**
- Foundational epics come first (Epic 1)
- Operational frameworks follow (Epics 2-4)
- Implementation epics that support frameworks come next (Epics 5-6)
- User research epic (Epic 7) bridges framework and project work, making it canonical
- FR Implementation (Epic 5) comes before BR Implementation (Epic 6) because Feature Requests typically precede Bug Reports in the intake flow
- UXR (Epic 7) bridges framework infrastructure and project-specific user research needs

---

## How to Use Canonical Epics

### Adoption Steps

1. **Adopt Structure:** Use these canonical epics as the foundation for your project
   - Start with Epics 1-6 as your base organizational structure
   - Customize names and descriptions to match your project context
   - Example: "AI Dev Kit Core" → "MyProject Core" or "Product Foundation"

2. **Customize:** Adapt epic names and descriptions to your project's specific context
   - Keep the core purpose and scope aligned with canonical definitions
   - Adjust terminology to match your domain
   - Maintain the logical ordering (foundational → operational → implementation)

3. **Extend:** Add additional epics as needed for your project's specific domains
   - Start numbering from Epic 8 (canonical epics are 1-7)
   - Example: Epic 8 (Mobile App), Epic 9 (API Integration), Epic 10 (Analytics)

4. **Maintain Order:** When adding new epics, continue numbering from Epic 7 (or your highest epic number). Note: Codebase Maintenance is now Epic 8 in the comprehensive structure.
   - Don't reuse canonical epic numbers (1-7) for project-specific epics
   - Keep canonical epics as the foundation

### Customization Examples

**Example 1: Software Product**
- Epic 1: Product Core → "Application Core"
- Epic 2: Workflow Management → "Process Automation"
- Epic 3: Numbering & Versioning → "Release Management"
- Epic 4: Kanban Framework → "Project Management"
- Epic 5: FR Implementation → "Feature Development"
- Epic 6: BR Implementation → "Bug Fixes"
- Epic 7: UXR (User Experience Research) → "User Research & UX"
- Epic 8: Mobile App (project-specific)
- Epic 9: API Integration (project-specific)

**Example 2: Framework Package**
- Epic 1: Framework Core → "Framework Foundation"
- Epic 2: Workflow Management → "Workflow Engine"
- Epic 3: Numbering & Versioning → "Versioning System"
- Epic 4: Kanban Framework → "Task Management"
- Epic 5: FR Implementation → "Feature Requests"
- Epic 6: BR Implementation → "Issue Resolution"
- Epic 7: UXR (User Experience Research) → "User Research & UX"
- Epic 8: Documentation (project-specific)
- Epic 9: Examples & Tutorials (project-specific)

---

## Adding New Canonical Epics

When an epic pattern proves reusable across multiple projects, it should be added to this document:

1. **Identify Pattern:** Epic appears in multiple projects or represents a common organizational need
   - Pattern must appear in at least 3 different projects
   - Pattern must represent a fundamental organizational structure
   - Pattern must be reusable across different domains

2. **Document Pattern:** Create entry in this document with:
   - Epic number (following canonical order, after Epic 7). See comprehensive structure for Epics 8+.
   - Purpose (clear, concise statement)
   - Scope (what's included/excluded)
   - Key characteristics (distinguishing features)
   - Typical stories (common story patterns)
   - Integration points (how it relates to other canonical epics)
   - Ordering rationale (why it comes in this position)

3. **Update Framework:** Add to Kanban framework documentation
   - Update `CANONICAL_EPICS.md` (this document)
   - Update `README.md` with new epic count
   - Update intake guides to reference new epic
   - Update examples to show new epic usage

4. **Update References:** Update all references to canonical epics in intake guides and other documentation
   - `FR_BR_INTAKE_GUIDE.md`
   - `FR_BR_INTAKE_AGENT_GUIDE.md`
   - `FR_BR_INTAKE_USER_GUIDE.md`
   - `FR_BR_INTAKE_QUICK_REFERENCE.md`
   - Any other framework documentation

### Example: Adding Epic 8 (Documentation Management)

If documentation management becomes a common pattern:

1. **Identify:** Documentation management appears in 3+ projects
2. **Document:**
   ```markdown
   ### Epic 8: Documentation Management
   
   **Purpose:** Documentation creation, maintenance, and quality assurance.
   **Scope:** Documentation workflows, quality standards, automation, and documentation tooling.
   **Status:** Canonical (part of framework structure)
   
   **Description:**
   This epic encompasses documentation management, including documentation workflows, quality standards, automation, and documentation-related tooling.
   
   **Key Characteristics:**
   - Documentation workflows
   - Quality standards and review processes
   - Documentation automation
   - Documentation tooling
   
   **Typical Stories:**
   - Story 1: Documentation Standards and Guidelines
   - Story 2: Documentation Quality Assurance
   - Story 3: Documentation Automation
   - Story 4: Documentation Maintenance Workflows
   
   **Integration Points:**
   - Epic 4 (Kanban Framework): Uses Kanban for documentation task tracking
   - Epic 2 (Workflow Management): May use workflows for documentation automation
   ```
3. **Update Framework:** Add to all relevant documentation
4. **Update References:** Update intake guides and examples

---

**Last Updated:** 2025-12-09  
**Version:** 1.1  
**Maintained By:** Kanban Framework Team

