## Vibe Dev Kit

[![Version](https://img.shields.io/badge/version-0.2.4.5%2B3-blue)](./CHANGELOG.md)
[![Changelog](https://img.shields.io/badge/changelog-Keep%20a%20Changelog-brightgreen)](./CHANGELOG.md)
[![Repo](https://img.shields.io/github/stars/earlution/vibe-dev-kit?style=social)](https://github.com/earlution/vibe-dev-kit)

**Repository for "Vibe Coding [for Dummies]" Book Project**

> An opinionated dev kit of **portable frameworks, workflows, and policies** used to build and run real projects with AI-first workflows.

---

## 📚 About The Project

This repository supports the **"Vibe Coding [for Dummies]"** book project (working title). It serves as a central collection of:

- **Frameworks** – Complete, reusable development frameworks
- **Tools** – Development tools and utilities
- **SOPs** – Standard Operating Procedures and workflows
- **Templates** – Ready-to-use templates for common tasks
- **Examples** – Reference implementations and examples

All packages are designed to be:

- ✅ **Portable** – Copy a package into any project and adapt locally  
- ✅ **Well-Documented** – Implementation guides and policy docs  
- ✅ **Versioned** – Using `RC.EPIC.STORY.TASK+BUILD` for forensic traceability  
- ✅ **Battle-Tested** – Used in real projects (e.g. fynd.deals)

---

## 🧱 Built With

The dev kit itself is deliberately **tool-agnostic** in runtime dependencies, but assumes:

- **Git & GitHub** for source control and collaboration
- **Cursor / AI coding assistants** for workflow execution
- **Markdown-first documentation** for policies, SOPs, and KB

For README and changelog conventions, we take inspiration from:

- **Best-README-Template** – [`https://github.com/othneildrew/Best-README-Template`](https://github.com/othneildrew/Best-README-Template)  
- **Keep a Changelog** – [`https://github.com/olivierlacan/keep-a-changelog`](https://github.com/olivierlacan/keep-a-changelog)  
- **Shields.io** badges – [`https://shields.io/`](https://shields.io/)

---

## 📦 Package Categories

### Frameworks (`packages/frameworks/`)

Complete, reusable development frameworks with full documentation and implementation guides.

- **Workflow Management** – Release Workflow (RW) trigger and agent-driven workflow execution (v2.0.0)
- **Numbering & Versioning** – Semantic versioning and numbering strategies (v2.0.0)
- **Kanban** – Kanban governance, templates, and integration with versioning & workflows

Planned frameworks:

- Architecture frameworks  
- Testing frameworks  
- Documentation frameworks  

### Tools (`packages/tools/`)

Development tools and utilities for common tasks.  
Examples (planned): code generators, validation tools, automation scripts.

### SOPs (`packages/sops/`)

Standard Operating Procedures and workflows for development practices:  
code review, deployment, incident response, and more (to be populated).

---

## 🚀 Getting Started

This is a **dev kit**, not a monolith. You typically **copy a package** into your own repo and customise it.

### Prerequisites

- Git  
- A GitHub account (recommended)  
- A modern editor (e.g. Cursor) with AI assistant support  

### Installation (Using the Dev Kit in Your Project)

1. **Clone this repo**:

   ```bash
   git clone https://github.com/earlution/vibe-dev-kit.git
   cd vibe-dev-kit
   ```

2. **Pick a framework** you want to adopt:

   ```bash
   # List all frameworks
   ls packages/frameworks/
   ```

3. **Copy the package** into your own project:

   ```bash
   # Example: just the workflow management framework
   cp -r packages/frameworks/workflow\ mgt/ /path/to/your/project/
   ```

4. **Follow that package’s `README.md` and implementation guide** inside your project.

---

## 📘 Usage

### Use a Single Package (Most Common)

- **Just the Release Workflow (RW) framework:**

  ```bash
  cp -r packages/frameworks/workflow\ mgt/ /path/to/your/project/
  ```

- **Just the Numbering & Versioning policies:**

  ```bash
  cp -r "packages/frameworks/numbering & versioning" /path/to/your/project/numbering-and-versioning
  ```

### Use Multiple Packages Together

For full power, combine frameworks:

```bash
cp -r packages/frameworks/workflow\ mgt/ /path/to/your/project/
cp -r "packages/frameworks/numbering & versioning" /path/to/your/project/numbering-and-versioning
cp -r packages/frameworks/kanban/ /path/to/your/project/
```

Each package documents its own **modularity and dependencies** in its README / overview, so you can see at a glance:

- Whether it is **standalone**
- Any **hard dependencies** (usually none)
- Any **optional companion packages** that work well with it

---

## 🧩 Modular Use

This repo is designed to be **modular**:

- Use **a single package** (e.g. just RW, or just Numbering & Versioning)  
- Use **multiple packages together** for tight integration  
- Treat each package as a **drop‑in module** you adapt to your own project structure

See the **Package Categories** and each package’s own docs for details.

---

## 📁 Repository Structure

```text
vibe-dev-kit/
├── README.md
├── CHANGELOG.md
├── packages/
│   ├── frameworks/
│   │   ├── workflow mgt/              # Release Workflow framework
│   │   ├── numbering & versioning/    # Versioning strategy framework
│   │   └── kanban/                    # Kanban governance & integration
│   ├── tools/                         # Development tools and utilities
│   └── sops/                          # Standard Operating Procedures
├── KB/                                # Knowledge base (epics, stories, policies)
├── docs/                              # Book-related docs and style guides
└── src/                               # Dev-kit version file, examples (when present)
```

---

## 🧱 Current Frameworks

### Workflow Management (`packages/frameworks/workflow mgt/`)

Complete package for implementing the Release Workflow (RW) trigger and agent-driven workflow execution pattern.

- 11-step Release Workflow with intelligent agent execution (including Branch Safety Check)
- “ALL sections” requirement for documentation consistency
- Atomicity and blocked protocol (accessibility-critical)
- Epic/Story/Task-aware branch and version enforcement
- Validation scripts for branch context and changelog format

**Package Version:** 2.0.0  
**Last Updated:** 2025-12-02  
**Source Project:** fynd.deals (Epic 15, Story 1)

**Latest Dev-Kit Release:**  
**v0.1.1.1+2** – 📚 Documentation: Restructured CHANGELOG and README to follow industry-standard templates. See `CHANGELOG.md` for details.

---

### Numbering & Versioning (`packages/frameworks/numbering & versioning/`)

Complete policy package for implementing numbering and versioning strategies.

- Semantic versioning schema: `RC.EPIC.STORY.TASK+BUILD`
- Epic renumbering strategy (legacy vs new format separation)
- Forensic traceability
- Kanban integration
- Templates for Epic and Story documents

**Package Version:** 2.0.0  
**Last Updated:** 2025-12-02  
**Source Project:** fynd.deals (Epic 15, Story 1)

---

### Kanban (`packages/frameworks/kanban/`)

Kanban governance and templates, refactored to be project-agnostic.

- Kanban governance policy
- Epic and Story templates
- Integration guides for:
  - Numbering & Versioning
  - Workflow Management

The dev-kit’s **local Kanban implementation** lives under:

- `KB/PM_and_Portfolio/kanban/` (board + stories)
- `KB/PM_and_Portfolio/rituals/policy/kanban-governance-policy.md`

---

## 🗺️ Roadmap

This roadmap is intentionally high-level and mirrors the internal Epics:

- **Epic 1 – Vibe Dev Kit Core**
  - Finalise `dev-kit-versioning-policy.md` and keep it in sync with `version.py` and RW docs.
  - Harden KB structure for architecture, PM & portfolio, and governance.

- **Epic 2 – Workflow Management Framework**
  - Complete RW agent execution docs as portable templates.
  - Add non-release workflows (e.g. refactors, migrations) using the same agent pattern.

- **Epic 3 – Numbering & Versioning Framework**
  - Align dev-kit usage examples with the generic versioning policy & strategy.
  - Publish a “versioning cookbook” for common scenarios (new story, new task, hotfix, rollback).

- **Epic 4 – Kanban Framework**
  - Evolve dev-kit Kanban (Epics/Stories/Tasks) with full E/S/T numbering.
  - Tighten FR/BR → Task → Story → Epic flow and deepen integration with RW + versioning.

For finer-grained work, see:

- `KB/PM_and_Portfolio/kanban/epics/`  
- `KB/PM_and_Portfolio/kanban/` (board and stories)

---

## 🔄 Release & Changelog

- Project versions follow **`RC.EPIC.STORY.TASK+BUILD`**  
- Changelog format follows **Keep a Changelog** principles:
  - See `CHANGELOG.md` (top-level summary, with `Unreleased` and version sections)
  - Detailed per-version notes live in `KB/Changelog_and_Release_Notes/Changelog_Archive/`

The Release Workflow is documented in:

- `packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md`

---

## 🤝 Contributing

To contribute new packages or improvements:

1. **Create a new package** in the appropriate category (`frameworks/`, `tools/`, or `sops/`)
2. **Follow package structure** – include `README`, `PACKAGE_OVERVIEW`, `IMPLEMENTATION_GUIDE`, templates/examples
3. **Document thoroughly** – clear usage instructions and customization notes
4. **Test in real projects** – validate packages work in practice
5. **Open a Pull Request** – include a clear description and updated version numbers

For inspiration on structure and sectioning, see:

- Best-README-Template – [`https://github.com/othneildrew/Best-README-Template`](https://github.com/othneildrew/Best-README-Template)

---

## 📝 License

Licensing may vary by package. See:

- Individual package `README` / `PACKAGE_OVERVIEW` files for license notes.

---

## 🔗 Related Projects

Packages here are developed and refined in real projects, for example:

- **fynd.deals** – Epic 15, Story 1 (Documentation and dev-kit extraction)

---

## 📚 Book Project

This repository supports the **"Vibe Coding [for Dummies]"** book project. Packages here represent:

- **Proven practices** – Tested in real-world projects  
- **Complete solutions** – Ready to use, not just concepts  
- **Learning resources** – Examples and guides for readers  
- **Reference implementations** – Code and configurations readers can study

---

**Repository:** `https://github.com/earlution/vibe-dev-kit`  
**Book Project:** *"Vibe Coding [for Dummies]"* (working title)  
**Current Repo Version:** `v0.2.4.5+3` (2025-12-04)
